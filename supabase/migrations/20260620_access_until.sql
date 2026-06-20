-- Paid-access mechanism: single source of truth for whether a hospital has access.
-- Access granted if access_until > now() OR plan = 'free' (bypassed in app code).
-- null access_until = locked (safe default; prevented by backfill + DB default below).

-- Step 1: Add column with no default (so existing rows get NULL, not wrong values)
ALTER TABLE public.hospitals
  ADD COLUMN IF NOT EXISTS access_until timestamptz;

-- Step 2: Backfill existing hospitals.
-- Mirrors the app's current trial logic:
--   effectiveStart = GREATEST(created_at, '2026-06-06') — same OFFICIAL_TRIAL_START floor
--   access_until   = effectiveStart + 14 days
-- This preserves current behaviour exactly: no one gets locked out, no one gets extra time.
UPDATE public.hospitals
SET access_until = GREATEST(created_at, '2026-06-06T00:00:00.000Z'::timestamptz) + interval '14 days'
WHERE access_until IS NULL;

-- Step 3: Set DB-level default so all future hospital inserts get a 14-day trial
-- automatically, without relying on the client to send the value.
ALTER TABLE public.hospitals
  ALTER COLUMN access_until SET DEFAULT now() + interval '14 days';


-- ── GRANT ACCESS (run per payment) ───────────────────────────────────────────

-- Grant 30 days from NOW (use for first payment or lapsed accounts):
-- UPDATE public.hospitals
-- SET plan = 'paid',
--     access_until = now() + interval '30 days'
-- WHERE id = (
--   SELECT hospital_id FROM public.profiles p
--   JOIN auth.users u ON u.id = p.id
--   WHERE u.email = 'CUSTOMER_EMAIL'
-- );

-- EXTEND by 30 days (use for renewals — stacks correctly if still active):
-- UPDATE public.hospitals
-- SET plan = 'paid',
--     access_until = GREATEST(access_until, now()) + interval '30 days'
-- WHERE id = (
--   SELECT hospital_id FROM public.profiles p
--   JOIN auth.users u ON u.id = p.id
--   WHERE u.email = 'CUSTOMER_EMAIL'
-- );


-- ── VERIFY backfill (run after Step 2 to sanity-check) ───────────────────────
-- SELECT id, name, created_at, access_until,
--        (access_until > now()) AS currently_active
-- FROM public.hospitals
-- ORDER BY created_at DESC
-- LIMIT 20;
