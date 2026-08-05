-- Quick Checklist "reviewed" ticks.
-- Date: 5 August 2026
--
-- An informal, personal tracking tick: "I have looked at this row." It is NOT a
-- compliance signal and must never be read as one. The checklist's existing
-- done/not-done state stays derived from scores / kpi_data / committee_meetings
-- (see the done-rules in src/components/QuickChecklist.jsx) and is unaffected by
-- these tables. Nothing here writes to, or is read by, accreditation scoring.
--
-- Presence of a row = reviewed. Un-ticking deletes the row, so there is no
-- boolean that can drift out of step with what the user sees.
--
-- Programme separation is absolute: one table per programme, never shared.
-- Idempotent: safe to re-run.

do $$
declare
  t text;
begin
  foreach t in array array[
    'hco_checklist_reviews',
    'shco_full_checklist_reviews',
    'eco_full_checklist_reviews',
    'hco_elc_checklist_reviews',
    'shco_elc_checklist_reviews'
  ]
  loop
    execute format($f$
      create table if not exists public.%I (
        hospital_id uuid        not null references public.hospitals(id) on delete cascade,
        section     text        not null check (section in ('oes','kpis','committees')),
        item_code   text        not null,
        reviewed_at timestamptz not null default now(),
        reviewed_by uuid        references auth.users(id) on delete set null default auth.uid(),
        primary key (hospital_id, section, item_code)
      );
    $f$, t);

    -- Every read is "all ticks for this hospital", which the PK's leading
    -- column already serves; no extra index needed.

    execute format('alter table public.%I enable row level security;', t);

    -- Same hospital-scoped membership pattern as the other per-hospital tables.
    execute format('drop policy if exists %I on public.%I;', t || '_member_all', t);
    execute format($f$
      create policy %I on public.%I
        for all to authenticated
        using      (hospital_id in (select hospital_id from public.profiles where id = auth.uid()))
        with check (hospital_id in (select hospital_id from public.profiles where id = auth.uid()));
    $f$, t || '_member_all', t);
  end loop;
end $$;
