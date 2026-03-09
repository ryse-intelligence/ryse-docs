#!/usr/bin/env python3
"""
Ryse Intelligence — Logistics Outreach Suite
Theme: Clean Signal | Brand: #45b7f7 | A4
Generates all 5 outreach PDFs with a shared design system.
"""

import os, sys

os.system("pip install weasyprint jinja2 pypdf --break-system-packages -q")

from weasyprint import HTML
from pypdf import PdfReader

# ── Brand Tokens (Clean Signal + custom #45b7f7) ──────────────────────────────
B = {
    "accent":       "#45b7f7",
    "primary":      "#0A0A0A",
    "bg":           "#FFFFFF",
    "card_bg":      "#FFFFFF",
    "body_text":    "#1A1F36",
    "muted":        "#6B7280",
    "divider":      "#E5E7EB",
    "accent_pale":  "#EEF9FF",
}

M  = 6   # page margin mm
FB = M + 9  # footer bottom mm — reserves space for @page footer

FOOTER_L = "Ryse Intelligence  ·  AI + Software & Data Consultancy"
FOOTER_R = "0420 560 617  ·  ryanjiang5@gmail.com  ·  getryse.io  ·  2026-03-09"


def PAGE_CSS():
    return f"""
@page {{
  size: A4;
  margin: {M}mm {M}mm {FB}mm {M}mm;

  @bottom-left {{
    content: "{FOOTER_L}";
    font-family: 'DM Sans', 'Helvetica Neue', sans-serif;
    font-size: 7.5pt; font-weight: 700;
    color: {B['accent']};
    vertical-align: top; padding-top: 2mm;
    border-top: 0.5pt solid {B['divider']};
  }}
  @bottom-right {{
    content: "{FOOTER_R}";
    font-family: 'DM Sans', 'Helvetica Neue', sans-serif;
    font-size: 7pt; color: {B['muted']};
    vertical-align: top; padding-top: 2mm;
    border-top: 0.5pt solid {B['divider']};
  }}
}}"""


SHARED_CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap');

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  background: {B['bg']};
  font-family: 'DM Sans', 'Helvetica Neue', sans-serif;
  font-size: 9.5pt;
  color: {B['body_text']};
  line-height: 1.5;
}}

/* ── HEADER ── */
.doc-header {{
  background: {B['primary']};
  margin: -{M}mm -{M}mm 5mm -{M}mm;
  padding: 8mm {M+4}mm 7mm {M+4}mm;
}}
.eyebrow {{
  font-size: 6.5pt; font-weight: 700;
  letter-spacing: 2.5px; text-transform: uppercase;
  color: {B['accent']}; margin-bottom: 2.5mm;
}}
.doc-title {{
  font-family: 'DM Serif Display', Georgia, serif;
  font-size: 21pt; font-weight: 400; font-style: italic;
  color: #FFFFFF; line-height: 1.22; margin-bottom: 2mm;
}}
.doc-subtitle {{
  font-size: 9.5pt; font-weight: 300;
  color: rgba(255,255,255,0.70); line-height: 1.5;
}}

/* ── STRUCTURE ── */
.section {{ margin-bottom: 4mm; }}
.section-label {{
  font-size: 7pt; font-weight: 700;
  letter-spacing: 2px; text-transform: uppercase;
  color: {B['muted']}; margin-bottom: 2.5mm;
  padding-bottom: 1.5mm; border-bottom: 0.5pt solid {B['divider']};
}}

/* ── CARDS ── */
.card {{
  background: {B['card_bg']};
  border-radius: 3pt; padding: 3mm 4mm;
  margin-bottom: 2mm; page-break-inside: avoid;
}}
.card-accent {{
  border-left: 2.5pt solid {B['accent']};
  background: {B['accent_pale']};
}}

/* ── CALLOUT (hero element — accent bg) ── */
.callout {{
  background: {B['accent']};
  color: white; padding: 4mm 5mm;
  border-radius: 3pt; margin: 3mm 0;
  page-break-inside: avoid;
}}
.callout-serif {{
  font-family: 'DM Serif Display', Georgia, serif;
  font-size: 12.5pt; font-style: italic; line-height: 1.5; color: white;
}}
.callout-body {{
  font-size: 9pt; color: rgba(255,255,255,0.9);
  margin-top: 2mm; line-height: 1.5;
}}

/* ── PROCESS STEPS ── */
.step {{
  display: flex; gap: 3.5mm;
  background: {B['card_bg']}; border-radius: 3pt;
  padding: 3mm 4mm; margin-bottom: 2mm;
  page-break-inside: avoid;
}}
.step-num {{
  font-family: 'DM Serif Display', Georgia, serif;
  font-size: 18pt; color: {B['accent']};
  line-height: 1; min-width: 8mm; flex-shrink: 0;
}}
.step-body h4 {{
  font-size: 10pt; font-weight: 700;
  color: {B['primary']}; margin-bottom: 1mm;
}}
.step-body p {{ font-size: 9pt; color: {B['body_text']}; line-height: 1.45; }}

/* ── LIFECYCLE STAGES ── */
.stage {{
  background: {B['card_bg']}; border-radius: 3pt;
  padding: 3mm 4mm; margin-bottom: 2mm;
  page-break-inside: avoid;
}}
.stage-header {{
  display: flex; align-items: baseline; gap: 3mm;
  padding-bottom: 1.5mm; margin-bottom: 2mm;
  border-bottom: 0.5pt solid {B['divider']};
}}
.stage-n  {{ font-family: 'DM Serif Display', Georgia, serif; font-size: 12pt; color: {B['accent']}; }}
.stage-name {{ font-weight: 700; font-size: 10pt; color: {B['primary']}; }}
.stage-time {{
  font-size: 7pt; font-weight: 600; color: {B['muted']};
  text-transform: uppercase; letter-spacing: 1px;
}}
.stage-cols {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 3mm; }}
.col-tag {{
  font-size: 6.5pt; font-weight: 700;
  text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 1.5mm;
}}
.col-tag.sq  {{ color: #E55A1C; }}
.col-tag.ai  {{ color: {B['accent']}; }}
.col-tag.out {{ color: #16A34A; }}
.col-text {{ font-size: 8.5pt; color: {B['body_text']}; line-height: 1.45; }}

/* ── AUDIT ROWS ── */
.audit-row {{
  display: flex; gap: 3mm; align-items: flex-start;
  padding: 2mm 2.5mm; border-radius: 2pt;
  margin-bottom: 1mm; background: {B['card_bg']};
}}
.audit-row.fragile {{ border-left: 2.5pt solid #E55A1C; }}
.audit-row.stable  {{ border-left: 2.5pt solid #F59E0B; }}
.audit-row.opt     {{ border-left: 2.5pt solid #22C55E; }}
.audit-badge {{
  font-size: 6pt; font-weight: 700; text-transform: uppercase;
  letter-spacing: 1px; padding: 1mm 2mm; border-radius: 2pt;
  white-space: nowrap; min-width: 17mm; text-align: center; flex-shrink: 0;
}}
.b-fragile {{ background: #FFF1EE; color: #E55A1C; }}
.b-stable  {{ background: #FFFBEB; color: #D97706; }}
.b-opt     {{ background: #F0FDF4; color: #16A34A; }}
.audit-checkbox {{
  width: 4mm; height: 4mm;
  border: 1pt solid {B['divider']}; border-radius: 1pt;
  flex-shrink: 0; margin-top: 0.5mm;
}}
.audit-text {{ font-size: 9pt; color: {B['body_text']}; line-height: 1.45; flex: 1; }}

/* ── TRENDS ── */
.trend {{
  background: {B['card_bg']}; border-radius: 3pt;
  padding: 3mm 4mm; margin-bottom: 2.5mm;
  page-break-inside: avoid;
}}
.trend-rows {{ display: flex; flex-direction: column; gap: 1mm; }}
.trend-row  {{ display: flex; gap: 3mm; align-items: flex-start; }}
.trend-num  {{
  font-family: 'DM Serif Display', Georgia, serif;
  font-size: 20pt; color: {B['accent']}; line-height: 1; margin-bottom: 2mm;
}}
.trend-title {{ font-weight: 700; font-size: 10pt; color: {B['primary']}; margin-bottom: 2.5mm; }}
.trend-pill {{
  font-size: 6pt; font-weight: 700; text-transform: uppercase;
  letter-spacing: 1px; padding: 1mm 2mm; border-radius: 2pt;
  white-space: nowrap; min-width: 18mm; text-align: center; flex-shrink: 0;
}}
.p-shift {{ background: #F3F4F6; color: #4B5563; }}
.p-ai    {{ background: {B['accent_pale']}; color: {B['accent']}; }}
.p-roi   {{ background: #F0FDF4; color: #16A34A; }}
.trend-row-text {{ font-size: 9pt; color: {B['body_text']}; line-height: 1.45; }}

/* ── COMPARISON TABLE ── */
.compare {{ width: 100%; border-collapse: collapse; margin-bottom: 4mm; }}
.compare th {{
  font-size: 7pt; font-weight: 700; text-transform: uppercase;
  letter-spacing: 1.5px; padding: 2.5mm 3.5mm; text-align: left;
}}
.th-challenge {{ background: {B['primary']}; color: white; width: 26%; }}
.th-tech      {{ background: {B['accent_pale']}; color: {B['accent']}; width: 37%; }}
.th-logistics {{ background: {B['accent']}; color: white; width: 37%; }}
.compare td {{
  font-size: 8.5pt; padding: 3mm 3.5mm; vertical-align: top;
  line-height: 1.45; border-bottom: 0.5pt solid {B['divider']};
}}
.td-challenge {{ background: #F3F4F6; font-weight: 600; color: {B['primary']}; }}
.td-tech      {{ background: {B['accent_pale']}; color: {B['body_text']}; }}
.td-logistics {{ background: #F0FFF4; color: {B['body_text']}; }}

.no-break {{ page-break-inside: avoid; }}
h2, h3   {{ page-break-after: avoid; }}
"""


def make_doc(title, subtitle, eyebrow, body_html):
    pcss = PAGE_CSS()
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<style>{pcss}
{SHARED_CSS}
</style></head>
<body>
<div class="doc-header">
  <div class="eyebrow">{eyebrow}</div>
  <h1 class="doc-title">{title}</h1>
  <p class="doc-subtitle">{subtitle}</p>
</div>
{body_html}
</body></html>"""


# ═══════════════════════════════════════════════════════════════════════════════
# DOC 1 — Ryse Consultancy Intro
# ═══════════════════════════════════════════════════════════════════════════════
DOC1 = make_doc(
    title    = "Engineering Operational Leverage",
    subtitle = "At Ryse, we don't sell generic solutions — we solve your specific, painful bottlenecks.",
    eyebrow  = "Ryse Intelligence  ·  Introduction",
    body_html = """
<div class="section">
  <div class="section-label">The Problem with Generic Software in Logistics</div>
  <div class="card card-accent">
    <p><strong>Most tech vendors sell you a one-size-fits-all software license, hand you a manual, and walk away.</strong> You don't need another tool your team has to learn — you need your specific, painful problems solved across teams and operation checkpoints.</p>
  </div>
</div>

<div class="section">
  <div class="section-label">The Ryse Approach</div>
  <div class="card">
    <p>At Ryse, we are a specialised tech and AI consultancy. We bring the expertise, knowledge, and systems from global tech giants to local Aussie businesses. We don't force you into a single ecosystem — we analyze your unique <strong>"Profit Leakers,"</strong> design a bespoke strategy, and build custom automation that fits <em>your</em> workflow.</p>
  </div>
</div>

<div class="callout">
  <div class="callout-serif">Guaranteed problem-solution fit.</div>
  <div class="callout-body">Your primary investment is simply the time to let us understand your business. We handle the heavy lifting of the technology.</div>
</div>

<div class="section">
  <div class="section-label">Our Engagement Process</div>

  <div class="step">
    <div class="step-num">1</div>
    <div class="step-body">
      <h4>The Workflow X-Ray</h4>
      <p>We sit with your Operations Manager. We observe the 90-minute morning data intake, the mid-day routing chaos, and the manual end-of-day billing — and quantify exactly how much this friction is costing you.</p>
    </div>
  </div>

  <div class="step">
    <div class="step-num">2</div>
    <div class="step-body">
      <h4>The Architecture Blueprint</h4>
      <p>We design a tailored AI+technology roadmap. Whether automating manifest ingestion or deploying predictive FTD alerts, we show you the expected ROI before any commitment.</p>
    </div>
  </div>

  <div class="step">
    <div class="step-num">3</div>
    <div class="step-body">
      <h4>Precision Implementation</h4>
      <p>We build and deploy solutions without ripping out your core systems. We build intelligent, automated layers that connect your existing tools and bridge the manual gaps.</p>
    </div>
  </div>

  <div class="step">
    <div class="step-num">4</div>
    <div class="step-body">
      <h4>Enablement &amp; Change Management</h4>
      <p>Technology is useless if your dispatchers hate it. We are deeply involved on the floor, training your team until the new automated workflow becomes second nature.</p>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-label">Limited Offer — This Month Only</div>
  <div class="card card-accent">
    <p>We are offering <strong>3 local logistics firms</strong> a complimentary <strong>25-Minute Workflow X-Ray</strong> this month. No sales pitch — just a whiteboard session to map out how much your manual data intake and delivery failures are actually costing you.</p>
  </div>
</div>
""")


# ═══════════════════════════════════════════════════════════════════════════════
# DOC 2 — AI Industry Map
# ═══════════════════════════════════════════════════════════════════════════════
DOC2 = make_doc(
    title    = "The Modern Delivery Lifecycle",
    subtitle = "Where AI+ Technology uplifts revenue, operational efficiency, and customer satisfaction across every stage.",
    eyebrow  = "Ryse Intelligence  ·  Operations Blueprint",
    body_html = """
<div class="section">
  <div class="section-label">The Five Stages — Status Quo vs AI Intervention vs Outcome</div>

  <div class="stage">
    <div class="stage-header">
      <span class="stage-n">01</span>
      <span class="stage-name">Start of Day — Data Intake &amp; Normalisation</span>
      <span class="stage-time">Morning</span>
    </div>
    <div class="stage-cols">
      <div><div class="col-tag sq">Status Quo</div><div class="col-text">90+ minutes manually standardising CSVs, EDI, and portal data. High risk of human error.</div></div>
      <div><div class="col-tag ai">AI Intervention</div><div class="col-text"><strong>Automated Data Ingestion.</strong> AI instantly reads, cleans, and standardises disparate client manifests into a single source of truth — in seconds.</div></div>
      <div><div class="col-tag out">Outcome</div><div class="col-text">Zero manual entry errors; dispatchers get <strong>1.5 hours back</strong> every morning.</div></div>
    </div>
  </div>

  <div class="stage">
    <div class="stage-header">
      <span class="stage-n">02</span>
      <span class="stage-name">Busy Morning — Depot Logistics &amp; Sorting</span>
      <span class="stage-time">Pre-Dispatch</span>
    </div>
    <div class="stage-cols">
      <div><div class="col-tag sq">Status Quo</div><div class="col-text">Manual LIFO loading and gut-feel labour scheduling leading to mis-sorts and wasteful resource allocations.</div></div>
      <div><div class="col-tag ai">AI Intervention</div><div class="col-text"><strong>Predictive Volume Forecasting.</strong> System flags sorting anomalies before the truck leaves the dock.</div></div>
      <div><div class="col-tag out">Outcome</div><div class="col-text">Eradicates <strong>30km+ deadhead trips</strong> caused by wrong-truck loading.</div></div>
    </div>
  </div>

  <div class="stage">
    <div class="stage-header">
      <span class="stage-n">03</span>
      <span class="stage-name">On the Road — Dispatch &amp; Route Generation</span>
      <span class="stage-time">In-Transit</span>
    </div>
    <div class="stage-cols">
      <div><div class="col-tag sq">Status Quo</div><div class="col-text">Static routing that cannot adapt to traffic, weather, or midday variables.</div></div>
      <div><div class="col-tag ai">AI Intervention</div><div class="col-text"><strong>Dynamic Route Resilience.</strong> AI generates optimal baseline routes and instantly recalculates based on live constraints.</div></div>
      <div><div class="col-tag out">Outcome</div><div class="col-text">Maximises stop-density and <strong>reduces fuel consumption</strong>.</div></div>
    </div>
  </div>

  <div class="stage">
    <div class="stage-header">
      <span class="stage-n">04</span>
      <span class="stage-name">Delivery — Last-Mile &amp; Exception Handling</span>
      <span class="stage-time">Last Mile</span>
    </div>
    <div class="stage-cols">
      <div><div class="col-tag sq">Status Quo</div><div class="col-text">12–15% First-Time Delivery (FTD) failure rate. Reactive re-routing takes 45 minutes of manual coordination.</div></div>
      <div><div class="col-tag ai">AI Intervention</div><div class="col-text"><strong>Predictive FTD Management.</strong> Automated comms based on recipient behaviour models with instant algorithmic re-routing.</div></div>
      <div><div class="col-tag out">Outcome</div><div class="col-text">Recoups redundant labour/fuel costs; turns "firefighting" into <strong>automated exception handling</strong>.</div></div>
    </div>
  </div>

  <div class="stage">
    <div class="stage-header">
      <span class="stage-n">05</span>
      <span class="stage-name">End of Day — Reconciliation &amp; Billing</span>
      <span class="stage-time">EOD</span>
    </div>
    <div class="stage-cols">
      <div><div class="col-tag sq">Status Quo</div><div class="col-text">2 hours of manual end-of-day POD cross-referencing. High invoice disputes.</div></div>
      <div><div class="col-tag ai">AI Intervention</div><div class="col-text"><strong>Automated Audit Trails.</strong> AI matches PODs to manifests and triggers clean, dispute-free invoices instantly.</div></div>
      <div><div class="col-tag out">Outcome</div><div class="col-text">Radically lowers <strong>Days Sales Outstanding (DSO)</strong> and administrative overhead.</div></div>
    </div>
  </div>
</div>

<div class="callout">
  <div class="callout-serif">Where vertical SaaS products miss the mark.</div>
  <div class="callout-body">Generic software is helpful, but built for everybody. Your operations need purposely-built intelligent integrations that solve complex business problems holistically — across every stage of the delivery lifecycle.</div>
</div>
""")


# ═══════════════════════════════════════════════════════════════════════════════
# DOC 3 — Operational Readiness Audit
# ═══════════════════════════════════════════════════════════════════════════════
DOC3 = make_doc(
    title    = "The 60-Second Logistics Profitability Audit",
    subtitle = "Are manual processes capping your growth? Check the box that best describes your current daily operations.",
    eyebrow  = "Ryse Intelligence  ·  Self-Assessment Tool",
    body_html = """
<div class="section">
  <div class="section-label">Section 1 — The Morning Rush (Data &amp; Dispatch)</div>
  <div class="audit-row fragile">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-fragile">Fragile</span>
    <div class="audit-text">We spend over 1 hour daily manually standardising client data (CSVs, Portals) before routes can even be planned.</div>
  </div>
  <div class="audit-row stable">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-stable">Stable</span>
    <div class="audit-text">Data intake is partially automated, but still requires manual review and formatting.</div>
  </div>
  <div class="audit-row opt">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-opt">Optimised</span>
    <div class="audit-text">Client data is ingested, standardised, and ready for dispatch automatically in seconds.</div>
  </div>
</div>

<div class="section">
  <div class="section-label">Section 2 — Route Execution &amp; Mid-Day Exceptions</div>
  <div class="audit-row fragile">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-fragile">Fragile</span>
    <div class="audit-text">When a truck breaks down or a rush order drops, it takes 30+ minutes of manual phone calls and white-boarding to re-route.</div>
  </div>
  <div class="audit-row stable">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-stable">Stable</span>
    <div class="audit-text">We have software, but dispatchers still have to manually drag-and-drop stops to fix mid-day issues.</div>
  </div>
  <div class="audit-row opt">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-opt">Optimised</span>
    <div class="audit-text">The system autonomously proposes optimised re-routes instantly when exceptions occur.</div>
  </div>
</div>

<div class="section">
  <div class="section-label">Section 3 — The Last-Mile Leak (First-Time Delivery)</div>
  <div class="audit-row fragile">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-fragile">Fragile</span>
    <div class="audit-text">Our First-Time Delivery (FTD) failure rate is over 10%. We only know about a failed delivery after the driver leaves the doorstep.</div>
  </div>
  <div class="audit-row stable">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-stable">Stable</span>
    <div class="audit-text">We send generic tracking links, but still suffer from high recipient no-shows.</div>
  </div>
  <div class="audit-row opt">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-opt">Optimised</span>
    <div class="audit-text">We use predictive text and automated workflows to confirm recipient availability before the truck arrives.</div>
  </div>
</div>

<div class="section">
  <div class="section-label">Section 4 — End-of-Day Overhead (Reconciliation)</div>
  <div class="audit-row fragile">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-fragile">Fragile</span>
    <div class="audit-text">It takes 1–2 hours daily to manually cross-reference Proof of Delivery (PODs) with manifests to generate invoices.</div>
  </div>
  <div class="audit-row stable">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-stable">Stable</span>
    <div class="audit-text">We have a system, but billing disputes and high Days Sales Outstanding (DSO) are still common.</div>
  </div>
  <div class="audit-row opt">
    <div class="audit-checkbox"></div>
    <span class="audit-badge b-opt">Optimised</span>
    <div class="audit-text">PODs automatically reconcile against manifests, generating flawless, dispute-free invoices instantly.</div>
  </div>
</div>

<div class="callout">
  <div class="callout-serif">If you checked "Fragile" in two or more categories — you're likely losing profit to invisible operational friction.</div>
  <div class="callout-body">At Ryse, we don't sell generic software subscriptions. We solve your specific, painful bottlenecks and engineer the systems that move you to "Optimised" — without disrupting your current operations.</div>
</div>
""")


# ═══════════════════════════════════════════════════════════════════════════════
# DOC 4 — Executive Brief: 2026 Trends
# ═══════════════════════════════════════════════════════════════════════════════
DOC4 = make_doc(
    title    = "Executive Brief: 2026 Logistics Trends",
    subtitle = "How couriers and 3PL operators are using technology to reclaim margins.",
    eyebrow  = "Ryse Intelligence  ·  Market Intelligence",
    body_html = """
<div class="section">
  <div class="section-label">Context — The 2026 Margin Challenge</div>
  <div class="card card-accent">
    <p>The 3PL and courier landscape is facing unprecedented margin compression. Between rising SLA demands, fluctuating fuel costs, and labour shortages, top-performing firms are no longer relying on "working harder" or adding headcount. Instead, they are engineering <strong>operational leverage through AI</strong>.</p>
  </div>
</div>

<div class="section">
  <div class="section-label">Trend 01 — Hyper-Automated Interoperability &amp; API Ecosystems</div>
  <div class="trend">
    <div class="trend-rows">
      <div class="trend-row">
        <span class="trend-pill p-shift">The Shift</span>
        <div class="trend-row-text">Historically, 3PLs struggled to integrate fragmented client systems, legacy WMS, and modern routing software — resulting in massive manual data entry overhead.</div>
      </div>
      <div class="trend-row">
        <span class="trend-pill p-ai">AI Today</span>
        <div class="trend-row-text">Leading operators now deploy "middleware AI" that autonomously translates and normalises data between completely different systems in real-time, requiring zero human intervention.</div>
      </div>
      <div class="trend-row">
        <span class="trend-pill p-roi">ROI</span>
        <div class="trend-row-text">Early adopters eliminated <strong>30+ hours of weekly manual administration</strong>, enabling new enterprise client onboarding in days rather than months.</div>
      </div>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-label">Trend 02 — Predictive Capacity &amp; Labour Forecasting</div>
  <div class="trend">
    <div class="trend-rows">
      <div class="trend-row">
        <span class="trend-pill p-shift">The Shift</span>
        <div class="trend-row-text">Labour scheduling and fleet allocation have traditionally relied on "gut feel" and lagging historical data — leading to either understaffed chaos or overstaffed waste.</div>
      </div>
      <div class="trend-row">
        <span class="trend-pill p-ai">AI Today</span>
        <div class="trend-row-text">Top-tier firms leverage AI to analyse seasonal trends, local market data, and client forecasts to predict exact daily volume before it arrives at the depot.</div>
      </div>
      <div class="trend-row">
        <span class="trend-pill p-roi">ROI</span>
        <div class="trend-row-text">Couriers reduce daily labour waste by aligning warehouse sorting shifts and driver schedules perfectly with <strong>AI-predicted volume</strong>.</div>
      </div>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-label">Trend 03 — Generative AI for Exception Management (WISMO)</div>
  <div class="trend">
    <div class="trend-rows">
      <div class="trend-row">
        <span class="trend-pill p-shift">The Shift</span>
        <div class="trend-row-text">"Where Is My Order?" (WISMO) calls and missing freight investigations consume massive administrative resources and degrade the customer experience.</div>
      </div>
      <div class="trend-row">
        <span class="trend-pill p-ai">AI Today</span>
        <div class="trend-row-text">Forward-thinking 3PLs deploy AI trained on their specific operational data to autonomously resolve up to <strong>60% of tier-1 customer inquiries</strong> and proactively alert clients about predicted delays.</div>
      </div>
      <div class="trend-row">
        <span class="trend-pill p-roi">ROI</span>
        <div class="trend-row-text">Early adopters see a massive reduction in customer service overhead — transforming support teams from reactive firefighters into proactive account managers.</div>
      </div>
    </div>
  </div>
</div>

<div class="callout">
  <div class="callout-serif">You are sitting on a goldmine of data.</div>
  <div class="callout-body">The companies that will thrive in the next decade are those who embrace AI to automate their administrative tail — allowing their human talent to focus entirely on customer relationships and scalable growth.</div>
</div>
""")


# ═══════════════════════════════════════════════════════════════════════════════
# DOC 5 — Cross-Industry Success Framework
# ═══════════════════════════════════════════════════════════════════════════════
DOC5 = make_doc(
    title    = "The Cross-Industry Success Framework",
    subtitle = "Applying Tier-1 Tech Giant architecture to local logistics operations.",
    eyebrow  = "Ryse Intelligence  ·  Why Ryse",
    body_html = """
<div class="section">
  <div class="section-label">Our Background</div>
  <div class="card card-accent">
    <p>Our background is designing and engineering complex, high-stakes data, software, and AI architectures at global tier-1 tech companies like <strong>Atlassian</strong>, <strong>Canva</strong>, and <strong>Oracle</strong>. We are bringing those exact frameworks to logistics — to help fleets scale efficiently, integrate legacy software, and turn their data into a competitive advantage.</p>
  </div>
</div>

<div class="section">
  <div class="section-label">Enterprise Tech → Logistics: Direct Translation</div>
  <table class="compare">
    <thead>
      <tr>
        <th class="th-challenge">Challenge</th>
        <th class="th-tech">Tech Giant Experience</th>
        <th class="th-logistics">Logistics Application</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="td-challenge">Unifying Fragmented Systems</td>
        <td class="td-tech">Orchestrating millions of distinct API requests and disparate data streams from global enterprise clients into a single, unified, real-time data warehouse — without dropping a single byte.</td>
        <td class="td-logistics"><strong>Eradicating Data Silos.</strong> We apply enterprise data orchestration to seamlessly connect fragmented WMS, routing software, and client portals — ensuring information flows autonomously from order creation to final invoice.</td>
      </tr>
      <tr>
        <td class="td-challenge">Scaling Without Proportional Headcount</td>
        <td class="td-tech">Building "elastic" cloud infrastructures that automatically scale to handle 10x spikes in user traffic — without requiring 10x more engineers.</td>
        <td class="td-logistics"><strong>Non-Linear Operational Growth.</strong> We implement AI + automation that allows your existing team to handle double the freight volume by automating the administrative tail and optimising asset utilisation.</td>
      </tr>
      <tr>
        <td class="td-challenge">Moving from Reactive to Predictive</td>
        <td class="td-tech">Leveraging advanced AI to analyse billions of micro-interactions, automating engineering workflows, and predicting system bottlenecks before they occur.</td>
        <td class="td-logistics"><strong>Predictive Operational Intelligence.</strong> We deploy predictive AI models over your historical data to forecast volume spikes, flag at-risk routes, and predict delays <em>before</em> the truck leaves the depot.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="callout">
  <div class="callout-serif">The Ryse Advantage.</div>
  <div class="callout-body">You are the absolute expert in trucks, pallets, and physical operations. We are the experts in AI, data, automation, and building software systems and integrations. Together, we build a foundation that doesn't just manage your current operation — it accelerates your growth.</div>
</div>
""")


# ═══════════════════════════════════════════════════════════════════════════════
# RENDER ALL
# ═══════════════════════════════════════════════════════════════════════════════
OUTPUT_DIR = "/Users/rjiang/dev/odocs/outreach_material/logistics/pdfs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DOCS = [
    (DOC1, "00_Ryse_Intro.pdf"),
    (DOC2, "01_AI_Industry_Map.pdf"),
    (DOC3, "02_Operational_Readiness_Audit.pdf"),
    (DOC4, "03_Executive_Brief_Trends.pdf"),
    (DOC5, "05_Cross_Industry_Framework.pdf"),
]

for html_str, filename in DOCS:
    out = os.path.join(OUTPUT_DIR, filename)
    # save preview HTML for debugging
    preview = out.replace(".pdf", ".html")
    with open(preview, "w", encoding="utf-8") as f:
        f.write(html_str)
    print(f"Rendering {filename} ...")
    try:
        HTML(string=html_str, base_url=".").write_pdf(out)
        print(f"  ✓  {out}")
    except Exception as e:
        print(f"  ✗  ERROR: {e}")
        sys.exit(1)

# ── Audit ─────────────────────────────────────────────────────────────────────
print("\n=== AUDIT ===")
all_ok = True
for _, filename in DOCS:
    path = os.path.join(OUTPUT_DIR, filename)
    try:
        size = os.path.getsize(path)
        r = PdfReader(path)
        n = len(r.pages)
        issues = []
        if size < 8000:
            issues.append("CRITICAL: file too small")
        for i, page in enumerate(r.pages):
            if len((page.extract_text() or "").strip()) < 50:
                issues.append(f"WARN: page {i+1} nearly empty")
        status = "OK" if not issues else "  |  ".join(issues)
        if issues:
            all_ok = False
        print(f"  {filename}: {n}p  {size//1024}KB  — {status}")
    except Exception as e:
        print(f"  {filename}: ERROR — {e}")
        all_ok = False

print("\n✓ All done." if all_ok else "\n⚠ Some issues found — review above.")
