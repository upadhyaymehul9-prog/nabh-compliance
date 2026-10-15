# Build Paid-Access Mechanism — Claude Code Prompt

Investigate first, then build. Do NOT deploy until I review. Show me all changes.

## Context
The app currently has only `plan` values 'free' and 'trial' on the hospitals table. `plan_activated_at` is null for everyone. Trials appear to expire 14 days from `created_at`. There is NO paid-access concept and no way to unlock a hospital after payment. I need a clean, reusable paid-access system so that when someone pays, I run one SQL command to grant 30 days of access.

## Step 1 — Investigate current logic (report before building)
- Find exactly how the app decides "has access" vs "show trial-expired paywall."
- Which column(s)? Is it `created_at + 14 days`? Does `plan='free'` currently mean unlimited access or is it also subject to expiry?
- Report the exact current logic before changing anything.

## Step 2 — Proposed design (use unless investigation shows a problem)
Single source of truth: an `access_until timestamptz` column on hospitals.
- Access granted if `access_until > now()`. Otherwise show paywall.
- On signup / hospital creation: set `access_until = now() + interval '14 days'` (the trial).
- `plan` column becomes a label only ('trial' / 'paid' / 'free'), not the access gate.
- `plan='free'` (if it should mean permanent comp access) = set `access_until` far in the future (e.g. 2099) OR handle 'free' as an explicit bypass — recommend which and explain.

If you think a different design is cleaner given the existing code, propose it and explain the tradeoff before building.

## Step 3 — Build
1. Migration SQL (I run manually in Supabase): add `access_until timestamptz` column. Backfill existing hospitals: set `access_until = created_at + interval '14 days'` so current trial logic is preserved exactly (no one's access changes unexpectedly).
2. Update App.js access check to use `access_until > now()` as the gate. Keep behaviour identical for current trial users (that's why we backfill from created_at).
3. Update hospital creation to set `access_until = now() + interval '14 days'`.
4. Make sure the check fails safe: if `access_until` is null for any reason, decide explicitly whether that = locked or open, and document it. (Recommend: null = locked, to avoid accidental free access — but confirm this won't lock out existing users, which is why we backfill.)

## Step 4 — Give me the reusable "grant 1 month" command
A clean SQL command I can run per payment, replacing the email:
```sql
UPDATE hospitals
SET plan = 'paid', access_until = now() + interval '30 days'
WHERE id = (SELECT hospital_id FROM profiles p JOIN auth.users u ON u.id = p.id WHERE u.email = 'CUSTOMER_EMAIL');
```
Confirm this matches the logic you build. Also give me a variant that EXTENDS (adds 30 days to existing access_until if still active, rather than resetting) so renewals stack correctly:
```sql
SET access_until = GREATEST(access_until, now()) + interval '30 days'
```

## Step 5 — Tests + manual checklist
- Test: trial user within 14 days → access. Trial expired → paywall. Paid user with future access_until → access. Paid expired → paywall.
- Tell me exactly what to test manually after deploy (including: confirm an EXISTING active trial user did NOT get locked out by the change).

## Critical safety
- The backfill is the riskiest part — if it's wrong, it could lock out or wrongly unlock existing users. Show me the exact backfill SQL and the access-check logic side by side so I can verify they agree before I run anything.
- Migration runs manually in Supabase, NOT via npm run deploy.
- Follow CLAUDE.md: explicit per-file git add, auto-push after deploy.
- Show all changes. Do not deploy until I say go.
