#!/usr/bin/env python3
"""
Generate output/llms-full.txt — a single-file plain-text concatenation of the
site's core informational pages, case studies, and data stories, for AI agents
that want the full content in one fetch (the companion to the lightweight
llms.txt index).

Runs AFTER `pelican` builds output/ (wired into the Makefile `html`/`publish`
targets), so it regenerates on every build/deploy and never drifts from the
content. Stdlib-only — no extra dependency in the GitHub Actions build.

Inclusion is rule-based (INCLUDE_PREFIXES below): new pages under solutions/,
research/, stories/, essays/ auto-include, as do the per-buyer pages named in
data/sectors.json and the connector page; the long-tail town/profile/vendor/
prospect pages auto-exclude. Add a prefix here to widen the corpus.

Usage:
    python3 tools/build_llms_full.py            # writes output/llms-full.txt
    python3 tools/build_llms_full.py --check     # build to stdout, don't write
"""

import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SITE_URL = "https://municipalalpha.com"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
SECTORS_FILE = Path(__file__).resolve().parent.parent / "data" / "sectors.json"

# Path prefixes (relative to output/) whose pages belong in the full-text corpus.
# A page qualifies if its directory is exactly one of these, or nested under one.
INCLUDE_PREFIXES = (
    "about",
    "how-it-works",
    "methodology",
    "solutions",
    "research",
    "stories",
    "essays",
    # The connector page: what the product is for today's buyer.
    "mcp-launch",
)


def _sector_slugs() -> tuple:
    """The per-buyer pages (for-saas-revenue-teams, ...), read from
    data/sectors.json so a new sector page joins the corpus without an edit
    here. A missing or unreadable file fails the build loudly: silently
    dropping the buyer pages is how this file came to describe nobody's
    current buyer."""
    with open(SECTORS_FILE, encoding="utf-8") as f:
        sectors = json.load(f)["sectors"]
    return tuple(s["slug"] for s in sectors.values())


INCLUDE_PREFIXES = INCLUDE_PREFIXES + _sector_slugs()

# Hard ceiling per page so one runaway page can't bloat the file.
MAX_CHARS_PER_PAGE = 24_000


class MainTextExtractor(HTMLParser):
    """Collect text inside <main>...</main>, skipping <script>/<style>.

    base.html puts nav/footer OUTSIDE <main>, so extracting <main> already
    drops the chrome; we only additionally guard against inline script/style.
    """

    _BREAK_TAGS = {"p", "div", "section", "li", "h1", "h2", "h3", "h4", "h5",
                   "tr", "br", "ul", "ol", "blockquote", "article"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_main = False
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == "main":
            self.in_main = True
            return
        if not self.in_main:
            return
        if tag in ("script", "style"):
            self.skip += 1
        elif tag in self._BREAK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag == "main":
            self.in_main = False
        elif self.in_main and tag in ("script", "style") and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if self.in_main and not self.skip:
            self.parts.append(data)


def _clean(text: str) -> str:
    text = html.unescape(text)
    # collapse runs of spaces/tabs, trim each line, squeeze blank lines
    text = re.sub(r"[ \t]+", " ", text)
    lines = [ln.strip() for ln in text.split("\n")]
    out, blanks = [], 0
    for ln in lines:
        if ln:
            blanks = 0
            out.append(ln)
        else:
            blanks += 1
            if blanks <= 1:
                out.append("")
    return "\n".join(out).strip()


def _title(raw_html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", raw_html, re.S | re.I)
    if not m:
        return ""
    t = html.unescape(m.group(1)).strip()
    # strip the " · Municipal Alpha" suffix the templates append
    return re.sub(r"\s*·\s*Municipal Alpha\s*$", "", t).strip()


def _md_title(md_text: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def _md_body(md_text: str) -> str:
    """Markdown twin body: drop the leading H1 (printed separately), squeeze blanks."""
    lines = md_text.splitlines()
    start = 0
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            start = i + 1
            break
    body = "\n".join(lines[start:])
    return re.sub(r"\n{3,}", "\n\n", body).strip()


def _url_for(index_html: Path) -> str:
    rel = index_html.parent.relative_to(OUTPUT_DIR).as_posix()
    return f"{SITE_URL}/{rel}/"


def _included(index_html: Path) -> bool:
    rel = index_html.parent.relative_to(OUTPUT_DIR).as_posix()
    if rel == ".":
        return False
    top = rel.split("/", 1)[0]
    return top in INCLUDE_PREFIXES


def collect() -> str:
    if not OUTPUT_DIR.is_dir():
        print(f"ERROR: {OUTPUT_DIR} not found — run `make html` first.", file=sys.stderr)
        sys.exit(1)

    pages = sorted(
        (p for p in OUTPUT_DIR.glob("**/index.html") if _included(p)),
        key=lambda p: p.parent.relative_to(OUTPUT_DIR).as_posix(),
    )

    chunks = [
        "# Municipal Alpha — Full Text",
        "",
        "> Plain-text concatenation of the core informational pages, case "
        "studies, and data stories from municipalalpha.com. Generated at build "
        "time; the lightweight index is at " + SITE_URL + "/llms.txt.",
        "",
    ]
    for page in pages:
        raw = page.read_text(encoding="utf-8", errors="replace")
        extractor = MainTextExtractor()
        extractor.feed(raw)
        body = _clean("".join(extractor.parts))
        if not body:
            continue
        if len(body) > MAX_CHARS_PER_PAGE:
            body = body[:MAX_CHARS_PER_PAGE].rsplit(" ", 1)[0] + " […]"
        title = _title(raw) or page.parent.name
        chunks.append("\n" + "=" * 72)
        chunks.append(f"# {title}")
        chunks.append(f"URL: {_url_for(page)}")
        chunks.append("=" * 72 + "\n")
        chunks.append(body)
        chunks.append("")

    # Standalone content/extra pages that ship a clean index.md twin (the
    # AI-facing markdown alternate, linked via <link rel="alternate"
    # type="text/markdown">). The presence of an index.md is the public-content
    # marker: discussion/prospect pages carry no twin, so they never join the
    # feed. Mirrors the rule-based inclusion above (Commandment VIII — one rule,
    # not a per-page list to maintain).
    for md in sorted(OUTPUT_DIR.glob("**/index.md"),
                     key=lambda p: p.parent.relative_to(OUTPUT_DIR).as_posix()):
        body = _md_body(md.read_text(encoding="utf-8", errors="replace"))
        if not body:
            continue
        if len(body) > MAX_CHARS_PER_PAGE:
            body = body[:MAX_CHARS_PER_PAGE].rsplit(" ", 1)[0] + " […]"
        title = _md_title(md.read_text(encoding="utf-8", errors="replace")) or md.parent.name
        chunks.append("\n" + "=" * 72)
        chunks.append(f"# {title}")
        chunks.append(f"URL: {_url_for(md)}")
        chunks.append("=" * 72 + "\n")
        chunks.append(body)
        chunks.append("")

    return "\n".join(chunks).rstrip() + "\n"


def main() -> None:
    text = collect()
    if "--check" in sys.argv:
        sys.stdout.write(text)
        return
    out = OUTPUT_DIR / "llms-full.txt"
    out.write_text(text, encoding="utf-8")
    n_pages = text.count("\nURL: ")
    print(f"Wrote {out} ({len(text):,} chars, {n_pages} pages)")


if __name__ == "__main__":
    main()
