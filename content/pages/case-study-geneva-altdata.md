Title: Case Study: One Town's Check Register, 15 Public Company Tickers
Slug: research/geneva-altdata
Sortorder: 12
Summary: Geneva, Illinois publishes bi-weekly check registers. Municipal Alpha resolves vendor names to stock tickers automatically. 9 years of data, 15+ tickers, from a single town.

<style>
.cs-intro { font-size: 19px; color: #333; max-width: 640px; line-height: 1.7; margin-bottom: 40px; }
.cs-intro strong { color: #0C0C0C; }

.cs-stats { display: flex; gap: 40px; margin: 40px 0; flex-wrap: wrap; }
.cs-stat { text-align: center; }
.cs-stat-value { display: block; font-family: 'Newsreader', serif; font-size: 36px; font-weight: 600; color: #0C0C0C; }
.cs-stat-label { display: block; font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }

.timeline { margin: 48px 0; position: relative; padding-left: 32px; }
.timeline::before { content: ''; position: absolute; left: 8px; top: 0; bottom: 0; width: 2px; background: #E8E4DF; }

.tl-event { position: relative; margin-bottom: 28px; }
.tl-event::before { content: ''; position: absolute; left: -28px; top: 6px; width: 12px; height: 12px; border-radius: 50%; border: 2px solid #E8E4DF; background: #fff; z-index: 1; }
.tl-event.tl-hot::before { border-color: #E8512D; background: #E8512D; }
.tl-event.tl-warm::before { border-color: #E8512D; background: #fff; }
.tl-event.tl-cool::before { border-color: #ccc; background: #fff; }

.tl-date { font-family: 'IBM Plex Mono', monospace; font-size: 12px; color: #E8512D; font-weight: 500; margin-bottom: 4px; }
.tl-cool .tl-date { color: #888; }
.tl-board { font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
.tl-text { font-size: 15px; color: #333; line-height: 1.6; max-width: 600px; }
.tl-text strong { color: #0C0C0C; }
.tl-source { font-family: 'IBM Plex Mono', monospace; font-size: 11px; margin-top: 6px; }
.tl-source a { color: #E8512D; text-decoration: none; }
.tl-source a:hover { text-decoration: underline; }

.tl-gap { margin: 32px 0 32px 0; padding: 16px 0 16px 0; position: relative; }
.tl-gap::before { content: ''; position: absolute; left: -28px; top: 0; bottom: 0; width: 12px; border-left: 2px dashed #E8E4DF; margin-left: 3px; }
.tl-gap-text { font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: #E8512D; text-transform: uppercase; letter-spacing: 2px; }

.cs-window { background: #0C0C0C; color: #F7F4F0; border-radius: 6px; padding: 32px 40px; margin: 48px 0; max-width: 640px; }
.cs-window h3 { font-family: 'Newsreader', serif; font-size: 22px; font-weight: 500; color: #F7F4F0; margin-bottom: 12px; }
.cs-window p { font-size: 14px; color: #aaa; line-height: 1.7; margin-bottom: 8px; }
.cs-window .cs-highlight { color: #E8512D; font-weight: 600; }

.cs-cta { background: #F7F4F0; border-radius: 6px; padding: 40px; margin: 48px 0; text-align: center; max-width: 640px; }
.cs-cta h3 { font-family: 'Newsreader', serif; font-size: 22px; font-weight: 500; color: #0C0C0C; margin-bottom: 12px; }
.cs-cta p { font-size: 15px; color: #555; margin-bottom: 20px; line-height: 1.6; }

.cs-note { font-size: 13px; color: #888; line-height: 1.6; margin-top: 48px; padding-top: 24px; border-top: 1px solid #E8E4DF; max-width: 640px; }

.ticker-table { max-width: 640px; margin: 32px 0; }
.ticker-table table { width: 100%; border-collapse: collapse; font-size: 14px; }
.ticker-table th { font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: #888; text-transform: uppercase; letter-spacing: 1px; text-align: left; padding: 8px 12px; border-bottom: 2px solid #E8E4DF; }
.ticker-table td { padding: 8px 12px; border-bottom: 1px solid #E8E4DF; color: #333; }
.ticker-table td:nth-child(2) { font-family: 'IBM Plex Mono', monospace; font-weight: 500; color: #E8512D; }
</style>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<p class="cs-intro">
Geneva, Illinois publishes bi-weekly check registers listing every payment the city makes. <strong>Municipal Alpha resolves vendor names to stock tickers automatically.</strong> A single check register contains payments to 10-15 publicly traded companies. Across 9 years of bi-weekly reports, that builds a continuous revenue signal for companies like Grainger, Tyler Technologies, Comcast, Waste Management, and others. Nobody else is reading 2,500 municipal check registers bi-weekly.
</p>

<div class="cs-stats">
<div class="cs-stat"><span class="cs-stat-value">9</span><span class="cs-stat-label">years of check registers</span></div>
<div class="cs-stat"><span class="cs-stat-value">15+</span><span class="cs-stat-label">public company tickers</span></div>
<div class="cs-stat"><span class="cs-stat-value">~200</span><span class="cs-stat-label">bi-weekly registers</span></div>
<div class="cs-stat"><span class="cs-stat-value">3,900+</span><span class="cs-stat-label">municipalities at scale</span></div>
</div>

<div class="cs-window">
<h3>What you're about to read</h3>
<p>Every entry is a real document from the City of Geneva, Illinois. Population: 22,000. The links go to geneva.il.us. <span class="cs-highlight">Each check register is a snapshot of municipal spending.</span> Bi-weekly snapshots over 9 years build a time series. For any company that sells to municipalities, this is micro-revenue data below the threshold of any SEC filing, updated every two weeks.</p>
</div>

## The Signal Chain

<div class="timeline">

<div class="tl-event tl-cool">
<div class="tl-date">January 3, 2017</div>
<div class="tl-board">Check Register</div>
<div class="tl-text">First register in the chain. Payments to Comcast, Grainger, AT&T, Home Depot, Staples, Dell. <strong>GWW is a recurring municipal customer for industrial supplies.</strong> This is the baseline. Grainger appears in nearly every register, bi-weekly payments for maintenance and operations.</div>
<div class="tl-source"><a href="https://www.geneva.il.us/ArchiveCenter/ViewFile/Item/1514">Source: geneva.il.us &rarr;</a></div>
</div>

<div class="tl-event tl-warm">
<div class="tl-date">August 7, 2017</div>
<div class="tl-board">Check Register</div>
<div class="tl-text">Tyler Technologies, American Water Works, Stantec, Verizon, Grainger, AT&T. <strong>TYL appears in the context of GIS-related services.</strong> Different signal type than Grainger. Tyler payments indicate a software contract, sticky, multi-year, high-margin revenue. One town is noise. The same pattern across 50 towns reveals TYL's government segment pipeline.</div>
<div class="tl-source"><a href="https://www.geneva.il.us/ArchiveCenter/ViewFile/Item/1582">Source: geneva.il.us &rarr;</a></div>
</div>

<div class="tl-event tl-cool">
<div class="tl-date">August 9, 2017</div>
<div class="tl-board">Check Register</div>
<div class="tl-text">Dedicated line item for "Household Hazardous Waste Collection Services." <strong>Waste Management (WM).</strong> Municipal contracts are long-cycle and geographically sticky. Contract renewals or losses are visible in the payment stream months before they hit quarterly earnings.</div>
<div class="tl-source"><a href="https://www.geneva.il.us/ArchiveCenter/ViewFile/Item/1614">Source: geneva.il.us &rarr;</a></div>
</div>

<div class="tl-event tl-hot">
<div class="tl-date">November 27, 2017</div>
<div class="tl-board">Check Register</div>
<div class="tl-text"><strong>"Electric Utility Geographic Information System" contract.</strong> Tyler Technologies and Microsoft both appear. This is the highest-value signal type: a named contract for a specific system. Geneva's electric utility is committing to Tyler's platform for years. Microsoft appears as the infrastructure layer (Azure/SQL licensing). Both represent committed recurring revenue.</div>
<div class="tl-source"><a href="https://www.geneva.il.us/ArchiveCenter/ViewFile/Item/1629">Source: geneva.il.us &rarr;</a></div>
</div>

<div class="tl-gap"><div class="tl-gap-text">8 years of bi-weekly registers</div></div>

<div class="tl-event tl-warm">
<div class="tl-date">January 5, 2026</div>
<div class="tl-board">Budget</div>
<div class="tl-text"><strong>FY 2026-27 Proposed Budget.</strong> Waste Management listed among continuing vendors, confirming contract continuity into FY27. Budget documents are forward-looking. When a vendor appears in a proposed budget, it signals the municipality expects to continue the relationship. This is pre-earnings intelligence: the contract renewal that won't show up in WM's next quarterly filing is already visible here.</div>
<div class="tl-source"><a href="https://www.geneva.il.us/ArchiveCenter/ViewFile/Item/3924">Source: geneva.il.us &rarr;</a></div>
</div>

<div class="tl-event tl-hot">
<div class="tl-date">February 17, 2026</div>
<div class="tl-board">Check Register</div>
<div class="tl-text"><strong>13 tickers resolved in a single bi-weekly cycle.</strong> TYL, CMCSA, GWW, AIQUY, NEE, AMZN, HD, UPS, USB, and more. Nine years after the first register, Grainger is still there. Tyler Technologies is still there. For any of these companies, an analyst watching municipal payment data would have seen 200+ data points from Geneva alone before the next 10-K is filed.</div>
<div class="tl-source"><a href="https://www.geneva.il.us/ArchiveCenter/ViewFile/Item/3930">Source: geneva.il.us &rarr;</a></div>
</div>

</div>

<div class="cs-window">
<h3>Why this matters</h3>
<p>Municipal check registers publish weeks to months before vendor revenue appears in quarterly earnings. An equity analyst watching GWW payments across 100 municipalities would see geographic expansion or contraction <span class="cs-highlight">before the earnings call.</span></p>
<p>A new town appearing in GWW's payment stream is a new customer. A town dropping out is a lost account. Neither event is visible in any filing until the quarter closes.</p>
<p><strong style="color: #F7F4F0;">Three signal types:</strong></p>
<p><span class="cs-highlight">Recurring supply payments</span> (GWW, HD, AMZN) confirm ongoing customer relationships. Aggregated across municipalities, this reveals geographic footprint and seasonal patterns.</p>
<p><span class="cs-highlight">Contract awards</span> (TYL, WM, STN) represent multi-year commitments. One contract in Geneva is noise. The same pattern across 50 towns is pipeline.</p>
<p><span class="cs-highlight">Utility and infrastructure payments</span> (NEE, AWK, VZ, CMCSA) show which utility serves which municipality, and whether that changes, before it appears anywhere else.</p>
</div>

## What One Register Produces

<div class="ticker-table">
<table>
<tr><th>Vendor Name (as printed)</th><th>Ticker</th><th>Sector</th></tr>
<tr><td>W.W. Grainger</td><td>GWW</td><td>Industrial distribution</td></tr>
<tr><td>Tyler Technologies</td><td>TYL</td><td>Government software</td></tr>
<tr><td>Comcast</td><td>CMCSA</td><td>Telecom / broadband</td></tr>
<tr><td>Stantec</td><td>STN</td><td>Engineering / consulting</td></tr>
<tr><td>Verizon</td><td>VZ</td><td>Telecom</td></tr>
<tr><td>NextEra Energy</td><td>NEE</td><td>Utilities</td></tr>
<tr><td>Airgas (Air Liquide)</td><td>AIQUY</td><td>Industrial gases</td></tr>
<tr><td>Home Depot</td><td>HD</td><td>Retail / supplies</td></tr>
<tr><td>Amazon</td><td>AMZN</td><td>General procurement</td></tr>
<tr><td>American Water Works</td><td>AWK</td><td>Water utilities</td></tr>
<tr><td>Waste Management</td><td>WM</td><td>Environmental services</td></tr>
<tr><td>AT&T</td><td>T</td><td>Telecom</td></tr>
<tr><td>UPS</td><td>UPS</td><td>Logistics</td></tr>
<tr><td>U.S. Bancorp</td><td>USB</td><td>Banking / treasury</td></tr>
<tr><td>Microsoft</td><td>MSFT</td><td>Software licensing</td></tr>
</table>
</div>

This is not insider information. Every check register cited above is a public document, published on a municipal website, available to anyone. The edge is not access. It's aggregation. No single check register moves a stock. 2,500 check registers, resolved to tickers, updated bi-weekly, with 9 years of history, is a dataset that doesn't exist anywhere else.

<div class="cs-cta">
<h3>See what your tickers look like.</h3>
<p>Pick a ticker. I'll pull the municipal payment history across every town in the network and show you what the signal looks like before it hits the 10-K.</p>
<a href="https://calendar.app.google/s6wDVSaJuqCkwcmg9" class="cta-button">Book a 15-Minute Data Review</a>
</div>

<div class="cs-note">
<strong>Methodology note:</strong> All documents cited in this case study are public records published by the City of Geneva, Illinois. Every link above goes to the original source document on geneva.il.us. No proprietary data sources were used. Vendor-to-ticker resolution runs automatically on every accounts payable document ingested. The documents have always been public. They were just sitting on a city website, unread. A retrospective chain like this proves the method and the lead time, not a hit rate; the forward call is what a pilot is for.
</div>
