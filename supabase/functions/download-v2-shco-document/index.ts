// SHCO Full v2 SOP/Record document delivery.
// Fetches a pre-built .docx from Storage, replaces «Hospital Name»
// with the hospital's name, streams it back.
// Mirrors download-v2-hco-document (the HCO generalised function), scoped
// to SHCO's shco_documents table / shco-sop-record-v2 bucket. SHCO policy
// masters are unaffected — those remain on download-v2-policy /
// shco_policy_masters / policy-masters-v2.
//
// Input: { document_id: "<uuid>", hospital_name: "HMP Foundation" }
//    or: { document_id: "<uuid>", hospital_id: "<uuid>" }  (name looked up)
//
// document_type can be 'sop' or 'record' — both can have more than one row
// per standard, so document_id is always required (no standard_code lookup
// shortcut, unlike download-v2-policy's single-policy-per-standard case).
//
// PAYWALL: AAC-chapter documents are free for every signed-in hospital.
// Every other chapter requires hospitals.plan = 'paid'. The plan check is
// derived server-side from the caller's own JWT (profiles -> hospital_id),
// never from a client-supplied hospital_id/hospital_name — those remain
// for display/personalisation only and cannot be used to bypass the gate.
//
// TRACKING: every successful download is logged to document_downloads
// (programme='shco') so usage is visible. Logging failures never block
// the download itself; they're just console.error'd.

import { createClient } from "https://esm.sh/@supabase/supabase-js@2";
import { personalizeDocx } from "../_shared/personalize-docx.ts";

const BUCKET = "shco-sop-record-v2";
const FREE_CHAPTER = "AAC";

const PROD_ORIGIN = "https://accredready.in";
const ALLOWED_ORIGINS = [
  PROD_ORIGIN,
  "http://localhost:3000", // CRA dev server, for local testing
];

function corsFor(req: Request): Record<string, string> {
  const origin = req.headers.get("Origin") ?? "";
  return {
    "Access-Control-Allow-Origin": ALLOWED_ORIGINS.includes(origin) ? origin : PROD_ORIGIN,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization, apikey",
    "Vary": "Origin",
  };
}

Deno.serve(async (req: Request) => {
  const CORS = corsFor(req);

  if (req.method === "OPTIONS") return new Response(null, { headers: CORS });

  try {
    const body = await req.json();
    const document_id: string | undefined = body?.document_id;
    let hospital_name: string | undefined = body?.hospital_name;
    const hospital_id: string | undefined = body?.hospital_id;

    if (!document_id) {
      return Response.json({ error: "Missing document_id" }, { status: 400, headers: CORS });
    }

    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
    if (!supabaseUrl) throw new Error("SUPABASE_URL missing");
    if (!serviceKey) throw new Error("SUPABASE_SERVICE_ROLE_KEY missing");

    const supabase = createClient(supabaseUrl, serviceKey);

    if (!hospital_name && hospital_id) {
      const { data: hosp, error: hospErr } = await supabase
        .from("hospitals")
        .select("name")
        .eq("id", hospital_id)
        .maybeSingle();
      if (hospErr) throw new Error(`Hospital lookup: ${hospErr.message}`);
      if (!hosp?.name) {
        return Response.json({ error: `No hospital found for id ${hospital_id}` }, { status: 404, headers: CORS });
      }
      hospital_name = hosp.name;
    }

    if (!hospital_name || typeof hospital_name !== "string") {
      return Response.json(
        { error: "Missing hospital_name (or hospital_id to look it up)" },
        { status: 400, headers: CORS },
      );
    }

    const { data: doc, error: docErr } = await supabase
      .from("shco_documents")
      .select("id, standard_code, document_type, title, storage_path")
      .eq("id", document_id)
      .maybeSingle();
    if (docErr) throw new Error(`Document fetch: ${docErr.message}`);
    if (!doc) {
      return Response.json({ error: `No document found for id ${document_id}.` }, { status: 404, headers: CORS });
    }

    // ── Paywall ───────────────────────────────────────────────────────────
    const chapter = doc.standard_code.split(".")[0];
    let callerHospitalId: string | null = null;
    if (chapter !== FREE_CHAPTER) {
      const authHeader = req.headers.get("Authorization");
      const jwt = authHeader?.replace(/^Bearer\s+/i, "");
      if (!jwt) {
        return Response.json(
          { error: "Sign in required to download this document." },
          { status: 401, headers: CORS },
        );
      }

      const { data: userData, error: userErr } = await supabase.auth.getUser(jwt);
      if (userErr || !userData?.user) {
        return Response.json(
          { error: "Your session has expired — sign in again." },
          { status: 401, headers: CORS },
        );
      }

      const { data: profile, error: profileErr } = await supabase
        .from("profiles")
        .select("hospital_id")
        .eq("id", userData.user.id)
        .maybeSingle();
      if (profileErr) throw new Error(`Profile lookup: ${profileErr.message}`);

      let planOk = false;
      if (profile?.hospital_id) {
        callerHospitalId = profile.hospital_id;
        const { data: hospRow, error: hospPlanErr } = await supabase
          .from("hospitals")
          .select("plan")
          .eq("id", profile.hospital_id)
          .maybeSingle();
        if (hospPlanErr) throw new Error(`Plan lookup: ${hospPlanErr.message}`);
        planOk = hospRow?.plan === "paid";
      }

      if (!planOk) {
        return Response.json(
          {
            error: `${chapter} documents need a paid plan. ${FREE_CHAPTER} chapter documents are free to try — upgrade to unlock the rest.`,
            upgrade_required: true,
          },
          { status: 402, headers: CORS },
        );
      }
    } else {
      const authHeader = req.headers.get("Authorization");
      const jwt = authHeader?.replace(/^Bearer\s+/i, "");
      if (jwt) {
        const { data: userData } = await supabase.auth.getUser(jwt);
        if (userData?.user) {
          const { data: profile } = await supabase
            .from("profiles")
            .select("hospital_id")
            .eq("id", userData.user.id)
            .maybeSingle();
          callerHospitalId = profile?.hospital_id ?? null;
        }
      }
    }
    // ─────────────────────────────────────────────────────────────────────

    const { data: blob, error: dlErr } = await supabase.storage
      .from(BUCKET)
      .download(doc.storage_path);
    if (dlErr || !blob) {
      throw new Error(`Storage download (${doc.storage_path}): ${dlErr?.message ?? "empty object"}`);
    }

    const masterBytes = new Uint8Array(await blob.arrayBuffer());
    const { bytes: personalised, replacements } = await personalizeDocx(masterBytes, hospital_name);

    if (replacements === 0 && doc.document_type !== "record") {
      return Response.json(
        { error: `${doc.document_type} ${doc.standard_code} had no «Hospital Name» placeholder — refusing to serve an unpersonalised document.` },
        { status: 500, headers: CORS },
      );
    }

    // Log the download — best-effort, never blocks or fails the response.
    try {
      await supabase.from("document_downloads").insert({
        hospital_id: callerHospitalId,
        hospital_name,
        programme: "shco",
        standard_code: doc.standard_code,
        document_type: doc.document_type,
        document_id: doc.id,
      });
    } catch (logErr) {
      console.error("document_downloads insert failed:", logErr);
    }

    const safeTitle = String(doc.title ?? doc.standard_code)
      .replace(/[^a-zA-Z0-9\s-]/g, "")
      .replace(/\s+/g, "_");

    return new Response(personalised, {
      headers: {
        ...CORS,
        "Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "Content-Disposition": `attachment; filename="${doc.standard_code}_${safeTitle}.docx"`,
      },
    });
  } catch (err) {
    console.error(err);
    return Response.json({ error: (err as Error).message }, { status: 500, headers: CORS });
  }
});
