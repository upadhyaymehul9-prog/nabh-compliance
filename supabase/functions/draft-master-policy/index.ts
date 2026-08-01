// PHASE A — Master document drafting (one-time per standard, human-reviewed).
//
// This is NOT the hospital-facing function. It drafts ONE master policy for
// one NABH standard (e.g. "HIC.2"), covering all its OEs, and inserts it into
// shco_policy_masters with status='draft'. A human (Mk) must review and
// change status to 'approved' before generate-hospital-policy can ever use it.
//
// Key difference from the old generate-policy-document: this call has
// web_search enabled, so universal facts (WHO technique steps, standard
// international guidelines, etc.) get verified against real current sources
// instead of relying on the model's training-data recall alone — the gap that
// caused the missing WHO 6-step hand hygiene technique earlier.
//
// Input: { standard_code: "HIC.2" }

import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const CORS = {
  "Access-Control-Allow-Origin": "https://accredready.in",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};

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

Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: CORS });

  try {
    const { standard_code } = await req.json();
    if (!standard_code || typeof standard_code !== "string") {
      return Response.json({ error: "Missing standard_code" }, { status: 400, headers: CORS });
    }

    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
    const anthropicKey = Deno.env.get("ANTHROPIC_API_KEY");
    if (!supabaseUrl) throw new Error("SUPABASE_URL missing");
    if (!serviceKey) throw new Error("SUPABASE_SERVICE_ROLE_KEY missing");
    if (!anthropicKey) throw new Error("ANTHROPIC_API_KEY missing");

    const supabase = createClient(supabaseUrl, serviceKey);

    // --- Fetch ALL OEs under this standard (e.g. all of HIC.2.*) ---
    const { data: oeRows, error: oeErr } = await supabase
      .from("shco_full_oes")
      .select("oe_code, chapter, standard_code, level, text, achieve_tips, doc_required, interpretation")
      .eq("standard_code", standard_code)
      .order("oe_code");
    if (oeErr) throw new Error(`OE fetch: ${oeErr.message}`);
    if (!oeRows || oeRows.length === 0) {
      return Response.json({ error: `No OEs found for standard ${standard_code}` }, { status: 404, headers: CORS });
    }

    const mandatoryOeCodes = oeRows.filter((r) => r.doc_required).map((r) => r.oe_code);
    if (mandatoryOeCodes.length === 0) {
      return Response.json(
        { error: `No OEs under ${standard_code} are flagged doc_required — this standard likely doesn't need a mandatory document.` },
        { status: 400, headers: CORS },
      );
    }

    // --- Fetch linked committee, if any ---
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

    const userMessage = `Standard: ${standard_code}
Chapter: ${oeRows[0].chapter}

All OEs under this standard:
${oesSummary}

Linked Committee Info: ${committeeInfo}

Draft the master policy document JSON now. Remember: use web_search for any universal
technique/standard/guideline that a real SOP on this topic would need to state explicitly.`;

    const anthropicRes = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": anthropicKey.trim(),
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({
        model: "claude-sonnet-4-6",
        max_tokens: 4000,
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

    // With web_search enabled, content may include tool_use/tool_result blocks
    // before the final text block — take the LAST text block as the answer.
    // deno-lint-ignore no-explicit-any
    const textBlocks = (anthropicData.content ?? []).filter((b: any) => b.type === "text");
    const rawText = textBlocks.length > 0 ? textBlocks[textBlocks.length - 1].text : "{}";

    let content: {
      policyTitle: string; purpose: string; scope: string; policyStatement: string;
      procedureSteps: string[]; responsibility: string; references: string;
      distribution: string; universalFactsChecklist: string;
    };
    try {
      const cleaned = rawText.replace(/```json|```/g, "").trim();
      content = JSON.parse(cleaned);
    } catch {
      throw new Error(`Failed to parse AI content as JSON: ${rawText.slice(0, 500)}`);
    }

    // --- Insert as DRAFT — human must approve before hospital-facing use ---
    const { data: inserted, error: insertErr } = await supabase
      .from("shco_policy_masters")
      .upsert(
        {
          standard_code,
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

    return Response.json({ draft: inserted }, { headers: CORS });
  } catch (err) {
    console.error(err);
    return Response.json({ error: (err as Error).message }, { status: 500, headers: CORS });
  }
});
