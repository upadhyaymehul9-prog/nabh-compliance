-- shco_policy_masters: version as text, revision_history jsonb, updated_at trigger
-- Date: 12 August 2026
--
-- Context: scripts/master-policy-todos.md — "Deferred from HIC.4" infrastructure item
-- (version / revision_history / updated_at). Template rendering already exists in
-- supabase/functions/_shared/policy-doc-template.ts (commit d64d84c). This migration
-- adds the database data path and backfills HIC.1–HIC.6.
--
-- Backfill dates verified against live created_at in Supabase (2026-08-12):
--   HIC.1  2026-08-03    HIC.4  2026-08-06 (version 1.1 — post-approval edit same day)
--   HIC.2  2026-08-01    HIC.5  2026-08-07
--   HIC.3  2026-08-03    HIC.6  2026-08-10
--
-- author_byline is deliberately NOT included — still open in the TODO; separate pass.
--
-- Idempotent where safe. Safe to re-run the backfill (deterministic values).

-- ---------------------------------------------------------------------------
-- 1. revision_history column
-- ---------------------------------------------------------------------------
alter table public.shco_policy_masters
  add column if not exists revision_history jsonb;

comment on column public.shco_policy_masters.revision_history is
  'Document revision history as a jsonb array of {version, date, description}. '
  'Dates are DD-MM-YYYY strings as rendered in the DOCX revision-history table.';

-- ---------------------------------------------------------------------------
-- 2. version: integer → text (skip if already text)
-- ---------------------------------------------------------------------------
do $$
begin
  if exists (
    select 1
    from information_schema.columns
    where table_schema = 'public'
      and table_name = 'shco_policy_masters'
      and column_name = 'version'
      and data_type = 'integer'
  ) then
    alter table public.shco_policy_masters
      alter column version drop default;

    alter table public.shco_policy_masters
      alter column version type text using (
        case
          when version::text ~ '^\d+$' then version::text || '.0'
          else version::text
        end
      );

    alter table public.shco_policy_masters
      alter column version set default '1.0';

    alter table public.shco_policy_masters
      alter column version set not null;
  end if;
end $$;

comment on column public.shco_policy_masters.version is
  'Semantic document version as text (e.g. "1.0", "1.1"). Not numeric — "2.10" must not sort as a number.';

-- ---------------------------------------------------------------------------
-- 3. updated_at trigger (column already exists; no trigger today)
-- ---------------------------------------------------------------------------
create or replace function public.set_shco_policy_masters_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists shco_policy_masters_set_updated_at
  on public.shco_policy_masters;

create trigger shco_policy_masters_set_updated_at
  before update on public.shco_policy_masters
  for each row
  execute function public.set_shco_policy_masters_updated_at();

-- ---------------------------------------------------------------------------
-- 4. Backfill HIC.1–HIC.6
--    Runs in the same session as the schema changes above. updated_at is set
--    explicitly from the latest revision-history date (TODO preference 2026-08-11).
-- ---------------------------------------------------------------------------

update public.shco_policy_masters
set
  version = '1.0',
  revision_history = '[{"version":"1.0","date":"03-08-2026","description":"Initial release."}]'::jsonb,
  updated_at = '2026-08-03 00:00:00+00'::timestamptz
where standard_code = 'HIC.1';

update public.shco_policy_masters
set
  version = '1.0',
  revision_history = '[{"version":"1.0","date":"01-08-2026","description":"Initial release."}]'::jsonb,
  updated_at = '2026-08-01 00:00:00+00'::timestamptz
where standard_code = 'HIC.2';

update public.shco_policy_masters
set
  version = '1.0',
  revision_history = '[{"version":"1.0","date":"03-08-2026","description":"Initial release."}]'::jsonb,
  updated_at = '2026-08-03 00:00:00+00'::timestamptz
where standard_code = 'HIC.3';

update public.shco_policy_masters
set
  version = '1.1',
  revision_history = '[
    {"version":"1.0","date":"06-08-2026","description":"Initial release."},
    {"version":"1.1","date":"06-08-2026","description":"Step 7 nested-bracket correction; step 31 and step 34 placeholder normalisation."}
  ]'::jsonb,
  updated_at = '2026-08-06 00:00:00+00'::timestamptz
where standard_code = 'HIC.4';

update public.shco_policy_masters
set
  version = '1.0',
  revision_history = '[{"version":"1.0","date":"07-08-2026","description":"Initial release."}]'::jsonb,
  updated_at = '2026-08-07 00:00:00+00'::timestamptz
where standard_code = 'HIC.5';

update public.shco_policy_masters
set
  version = '1.0',
  revision_history = '[{"version":"1.0","date":"10-08-2026","description":"Initial release."}]'::jsonb,
  updated_at = '2026-08-10 00:00:00+00'::timestamptz
where standard_code = 'HIC.6';

-- ---------------------------------------------------------------------------
-- 5. Post-run sanity check (informational — returns rows to the SQL Editor)
-- ---------------------------------------------------------------------------
select
  standard_code,
  version,
  revision_history,
  updated_at,
  created_at
from public.shco_policy_masters
where standard_code like 'HIC.%'
order by standard_code;
