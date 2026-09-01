#!/usr/bin/env python3
"""
Inject <meta name="robots" content="noindex"> into the unlinked standalone
pages under content/extra/ as they sit in output/.

WHY: every page under content/extra/ is an unlinked, directly-shared page
(prospect/buyer discussion pages, dispatches, decks, overviews). None of them
are in sitemap.xml and none are linked from the public site — they are sent to
specific recipients via tracked links, not meant to be found via organic search.
Without an explicit noindex they are protected only by obscurity: one forwarded
or leaked URL away from Google discovering and indexing a buyer's prospect page,
which could then surface "DESRI"/"Connell"/"Ready.net" pages in search results
(a confidentiality break — Commandment II, guard the trust).

noindex (NOT a robots.txt Disallow) is the correct control here: a Disallow
blocks crawling, which means Google never sees the noindex and can still index
the bare URL if it discovers it via a link. Allow-crawl + noindex is Google's
prescribed way to guarantee a page never appears in search.

Runs AFTER `copy-static-html` (wired into the Makefile html/publish targets), so
it regenerates on every build/deploy and never drifts. Stdlib-only — no extra
dependency in the GitHub Actions build, same behavior on macOS (local) and
ubuntu-latest (CI), unlike a cross-platform sed injection.

SCOPE: output/<dir>/**.html files that have a corresponding content/extra/<dir>/
source, MINUS the dirs named in PUBLIC_EXTRA_DIRS. New buyer pages added to
copy-static-html are covered automatically.

PUBLIC_EXTRA_DIRS exists because content/extra/ stopped being a synonym for
"buyer-only" on 2026-08-30, when the public record layer (towns/, topics/,
scope/) shipped into it so copy-static-html would carry it. scope/ is currently
held OUT of the index by founder decision — see HELD_BACK_EXTRA_DIRS. Without the
exclusion this tool noindexed all 538 of those pages, and — because it walks
output/<dir>/**.html for any dir with an extra source — it also reached the 221
dated Pelican town data stories under output/towns/, which have no extra source
of their own and were public and in sitemap.xml. Every /towns/ URL in the
sitemap served noindex for two days. The build gate that now catches this class
is tools/check_index_coherence.py; this list is the fix, that gate is the
witness.

Idempotent: skips any page that already carries a name="robots" meta (respects
an explicit directive a page author may have set).

Usage:
    python3 tools/inject_noindex.py            # inject into output/, report count
    python3 tools/inject_noindex.py --check     # report what WOULD change, write nothing
"""

import re
import sys
from pathlib import Path

BASEDIR = Path(__file__).resolve().parent.parent
EXTRA_DIR = BASEDIR / "content" / "extra"
OUTPUT_DIR = BASEDIR / "output"

NOINDEX_TAG = '<meta name="robots" content="noindex">'

# content/extra/ dirs that are PUBLIC surfaces, not buyer pages. Their pages get
# any noindex STRIPPED. Adding a dir here is a deliberate decision to expose it
# to search; removing one hides it.
PUBLIC_EXTRA_DIRS = frozenset({"towns", "topics"})

# Public-by-construction dirs that are deliberately held OUT of the search index.
# They stay live, stay linked from the desk, and keep the noindex their generator
# writes — obscurity plus an explicit directive, the same posture as a buyer page.
#
# scope/ is held back by founder decision, 2026-09-01. The class-* pages carry
# the names of private individuals taken from the municipal record — the person
# who applied for an ADU permit, by name. Those names are public in the sense
# that the minutes are public; making them SEARCHABLE BY NAME on our own domain
# is a different act, and it would be the first time this company did it
# (Commandment II — guard the trust; adjacent to memory/project_buyer_exclusions).
# Towns and topics ship; scope waits on a separate call.
#
# This is not a comment. tools/check_index_coherence.py asserts that every page
# under these dirs still carries noindex and appears in no sitemap, and BLOCKS
# the build otherwise — so moving a dir from here to PUBLIC_EXTRA_DIRS is a
# visible decision rather than a quiet one.
HELD_BACK_EXTRA_DIRS = frozenset({"scope"})

# First <head ...> opening tag, case-insensitive.
HEAD_OPEN_RE = re.compile(r"<head\b[^>]*>", re.IGNORECASE)
# Any existing robots meta — if present, leave the page alone.
ROBOTS_META_RE = re.compile(r"""<meta\s+[^>]*name\s*=\s*['"]robots['"]""", re.IGNORECASE)
# A robots meta that actually says noindex — the only kind stripped from public
# pages. A page carrying e.g. `noarchive` alone keeps it.
NOINDEX_META_RE = re.compile(
    r"""\s*<meta\s+[^>]*name\s*=\s*['"]robots['"][^>]*content\s*=\s*['"][^'"]*\bnoindex\b[^'"]*['"][^>]*>""",
    re.IGNORECASE,
)


def extra_output_pages():
    """Yield output/*.html paths that derive from a content/extra/<dir> source.

    Mirrors how copy-static-html populates output/: each content/extra/<dir>
    contributes output/<dir>/**.html. We only ever return paths that both
    (a) have an extra source and (b) actually exist in output/ (i.e. were
    copied this build), so the set is exactly the unlinked standalone pages.
    """
    if not EXTRA_DIR.is_dir() or not OUTPUT_DIR.is_dir():
        return
    for src in sorted(EXTRA_DIR.iterdir()):
        if not src.is_dir():
            continue  # skip robots.txt, CNAME, favicons, etc.
        out_dir = OUTPUT_DIR / src.name
        if not out_dir.is_dir():
            continue  # this extra dir wasn't copied into output this build
        for html_path in sorted(out_dir.rglob("*.html")):
            # Only pages that ACTUALLY came from this extra dir. output/<name>/
            # is not owned by content/extra/<name>/ — a Pelican page can render
            # into the same directory, and its children certainly can. Matching
            # on the directory name alone reached, in one build:
            #   output/case-studies/index.html   (Pelican marketing hub; the extra
            #                                     dir holds seven PDFs and no HTML)
            #   output/towns/<slug>/<date>/      (221 dated Pelican data stories,
            #                                     public and in sitemap.xml)
            # Requiring the source file to exist is what makes the scope claim in
            # this module's docstring true rather than aspirational.
            if not (src / html_path.relative_to(out_dir)).is_file():
                continue
            yield html_path, src.name in PUBLIC_EXTRA_DIRS


def strip_noindex(html_path: Path, write: bool) -> str:
    """Remove a noindex robots meta from a PUBLIC page. Returns a status.

    The record-layer pages (towns/, topics/, scope/) are generated by
    tools/gen_brief_review_pages.py in the muni-scraper repo, which emits
    `<meta name="robots" content="noindex">` into every page it writes. That was
    right while those pages were buyer-only research views; it became wrong on
    2026-08-30 when the same generator's output was promoted to a public layer
    and the meta was not revisited. All 538 shipped noindexed.

    Stripping here makes the SITE the single authority on indexability, which is
    where robots.txt and the sitemaps already live. It also means the committed
    HTML and the served HTML differ on this one tag — a real wart, and the
    durable fix is for the generator to stop emitting the meta for public
    output. Until then this is fail-safe in the right direction: a page we
    intend to publish is published.
    """
    text = html_path.read_text(encoding="utf-8")
    new_text, n = NOINDEX_META_RE.subn("", text)
    if not n:
        return "already-indexable"
    if write:
        html_path.write_text(new_text, encoding="utf-8")
    return "stripped"


def inject(html_path: Path, write: bool) -> str:
    """Return a status: 'injected', 'skipped-has-robots', 'skipped-no-head'."""
    text = html_path.read_text(encoding="utf-8")
    if ROBOTS_META_RE.search(text):
        return "skipped-has-robots"
    m = HEAD_OPEN_RE.search(text)
    if not m:
        return "skipped-no-head"
    new_text = text[: m.end()] + "\n" + NOINDEX_TAG + text[m.end():]
    if write:
        html_path.write_text(new_text, encoding="utf-8")
    return "injected"


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    counts = {"injected": 0, "skipped-has-robots": 0, "skipped-no-head": 0,
              "stripped": 0, "already-indexable": 0}
    skipped_no_head = []
    for html_path, is_public in extra_output_pages():
        if is_public:
            status = strip_noindex(html_path, write=not check_only)
        else:
            status = inject(html_path, write=not check_only)
        counts[status] += 1
        if status == "skipped-no-head":
            skipped_no_head.append(html_path.relative_to(OUTPUT_DIR))

    verb = "would inject" if check_only else "injected"
    stripped_verb = "would strip" if check_only else "stripped"
    print(f"[noindex] public dirs ({', '.join(sorted(PUBLIC_EXTRA_DIRS))}): "
          f"{stripped_verb} noindex from {counts['stripped']} page(s); "
          f"{counts['already-indexable']} already indexable.")
    print(f"[noindex] held back by decision ({', '.join(sorted(HELD_BACK_EXTRA_DIRS))}): "
          f"left noindexed; see HELD_BACK_EXTRA_DIRS for why.")
    print(
        f"[noindex] {verb} into {counts['injected']} unlinked extra page(s); "
        f"{counts['skipped-has-robots']} already had a robots meta; "
        f"{counts['skipped-no-head']} had no <head>."
    )
    for p in skipped_no_head:
        print(f"[noindex]   WARNING no <head>, left unprotected: {p}")
    # Build step: never fail the build over this. A missing <head> is surfaced
    # as a WARNING above (Commandment VII — diagnostic reports status, exits 0).
    return 0


if __name__ == "__main__":
    sys.exit(main())
