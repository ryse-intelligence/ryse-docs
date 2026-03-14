# Existing SaaS Platforms: Last-Mile Delivery — What's Out There & Where the Gaps Are

Here are the six most relevant platforms a business like mine would encounter, evaluated as an Australian SMB last-mile operator.

---

## 1. 🇦🇺 Locate2u

**What they do:** Australian-built all-in-one delivery management — route optimisation, live driver tracking, customer ETAs, proof of delivery, dispatch, and a basic billing engine. Built for the Australian market.

**Pricing:** GPS package at $15/seat/month; Premium package at $260 for four seats/month with additional seats at $55/month. Enterprise pricing available for 50+ users or API access. [Locate2u](https://www.locate2u.com/route-planning/locate2u-vs-circuit-route-planner/)

**Target customer:** Australian SMBs — furniture retailers, pharmacies, food delivery, field service. Deliberately positioned below enterprise complexity.

**Australian prevalence:** High. One of the most commonly used tools in the SMB last-mile segment. Backed by Zoom2u's local market knowledge. Well-reviewed for ease of setup and local support.

**Market quote:** _"Use Locate2u to manage your deliveries from start to finish... your staff and customers will love it."_

**Gaps as my business owner:**

- Billing engine is basic — doesn't handle the complexity of multi-client rate cards or automated invoice reconciliation
- No AI-driven predictive FTD alerting — it tracks, it doesn't anticipate
- No manifest normalisation — still need to clean data before import
- Analytics are operational (where are my drivers?) not strategic (which client is unprofitable?)

---

## 2. 🇺🇸 Onfleet

**What they do:** Delivery management platform — route optimisation, real-time dispatch dashboard, driver app, customer notifications, analytics. Well-regarded API. Used globally across courier, food, pharmacy, cannabis.

**Pricing:** Launch at $550/month for 2,000 tasks; Scale at $1,265/month for 5,000 tasks; Enterprise at custom pricing. [Spoke](https://spoke.com/dispatch/blog/onfleet-reviews) Per-task model means costs spike during peak periods.

**Target customer:** Mid-market operators (50–500 deliveries/day) up to enterprise. Strong in the US; growing Australian presence.

**Australian prevalence:** Moderate. Used by tech-forward Australian operators, particularly those running high-volume B2C e-commerce delivery. Less prevalent in traditional freight/courier businesses.

**Market quote:** _"Onfleet's modern, delightful delivery management software makes it easy for businesses to manage and analyze their local deliveries."_

**Gaps as my business owner:**

- Per-task pricing is punishing during peak — my Christmas volume spike could double my bill
- No manifest ingestion layer — data normalisation still manual
- Limited customisation of client-facing reporting (one format, not bespoke per client)
- No demand forecasting or staffing intelligence
- The UI has persistent complaints about clunkiness and driver location lag

---

## 3. 🇺🇸 OptimoRoute

**What they do:** Pure-play route optimisation and scheduling. Strong algorithm, weekly planning, live tracking, proof of delivery, basic analytics. Focused on doing routing very well rather than being an all-in-one.

**Pricing:** Priced per driver per month — Lite at ~$39/driver/month, Pro at ~$49/driver/month. [OptimoRoute](https://optimoroute.com/pricing/) For my 42 drivers, that's ~$1,600–2,050/month at Pro.

**Target customer:** Delivery and field service businesses of any size that need better routing but don't need a full DMS. Popular with SMBs.

**Australian prevalence:** Moderate-to-high. Frequently appears in Australian operator comparisons. Affordable per-driver model suits growing fleets.

**Market quote:** _"OptimoRoute customers reduce time spent planning routes by up to 80% and cut fuel and driving expenses by 20%."_

**Gaps as my business owner:**

- Routing only — no dispatch management, no customer-facing comms platform, no exception alerting
- No client reporting automation whatsoever
- No manifest normalisation
- Static route planning — optimises at the start of day, limited real-time re-routing capability
- Noted issues with Australian rural address recognition

---

## 4. 🇦🇺 Shippit

**What they do:** Multi-carrier shipping and dispatch platform targeting retailers. Connects to 100+ carriers, automates fulfilment rules, compares carrier rates, and provides delivery tracking. More a shipper-side tool than an operator-side tool.

**Pricing:** Tiered plans based on shipment volume; pricing now customised per account post-October 2024 changes. Broadly in the $100–$500+/month range for SMBs depending on volume.

**Target customer:** Large retailers, fleet managers, and ecommerce teams — positioned as enterprise-grade for shipping optimisation and multi-carrier management. [Shippit](https://www.shippit.com)

**Australian prevalence:** Very high — one of the most widely used shipping platforms in Australian e-commerce retail. Strong with Shopify, Magento, WooCommerce merchants.

**Market quote:** _"Shippit is Australia's leading multi-carrier shipping & delivery management software for large retailers, fleet managers, and ecommerce teams."_

**Gaps as my business owner:**

- This is a _shipper_ tool, not a _last-mile operator_ tool — designed for my clients, not for me
- No driver dispatch, no driver app, no run sheet management
- No operational visibility during route execution
- Doesn't help with FTD rates, exception handling, or reconciliation from the operator side

---

## 5. 🇦🇺 Teletrac Navman (TN360)

**What they do:** Fleet telematics and GPS tracking — live vehicle location, driver behaviour scoring (harsh braking, speeding, fatigue), AI dashcam, maintenance scheduling, compliance. Sold in Australia through Telstra channel.

**Pricing:** Starting at approximately $25/vehicle/month [SelectHub](https://www.selecthub.com/p/fleet-management-software/teletrac-navman/), scaling with fleet size and modules. Hardware costs additional (OBD or hardwired device per vehicle). Contract terms typically 12–36 months.

**Target customer:** Commercial fleets of all sizes — construction, transport, retail. Strong Australian enterprise and mid-market penetration via Telstra.

**Australian prevalence:** Very high — one of the dominant fleet telematics providers in Australia. Widely used in transport and logistics businesses.

**Market quote:** _"Teletrac Navman's TN360 is the best for understanding fleet data."_ (Expert Market)

**Gaps as my business owner:**

- This is telematics, not delivery management — no routing, no dispatch, no customer notifications, no proof of delivery
- No integration with delivery manifests or client systems
- Driver scorecards exist but are not connected to delivery performance or FTD data
- Requires separate routing and DMS tools to be useful operationally — another system to stitch together
- User reviews note poor customer support and integration limitations

---

## 6. 🇺🇸 Routific

**What they do:** Route optimisation with a clean, simple interface. Schedules routes, tracks drivers, sends customer ETAs. Designed for ease of use over feature depth.

**Pricing:** Order-based pricing — approximately $150/month for up to 1,000 orders/month, scaling linearly above that.

**Target customer:** Small-to-mid delivery teams that want lightweight, easy route planning. Not designed for high-complexity multi-client operations.

**Australian prevalence:** Low-to-moderate. Used by smaller Australian operators, but less common at the 30+ vehicle scale.

**Market quote:** _"Routific offers intelligent route optimization with features like driver tracking, customer notifications, and analytics — best for businesses focused on reducing delivery times and fuel expenses."_

**Gaps as my business owner:**

- Too lightweight for my scale — designed for simple delivery, not multi-client complexity
- No manifest ingestion or data normalisation
- No exception management or real-time intervention capability
- No client-specific reporting
- Pricing scales steeply with order volume — at 3,000+ deliveries/day, cost becomes prohibitive

---

## The Consistent Gaps Across ALL of Them

This is the critical insight for your product positioning. None of these platforms solve my five biggest problems together:

**1. Intelligent manifest ingestion** — Nobody automatically normalises multi-format client data before it hits routing. This is still universally manual.

**2. Predictive FTD reduction** — Platforms track failures after they happen. Nobody predicts which deliveries are at risk _before_ the driver leaves the depot based on recipient patterns, address history, or time-of-day intelligence.

**3. Mid-day dynamic exception alerting** — "Your run is falling behind and these 8 stops are now at risk" — nobody does this proactively. It's passive maps, not active intervention.

**4. Multi-client automated reporting** — Every platform generates generic reports. None auto-format bespoke outputs per client (their format, their portal, their SLA metrics).

**5. Unified profitability analytics** — No platform tells me _which client_ is making or losing me money at the run level. They show me operational data, not business intelligence.

The platforms all solve pieces. Nobody connects the full operational picture from inbound manifest to outgoing client invoice with AI embedded throughout.

---

## Summary Table

|Platform|Pricing (AUD est.)|Target Segment|Primary Function|AU Prevalence|Website|
|---|---|---|---|---|---|
|**Locate2u**|$15–$55/seat/mo; $260+/mo for teams|Aus SMB operators|All-in-one DMS|⭐⭐⭐⭐ High|[locate2u.com](https://www.locate2u.com)|
|**Onfleet**|$550–$1,265+/mo (task-based)|Mid-market operators|Delivery mgmt + dispatch|⭐⭐⭐ Moderate|[onfleet.com](https://onfleet.com)|
|**OptimoRoute**|~$39–49/driver/mo|SMB delivery & field service|Route optimisation|⭐⭐⭐ Moderate|[optimoroute.com](https://optimoroute.com)|
|**Shippit**|Custom (vol-based, ~$100–500+/mo)|Retailers & e-commerce|Multi-carrier shipping|⭐⭐⭐⭐⭐ Very High|[shippit.com](https://www.shippit.com)|
|**Teletrac Navman**|From $25/vehicle/mo + hardware|Commercial fleets, enterprise|Fleet telematics & GPS|⭐⭐⭐⭐ High|[teletracnavman.com.au](https://www.teletracnavman.com.au)|
|**Routific**|From ~$150/mo (order-based)|Small delivery teams|Route optimisation|⭐⭐ Low-moderate|[routific.com](https://routific.com)|

**The white space:** An AI-native platform that connects manifest intake → intelligent routing → live exception alerting → automated client reporting → profitability analytics in one workflow built for the Australian SMB operator running 20–100 vehicles. None of the above do this end-to-end.