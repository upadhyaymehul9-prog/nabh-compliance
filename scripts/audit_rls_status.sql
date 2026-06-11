-- Diagnostic: report current RLS state for every table in the public schema.
-- READ-ONLY. Safe to run anytime in the Supabase SQL Editor.
-- Run this FIRST (audit HIGH item #5) to see which tables are exposed before
-- applying enable_rls_and_policies.sql.

-- 1) Which tables have RLS enabled vs disabled (disabled = anon key can read/write freely)
select
  c.relname                              as table_name,
  c.relrowsecurity                       as rls_enabled,
  c.relforcerowsecurity                  as rls_forced,
  coalesce(p.policy_count, 0)            as policy_count
from pg_class c
join pg_namespace n on n.oid = c.relnamespace
left join (
  select schemaname, tablename, count(*) as policy_count
  from pg_policies
  where schemaname = 'public'
  group by schemaname, tablename
) p on p.tablename = c.relname
where n.nspname = 'public'
  and c.relkind = 'r'
order by rls_enabled asc, c.relname;   -- tables with RLS off float to the top

-- 2) Full list of existing policies (so we don't clobber anything we didn't expect)
select
  tablename,
  policyname,
  cmd          as command,
  roles,
  qual         as using_expression,
  with_check   as with_check_expression
from pg_policies
where schemaname = 'public'
order by tablename, policyname;

-- 3) Confirm the ownership anchor exists: profiles(id -> hospital_id)
select column_name, data_type
from information_schema.columns
where table_schema = 'public' and table_name = 'profiles'
order by ordinal_position;
