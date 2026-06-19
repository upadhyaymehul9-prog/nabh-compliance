Bug found in live testing: when the AI assistant can't find a matching OE,
it adds speculative commentary about NABH structure that is NOT grounded in
retrieved context — e.g. guessing a chapter exists ("likely housed under a
dedicated IC chapter") that isn't even the correct chapter code (real code
is IPC, not IC). This violates the no-hallucination rule even though the
core refusal-to-answer behavior is correct.

Fix: update the system prompt in supabase/functions/ai-assistant/index.ts.
Add this explicit rule to the existing system prompt rules list:

"6. When you cannot find a match, state ONLY that no matching SHCO Full
requirement was found, and suggest the user rephrase or check with their
AccredReady admin. Do NOT speculate about which chapter, standard, or OE
might contain the answer, do NOT guess chapter names or codes, and do NOT
describe NABH structure beyond what is explicitly in <context>. If <context>
is empty, your entire response must be limited to the refusal sentence —
nothing else."

Also: the suggested follow-up question chips (HRM.2.b, PSQ.1.a etc.) shown
after a no-match response are pulling from the KEYWORD FALLBACK search
results, which matched loosely related but wrong content. When <context> is
empty/no real match, do not show suggestion chips drawn from irrelevant
keyword matches — either show no chips, or show a fixed set of example
questions instead (the ones already in the welcome message: infection
control, antibiotic approvals, injection practices, IC committee meetings).

After the fix: redeploy with npx supabase functions deploy ai-assistant,
then test the EXACT same question that failed: "What do I need to do for
infection control programme documentation?" — confirm the response no
longer mentions any chapter codes or speculates about NABH structure.
