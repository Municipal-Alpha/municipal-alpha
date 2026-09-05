Title: Geneva, Illinois
Slug: profiles/geneva-il
Sortorder: 11

*This profile is generated from continuous automated monitoring and updates weekly as new documents are published.*

## The Check Register Town

Geneva is a city of ~22,000 people about 40 miles west of Chicago, in Kane County. It has a City Council, a Plan Commission, a Zoning Board of Appeals, a Historic Preservation Commission, a Mental Health Board, a Fire & Police Commission, a Cultural Arts Commission, and about 40 more boards and committees. Suburban Illinois municipal government at its most thorough.

What makes Geneva interesting to us isn't the board count. It's the check registers.

Geneva publishes 250+ accounts payable invoice reports -- detailed, line-item records of every vendor payment the city makes. Our pipeline has resolved entities in those records to 50 distinct publicly-traded companies, with over 1,700 individual entity sightings linked to tickers. This is one city. One set of check registers. Fifty tickers.

| Metric | Value |
|---|---|
| Documents ingested | 1,300+ |
| Document types | 8 (minutes, check registers, agendas, reports, documents, attachments, notices, ordinances) |
| Active boards monitored | 45 |
| Classified signals | 49 (HIGH and MEDIUM) |
| Public company tickers touched | 50 |
| Check registers analyzed | 250+ |
| Entity sightings with tickers | 1,700+ |
| Tower structures registered | 12 |
| Monitoring | Active, continuous |

## What a Check Register Actually Shows

A municipal check register is a list of every payment a city makes to every vendor. Most people's eyes glaze over. Ours don't, because every line item is an entity that can be resolved to a public company.

Here's what Geneva's check registers map to when you run entity resolution at scale. Showing 10 of 50 resolved tickers:

| Entity | Ticker | Sightings | What They're Paying For |
|---|---|---|---|
| AT&T | T | 200+ | Monthly phone service, pedestal installations |
| W.W. Grainger | GWW | 150+ | Industrial supplies, maintenance equipment |
| Comcast | CMCSA | 130+ | Cable service, internet |
| Home Depot | HD | 130+ | Hardware, maintenance supplies |
| Amazon | AMZN | 120+ | Office supplies, electronics, cleaning supplies, server equipment |
| UPS | UPS | 120+ | Shipping |
| Verizon | VZ | 120+ | Communications |
| Core & Main | CNM | 110+ | Water meters, gaskets, pipes |
| Airgas | AIQUY | 100+ | Cylinder rentals, welding supplies |
| NextEra Energy | NEE | 90+ | Electric utility |

That's ten companies, all publicly traded, all receiving regular payments from a single municipality. This is recurring revenue from government operations, visible in public documents that nobody in the market is reading.

Now multiply by 4,500+ municipalities. Then by 19,500.

## Pipeline Activity

| Week | Documents | Boards Active | Signals |
|---|---|---|---|
| Week 1 (backfill) | 1,200+ | 42 | 43 |
| Week 2 | 126 | 8 | 6 |
| Week 3 | 1 | 1 | -- |

Week 1 was the initial backfill -- Geneva has deep archives. The Accounts Payable Invoice Reports alone account for 220+ check registers going back years. This historical depth is the point: it's not just what a city is spending today, it's the longitudinal pattern of who they pay, how much, and whether it's changing.

## Why This Matters for Alt Data

Check registers are the only municipal document type where we've measured positive alpha against the broader market. The signal is straightforward: if a public company is receiving payments from dozens of municipalities that are growing quarter over quarter, that's a revenue signal that isn't in the company's reported numbers yet.

The entity resolution is the hard part. "CORE & MAIN LP" in one check register is the same company as "Core and Main" in another and "C&M" in a third. Our pipeline handles this across 4,500+ municipalities, resolving vendor names to canonical entities and tickers. Geneva alone has 15+ distinct name variants that resolve to the same set of national companies.

One city's check register is a curiosity. A thousand cities' check registers, entity-resolved and longitudinally tracked, is an alternative dataset.

## Infrastructure

Geneva has 12 registered tower structures, more than you'd expect for a city this size. The same records-request-based assessor data acquisition that works in Maine works in Illinois -- different statute (Illinois FOIA), different contact roles, different response patterns. The system adapts.

## The Boring Part That Matters

Showing 6 of 45 monitored boards:

| Board | Minutes | Check Registers | Agendas | Reports | Other |
|---|---|---|---|---|---|
| Committee of the Whole | 252 | -- | 62 | -- | -- |
| Accounts Payable | -- | 220+ | -- | -- | -- |
| City Council | 130 | -- | 59 | -- | -- |
| Plan Commission | 63 | -- | -- | -- | -- |
| Approved Vendor Contracts | -- | 37 | -- | -- | -- |
| Zoning Board of Appeals | 41 | -- | 47 | -- | -- |

The Accounts Payable board alone produces 220+ check registers. The Approved Vendor Contracts board adds another 37 with contract-level detail. That's 250+ documents with line-item vendor payment data from a single city. The Committee of the Whole produces 252 minutes documenting what the city is debating, planning, and approving.

This is the kind of data that's too boring for anyone to read manually and too valuable to ignore.

## So What

Geneva demonstrates what becomes possible when you apply entity resolution to municipal spending data at scale. One check register is a spreadsheet. A thousand check registers, entity-resolved across jurisdictions, is a dataset that tracks public company government revenue in near-real-time from the source documents.

Nobody at Grainger's investor relations desk knows how often Geneva, Illinois pays them. We do. And we know the same thing for every municipality in the pipeline.

---

### Want this data?

Geneva's check register data is a sample of what entity resolution produces at scale. The full dataset spans 4,500+ municipalities and 100+ public tickers.

- **[Download a sample of our signal data (CSV)](/sample-data/signals-sample.csv)** -- 50 entity-resolved signals including Geneva check register entries
- **[See our alt data product](/solutions/alt-data/)** -- how we deliver municipal vendor data
- **[Get entity data for specific tickers](mailto:matt@municipalalpha.com?subject=Alt%20data%20inquiry)** -- tell us which companies you're tracking
