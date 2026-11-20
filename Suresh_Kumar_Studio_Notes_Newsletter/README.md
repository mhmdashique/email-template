# Suresh Kumar — Studio Notes Newsletter
### November 2026

A fully responsive HTML email newsletter with a matching landing page, built with nested presentation tables and inline CSS.

---

## 📁 Project Structure

```
email template/
│
├── README.md                          ← You are here
│
├── deliverables/                      ← Master working files
│   ├── newsletter.html                ← Master email HTML (source of truth)
│   ├── images/                        ← Optimised email images
│   │   ├── hero_workflow.png
│   │   ├── icon_1_plan.png
│   │   ├── icon_2_build.png
│   │   └── icon_3_improve.png
│   ├── test_matrix.csv                ← Full QA test results
│   ├── technical_summary.md           ← Technical spec & limitations
│   └── evidence/                      ← Screenshot & static-check evidence
│       ├── desktop_1440.png
│       ├── mobile_375.png
│       ├── viewport_600.png
│       ├── images_blocked_600.png
│       ├── page1_index_1440.png
│       ├── page2_framework_1440.png
│       ├── page2_framework_375.png
│       └── static_checks.txt
│
├── INPUT_FILES/                       ← Source assets & references
│   ├── BRAND_ASSETS/                  ← Logos, icons, hero (PNG + SVG originals)
│   ├── DESIGN_REFERENCES/             ← desktop_1440.png, mobile_375.png (visual ref only)
│   ├── LANDING_PAGE/                  ← Web landing pages
│   │   ├── index.html                 ← Page 1: Promotional landing page
│   │   ├── framework.html             ← Page 2: Checklist + Preferences/Unsub/Contact
│   │   └── images/                    ← Landing page image assets
│   └── QA_RESOURCES/                  ← Starter HTML, spec, content file
│
├── Suresh_Kumar_Studio_Notes_Newsletter/   ← 📦 FINAL SUBMISSION PACKAGE
│   ├── newsletter.html
│   ├── images/
│   ├── LANDING_PAGE/
│   │   ├── index.html
│   │   └── framework.html
│   ├── test_matrix.csv
│   ├── technical_summary.md
│   └── evidence/
│
├── check_static.py                    ← QA: static code checks
├── run_verify.py                      ← QA: full browser + link verification
└── validate_package.py                ← QA: package integrity check
```

---

## 🚀 Local Preview

**Step 1 — Start the local server** (from workspace root):

```bash
python -m http.server 8000 --directory INPUT_FILES
```

**Step 2 — Open in browser:**

| URL | What you see |
|-----|-------------|
| `http://localhost:8000/LANDING_PAGE/index.html` | Promotional landing page |
| `http://localhost:8000/LANDING_PAGE/framework.html` | Checklist + account sections |

> **Email preview:** Open `deliverables/newsletter.html` directly in your browser.  
> Images load correctly when served via the local server.

---

## 📧 Email — newsletter.html

### Design
| Property | Value |
|----------|-------|
| Max width | 600 px |
| Body background | `#FAF8F3` warm white |
| Header | Full-width navy `#132B3D`, live text |
| Accent (teal) | `#007F79` |
| Accent (gold) | `#E0A85F` |
| Muted text | `#54717E` |
| Font | Arial, Helvetica, sans-serif |

### Layout Rules
- `<table role="presentation">` only — no CSS Grid, no Flexbox
- All styles inline; ONE embedded `<style>` with one `@media (max-width:600px)` block
- No JavaScript, no external stylesheets
- File size < 100 KB (images excluded)

### Sections (top → bottom)
1. **Header** — full-width navy band, "SURESH KUMAR" bold white + "STUDIO NOTES / NOVEMBER 2026"
2. **Intro** — eyebrow "A BETTER WAY TO WORK", H1, intro paragraph
3. **Hero** — `hero_workflow.png` illustration
4. **Primary CTA** — teal "EXPLORE THE FRAMEWORK" button
5. **Three Cards** — 01 / CLARITY · 02 / MOMENTUM · 03 / PROGRESS (3-col desktop, stacked mobile)
6. **Banner** — rounded navy block, "Ready for a clearer next week?" + gold "READ THE CHECKLIST"
7. **Footer** — Suresh Kumar | Studio Notes · Preferences · Unsubscribe · Contact

---

## 🌐 Landing Pages

### Page 1 — `index.html` (Promotional)
Mirrors the email design. Centred 600 px column on the warm-white background.

| Element | Destination |
|---------|------------|
| "EXPLORE THE FRAMEWORK" button | `framework.html` |
| "READ THE CHECKLIST" button | `framework.html` |
| Footer — Preferences | `framework.html#preferences` |
| Footer — Unsubscribe | `framework.html#unsubscribe` |
| Footer — Contact | `framework.html#contact` |

### Page 2 — `framework.html` (Content)
All sections scroll-linked. ← back arrow returns to `index.html`.

| Anchor | Section |
|--------|---------|
| `#checklist` | Weekly Workflow Checklist (3 steps) |
| `#preferences` | Subscription Preferences |
| `#unsubscribe` | Opt Out / Unsubscribe |
| `#contact` | Get In Touch |

---

## 🔗 CTA Links

Both email CTAs use this URL (UTM-tagged):

```
http://localhost:8000/LANDING_PAGE/index.html
  ?utm_source=newsletter
  &utm_medium=email
  &utm_campaign=nov2026_studio_notes
```

> ⚠️ **Replace `localhost:8000` with the authorized hosted domain before any send.**  
> No live sending has been performed.

---

## ✅ QA Results Summary

| Test | Condition | Result |
|------|-----------|--------|
| T01 | 375 px viewport — no horizontal scroll | ✅ Pass |
| T02 | 600 px viewport — no horizontal scroll | ✅ Pass |
| T03 | 1440 px — content stays 600 px wide | ✅ Pass |
| T04 | Images blocked — alt text visible | ✅ Pass |
| T05 | CTA links — HTTP 200 OK | ✅ Pass |
| T06 | Footer anchors resolve | ✅ Pass |
| T07 | No JavaScript | ✅ Pass |
| T08 | Inline CSS only (1 media query) | ✅ Pass |
| T09 | Table-only layout | ✅ Pass |
| T10 | Outlook rendering | Not tested — client not available |
| T11 | Gmail mobile rendering | Not tested — client not available |
| T12 | Apple Mail rendering | Not tested — client not available |

Full results with evidence paths: `deliverables/test_matrix.csv`

---

## 🖼️ Image Assets

| File | Displayed | Actual | Use |
|------|-----------|--------|-----|
| `hero_workflow.png` | 552 px | 1104 px @2x | Hero illustration |
| `icon_1_plan.png` | 44 px | 88 px @2x | Card 1 — Clarity |
| `icon_2_build.png` | 44 px | 88 px @2x | Card 2 — Momentum |
| `icon_3_improve.png` | 44 px | 88 px @2x | Card 3 — Progress |

> Icons include the pale aqua tile `#DDF3EE` baked in — no additional wrapper needed.

---

## ⚠️ Known Limitations

- **Localhost URL** — must be replaced with the authorized hosted URL before any distribution
- **Outlook rendering** — rounded corners fall back to square; not tested in Outlook client
- **Email clients T10–T12** — Outlook, Gmail mobile, Apple Mail not tested (no live client available)
- **No live send** — this package is for reviewer upload only

---

## 📦 Delivery

Upload the **`Suresh_Kumar_Studio_Notes_Newsletter/`** folder to Google Drive and share with the authorized reviewer as **Viewer**.

```
Suresh_Kumar_Studio_Notes_Newsletter/
  newsletter.html
  images/
  LANDING_PAGE/
    index.html
    framework.html
    images/
  test_matrix.csv
  technical_summary.md
  evidence/
```

---

*Built November 2026 · Suresh Kumar Studio Notes*
