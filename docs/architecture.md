# Architecture

## Overview

AccredReady is a Create React App (CRA) single-page application backed by Supabase. Almost all product logic lives in one file — `src/App.js` (~13,500 lines). A small set of UI modules is extracted to `src/components/`.

```
Browser (accredready.in)
    │
    ├── React SPA (src/App.js)
    │       ├── Supabase Auth (email, Google OAuth)
    │       ├── Supabase Postgres (RLS-scoped queries)
    │       └── Edge Functions (AI, policy DOCX)
    │
    └── Static HTML (public/*.html, learn/, blog/)
            └── Served alongside CRA build via GitHub Pages
```

---

## Entry points

| File | Role |
|------|------|
| `src/index.js` | CRA bootstrap — renders `<App />` |
| `src/App.js` | Main application shell and all programme UIs |
| `src/supabaseClient.js` | Supabase client initialisation |
| `public/index.html` | CRA shell + SEO meta, JSON-LD, embedded resources |

---

## Auth and onboarding flow

The app uses a state machine driven by `appState`:

```
loading → homepage → login/signup → setup → programme → app
                              ↘ recovery (password reset)
```

| State | Component | Purpose |
|-------|-----------|---------|
| `homepage` | `HomepageScreen` | Marketing landing with embedded auth |
| `login` | `AuthForm` | Full-page login/signup |
| `setup` | `SetupScreen` | Create or link a hospital record |
| `programme` | `ProgrammeSelector` | Choose NABH programme |
| `app` | Main shell | Programme-specific navigation and screens |
| `recovery` | `RecoveryScreen` | Password reset flow |

Auth is handled by Supabase Auth. Each user links to a hospital via the `profiles` table (`id` → user, `hospital_id` → tenant).

---

## Programmes

Programme keys used in app state (`selectedProgramme`):

| Key | Programme | Primary UI |
|-----|-----------|------------|
| `hco` | HCO Full Accreditation (6th Edition) | Full nav drawer — scoring, dashboard, gaps, KPIs, audits, etc. |
| `hco-elc` | HCO Entry Level Certification | Document/license checklist |
| `shco-full` | SHCO Full Accreditation (3rd Edition) | Tab bar — dashboard, scoring, KPIs, committees, checklist, gaps |
| `shco-elc` | SHCO Entry Level Certification | Document/license checklist |
| `eco-full` | ECO Full Accreditation | Tab bar — same pattern as SHCO Full |
| `dental-elc` | Dental Entry Level Certification | Checklist-based tracker |

The programme selector also links to **Revenue Leakage Self-Audit** (`/revenue-leakage-review/`) as a standalone free tool with no login.

---

## Navigation (HCO Full)

HCO Full uses a drawer grouped into four sections. Navigation items are defined in `ALL_NAV` and filtered by programme:

| Group | Screens |
|-------|---------|
| **ASSESS** | Dashboard, Fix Gaps, Quick Checklist, Tracer |
| **GOVERNANCE** | Committees, Audits, Drills, KPIs |
| **EVIDENCE** | Checklists, Docs (external Google Drive link), Licenses |
| **PLAN** | Committee Calendar |

Primary action (header button): **Score OEs**.

SHCO Full and ECO Full use an internal tab bar instead of the drawer. ELC programmes use a single primary checklist screen.

---

## Extracted components

| File | Role |
|------|------|
| `src/components/HomepageScreen.js` | Public marketing homepage |
| `src/components/AuthForm.js` | Login, signup, password reset |
| `src/components/AIAssistantWidget.jsx` | "Gennie" chat widget → `ai-assistant` edge function |
| `src/components/GennieMascot.jsx` | Mascot UI for the AI widget |
| `src/components/QuickChecklist.jsx` | Read-only OE/KPI/committee checklist with review ticks |

---

## Key features by programme

### HCO Full (`hco`)

- OE scoring (1–5) against NABH 6th Edition standards
- Dashboard with compliance verdict, chapter heatmap, readiness score
- Gap list and CAPA tracking
- Quick Checklist (OE/KPI/committee roll-up)
- Committee reference and meeting tracking
- NABH audit checklists and custom audits
- Mock drill tracker
- KPI data entry and trend charts
- Patient tracer studies
- Statutory license tracker
- Committee meeting calendar
- Department checklists
- PDF gap report export (jsPDF)
- Onboarding walkthrough tour
- Dark/light theme

### SHCO Full / ECO Full

- OE scoring from `shco_full_oes` / `eco_full_oes`
- Scores in `shco_full_scores` / `eco_full_scores`
- CAPA support
- KPI tab, committees, Quick Checklist

### ELC programmes (HCO, SHCO, Dental)

- Checklist-based document and license tracking
- Progress persisted per hospital/assessment
- Static document lists embedded in `App.js` (e.g. `SHCO_ELC_DOCS`, `HCO_ELC_DOCS`, `DENTAL_ELC_DOCS`)

---

## Shared utilities in App.js

- `pdfSafe()` — jsPDF WinAnsi character sanitisation for PDF export
- `Ring`, `KpiTrendChart`, `AuditComplianceChart` — dashboard chart components
- `UpgradeWall` — trial-expired gate overlay
- Static NABH reference data: OE tips, ELC document lists, chapter colours, KPI definitions

---

## Monolithic structure note

`App.js` contains all programme screens, data-fetching hooks, and static NABH data arrays. There is no component extraction plan documented yet. When working in the codebase:

- Search by screen name or `case 'screenId'` in the main render switch
- Programme-specific logic is gated on `selectedProgramme`
- Supabase queries generally use `context.hospitalId` without explicit owner filters — tenant isolation depends on RLS (see [security.md](security.md))

---

## Static assets and SEO

Marketing and SEO content lives in `public/` as standalone HTML files. These deploy alongside the CRA build. See [seo-content.md](seo-content.md) for the full inventory.

The `marketing/` folder holds strategy documents, LinkedIn automation scripts, and video production assets — not served directly by the app.
