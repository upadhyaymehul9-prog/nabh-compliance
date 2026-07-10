# Playbook: LinkedIn Content Engine

Role in the system: LinkedIn is the prospecting surface and credibility layer
that feeds the WhatsApp outreach channel. Posts build the founder's authority so
that connection requests (T1 in the outreach sequence) land warm.

Infrastructure already exists: `marketing/linkedin/content-queue.json` rotates
one post daily at 9 AM IST (see `marketing/linkedin/AUTOMATION-SETUP.md`).
This playbook governs queue health and content mix.

## Queue health rules

- Keep at least 14 unposted items in the queue at all times
- Refresh monthly: retire posts that have run twice, add new ones
- Every new /learn or blog page shipped gets a queue entry within a week

## Content mix (per 10 posts)

| Count | Type | Notes |
|-------|------|-------|
| 4 | Practical NABH tip | Assessor-perspective, specific chapter codes, one concrete finding |
| 2 | /learn or blog article link | `type: article` with link metadata |
| 2 | Video | `type: video_link`, YouTube demo or new videos |
| 1 | Founder story / build-in-public | Why a feature exists, what a quality manager asked for |
| 1 | Question post | Ask quality managers about their practice — engagement source and prospect finder |

## Writing rules

All brand-skill rules apply. Additionally for LinkedIn:

- First line must stop a quality manager mid-scroll: a finding, a number, or a
  hard question. No "I'm excited to share."
- Short paragraphs (1-2 sentences), plain text, no more than 4 hashtags
- Always include the accredready.in link with a reason to click, not "check us out"
- No fake urgency; the CTA is always free trial or free resource
- Match existing queue JSON shape exactly (`id`, `type`, `text`, optional
  `link`, `link_title`, `link_description`)

## Engagement duty (daily, founder)

- Reply to every comment on our posts the same day
- Comment substantively on 3 posts from target-persona authors — comments by
  the founder on quality managers' posts are prospecting touches; log promising
  authors into `data/prospects.csv`

## Question-post harvesting

Anyone who comments on a question post with a real practice problem is a warm
prospect: add to `prospects.csv` at stage `identified` with the comment as the
personal hook.
