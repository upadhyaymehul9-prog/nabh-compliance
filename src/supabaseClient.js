import { createClient } from "@supabase/supabase-js";

export const supabase = createClient(
  "https://tbptllgcjtiiqspxqcde.supabase.co",
  "sb_publishable_tEu-kA8f9VLW-5uvU4E7ZA_PtaX59bw",
  { auth: { flowType: "implicit", detectSessionInUrl: true, persistSession: true, autoRefreshToken: true } }
);
