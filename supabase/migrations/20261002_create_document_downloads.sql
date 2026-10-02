-- Tracks every successful document download (HCO v2 + SHCO v2) so we can
-- see real usage: which hospitals download, which standards get pulled
-- most. Written by download-v2-hco-document and download-v2-policy edge
-- functions via the service role; no end-user RLS policy is defined on
-- purpose (RLS enabled, zero policies = anon/authenticated get no access,
-- same pattern as razorpay_webhook_events).

create table if not exists public.document_downloads (
  id uuid primary key default gen_random_uuid(),
  hospital_id uuid references public.hospitals(id),
  hospital_name text not null,
  programme text not null check (programme in ('hco','shco')),
  standard_code text not null,
  document_type text,
  document_id uuid,
  downloaded_at timestamptz not null default now()
);

create index if not exists document_downloads_hospital_id_idx on public.document_downloads(hospital_id);
create index if not exists document_downloads_downloaded_at_idx on public.document_downloads(downloaded_at);

alter table public.document_downloads enable row level security;
