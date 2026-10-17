-- Records who downloaded each document and whether they acknowledged the
-- consent checkbox ("I will read this document thoroughly, adapt it, and
-- this document's use is entirely my hospital's own responsibility") before
-- the download fired. user_id ties the download to the specific signed-in
-- account, not just the hospital. consent_version lets us tell which wording
-- of the consent text a given download was made under, in case it changes.

alter table public.document_downloads
  add column if not exists user_id uuid references auth.users(id),
  add column if not exists consent_acknowledged boolean not null default false,
  add column if not exists consent_version text;

create index if not exists document_downloads_user_id_idx on public.document_downloads(user_id);
