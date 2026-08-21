# Security

AccredReady is a multi-tenant SaaS application. Each hospital's data must be isolated from other tenants. Security depends on **Row Level Security (RLS)** in Supabase — the React client does not filter queries by owner.

---

## Threat model

The Supabase anon key is embedded in the shipped JavaScript bundle. This is standard for client-side Supabase apps. The key being public is safe **only if RLS is enforced on every table**.

Without RLS, any logged-in user (or anyone with the anon key) can read or write another hospital's scores, KPIs, audits, and other data.

The React client fetches hospital data with no owner filter — for example, `hospitals.select('*').limit(1).single()`. Isolation depends entirely on database policies.

---

## Security runbook

Step-by-step SQL instructions: [scripts/SECURITY_RUNBOOK.md](../scripts/SECURITY_RUNBOOK.md)

Run these in the **Supabase SQL Editor** (Dashboard → SQL Editor → New query). Order matters.

### Step 1: Diagnose

Run `scripts/audit_rls_status.sql`:

- Section (1): any row with `rls_enabled = false` is currently wide open
- Section (2): note pre-existing policies to avoid conflicts
- Section (3): confirm `profiles` has `id` and `hospital_id` columns

### Step 2: Enable RLS

Run `scripts/enable_rls_and_policies.sql`:

- Enables RLS on all 27 tables
- Adds owner-scoped policies
- Idempotent (drop-if-exists then create) — safe to re-run

**Smoke-test with two accounts** after applying: each must see only its own hospital, scores, KPIs, and audits.

Re-run `audit_rls_status.sql` — every table should show `rls_enabled = true` with `policy_count >= 1`.

### Step 3: Trial enforcement

Run `scripts/trial_enforcement.sql` (after step 2):

- Adds `hospitals.trial_ends_at`
- Backfills existing rows
- Gates data tables behind `has_active_access()` so expired accounts cannot bypass the UI wall via the API
- `hospitals` and `profiles` remain readable so the app can render the "trial ended" wall

---

## Day-to-day operations

| Action | SQL |
|--------|-----|
| Mark customer as paid | `update public.hospitals set plan = 'paid' where id = '<id>';` |
| Extend a trial | `update public.hospitals set trial_ends_at = '<date>' where id = '<id>';` |

Any plan value other than `trial` unlocks access (via `has_active_access()`).

---

## Type caveat

The SQL assumes `hospitals.id` is `uuid`. If the schema uses `bigint`/`int`, change the `has_active_access(target_hospital uuid)` argument type in `trial_enforcement.sql` before running.

---

## Edge function security

| Function | Security notes |
|----------|----------------|
| `ai-assistant` | CORS locked to `accredready.in`; uses service role for KB/OE retrieval |
| `generate-hospital-policy` | Requires authenticated user; fetches only approved masters |
| `generate-policy-document` | Requires Anthropic API key as edge function secret |
| `backfill-embeddings` | Admin utility — uses service role; not exposed to client |

Secrets (Anthropic API key, Supabase service role key) are configured in the Supabase dashboard. Never commit them to the repository.

---

## Client-side considerations

| Item | Detail |
|------|--------|
| Anon key in source | Expected — RLS must compensate |
| No `.env` file | Keys hardcoded in `src/supabaseClient.js` |
| Post-deploy git sync | Never `git add .` — avoids staging `.claude/settings.local.json` and other secrets |
| Account deletion | `public/delete-account.html` documents the deletion process |

---

## Rollback

If RLS causes issues during testing, RLS can be disabled per table temporarily:

```sql
alter table public.<table_name> disable row level security;
```

This re-opens the tenant gap. Use only as a temporary measure during debugging, then re-enable immediately.

---

## Verification checklist

Before considering production secure:

- [ ] `audit_rls_status.sql` shows RLS enabled on all 27 tables
- [ ] Two test accounts cannot see each other's data
- [ ] Expired trial account cannot read scores/KPIs via direct API call
- [ ] Edge function secrets configured in Supabase dashboard
- [ ] `ai-assistant` CORS rejects requests from non-`accredready.in` origins

---

## Related migrations

| Migration | Security relevance |
|-----------|-------------------|
| `20260620_hospitals_created_by.sql` | Hospital ownership tracking |
| `20260620_add_profile_trigger.sql` | Auto-create profile on signup |
| `20260620_access_until.sql` | Access control column |
| `20260702_add_ownership_guards.sql` | Ownership guard functions |
| `20260702_snapshot_security_definer_functions.sql` | Security definer functions |

RLS policies themselves are in `scripts/enable_rls_and_policies.sql` (not in migrations).
