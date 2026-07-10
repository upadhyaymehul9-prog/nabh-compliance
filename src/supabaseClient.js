import { createClient } from "@supabase/supabase-js";

export const supabase = createClient(
  "https://tbptllgcjtiiqspxqcde.supabase.co",
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRicHRsbGdjanRpaXFzcHhxY2RlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY2NjkzNjAsImV4cCI6MjA5MjI0NTM2MH0.4CPgNp6ytVNRmTU0FJbu2io94QJmsAow5im-vGtoRAU",
  { auth: { flowType: "implicit", detectSessionInUrl: true, persistSession: true, autoRefreshToken: true } }
);
