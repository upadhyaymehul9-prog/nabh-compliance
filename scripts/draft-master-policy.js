// ⚠️ DEPRECATED — NOT IN USE. DO NOT RUN.
//
// This was the local-Node workaround for supabase/functions/draft-master-policy
// hitting Supabase's compute limit (see the note below). Both are now dead: the
// whole API-driven drafting flow has been replaced by drafting directly in
// Claude Code sessions — fetch the OEs and any linked committee from Supabase,
// draft and verify the content in-session with web search, then insert the row
// into shco_policy_masters with status='draft'. Doing it in-session also makes
// the universal-facts checklist reviewable before anything is written, which
// this script could not do.
//
// Kept in the repo for reference only. Two known reasons it would produce a bad
// row if anyone ran it today:
//   1. shco_policy_masters gained `abbreviations` and `disclaimer` columns
//      (2026-08-01). The insert object and DRAFT_SYSTEM_PROMPT below predate
//      them and would write a row with both fields empty.
//   2. It has no notion of the deferred-topic tracking now kept in
//      scripts/master-policy-todos.md.
// Neither is worth fixing unless this script is genuinely revived — if it is,
// fix both first.
//
// PHASE A — Master document drafting, run as a LOCAL Node script (not a Supabase
// Edge Function). Reason: this hit Supabase's free-tier serverless compute limit
// (WORKER_RESOURCE_LIMIT) because web_search + an 8000-token response is heavy.
// It also doesn't need to be an Edge Function at all — this isn't called by the
// app or by any hospital, it's a one-time authoring tool YOU run 43 times, once,
// during content review. Running it locally removes the resource cap entirely.
//
// Usage:
//   node draft-master-policy.js HIC.2
//
// Requires environment variables (set these in your terminal session, or a .env
// file loaded via `node -r dotenv/config`):
//   SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, ANTHROPIC_API_KEY
//
// Result: inserts/updates one row in shco_policy_masters with status='draft'.
// You then review it in Supabase Table Editor and manually change status to
// 'approved' (or 'needs_revision') before generate-hospital-policy can use it.

const { createClient } = require("@supabase/supabase-js");

const DRAFT_SYSTEM_PROMPT = `You are drafting a MASTER policy document for one NABH SHCO Full standard,
covering all its individual OEs together as one coherent document. This draft
will be reviewed by a human quality expert before ANY hospital ever sees it —
your job is to produce the most complete and accurate possible draft, flagging
anything you're unsure of rather than guessing.

Critical rules:
1. Write in your OWN original words — never copy phrasing from any NABH document
   (NABH content is their intellectual property).
2. This document must include ALL universal facts a real hospital SOP on this
   topic needs — not just what NABH's own OE text mentions. If the topic has a
   well-known international standard procedure (e.g. WHO's 6-step hand hygiene
   technique, WHO's 5 Moments, standard PPE donning/doffing sequence, standard
   BMW colour-coding), you MUST use web_search to verify the current, accurate
   version of that content and include it explicitly and completely. Do not
   summarize a well-known technique vaguely if the actual steps can be found
   and included.
3. Wherever the hospital's own identity would naturally appear (e.g. "the
   hospital shall...", "at [hospital]..."), use the literal placeholder token
   {{HOSPITAL_NAME}} instead of a generic phrase like "the organisation". This
   document will later be personalized by simple find-and-replace of
   {{HOSPITAL_NAME}} — no further AI editing happens after your draft is
   approved, so the placeholder must read naturally once substituted (e.g.
   "{{HOSPITAL_NAME}} shall install..." reads correctly as "HMP Foundation
   shall install...").
4. If a detail is genuinely hospital-specific (exact audit frequency, named
   role, specific target number beyond what's in the OE/KPI data), write
   "[Hospital to define]" rather than inventing a number.
5. In "universalFactsChecklist", list every universal (non-NABH-specific) fact
   you included and where you verified it from (e.g. "WHO 6-step hand hygiene
   technique — verified via WHO Guidelines on Hand Hygiene in Health Care").
   This is what the human reviewer will check first.
6. Output ONLY valid JSON, no other text, matching exactly this shape:
{
  "policyTitle": "string",
  "purpose": "string",
  "scope": "string",
  "policyStatement": "string",
  "procedureSteps": ["string", ...],
  "responsibility": "string",
  "references": "string",
  "distribution": "string",
  "universalFactsChecklist": "string — bullet-point summary for human review"
}`;

async function main() {
  const standardCode = process.argv[2];
  if (!standardCode) {
    console.error("Usage: node draft-master-policy.js <standard_code>  (e.g. HIC.2)");
    process.exit(1);
  }

  const supabaseUrl = process.env.SUPABASE_URL;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  const anthropicKey = process.env.ANTHROPIC_API_KEY;
  if (!supabaseUrl) throw new Error("SUPABASE_URL env var missing");
  if (!serviceKey) throw new Error("SUPABASE_SERVICE_ROLE_KEY env var missing");
  if (!anthropicKey) throw new Error("ANTHROPIC_API_KEY env var missing");

  const supabase = createClient(supabaseUrl, serviceKey);

  console.log(`Fetching OEs for standard ${standardCode}...`);
  const { data: oeRows, error: oeErr } = await supabase
    .from("shco_full_oes")
    .select("oe_code, chapter, standard_code, level, text, achieve_tips, doc_required, interpretation")
    .eq("standard_code", standardCode)
    .order("oe_code");
  if (oeErr) throw new Error(`OE fetch: ${oeErr.message}`);
  if (!oeRows || oeRows.length === 0) {
    throw new Error(`No OEs found for standard ${standardCode}`);
  }

  const mandatoryOeCodes = oeRows.filter((r) => r.doc_required).map((r) => r.oe_code);
  if (mandatoryOeCodes.length === 0) {
    throw new Error(`No OEs under ${standardCode} are flagged doc_required — this standard likely doesn't need a mandatory document.`);
  }
  console.log(`Found ${oeRows.length} OEs (${mandatoryOeCodes.length} mandatory-doc).`);

  const { data: committeeRows } = await supabase
    .from("shco_kb")
    .select("title, content, source_label")
    .eq("category", "committees")
    .overlaps("linked_oe_codes", oeRows.map((r) => r.oe_code));
  const committeeInfo = committeeRows && committeeRows.length > 0
    ? committeeRows.map((r) => `${r.title}: ${r.content}`).join("\n")
    : "No specific committee linked to this standard.";

  const oesSummary = oeRows
    .map((oe) => `- ${oe.oe_code} (${oe.level}${oe.doc_required ? ", MANDATORY DOC" : ""}): ${oe.text}\n  Achieve tips: ${Array.isArray(oe.achieve_tips) ? oe.achieve_tips.join(" | ") : "none"}\n  Interpretation: ${oe.interpretation ?? "none"}`)
    .join("\n\n");

  const userMessage = `Standard: ${standardCode}
Chapter: ${oeRows[0].chapter}

All OEs under this standard:
${oesSummary}

Linked Committee Info: ${committeeInfo}

Draft the master policy document JSON now. Remember: use web_search for any universal
technique/standard/guideline that a real SOP on this topic would need to state explicitly.`;

  console.log("Calling Anthropic API (with web_search enabled — this may take 30-60s)...");
  const anthropicRes = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": anthropicKey.trim(),
      "anthropic-version": "2023-06-01",
    },
    body: JSON.stringify({
      model: "claude-sonnet-4-6",
      max_tokens: 8000,
      system: DRAFT_SYSTEM_PROMPT,
      tools: [{ type: "web_search_20250305", name: "web_search" }],
      messages: [{ role: "user", content: userMessage }],
    }),
  });
  if (!anthropicRes.ok) {
    const body = await anthropicRes.text();
    throw new Error(`Anthropic API error: ${anthropicRes.status} — ${body}`);
  }
  const anthropicData = await anthropicRes.json();

  if (anthropicData.stop_reason === "max_tokens") {
    throw new Error("Response was truncated (hit max_tokens limit). Increase max_tokens further and retry.");
  }

  const textBlocks = (anthropicData.content ?? []).filter((b) => b.type === "text");
  const rawText = textBlocks.length > 0 ? textBlocks[textBlocks.length - 1].text : "{}";

  let content;
  try {
    const cleaned = rawText.replace(/```json|```/g, "").trim();
    content = JSON.parse(cleaned);
  } catch {
    console.error("RAW RESPONSE (for debugging):\n", rawText.slice(0, 2000));
    throw new Error("Failed to parse AI content as JSON — see raw response above.");
  }

  console.log("\n=== universalFactsChecklist (review this first) ===");
  console.log(content.universalFactsChecklist);
  console.log("=====================================================\n");

  console.log("Saving as DRAFT to shco_policy_masters...");
  const { data: inserted, error: insertErr } = await supabase
    .from("shco_policy_masters")
    .upsert(
      {
        standard_code: standardCode,
        chapter: oeRows[0].chapter,
        oe_codes: oeRows.map((r) => r.oe_code),
        policy_title: content.policyTitle,
        purpose: content.purpose,
        scope: content.scope,
        policy_statement: content.policyStatement,
        procedure_steps: content.procedureSteps,
        responsibility: content.responsibility,
        references_text: content.references,
        distribution: content.distribution,
        universal_facts_checklist: content.universalFactsChecklist,
        status: "draft",
        updated_at: new Date().toISOString(),
      },
      { onConflict: "standard_code" },
    )
    .select()
    .single();
  if (insertErr) throw new Error(`DB insert: ${insertErr.message}`);

  console.log(`✅ Draft saved for ${standardCode}: "${content.policyTitle}"`);
  console.log(`Review it in Supabase Table Editor → shco_policy_masters → row where standard_code = '${standardCode}'`);
  console.log(`Change status to 'approved' once you've verified the universal facts checklist against real sources.`);
}

main().catch((err) => {
  console.error("FAILED:", err.message);
  process.exit(1);
});
