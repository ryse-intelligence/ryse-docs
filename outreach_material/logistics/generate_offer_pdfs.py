#!/usr/bin/env python3
"""
Ryse Intelligence — Logistics Sales Outreach: Web Offer PDFs
Theme: Clean Signal | Brand: #45b7f7 | A4 single page
Generates 3 personalised offer PDFs (btk, vfs, tri) with QR codes.
"""

import os, sys, base64, tempfile

os.system("pip install weasyprint qrcode[pil] pypdf --break-system-packages -q")

import qrcode
from qrcode.image.pure import PyPNGImage
from weasyprint import HTML
from pypdf import PdfReader

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR   = "/Users/rjiang/dev/odocs/outreach_material/logistics"
QR_DIR     = os.path.join(BASE_DIR, "QRs")
OUTPUT_DIR = os.path.join(BASE_DIR, "pdfs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Brand Tokens ──────────────────────────────────────────────────────────────
B = {
    "primary":     "#0A0A0A",
    "accent":      "#45b7f7",
    "bg":          "#FFFFFF",
    "card_bg":     "#FFFFFF",
    "body_text":   "#1A1F36",
    "muted":       "#6B7280",
    "divider":     "#E5E7EB",
    "accent_pale": "#EEF9FF",
    "navy_pale":   "#F0F4FF",
}

M  = 6    # page margin mm
FB = M + 9  # footer bottom margin — reserves space for @page footer

FOOTER_L = "Ryse Intelligence  ·  AI + Software & Data Consultancy"
FOOTER_R = "0420 560 617  ·  ryanjiang5@gmail.com  ·  getryse.io  ·  2026-03-10"

CALENDAR_URL = "https://calendar.app.google/rtbUjwWUXhSiVBACA"

# ── Step 1: Generate calendar QR code ────────────────────────────────────────
print("Generating calendar QR code...")
cal_qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=2,
)
cal_qr.add_data(CALENDAR_URL)
cal_qr.make(fit=True)
cal_img = cal_qr.make_image(fill_color="black", back_color="white")

cal_qr_path = os.path.join(tempfile.gettempdir(), "ryse_calendar_qr.png")
cal_img.save(cal_qr_path)
print(f"  Saved calendar QR to {cal_qr_path}")

# ── Step 2: Base64 encode all QR images ──────────────────────────────────────
def b64_png(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

cal_qr_b64 = b64_png(cal_qr_path)
print("  Calendar QR encoded.")

PROSPECTS = [
    {"name": "btk",  "label": "BTK",  "filename": "web-offer-btk.pdf"},
    {"name": "vfs",  "label": "VFS",  "filename": "web-offer-vfs.pdf"},
    {"name": "tri",  "label": "TRI",  "filename": "web-offer-tri.pdf"},
]

for p in PROSPECTS:
    qr_path = os.path.join(QR_DIR, f"qr-code-{p['name']}.png")
    p["site_qr_b64"] = b64_png(qr_path)
    print(f"  Site QR for {p['name']} encoded.")

# ── CSS ───────────────────────────────────────────────────────────────────────
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

html, body {{
  height: 100%;
}}

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
  margin: -{M}mm -{M}mm 0 -{M}mm;
  padding: 9mm {M+5}mm 8mm {M+5}mm;
}}
.eyebrow {{
  font-size: 6.5pt; font-weight: 700;
  letter-spacing: 2.5px; text-transform: uppercase;
  color: {B['accent']}; margin-bottom: 3mm;
}}
.doc-title {{
  font-family: 'DM Serif Display', Georgia, serif;
  font-size: 26pt; font-weight: 400; font-style: italic;
  color: #FFFFFF; line-height: 1.18; margin-bottom: 2.5mm;
}}
.doc-subtitle {{
  font-size: 10pt; font-weight: 300;
  color: rgba(255,255,255,0.72); line-height: 1.5;
}}

/* ── HERO CALLOUT ── */
.hero-callout {{
  background: {B['accent']};
  color: white;
  padding: 5mm 6mm;
  margin: 5mm 0 4mm 0;
  border-radius: 4pt;
  page-break-inside: avoid;
}}
.hero-callout-text {{
  font-family: 'DM Serif Display', Georgia, serif;
  font-size: 13pt; font-style: italic;
  line-height: 1.45; color: white;
}}

/* ── BODY COPY ── */
.body-section {{
  margin: 0 0 3.5mm 0;
}}
.body-section p {{
  font-size: 9.5pt;
  color: {B['body_text']};
  line-height: 1.58;
  margin-bottom: 2.5mm;
}}
.body-section p:last-child {{
  margin-bottom: 0;
}}
.body-section p strong {{
  color: {B['primary']};
  font-weight: 700;
}}

/* ── QR SECTION ── */
.qr-row {{
  display: flex;
  gap: 5mm;
  margin: 4mm 0 3mm 0;
  page-break-inside: avoid;
}}
.qr-card {{
  flex: 1;
  background: {B['bg']};
  border: 1pt solid {B['divider']};
  border-radius: 5pt;
  padding: 4mm 4mm 3mm 4mm;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  page-break-inside: avoid;
}}
.qr-card-label {{
  font-size: 6.5pt; font-weight: 700;
  letter-spacing: 2px; text-transform: uppercase;
  color: {B['primary']};
  margin-bottom: 3mm;
}}
.qr-card img {{
  width: 50mm; height: 50mm;
  display: block;
  padding: 2mm;
  border: 0.5pt solid {B['divider']};
  border-radius: 3pt;
  background: white;
}}
.qr-card-caption {{
  font-size: 7.5pt;
  color: {B['muted']};
  margin-top: 2.5mm;
  line-height: 1.45;
}}

/* ── AMBIENT NOTE ── */
.ambient-note {{
  border-left: 2pt solid {B['divider']};
  padding: 2.5mm 0 2.5mm 4mm;
  margin: 4mm 0 3mm 0;
  page-break-inside: avoid;
}}
.ambient-note {{
  font-size: 8pt;
  font-style: italic;
  color: {B['muted']};
  line-height: 1.55;
}}
.ambient-note-icon {{
  color: {B['divider']};
  margin-right: 1.5mm;
}}

/* ── URGENCY STRIP ── */
.urgency-strip {{
  background: {B['primary']};
  color: {B['accent']};
  text-align: center;
  padding: 2.5mm 4mm;
  border-radius: 3pt;
  font-size: 7pt; font-weight: 700;
  letter-spacing: 1.5px; text-transform: uppercase;
  margin: 3mm 0 0 0;
  page-break-inside: avoid;
}}

.no-break {{ page-break-inside: avoid; }}
"""


def build_html(prospect_label, site_qr_b64, cal_qr_b64_data):
    pcss = PAGE_CSS()
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<style>{pcss}
{SHARED_CSS}
</style></head>
<body>

<div class="doc-header">
  <div class="eyebrow">AI-POWERED WEB REDESIGN  ·  COMPLIMENTARY OFFER</div>
  <h1 class="doc-title">Your New Website is Ready.</h1>
  <p class="doc-subtitle">We built it overnight. You can have it today.</p>
</div>

<div class="hero-callout">
  <div class="hero-callout-text">In the time it takes to read this, our AI agent rebuilt your website — from scratch.</div>
</div>

<div class="body-section">
  <p>We noticed your current site isn't doing your business justice. So we put our autonomous AI agent to work — overnight, while your competitors slept, it redesigned a fully functional, modern website for you (and 50 other logistics businesses we've reached out to this week).</p>
  <p>No brief. No back-and-forth. No waiting weeks for a developer. Just a better web presence, <strong>ready now.</strong></p>
  <p>But here's the real question: if it can rebuild a website overnight — <strong>imagine what it could do for your business.</strong> What if it could automate the repetitive, toilsome tasks that are slowing your teams down, creating errors, and ultimately limiting your growth and margin?</p>
  <p>Scan the QR code on the left to see your new website. If you like what you see — it's yours, <strong>completely free</strong>, with no strings attached. All we ask is 30 minutes of your time for a strategy call.</p>
  <p>Whether we end up working together or not, the site is yours to keep. We just want to show you what's possible when AI is on your side.</p>
  <p>This offer is open for <strong>14 days</strong>. After that, we move on to the next business.</p>
</div>

<div class="qr-row">
  <div class="qr-card">
    <div class="qr-card-label">YOUR NEW WEBSITE</div>
    <img src="{site_qr_b64}" alt="Website QR code" />
    <div class="qr-card-caption">See your AI-rebuilt site</div>
  </div>
  <div class="qr-card">
    <div class="qr-card-label">BOOK YOUR FREE CALL</div>
    <img src="{cal_qr_b64_data}" alt="Calendar booking QR code" />
    <div class="qr-card-caption">30 mins · No obligation · Keep the site either way</div>
  </div>
</div>

<div class="ambient-note">
  <span class="ambient-note-icon">&#x2014;</span>
  This outreach — the lead research, market analysis, copywriting, and graphic design — was produced entirely by our AI agents and the specialised workflows we've built around them. We have no researchers or designers on staff. If this is what AI can do for <em>us</em>, imagine what it could do for <em>your</em> team.
</div>

<div class="urgency-strip">
  Offer expires in 14 days · getryse.io · 0420 560 617
</div>

</body></html>"""


# ── Step 3: Render PDFs ───────────────────────────────────────────────────────
print("\nRendering PDFs...")
for p in PROSPECTS:
    html_str = build_html(p["label"], p["site_qr_b64"], cal_qr_b64)
    out_path  = os.path.join(OUTPUT_DIR, p["filename"])

    # Save HTML preview for debugging
    preview_path = out_path.replace(".pdf", ".html")
    with open(preview_path, "w", encoding="utf-8") as f:
        f.write(html_str)

    print(f"  Rendering {p['filename']} ...")
    try:
        HTML(string=html_str, base_url=".").write_pdf(out_path)
        print(f"    ✓  {out_path}")
    except Exception as e:
        print(f"    ✗  ERROR: {e}")
        sys.exit(1)

# ── Step 4: Audit ─────────────────────────────────────────────────────────────
print("\n=== AUDIT ===")
all_ok = True
for p in PROSPECTS:
    path = os.path.join(OUTPUT_DIR, p["filename"])
    try:
        size = os.path.getsize(path)
        reader = PdfReader(path)
        n_pages = len(reader.pages)
        issues = []
        if size < 8000:
            issues.append("CRITICAL: file too small")
        if n_pages != 1:
            issues.append(f"WARN: expected 1 page, got {n_pages}")
        status = "OK" if not issues else "  |  ".join(issues)
        if issues:
            all_ok = False
        print(f"  {p['filename']}: {n_pages}p  {size//1024}KB  — {status}")
    except Exception as e:
        print(f"  {p['filename']}: ERROR — {e}")
        all_ok = False

# ── Step 5: Verify all 3 files exist ─────────────────────────────────────────
print("\n=== FILE VERIFICATION ===")
for p in PROSPECTS:
    path = os.path.join(OUTPUT_DIR, p["filename"])
    exists = os.path.isfile(path)
    print(f"  {p['filename']}: {'EXISTS' if exists else 'MISSING'}")
    if not exists:
        all_ok = False

print("\n✓ All done." if all_ok else "\n⚠ Some issues found — review above.")
