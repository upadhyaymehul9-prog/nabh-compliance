// Replace hospital placeholders inside a .docx (zip of XML parts).
// Masters use «Hospital Name»; legacy JSON fields may still carry {{HOSPITAL_NAME}}.

import JSZip from "npm:jszip@3.10.1";

export const V2_HOSPITAL_PLACEHOLDER = "«Hospital Name»";
export const V1_HOSPITAL_PLACEHOLDER = "{{HOSPITAL_NAME}}";

const XML_PART = /\.(xml|rels)$/i;

// The name lands in XML text nodes, so any XML metacharacter in it
// (& < > and, defensively, quotes) would corrupt the document.
function escapeXml(s: string): string {
  return s
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&apos;");
}

export function substituteHospitalName(
  text: string,
  hospitalName: string,
): { xml: string; count: number } {
  const safe = escapeXml(hospitalName);
  let count = 0;
  const xml = text
    .replaceAll(V2_HOSPITAL_PLACEHOLDER, () => { count++; return safe; })
    .replaceAll(V1_HOSPITAL_PLACEHOLDER, () => { count++; return safe; });
  return { xml, count };
}

/** Personalise every XML/rels part; returns bytes + total replacement count. */
export async function personalizeDocx(
  docxBytes: Uint8Array,
  hospitalName: string,
): Promise<{ bytes: Uint8Array; replacements: number }> {
  const zip = await JSZip.loadAsync(docxBytes);
  let total = 0;

  for (const path of Object.keys(zip.files)) {
    const entry = zip.files[path];
    if (!entry || entry.dir || !XML_PART.test(path)) continue;
    const { xml, count } = substituteHospitalName(await entry.async("string"), hospitalName);
    if (count > 0) zip.file(path, xml);
    total += count;
  }

  const bytes = new Uint8Array(await zip.generateAsync({ type: "uint8array", compression: "DEFLATE" }));
  return { bytes, replacements: total };
}
