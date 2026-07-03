Title: Methodology
Slug: methodology
Sortorder: 5
Summary: Coverage, data freshness, classification, entity resolution, alpha measurement, and known gaps. How we build structured intelligence from municipal public records.

## Coverage

We have records from 3,900+ municipalities across 50 states (as of July 2026). The United States has 19,500 municipalities. Our coverage is concentrated in New England, the Midwest, and the Mountain West, expanding weekly through automated onboarding.

**What we cover well today:**

- Municipal meeting documents (agendas, minutes, packets) from 3,900+ municipalities
- Check registers and accounts payable data from 200+ municipalities
- Building permits from 400+ municipalities (44,000+ structured records)
- Tower and infrastructure lease data from assessor records (13,000+ sites screened)
- FOAA/FOIA response data from 100+ jurisdictions with active records requests

**Known coverage gaps:**

- County-level data (recorder, probate, assessor) is early stage -- depth in Maine and New Hampshire, limited elsewhere
- Western and Southern states are underrepresented relative to New England and Midwest
- Insurance rate filings and mineral rights data are in pilot phase
- Real-time check register feeds exist for a minority of covered municipalities -- most are periodic via records requests

We are transparent about where our coverage is strong and where it is thin. If you need data from a specific jurisdiction, [ask](/contact/) -- we can often onboard a new municipality in days.

## Data Freshness

The pipeline runs daily. Every covered municipality is crawled, new documents are classified, and entities are resolved against the knowledge graph.

- **Document ingestion:** Daily for web-published documents. Varies for FOAA/FOIA responses (depends on jurisdiction response times, typically 5-10 business days)
- **Signal classification:** Same-day. Documents ingested in the evening crawl are classified and available by morning
- **Entity resolution:** Same-day. New vendor names are matched against the ticker database during classification
- **Tower/infrastructure data:** Weekly census. FCC and FAA cross-referencing runs on a weekly cycle

## Source Types

| Source | Method | Typical Latency |
|---|---|---|
| Municipal agendas and minutes | Automated collection (CivicPlus, Granicus, BoardDocs, custom) | Same-day |
| Check registers / AP data | FOAA/FOIA records requests + web collection where available | 5-30 days (records request) or same-day (web) |
| Building permits | Web collection + records requests | Same-day to 30 days |
| Assessor records | Records requests + GIS portal collection | 5-30 days |
| FCC/FAA tower data | Federal database cross-reference | Weekly |
| Insurance rate filings | State DOI portal collection | Same-day (pilot) |

All data is sourced from publicly available government records or obtained through formal public records requests. We do not access authentication-gated, paywalled, or restricted content. See our [data sourcing policy](/legal/privacy/) for details.

## Classification

Documents are classified by a multi-provider LLM classifier into 14 canonical document types (agenda, minutes, check_register, budget, capital_plan, ordinance, permit, rfp, legislative_document, and others) and assigned an investment priority (HIGH, MEDIUM, LOW).

**Pre-classification noise filtering:** Before the LLM sees a document, a rules-based filter applies 70+ patterns to remove non-signal documents (newsletters, police blotters, election results, blank forms, recreational schedules). Each pattern is derived from data analysis requiring 20+ matching documents with a 0% signal rate. Tower and wireless documents are exempt from noise filtering.

**What "HIGH priority" means:** The document contains information that maps directly to a public company ticker, infrastructure asset, or fiscal health indicator. Examples: a check register payment to a publicly-traded contractor, a tower lease renewal on a planning board agenda, a budget amendment showing a revenue shortfall.

**What the classifier does not do:** It does not make investment recommendations, predict price movements, or assign sentiment. It structures facts from public documents and resolves entities. The signal is the structured data itself.

## Entity Resolution

Vendor names in municipal documents are messy. "Waste Management of Maine," "WM," "Waste Mgmt," and "WASTE MANAGEMENT INC" are the same company (ticker: WM). Our entity resolution system maps these variations to canonical company names and public tickers.

**Two-tier architecture:**

- **Tier 1 (Watchlist):** Curated ticker-company pairs. Exact string matching. High confidence. Primary source for trading signals.
- **Tier 2 (Discovery):** Broader matching against subsidiary names, DBAs, and known aliases. Substring and fuzzy matching. Medium confidence. Stored for validation and portfolio expansion.

Current resolution covers 136 public company tickers across 3,900+ municipalities. Resolution accuracy varies by entity -- large, frequently-appearing companies (AT&T, Verizon, Waste Management) resolve at high accuracy. Smaller or regional companies may not resolve on first appearance and are queued for review.

**Known limitation:** Entity confidence is currently expressed as a tier label, not a numeric probability score. Numeric confidence scoring is planned.

## Investment Vectors

Each classified document is evaluated against 12 proprietary investment vectors spanning vendor relationships, infrastructure assets, regulatory patterns, real estate dynamics, and fiscal health indicators. A single document may generate signals across multiple vectors.

Vector definitions and example signals are available under NDA. [Contact us](/contact/?subject=Investment%20vector%20details) to learn more.

## Alpha Measurement

We measure the relationship between our signals and subsequent stock returns. This section describes the methodology for transparency, not as a performance guarantee.

**Approach:** For each signal with a resolved ticker, we compute excess returns over SPY and sector-specific ETFs at 1, 2, 4, 8, and 12-week horizons.

**Document-level deduplication:** A single check register may mention 10+ companies. Treating each ticker-document pair as independent inflates sample size and overstates significance. We compute the median excess return per document, yielding one observation per document. Both raw pair counts and effective n (unique documents) are reported.

**Statistical framework:** t-statistics, Sharpe ratios, and excess returns computed per document type and vector. Significance threshold: |t| >= 2.0 (approximately 95% confidence).

**Current status:** Preliminary results show statistically significant positive excess returns for legislative documents, capital plans, and budgets at short horizons. Check registers show slightly negative excess returns after proper deduplication -- an earlier analysis that did not deduplicate at the document level overstated their effect. Results are based on limited history and should be treated as preliminary.

A detailed methodology paper is available on request for quantitative analysts evaluating the data. [Contact us](/contact/).

## Quality Controls

- **Automated expectations:** Minimum active municipalities, signal volume stability, valid classification rates, entity extraction rates -- checked after every daily run
- **Regression testing:** Golden set of 80+ pre-classified signals verified after any classifier, navigator, or schema change
- **Noise filter validation:** Every pattern requires 20+ matching documents with 0% signal rate before deployment
- **Self-healing pipeline:** Automated health checks, structural drift detection, and remediation

## Data Security & Handling

All data originates from publicly available government records or formal public records requests. No authentication-gated, paywalled, or restricted sources.

- **Encryption:** Data delivered via encrypted channels (HTTPS, encrypted email, or secure file transfer)
- **No PII in delivered datasets:** Delivered data products contain business entities, government records, and public filings. Private citizen PII is not included in delivered datasets beyond what appears in public government records (e.g., property owner names in public tax rolls)
- **Access control:** Data licensing agreements govern access. No self-service access to raw data without agreement
- **Infrastructure:** Pipeline runs on dedicated infrastructure with daily encrypted backups
- **Confidentiality:** Coverage requests, evaluation data, and client identity are treated as confidential. NDA available on request

For questions about data handling or security requirements, [contact us](/contact/).

## What We Don't Do

- We don't access paywalled or subscription-only data sources
- We don't use social media, news, or web traffic data
- We don't make investment recommendations or predictions
- We don't sell data that isn't derived from public records
- We don't access non-public government systems -- everything we structure is published by governments for public consumption or obtained through formal records requests

## Data Dictionary

A complete data dictionary covering all data products (signals, entity sightings, municipal receivables, permit records, tower/infrastructure data, contagion events) is available on request. Each field includes type, description, update frequency, and example values.

[Request the data dictionary](/contact/?subject=Data%20dictionary%20request)

## Questions About Our Data

If you want to understand our coverage for a specific jurisdiction, entity, or data type, reach out. We'll tell you exactly what we have and what we don't.

**Email:** [matt@municipalalpha.com](mailto:matt@municipalalpha.com?subject=Data%20methodology%20question)
