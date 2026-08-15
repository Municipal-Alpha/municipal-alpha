Title: Case Study: Waste Management (WM) Across 111 Municipalities
Slug: research/wm-entity-resolution
Sortorder: 13
Summary: 1,099 sightings across 28 states. Contract extensions, competitive displacement, recurring payments, and regulatory signals for a single ticker extracted from public records.

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

.cs-entity-table { margin: 48px 0; max-width: 640px; }
.cs-entity-table h3 { font-family: 'Newsreader', serif; font-size: 22px; font-weight: 500; margin-bottom: 16px; color: #0C0C0C; }
.cs-entity-table table { width: 100%; border-collapse: collapse; font-size: 14px; }
.cs-entity-table th { font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: #888; text-transform: uppercase; letter-spacing: 1px; text-align: left; padding: 8px 12px; border-bottom: 2px solid #E8E4DF; }
.cs-entity-table td { padding: 8px 12px; border-bottom: 1px solid #E8E4DF; color: #333; }
.cs-entity-table td:last-child { font-family: 'IBM Plex Mono', monospace; font-weight: 600; color: #E8512D; }

.cs-cta { background: #F7F4F0; border-radius: 6px; padding: 40px; margin: 48px 0; text-align: center; max-width: 640px; }
.cs-cta h3 { font-family: 'Newsreader', serif; font-size: 22px; font-weight: 500; color: #0C0C0C; margin-bottom: 12px; }
.cs-cta p { font-size: 15px; color: #555; margin-bottom: 20px; line-height: 1.6; }

.cs-note { font-size: 13px; color: #888; line-height: 1.6; margin-top: 48px; padding-top: 24px; border-top: 1px solid #E8E4DF; max-width: 640px; }
</style>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<p class="cs-intro">
Waste Management (NYSE: WM) appears in municipal documents under dozens of name variants across 28 states. <strong>Municipal Alpha's entity resolution engine resolves them all to a single ticker.</strong> Contract extensions, competitive bids, recurring payments, and regulatory signals, all visible weeks to months before they surface in quarterly earnings.
</p>

<div class="cs-stats">
<div class="cs-stat"><span class="cs-stat-value">111</span><span class="cs-stat-label">municipalities</span></div>
<div class="cs-stat"><span class="cs-stat-value">1,099</span><span class="cs-stat-label">sightings</span></div>
<div class="cs-stat"><span class="cs-stat-value">28</span><span class="cs-stat-label">states</span></div>
<div class="cs-stat"><span class="cs-stat-value">2013&ndash;2026</span><span class="cs-stat-label">date range</span></div>
</div>

<div class="cs-window">
<h3>The entity resolution challenge</h3>
<p>Municipal documents do not use ticker symbols. They use whatever name appears on the contract, the check, or the agenda: "Waste Management," "WASTE MANAGEMENT OF LONDONDERRY LLC," "Waste Management Inc of Florida." And "waste management" as a phrase appears constantly in documents about waste management <em>policy</em> that have nothing to do with the company.</p>
<p><span class="cs-highlight">The engine uses context</span> (vendor payment lists, contract language, meeting agenda items) to distinguish the company from the generic term, then resolves all variants to ticker WM. That is what makes the signal chain below possible.</p>
</div>

## The Signal Chain

<div class="timeline">

<div class="tl-event tl-hot">
<div class="tl-date">February 17, 2026</div>
<div class="tl-board">Committee Minutes</div>
<div class="tl-text">Manchester, NH Special Committee on Solid Waste Activities discusses <strong>extending the city's contract with Waste Management for solid waste disposal services.</strong> Manchester is a city of 115,000. The extension appears in committee minutes weeks before the full board vote and months before it would appear in WM's earnings.</div>
<div class="tl-source"><a href="https://www.manchesternh.gov/Departments/City-Clerk/Agendas-Minutes">Source: manchesternh.gov &rarr;</a></div>
</div>

<div class="tl-event tl-hot">
<div class="tl-date">February 18, 2026</div>
<div class="tl-board">Committee Minutes</div>
<div class="tl-text">Durham, NH Integrated Waste Management Advisory Committee minutes reveal neighboring <strong>Dover switched from Waste Management to RMI for sludge handling.</strong> Same document notes WM is developing a sludge dryer. Two signals: a competitive loss and a strategic capex response. An analyst reading only WM's filings would see the capex line item but not the competitive context.</div>
<div class="tl-source"><a href="https://www.ci.durham.nh.us/bos_committees/integrated-waste-management-advisory-committee">Source: durham.nh.us &rarr;</a></div>
</div>

<div class="tl-event tl-warm">
<div class="tl-date">March 18, 2026</div>
<div class="tl-board">Select Board</div>
<div class="tl-text">Norridgewock, ME. WM provides the Select Board with an annual update on business operations, facility investments, and <strong>PFAS treatment and biosolids processing.</strong> Facility-level investment detail that may not appear in investor presentations for quarters.</div>
<div class="tl-source"><a href="https://norridgewock.gov/AgendaCenter/ViewFile/Minutes/_03182026-127?html=true">Source: norridgewock.gov &rarr;</a></div>
</div>

<div class="tl-event tl-warm">
<div class="tl-date">April 2, 2026</div>
<div class="tl-board">Select Board</div>
<div class="tl-text">Coventry, CT evaluating vendors for waste and composting services. <strong>WM is in the running but has not won yet.</strong> A pipeline signal: the bid outcome will be visible in follow-up documents before it hits any financial filing.</div>
<div class="tl-source"><a href="https://www.coventry-ct.gov/ArchiveCenter/ViewFile/Item/1588">Source: coventry-ct.gov &rarr;</a></div>
</div>

<div class="tl-event tl-warm">
<div class="tl-date">March 3, 2026</div>
<div class="tl-board">Select Board</div>
<div class="tl-text">Wilton, ME. WM submitted bids for waste hauling but <strong>did not bid on recycling.</strong> A competitive positioning signal: WM is selectively bidding on service lines, potentially ceding recycling to a competitor or signaling margin pressure in that segment.</div>
<div class="tl-source"><a href="https://www.wiltonmaine.gov/wp-content/uploads/2026/02/Selectboard-Agenda-Package-2026-03-03.pdf">Source: wiltonmaine.gov &rarr;</a></div>
</div>

<div class="tl-event tl-cool">
<div class="tl-date">2013&ndash;2026</div>
<div class="tl-board">Check Register</div>
<div class="tl-text">Nashua, NH. <strong>226 sightings across 13 years of check registers.</strong> Most recent: March 4, 2026, $247.67. A long-duration revenue relationship visible in accounts payable data. Payment history shows contract continuity, price trends, and service consistency over more than a decade.</div>
<div class="tl-source"><a href="https://www.nashuanh.gov/ArchiveCenter/ViewFile/Item/8288">Source: nashuanh.gov &rarr;</a></div>
</div>

<div class="tl-event tl-cool">
<div class="tl-date">January 16, 2026</div>
<div class="tl-board">Check Register</div>
<div class="tl-text">Bedford, NH. AP Check Warrant showing <strong>$7,511.14 to "WASTE MANAGEMENT OF LONDONDERRY LLC."</strong> The entity name on the check is a local subsidiary variant. The entity resolution engine maps it to ticker WM.</div>
<div class="tl-source"><a href="https://www.bedfordnh.org/ArchiveCenter/ViewFile/Item/1425">Source: bedfordnh.org &rarr;</a></div>
</div>

<div class="tl-event tl-warm">
<div class="tl-date">February 26, 2026</div>
<div class="tl-board">Legislative</div>
<div class="tl-text">State of Georgia HB320: <strong>"Waste management; require recycling of solar panels."</strong> A regulatory signal affecting WM's recycling operations. If passed, creates a new compliance requirement and potentially a new revenue stream. Signals the direction of state-level waste regulation.</div>
<div class="tl-source"><a href="https://legiscan.com/GA/bill/HB320/2025">Source: legiscan.com &rarr;</a></div>
</div>

</div>

<div class="cs-entity-table">
<h3>Entity Resolution in Action</h3>
<table>
<tr><th>As Written in Municipal Documents</th><th>Resolved To</th></tr>
<tr><td>Waste Management</td><td>WM</td></tr>
<tr><td>WASTE MANAGEMENT OF LONDONDERRY LLC</td><td>WM</td></tr>
<tr><td>Waste Management Inc of Florida</td><td>WM</td></tr>
<tr><td>WM</td><td>WM</td></tr>
</table>
<p style="font-size: 13px; color: #888; margin-top: 12px; line-height: 1.6;">The mapping is not simple string matching. "Waste management" as a phrase appears in document titles about waste management policy that have nothing to do with the company. The engine uses context to distinguish the company from the generic term.</p>
</div>

<div class="cs-window">
<h3>The competitive window</h3>
<p><strong>Contract extensions</strong> appear in committee minutes 2-6 weeks before the vote, and months before the next earnings call. <strong>Competitive bids</strong> appear in agendas before awards are announced. <strong>Check register payments</strong> are published monthly or quarterly, but do not appear in WM's filings until the relevant quarter closes. <strong>Legislative signals</strong> appear when bills are filed, months before they are voted on.</p>
<p><span class="cs-highlight">No sell-side analyst is reading meeting minutes from 111 municipalities.</span> No alternative data provider is resolving "WASTE MANAGEMENT OF LONDONDERRY LLC" to ticker WM. The signal exists in public records. The edge is in systematic extraction, entity resolution, and classification at scale.</p>
</div>

<div class="cs-cta">
<h3>WM is one company. We monitor 4,300+ municipalities.</h3>
<p>The same entity resolution runs across every document for every company that does business with local government. Waste haulers, engineering firms, construction companies, insurers, law firms, IT vendors. Tell me what ticker you're watching and I'll show you what the municipal record says.</p>
<a href="https://calendar.app.google/HkZk29hxj7Cdtvuc9" class="cta-button">Book a Data Review</a>
</div>

<div class="cs-note">
<strong>Methodology note:</strong> This signal chain was assembled from public meeting minutes, check registers, and legislative filings across 111 municipalities in 28 states. Every link above goes to the original source document. No proprietary data sources were used. These documents have always been public. They were sitting on town websites and state legislative databases, unconnected until entity resolution tied them to a single ticker.
</div>
