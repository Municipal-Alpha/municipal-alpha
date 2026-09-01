#!/usr/bin/env python3
"""
build_records_sitemap.py — emit output/sitemap-records.xml for the public record
layer (towns/, topics/, scope/).

WHY A SECOND SITEMAP

output/sitemap.xml is rendered by Pelican from its own `pages` and `articles`
collections (theme/municipal-alpha/templates/sitemap.html). The record layer is
not Pelican content — it is static HTML copied into output/ by the Makefile's
copy-static-html step — so the template cannot see it and never will. As of
2026-09-01 that left 538 pages absent from every sitemap. Rather than convert
537 generated pages into Pelican pages, this writes a companion sitemap from the
built output, the same post-build pattern build_llms_full.py already uses.

robots.txt carries a Sitemap: line for each. Multiple Sitemap directives are
part of the sitemaps.org protocol and are read by Google and Bing; no sitemap
index file is needed for two maps.

WHAT IT DELIBERATELY EXCLUDES

- Anything already listed in output/sitemap.xml. The ten town hubs that Pelican
  also generates (/towns/augusta-me/ and friends) are overwritten by the record
  layer's copy but keep their Pelican sitemap entry, so listing them again here
  would put one URL in two sitemaps. First map wins.
- Anything already carrying <meta name="robots" content="noindex">. A sitemap
  entry for a noindexed page is a self-contradiction; refusing to write one
  means this tool cannot itself create the defect that
  tools/check_index_coherence.py exists to catch.

  But a SILENT skip here would re-create that defect one level up: by the time
  this runs, inject_noindex.py's strip pass has already cleared the record
  layer, so a noindexed record page means that pass did not do its job — and
  quietly dropping the page would leave check_index_coherence.py reporting
  "0 conflicts" over a sitemap that simply lists nothing. Healthy output and
  broken output would be the same green line. So any noindexed record page is
  a BLOCK (exit 1), not a skip.

Usage:
    python3 tools/build_records_sitemap.py           # writes output/sitemap-records.xml
    python3 tools/build_records_sitemap.py --check    # print to stdout, write nothing
"""

import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit, quote

BASEDIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASEDIR / "output"
SITE_URL = "https://municipalalpha.com"

# Directories of the public record layer, relative to output/. Mirrors
# PUBLIC_EXTRA_DIRS in tools/inject_noindex.py — the same set, seen from the
# other side: those are the dirs we refuse to noindex, these are the dirs we
# advertise. If one list changes the other almost certainly should.
RECORD_DIRS = ("towns", "topics", "scope")

LOC_RE = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>", re.IGNORECASE)
NOINDEX_RE = re.compile(
    r"""<meta\s+[^>]*name\s*=\s*['"]robots['"][^>]*content\s*=\s*['"][^'"]*\bnoindex\b""",
    re.IGNORECASE,
)


def existing_locs() -> set[str]:
    """Path components of every URL already in a Pelican-built sitemap."""
    out = set()
    for sm in OUTPUT_DIR.glob("sitemap.xml"):
        for loc in LOC_RE.findall(sm.read_text(encoding="utf-8", errors="replace")):
            out.add(urlsplit(loc).path or "/")
    return out


def url_for(html_path: Path) -> str:
    """Canonical site path for a built file. index.html collapses to its directory."""
    rel = html_path.relative_to(OUTPUT_DIR).as_posix()
    if rel.endswith("/index.html"):
        rel = rel[: -len("index.html")]
    elif rel == "index.html":
        rel = ""
    return "/" + rel


def collect():
    """Yield (url_path, lastmod) for record-layer pages that belong in a sitemap."""
    already = existing_locs()
    skipped = {"already-in-sitemap": 0, "noindex": 0}
    rows = []
    for d in RECORD_DIRS:
        base = OUTPUT_DIR / d
        if not base.is_dir():
            continue
        for html_path in sorted(base.rglob("*.html")):
            url_path = url_for(html_path)
            if url_path in already:
                skipped["already-in-sitemap"] += 1
                continue
            if NOINDEX_RE.search(html_path.read_text(encoding="utf-8", errors="replace")):
                skipped["noindex"] += 1
                continue
            lastmod = date.fromtimestamp(html_path.stat().st_mtime).isoformat()
            rows.append((url_path, lastmod))
    return rows, skipped


def render(rows) -> str:
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url_path, lastmod in rows:
        loc = SITE_URL + quote(url_path)
        parts.append("  <url>")
        parts.append(f"    <loc>{loc}</loc>")
        parts.append(f"    <lastmod>{lastmod}</lastmod>")
        parts.append("  </url>")
    parts.append("</urlset>")
    return "\n".join(parts) + "\n"


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    if not OUTPUT_DIR.is_dir():
        print("[records-sitemap] COULD NOT LOOK — output/ does not exist; run the build first")
        return 2

    rows, skipped = collect()
    xml = render(rows)
    if check_only:
        sys.stdout.write(xml)
    else:
        (OUTPUT_DIR / "sitemap-records.xml").write_text(xml, encoding="utf-8")

    verb = "would write" if check_only else "wrote"
    per_dir = {d: sum(1 for u, _ in rows if u.startswith(f"/{d}/")) for d in RECORD_DIRS}
    print(f"[records-sitemap] {verb} sitemap-records.xml with {len(rows)} URL(s) "
          + ", ".join(f"{d}={n}" for d, n in per_dir.items()))
    print(f"[records-sitemap]   skipped {skipped['already-in-sitemap']} already in sitemap.xml, "
          f"{skipped['noindex']} noindexed")
    if not rows:
        # An empty record sitemap means the layer vanished from output/ — that is
        # a build problem, not a clean run, and must not read as one.
        print("[records-sitemap] BLOCKED — no record-layer pages found in output/; "
              "did copy-static-html run?")
        return 1
    if skipped["noindex"]:
        print(f"[records-sitemap] BLOCKED — {skipped['noindex']} record-layer page(s) "
              f"still carry noindex after inject_noindex.py's strip pass.")
        print("[records-sitemap] They would be silently absent from the sitemap and "
              "nothing downstream would notice. Check PUBLIC_EXTRA_DIRS in "
              "tools/inject_noindex.py covers " + ", ".join(RECORD_DIRS) + ".")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
