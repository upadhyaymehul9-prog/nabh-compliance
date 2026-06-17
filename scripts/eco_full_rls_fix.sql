-- Fix: RLS policies for eco_full_oes and eco_full_scores.
-- These tables were created in Supabase without SELECT/CRUD policies,
-- so every query returned [] silently — causing the "0 OEs" bug.
--
-- HOW TO RUN:
--   Paste into Supabase SQL Editor and click Run.
--   Idempotent — safe to re-run.

------------------------------------------------------------------------
-- eco_full_oes: reference table — any authenticated user can SELECT.
-- Nobody writes to this from the client (seeded via service role).
------------------------------------------------------------------------
alter table public.eco_full_oes enable row level security;

drop policy if exists "eco_full_oes_read" on public.eco_full_oes;
create policy "eco_full_oes_read" on public.eco_full_oes
  for select to authenticated using (true);

------------------------------------------------------------------------
-- eco_full_scores: hospital-scoped — members read/write their own rows.
------------------------------------------------------------------------
alter table public.eco_full_scores enable row level security;

drop policy if exists "eco_full_scores_member_all" on public.eco_full_scores;
create policy "eco_full_scores_member_all" on public.eco_full_scores
  for all to authenticated
  using  (hospital_id in (select hospital_id from public.profiles where id = auth.uid()))
  with check (hospital_id in (select hospital_id from public.profiles where id = auth.uid()));

-- Verify:
-- select tablename, rowsecurity from pg_tables
-- where tablename in ('eco_full_oes','eco_full_scores','eco_full_capa','eco_kpi_data');
