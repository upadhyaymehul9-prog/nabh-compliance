# Playbook: Founder-Led WhatsApp Outreach

Why this channel: structured personal WhatsApp outreach is the documented
cheapest growth motion for Indian B2B SaaS — reply rates near 68% vs 4-9% for
cold email/LinkedIn, CAC under ₹1,000 vs ₹9,000+ for paid demo booking.
Sources: richautomate.in founder-led growth playbook (2026), toflow.ai WhatsApp
B2B sequence guide.

The agent drafts every message; Dr. Mehul sends from his personal WhatsApp
Business number. Founder voice is the mechanism — do not automate sending.

## Who to target

Search LinkedIn for (India, healthcare):
- "quality manager" + NABH, "NABH coordinator", "quality assurance" hospital
- "hospital administrator" at 20-200 bed facilities
- Owner-doctors of nursing homes / SHCOs in states with ELC incentive schemes
- People posting or commenting about NABH assessment prep

Qualify before adding to `data/prospects.csv`: facility type, likely programme
(HCO/SHCO/ELC/ECO), and a personal hook (their post, their hospital's news,
their city).

## The touch sequence

Log every touch and set `next_action_date` in `prospects.csv`.

| Touch | Day | Channel | Content |
|-------|-----|---------|---------|
| T1 | 0 | LinkedIn | Connection request, short note referencing their work — no product mention |
| T2 | 2-3 | LinkedIn | Share one specific, useful NABH pointer relevant to their facility type |
| T3 | 5-7 | WhatsApp (if number known) or LinkedIn | Free resource: a /learn page or checklist matching their programme |
| T4 | 10 | WhatsApp | Ask about their assessment timeline; offer a 10-minute gap-analysis walkthrough |
| T5 | 15 | WhatsApp | Case-style message: how a quality team tracks readiness in one workspace |
| T6 | 21 | WhatsApp | Soft close: free trial link, offer to set up their programme structure |
| — | +30 | — | No response after T6: mark `dormant`, revisit next quarter |

Rules:
- Every message must contain one specific fact or resource. Never "just following up."
- Reference the earlier touch ("sent you the gap analysis guide last week...").
- Reply within 2 hours during work hours once a conversation starts.
- Move stage in the CSV the same day anything changes.

## Message templates

Adapt, never paste verbatim — insert their name, facility, programme, city.

T1 (LinkedIn note):
> Hi [Name], saw your post on [topic]. I head medical services at HMP Foundation
> and work on NABH readiness daily — always good to connect with quality people
> doing this work.

T3 (first WhatsApp):
> Hi [Name], Mehul here — we connected on LinkedIn. You mentioned [facility] is
> working toward [programme]. This gap-analysis walkthrough we published may
> save your team some spreadsheet hours:
> https://accredready.in/learn/nabh-gap-analysis.html. Happy to answer any
> NABH question, no strings.

T4:
> Quick question — when is [facility] targeting its assessment? Asking because
> the order you close gaps in matters a lot (CORE OEs first). If useful I can
> show you a 10-minute readiness view for [programme] on a call this week.

T6:
> [Name], if the spreadsheet reconciliation before audits is still eating your
> team's time — AccredReady has a 14-day free trial, no card needed. I'll set up
> your [programme] structure myself so you start from a working baseline:
> https://accredready.in

## Trial-to-paid save touch

For any prospect in `trial` stage, on day 11-13 of their trial draft a personal
message referencing their actual usage ("you've scored X chapters so far...")
plus an offer to help finish setup. This single founder touch is the documented
highest-leverage conversion point for Indian B2B SaaS trials (14% → 38% save
rate in published cohorts).

## Weekly quota

- 5 new qualified prospects added and T1-touched, twice a week (10/week total)
- All due follow-ups drafted every `/marketing weekly` run
- Pipeline review: anything stuck in `connected` for 3+ weeks gets a T3 resource touch or goes `dormant`
