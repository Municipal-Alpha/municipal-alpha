Title: The Company That Shows Up in 123 Towns
Slug: research/company-footprint
Sortorder: 21
Header_image: story-company-footprint.png
Summary: Entity resolution across 3,900+ municipalities reveals which public companies have the deepest municipal government footprint.

*Analysis based on entity resolution across 3,900+ municipalities.*

## Municipal Government Revenue Is Hiding in Plain Sight

Every municipality in America pays vendors. Phone companies, waste haulers, equipment suppliers, software providers, utilities. These payments are recorded in public documents -- check registers, budgets, RFPs, contracts, meeting minutes. The documents are public. The vendors are often publicly traded. And nobody is connecting the dots at scale.

We are. Our pipeline resolves vendor names to public company tickers across 3,900+ municipalities. The result is a dataset that shows which companies have the deepest municipal government footprint in America, sourced from the actual payment records.

## The Scale

The dataset is growing as the pipeline expands coverage. Every new municipality brings its own vendor relationships, and every vendor relationship that maps to a public company enriches the dataset. The total entity sighting count is in the tens of thousands and growing rapidly as we onboard new jurisdictions and backfill their document archives.

The compounding is fast.

## The Top 10

Showing 10 of 136 resolved tickers:

| Company | Ticker | Municipalities | Sightings |
|---|---|---|---|
| American Tower | AMT | 120+ | 200+ |
| AT&T | T | 115+ | 1,900+ |
| Crown Castle | CCI | 115+ | 380+ |
| Verizon | VZ | 110+ | 6,100+ |
| Waste Management | WM | 100+ | 2,000+ |
| Comcast | CMCSA | 95+ | 3,300+ |
| T-Mobile | TMUS | 85+ | 1,300+ |
| Tyler Technologies | TYL | 85+ | 1,100+ |
| Charter Communications | CHTR | 75+ | 1,700+ |
| Algonquin Power | AQN | 70+ | 2,000+ |

Verizon appears in 110+ municipalities with 6,100+ individual sightings -- check register payments, RFP mentions, contract references, budget line items. That's recurring government revenue from the actual source documents.

And this is from 3,900+ municipalities. The United States has 19,500.

## What the Breadth Tells You

The companies at the top of this list aren't surprising. Of course municipalities pay AT&T and Waste Management. But the data gets interesting in the details:

**Telecom is the deepest municipal vertical.** The top three non-tower companies by municipal footprint are AT&T (118 towns), Verizon (113), and Comcast (97). Municipal telecom spending is operationally recurring, budget-resistant, and growing (broadband mandates, public safety networks, IoT infrastructure). This is not discretionary spend.

**Tyler Technologies is in 85+ towns.** TYL provides municipal software -- tax collection, court management, utility billing, permitting. That's 85+ recurring SaaS contracts, visible in check registers as monthly or annual payments. When a municipality adopts Tyler, they rarely switch. This is municipal lock-in, measurable from public documents.

**Water infrastructure companies have national reach.** The pipeline tracks multiple water infrastructure vendors across 50-65+ municipalities each. These aren't household names, but they're embedded in municipal water operations across the country. Every water main break, every meter replacement, every treatment upgrade flows through these companies.

**Amazon is a municipal vendor.** Municipalities buy office supplies, server equipment, cleaning supplies, and maintenance items through Amazon. It's a line item in check registers that most analysts don't think about, but it's measurable, it's recurring, and it's growing.

## The Entity Resolution Problem

The hard part isn't finding the data. It's resolving the entities.

"WASTE MGMT" in one town's check register is the same company as "Waste Management of Maine" in another and "WM" in a third. "CORE & MAIN LP" matches "Core and Main" matches "HD SUPPLY WATERWORKS" (their former name). Our pipeline handles this across every municipality, resolving variant names to canonical entities and tickers.

This is why nobody else has this dataset. The documents are public. The entity resolution at scale is the hard part. And it gets better with every municipality we add -- every new name variant we resolve improves resolution for every other town.

## What You Can Do With This

One check register from one town is a curiosity. Entity-resolved vendor payment data across 3,900+ municipalities is an alternative dataset that tracks public company government revenue from the source documents, in near-real-time, before it shows up in quarterly earnings.

The applications are straightforward:

- **Revenue signal.** If a company's municipal payment volume is growing quarter over quarter across dozens of jurisdictions, that's a revenue signal.
- **Market share.** If Tyler Technologies is in 88 towns and a competitor is in 12, that's a market share signal.
- **Geographic exposure.** If a company's municipal revenue is concentrated in one state, that's a concentration risk signal.
- **Contract lifecycle.** RFPs show new opportunities. Check registers show active payments. The absence of payments after years of presence shows a lost contract.

We see all of these. Across every municipality in the pipeline. Every day.

---

### Want this data?

This story is built from [entity-resolved vendor payments](/data-stories/#entity-resolved-vendor-payments) -- vendor names from check registers and AP warrants resolved to public company tickers across 200+ municipalities. Updated daily.

- **[Download vendor payment sample (CSV)](/sample-data/signals-sample.csv)** -- entity-resolved signals with tickers, amounts, and municipality
- **[See how we resolve entities](/methodology/#entity-resolution)** -- our approach to matching vendor names to tickers
- **[Get entity data for specific tickers](mailto:matt@municipalalpha.com?subject=Entity%20data%20inquiry)** -- tell us which companies you're tracking
