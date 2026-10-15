# Hospital Setup Bug — Full Fix Instruction

Paste into Claude Code (it already has context on this bug from the investigation).

---

You already investigated the hospital-setup bug and found the root cause: line ~2545, the `profiles` upsert that sets `hospital_id` has NO error handling, so when it fails the hospital gets created but never linked to the user, leaving them stuck on the "Set up your hospital" screen on next login. We confirmed 14 orphaned hospitals in the database going back to May 18, including real ones (Dar Alfouad hospital, neuro spinal hospital, PPMHPL, SDW Hospital).

We also confirmed:
- RLS on profiles UPDATE is `own_profile_update USING (id = auth.uid())` — looks permissive, so RLS is probably NOT the blocker, but the swallowed error has hidden the true cause.
- The `hospitals` table has NO `created_by` / `owner_id` column — the ONLY user↔hospital link is `profiles.hospital_id`. This is a single point of failure: when that write fails, the hospital is orphaned with no way to trace it back.

Do the following. Do NOT deploy until I review the changes.

**1. Fix the profiles write (line ~2545):**
- Change `.upsert()` to `.update()` — the profile row already exists at this point (created by the trigger at signup), so we're updating, not inserting. Update where `id = user.id`, setting `hospital_id`, `role`, `name`.
- CAPTURE the error: `const { error } = await supabase.from("profiles").update({...}).eq("id", user.id);`
- If `error`, surface it to the user via the existing `setError()` and `console.error()` it with a clear label like `"Hospital link failed:"` so the real cause is visible in the browser console. Do NOT swallow it.
- If the link fails, the hospital row was already created (line ~2543) — decide the cleanest UX: either roll back / delete the just-created hospital so we don't orphan it, OR keep it and retry the link. Recommend the approach and explain the tradeoff before implementing.

**2. Add a recovery-safety column to hospitals:**
- Add a `created_by uuid` column to the `hospitals` table (write the migration SQL — I'll run it in Supabase).
- Update the hospital INSERT (line ~2543) to stamp `created_by: user.id`.
- This way, even if the profile link ever fails again, orphaned hospitals can be traced back to their user. Insurance against this exact bug recurring.

**3. Add a self-heal fallback (like the profile auto-recovery):**
- On app load, if a user has a `created_by` hospital but their `profiles.hospital_id` is null (orphaned-link state), auto-relink it. This recovers anyone who hits this in the gap before/after deploy. (This only works for hospitals created AFTER created_by is added — acknowledge that limitation.)

**4. Before deploying:**
- Write 2-3 test cases: normal hospital creation (link succeeds), simulated link failure (error surfaces, no silent swallow), and the self-heal path.
- Tell me exactly what to test manually: a fresh signup → create hospital → confirm `profiles.hospital_id` is set in Supabase, with browser console open to confirm no swallowed errors.

Follow CLAUDE.md: explicit per-file git add, auto-push after npm run deploy, flag anything uncertain for manual verification. The Supabase migration (created_by column) must be run manually in the dashboard, NOT via npm run deploy — give me that SQL separately.

Show me all changes before deploying. Do not deploy yet.
