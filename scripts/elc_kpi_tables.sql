-- hco_elc_kpi_data and shco_elc_kpi_data tables for ELC KPI tracking.
-- Mirrors eco_kpi_data / shco_kpi_data exactly (structure + RLS pattern),
-- with the SSI three-stage surveillance column built in from creation.
--
-- Project rule: every programme gets its OWN separate tables — no shared
-- data tables across programmes. These are ELC-only and never mix with Full.
--
-- ELC KPI definitions live in public.kpis, kpi_no 51-64, filtered by
-- programme_scope @> ARRAY['HCO_ELC'] (or 'SHCO_ELC'). SSI = kpi_no 52.
--
-- HOW TO RUN:
--   Paste this entire file into the Supabase SQL Editor and click Run.
--   Idempotent — safe to re-run.

------------------------------------------------------------------------
-- surveillance_stage: 'final' is the default used by all 13 non-SSI ELC
-- KPIs. SSI (kpi_no 52) uses 'preliminary' -> 'day_30' -> 'day_90_final',
-- each stage stored as its own row for the same hospital/kpi/month/year.
------------------------------------------------------------------------

------------------------------------------------------------------------
-- TABLE 1: hco_elc_kpi_data  (HCO Entry Level Certification KPI entries)
------------------------------------------------------------------------
create table if not exists public.hco_elc_kpi_data (
  id                 uuid        default gen_random_uuid() primary key,
  hospital_id        uuid        not null references public.hospitals(id) on delete cascade,
  kpi_id             integer     not null,
  month              integer     not null check (month between 1 and 12),
  year               integer     not null check (year >= 2020),
  numerator          numeric     not null,
  denominator        numeric     not null,
  value              numeric     not null,
  surveillance_stage text        not null default 'final'
                       check (surveillance_stage in ('final','preliminary','day_30','day_90_final')),
  created_at         timestamptz default now(),
  updated_at         timestamptz default now(),
  unique (hospital_id, kpi_id, month, year, surveillance_stage)
);

alter table public.hco_elc_kpi_data enable row level security;

drop policy if exists "hco_elc_kpi_data_member_all" on public.hco_elc_kpi_data;
create policy "hco_elc_kpi_data_member_all" on public.hco_elc_kpi_data
  for all to authenticated
  using  (hospital_id in (select hospital_id from public.profiles where id = auth.uid()))
  with check (hospital_id in (select hospital_id from public.profiles where id = auth.uid()));

------------------------------------------------------------------------
-- TABLE 2: shco_elc_kpi_data  (SHCO Entry Level Certification KPI entries)
------------------------------------------------------------------------
create table if not exists public.shco_elc_kpi_data (
  id                 uuid        default gen_random_uuid() primary key,
  hospital_id        uuid        not null references public.hospitals(id) on delete cascade,
  kpi_id             integer     not null,
  month              integer     not null check (month between 1 and 12),
  year               integer     not null check (year >= 2020),
  numerator          numeric     not null,
  denominator        numeric     not null,
  value              numeric     not null,
  surveillance_stage text        not null default 'final'
                       check (surveillance_stage in ('final','preliminary','day_30','day_90_final')),
  created_at         timestamptz default now(),
  updated_at         timestamptz default now(),
  unique (hospital_id, kpi_id, month, year, surveillance_stage)
);

alter table public.shco_elc_kpi_data enable row level security;

drop policy if exists "shco_elc_kpi_data_member_all" on public.shco_elc_kpi_data;
create policy "shco_elc_kpi_data_member_all" on public.shco_elc_kpi_data
  for all to authenticated
  using  (hospital_id in (select hospital_id from public.profiles where id = auth.uid()))
  with check (hospital_id in (select hospital_id from public.profiles where id = auth.uid()));

-- Done. Verify with:
--   select tablename, rowsecurity from pg_tables
--   where tablename in ('hco_elc_kpi_data','shco_elc_kpi_data');
--   select conname, pg_get_constraintdef(oid) from pg_constraint
--   where conrelid = 'public.hco_elc_kpi_data'::regclass;
