#!/usr/bin/env python3
"""
index_policy.py — the single place that says which surfaces are indexable.

WHY THIS MODULE EXISTS

Three tools need the same two lists of directories:

    tools/inject_noindex.py        strips noindex from public dirs, keeps it on held dirs
    tools/build_records_sitemap.py advertises public dirs, never held dirs
    tools/check_index_coherence.py asserts both of the above actually happened

They first shipped with the lists duplicated in each file and a comment in each
saying to keep them in sync. A class-2 adversarial review (Gemini, strategic,
2026-09-01) named that as the design's primary risk, and named the failure
precisely: *a new directory containing private data added to inject_noindex.py's
held-back list but not to check_index_coherence.py's assertion list — the privacy
guardrail would silently vanish.* That is right, and it is Commandment XI: a
repeated judgment ("remember to update the other two") is a failure of encoding.

The review proposed a build step that parses all three files' ASTs and asserts
the lists match. That detects the drift. Importing from one module makes the
drift unrepresentable, which is cheaper and stronger (Commandment VI — reach for
the lightest thing that works; VIII — fix at the level the evidence supports).

The regexes live here for the same reason: three tools were each carrying their
own copy of "what does a noindex meta look like", and a divergence between the
one that STRIPS and the one that VERIFIES the strip is exactly a gate that
passes over a defect it was built to catch.
"""

import re

# --------------------------------------------------------------------------
# Policy
# --------------------------------------------------------------------------

# content/extra/ dirs that are PUBLIC surfaces, not buyer pages. Their pages get
# any noindex STRIPPED and are listed in sitemap-records.xml. Adding a dir here
# is a deliberate decision to expose it to search.
PUBLIC_EXTRA_DIRS = frozenset({"towns", "topics"})

# Public-by-construction dirs deliberately held OUT of the search index. They
# stay live, stay linked from the desk, and keep the noindex their generator
# writes — obscurity plus an explicit directive, the same posture as a buyer
# page. Nothing is taken down; it is simply not promoted.
#
# scope/ is held back by founder decision, 2026-09-01. The class-* pages carry
# the names of private individuals taken from the municipal record — the person
# who applied for an ADU permit, by name. Those names are public in the sense
# that the minutes are public; making them SEARCHABLE BY NAME on our own domain
# is a different act, and it would be the first time this company did it
# (Commandment II — guard the trust). Towns and topics ship; scope waits on a
# separate call.
#
# This is not merely a comment. check_index_coherence.py asserts that every page
# under these dirs still carries noindex and appears in no sitemap, and BLOCKS
# the build otherwise — so moving a dir from here into PUBLIC_EXTRA_DIRS is a
# visible decision rather than a quiet one.
HELD_BACK_EXTRA_DIRS = frozenset({"scope"})

# The two sets must never overlap: a dir cannot be both advertised and held.
assert not (PUBLIC_EXTRA_DIRS & HELD_BACK_EXTRA_DIRS), (
    "a directory is in both PUBLIC_EXTRA_DIRS and HELD_BACK_EXTRA_DIRS"
)

# sitemaps.org caps a single sitemap at 50,000 URLs and 50MB uncompressed. We
# refuse well short of it, so the decision about sharding is made deliberately
# rather than discovered when a crawler starts rejecting the file. Raised by the
# same class-2 review; the record layer grows with every town onboarded.
SITEMAP_MAX_URLS = 49_000
SITEMAP_MAX_BYTES = 45 * 1024 * 1024

# --------------------------------------------------------------------------
# Shared patterns
# --------------------------------------------------------------------------

# Attribute order is not fixed by HTML, and every one of these is valid and
# means the same thing:
#     <meta name="robots" content="noindex">
#     <meta content="noindex" name="robots">
#     <meta name='robots' content='noindex, nofollow'>
# Every page this repo generates today writes name-then-content (1,659 of 1,659
# robots metas in the 2026-09-01 build), but a checker that only recognises the
# shape we happen to emit would pass silently the first time a template or an
# upstream generator emitted the other one — and for the coherence gate that is
# a false PASS, the unsafe direction. So match either order.
NOINDEX_META_RE = re.compile(
    r"""<meta\s+(?=[^>]*\bname\s*=\s*['"]robots['"])"""
    r"""(?=[^>]*\bcontent\s*=\s*['"][^'"]*\bnoindex\b)[^>]*>""",
    re.IGNORECASE,
)

# Any robots meta at all, whatever it says. Used to decide "this page already
# has an explicit directive, leave it alone".
ROBOTS_META_RE = re.compile(
    r"""<meta\s+[^>]*\bname\s*=\s*['"]robots['"][^>]*>""", re.IGNORECASE
)

# A <link rel="canonical"> and its href, in either attribute order.
CANONICAL_LINK_RE = re.compile(
    r"""<link\s+(?=[^>]*\brel\s*=\s*['"]canonical['"])[^>]*>""", re.IGNORECASE
)
HREF_RE = re.compile(r"""\bhref\s*=\s*['"]([^'"]+)['"]""", re.IGNORECASE)

LOC_RE = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>", re.IGNORECASE)
