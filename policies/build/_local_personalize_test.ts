// Local harness: same personalizeDocx as download-v2-policy edge function.
// Usage: deno run --allow-read --allow-write policies/build/_local_personalize_test.ts <in.docx> <hospital> <out.docx>

import { personalizeDocx } from "../../supabase/functions/_shared/personalize-docx.ts";

const [inPath, hospitalName, outPath] = Deno.args;
if (!inPath || !hospitalName || !outPath) {
  console.error("usage: _local_personalize_test.ts <in.docx> <hospital-name> <out.docx>");
  Deno.exit(1);
}

const masterBytes = await Deno.readFile(inPath);
const out = await personalizeDocx(masterBytes, hospitalName);
await Deno.writeFile(outPath, out);
console.log(`wrote ${outPath} (${out.byteLength} bytes)`);
