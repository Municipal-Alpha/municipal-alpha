#!/usr/bin/env python3
"""check_no_diffview.py — refuse to publish a review-scaffolding page.

`muni-scraper/tools/diffview/annotate_html_diff.py` renders a page with its
changes highlighted so a human can read the result instead of a unified diff.
That artifact is scaffolding: it carries highlight spans, a fixed legend, and
a navigation script. It is not the page, and it must never ship.

The generator already refuses to write inside any git working tree, so an
annotated copy cannot normally reach a repo at all. This is the other half:
prevention catches the expected path, a detector catches the unexpected one
(hand-copied file, a future generator without the guard, a stray --out).
Both halves are cheap and neither is sufficient alone
(`.claude/rules/mechanism-witness.md`).

Runs over the BUILT output, not the source, because the built tree is what
GitHub Pages serves and is therefore the surface the claim is about.

Exit codes (per `.claude/rules/diagnostic-exit-codes.md`):
    0 = scanned successfully, nothing found
    1 = a scaffolding artifact is present in the output (blocks the build)
    2 = the check could not run (no output tree) — NOT a pass
"""
import sys
from pathlib import Path

# Any one of these in published HTML means an annotated copy got through.
FINGERPRINTS = ("diffview-css", "diffview-js", "DIFFVIEW ANNOTATED COPY",
                'class="dv-new"', 'class="dv-chg"', 'class="dv-legend"')


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "output")
    if not out.is_dir():
        print(f"check-no-diffview: SKIPPED, no build output at {out}/ "
              f"(this is not a pass)", file=sys.stderr)
        return 2

    pages = sorted(out.rglob("*.html"))
    bad = []
    for p in pages:
        try:
            body = p.read_text(errors="replace")
        except OSError as e:
            print(f"check-no-diffview: cannot read {p}: {type(e).__name__}",
                  file=sys.stderr)
            return 2
        hits = [f for f in FINGERPRINTS if f in body]
        if hits:
            bad.append((p, hits))

    # Witness: announce the population, always, including the boring case.
    # "0 findings / 0 pages scanned" and "0 findings / 61 pages scanned" must
    # not look alike (mechanism-witness.md).
    print(f"check-no-diffview: {len(pages)} published page(s) scanned, "
          f"{len(bad)} carrying review scaffolding")

    if bad:
        print("\nBLOCK: review-scaffolding artifact(s) in the build output.")
        for p, hits in bad:
            print(f"  {p.relative_to(out)}  ({', '.join(hits)})")
        print("\nThese are annotated diff copies, not pages. Restore the real "
              "file from git and rebuild; never publish the annotated copy.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
