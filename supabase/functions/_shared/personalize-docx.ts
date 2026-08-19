// Replace hospital placeholders inside a .docx (zip of XML parts).
// Masters use «Hospital Name»; legacy JSON fields may still carry {{HOSPITAL_NAME}}.

import JSZip from "npm:jszip@3.10.1";

export const V2_HOSPITAL_PLACEHOLDER = "«Hospital Name»";
export const V1_HOSPITAL_PLACEHOLDER = "{{HOSPITAL_NAME}}";

const XML_PART = /\.(xml|rels)$/i;

export function substituteHospitalName(text: string, hospitalName: string): string {
  return text
    .replaceAll(V2_HOSPITAL_PLACEHOLDER, hospitalName)
    .replaceAll(V1_HOSPITAL_PLACEHOLDER, hospitalName);
}

/** Personalise every XML/rels part in the docx buffer. */
export async function personalizeDocx(
  docxBytes: Uint8Array,
  hospitalName: string,
): Promise<Uint8Array> {
  const zip = await JSZip.loadAsync(docxBytes);
  const paths = Object.keys(zip.files);

  for (const path of paths) {
    const entry = zip.files[path];
    if (!entry || entry.dir || !XML_PART.test(path)) continue;
    const xml = await entry.async("string");
    zip.file(path, substituteHospitalName(xml, hospitalName));
  }

  return new Uint8Array(await zip.generateAsync({
    type: "uint8array",
    compression: "DEFLATE",
  }));
}
