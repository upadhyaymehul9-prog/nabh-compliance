-- SHCO knowledge base schema (book-only curated content)
-- Tier 1: chapter intents, summary of standards, general reference
-- Paired seed: scripts/shco_kb_seed.sql (generated from official PDF)

-- 1. Curated knowledge table
create table if not exists public.shco_kb (
  id uuid primary key default gen_random_uuid(),
  kb_type text not null check (kb_type in ('chapter_intent', 'chapter_summary', 'general', 'oe_interpretation')),
  chapter text,
  oe_code text,
  title text not null,
  content text not null,
  source_label text not null,
  book_page int,
  created_at timestamptz not null default now()
);

create index if not exists shco_kb_chapter_idx on public.shco_kb (chapter);
create index if not exists shco_kb_oe_code_idx on public.shco_kb (oe_code);
create index if not exists shco_kb_kb_type_idx on public.shco_kb (kb_type);

-- Full-text search vector (title + content + chapter + oe_code)
alter table public.shco_kb
  add column if not exists search_vector tsvector
  generated always as (
    setweight(to_tsvector('english', coalesce(title, '')), 'A') ||
    setweight(to_tsvector('english', coalesce(content, '')), 'B') ||
    setweight(to_tsvector('english', coalesce(chapter, '')), 'C') ||
    setweight(to_tsvector('english', coalesce(oe_code, '')), 'A')
  ) stored;

create index if not exists shco_kb_search_idx on public.shco_kb using gin (search_vector);

-- 2. OE table extensions for book-sourced fields
alter table public.shco_full_oes
  add column if not exists doc_required boolean,
  add column if not exists interpretation text,
  add column if not exists book_page_ref int;

comment on column public.shco_full_oes.doc_required is
  'True when the OE is marked * (mandatory system documentation) in the SHCO 3rd Edition book.';
comment on column public.shco_full_oes.interpretation is
  'Official NABH interpretation text — populate only from verified book source. NULL until extracted.';

-- FTS on shco_full_oes if not already present
alter table public.shco_full_oes
  add column if not exists search_vector tsvector
  generated always as (
    setweight(to_tsvector('english', coalesce(oe_code, '')), 'A') ||
    setweight(to_tsvector('english', coalesce(standard_code, '')), 'A') ||
    setweight(to_tsvector('english', coalesce(text, '')), 'B') ||
    setweight(to_tsvector('english', coalesce(standard_text, '')), 'C') ||
    setweight(to_tsvector('english', coalesce(chapter, '')), 'C') ||
    setweight(to_tsvector('english', coalesce(level, '')), 'D') ||
    setweight(to_tsvector('english', coalesce(interpretation, '')), 'B')
  ) stored;

create index if not exists shco_full_oes_search_idx on public.shco_full_oes using gin (search_vector);

-- 3. RLS — reference data, readable by authenticated users
alter table public.shco_kb enable row level security;
drop policy if exists "shco_kb_read" on public.shco_kb;
create policy "shco_kb_read" on public.shco_kb
  for select to authenticated using (true);

-- 4. Search RPCs for AI assistant
create or replace function public.search_shco_kb(q text, match_count int default 8)
returns table (
  id uuid,
  kb_type text,
  chapter text,
  oe_code text,
  title text,
  content text,
  source_label text,
  book_page int,
  rank real
)
language sql
stable
security definer
set search_path = public
as $$
  select
    k.id,
    k.kb_type,
    k.chapter,
    k.oe_code,
    k.title,
    k.content,
    k.source_label,
    k.book_page,
    ts_rank(k.search_vector, websearch_to_tsquery('english', q)) as rank
  from public.shco_kb k
  where k.search_vector @@ websearch_to_tsquery('english', q)
  order by rank desc
  limit greatest(match_count, 1);
$$;

create or replace function public.search_shco_full_oes(q text, match_count int default 8)
returns table (
  oe_code text,
  chapter text,
  standard_code text,
  level text,
  text text,
  achieve_tips jsonb,
  doc_required boolean,
  interpretation text,
  rank real
)
language sql
stable
security definer
set search_path = public
as $$
  select
    o.oe_code,
    o.chapter,
    o.standard_code,
    o.level,
    o.text,
    o.achieve_tips,
    o.doc_required,
    o.interpretation,
    ts_rank(o.search_vector, websearch_to_tsquery('english', q)) as rank
  from public.shco_full_oes o
  where o.search_vector @@ websearch_to_tsquery('english', q)
  order by rank desc
  limit greatest(match_count, 1);
$$;

grant execute on function public.search_shco_kb(text, int) to authenticated, anon;
grant execute on function public.search_shco_full_oes(text, int) to authenticated, anon;
