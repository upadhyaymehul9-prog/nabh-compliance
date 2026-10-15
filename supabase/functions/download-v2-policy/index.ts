// v2 policy delivery (SHCO) — fetch pre-rendered master .docx from Storage,
// replace «Hospital Name» with the hospital's name, stream back.
// Does not call AI. Does not rebuild from database fields.
// v1 generate-hospital-policy and database-rendered masters are untouched.
//
// Input: { standard_code: "FMS.4", hospital_name: "HMP Foundation" }
//    or: { standard_code: "FMS.4", hospital_id: "<uuid>" }  (name looked up)
//
// PAYWALL: AAC-chapter documents are free for every signed-in hospital.
// Every other chapter requires hospitals.plan = 'paid'. The plan check is
// derived server-side from the caller's own JWT (profiles -> hospital_id),
// never from a client-supplied hospital_id/hospital_name — those remain
// for display/personalisation only and cannot be used to bypass the gate.
//
// TRACKING: every successful download is logged to document_downloads
// (programme='shco') so we can see real usage. Logging failures never
// block the download itself; they're just console.error'd.

import { createClient } from "https://esm.sh/@supabase/supabase-js@2";
import { personalizeDocx } from "../_shared/personalize-docx.ts";

const BUCKET = "policy-masters-v2";
const FREE_CHAPTER = "AAC";

const PROD_ORIGIN = "https://accredready.in";
const ALLOWED_ORIGINS = [
  PROD_ORIGIN,
  "http://localhost:3000", // CRA dev server, for local testing
];

// Must be computed per-request: the allowed origin echoes back the caller's own
// Origin header. Unknown origins fall back to production, which the browser then
// rejects — the header is never wildcarded.
function corsFor(req: Request): Record<string, string> {
  const origin = req.headers.get("Origin") ?? "";
  return {
    "Access-Control-Allow-Origin": ALLOWED_ORIGINS.includes(origin) ? origin : PROD_ORIGIN,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization, apikey",
    // response differs per Origin, so caches and proxies must key on it
    "Vary": "Origin",
  };
}

Deno.serve(async (req: Request) => {
  const CORS = corsFor(req);

  if (req.method === "OPTIONS") return new Response(null, { headers: CORS });

  try {
    const body = await req.json();
    const standard_code = body?.standard_code;
    let hospital_name: string | undefined = body?.hospital_name;
    const hospital_id: string | undefined = body?.hospital_id;

    if (!standard_code || typeof standard_code !== "string") {
      return Response.json({ error: "Missing standard_code" }, { status: 400, headers: CORS });
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

    // ── Paywall ───────────────────────────────────────────────────────────
    const chapter = standard_code.split(".")[0];
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

    const { data: masterRows, error: masterErr } = await supabase
      .from("shco_policy_masters")
      .select("standard_code, policy_title, master_docx_path")
      .eq("standard_code", standard_code)
      .limit(1);

    if (masterErr) throw new Error(`Master fetch: ${masterErr.message}`);
    if (!masterRows?.length) {
      return Response.json(
        { error: `No master document exists for standard ${standard_code}.` },
        { status: 404, headers: CORS },
      );
    }

    const master = masterRows[0];
    const storagePath = master.master_docx_path as string | null;
    if (!storagePath) {
      return Response.json(
        {
          error: `Master for ${standard_code} has no master_docx_path — v2 storage delivery is not configured. Use generate-hospital-policy for v1 database-rendered masters.`,
        },
        { status: 404, headers: CORS },
      );
    }

    const { data: blob, error: dlErr } = await supabase.storage
      .from(BUCKET)
      .download(storagePath);
    if (dlErr || !blob) {
      throw new Error(`Storage download (${storagePath}): ${dlErr?.message ?? "empty object"}`);
    }

    const masterBytes = new Uint8Array(await blob.arrayBuffer());
    const { bytes: personalised, replacements } = await personalizeDocx(masterBytes, hospital_name);
    if (replacements === 0) {
      return Response.json(
        { error: `Master ${standard_code} had no «Hospital Name» placeholder — refusing to serve an unpersonalised document.` },
        { status: 500, headers: CORS },
      );
    }

    // Log the download — best-effort, never blocks or fails the response.
    try {
      await supabase.from("document_downloads").insert({
        hospital_id: callerHospitalId,
        hospital_name,
        programme: "shco",
        standard_code,
        document_type: "policy",
        document_id: null,
      });
    } catch (logErr) {
      console.error("document_downloads insert failed:", logErr);
    }

    const safeTitle = String(master.policy_title ?? standard_code)
      .replace(/[^a-zA-Z0-9\s-]/g, "")
      .replace(/\s+/g, "_");

    return new Response(personalised, {
      headers: {
        ...CORS,
        "Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "Content-Disposition": `attachment; filename="${standard_code}_${safeTitle}.docx"`,
      },
    });
  } catch (err) {
    console.error(err);
    return Response.json({ error: (err as Error).message }, { status: 500, headers: CORS });
  }
});
