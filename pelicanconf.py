import json
from pathlib import Path

# Load metrics from data file (auto-updated weekly by VPS)
_metrics_file = Path(__file__).parent / "data" / "metrics.json"
if _metrics_file.exists():
    with open(_metrics_file) as f:
        METRICS = json.load(f)
else:
    METRICS = {
        "municipalities": "2,100+",
        "states": "50",
        "documents": "309,000+",
        "signals": "57,000+",
        "tower_sites": "4,700+",
        "permits": "43,000+",
        "tickers": "100+",
        "updated": "2026-03-29",
    }

# Site-redesign content data (2026-08-31) — sector-page and case-studies-hub
# copy, mirrors the METRICS loading pattern above. See
# docs/plans/site-redesign-implementation.md in muni-scraper for the build spec.
def _substitute_metrics_tokens(obj, metrics):
    """Recursively replace {{METRICS_<KEY>}} tokens in string values so
    corpus-scale figures in data/sectors.json stay pinned to the live
    data/metrics.json rather than drifting as separate hardcoded literals."""
    if isinstance(obj, dict):
        return {k: _substitute_metrics_tokens(v, metrics) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_substitute_metrics_tokens(v, metrics) for v in obj]
    if isinstance(obj, str):
        for key, value in metrics.items():
            obj = obj.replace("{{METRICS_" + key.upper() + "}}", str(value))
        return obj
    return obj


_sectors_file = Path(__file__).parent / "data" / "sectors.json"
with open(_sectors_file) as f:
    _sectors_data = json.load(f)
SECTORS = _substitute_metrics_tokens(_sectors_data["sectors"], METRICS)
SECTOR_ORDER = _sectors_data["order"]

_case_studies_file = Path(__file__).parent / "data" / "case_studies.json"
with open(_case_studies_file) as f:
    _case_studies_data = json.load(f)
CASE_STUDIES = _case_studies_data["articles"]
CASE_STUDY_ORDER = _case_studies_data["order"]

AUTHOR = "Municipal Alpha"
SITENAME = "Municipal Alpha"
SITEURL = ""
SITESUBTITLE = "A Knowledge Graph of US Public Records"

PATH = "content"
THEME = "theme/municipal-alpha"

TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

# No blog feed until we have articles
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pages config
PAGE_ORDER_BY = "sortorder"
DISPLAY_PAGES_ON_MENU = True

# No blogroll or social links yet
LINKS = ()
SOCIAL = ()

DEFAULT_PAGINATION = False

# Markdown extensions -- toc adds heading IDs for anchor links
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.toc": {"permalink": False},
        "markdown.extensions.tables": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

# Static paths
STATIC_PATHS = ["images", "extra/CNAME", "extra/sample-data", "extra/case-studies", "extra/decks", "extra/robots.txt", "extra/brand-review", "extra/materials-periodic-table", "extra/hipcamp", "extra/favicon.ico", "extra/favicon-32.png", "extra/apple-touch-icon.png"]
# Prevent Pelican from treating HTML in extra/ as content
READERS = {"html": None}
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/sample-data/tower-prospects-sample.csv": {"path": "sample-data/tower-prospects-sample.csv"},
    "extra/sample-data/signals-sample.csv": {"path": "sample-data/signals-sample.csv"},
    "extra/sample-data/credit-sample.csv": {"path": "sample-data/credit-sample.csv"},
    "extra/sample-data/contractor-signals-sample.csv": {"path": "sample-data/contractor-signals-sample.csv"},
    "extra/sample-data/infrastructure-risk-sample.csv": {"path": "sample-data/infrastructure-risk-sample.csv"},
    "extra/sample-data/connell-redev-sample-2026-03-27.pdf": {"path": "sample-data/connell-redev-sample-2026-03-27.pdf"},
    "extra/sample-data/simon-redev-sample-2026-03-27.pdf": {"path": "sample-data/simon-redev-sample-2026-03-27.pdf"},
    "extra/sample-data/sw-cole-infrastructure-sample-2026-03-27.pdf": {"path": "sample-data/sw-cole-infrastructure-sample-2026-03-27.pdf"},
    "extra/sample-data/desri-energy-sample-2026-03-28.pdf": {"path": "sample-data/desri-energy-sample-2026-03-28.pdf"},
    "extra/sample-data/amt-combined-alert-2026-03-28.html": {"path": "sample-data/amt-combined-alert-2026-03-28.html"},
    "extra/case-studies/amherst-nh-procurement-chain.pdf": {"path": "case-studies/amherst-nh-procurement-chain.pdf"},
    "extra/case-studies/infrastructure-equity-signals.pdf": {"path": "case-studies/infrastructure-equity-signals.pdf"},
    "extra/case-studies/muni-credit-early-warning.pdf": {"path": "case-studies/muni-credit-early-warning.pdf"},
    "extra/case-studies/geneva-il-vendor-payments.pdf": {"path": "case-studies/geneva-il-vendor-payments.pdf"},
    "extra/case-studies/waste-management-entity-resolution.pdf": {"path": "case-studies/waste-management-entity-resolution.pdf"},
    "extra/case-studies/solar-siting-moratorium-to-permit.pdf": {"path": "case-studies/solar-siting-moratorium-to-permit.pdf"},
    "extra/case-studies/hartford-vt-pfas-chain.pdf": {"path": "case-studies/hartford-vt-pfas-chain.pdf"},
    "extra/decks/municipal-alpha-overview-deck-v4.pdf": {"path": "decks/municipal-alpha-overview-deck-v4.pdf"},
    "extra/brand-review/index.html": {"path": "brand-review/index.html"},
    "extra/materials-periodic-table/index.html": {"path": "materials-periodic-table/index.html"},
    "extra/hipcamp/index.html": {"path": "hipcamp/index.html"},
    "extra/brand-review/expressive-particle-dark-v3.png": {"path": "brand-review/expressive-particle-dark-v3.png"},
    "extra/brand-review/wordmark-dark.png": {"path": "brand-review/wordmark-dark.png"},
    "extra/brand-review/wordmark-light.png": {"path": "brand-review/wordmark-light.png"},
    "extra/brand-review/wordmark-tagline-dark.png": {"path": "brand-review/wordmark-tagline-dark.png"},
    "extra/brand-review/wordmark-tagline-light.png": {"path": "brand-review/wordmark-tagline-light.png"},
    "extra/brand-review/mark-dark.png": {"path": "brand-review/mark-dark.png"},
    "extra/brand-review/mark-light.png": {"path": "brand-review/mark-light.png"},
    "extra/brand-review/icon-square-dark.png": {"path": "brand-review/icon-square-dark.png"},
    "extra/brand-review/icon-square-light.png": {"path": "brand-review/icon-square-light.png"},
    "extra/brand-review/wordmark-nav.png": {"path": "brand-review/wordmark-nav.png"},
    "extra/brand-review/downloads/wordmark-white-transparent.png": {"path": "brand-review/downloads/wordmark-white-transparent.png"},
    "extra/brand-review/downloads/wordmark-ink-transparent.png": {"path": "brand-review/downloads/wordmark-ink-transparent.png"},
    "extra/brand-review/downloads/wordmark-black-transparent.png": {"path": "brand-review/downloads/wordmark-black-transparent.png"},
    "extra/brand-review/downloads/wordmark-tagline-white-transparent.png": {"path": "brand-review/downloads/wordmark-tagline-white-transparent.png"},
    "extra/brand-review/downloads/wordmark-tagline-ink-transparent.png": {"path": "brand-review/downloads/wordmark-tagline-ink-transparent.png"},
    "extra/brand-review/downloads/wordmark-tagline-on-ink.png": {"path": "brand-review/downloads/wordmark-tagline-on-ink.png"},
    "extra/brand-review/downloads/wordmark-tagline-on-paper.png": {"path": "brand-review/downloads/wordmark-tagline-on-paper.png"},
    "extra/brand-review/downloads/mark-white-transparent.png": {"path": "brand-review/downloads/mark-white-transparent.png"},
    "extra/brand-review/downloads/mark-ink-transparent.png": {"path": "brand-review/downloads/mark-ink-transparent.png"},
    "extra/brand-review/downloads/mark-black-transparent.png": {"path": "brand-review/downloads/mark-black-transparent.png"},
    "extra/brand-review/downloads/icon-ink-512.png": {"path": "brand-review/downloads/icon-ink-512.png"},
    "extra/brand-review/downloads/icon-signal-512.png": {"path": "brand-review/downloads/icon-signal-512.png"},
    "extra/brand-review/downloads/icon-edge-512.png": {"path": "brand-review/downloads/icon-edge-512.png"},
    "extra/brand-review/downloads/icon-paper-512.png": {"path": "brand-review/downloads/icon-paper-512.png"},
    "extra/brand-review/downloads/favicon-64.png": {"path": "brand-review/downloads/favicon-64.png"},
    "extra/brand-review/downloads/expressive-particle-dark.png": {"path": "brand-review/downloads/expressive-particle-dark.png"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/favicon-32.png": {"path": "favicon-32.png"},
    "extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
}

# Clean URLs
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

# Landing page is custom index.html template at root
# Article listing (if any) goes to /blog/
INDEX_SAVE_AS = "index.html"

# Build-time generated artifacts (regenerate on every `make publish`, so they
# never drift from content/metrics):
#   - sitemap.xml : loops `pages` + `articles` (hidden pages auto-excluded).
#                   Advertised in extra/robots.txt; submit in Google Search Console.
#   - llms.txt    : metrics from data/metrics.json (METRICS) + product/story lists
#                   looped from the page collection. Replaces the old static
#                   content/extra/llms.txt.
DIRECT_TEMPLATES = ["index", "sitemap", "llms"]
SITEMAP_SAVE_AS = "sitemap.xml"
LLMS_SAVE_AS = "llms.txt"
