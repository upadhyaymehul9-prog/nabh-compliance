-- Add created_by column to hospitals so orphaned rows can be traced back to their user.
-- This is insurance: if the profiles.hospital_id link ever fails silently again,
-- we can find and relink the hospital via created_by rather than losing it.

ALTER TABLE public.hospitals
  ADD COLUMN IF NOT EXISTS created_by uuid REFERENCES auth.users(id);

-- Index for the self-heal query in SetupScreen.init():
-- supabase.from("hospitals").select("id").eq("created_by", user.id)
CREATE INDEX IF NOT EXISTS idx_hospitals_created_by ON public.hospitals(created_by);

-- Update the SELECT RLS policy on hospitals to also allow a user to see hospitals
-- they created (even if profiles.hospital_id hasn't been linked yet).
-- This makes the self-heal query in SetupScreen.init() work correctly.
-- Note: no DELETE policy update needed — account deletion uses service role separately.
--
-- IMPORTANT: Check your current SELECT policy name in the Supabase dashboard first.
-- The policy below assumes the current policy is named something like "hospitals_select_own".
-- Replace the policy name below with whatever appears in Dashboard → Authentication → Policies → hospitals.
--
-- DROP POLICY IF EXISTS "hospitals_select_own" ON public.hospitals;
-- CREATE POLICY "hospitals_select_own" ON public.hospitals
--   FOR SELECT
--   USING (
--     id IN (SELECT hospital_id FROM public.profiles WHERE id = auth.uid())
--     OR created_by = auth.uid()
--   );
--
-- ^^^ Uncomment those 4 lines AFTER verifying the exact policy name in the dashboard.

-- Recovery: manually relink the 14 known orphaned hospitals (pre-created_by era).
-- Run this AFTER adding the created_by column and deploying the new code.
-- These hospitals have no created_by, so the self-heal can't find them automatically.
-- You'll need to manually identify the owner via auth.users email and run:
--
--   UPDATE public.profiles
--   SET hospital_id = '<hospital-uuid>'
--   WHERE id = (SELECT id FROM auth.users WHERE email = '<user-email>');
--
-- Check the Supabase dashboard for the list:
--   SELECT h.id, h.name, h.created_at
--   FROM hospitals h
--   WHERE h.id NOT IN (
--     SELECT hospital_id FROM profiles WHERE hospital_id IS NOT NULL
--   );
