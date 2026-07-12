# Plan: First 10 Paying Customers

Owner: Dr. Mehul Upadhyay  
Operated with: `accredready-marketing-agent`  
Target: **10 hospitals paying ₹499/month**  
Method: founder-led WhatsApp + consultant partners + commercial SEO pages (zero paid ads until messaging is proven)

This plan uses only channels already in `marketing/STRATEGY.md` that have published Indian B2B SaaS benchmarks: WhatsApp reply rates near 68% vs 4–9% cold email, CAC under ₹1,000, and founder trial-save touches moving conversion from ~14% → ~38% in published cohorts.

## Math (conservative)

Goal: **10 paid** in ~8 weeks of disciplined outreach.

| Stage | Volume needed | Assumption |
|-------|---------------|------------|
| LinkedIn T1 (new connects) | 160 | 20/week × 8 weeks |
| Move to WhatsApp / conversation | 80 | ~50% of accepts + warm replies |
| Demo / readiness walkthrough | 40 | ~50% of conversations |
| Trial start | 28 | ~70% of demos |
| Paid (won) | **10** | ~35% trial→paid with day-11 founder save touch |

If trial→paid is weaker (20%), raise weekly T1 to 25–30 — do not start Meta ads yet.

Revenue at 10 paid: **₹4,990 MRR**. That is the proof point, not the ceiling.

## Who to sell first (ICP order)

1. **Quality managers / NABH coordinators** at 50–200 bed hospitals preparing for HCO Full or ELC (owns the pain: Excel reconciliation).
2. **Owner-doctors / administrators** at SHCOs and nursing homes chasing ELC for empanelment or state incentives.
3. **NABH consultants** with 5+ active client facilities (one partner can deliver multiple hospital accounts).

Do **not** chase large multi-specialty chains first — longer sales cycles kill the 10-customer clock.

## Three engines that produce the 10

### Engine A — Founder WhatsApp (delivers ~7 of 10)

Twice weekly: add **5 qualified prospects** to `data/prospects.csv` and send T1 the same day (10/week).

Sequence (from `playbooks/whatsapp-outreach.md`):

| Day | Touch |
|-----|--------|
| 0 | LinkedIn connect — their work, no product pitch |
| 2–3 | One useful NABH pointer (programme-specific) |
| 5–7 | Free resource: gap analysis, timeline, or new decision pages |
| 10 | Ask assessment timing; offer 10-minute readiness walkthrough |
| 15 | Case-style: tracking between consultant visits / Excel drift |
| 21 | Soft close: 14-day trial, you set up their programme structure |
| 11–13 of trial | **Save touch** referencing their actual usage — highest leverage conversion |

Free resources to send (live):

- https://accredready.in/learn/nabh-gap-analysis
- https://accredready.in/nabh-software-vs-excel
- https://accredready.in/nabh-consultant-vs-software
- https://accredready.in/learn/nabh-accreditation-timeline

**Weekly founder time budget:** ~5–7 hours (prospecting + sending + replies within 2 hours during work hours).

### Engine B — Consultant partners (delivers ~2–3 of 10)

One active consultant with 10–20 clients can seed multiple trials without cold outreach.

Weekly: identify **3 consultants**, log in `data/consultants.csv`, send P1 (peer intro).

Offer stack (value first):

1. Free multi-facility readiness view for their clients
2. Referral / extended free months (you set exact terms per partner)
3. Co-marketing byline on a /learn or decision page

Close path: P1 → P2 (Excel drift between visits) → 15-min demo → pilot 1–2 client hospitals → `active`.

### Engine C — Commercial SEO pages (warms inbound + supports A/B)

Already live decision pages:

1. `/nabh-software-vs-excel` — Excel fragmentation buyers
2. `/nabh-consultant-vs-software` — “do we need software if we have a consultant?” buyers

Use these as T3/T5 links. Request indexing in Google Search Console for both. Do **not** wait for SEO to deliver the first 10 — outreach does; SEO compounds.

## Weekly operating rhythm (non-negotiable)

| When | Action | Done when |
|------|--------|-----------|
| Mon + Thu | 5 new prospects each day + T1 | 10 rows added + touched in CSV |
| Daily | LinkedIn post + reply to every comment/DM | Queue post published |
| Daily | WhatsApp replies < 2 hours (work hours) | Conversations advancing |
| Tue | 3 consultant P1s | 3 rows in consultants.csv |
| Fri | `/marketing weekly` + pipeline review | Report in `marketing/reports/` |
| Every trial day 11–13 | Personal save message | Trial→won or clear next step |

## Trial → paid playbook (protect the 10)

For every trial:

1. Same-day setup call or WhatsApp: load their programme (HCO/SHCO/ELC).
2. Get them to score **one chapter** in the first 48 hours.
3. Day 7: check-in — which gaps are open?
4. Day 11–13: founder save touch with usage-specific detail + offer to finish setup.
5. Day 14: if not paid, ask blocker; offer one more week only if they are actively scoring.

## Tracking (CSV is the source of truth)

- `prospects.csv` stages: `identified → connected → conversation → demo → trial → won | lost | dormant`
- `consultants.csv` stages: `identified → contacted → call → pilot → active | declined`
- After each won: note source (`whatsapp` / `consultant` / `seo` / `linkedin`)

App backlog (product): add “How did you hear about us?” at signup so dark-funnel referrals are visible.

## What not to do until you have 10

- No Meta CTWA ads (₹50k/month) until Engines A+B convert
- No broad “brand awareness” content that does not feed a free resource or trial
- No competitor bashing; no OE-count claims in public posts
- No automating WhatsApp sends — founder voice is the mechanism

## 8-week scoreboard

| Week | Cumulative T1 | Conversations | Trials | Paid |
|------|---------------|---------------|--------|------|
| 2 | 40 | 15 | 4 | 1 |
| 4 | 80 | 35 | 12 | 3–4 |
| 6 | 120 | 55 | 20 | 6–7 |
| 8 | 160 | 80 | 28 | **10** |

If Week 4 paid < 2: fix messaging (lead with Excel drift / between-visit tracking), not volume. If conversations are high but trials low: shorten the ask to a 10-minute readiness view. If trials are high but paid low: strengthen day-11 save touches and same-day programme setup.

## Your first actions this week (founder)

1. Post today’s LinkedIn (or enable `LINKEDIN_ACCESS_TOKEN`).
2. Add **10 prospects** to `prospects.csv` from LinkedIn (“quality manager NABH”, “NABH coordinator”).
3. Add **3 consultants** to `consultants.csv`.
4. Send T1 / P1 messages (agent drafts; you send).
5. Search Console: Request Indexing on `/nabh-consultant-vs-software` and refresh sitemap.

When those two CSVs have real names, the next `/marketing weekly` run drafts every due touch for you.
