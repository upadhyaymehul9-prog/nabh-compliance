# Fix 1 — Expand OE retrieval limit

In supabase/functions/ai-assistant/index.ts, the retrieval query currently
limits results to 6 rows (.limit(6)) for both the oe_code match and the
keyword fallback search.

Change both limits to 12 rows instead of 6. This gives the AI more context
for broader questions (e.g. "what do I need for infection control overall")
that may legitimately span multiple OEs within a chapter or topic.

No other logic changes — keep the existing regex normalization, the system
prompt, and the no-hallucination rules exactly as they are.

After the change: redeploy with npx supabase functions deploy ai-assistant.
Test with a broad question (e.g. "what do I need for infection control")
and confirm the response now references more than 6 distinct OE codes if
relevant ones exist in that chapter.

---

# Fix 2 — Move Suggest button under the 3-dot menu

Currently there's a floating green "Suggest" button cluttering the same
screen area as the AI assistant widget and other floating buttons (visible
on the Dashboard).

Find this button in App.js (likely near the other floating action buttons:
Export PDF, WhatsApp, Tour replay, AI Assistant).

Move it OUT of the floating button stack. Instead, add it as a menu item
inside the existing "..." (3-dot) menu in the top navigation bar — the one
that's already next to "Switch" / theme toggle / profile icon in the header.

Match the existing dropdown menu styling (same T design tokens, same item
style as whatever else is already in that 3-dot menu, if anything is).
If the 3-dot menu doesn't currently have a dropdown built, create a simple
one that opens on click with at least this one item: "Suggest a feature"
(or whatever the button's original label/action was).

Do not change what clicking "Suggest" actually does — only relocate where
the trigger lives in the UI.

After both fixes: explicit per-file git add (never git add .), commit
"fix: expand OE retrieval limit, relocate Suggest button to menu",
npm run deploy.
