Title: Data Stories
Slug: data-stories
Sortorder: 2
Summary: Cross-municipal patterns from live pipeline data. Each story is built entirely from public records across 4,300+ municipalities.

<style>
.ds-hero {
    max-width: 640px;
    margin-bottom: 48px;
}
.ds-hero h2 {
    font-family: 'Newsreader', serif;
    font-size: 28px;
    font-weight: 500;
    color: #0C0C0C;
    margin: 0 0 16px;
}
.ds-hero p {
    font-size: 17px;
    color: #555;
    line-height: 1.7;
    margin-bottom: 24px;
}

.ds-section-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: #E8512D;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 24px;
}

.ds-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 28px;
    margin-bottom: 56px;
}

.ds-card {
    border: 1px solid #E8E4DF;
    border-radius: 6px;
    overflow: hidden;
    background: #fff;
    text-decoration: none;
    display: flex;
    flex-direction: column;
    transition: border-color 0.15s, box-shadow 0.15s;
}
.ds-card:hover {
    border-color: #E8512D;
    box-shadow: 0 2px 16px rgba(232, 81, 45, 0.1);
}

.ds-card-img {
    width: 100%;
    height: 160px;
    object-fit: cover;
}

.ds-card-body {
    padding: 24px;
    flex: 1;
    display: flex;
    flex-direction: column;
}

.ds-card h3 {
    font-family: 'Newsreader', serif;
    font-size: 18px;
    font-weight: 500;
    color: #0C0C0C;
    margin: 0 0 8px;
    line-height: 1.3;
}

.ds-card-desc {
    font-size: 14px;
    color: #555;
    line-height: 1.6;
    margin-bottom: 12px;
    flex: 1;
}

.ds-card-stat {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: #888;
    border-top: 1px solid #E8E4DF;
    padding-top: 12px;
    margin-top: auto;
}
.ds-card-stat strong {
    color: #E8512D;
    font-weight: 600;
}

.ds-mid-cta {
    background: #0C0C0C;
    color: #F7F4F0;
    border-radius: 6px;
    padding: 40px 48px;
    margin: 8px 0 56px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 32px;
    flex-wrap: wrap;
}
.ds-mid-cta h3 {
    font-family: 'Newsreader', serif;
    font-size: 22px;
    font-weight: 500;
    margin: 0 0 8px;
    color: #F7F4F0;
}
.ds-mid-cta p {
    font-size: 14px;
    color: #aaa;
    margin: 0;
    line-height: 1.5;
}
.ds-mid-cta .cta-button {
    flex-shrink: 0;
}

/* Dataset cards */
.ds-dataset-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-bottom: 56px;
}

.ds-dataset {
    border: 1px solid #E8E4DF;
    border-radius: 6px;
    padding: 24px;
    background: #fff;
}

.ds-dataset h4 {
    font-family: 'Newsreader', serif;
    font-size: 16px;
    font-weight: 500;
    color: #0C0C0C;
    margin: 0 0 8px;
}

.ds-dataset p {
    font-size: 13px;
    color: #555;
    line-height: 1.5;
    margin: 0 0 12px;
}

.ds-dataset-meta {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: #888;
    margin-bottom: 12px;
}
.ds-dataset-meta strong {
    color: #0C0C0C;
}

.ds-dataset a {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: #E8512D;
    text-decoration: none;
    font-weight: 500;
}
.ds-dataset a:hover {
    text-decoration: underline;
}

/* Profile cards */
.ds-profile-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-bottom: 56px;
}

.ds-profile {
    border: 1px solid #E8E4DF;
    border-radius: 6px;
    padding: 24px;
    background: #fff;
    text-decoration: none;
    display: block;
    transition: border-color 0.15s;
}
.ds-profile:hover {
    border-color: #E8512D;
}

.ds-profile h4 {
    font-family: 'Newsreader', serif;
    font-size: 16px;
    font-weight: 500;
    color: #0C0C0C;
    margin: 0 0 8px;
}

.ds-profile p {
    font-size: 13px;
    color: #555;
    line-height: 1.5;
    margin: 0 0 8px;
}

.ds-profile-stats {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: #888;
}
.ds-profile-stats strong {
    color: #0C0C0C;
}

.ds-bottom-cta {
    text-align: center;
    padding: 24px 0 8px;
}
.ds-bottom-cta h3 {
    font-family: 'Newsreader', serif;
    font-size: 24px;
    font-weight: 500;
    color: #0C0C0C;
    margin-bottom: 12px;
}
.ds-bottom-cta p {
    font-size: 15px;
    color: #555;
    margin-bottom: 24px;
    line-height: 1.6;
}
.ds-bottom-cta .ds-or {
    display: block;
    margin: 16px 0;
    font-size: 13px;
    color: #888;
}
.ds-bottom-cta a.ds-email {
    color: #E8512D;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
}
.ds-bottom-cta a.ds-email:hover {
    text-decoration: underline;
}

@media (max-width: 640px) {
    .ds-grid { grid-template-columns: 1fr; }
    .ds-dataset-grid { grid-template-columns: 1fr; }
    .ds-profile-grid { grid-template-columns: 1fr; }
    .ds-mid-cta { padding: 28px 24px; flex-direction: column; text-align: center; }
}
</style>

<div class="ds-hero">
<h2>Patterns only visible at 4,300+ municipalities</h2>
<p>Each story is built entirely from public records. The pipeline classifies every document, resolves vendor names to public company tickers, and tracks policy contagion across jurisdictions. These are the patterns that fall out.</p>
</div>

<div class="ds-section-label">Data Stories</div>

<div class="ds-grid">

<a href="/research/pfas-contagion/" class="ds-card">
<img src="/images/story-pfas.png" alt="PFAS Contagion" class="ds-card-img">
<div class="ds-card-body">
<h3>PFAS Is Spreading Through Municipal Agendas Faster Than Groundwater</h3>
<div class="ds-card-desc">The remediation wave is visible in town council agendas months before EPA enforcement actions.</div>
<div class="ds-card-stat"><strong>120</strong> events &middot; <strong>72</strong> municipalities &middot; <strong>23</strong> states</div>
</div>
</a>

<a href="/research/company-footprint/" class="ds-card">
<img src="/images/story-company-footprint.png" alt="Company Footprint" class="ds-card-img">
<div class="ds-card-body">
<h3>The Company That Shows Up in 123 Towns</h3>
<div class="ds-card-desc">Entity resolution reveals which public companies have the deepest municipal government footprint. Verizon: 6,183 sightings.</div>
<div class="ds-card-stat"><strong>4,300+</strong> municipalities &middot; <strong>100+</strong> resolved tickers</div>
</div>
</a>

<a href="/research/housing-density-wave/" class="ds-card">
<img src="/images/story-housing-wave.png" alt="Housing Density Wave" class="ds-card-img">
<div class="ds-card-body">
<h3>The Housing Density Wave Is Rewriting Municipal Zoning</h3>
<div class="ds-card-desc">ADU mandates, density increases, and short-term rental regulation are one wave, moving through regions at different speeds.</div>
<div class="ds-card-stat"><strong>399</strong> events &middot; <strong>130+</strong> municipalities &middot; <strong>27</strong> states</div>
</div>
</a>

<a href="/research/lead-pipes/" class="ds-card">
<img src="/images/story-lead-pipes.png" alt="Lead Pipes" class="ds-card-img">
<div class="ds-card-body">
<h3>Lead Pipes Are a $50B Problem Hiding in Municipal Agendas</h3>
<div class="ds-card-desc">The EPA's Lead and Copper Rule is creating a predictable cascade of municipal spending.</div>
<div class="ds-card-stat"><strong>77</strong> events &middot; <strong>39</strong> municipalities &middot; <strong>13</strong> states</div>
</div>
</a>

<a href="/research/data-center-zoning/" class="ds-card">
<img src="/images/story-data-center-zoning.png" alt="Data Center Zoning" class="ds-card-img">
<div class="ds-card-body">
<h3>Data Centers Are Now a Zoning Fight in 20 States</h3>
<div class="ds-card-desc">Moratoriums, tax breaks, and electricity caps hitting municipal agendas faster than the power grid can keep up.</div>
<div class="ds-card-stat"><strong>58</strong> signals &middot; <strong>30</strong> jurisdictions &middot; <strong>20</strong> states</div>
</div>
</a>

<a href="/research/pickleball-wave/" class="ds-card">
<img src="/images/story-pickleball.png" alt="Pickleball Wave" class="ds-card-img">
<div class="ds-card-body">
<h3>The Pickleball Boom Is Now a Line Item in Municipal Budgets</h3>
<div class="ds-card-desc">From federal grants to tennis court conversions, a consumer trend becoming municipal capex.</div>
<div class="ds-card-stat"><strong>29</strong> signals &middot; <strong>14</strong> municipalities &middot; <strong>9</strong> states</div>
</div>
</a>

</div>

<div class="ds-mid-cta">
<div>
<h3>See a pattern relevant to your portfolio?</h3>
<p>Every story above was built from the same pipeline that powers our data products. Tell me what you're watching.</p>
</div>
<a href="https://calendar.app.google/HkZk29hxj7Cdtvuc9" class="cta-button">Book a Call</a>
</div>

<div class="ds-section-label">Datasets</div>

<div class="ds-dataset-grid">

<div class="ds-dataset">
<h4>Entity-Resolved Vendor Payments</h4>
<p>Check registers and AP warrants resolved to public company tickers. One payment is a curiosity. Thousands across jurisdictions is a revenue signal.</p>
<div class="ds-dataset-meta"><strong>200+</strong> municipalities &middot; <strong>100+</strong> tickers</div>
<a href="/sample-data/signals-sample.csv">Download sample CSV &rarr;</a>
</div>

<div class="ds-dataset">
<h4>Contagion &amp; Policy Signals</h4>
<p>Cross-municipal event tracking for regulatory waves, infrastructure mandates, and spending cascades. Which town moved first, how fast it spread.</p>
<div class="ds-dataset-meta"><strong>459</strong> topics &middot; <strong>50</strong> states</div>
<a href="/sample-data/infrastructure-risk-sample.csv">Download sample CSV &rarr;</a>
</div>

<div class="ds-dataset">
<h4>Tower &amp; Infrastructure Prospects</h4>
<p>Cell tower sites cross-referenced across assessor records, FCC, FAA, and municipal payments. Parcel-level with owner ID and confidence scoring.</p>
<div class="ds-dataset-meta"><strong>7,700+</strong> sites &middot; multi-source cross-reference</div>
<a href="/sample-data/tower-prospects-sample.csv">Download sample CSV &rarr;</a>
</div>

<div class="ds-dataset">
<h4>Building Permits &amp; Contractor Signals</h4>
<p>Structured permit records resolved to public company tickers. Leading indicator for construction activity and government contractor revenue.</p>
<div class="ds-dataset-meta"><strong>43K+</strong> permits &middot; <strong>400+</strong> municipalities</div>
<a href="/sample-data/contractor-signals-sample.csv">Download sample CSV &rarr;</a>
</div>

<div class="ds-dataset">
<h4>Credit Quality Indicators</h4>
<p>Budget trends, fund balances, debt service patterns, and fiscal stress signals from source financial documents. Structured daily instead of annually.</p>
<div class="ds-dataset-meta"><strong>4,300+</strong> municipalities &middot; daily updates</div>
<a href="/sample-data/credit-sample.csv">Download sample CSV &rarr;</a>
</div>

<div class="ds-dataset">
<h4>Full Methodology</h4>
<p>Coverage maps, freshness guarantees, known gaps, and classification details. How the pipeline works, what it captures, and what it misses.</p>
<div class="ds-dataset-meta">Updated with every pipeline change</div>
<a href="/methodology/">Read methodology &rarr;</a>
</div>

</div>

<div class="ds-section-label">Town Profiles</div>

<p style="font-size: 15px; color: #555; margin-bottom: 24px; line-height: 1.6;">What the pipeline sees in a single municipality. Document volume, signal classification, entity resolution, and vendor landscape. Auto-generated from continuous monitoring.</p>

<div class="ds-profile-grid">

<a href="/profiles/falmouth-me/" class="ds-profile">
<h4>Falmouth, Maine</h4>
<p>Coastal New England town with active development, climate, and infrastructure lease signals.</p>
<div class="ds-profile-stats"><strong>689</strong> docs &middot; <strong>18</strong> boards &middot; <strong>45</strong> tickers &middot; <strong>8</strong> tower sites</div>
</a>

<a href="/profiles/geneva-il/" class="ds-profile">
<h4>Geneva, Illinois</h4>
<p>The alt data story: entity resolution maps vendor payments to public company revenue across 1,700+ sightings.</p>
<div class="ds-profile-stats"><strong>1,338</strong> docs &middot; <strong>45</strong> boards &middot; <strong>50</strong> tickers &middot; <strong>257</strong> check registers</div>
</a>

<a href="/profiles/pocatello-id/" class="ds-profile">
<h4>Pocatello, Idaho</h4>
<p>The town nobody's watching, producing more high-priority signals than cities ten times its profile.</p>
<div class="ds-profile-stats"><strong>2,244</strong> docs &middot; <strong>39</strong> boards &middot; <strong>98</strong> HIGH signals &middot; <strong>38</strong> tower sites</div>
</a>

</div>

<div class="ds-bottom-cta">
<h3>What should we investigate next?</h3>
<p>The pipeline monitors 4,300+ municipalities in real time. If there's a trend, policy wave, or spending pattern you want us to dig into, we'll build the data story.</p>
<a href="https://calendar.app.google/HkZk29hxj7Cdtvuc9" class="cta-button">Book a Data Review</a>
<span class="ds-or">or</span>
<a href="mailto:matt@municipalalpha.com?subject=Data%20story%20request" class="ds-email">matt@municipalalpha.com</a>
</div>
