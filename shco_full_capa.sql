-- shco_full_capa: stores CAPA (Corrective Action / Preventive Action) entries
-- for SHCO Full Accreditation gaps. Scoped by hospital_id + oe_code (unique pair).
--
-- HOW TO RUN:
--   Run this entire file in the Supabase SQL Editor once.
--   Idempotent — safe to re-run.

create table if not exists public.shco_full_capa (
  id                 uuid        default gen_random_uuid() primary key,
  hospital_id        uuid        not null references public.hospitals(id) on delete cascade,
  oe_code            text        not null,
  finding            text        not null default '',
  action_planned     text        not null default '',
  responsible_person text        default '',
  target_date        date,
  status             text        default 'open',
  created_at         timestamptz default now(),
  updated_at         timestamptz default now(),
  unique(hospital_id, oe_code)
);

-- RLS: hospital members can do full CRUD on their own rows
alter table public.shco_full_capa enable row level security;

drop policy if exists "shco_full_capa_member_all" on public.shco_full_capa;
create policy "shco_full_capa_member_all" on public.shco_full_capa
  for all to authenticated
  using  (hospital_id in (select hospital_id from public.profiles where id = auth.uid()))
  with check (hospital_id in (select hospital_id from public.profiles where id = auth.uid()));
