-- Migration: enable Row Level Security + owner-scoped policies on all tables.
-- Closes the multi-tenant gap (audit HIGH #5): the app fetches hospital data
-- with NO owner filter in the client (e.g. hospitals.select('*').limit(1)),
-- so isolation depends 100% on these policies.
--
-- HOW TO RUN:
--   1. Run scripts/audit_rls_status.sql first and read section (2) — if you have
--      pre-existing policies with different names, reconcile before running this.
--   2. Run this whole file in the Supabase SQL Editor.
--   3. Smoke-test the app with TWO different accounts: each must see only its own
--      hospital. Then optionally apply scripts/trial_enforcement.sql (#6).
--
-- OWNERSHIP MODEL (from the app code): profiles.id = auth.uid() maps a user to a
-- hospital via profiles.hospital_id. Everything scopes off that.
--
-- Idempotent: every policy is dropped-if-exists then recreated, so re-running is safe.

------------------------------------------------------------------------
-- SECTION A — reference tables: readable by any logged-in user, never writable
-- from the client. (Seed/maintain these via the service role, not the anon key.)
------------------------------------------------------------------------
do $$
declare t text;
begin
  foreach t in array array[
    'achieve_tips','audit_checklists','checklist_links','committees',
    'department_checklists','kpis','mock_drills','objective_elements','standards'
  ] loop
    execute format('alter table public.%I enable row level security;', t);
    execute format('drop policy if exists "%s_read" on public.%I;', t, t);
    execute format(
      'create policy "%s_read" on public.%I for select to authenticated using (true);',
      t, t);
  end loop;
end $$;

------------------------------------------------------------------------
-- SECTION B — profiles: a user sees and edits only their own row.
------------------------------------------------------------------------
alter table public.profiles enable row level security;
drop policy if exists "profiles_own_select" on public.profiles;
drop policy if exists "profiles_own_upsert" on public.profiles;
drop policy if exists "profiles_own_update" on public.profiles;
create policy "profiles_own_select" on public.profiles
  for select to authenticated using (id = auth.uid());
create policy "profiles_own_upsert" on public.profiles
  for insert to authenticated with check (id = auth.uid());
create policy "profiles_own_update" on public.profiles
  for update to authenticated using (id = auth.uid()) with check (id = auth.uid());

------------------------------------------------------------------------
-- SECTION C — hospitals: a user sees/updates only hospitals they belong to.
-- INSERT is allowed for any authenticated user (the app lets a new user create
-- their first hospital, then writes a matching profiles row).
------------------------------------------------------------------------
alter table public.hospitals enable row level security;
drop policy if exists "hospitals_member_select" on public.hospitals;
drop policy if exists "hospitals_insert"       on public.hospitals;
drop policy if exists "hospitals_member_update" on public.hospitals;
create policy "hospitals_member_select" on public.hospitals
  for select to authenticated
  using (id in (select hospital_id from public.profiles where id = auth.uid()));
create policy "hospitals_insert" on public.hospitals
  for insert to authenticated with check (true);
create policy "hospitals_member_update" on public.hospitals
  for update to authenticated
  using (id in (select hospital_id from public.profiles where id = auth.uid()))
  with check (id in (select hospital_id from public.profiles where id = auth.uid()));

------------------------------------------------------------------------
-- SECTION D — hospital-scoped tables (have a hospital_id column).
-- Full CRUD for members of that hospital.
------------------------------------------------------------------------
do $$
declare t text;
begin
  foreach t in array array[
    'assessments','elc_scores','kpi_data','kpi_custom_targets','audit_records',
    'custom_audits','committee_meetings','mock_drill_records','statutory_licenses',
    'calendar_plan','patient_tracers'
  ] loop
    execute format('alter table public.%I enable row level security;', t);
    execute format('drop policy if exists "%s_member_all" on public.%I;', t, t);
    execute format($f$
      create policy "%1$s_member_all" on public.%1$I
        for all to authenticated
        using (hospital_id in (select hospital_id from public.profiles where id = auth.uid()))
        with check (hospital_id in (select hospital_id from public.profiles where id = auth.uid()));
    $f$, t);
  end loop;
end $$;

------------------------------------------------------------------------
-- SECTION E — assessment-scoped tables (have an assessment_id column).
-- Scoped through assessments -> hospital -> profile membership.
------------------------------------------------------------------------
do $$
declare t text;
begin
  foreach t in array array[
    'scores','capa','hco_elc_progress','shco_elc_progress'
  ] loop
    execute format('alter table public.%I enable row level security;', t);
    execute format('drop policy if exists "%s_member_all" on public.%I;', t, t);
    execute format($f$
      create policy "%1$s_member_all" on public.%1$I
        for all to authenticated
        using (assessment_id in (
          select a.id from public.assessments a
          where a.hospital_id in (select hospital_id from public.profiles where id = auth.uid())))
        with check (assessment_id in (
          select a.id from public.assessments a
          where a.hospital_id in (select hospital_id from public.profiles where id = auth.uid())));
    $f$, t);
  end loop;
end $$;

------------------------------------------------------------------------
-- SECTION F — programme_interest: anonymous lead capture. Anyone may INSERT;
-- nobody reads it from the client (review via the service role / dashboard).
------------------------------------------------------------------------
alter table public.programme_interest enable row level security;
drop policy if exists "programme_interest_insert" on public.programme_interest;
create policy "programme_interest_insert" on public.programme_interest
  for insert to anon, authenticated with check (true);

-- Done. Re-run scripts/audit_rls_status.sql to confirm every table now shows
-- rls_enabled = true with at least one policy.
