# AccredReady

**NABH accreditation compliance software for Indian hospitals and healthcare organisations.**

Live site: [https://accredready.in](https://accredready.in)

AccredReady helps hospitals track objective elements (OEs), KPIs, committees, audits, and evidence against NABH standards across multiple programmes — from large hospitals (HCO Full, 6th Edition) to small hospitals (SHCO Full, 3rd Edition), entry-level certification, eye care (ECO), and dental clinics.

> AccredReady is an independent educational tool. It is not affiliated with NABH or QCI.

---

## Programmes supported

| Programme | App key | Description |
|-----------|---------|-------------|
| HCO Full Accreditation | `hco` | Hospitals with 51+ beds — NABH 6th Edition OE scoring and gap analysis |
| HCO Entry Level Certification (ELC) | `hco-elc` | Document and license checklist for large hospitals |
| SHCO Full Accreditation | `shco-full` | Small hospitals (≤50 beds) — SHCO 3rd Edition OE scoring |
| SHCO Entry Level Certification (ELC) | `shco-elc` | Document and license checklist for small hospitals |
| ECO Full Accreditation | `eco-full` | Eye Care Organisations — full OE scoring |
| Dental Entry Level Certification | `dental-elc` | Dental clinics (1–8 chairs) — checklist-based |

Additional surfaces: **Gennie AI assistant** (NABH Q&A), **master policy generation** (SHCO Full), and **public SEO content** (learn hub, blog, landing pages).

---

## Tech stack

| Layer | Technology |
|-------|------------|
| Frontend | React 19 (Create React App) |
| Backend | Supabase — Postgres, Auth, Row Level Security |
| Edge functions | Deno TypeScript on Supabase |
| Charts / PDF | Recharts, jsPDF |
| Deployment | GitHub Pages → `accredready.in` |

---

## Quick start

```bash
git pull origin master
npm install
npm start          # http://localhost:3000
```

Build and deploy (local verification required first — see [docs/deployment.md](docs/deployment.md)):

```bash
npm run build
npm run deploy     # gh-pages → accredready.in
```

---

## Repository layout

```
src/                  React app (App.js is the main shell)
public/               Static SEO pages, sitemap, CRA index.html
supabase/
  functions/          Edge functions (AI assistant, policy generation)
  migrations/         Incremental SQL migrations
scripts/              SQL seeds, KB builders, security runbook
policies/             SHCO master policy drafting pipeline (HIC chapter)
marketing/            Marketing collateral and reports
docs/                 Project documentation (this repo)
CLAUDE.md             Agent workflow rules (local-first, NABH accuracy)
```

---

## Documentation

| Doc | Contents |
|-----|----------|
| [docs/README.md](docs/README.md) | Documentation index |
| [docs/architecture.md](docs/architecture.md) | App structure, auth flow, programme routing |
| [docs/supabase.md](docs/supabase.md) | Schema, migrations, edge functions |
| [docs/deployment.md](docs/deployment.md) | Local → build → deploy workflow |
| [docs/policy-pipeline.md](docs/policy-pipeline.md) | Master policy authoring for SHCO Full |
| [docs/seo-content.md](docs/seo-content.md) | Public pages and NABH accuracy rules |
| [docs/security.md](docs/security.md) | RLS, trial enforcement, security runbook |

Other reference files:

- [CLAUDE.md](CLAUDE.md) — session rules for AI agents working in this repo
- [scripts/master-policy-todos.md](scripts/master-policy-todos.md) — policy drafting TODOs and standing rules
- [scripts/SECURITY_RUNBOOK.md](scripts/SECURITY_RUNBOOK.md) — RLS and trial enforcement SQL steps

---

## npm scripts

| Script | Action |
|--------|--------|
| `npm start` | Development server on port 3000 |
| `npm run build` | Production build to `build/` |
| `npm run deploy` | Build + publish to GitHub Pages |
| `npm test` | Jest test runner (CRA default) |

---

## Contributing / agent rules

Before making changes, read [CLAUDE.md](CLAUDE.md). Key rules:

1. **Local-first** — test with `npm start` before deploying.
2. **Never deploy untested code.**
3. **Post-deploy auto-sync** — after `npm run deploy`, commit only `src/`, `public/`, `supabase/functions/`, and `scripts/` (never `git add .`).
4. **NABH accuracy** — do not publish specific OE or standard counts on public SEO pages; only the app may reference OE numbers from Supabase.
