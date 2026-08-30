PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

.PHONY: html clean serve publish copy-static-html noindex-extra goatcounter-extra llms-full metrics-drift no-diffview

html: metrics-drift
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
	$(MAKE) copy-static-html
	$(MAKE) noindex-extra
	$(MAKE) goatcounter-extra
	$(MAKE) llms-full
	$(MAKE) no-diffview

clean:
	rm -rf $(OUTPUTDIR)

serve: html
	cd $(OUTPUTDIR) && $(PY) -m http.server 8000

publish: metrics-drift
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	$(MAKE) copy-static-html
	$(MAKE) noindex-extra
	$(MAKE) goatcounter-extra
	$(MAKE) llms-full
	$(MAKE) no-diffview

# Fail the build when a content page carries a platform-scale claim (N
# municipalities / documents / signals / tickers) that diverges from
# data/metrics.json. Content pages hardcode their numbers (only the homepage
# template + llms.txt read METRICS), so without this gate corpus-scale claims
# silently drift as the pipeline grows. See tools/check_metrics_drift.py
# header for pass rules, thresholds, and the `metrics-ok` waiver.
metrics-drift:
	$(PY) tools/check_metrics_drift.py

# Inject <meta name="robots" content="noindex"> into the unlinked standalone
# pages under content/extra/ (prospect/buyer pages, dispatches, decks). They are
# absent from sitemap.xml and unlinked, so without noindex they are protected
# only by obscurity. Runs after copy-static-html so it sees the copied output.
# Scoped to content/extra-derived pages only — never touches public Pelican
# pages. See tools/inject_noindex.py header for the full rationale.
noindex-extra:
	$(PY) tools/inject_noindex.py

# Inject the GoatCounter loader <script> into the content/extra standalone pages.
# They bypass base.html (which carries the loader on public Pelican pages), so
# without this they record no pageviews and their on-page depth-event JS no-ops.
# Runs after copy-static-html so it sees the copied output. Byte-identical loader
# to base.html. See tools/inject_goatcounter.py header for the full rationale.
goatcounter-extra:
	$(PY) tools/inject_goatcounter.py

# Generate output/llms-full.txt (full-text concatenation for AI agents) from the
# freshly-built output. Runs after pelican + copy-static-html on every build.
llms-full:
	$(PY) tools/build_llms_full.py

# Copy standalone HTML pages from content/extra/ to output/.
# Pelican's READERS = {"html": None} setting skips HTML in STATIC_PATHS,
# so these need to be copied manually post-build. Each entry pairs a
# source HTML in content/extra/<dir>/index.html with output/<dir>/index.html.
copy-static-html:
	@for d in how-this-company-runs brand-review materials-periodic-table hipcamp verizon towers discussion-our-katahdin-2026-05-28 our-katahdin-watchlist our-katahdin-pilot discussion-desri-svedlow discussion-desri-nicc-johnson discussion-desri-backtrack discussion-maine-redevelopment discussion-maine-chamber discussion-oskar-serrander-2026-06-01 discussion-ready-net discussion-kite-realty discussion-new-leaf-energy discussion-ac-power discussion-ct-mirror discussion-john-davidow discussion-schola discussion-invoicecloud for-newsrooms discussion-verogy discussion-cianbro discussion-woodard-curran discussion-aec-water-wastewater discussion-tower-siting discussion-solar-storage discussion-column dispatch-connell discussion-smpdc discussion-gpcog discussion-smpdc-gpcog discussion-housing-read discussion-isom discussion-point-and-pay isom-backtraces newsroom-black-by-god newsroom-appalachia-mid-south aec-before-the-rfp syncarpha syncarpha-storage syncarpha-pilot column-pilot overview-v4 partners trending-maine ebikes-maine window-solar window-tower window-datacenter window-aec; do \
		if [ -f $(INPUTDIR)/extra/$$d/index.html ]; then \
			mkdir -p $(OUTPUTDIR)/$$d ; \
			cp $(INPUTDIR)/extra/$$d/index.html $(OUTPUTDIR)/$$d/index.html ; \
			echo "Copied $$d/index.html" ; \
		fi ; \
	done
	@for d in qa-startup-maine-2026-05-18 ai-in-action ready-net-pilot mtln-pilot katahdin-salmon research-mtln-2026-08-29 towns topics scope; do \
		if [ -d $(INPUTDIR)/extra/$$d ]; then \
			mkdir -p $(OUTPUTDIR)/$$d ; \
			cp -R $(INPUTDIR)/extra/$$d/. $(OUTPUTDIR)/$$d/ ; \
			echo "Copied $$d/ (recursive)" ; \
		fi ; \
	done

# Refuse to publish a review-scaffolding page. annotate_html_diff.py renders a
# page with its changes highlighted for reading; that artifact carries a legend
# and a nav script and is not the page. The generator already refuses to write
# inside a git tree; this is the detector half, run against the BUILT output
# because that is what Pages serves. See tools/check_no_diffview.py.
no-diffview:
	$(PY) tools/check_no_diffview.py $(OUTPUTDIR)
