-- Migration: server-side trial / plan enforcement (audit HIGH #6).
-- Today the trial wall is client-side only (App.js computes trialExpired in the
-- browser); the Supabase queries still succeed, so a user can bypass it via the
-- API and keep reading/writing data after expiry. This makes the database itself
-- refuse access to compliance DATA tables once a hospital's trial has lapsed and
-- it has no paid plan.
--
-- PREREQUISITE: run scripts/enable_rls_and_policies.sql FIRST. This file REPLACES
-- the data-table policies created there with access-gated versions.
--
-- Design note: hospitals + profiles stay readable by members regardless of trial
-- state, so the app can still read hospitals.plan to render the "trial ended" wall.
-- Only the value-bearing data tables are gated.

------------------------------------------------------------------------
-- 1) trial_ends_at column on hospitals.
-- Default = created_at + 14 days. Existing rows are backfilled to 2026-06-20 to
-- match the app's OFFICIAL_TRIAL_START clamp (2026-06-06 + 14 days, App.js:5536).
------------------------------------------------------------------------
alter table public.hospitals
  add column if not exists trial_ends_at timestamptz;

update public.hospitals
  set trial_ends_at = timestamptz '2026-06-20 00:00:00+00'
  where trial_ends_at is null;

alter table public.hospitals
  alter column trial_ends_at set default (now() + interval '14 days');

------------------------------------------------------------------------
-- 2) Access predicate: paid plan OR trial still running.
-- plan IS NULL or 'trial' counts as trial (matches App.js:5541).
------------------------------------------------------------------------
create or replace function public.has_active_access(target_hospital uuid)
returns boolean
language sql
security definer
stable
set search_path = public
as $$
  select exists (
    select 1
    from public.hospitals h
    where h.id = target_hospital
      and (
        (h.plan is not null and h.plan <> 'trial')                          -- paid
        or coalesce(h.trial_ends_at, h.created_at + interval '14 days') > now()  -- trial live
      )
  );
$$;
-- NOTE: target_hospital is typed uuid. If hospitals.id is bigint/int in your
-- schema, change the argument type to bigint here before running.

------------------------------------------------------------------------
-- 3) Re-create hospital-scoped data policies WITH the access gate.
------------------------------------------------------------------------
do $$
declare t text;
begin
  foreach t in array array[
    'assessments','elc_scores','kpi_data','kpi_custom_targets','audit_records',
    'custom_audits','committee_meetings','mock_drill_records','statutory_licenses',
    'calendar_plan','patient_tracers'
  ] loop
    execute format('drop policy if exists "%s_member_all" on public.%I;', t, t);
    execute format($f$
      create policy "%1$s_member_all" on public.%1$I
        for all to authenticated
        using (
          hospital_id in (select hospital_id from public.profiles where id = auth.uid())
          and public.has_active_access(hospital_id))
        with check (
          hospital_id in (select hospital_id from public.profiles where id = auth.uid())
          and public.has_active_access(hospital_id));
    $f$, t);
  end loop;
end $$;

------------------------------------------------------------------------
-- 4) Re-create assessment-scoped data policies WITH the access gate.
------------------------------------------------------------------------
do $$
declare t text;
begin
  foreach t in array array[
    'scores','capa','hco_elc_progress','shco_elc_progress','dental_elc_progress'
  ] loop
    execute format('drop policy if exists "%s_member_all" on public.%I;', t, t);
    execute format($f$
      create policy "%1$s_member_all" on public.%1$I
        for all to authenticated
        using (assessment_id in (
          select a.id from public.assessments a
          where a.hospital_id in (select hospital_id from public.profiles where id = auth.uid())
            and public.has_active_access(a.hospital_id)))
        with check (assessment_id in (
          select a.id from public.assessments a
          where a.hospital_id in (select hospital_id from public.profiles where id = auth.uid())
            and public.has_active_access(a.hospital_id)));
    $f$, t);
  end loop;
end $$;

-- To grant a paying customer access: update public.hospitals set plan = 'paid'
-- (any value other than 'trial') where id = '<hospital-id>';
-- To extend a trial: update public.hospitals set trial_ends_at = '<date>' where id = '<hospital-id>';
