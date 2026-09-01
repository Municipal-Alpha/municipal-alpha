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

IT ALSO ASSERTS THE HOLD

A second, positive check: every page under HELD_BACK_DIRS must still carry
noindex and appear in no sitemap. That turns a founder decision (scope/ is not
indexed, 2026-09-01) from a comment plus a frozenset into something the build
enforces, so lifting it is a visible act rather than a plausible-looking tidy-up
of two "inconsistent" lists.

Usage:
    python3 tools/check_index_coherence.py          # gate the built output/
    python3 tools/check_index_coherence.py --quiet  # findings + totals only
"""

import sys
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))

BASEDIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASEDIR / "output"

# Policy lives in tools/index_policy.py. Importing rather than restating it is
# what makes 'the assertion list drifted from the strip list' unrepresentable
# rather than merely detectable — see that module's header for the review
# finding behind it.
from index_policy import (  # noqa: E402
    HELD_BACK_EXTRA_DIRS,
    SITEMAP_MAX_URLS,
    SITEMAP_MAX_BYTES,
    NOINDEX_META_RE,
    CANONICAL_LINK_RE,
    HREF_RE,
    LOC_RE,
)

HELD_BACK_DIRS = tuple(sorted(HELD_BACK_EXTRA_DIRS))



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
            if NOINDEX_META_RE.search(fp.read_text(encoding="utf-8", errors="replace")):
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

    # A sitemapped URL whose canonical points somewhere else is the same
    # contradiction as noindex, in a form the noindex check cannot see: the
    # sitemap says "index this URL", the page says "no, index that one".
    # Measured on the 2026-09-01 build: 127 sitemapped pages carry a
    # self-canonical, 150 carry none, 0 point elsewhere — so this gate starts
    # green, which is the cheap moment to add it. Raised by the class-2 review.
    # A page with NO canonical tag is fine and common; only a mismatch is a
    # finding.
    canonical_mismatches: list[tuple[str, str]] = []
    canonical_checked = 0
    for loc, sm in seen.items():
        fp = url_to_path(loc)
        if not fp.is_file():
            continue
        text = fp.read_text(encoding="utf-8", errors="replace")
        tag = CANONICAL_LINK_RE.search(text)
        if not tag:
            continue
        href = HREF_RE.search(tag.group(0))
        if not href:
            continue
        canonical_checked += 1
        if urlsplit(href.group(1)).path.rstrip("/") != urlsplit(loc).path.rstrip("/"):
            canonical_mismatches.append((loc, href.group(1)))
    print(f"[index-coherence] canonicals: {canonical_checked} sitemapped page(s) "
          f"declare one, {len(canonical_mismatches)} point elsewhere")

    if canonical_mismatches:
        print(f"[index-coherence] BLOCKED — {len(canonical_mismatches)} sitemapped "
              f"URL(s) declare a canonical pointing at a different URL.")
        print("[index-coherence] The sitemap says index this; the page says index "
              "something else. Fix one side.")
        for loc, href in canonical_mismatches[:20]:
            print(f"[index-coherence]   {loc}\n[index-coherence]     -> {href}")
        return 1

    # Sitemap size, per sitemaps.org: 50,000 URLs / 50MB per file.
    for sm in maps:
        n = len(LOC_RE.findall(sm.read_text(encoding="utf-8", errors="replace")))
        size = sm.stat().st_size
        if n > SITEMAP_MAX_URLS or size > SITEMAP_MAX_BYTES:
            print(f"[index-coherence] BLOCKED — {sm.name} has {n:,} URLs / "
                  f"{size:,} bytes, past the safe single-file limit "
                  f"({SITEMAP_MAX_URLS:,} / {SITEMAP_MAX_BYTES:,}). Shard it "
                  f"behind a sitemap index.")
            return 1

    # The hold, asserted positively rather than assumed.
    #
    # An empty HELD_BACK_DIRS is a real state ("nothing is held back") and must
    # not print as a quiet pass, because it is also what removing a dir from the
    # list looks like — and one of those is a privacy decision being reversed.
    # Say it out loud either way.
    if not HELD_BACK_DIRS:
        print("[index-coherence] held back: NOTHING — no surface is being kept "
              "out of the index. If that is a change, it is a decision "
              "(see HELD_BACK_EXTRA_DIRS in tools/index_policy.py).")
    held_examined = 0
    held_indexable: list[str] = []
    for d in HELD_BACK_DIRS:
        base = OUTPUT_DIR / d
        if not base.is_dir():
            print(f"[index-coherence] WARNING held-back dir output/{d}/ is absent; "
                  f"nothing to hold, which is not the same as holding it")
            continue
        for html_path in sorted(base.rglob("*.html")):
            held_examined += 1
            if not NOINDEX_META_RE.search(html_path.read_text(encoding="utf-8", errors="replace")):
                held_indexable.append(str(html_path.relative_to(OUTPUT_DIR)))
    print(f"[index-coherence] held back ({', '.join(HELD_BACK_DIRS)}): "
          f"{held_examined} page(s) examined, {len(held_indexable)} missing noindex")

    if held_indexable:
        print(f"[index-coherence] BLOCKED — {len(held_indexable)} page(s) under a "
              f"held-back dir have no noindex.")
        print("[index-coherence] These are held out of the index by decision "
              "(see HELD_BACK_EXTRA_DIRS in tools/inject_noindex.py). If the hold "
              "was lifted deliberately, move the dir into PUBLIC_EXTRA_DIRS and "
              "RECORD_DIRS and remove it from both HELD_BACK lists.")
        for rel in held_indexable[:20]:
            print(f"[index-coherence]   {rel}")
        if len(held_indexable) > 20:
            print(f"[index-coherence]   ... and {len(held_indexable) - 20} more")
        return 1

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
