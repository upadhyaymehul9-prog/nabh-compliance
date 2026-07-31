// Reusable NABH-format policy document builder.
// This is the FIXED FORMAT layer — the same structure every time.
// The content layer (fetched OE data + AI-generated prose) is passed in as `data`.
// Used by generate-policy-document/index.ts (Supabase Edge Function).

import {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, AlignmentType, ShadingType,
} from "docx";

export interface PolicyDocData {
  hospitalName: string;
  docNo: string;
  docTitle: string;
  oeCode: string;
  oeLevel: string;
  chapterName: string;
  purpose: string;
  scope: string;
  policyStatement: string;
  procedureSteps: string[];
  responsibility: string;
  references: string;
  distribution: string;
}

const cell = (text: string, opts: { bold?: boolean; shade?: boolean; width?: number } = {}) =>
  new TableCell({
    width: { size: opts.width ?? 25, type: WidthType.PERCENTAGE },
    shading: opts.shade ? { type: ShadingType.CLEAR, fill: "E8E8E8" } : undefined,
    children: [new Paragraph({ children: [new TextRun({ text, bold: opts.bold ?? false, size: 18 })] })],
  });

const heading = (text: string) =>
  new Paragraph({ text, heading: HeadingLevel.HEADING_1, spacing: { before: 300, after: 150 } });
const body = (text: string) =>
  new Paragraph({ children: [new TextRun({ text, size: 22 })], spacing: { after: 150 } });
const bullet = (text: string) =>
  new Paragraph({ children: [new TextRun({ text, size: 22 })], bullet: { level: 0 }, spacing: { after: 80 } });

export function buildPolicyDocument(data: PolicyDocData): Document {
  const today = new Date().toLocaleDateString("en-GB").replace(/\//g, "-");

  const controlTable = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({ children: [cell("Document No.", { bold: true, shade: true }), cell(data.docNo), cell("Version", { bold: true, shade: true }), cell("1.0")] }),
      new TableRow({ children: [cell("Effective Date", { bold: true, shade: true }), cell("[DD-MM-YYYY]"), cell("Review Date", { bold: true, shade: true }), cell("[DD-MM-YYYY]")] }),
      new TableRow({ children: [cell("Applicable OE", { bold: true, shade: true }), cell(`${data.oeCode} (${data.oeLevel})`), cell("NABH Chapter", { bold: true, shade: true }), cell(data.chapterName)] }),
      new TableRow({ children: [cell("Prepared By", { bold: true, shade: true }), cell("_________________"), cell("Date", { bold: true, shade: true }), cell("________")] }),
      new TableRow({ children: [cell("Reviewed By", { bold: true, shade: true }), cell("_________________"), cell("Date", { bold: true, shade: true }), cell("________")] }),
      new TableRow({ children: [cell("Approved By", { bold: true, shade: true }), cell("_________________"), cell("Date", { bold: true, shade: true }), cell("________")] }),
    ],
  });

  const revisionHistory = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({ children: [cell("Version", { bold: true, shade: true }), cell("Date", { bold: true, shade: true }), cell("Description of Change", { bold: true, shade: true, width: 50 })] }),
      new TableRow({ children: [cell("1.0"), cell(today), cell("Initial release (AI-generated draft — review before use)", { width: 50 })] }),
    ],
  });

  return new Document({
    sections: [
      {
        properties: { page: { size: { width: 11906, height: 16838 } } }, // A4
        children: [
          new Paragraph({ children: [new TextRun({ text: data.hospitalName, bold: true, size: 32 })], alignment: AlignmentType.CENTER, spacing: { after: 60 } }),
          new Paragraph({ children: [new TextRun({ text: data.docTitle, bold: true, size: 28 })], alignment: AlignmentType.CENTER, spacing: { after: 60 } }),
          new Paragraph({
            children: [new TextRun({ text: `(Mandatory System Documentation as per NABH SHCO 3rd Edition — ${data.oeCode})`, italics: true, size: 20 })],
            alignment: AlignmentType.CENTER,
            spacing: { after: 300 },
          }),
          controlTable,
          heading("1. Purpose"),
          body(data.purpose),
          heading("2. Scope"),
          body(data.scope),
          heading("3. Policy Statement"),
          body(data.policyStatement),
          heading("4. Procedure"),
          ...data.procedureSteps.map(bullet),
          heading("5. Responsibility"),
          body(data.responsibility),
          heading("6. References"),
          body(data.references),
          heading("7. Distribution"),
          body(data.distribution),
          heading("8. Revision History"),
          revisionHistory,
        ],
      },
    ],
  });
}

export async function documentToBuffer(doc: Document): Promise<Uint8Array> {
  const buf = await Packer.toBuffer(doc);
  return new Uint8Array(buf);
}
