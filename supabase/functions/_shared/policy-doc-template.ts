// Reusable NABH-format policy document builder.
// This is the FIXED FORMAT layer — the same structure every time.
// The content layer (fetched OE data + AI-generated prose) is passed in as `data`.
// Used by generate-policy-document/index.ts (Supabase Edge Function).

import {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, AlignmentType, ShadingType, Footer,
} from "npm:docx";

export interface PolicyDocData {
  hospitalName: string;
  docNo: string;
  docTitle: string;
  oeCode: string;
  oeLevel: string;
  chapterName: string;
  abbreviations?: string;
  purpose: string;
  scope: string;
  policyStatement: string;
  procedureSteps: string[];
  responsibility: string;
  references: string;
  distribution: string;
  disclaimer?: string;
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

// Procedure steps arrive as one fused string per step, e.g.:
//   "4. Choosing between alcohol-based handrub and soap and water\n\nAlcohol-based
//    handrub is the routine method... - hands are visibly dirty...\n- hands feel sticky..."
// Splitting the title from the body (and any "- " sub-list within the body) turns this
// from one dense wall of text into a scannable step: bold title, then body, then real
// bullet points for any embedded list — instead of everything mashed into one bullet.
const renderProcedureStep = (text: string): Paragraph[] => {
  const titleMatch = text.match(/^(\d+\.\s[^\n]+)\n\n([\s\S]*)$/);
  if (!titleMatch) {
    // No recognizable "N. Title\n\nBody" shape — render as-is rather than guess.
    return [new Paragraph({ children: [new TextRun({ text, size: 22 })], spacing: { after: 200 } })];
  }
  const [, title, rest] = titleMatch;
  const paragraphs: Paragraph[] = [
    new Paragraph({ children: [new TextRun({ text: title, bold: true, size: 23 })], spacing: { before: 240, after: 90 } }),
  ];

  const blocks = rest.split(/\n\n+/);
  for (const block of blocks) {
    const trimmed = block.trim();
    if (!trimmed) continue;
    if (/^- /.test(trimmed) || trimmed.includes("\n- ")) {
      const lines = trimmed.split(/\n(?=- )/).map((l) => l.trim()).filter(Boolean);
      for (const line of lines) {
        const cleaned = line.replace(/^- /, "");
        paragraphs.push(
          new Paragraph({ children: [new TextRun({ text: cleaned, size: 22 })], bullet: { level: 0 }, spacing: { after: 60 } }),
        );
      }
    } else {
      paragraphs.push(new Paragraph({ children: [new TextRun({ text: trimmed, size: 22 })], spacing: { after: 120 } }));
    }
  }
  return paragraphs;
};

export function buildPolicyDocument(data: PolicyDocData): Document {
  const today = new Date().toLocaleDateString("en-GB").replace(/\//g, "-");

  const controlTable = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({ children: [cell("Document No.", { bold: true, shade: true }), cell(data.docNo), cell("Version", { bold: true, shade: true }), cell("1.0")] }),
      new TableRow({ children: [cell("Effective Date", { bold: true, shade: true }), cell("[DD-MM-YYYY]"), cell("Review Date", { bold: true, shade: true }), cell("[DD-MM-YYYY]")] }),
      new TableRow({ children: [cell("Applicable OE(s)", { bold: true, shade: true }), cell(data.oeLevel ? `${data.oeCode} (${data.oeLevel})` : data.oeCode), cell("NABH Chapter", { bold: true, shade: true }), cell(data.chapterName)] }),
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
        footers: {
          default: new Footer({
            children: [
              new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [
                  new TextRun({ text: `${data.hospitalName}  |  ${data.docNo}  |  Confidential — Controlled Document`, size: 16, italics: true }),
                ],
              }),
            ],
          }),
        },
        children: [
          new Paragraph({ children: [new TextRun({ text: data.hospitalName, bold: true, size: 32 })], alignment: AlignmentType.CENTER, spacing: { after: 60 } }),
          new Paragraph({ children: [new TextRun({ text: data.docTitle, bold: true, size: 28 })], alignment: AlignmentType.CENTER, spacing: { after: 60 } }),
          new Paragraph({
            children: [new TextRun({ text: `(Mandatory System Documentation as per NABH SHCO 3rd Edition — ${data.oeCode})`, italics: true, size: 20 })],
            alignment: AlignmentType.CENTER,
            spacing: { after: 300 },
          }),
          controlTable,
          ...(data.abbreviations
            ? [heading("Abbreviations"), body(data.abbreviations)]
            : []),
          heading("1. Purpose"),
          body(data.purpose),
          heading("2. Scope"),
          body(data.scope),
          heading("3. Policy Statement"),
          body(data.policyStatement),
          heading("4. Procedure"),
          ...data.procedureSteps.flatMap(renderProcedureStep),
          heading("5. Responsibility"),
          body(data.responsibility),
          heading("6. References"),
          body(data.references),
          heading("7. Distribution"),
          body(data.distribution),
          heading("8. Revision History"),
          revisionHistory,
          ...(data.disclaimer
            ? [heading("Disclaimer"), body(data.disclaimer)]
            : []),
        ],
      },
    ],
  });
}

export async function documentToBuffer(doc: Document): Promise<Uint8Array> {
  const buf = await Packer.toBuffer(doc);
  return new Uint8Array(buf);
}
