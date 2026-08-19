// Local stand-in for download-v2-policy — reads masters from policies/build/masters/.
// Usage: deno run --allow-read --allow-net policies/build/serve_v2_download_local.ts

import { personalizeDocx } from "../../supabase/functions/_shared/personalize-docx.ts";

const REPO = new URL("../../", import.meta.url);
const MASTERS = new URL("policies/build/masters/", REPO);
const PORT = Number(Deno.env.get("PORT") ?? "8765");

Deno.serve({ port: PORT }, async (req) => {
  if (req.method !== "POST") {
    return new Response("POST { standard_code, hospital_name }", { status: 405 });
  }
  try {
    const { standard_code, hospital_name } = await req.json();
    if (!standard_code || !hospital_name) {
      return Response.json({ error: "Missing standard_code or hospital_name" }, { status: 400 });
    }
    const path = new URL(`${standard_code}_v2_master.docx`, MASTERS);
    const masterBytes = await Deno.readFile(path);
    const out = await personalizeDocx(masterBytes, hospital_name);
    return new Response(out, {
      headers: {
        "Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "Content-Disposition": `attachment; filename="${standard_code}_local.docx"`,
      },
    });
  } catch (err) {
    return Response.json({ error: (err as Error).message }, { status: 500 });
  }
});

console.log(`local download-v2-policy on http://127.0.0.1:${PORT}/`);
