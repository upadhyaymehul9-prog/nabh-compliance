-- v2 policy delivery: pre-rendered .docx masters in Supabase Storage.
-- Edge function download-v2-policy fetches by master_docx_path and personalises
-- «Hospital Name» → the requesting hospital's name. v1 fields and
-- generate-hospital-policy are untouched.
--
-- Run in Supabase SQL Editor if not applied via migration tooling.

-- ---------------------------------------------------------------------------
-- 1. Column on shco_policy_masters
-- ---------------------------------------------------------------------------
alter table public.shco_policy_masters
  add column if not exists master_docx_path text;

comment on column public.shco_policy_masters.master_docx_path is
  'Storage object path (within bucket policy-masters-v2) for the finished v2 '
  'master .docx with «Hospital Name» placeholder. Null for v1 database-rendered masters.';

-- ---------------------------------------------------------------------------
-- 2. Private storage bucket for v2 masters
-- ---------------------------------------------------------------------------
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values (
  'policy-masters-v2',
  'policy-masters-v2',
  false,
  52428800,
  array[
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/octet-stream'
  ]
)
on conflict (id) do nothing;

-- Service role (edge functions) can read/write objects in this bucket.
-- Authenticated users do not read masters directly; download-v2-policy streams
-- the personalised file after substitution.

drop policy if exists "service role full access policy-masters-v2"
  on storage.objects;

create policy "service role full access policy-masters-v2"
  on storage.objects
  for all
  to service_role
  using (bucket_id = 'policy-masters-v2')
  with check (bucket_id = 'policy-masters-v2');
