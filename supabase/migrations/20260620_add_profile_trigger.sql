-- Auto-create a profiles row whenever a new user registers.
-- This is the source of truth for profile creation — client-side upserts are
-- unreliable when email confirmation is required (no session = no auth token = RLS rejects insert).

CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
  INSERT INTO public.profiles (id)
  VALUES (NEW.id)
  ON CONFLICT (id) DO NOTHING;
  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW
  EXECUTE FUNCTION public.handle_new_user();

-- Manual test cases (run in Supabase SQL editor to verify):
--
-- 1. Normal signup: INSERT a row into auth.users, confirm a profiles row appears with matching id.
--    SELECT id FROM public.profiles WHERE id = '<new-user-uuid>';
--
-- 2. Duplicate guard: Run the INSERT again with the same UUID, confirm no error and no duplicate.
--    SELECT COUNT(*) FROM public.profiles WHERE id = '<same-uuid>';  -- should be 1
--
-- 3. Existing broken accounts (3 affected users): Manually insert their profiles rows
--    so they can log in without waiting for a new signup:
--    INSERT INTO public.profiles (id)
--    SELECT id FROM auth.users
--    WHERE email IN (
--      'sbsms.2021@gmail.com',
--      'dushyantkataria382@gmail.com',
--      'jagatjeeban@gmail.com'
--    )
--    ON CONFLICT (id) DO NOTHING;
