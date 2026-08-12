// PHASE B — Hospital personalization (repeated, per-hospital, per-download).
//
// CRITICAL DESIGN CHOICE: this function does NOT call any AI model. It fetches
// an APPROVED master document (see shco_policy_masters, status='approved',
// authored + human-reviewed via draft-master-policy) and does pure
// find-and-replace of {{HOSPITAL_NAME}} → the real hospital name, then builds
// the docx. There is no step here that can alter approved content — that's
// the entire point: content risk lives only in Phase A, reviewed once by a
// human, not repeated on every hospital's download.
//
// Refuses to run on anything not explicitly status='approved'.
//
// Input: { standard_code: "HIC.2", hospital_name: "HMP Foundation" }

import { createClient } from "https://esm.sh/@supabase/supabase-js@2";
import { buildPolicyDocument, documentToBuffer, type RevisionEntry } from "../_shared/policy-doc-template.ts";

const CORS = {
  "Access-Control-Allow-Origin": "https://accredready.in",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};

const substitute = (text: string, hospitalName: string): string =>
  text.replaceAll("{{HOSPITAL_NAME}}", hospitalName);

Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: CORS });

  try {
    const { standard_code, hospital_name } = await req.json();
    if (!standard_code || typeof standard_code !== "string") {
      return Response.json({ error: "Missing standard_code" }, { status: 400, headers: CORS });
    }
    if (!hospital_name || typeof hospital_name !== "string") {
      return Response.json({ error: "Missing hospital_name" }, { status: 400, headers: CORS });
    }

    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
    if (!supabaseUrl) throw new Error("SUPABASE_URL missing");
    if (!serviceKey) throw new Error("SUPABASE_SERVICE_ROLE_KEY missing");

    const supabase = createClient(supabaseUrl, serviceKey);

    // --- Fetch ONLY if approved. This check is the safety gate. ---
    const { data: masterRows, error: masterErr } = await supabase
      .from("shco_policy_masters")
      .select("*")
      .eq("standard_code", standard_code)
      .limit(1);
    if (masterErr) throw new Error(`Master fetch: ${masterErr.message}`);
    if (!masterRows || masterRows.length === 0) {
      return Response.json({ error: `No master document exists for standard ${standard_code}. Run draft-master-policy first, then approve it.` }, { status: 404, headers: CORS });
    }
    const master = masterRows[0];
    if (master.status !== "approved") {
      return Response.json(
        { error: `Master document for ${standard_code} has status '${master.status}', not 'approved'. Refusing to generate — review and approve it first (this is intentional: unapproved content must never reach a hospital).` },
        { status: 403, headers: CORS },
      );
    }

    // --- Pure substitution. No AI call. No content risk. ---
    const hospitalPrefix = (hospital_name.match(/^\S+/)?.[0] ?? "HOSP").toUpperCase();
    const docNo = `${hospitalPrefix}/${master.chapter}/POL-${master.standard_code.split(".").slice(1).join("")}`;

    const doc = buildPolicyDocument({
      hospitalName: hospital_name,
      docNo,
      docTitle: substitute(master.policy_title, hospital_name),
      oeCode: (master.oe_codes as string[]).join(", "),
      oeLevel: "", // multiple OEs, level varies — omitted at this granularity
      chapterName: master.chapter,
      abbreviations: master.abbreviations ? substitute(master.abbreviations, hospital_name) : undefined,
      definitions: master.definitions ? substitute(master.definitions, hospital_name) : undefined,
      oeMapping: Array.isArray(master.oe_mapping)
        ? (master.oe_mapping as { oe_code: string; requirement: string; steps: string; evidence?: string; responsible?: string }[]).map((m) => ({
            oeCode: m.oe_code,
            requirement: substitute(m.requirement, hospital_name),
            steps: m.steps,
            evidence: m.evidence ? substitute(m.evidence, hospital_name) : undefined,
            responsible: m.responsible ? substitute(m.responsible, hospital_name) : undefined,
          }))
        : undefined,
      purpose: substitute(master.purpose, hospital_name),
      scope: substitute(master.scope, hospital_name),
      policyStatement: substitute(master.policy_statement, hospital_name),
      procedureSteps: (master.procedure_steps as string[]).map((s) => substitute(s, hospital_name)),
      trainingCompetency: master.training_competency ? substitute(master.training_competency, hospital_name) : undefined,
      responsibility: substitute(master.responsibility, hospital_name),
      resourcesRequired: master.resources_required ? substitute(master.resources_required, hospital_name) : undefined,
      monitoringAudit: master.monitoring_audit ? substitute(master.monitoring_audit, hospital_name) : undefined,
      exceptions: master.exceptions ? substitute(master.exceptions, hospital_name) : undefined,
      references: substitute(master.references_text, hospital_name),
      distribution: substitute(master.distribution, hospital_name),
      disclaimer: master.disclaimer ? substitute(master.disclaimer, hospital_name) : undefined,
      version: master.version ?? "1.0",
      revisionHistory: master.revision_history as RevisionEntry[] | undefined,
    });

    const buffer = await documentToBuffer(doc);
    const safeTitleForFilename = substitute(master.policy_title, hospital_name)
      .replace(/[^a-zA-Z0-9\s-]/g, "")
      .replace(/\s+/g, "_");

    return new Response(buffer, {
      headers: {
        ...CORS,
        "Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "Content-Disposition": `attachment; filename="${master.standard_code}_${safeTitleForFilename}.docx"`,
      },
    });
  } catch (err) {
    console.error(err);
    return Response.json({ error: (err as Error).message }, { status: 500, headers: CORS });
  }
});
