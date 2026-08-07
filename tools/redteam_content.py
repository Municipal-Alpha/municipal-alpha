#!/usr/bin/env python3
"""
Red team scanner for published content.

Scans markdown files for competitive intelligence leaks before publishing.
Enforces CONTENT-RULES.md programmatically. Run manually or as a CI gate.

Usage:
    python tools/redteam_content.py                          # scan all content
    python tools/redteam_content.py content/pages/town-*.md  # specific files
    python tools/redteam_content.py --strict                 # fail on warnings too
    python tools/redteam_content.py --fix                    # auto-fix simple violations

Exit codes:
    0 = clean
    1 = violations found
"""

import argparse
import re
import sys
from pathlib import Path


# --- Violation patterns ---

# Ticker symbols: (WM), (STN), (ticker: WM), etc.
TICKER_PATTERNS = [
    (r'\(ticker:\s*[A-Z]{1,5}\)', 'Ticker symbol in parenthetical'),
    (r'\([A-Z]{2,5}\)', 'Possible ticker symbol in parenthetical'),
    (r'ticker\s+[A-Z]{2,5}\b', 'Ticker symbol reference'),
    (r'\bNYSE:\s*[A-Z]+', 'NYSE ticker reference'),
    (r'\bNASDAQ:\s*[A-Z]+', 'NASDAQ ticker reference'),
]

# Generic government/document acronyms that are NOT stock tickers. The
# parenthetical-ticker heuristic (r'\([A-Z]{2,5}\)') is skipped for these only.
# Keep this set TIGHT and unambiguous — real or ticker-shaped acronyms
# (WM, STN, XYL, TTEK, CG=Carlyle, CNM, VEOEY, ...) must still flag, since the
# whole point of this gate is to stop leaking that we track public companies.
NONTICKER_ACRONYMS = {'MRRA', 'BRAC', 'RFP', 'RFQ', 'CSV', 'PDF'}
GENERIC_PARENS_PATTERN = r'\([A-Z]{2,5}\)'

# Ticker-shaped acronyms that MUST keep flagging even when spelled out, because
# the whole point of this gate is to hide that we track public companies. An
# expansion like "Waste Management (WM)" is exactly the leak, not an exemption.
TICKER_DENY = {'WM', 'STN', 'XYL', 'TTEK', 'CG', 'CNM', 'VEOEY', 'RSG', 'CWST',
               'AWK', 'WTRG', 'ECOL', 'CLH', 'NVRI', 'AMT', 'CCI', 'SBAC'}

_STOPWORDS = {'of', 'and', 'the', 'for', 'in', 'on', 'at', 'to', '&'}


def _is_acronym_definition(line, acronym):
    """True when the words immediately before "(ACRO)" spell it out.

    "Capital Improvement Program (CIP)" defines an acronym; a bare "(WM)" does
    not. This distinguishes the two structurally instead of growing an
    allowlist one municipal board at a time, which would weaken the gate with
    every entry. Ticker-shaped acronyms in TICKER_DENY are never exempted.
    """
    if acronym in TICKER_DENY:
        return False
    idx = line.find('(' + acronym + ')')
    if idx <= 0:
        return False
    before = re.sub(r'[^A-Za-z&\s]', ' ', line[:idx])
    words = [w for w in before.split() if w.lower() not in _STOPWORDS]
    if len(words) < len(acronym):
        return False
    initials = ''.join(w[0] for w in words[-len(acronym):]).upper()
    return initials == acronym.upper()


# Pipeline/architecture leaks
PIPELINE_PATTERNS = [
    (r'\bnavigator[s]?\b', 'Navigator reference (pipeline architecture)'),
    (r'\bCivicPlus\b', 'CMS platform name'),
    (r'\bGranicus\b', 'CMS platform name'),
    (r'\bBoardDocs\b', 'CMS platform name'),
    (r'\bRevize\b', 'CMS platform name'),
    (r'\bLegistar\b', 'CMS platform name'),
    (r'\bcrawl\s+schedule', 'Crawl schedule reference'),
    (r'\bclassifier\b', 'Classifier reference (pipeline architecture)'),
    (r'\bsignal\s+classification', 'Signal classification reference'),
    (r'\breward\s+track', 'Reward tracker reference'),
    (r'\bself-heal', 'Self-healing pipeline reference'),
    (r'\bauto.?onboard', 'Auto-onboarding reference'),
    (r'\bconfidence\s+decay', 'Confidence decay reference'),
    (r'\barchetype\s+match', 'Archetype matching reference'),
    (r'\bcooling\s+period', 'Cooling period reference'),
]

# FOAA strategy leaks
FOAA_PATTERNS = [
    (r'\bFOAA\s+request', 'FOAA request process mentioned'),
    (r'\bFOIA\s+request', 'FOIA request process mentioned'),
    (r'\brecords\s+request\s+(?:strategy|template|pattern)', 'Request strategy mentioned'),
    (r'\bfiled\s+a\s+(?:FOAA|FOIA|public\s+records)', 'Request filing described'),
    (r'\bemail\s+template', 'Email template reference'),
    (r'\bcontact\s+discover', 'Contact discovery reference'),
]

# Entity resolution leaks (in town digest context)
ENTITY_PATTERNS = [
    (r'\bentity\s+resolution', 'Entity resolution methodology'),
    (r'\bentity\s+sighting', 'Entity sighting count'),
    (r'\bresolved\s+ticker', 'Resolved ticker reference'),
    (r'\bsighting[s]?\s+across', 'Cross-town sighting count'),
    (r'\bappears?\s+in\s+\d+\s+(?:other\s+)?town', 'Cross-town pattern in digest'),
    (r'\b\d+\s+public\s+compan(?:y|ies)\s+identified', 'Entity count disclosure'),
]

# Signal/classification labels
SIGNAL_PATTERNS = [
    (r'\bHIGH\s+priority\b', 'Signal priority label'),
    (r'\bMEDIUM\s+priority\b', 'Signal priority label'),
    (r'\bLOW\s+priority\b', 'Signal priority label'),
    (r'\bclassified\s+signal', 'Classified signal reference'),
    (r'\bsignal\s+score', 'Signal score reference'),
]

# Coverage/expansion leaks
EXPANSION_PATTERNS = [
    (r'\badding\s+(?:police|fire|EMS|school)', 'Coverage expansion plan'),
    (r'\bexpanding\s+(?:to|coverage)', 'Coverage expansion plan'),
    (r'\bnext\s+month\s+we', 'Future plans disclosure'),
    (r'\bpipeline\s+(?:plans|roadmap)\b', 'Pipeline roadmap'),
    (r'\bwe\s+(?:plan|intend)\s+to\s+(?:add|expand|build)', 'Expansion plan'),
]


def is_town_digest(filepath):
    """Check if file is a town digest (stricter rules apply)."""
    name = filepath.name
    return name.startswith('town-') and not name.endswith('-index.md')


def is_data_story(filepath):
    """Check if file is a data story."""
    return filepath.name.startswith('story-')


def is_town_hub(filepath):
    """Check if file is a town hub page."""
    name = filepath.name
    return name.startswith('town-') and '-202' not in name


# Pages where architecture/methodology details are intentional.
# These get warnings instead of errors for pipeline patterns.
ALLOWLISTED_PAGES = {
    'methodology.md',       # Deliberately explains coverage and methods
    'how-it-works.md',      # Product page explaining the pipeline
    'about.md',             # Company overview
    'landing-altdata.md',   # Landing page for alt data buyers
    'landing-tower.md',     # Landing page for tower buyers
    'research.md',          # Data stories hub (mentions signal classification)
    'towns-index.md',       # Towns index (mentions expansion)
}


def scan_file(filepath, strict=False):
    """Scan a single file for violations. Returns list of (line_num, severity, message)."""
    violations = []
    text = filepath.read_text()
    lines = text.split('\n')
    is_digest = is_town_digest(filepath)
    is_story = is_data_story(filepath)
    is_allowlisted = filepath.name in ALLOWLISTED_PAGES

    for i, line in enumerate(lines, 1):
        # Skip frontmatter
        if i <= 5 and (line.startswith('Title:') or line.startswith('Slug:')
                       or line.startswith('Sortorder:') or line.startswith('Summary:')
                       or line == '---'):
            continue

        # Skip HTML comments and ad slots
        if line.strip().startswith('<!--') or line.strip().startswith('<div class="ad-'):
            continue

        # Pipeline patterns (WARNING on allowlisted pages, ERROR elsewhere)
        for pattern, desc in PIPELINE_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                severity = 'WARNING' if is_allowlisted else 'ERROR'
                violations.append((i, severity, f'{desc}: "{line.strip()[:80]}"'))

        # Expansion plans (WARNING on allowlisted pages, ERROR elsewhere)
        for pattern, desc in EXPANSION_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                severity = 'WARNING' if is_allowlisted else 'ERROR'
                violations.append((i, severity, f'{desc}: "{line.strip()[:80]}"'))

        # Ticker patterns (ERROR in digests, WARNING in stories)
        for pattern, desc in TICKER_PATTERNS:
            if pattern == GENERIC_PARENS_PATTERN:
                # Generic parenthetical heuristic: skip known non-ticker acronyms
                # (RFP, MRRA, BRAC, ...) so government/document terms don't false-flag,
                # but still flag any parenthetical that could be a real ticker.
                if not [m for m in re.findall(pattern, line)
                        if m.strip('()') not in NONTICKER_ACRONYMS
                        and not _is_acronym_definition(line, m.strip('()'))]:
                    continue
            elif not re.search(pattern, line):
                continue
            severity = 'ERROR' if is_digest else 'WARNING'
            violations.append((i, severity, f'{desc}: "{line.strip()[:80]}"'))

        # FOAA strategy (ERROR in digests, WARNING in stories)
        for pattern, desc in FOAA_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                severity = 'ERROR' if is_digest else 'WARNING'
                violations.append((i, severity, f'{desc}: "{line.strip()[:80]}"'))

        # Entity resolution details (ERROR in digests only)
        if is_digest:
            for pattern, desc in ENTITY_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append((i, 'ERROR', f'{desc}: "{line.strip()[:80]}"'))

        # Signal labels (ERROR in digests only)
        if is_digest:
            for pattern, desc in SIGNAL_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append((i, 'ERROR', f'{desc}: "{line.strip()[:80]}"'))

    # Structural checks for digests
    if is_digest:
        # Must have source links
        if 'http' not in text and '](/towns/' not in text:
            violations.append((0, 'WARNING', 'No source document links found in digest'))

        # Must have footer CTA
        if 'Municipal Alpha' not in text.split('---')[-1] if '---' in text else True:
            violations.append((0, 'WARNING', 'Missing footer CTA'))

        # Must not have cross-town references
        if re.search(r'across\s+\d+\s+municipalit', text):
            violations.append((0, 'ERROR', 'Cross-town pattern analysis in digest'))

    return violations


def main():
    parser = argparse.ArgumentParser(description='Red team content scanner')
    parser.add_argument('files', nargs='*', help='Files to scan (default: all content)')
    parser.add_argument('--strict', action='store_true', help='Fail on warnings too')
    args = parser.parse_args()

    content_dir = Path(__file__).parent.parent / 'content' / 'pages'

    if args.files:
        files = [Path(f) for f in args.files]
    else:
        files = sorted(content_dir.glob('*.md'))

    total_errors = 0
    total_warnings = 0
    files_with_issues = 0

    for filepath in files:
        if not filepath.exists():
            print(f"  File not found: {filepath}", file=sys.stderr)
            continue

        violations = scan_file(filepath, args.strict)
        errors = [v for v in violations if v[1] == 'ERROR']
        warnings = [v for v in violations if v[1] == 'WARNING']

        if violations:
            files_with_issues += 1
            print(f"\n{'=' * 60}")
            print(f"  {filepath.name}")
            print(f"{'=' * 60}")
            for line_num, severity, message in sorted(violations):
                marker = 'X' if severity == 'ERROR' else '!'
                loc = f"L{line_num}" if line_num > 0 else "FILE"
                print(f"  [{marker}] {loc:>6s}  {message}")

        total_errors += len(errors)
        total_warnings += len(warnings)

    # Summary
    print(f"\n{'─' * 60}")
    print(f"  Scanned {len(files)} files.")
    print(f"  {total_errors} errors, {total_warnings} warnings in {files_with_issues} files.")

    if total_errors > 0:
        print(f"\n  FAIL: {total_errors} red team violations found.")
        sys.exit(1)
    elif args.strict and total_warnings > 0:
        print(f"\n  FAIL (strict): {total_warnings} warnings found.")
        sys.exit(1)
    else:
        print(f"\n  PASS: No red team violations.")
        sys.exit(0)


if __name__ == '__main__':
    main()
