-- Lead capture for the NABH ELC Readiness Checklist (/nabh-elc-readiness-checklist/).
-- Same shape as revenue_leakage_leads and marketing_audit_leads: public insert only,
-- no SELECT policy, so captured leads aren't readable by anon/authenticated roles.
-- No phone column -- AccredReady only collects email for this tool.

create table if not exists public.elc_checklist_leads (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  name text not null,
  hospital_name text not null,
  email text not null,
  programme text,
  cert_type text,
  readiness_score integer,
  readiness_band text,
  answered_count integer,
  total_count integer
);

alter table public.elc_checklist_leads enable row level security;

drop policy if exists "public can insert audit leads" on public.elc_checklist_leads;
create policy "public can insert audit leads" on public.elc_checklist_leads
  for insert
  to anon, authenticated
  with check (true);
