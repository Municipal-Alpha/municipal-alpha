Title: Case Study: Waste Management (WM) Across 111 Municipalities
Slug: research/wm-entity-resolution
Template: redesign_case_study
Article_Key: wm-entity-resolution
Sortorder: 13
Summary: 1,099 sightings across 28 states. Contract extensions, competitive displacement, recurring payments, and regulatory signals for a single ticker extracted from public records.

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
<h3>WM is one company. We monitor 4,500+ municipalities.</h3>
<p>The same entity resolution runs across every document for every company that does business with local government. Waste haulers, engineering firms, construction companies, insurers, law firms, IT vendors. Tell me what ticker you're watching and I'll show you what the municipal record says.</p>
<a href="https://calendar.app.google/HkZk29hxj7Cdtvuc9" class="cta-button">Book a Data Review</a>
</div>

<div class="cs-note">
<strong>Methodology note:</strong> This signal chain was assembled from public meeting minutes, check registers, and legislative filings across 111 municipalities in 28 states. Every link above goes to the original source document. No proprietary data sources were used. These documents have always been public. They were sitting on town websites and state legislative databases, unconnected until entity resolution tied them to a single ticker.
</div>
