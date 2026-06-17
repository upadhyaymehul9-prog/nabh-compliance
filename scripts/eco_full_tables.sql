-- eco_full_capa and eco_kpi_data tables for ECO Full Accreditation.
-- Mirrors shco_full_capa and shco_kpi_data exactly (structure + RLS pattern).
--
-- HOW TO RUN:
--   Paste this entire file into the Supabase SQL Editor and click Run.
--   Idempotent — safe to re-run.

------------------------------------------------------------------------
-- TABLE 1: eco_full_capa
-- Stores Corrective Action / Preventive Action entries for ECO Full gaps.
-- Scoped by hospital_id + oe_code (unique pair).
------------------------------------------------------------------------
create table if not exists public.eco_full_capa (
  id                 uuid        default gen_random_uuid() primary key,
  hospital_id        uuid        not null references public.hospitals(id) on delete cascade,
  oe_code            text        not null,
  finding            text        not null default '',
  action_planned     text        not null default '',
  responsible_person text                 default '',
  target_date        date,
  status             text                 default 'open',
  created_at         timestamptz          default now(),
  updated_at         timestamptz          default now(),
  unique (hospital_id, oe_code)
);

-- RLS: hospital members can do full CRUD on their own rows only
alter table public.eco_full_capa enable row level security;

drop policy if exists "eco_full_capa_member_all" on public.eco_full_capa;
create policy "eco_full_capa_member_all" on public.eco_full_capa
  for all to authenticated
  using  (hospital_id in (select hospital_id from public.profiles where id = auth.uid()))
  with check (hospital_id in (select hospital_id from public.profiles where id = auth.uid()));

------------------------------------------------------------------------
-- TABLE 2: eco_kpi_data
-- Stores monthly KPI numerator/denominator/value entries for ECO Full.
-- Mirrors shco_kpi_data: unique on (hospital_id, kpi_id, month, year).
------------------------------------------------------------------------
create table if not exists public.eco_kpi_data (
  id          uuid        default gen_random_uuid() primary key,
  hospital_id uuid        not null references public.hospitals(id) on delete cascade,
  kpi_id      integer     not null,
  month       integer     not null check (month between 1 and 12),
  year        integer     not null check (year >= 2020),
  numerator   numeric     not null,
  denominator numeric     not null,
  value       numeric     not null,
  created_at  timestamptz default now(),
  updated_at  timestamptz default now(),
  unique (hospital_id, kpi_id, month, year)
);

-- RLS: hospital members can do full CRUD on their own rows only
alter table public.eco_kpi_data enable row level security;

drop policy if exists "eco_kpi_data_member_all" on public.eco_kpi_data;
create policy "eco_kpi_data_member_all" on public.eco_kpi_data
  for all to authenticated
  using  (hospital_id in (select hospital_id from public.profiles where id = auth.uid()))
  with check (hospital_id in (select hospital_id from public.profiles where id = auth.uid()));

-- Done. Verify with:
--   select tablename, rowsecurity from pg_tables
--   where tablename in ('eco_full_capa','eco_kpi_data');
