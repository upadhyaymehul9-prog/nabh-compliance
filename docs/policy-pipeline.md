# Policy Pipeline

AccredReady generates NABH-format SOP documents for **SHCO Full Accreditation** standards. The system has two phases:

1. **Phase A (authoring)** — Human-reviewed master policies stored in `shco_policy_masters`
2. **Phase B (personalisation)** — Hospital-specific DOCX via `generate-hospital-policy` edge function

A third path generates per-OE AI policies for asterisked objective elements via `generate-policy-document`.

---

## Phase A: Master policy authoring

Master policies are drafted outside the app, reviewed by a human, and inserted into Supabase. They use `{{HOSPITAL_NAME}}` as a placeholder for Phase B substitution.

### Current progress

The **Hospital Infection Control (HIC)** chapter is complete:

| Standard | Status |
|----------|--------|
| HIC.1 | Drafted and approved |
| HIC.2 | Drafted (reconstructed 2026-08-06) |
| HIC.3 | Drafted and approved |
| HIC.4 | Drafted and approved |
| HIC.5 | Drafted and approved |
| HIC.6 | Drafted and approved |

Remaining ~65 SHCO Full standards are pending under the two-tier depth rule (see below).

### Standing rules

Before drafting any master policy, read [scripts/master-policy-todos.md](../scripts/master-policy-todos.md). Key rules:

**Two-tier depth (from HIC.7 onward):**

| Tier | Applies to | Treatment |
|------|------------|-----------|
| Tier 1 | Asterisked OEs (`doc_required = true`) | Full HIC.6-grade depth: reasoning, evidence detail, cross-checks, fact-checking, hash verification |
| Tier 2 | Non-asterisked OEs | Accurate but lighter: requirement and method stated clearly, no extended rationale |

HIC.1–HIC.6 remain at uniform maximum depth (not retroactively changed).

**Structural requirements (all standards):**

- Full control box (Doc No., Issue No., Rev. No., etc.)
- OE cross-reference table
- Abbreviations with back-pointer
- Eight numbered sections
- Hash-checked disclaimer
- `status = 'draft'` until human approval
- Five optional sections left unset (definitions, training, resources, monitoring, exceptions)
- `policy_placeholder_audit.py` run on every build

### Directory structure

```
policies/
├── build/
│   ├── build_hic1.py … build_hic6.py   # Generate draft JSON + SQL INSERT
│   ├── build_hic2_draft.py
│   ├── policy_placeholder_audit.py     # Count [Hospital to define] placeholders
│   └── render_previews.ts              # Preview DOCX from DB rows
├── drafts/
│   └── hic1_draft.json … hic6_draft.json
└── sql/
    └── hic1_insert.sql … hic6_insert.sql   # Run in Supabase SQL Editor
```

Build scripts resolve output paths relative to the script file (`policies/build/`), so they produce the same result regardless of working directory.

### Authoring workflow

```
1. Read standing rules in master-policy-todos.md
2. Verify doc_required flags against official SHCO 3rd Edition PDF
3. Draft content (Claude Code session: web search, cross-check prior standards)
4. Run policies/build/build_hicN.py → produces JSON draft + SQL INSERT
5. Run policy_placeholder_audit.py → verify placeholder count
6. Human review of draft JSON
7. Run SQL in Supabase SQL Editor → inserts row with status='draft'
8. Final review → set status='approved'
```

### Build script output

Each `build_hicN.py` script produces:

- **`policies/drafts/hicN_draft.json`** — full policy content for review
- **`policies/sql/hicN_insert.sql`** — INSERT statement for `shco_policy_masters`

The JSON includes: purpose, scope, procedure steps (per OE), evidence requirements, OE mapping, universal facts checklist, and document control metadata.

### Deprecated tooling

| File | Status |
|------|--------|
| `scripts/draft-master-policy.js` | Deprecated — compute limits, missing columns |
| `supabase/functions/draft-master-policy` | Deprecated — replaced by in-session Claude Code workflow |

---

## Phase B: Hospital personalisation

Once a master policy is approved (`status='approved'`), hospitals download a personalised DOCX via the `generate-hospital-policy` edge function.

**No AI is involved in Phase B.** The function:

1. Fetches the approved master from `shco_policy_masters`
2. Replaces `{{HOSPITAL_NAME}}` with the hospital's name
3. Renders a NABH-format DOCX using `_shared/policy-doc-template.ts`

---

## Per-OE AI generation

`generate-policy-document` generates individual policy documents for asterisked OEs (`doc_required = true`) using the Anthropic API. This is a separate path from the master policy pipeline and is used when a hospital needs a single-OE document rather than a full standard SOP.

---

## Open infrastructure items

Tracked in [scripts/master-policy-todos.md](../scripts/master-policy-todos.md):

- **Document version and revision history** — no working data path yet; version integer bump is a no-op in rendered documents
- **Cross-standard reconciliation** — HIC.2/HIC.3/HIC.5 overlap items flagged for a dedicated pass
- **Required Records checklist** — rendering added 2026-08-06; verify across all approved standards
- **Document control block** — Doc No., Issue No., Rev. No. schema vs renderer decisions pending

---

## Preview rendering

To preview a policy as DOCX from a database row:

```bash
# Requires Deno and Supabase credentials
deno run policies/build/render_previews.ts
```

See script header for required environment variables.

---

## Placeholder audit

Count unresolved `[Hospital to define]` placeholders before approving a draft:

```bash
python policies/build/policy_placeholder_audit.py policies/drafts/hicN_draft.json
```

A non-zero count means the policy still has hospital-specific gaps that Phase B cannot fill automatically.
