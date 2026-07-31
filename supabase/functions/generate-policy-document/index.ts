// Generates one NABH-format policy document (.docx) for a given SHCO Full OE code.
//
// Pipeline: fetch real OE data (+ linked committee, via the same linked_oe_codes
// mechanism built for Gennie) → Claude writes ORIGINAL policy prose from that data
// only (never copies NABH's own document wording — legal requirement, NABH content
// is their IP) → fill the fixed docx template → return the file.
//
// Input: { oe_code: "HIC.2.b", hospital_name?: "HMP Foundation" }
// Output: a .docx file (binary), or JSON error.

import { createClient } from "https://esm.sh/@supabase/supabase-js@2";
import { buildPolicyDocument, documentToBuffer } from "../_shared/policy-doc-template.ts";

const CORS = {
  "Access-Control-Allow-Origin": "https://accredready.in",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};

const CONTENT_SYSTEM_PROMPT = `You write original hospital policy documents based ONLY on the NABH SHCO Full
requirement data provided. This will become an official document a real hospital
uses and may show to NABH assessors, so accuracy and honesty matter more than
completeness-sounding prose.

Critical rules:
1. Write in your OWN original words — never copy phrasing from any NABH document.
   You are given the underlying requirement (OE text, achieve tips, committee info);
   express it as clear, actionable hospital policy language.
2. Use the actual hospital name provided (not "the organisation" or "the hospital")
   naturally throughout the Purpose, Scope, Policy Statement, and Responsibility
   sections — real hospital policy documents name the facility repeatedly, not once.
3. If the source data does not specify a detail (exact frequency, named role,
   specific number), write "[Hospital to define — not specified in NABH SHCO 3rd
   Edition]" in that spot. NEVER invent a plausible-sounding specific.
4. If committee info is provided and includes "AccredReady recommended practice"
   content, you may use it but must phrase it as a suggested/example practice, not
   as an official NABH requirement.
5. Output ONLY valid JSON, no other text, matching exactly this shape:
{
  "purpose": "string",
  "scope": "string",
  "policyStatement": "string",
  "procedureSteps": ["string", "string", ...],
  "responsibility": "string",
  "references": "string",
  "distribution": "string"
}`;

Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: CORS });

  try {
    const { oe_code, hospital_name } = await req.json();
    if (!oe_code || typeof oe_code !== "string") {
      return Response.json({ error: "Missing oe_code" }, { status: 400, headers: CORS });
    }

    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
    const anthropicKey = Deno.env.get("ANTHROPIC_API_KEY");
    if (!supabaseUrl) throw new Error("SUPABASE_URL missing");
    if (!serviceKey) throw new Error("SUPABASE_SERVICE_ROLE_KEY missing");
    if (!anthropicKey) throw new Error("ANTHROPIC_API_KEY missing");

    const supabase = createClient(supabaseUrl, serviceKey);

    // --- Fetch the OE ---
    const { data: oeRows, error: oeErr } = await supabase
      .from("shco_full_oes")
      .select("oe_code, chapter, standard_code, level, text, achieve_tips, doc_required, interpretation")
      .eq("oe_code", oe_code)
      .limit(1);
    if (oeErr) throw new Error(`OE fetch: ${oeErr.message}`);
    if (!oeRows || oeRows.length === 0) {
      return Response.json({ error: `No OE found for ${oe_code}` }, { status: 404, headers: CORS });
    }
    const oe = oeRows[0];

    if (oe.doc_required !== true) {
      return Response.json(
        { error: `${oe_code} is not flagged as mandatory documentation (doc_required). Refusing to generate — this endpoint is only for mandatory-doc OEs.` },
        { status: 400, headers: CORS },
      );
    }

    // --- Fetch linked committee, if any (same mechanism as Gennie's Step 5.5) ---
    const { data: committeeRows } = await supabase
      .from("shco_kb")
      .select("title, content, source_label")
      .eq("category", "committees")
      .contains("linked_oe_codes", [oe_code]);
    const committeeInfo = committeeRows && committeeRows.length > 0
      ? committeeRows.map((r) => `${r.title}: ${r.content}`).join("\n")
      : "No specific committee linked to this OE.";

    // --- Ask Claude to write original content ---
    const userMessage = `Hospital Name: ${hospital_name || "[HOSPITAL NAME]"}

OE Code: ${oe.oe_code}
Level: ${oe.level}
Chapter: ${oe.chapter}
OE Requirement Text: ${oe.text}
Achieve Tips (practical guidance from NABH book): ${Array.isArray(oe.achieve_tips) ? oe.achieve_tips.join(" | ") : "none"}
Official Interpretation: ${oe.interpretation ?? "none provided"}
Linked Committee Info: ${committeeInfo}

Write the policy document content JSON now.`;

    const anthropicRes = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": anthropicKey.trim(),
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({
        model: "claude-sonnet-4-6",
        max_tokens: 2500,
        system: CONTENT_SYSTEM_PROMPT,
        messages: [{ role: "user", content: userMessage }],
      }),
    });
    if (!anthropicRes.ok) {
      const body = await anthropicRes.text();
      throw new Error(`Anthropic API error: ${anthropicRes.status} — ${body}`);
    }
    const anthropicData = await anthropicRes.json();
    const rawText = anthropicData.content?.[0]?.text ?? "{}";

    let content: {
      purpose: string; scope: string; policyStatement: string;
      procedureSteps: string[]; responsibility: string; references: string; distribution: string;
    };
    try {
      // Strip accidental markdown fences before parsing
      const cleaned = rawText.replace(/```json|```/g, "").trim();
      content = JSON.parse(cleaned);
    } catch {
      throw new Error(`Failed to parse AI content as JSON: ${rawText.slice(0, 300)}`);
    }

    // --- Build the docx ---
    const docTitle = `${oe.chapter} Policy — ${oe.oe_code}`;
    const hospitalPrefix = (hospital_name?.match(/^\S+/)?.[0] ?? "HOSP").toUpperCase();
    const oeSuffix = oe.oe_code.split(".").slice(1).join(""); // "MOM.2.b" -> "2b"
    const docNo = `${hospitalPrefix}/${oe.chapter}/POL-${oeSuffix}`;

    const doc = buildPolicyDocument({
      hospitalName: hospital_name || "[HOSPITAL NAME]",
      docNo,
      docTitle,
      oeCode: oe.oe_code,
      oeLevel: oe.level,
      chapterName: oe.chapter,
      purpose: content.purpose,
      scope: content.scope,
      policyStatement: content.policyStatement,
      procedureSteps: content.procedureSteps,
      responsibility: content.responsibility,
      references: `NABH SHCO 3rd Edition (August 2022) — ${oe.oe_code}. ${content.references ?? ""}`.trim(),
      distribution: content.distribution,
    });

    const buffer = await documentToBuffer(doc);

    return new Response(buffer, {
      headers: {
        ...CORS,
        "Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "Content-Disposition": `attachment; filename="${oe.oe_code}_policy.docx"`,
      },
    });
  } catch (err) {
    console.error(err);
    return Response.json({ error: (err as Error).message }, { status: 500, headers: CORS });
  }
});
