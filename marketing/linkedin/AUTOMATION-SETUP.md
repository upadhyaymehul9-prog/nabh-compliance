# LinkedIn daily posting — AccredReady company page

**Company page:** https://www.linkedin.com/company/135244094/  
**Organization ID:** `135244094`

This repo includes a **14-day rotating content queue** and a script that posts to your company page via LinkedIn’s **official API** (not browser bots — those risk account bans).

---

## What gets posted

| Day type | Content |
|----------|---------|
| **Text** | NABH tips + link to accredready.in |
| **Article** | Links to `/learn/` and `/blog/` pages |
| **Video** | Link post to your YouTube demo (3× per 14-day cycle) |

The **same YouTube video is not posted every day** — that triggers spam filters. Video link posts run ~2× per week; other days are tips and articles.

---

## Quick preview (no LinkedIn account needed)

```bash
python3 scripts/linkedin/daily_post.py --dry-run
python3 scripts/linkedin/daily_post.py --list
```

---

## One-time LinkedIn API setup (~30 min)

### Step 1 — Create a LinkedIn app

1. Go to https://www.linkedin.com/developers/apps → **Create app**
2. App name: `AccredReady Marketing`
3. LinkedIn Page: select **Accredready** (ID 135244094)
4. Verify the app (business email: doctor@accredready.in)

### Step 2 — Request products / scopes

In the app → **Products**, request:

- **Share on LinkedIn** (legacy) or **Community Management API**

Required scope for company posts:

- `w_organization_social`

You must be a **super admin** of the AccredReady company page.

### Step 3 — Get an access token

**Option A — OAuth test tool (easiest for testing)**

1. App → **Auth** → add redirect URL: `https://www.linkedin.com/developers/tools/oauth/redirect`
2. Use LinkedIn’s OAuth token generator with scope `w_organization_social`
3. Copy the access token (expires in ~60 days — see refresh below)

**Option B — Buffer / Hootsuite (no code)**

If API approval is slow, connect the company page to **Buffer** (free tier schedules 10 posts):

1. https://buffer.com → Connect LinkedIn → select AccredReady page
2. Schedule posts from `content-queue.json` manually once, then reuse queue

### Step 4 — Post manually first time

```bash
export LINKEDIN_ACCESS_TOKEN="your_token_here"
export LINKEDIN_ORG_ID="135244094"

python3 scripts/linkedin/daily_post.py --dry-run   # preview
python3 scripts/linkedin/daily_post.py --post      # publish
```

Log file: `marketing/linkedin/post-log.json` (prevents duplicate posts same day).

---

## Automate daily (GitHub Actions)

After you have a token:

1. GitHub repo → **Settings → Secrets → Actions**
2. Add secret: `LINKEDIN_ACCESS_TOKEN`
3. Workflow runs daily at **9:00 AM IST** (`.github/workflows/linkedin-daily-post.yml`)

**Token expiry:** LinkedIn tokens expire. Set a calendar reminder every 50 days to refresh, or implement OAuth refresh (advanced).

---

## Native video upload (optional)

The script posts **YouTube links** (LinkedIn shows a rich preview). For **native video** in the feed:

1. Upload manually once per week via LinkedIn → Create → Video, or
2. Use LinkedIn Marketing API video upload (multi-step; requires additional API access)

File: `public/accredready-promo.mp4` or YouTube URL.

---

## Edit the content queue

File: `marketing/linkedin/content-queue.json`

- 14 posts rotate automatically by day-of-year
- Add/edit posts — keep `id`, `type`, `text`; for links add `link`, `link_title`, `link_description`
- Types: `text` | `article` | `video_link`

---

## Recommended weekly rhythm

| Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|-----|-----|-----|-----|-----|-----|-----|
| NABH tip | YouTube link | Learn article | KPI tip | Blog link | — | Founder story |

Skip weekends in GitHub Action cron if you prefer (edit workflow).

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `403` / insufficient scope | Re-authorize with `w_organization_social` |
| `426` version header | Script uses `LinkedIn-Version: 202411` — update if LinkedIn deprecates |
| Token expired | Generate new token in Developer Portal |
| Duplicate post | Script blocks same post same day; use `--force` only for testing |

---

## What we cannot automate (LinkedIn rules)

- ❌ Scraping / browser bots to post (account ban risk)
- ❌ Posting identical video every day (spam)
- ❌ Liking/commenting at scale without API

- ✅ Official API posts with your admin token
- ✅ Scheduled queue + daily cron
- ✅ YouTube link posts for video days

---

*AccredReady · company page 135244094 · accredready.in*
