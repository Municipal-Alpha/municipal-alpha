Title: How It Works
Slug: how-it-works
Sortorder: 4

<!-- IMAGE DROPPED 2026-07-02 (interim per open-items graphics-cleanup item): AI-generated PNG rendered literal hex codes / garbled labels. Restore when regenerated to deck brand. Was: ![Data Layer Stack: a query enters through four data layers (Federal, County, Municipal, FOAA) and returns as  -->

## Precursor Intelligence from a Knowledge Graph

The precursor documents that predict market events -- vendor payments, planning board votes, budget approvals, assessor records -- sit on 19,500 town hall websites. Reading any one is easy. Reading all of them, every day, structuring them into entities and relationships, and connecting signals across jurisdictions -- that's the system.

It is a knowledge graph: entities, types, properties, and the relationships between them, continuously growing as new documents are ingested. Every municipality added, every document parsed, every entity resolved adds nodes and edges to the graph. Different data types from different jurisdictions connect into a unified picture because the graph connects them.

## How a Parcel Connects Everything

<!-- IMAGE DROPPED 2026-07-02 (interim per open-items graphics-cleanup item): AI-generated PNG rendered literal hex codes / garbled labels. Restore when regenerated to deck brand. Was: ![Diagram showing a single parcel connected to five data sources: Assessor Records, FCC Registry, FAA Database -->

A single parcel in Falmouth, Maine appears in:

- **Assessor data** -- tower lease, landowner identity, property valuation
- **FCC registry** -- tower tenant (American Tower, Crown Castle, etc.)
- **FAA filing database** -- construction permit, tower height, coordinates
- **Municipal check register** -- lease payment to landowner, amount, frequency
- **Planning board agenda** -- zoning variance, public hearing, conditions

Each source adds nodes and edges to that parcel's place in the graph. None is complete alone. Together, they produce a lead that no single-source competitor can match.

## How an Entity Connects Everything

An entity like American Tower appears in assessor records across 50 states, FCC registrations nationwide, FAA filings, municipal RFPs, insurance rate filings (tower liability coverage), and county recorder mineral lease assignments. Each appearance enriches the entity's node in the graph, connecting it to new jurisdictions, new document types, new relationships.

Resolving "Waste Management of Maine" to ticker WM in AP data simultaneously improves entity resolution for insurance rate filings, permit data, and contract tracking. One resolution, four graph improvements.

## How a Jurisdiction Connects Everything

A single jurisdiction like Cumberland County, Maine produces assessor data (tower + solar + utility leases), probate filings (estate property transfers), recorder data (mineral rights, if applicable), municipal spending (AP + permits), and insurance territory data. All from one county.

Every new jurisdiction added to the pipeline activates data for every active vertical simultaneously. The graph gets denser, and denser graphs produce better intelligence.

## Why 19,500 Municipalities <!-- metrics-ok: total US municipalities, not our coverage -->

The big data vendors cover New York and Chicago. Nobody is reading the 19,500 small and mid-sized municipalities that issue the same building permits, check registers, and assessor records -- just on worse websites, behind more obscure FOIA statutes. That's where the precursor signals are least picked-over.

Nobody else reads Gorham, Maine. Or Pocatello, Idaho. Or the thousands of other towns where the finance director posts a check register to a CivicPlus portal and nobody outside city hall ever looks at it. Those check registers contain vendor payment data that precedes quarterly earnings reports, just at the local level, where 19,500 jurisdictions spend a combined $3.9 trillion annually. <!-- metrics-ok: total US -->

The coverage gap is the product.

**Where the system is today (as of July 2026):**

- **4,500+** municipalities monitored daily, all 50 states
- **1,184,000+** documents ingested and classified
- **44,000+** building permits structured
- **100+** public company tickers resolved from municipal vendor names
- **444,000+** classified signals
- Adding new municipalities weekly, with infrastructure built to scale past 5,000

**Where this goes:**

- **19,500** US municipalities issuing these same records
- **~1.5M** building permits issued nationally per year (Census Bureau)
- **$3.9T** in annual municipal government spending (Census of Governments)
- **$4T** municipal bond market
- **130,000+** FCC-registered tower structures

The marginal cost of adding a municipality is near zero once the CMS connector exists. Six connector platforms cover the majority of US municipal websites.

## The Dark Document Problem

You can Google for municipal documents. You can ask an AI agent to find them. You will miss almost everything.

We tested this. Across a sample of municipalities where we have deep coverage, roughly 99% of the documents in our database exist at URLs with no public navigation link. They are stored in the content management system, they are public record, but no menu points to them. No sitemap lists them. No search engine has ever seen them.

This is not a search engine problem. It is a platform architecture problem. The six CMS vendors that power most US municipal websites store documents in flat file directories and sequential archive IDs. A town clerk uploads a check register to the portal, it gets a URL like `/ArchiveCenter/ViewFile/Item/4605`, and that URL is never linked from any navigation page. The document exists. It is public. It is invisible.

Google indexes what it can find through links. AI agents browse the same public-facing pages Google does. Neither has any way to discover a document that the CMS stored but never surfaced. In one Maine city, we found 3,600+ documents, all stored in a deep upload directory with no inbound links from the site's navigation. Planning board agendas, septic permits, zoning documents, all public record, all effectively dark.

This is why scraping municipal websites the normal way produces almost nothing. The navigation tree shows what the CMS vendor's default menu structure exposes. The actual document store is orders of magnitude larger. Our connectors understand how each platform stores data internally, not just what it shows visitors.

For data teams, research firms, and AI companies building on public records: the documents you are missing are not behind a paywall or a login. They are sitting on a public server at a URL that nothing links to. We know where they are because we built connectors for each platform, not a general-purpose web crawler.

## Could You Build This Yourself?

You should ask. The AI classification step is a commodity, and the honest answer depends on your footprint. The expensive parts aren't the AI, they're the registry of where each of thousands of towns actually publishes, the OCR on scanned PDFs, the connector repairs every time a portal changes, and the history no new build can produce. We published [the evaluation prompt we hand buyers](/build-vs-buy/) so you can run the build-vs-buy analysis yourself, against your whole exposed footprint, before you pay us a dollar.

## The Recipe Library

The agents share a growing library of learned approaches, what we call recipes. A recipe is a proven combination: this source type, plus this extraction method, applied in this context, delivered to this buyer segment. Some recipes were designed. Most were discovered, the system tried something, it worked, it got recorded. Recipes that work three or more times get promoted to playbooks. The library grows with every jurisdiction touched, every FOIA response processed, every edge case solved. What changes per vertical is the recipe, not the infrastructure.

| Agent Capability | Verticals It Serves |
|---|---|
| FOIA/FOIL/OPRA filing (state-adapted) | All verticals |
| Government portal discovery + scraping | All verticals |
| Document classification (LLM-based) | Alt data, insurance, probate |
| Entity resolution (vendor/company names) | Alt data, insurance |
| Parcel screening + owner resolution | Tower leases, mineral rights |
| Chain-of-title tracing | Mineral rights, probate |
| Format auto-detection + parsing | All verticals |
| Lead scoring + qualification | Tower leases, mineral rights, probate |
| Cross-reference with federal databases | Tower (FCC/FAA), mineral (BLM), insurance (NAIC) |

## Automated Public Records Requests

Most valuable government data isn't on a website. Assessor records, detailed check registers, and permit databases usually require a formal public records request -- FOIA at the federal level, but every state has its own statute with its own rules, deadlines, contact roles, and fee structures. Maine calls it FOAA. New Hampshire calls it Right-to-Know. New York calls it FOIL.

The platform files these requests autonomously, adapted to each state's statute. But the real advantage isn't the filing -- it's the learning. Over hundreds of requests, the system tracks which contact roles respond (town clerks vs. assessors vs. finance directors), which email formats get through, which request language produces usable data vs. form-letter denials, optimal cooling periods between follow-ups, and which towns respond to the first request vs. the third. Every interaction is scored. Successful patterns propagate to similar jurisdictions automatically. Failed approaches get deprioritized.

A competitor can read the statute. They can't replicate what we've learned from the responses.

## Building Permits as a Signal Source

Building permits are one of the most underrated public data sources. Every commercial construction project, infrastructure upgrade, and development phase starts with a permit. The data tells you which contractors are winning work, which developers are active in a geography, where infrastructure spending is accelerating, and how local construction activity maps to public company revenue -- months before any of it shows up in earnings or analyst reports.

Small and mid-sized municipalities issue the same permits as large cities, just on worse websites with less standardization. That's where the coverage gap is widest. We monitor 4,500+ municipalities and structure the permit records they publish into entity- and ticker-resolved time series, 44,000+ records and growing.

## The Pipeline

<!-- IMAGE DROPPED 2026-07-02 (interim per open-items graphics-cleanup item): AI-generated PNG rendered literal hex codes / garbled labels. Restore when regenerated to deck brand. Was: ![Diagram showing the self-improving pipeline cycle: Crawl, Classify, Score, Improve, Learn]({static}/images/p -->

The system runs daily, autonomously. It crawls municipal portals, classifies documents, resolves entities to public company tickers, scores signals, and delivers qualified leads. Self-healing automation detects when a municipality changes its website and adapts. A reward-based learning system tracks which automated actions succeed and evolves strategy over time. When a fix works for one town, the system propagates it to similar towns with decaying confidence by similarity.

The pipeline doesn't just collect data. It files records requests, processes responses, follows up on non-responses, onboards new jurisdictions, retrains its own classifiers, and evaluates the business value of every action it takes. Every day it runs, it gets better at locating things.

## What "Gets Better" Means

A landowner in an unorganized territory in northern Maine sits on a cell tower lease worth $50,000 a year. The tower does not appear in the FCC's standard registration database. There is no municipal assessor, no town website, no CMS platform to scrape. The system found it anyway, by combining an FCC land mobile license, an FAA obstruction filing, a trail database entry for "Cell Tower Access Road," USGS elevation data showing the only viable ridge in the area, and a state unorganized territory tax roll. Five sources, none sufficient alone, each one a recipe the system learned from a previous dead end somewhere else.

That is what getting better means. Not faster hardware or bigger databases, more recipes for locating things that nobody else is looking for.
