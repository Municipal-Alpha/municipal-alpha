#!/usr/bin/env python3
"""
check_index_coherence.py — refuse to publish a build whose sitemaps and whose
pages disagree about whether a URL should be indexed.

WHY THIS IS A GATE AND NOT A REPORT

A page listed in a sitemap is an instruction to a crawler: "this URL is
canonical, come get it." A `<meta name="robots" content="noindex">` on that same
page is the opposite instruction. A URL carrying both is not a style problem —
Google fetches it, drops it, and repeated contradiction costs the whole sitemap
credibility. There is no case where a site wants both, so this is mechanically
decidable and it fails the build (the same shape as check_metrics_drift.py and
check_no_diffview.py, both of which refuse rather than report).

That distinguishes it from a diagnostic under .claude/rules/diagnostic-exit-codes.md
— nothing downstream reads its exit code as "found nothing," it IS the refusal.
Exit 2 is reserved for the tool failing to look (no output/, no sitemap), which
must never be mistaken for a clean pass.

THE DEFECT IT WAS BUILT ON (2026-08-30 → 2026-09-01)

tools/inject_noindex.py scoped itself as "every directory under content/extra/".
When the public record layer (towns/, topics/, scope/ — 538 pages) shipped into
content/extra/ so copy-static-html would carry it, the injector noindexed all of
it, and because it walks output/<dir>/**.html for any dir with an extra source it
also reached the 221 dated Pelican town stories under output/towns/ that have no
extra source at all. Those were public and in sitemap.xml. 12 of 12 sampled
/towns/ URLs in the live sitemap served noindex.

Nothing caught it, because the injector's healthy output and its over-reach
output are the same line: "[noindex] injected into N pages". This gate is the
witness that can go red (.claude/rules/mechanism-witness.md) — it reports the
POPULATION it examined, not just its findings, so "0 conflicts / 0 URLs checked"
can never be mistaken for "0 conflicts / 700 URLs checked".

Usage:
    python3 tools/check_index_coherence.py          # gate the built output/
    python3 tools/check_index_coherence.py --quiet  # findings + totals only
"""

import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

BASEDIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASEDIR / "output"

LOC_RE = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>", re.IGNORECASE)
NOINDEX_RE = re.compile(
    r"""<meta\s+[^>]*name\s*=\s*['"]robots['"][^>]*content\s*=\s*['"][^'"]*\bnoindex\b""",
    re.IGNORECASE,
)


def sitemap_files():
    """Every sitemap XML at the root of output/ (sitemap.xml, sitemap-records.xml, ...)."""
    return sorted(OUTPUT_DIR.glob("sitemap*.xml"))


def url_to_path(loc: str) -> Path:
    """Map a sitemap <loc> to the file on disk that GitHub Pages would serve."""
    path = urlsplit(loc).path.lstrip("/")
    if path == "" or path.endswith("/"):
        return OUTPUT_DIR / path / "index.html"
    cand = OUTPUT_DIR / path
    if cand.is_dir():
        return cand / "index.html"
    return cand


def main() -> int:
    quiet = "--quiet" in sys.argv[1:]

    if not OUTPUT_DIR.is_dir():
        print("[index-coherence] COULD NOT LOOK — output/ does not exist; run the build first")
        return 2
    maps = sitemap_files()
    if not maps:
        print("[index-coherence] COULD NOT LOOK — no sitemap*.xml in output/")
        return 2

    seen: dict[str, str] = {}          # loc -> sitemap that first listed it
    conflicts: list[tuple[str, str]] = []   # (loc, sitemap)
    missing: list[tuple[str, str]] = []
    duplicates: list[tuple[str, str, str]] = []
    checked = 0

    for sm in maps:
        for loc in LOC_RE.findall(sm.read_text(encoding="utf-8", errors="replace")):
            checked += 1
            if loc in seen:
                duplicates.append((loc, seen[loc], sm.name))
                continue
            seen[loc] = sm.name
            fp = url_to_path(loc)
            if not fp.is_file():
                missing.append((loc, sm.name))
                continue
            if NOINDEX_RE.search(fp.read_text(encoding="utf-8", errors="replace")):
                conflicts.append((loc, sm.name))

    # Population witness: what was examined, always, including the boring case.
    print(
        f"[index-coherence] checked {checked} <loc> across "
        f"{len(maps)} sitemap(s): {', '.join(m.name for m in maps)}"
    )
    if not quiet and checked:
        print(f"[index-coherence]   unique URLs {len(seen)}, "
              f"conflicts {len(conflicts)}, dead {len(missing)}, dupes {len(duplicates)}")

    for loc, first, second in duplicates[:10]:
        print(f"[index-coherence] WARNING duplicate: {loc} in both {first} and {second}")
    for loc, sm in missing[:10]:
        print(f"[index-coherence] WARNING dead entry: {loc} ({sm}) resolves to no file")
    if len(missing) > 10:
        print(f"[index-coherence] WARNING ... and {len(missing) - 10} more dead entries")

    if conflicts:
        print(
            f"[index-coherence] BLOCKED — {len(conflicts)} URL(s) are listed in a "
            f"sitemap AND carry <meta name=\"robots\" content=\"noindex\">."
        )
        print("[index-coherence] A crawler is being told to fetch these and then to drop them.")
        for loc, sm in conflicts[:20]:
            print(f"[index-coherence]   {loc}  ({sm})")
        if len(conflicts) > 20:
            print(f"[index-coherence]   ... and {len(conflicts) - 20} more")
        print("[index-coherence] Fix ONE side: drop the URL from the sitemap, or stop "
              "noindexing it (see PUBLIC_EXTRA_DIRS in tools/inject_noindex.py).")
        return 1

    print("[index-coherence] OK — no sitemap URL carries noindex.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
