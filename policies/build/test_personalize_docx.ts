import { assertEquals } from "jsr:@std/assert@1";
import { personalizeDocx, substituteHospitalName, V2_HOSPITAL_PLACEHOLDER } from "../../supabase/functions/_shared/personalize-docx.ts";

Deno.test("substituteHospitalName replaces v2 placeholder", () => {
  const out = substituteHospitalName(`Policy of ${V2_HOSPITAL_PLACEHOLDER} applies.`, "HMP Foundation");
  assertEquals(out, "Policy of HMP Foundation applies.");
});

Deno.test("personalizeDocx on FMS.4 master", async () => {
  const masterPath = new URL("./masters/FMS.4_v2_master.docx", import.meta.url);
  const bytes = await Deno.readFile(masterPath);
  const out = await personalizeDocx(bytes, "HMP Foundation");
  const { default: JSZip } = await import("npm:jszip@3.10.1");
  const zip = await JSZip.loadAsync(out);
  const xml = await zip.file("word/document.xml")!.async("string");
  assertEquals(xml.includes("HMP Foundation"), true);
  assertEquals(xml.includes(V2_HOSPITAL_PLACEHOLDER), false);
});
