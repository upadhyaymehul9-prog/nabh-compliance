# AccredReady Documentation

Project documentation for the [AccredReady](https://accredready.in) codebase (`nabh-compliance`).

---

## Guides

| Document | When to read it |
|----------|-----------------|
| [architecture.md](architecture.md) | Understanding the React app, auth flow, programmes, and navigation |
| [supabase.md](supabase.md) | Database schema, migrations, edge functions, and search |
| [deployment.md](deployment.md) | Local development, build, GitHub Pages deploy, post-deploy sync |
| [policy-pipeline.md](policy-pipeline.md) | SHCO Full master policy drafting and hospital DOCX generation |
| [seo-content.md](seo-content.md) | Public HTML pages, learn hub, blog, and content accuracy rules |
| [security.md](security.md) | Row Level Security, trial enforcement, and operational security |

---

## External reference

| File | Purpose |
|------|---------|
| [../CLAUDE.md](../CLAUDE.md) | Agent workflow rules (local-first deploy, NABH accuracy) |
| [../scripts/master-policy-todos.md](../scripts/master-policy-todos.md) | Policy drafting standing rules, deferred topics, open reconciliation items |
| [../scripts/SECURITY_RUNBOOK.md](../scripts/SECURITY_RUNBOOK.md) | Step-by-step RLS and trial enforcement SQL |

---

## Product summary

AccredReady is a web-based compliance tool for Indian healthcare organisations preparing for **NABH (National Accreditation Board for Hospitals & Healthcare Providers)** accreditation. It supports:

- **OE scoring and gap analysis** (HCO Full, SHCO Full, ECO Full)
- **Checklist-based ELC tracking** (HCO, SHCO, Dental)
- **KPIs, committees, audits, mock drills, tracers, licenses** (HCO Full)
- **Gennie AI assistant** — grounded NABH Q&A from official SHCO book content
- **Policy document generation** — approved master SOPs personalised per hospital

The React frontend talks directly to Supabase (Postgres + Auth + Edge Functions). The static marketing site and app shell deploy to GitHub Pages at `accredready.in`.
