# Playbook: Measurement & Weekly Report

Principle: measure pipeline and revenue signals, not vanity metrics. Self-reported
attribution ("How did you hear about us?") is the cheapest reliable way to see
the dark funnel — WhatsApp forwards, consultant referrals, peer recommendations —
that analytics tools cannot track.

## Data sources

| Source | What it gives |
|--------|---------------|
| `data/prospects.csv` | Outreach pipeline by stage, follow-up discipline |
| `data/consultants.csv` | Partner pipeline |
| `data/content-backlog.csv` | Content shipped vs planned |
| `marketing/linkedin/content-queue.json` | Queue depth |
| Supabase | Signups, trials, conversions (founder pulls; agent asks) |
| Google Search Console | Queries, clicks, page performance (founder pulls monthly) |

Backlog app change (owned by product work, not this agent): add an optional
"How did you hear about us?" field to signup, stored in Supabase. Values:
LinkedIn / WhatsApp / Google search / AI assistant (ChatGPT etc.) / consultant
referral / colleague / other.

## Weekly report format

Save to `marketing/reports/YYYY-MM-DD.md`:

```markdown
# Marketing Week — [date]

## Pipeline
- Prospects: X total | identified A, connected B, conversation C, demo D, trial E, won F
- Moved stage this week: [names + from→to]
- Overdue follow-ups: N (drafted today: N)

## Partners
- Consultants: X total | stage breakdown
- Active partners: [names], this week's activity

## Content
- Shipped: [page + URL] (or "none — reason")
- Next up: [top planned backlog item]
- LinkedIn queue depth: N unposted

## Signups & attribution (from Supabase, if provided)
- Trials started: N | converted: N | attribution breakdown

## Next week
- [3 concrete actions max]
```

## Monthly review (first weekly run of the month)

- Funnel conversion by stage: where do prospects stall? Adjust touch templates.
- Which content pages appear in prospect conversations? Prioritise that cluster.
- Retire what is not working: a channel with zero conversations in 8 weeks gets
  its quota halved; reallocate to what converts.
- Search Console check: which queries grew, which pages need a refresh.

## Honesty rules

- Report misses plainly ("no page shipped this week — outreach took priority")
- Never inflate stage names: `conversation` means they replied substantively,
  `demo` means a call happened
