# Security Runbook — RLS & Trial Enforcement

Addresses audit HIGH items #5 (multi-tenant isolation) and #6 (server-side trial
enforcement). These require database access I don't have, so run them yourself in
the **Supabase SQL Editor** (Dashboard → SQL Editor → New query). Order matters.

## Why this is needed
The React client fetches hospital data with **no owner filter** — e.g.
`hospitals.select('*').limit(1).single()` (App.js ~2456). Isolation depends
entirely on Row Level Security. If RLS is off or incomplete, any logged-in user
(or anyone with the public anon key, which is in the shipped bundle) can read or
write another hospital's data. The anon key being public is normal **only if RLS
is enforced.**

## Steps

1. **Diagnose (read-only).** Run `audit_rls_status.sql`.
   - Section (1): any row with `rls_enabled = false` is currently wide open.
   - Section (2): note any pre-existing policies so step 2 doesn't conflict.
   - Section (3): confirm `profiles` has `id` and `hospital_id` columns (the
     ownership anchor). If your column names differ, adjust the SQL in step 2.

2. **Close the tenant gap.** Run `enable_rls_and_policies.sql`.
   - Enables RLS on all 27 tables and adds owner-scoped policies.
   - Idempotent (drop-if-exists then create) — safe to re-run.
   - **Then smoke-test with TWO accounts**: each must see only its own hospital,
     scores, KPIs, audits. Create a throwaway second account if needed.
   - Re-run `audit_rls_status.sql` — every table should now show
     `rls_enabled = true` with `policy_count >= 1`.

3. **Enforce trial/plan server-side.** Run `trial_enforcement.sql` (after step 2).
   - Adds `hospitals.trial_ends_at`, backfills existing rows to **2026-06-20**
     (matches the app's hard-coded trial clamp), and gates the data tables behind
     `has_active_access()` so an expired/unpaid account can't bypass the UI wall
     via the API.
   - `hospitals` and `profiles` remain readable by members so the app can still
     read `plan` to render the "trial ended" wall.

## Type caveat
The SQL assumes `hospitals.id` is `uuid`. If it's `bigint`/`int` in your schema,
change the `has_active_access(target_hospital uuid)` argument type in
`trial_enforcement.sql` before running. Everything else uses inline subqueries and
is type-agnostic.

## Day-to-day operations
- **Mark a customer as paid:** `update public.hospitals set plan = 'paid' where id = '<id>';`
  (any value other than `trial` unlocks access)
- **Extend a trial:** `update public.hospitals set trial_ends_at = '<date>' where id = '<id>';`

## Rollback
RLS can be disabled per table if something breaks during testing:
`alter table public.<t> disable row level security;`
Do this only as a temporary measure — disabled RLS re-opens the tenant gap.
