-- Dental Clinic ELC progress tracker (checklist-based module).
-- Self-contained: does not touch any other programme's tables.
-- One row per assessment; three JSONB maps of { itemId: 'ready'|'pending'|'na' }.
-- Idempotent: safe to re-run.

create table if not exists public.dental_elc_progress (
  assessment_id uuid primary key references public.assessments(id) on delete cascade,
  doc_progress  jsonb not null default '{}'::jsonb,
  stat_progress jsonb not null default '{}'::jsonb,
  form_progress jsonb not null default '{}'::jsonb,
  updated_at    timestamptz not null default now()
);

-- RLS — same assessment-scoped membership pattern as scores / shco_elc_progress.
alter table public.dental_elc_progress enable row level security;

drop policy if exists "dental_elc_progress_member_all" on public.dental_elc_progress;
create policy "dental_elc_progress_member_all" on public.dental_elc_progress
  for all to authenticated
  using (assessment_id in (
    select a.id from public.assessments a
    where a.hospital_id in (select hospital_id from public.profiles where id = auth.uid())))
  with check (assessment_id in (
    select a.id from public.assessments a
    where a.hospital_id in (select hospital_id from public.profiles where id = auth.uid())));
