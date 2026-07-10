# Playbook: SEO + AEO/GEO Content Engine

Why this channel: bottom-funnel, commercial-intent pages are the documented
highest-ROI SEO work for SaaS (4x organic pipeline in published case studies by
prioritising evaluator keywords over traffic). For healthcare India, AI search
(ChatGPT, Perplexity, Google AI Overviews) is now a primary research channel, so
every page is written to be citable by answer engines.

All structure, voice, AEO, and GEO rules come from
`.claude/skills/accredready-marketing/SKILL.md` and its `data/` CSVs. This
playbook adds the pipeline and prioritisation on top.

## Content types, in priority order

1. **Commercial / decision pages** (highest priority — converts evaluators)
   - "NABH software vs Excel tracker", "NABH consultant vs software",
     "best NABH compliance software for SHCOs", pricing/cost explainers
   - Target searches where the buyer is choosing, not learning
2. **Programme-specific /learn pages** — gap analysis, timelines, checklists
   per programme (HCO, SHCO, ELC, ECO)
3. **Blog articles** — E-E-A-T authority: assessor-perspective pieces,
   chapter deep-dives, KPI guides
4. **Refreshes** — pages older than 6 months: update facts, add FAQ schema,
   apply answer-first opening if missing

## Pipeline

Backlog lives in `data/content-backlog.csv`. Each `/marketing content` run:

1. Pick the highest-priority row with status `planned`.
2. Set status `drafting`. Write the page:
   - Follow the SEO structure template in the brand skill (H1 keyword,
     answer-first opening of 100-150 words, question H2s, FAQ section with
     JSON-LD schema, /learn CTA block)
   - Author byline per `geo-signals.csv`
   - At least one specific number and one citation to nabh.co or official PDF
   - Never publish OE counts or per-chapter standard counts
3. Interlink: add a link from at least 2 existing related informational pages
   to this page, and from this page to 1 commercial page (if it is informational).
4. Update `sitemap.xml`.
5. Local-first: `npm start`, verify the page renders on localhost:3000
   (static pages: open the HTML directly). Only then deploy per `CLAUDE.md`.
6. Set status `built` (after deploy: `live`), fill `url` and `shipped_date`.

## Prioritisation rules

- Commercial intent beats informational at equal effort
- Fills a gap in an existing topic cluster beats a new orphan topic
- A page targeting a programme with government incentives (ELC) ranks up
- Anything requiring OE-count specifics gets status `skip` with a note

## Interlinking check (monthly)

Every informational page must link to at least one commercial page. Grep the
`public/` HTML for orphans and fix in the monthly cycle. Internal links from
informational to product pages measurably lift product-page rankings.

## Cadence

One page shipped per week minimum. A refresh counts as half a page.
