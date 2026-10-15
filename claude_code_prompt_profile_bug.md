# Bug Investigation Prompt — for Claude Code terminal

Paste this into Claude Code on the PC with the actual nabh-compliance codebase.

---

I have a critical signup bug in AccredReady (NABH compliance SaaS). 

**Confirmed via Supabase SQL query:** 3 out of 3 recent real signups have a row in `auth.users` (auth succeeded, email confirmed within milliseconds) but NO corresponding row in the `profiles` table. This means new users sign up successfully but never get a profile created, so they can never proceed to add hospital name, select a programme, or reach the dashboard.

Affected users (for reference, do not contact):
- sbsms.2021@gmail.com — signed up 2026-06-18 05:37 UTC
- dushyantkataria382@gmail.com — signed up 2026-06-18 05:35 UTC
- jagatjeeban@gmail.com — signed up 2026-06-20 02:09 UTC

**My own test signups work fine** — profile gets created correctly when I test. This suggests either a race condition that only shows up on slower/mobile connections, or an issue specific to how real users are arriving (some come via WhatsApp outreach links — possible WhatsApp in-app browser issue), or an RLS policy edge case.

**What I need you to do:**

1. Find where the `profiles` row is supposed to get created after signup. Search for:
   - Any Postgres trigger function on `auth.users` (e.g. `handle_new_user`, `on_auth_user_created`)
   - Any client-side code in the signup component that inserts into `profiles` after calling `supabase.auth.signUp()`

2. Once found, identify the failure mode:
   - If it's a DB trigger: check if it could be failing silently (e.g. exception swallowed, missing error handling, depends on a column that might be null/missing)
   - If it's client-side: check what happens if the network is slow or the component unmounts/redirects before the insert completes (race condition), and whether errors are caught and surfaced or silently swallowed
   - Check current RLS policies on `profiles` table for INSERT — confirm a newly authenticated, unconfirmed-until-just-now user actually has permission to insert their own row. We patched several RLS policies recently (5 overly-permissive policies fixed) — check if one of those changes accidentally tightened something that breaks first-time inserts.

3. Check if the signup flow is being accessed via WhatsApp in-app browser vs regular browser — flag if there's any redirect or session-handling logic that could behave differently there.

4. Propose a fix. Strong preference for a **database trigger as the source of truth** (`AFTER INSERT ON auth.users` → creates `profiles` row server-side) rather than relying on client-side JS, because triggers can't fail due to network issues, tab closes, or slow connections on the user's end. If a trigger doesn't exist, this is likely the root cause — client-side profile creation is inherently fragile for exactly this kind of failure.

5. Before deploying, write 2-3 test cases including non-round/edge inputs (per our calculation verification rule) and a simulated slow-network test if possible.

6. After fix is deployed: also add a fallback — if a logged-in user has no `profiles` row when they hit the app, auto-create one on next load rather than leaving them stuck. This protects against any future instance of this bug and recovers the 3 affected users automatically next time they log in.

Follow CLAUDE.md rules: explicit per-file git add (never `git add .`), auto-push after `npm run deploy`, flag anything uncertain for my manual verification before going live.
