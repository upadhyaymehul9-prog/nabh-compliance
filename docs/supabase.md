# Supabase

AccredReady uses Supabase for authentication, Postgres database, Row Level Security, and Deno edge functions.

**Project URL:** `https://tbptllgcjtiiqspxqcde.supabase.co`

The Supabase anon key is embedded in `src/supabaseClient.js` and `src/components/AIAssistantWidget.jsx`. This is normal for client-side apps — tenant isolation must be enforced by RLS on the database side.

---

## Schema overview

Tables are spread across three locations:

1. **`supabase/migrations/`** — incremental migrations (preferred for new changes)
2. **`scripts/`** — seed files, one-off SQL, KB builders
3. **Root-level SQL** — large seed files (`shco_full_oes.sql`, `shco_full_capa.sql`)

There is no single ERD. Use migrations plus the table groups below as a reference.

### Identity and tenancy

| Table | Purpose |
|-------|---------|
| `profiles` | Maps Supabase Auth user → hospital; stores theme preference |
| `hospitals` | Tenant record: name, plan, `access_until`, `trial_ends_at`, walkthrough flag |

### HCO Full (6th Edition)

| Table | Purpose |
|-------|---------|
| `objective_elements`, `standards`, `achieve_tips` | NABH 6th Edition reference data |
| `assessments`, `scores`, `capa` | OE scoring and corrective actions |
| `kpis`, `kpi_data`, `kpi_custom_targets` | KPI definitions and data entry |
| `committees`, `committee_meetings`, `calendar_plan` | Committee tracking |
| `audit_checklists`, `audit_records`, `custom_audits` | Audit management |
| `mock_drills`, `mock_drill_records` | Mock drill tracker |
| `department_checklists`, `checklist_links` | Department checklists |
| `statutory_licenses` | License tracker |
| `patient_tracers` | Tracer studies |
| `hco_checklist_reviews` | Quick Checklist review ticks |

### SHCO Full (3rd Edition)

| Table | Purpose |
|-------|---------|
| `shco_full_oes` | 408 OEs; columns include `doc_required` (asterisk flag), `interpretation`, `embedding`, FTS `search_vector` |
| `shco_full_scores`, `shco_full_capa` | Scoring and CAPA |
| `shco_kb` | Curated knowledge base from official SHCO book |
| `shco_policy_masters` | Human-reviewed master policies per standard |
| `shco_full_checklist_reviews` | Quick Checklist review ticks |

### ECO Full

| Table | Purpose |
|-------|---------|
| `eco_full_oes`, `eco_full_scores`, `eco_full_capa` | OE data, scoring, CAPA |
| `eco_full_checklist_reviews` | Quick Checklist review ticks |

### ELC programmes

| Table | Purpose |
|-------|---------|
| `hco_elc_progress`, `shco_elc_progress`, `dental_elc_progress` | Document/license progress |
| `elc_scores` | ELC OE scoring (where applicable) |
| `hco_elc_checklist_reviews`, `shco_elc_checklist_reviews` | Checklist review ticks |

### Other

| Table | Purpose |
|-------|---------|
| `programme_interest` | Lead capture from "coming soon" programme notifications |

---

## Search RPCs

| Function | Purpose |
|----------|---------|
| `search_shco_kb(q, match_count)` | Full-text search on SHCO knowledge base |
| `search_shco_full_oes(q, match_count)` | Full-text search on SHCO Full OEs |

These power the Gennie AI assistant retrieval pipeline alongside vector similarity on embeddings.

---

## Edge functions

Located in `supabase/functions/`. Deploy separately from the GitHub Pages frontend (Supabase CLI or dashboard).

| Function | Status | Purpose |
|----------|--------|---------|
| `ai-assistant` | Active | RAG Q&A: FTS + embeddings + SHCO glossary. CORS locked to `accredready.in` |
| `generate-hospital-policy` | Active | Phase B: fetch approved master → `{{HOSPITAL_NAME}}` substitution → DOCX (no AI) |
| `generate-policy-document` | Active | Per-OE AI policy DOCX for asterisked (`doc_required=true`) OEs |
| `backfill-embeddings` | Utility | Batch job: `gte-small` embeddings for OEs and KB rows |
| `draft-master-policy` | Deprecated | Was Phase A AI drafting; replaced by in-session Claude Code workflow |
| `_shared/policy-doc-template.ts` | Shared module | Fixed NABH-format DOCX builder |

### Environment secrets (edge functions)

Edge functions require secrets configured in the Supabase dashboard:

- **Anthropic API key** — for `ai-assistant` and `generate-policy-document`
- **Supabase service role key** — for functions that bypass RLS (e.g. `backfill-embeddings`)

Do not commit secrets to the repository.

---

## Migrations

Current migrations in `supabase/migrations/` (run in filename order):

| Migration | Purpose |
|-----------|---------|
| `20260620_access_until.sql` | Hospital access control column |
| `20260620_add_profile_trigger.sql` | Auto-create profile on signup |
| `20260620_hospitals_created_by.sql` | Hospital ownership |
| `20260702_add_ownership_guards.sql` | Ownership guard functions |
| `20260702_snapshot_security_definer_functions.sql` | Security definer functions |
| `20260706_shco_kb_schema.sql` | SHCO knowledge base schema |
| `20260706_shco_elc_committee_map.sql` | SHCO ELC committee mapping |
| `20260708_kpi_total_exclude_elc.sql` | KPI calculation fix |
| `20260711_dental_elc_progress.sql` | Dental ELC progress table |
| `20260721_committee_programme_map_chapter_ref.sql` | Committee programme mapping |
| `20260803_shco_policy_masters_oe_mapping.sql` | Policy masters OE mapping |
| `20260805_quick_checklist_reviews.sql` | Quick Checklist review tables |

Large seed files (408 SHCO OEs, CAPA tables, KB content) remain in `scripts/` and root-level SQL — run these manually in the Supabase SQL Editor when setting up a new environment.

---

## SHCO knowledge base

The SHCO KB is built from the official NABH SHCO 3rd Edition PDF:

| Script | Purpose |
|--------|---------|
| `scripts/extract_shco_book.py` | Extract text from PDF |
| `scripts/build_annexure_kb.py` | Build annexure knowledge |
| `scripts/generate_shco_kb_sql.py` | Generate SQL seed |
| `scripts/shco_book_knowledge.json` | Extracted book content |
| `scripts/shco_kb_seed.sql` | KB seed SQL |

Achieve tips per chapter: `scripts/tips_*.sql` and `scripts/tips_upload_*.sql`.

---

## Local development notes

There is no `.env.example` in the repo. The Supabase URL and anon key are hardcoded in source. For a new developer:

1. Clone the repo and run `npm install && npm start`
2. The app connects to the production Supabase project by default
3. For an isolated environment, create a new Supabase project, run migrations + seeds, and update `src/supabaseClient.js`

Edge function changes require deployment via Supabase CLI:

```bash
supabase functions deploy ai-assistant
supabase functions deploy generate-hospital-policy
```

See [security.md](security.md) for RLS setup before using any shared Supabase project.
