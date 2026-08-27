#!/usr/bin/env python3
"""check_live_surface.py — verify the site we just published actually serves
what we think it serves.

Runs as the LAST step of the deploy workflow, after Pages reports success. A
green Actions run means the artifact uploaded; it is not evidence that a reader
loading the page gets the right bytes.

This is the immediate half of a two-part witness (see
muni-scraper `docs/plans/deploy-witness-scope.md`, finding M1). The other half
is a daily sweep in muni-scraper, and BOTH are needed:

  this file    fires on every deploy -> fast feedback, catches a bad publish
  daily sweep  fires whether or not anything deployed -> catches the silent
               case, which is the one that actually happened. A wrong LinkedIn
               URL sat on /contact/ for days precisely because nobody deployed;
               a deploy-triggered check is silent for exactly as long as
               nothing is deployed.

Deliberately SMALL and deliberately about correctness, not copy. Assert
canonical links, handles, schemes, redirect targets -- things that are WRONG
when they change. Never a sentence of marketing prose: that goes red on the
next legitimate edit, and a check that cries wolf is muted within a week, at
which point it reads as coverage while watching nothing.

Exit codes:
    0 = every assertion checked and holding
    1 = at least one assertion failed
    2 = could not check (no base URL, fetch failed) -- NOT a pass
"""
import sys
import urllib.error
import urllib.request

TIMEOUT = 20
UA = "Mozilla/5.0 (compatible; MunicipalAlpha-postdeploy-check/1.0)"

# (path, must_contain, must_not_contain, why)
ASSERTIONS = [
    ("/contact/",
     "linkedin.com/in/mattmacdonald2",
     "linkedin.com/in/matthewmacdonald",
     "the wrong handle sends every reader who clicks it to a stranger"),
    ("/",
     None,
     "diffview-css",
     "a review-scaffolding page must never be published (check_no_diffview.py "
     "guards the build; this guards the served result)"),
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            if r.status != 200:
                return None, f"HTTP {r.status}"
            return r.read().decode("utf-8", errors="replace"), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return None, f"{type(e).__name__}: {e}"


def main():
    base = (sys.argv[1] if len(sys.argv) > 1 else "https://municipalalpha.com").rstrip("/")
    failures, unreachable = [], []

    for path, need, deny, why in ASSERTIONS:
        url = base + path
        body, reason = fetch(url)
        if body is None:
            unreachable.append((url, reason))
            continue
        if deny and deny in body:
            failures.append((url, f"found {deny!r}, which must not be present", why))
        elif need and need not in body:
            failures.append((url, f"expected {need!r}, absent", why))

    # Witness: the population prints unconditionally, including the all-clear.
    # "0 failures / 0 checked" must never look like "0 failures / 2 checked".
    checked = len(ASSERTIONS) - len(unreachable)
    print(f"check-live-surface: {base} — {checked} of {len(ASSERTIONS)} "
          f"assertion(s) evaluated, {len(failures)} failing, "
          f"{len(unreachable)} unreachable")

    for url, reason in unreachable:
        print(f"  UNREACHABLE  {url}  ({reason})")
    for url, detail, why in failures:
        print(f"  FAIL  {url}\n        {detail}\n        why it matters: {why}")

    if unreachable:
        print("\nCould not check every assertion. This is not a pass.")
        return 2
    if failures:
        print("\nThe published site does not serve what it should.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
