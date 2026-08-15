Title: About
Slug: about
Sortorder: 4

## The Shift

Every day, 19,500 town halls in America publish documents that predict market events weeks or months before they happen. Vendor payments that precede earnings reports. Planning board votes that precede building permits. Budget approvals that precede RFPs. Rating agency downgrades that are visible in spending data months early.

The documents have always been public. They were just scattered across thousands of websites in incompatible formats, and the cost of reading them all exceeded the value of reading any one. That changed. I built a system that reads them all, every day, and tells you what's about to happen.

You see the thing before it becomes a thing.

## The Problem Everyone Has (and Nobody Notices)

Everyone in the market operates on published events -- posted RFPs, rating changes, earnings surprises, lease listings. The precursor documents that produce those events sit unread on town hall websites. Your competitors are in the same position, so nobody notices they're all late. It feels normal. It's just not necessary anymore.

The big data vendors cover New York and Chicago. Nobody is systematically reading Gorham, Maine or Franklin, New Hampshire. But small and mid-sized municipalities issue the same building permits, the same check registers, the same assessor records as large cities -- just on worse websites, with less standardization, behind more obscure FOIA statutes. That's where the gap is widest and the signal is least picked-over.

## How the System Learns

The system is good at finding things because it has spent a year learning the system it operates in. Which CMS platforms hide documents behind JavaScript. Which FOIA statutes require which language. Which assessor offices respond to email and which require certified mail. Which board names mean "check registers" in which towns. None of this was designed upfront. It was learned through contact with 4,300+ jurisdictions, thousands of FOIA interactions, and hundreds of dead ends that each taught the system something. Every interaction produces a recipe. The recipes accumulate.

## Two Precedents

**The business model:** The Echo Nest built a structured understanding of music from fragmented public sources. No single source was complete. But by ingesting everything, structuring it, and building intelligence on top, they created the canonical layer that Spotify, Pandora, and the rest of the streaming industry built on top of. Multiple revenue streams on one underlying data asset. The Echo Nest was acquired by Spotify for ~$100M in 2014. That business model, applied to US public records, is what I am building.

**The technical architecture:** Google acquired Metaweb in 2010 to get Freebase, a knowledge base that structured the messy open web into entities and relationships. That became the Google Knowledge Graph. The insight: structured relationships between entities are more valuable than the raw documents that contain them. Municipal Alpha is a knowledge graph of US public records -- entities, relationships, and the precursor signals they produce.

## The Scale of What's Unread

| What exists nationally | Volume | What's structured today |
|---|---|---|
| US municipalities | 19,500 | 4,300+ monitored daily |
| Building permits issued annually | ~1.5 million (Census Bureau) | 44,000+ structured in our pipeline |
| Annual municipal government spending | $3.9 trillion (Census of Governments) | Vendor payments from 230+ towns, 100+ resolved tickers |
| Municipal bond market | $4 trillion (SIFMA) | Credit signals from source spending documents |
| FCC-registered tower structures | 130,000+ | 5,400+ screened with parcel cross-reference |
| Municipal infrastructure investment gap | $2.6 trillion (ASCE) | Deferred maintenance signals from spending patterns |

These records all exist as public documents. The acquisition cost has been too high for anyone to aggregate them. Six CMS connector platforms cover the majority of US municipal websites, and the marginal cost of adding a municipality is near zero once the connector exists. Every new municipality added produces precursor data for every active vertical simultaneously.

## Revenue Verticals

Applications built on the knowledge graph, not separate businesses.

| Vertical | Data Source | Buyer | Status |
|---|---|---|---|
| Infrastructure lease intelligence | Municipal assessor records + FCC/FAA | Tower REITs, aggregators, solar/wind developers | Pilot live |
| Municipal alternative data | Municipal AP, permits, agendas | Hedge funds, permit aggregators | Signal validated |
| Insurance rate filing intelligence | State DOI filing portals | Hedge funds, insurers, research | Ready to build |
| Mineral rights intelligence | County recorder deeds + state O&G commissions | Mineral aggregators, energy PE | Ready to build |
| Probate & estate intelligence | County probate courts | Wealth mgmt, RE investors, PE | Ready to build |

## The Compounding Effect

![Diagram showing one jurisdiction at top funneling into multiple revenue verticals below]({static}/images/compounding-effect.png)

Two things compound in this system, and the second one is less obvious. The data compounds: more jurisdictions, more documents, more cross-references, more history. But the operational intelligence also compounds. Every FOIA interaction teaches the system something about that jurisdiction. Every failed crawl produces a recipe for the next attempt. Every edge case solved becomes available to every future jurisdiction. The system does not just get bigger. It gets better at locating things.

- One FOIA request to a municipal assessor produces tower lease leads, solar lease leads, property tax signals, AND feeds alt data scoring. Five products from one acquisition.
- One entity resolution ("Waste Management of Maine" resolves to ticker WM) simultaneously improves insurance rate filing data, permit tracking, and contract award detection.
- One new jurisdiction activates documents for alt data, parcels for infrastructure screening, jurisdiction coverage for insurance territory mapping, and a new court for probate monitoring. And it onboards faster than the last one, because the recipe library is larger.
- One dead end: the FCC tower registration database missed a $50K/year tower lease in rural Maine. That dead end produced a recipe combining ULS licenses, FAA filings, trail databases, and elevation data. That recipe now applies to every rural tower search, not just the one that produced it.

The cost of acquiring a jurisdiction is paid once. The revenue is collected from every vertical that uses it. And the recipe learned from acquiring it makes the next acquisition cheaper.

## The Moat

The mess is why nobody starts. The recipes are why nobody catches up.

- **Recipes compound faster than data.** The data asset grows linearly with jurisdictions covered. The recipe library grows combinatorially, because a recipe learned in one context often applies in others. The recipe for extracting tower data from unorganized territories came from combining five techniques each learned in a different jurisdiction. A competitor would need to hit those same dead ends to develop the same recipe.
- **Time is the ingredient you cannot buy.** The system knows which FOIA language works in Maine vs New Hampshire, which assessor offices send Vision caidump format vs custom exports, which CMS platforms require JavaScript rendering, which board names correspond to financial data in which towns. This is not infrastructure. It is accumulated operational intelligence. It took a year of daily interactions to learn. A well-funded competitor starting today starts with zero recipes.
- **The work is unglamorous.** Nobody wants to parse 15 assessor data formats, navigate 50 state FOIA statutes, build connectors for 6 CMS platforms, or trace mineral title chains through 100-year-old deeds. This is exactly the kind of messy, real-world work that well-funded competitors find unappealing. That is fine. I like it here.
- **Cross-domain recipes transfer.** A FOIA playbook developed for Maine municipal assessors applies to Maine school districts and special districts too, same statute, same language. A CMS connector built for one CivicPlus municipality works for hundreds. Every new domain entered activates recipes already in the library.

## The Team

Municipal Alpha is built and operated by Matt MacDonald.

Previously: Chief Product Officer at Acast (podcast infrastructure, $200M revenue, NASDAQ IPO), co-founder of RadioPublic (raised $3.5M, grew to acquisition). Two decades building data products from fragmented, unstructured sources at scale, first in audio, now in public records.

The pipeline runs autonomously: 4,300+ municipalities crawled daily, documents classified and entity-resolved same-day, self-healing infrastructure that detects and adapts to website changes without human intervention. One person built it. The automation operates it.

Embedded at the Roux Institute NSIH (National Security Innovation Hub, Northeastern University, Portland ME).

**[Book a data review](https://calendar.app.google/HkZk29hxj7Cdtvuc9)** or email [matt@municipalalpha.com](mailto:matt@municipalalpha.com).
