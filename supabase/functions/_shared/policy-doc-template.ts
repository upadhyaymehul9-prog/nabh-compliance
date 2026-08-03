// Reusable NABH-format policy document builder.
// This is the FIXED FORMAT layer — the same structure every time.
// The content layer (fetched OE data + AI-generated prose) is passed in as `data`.
// Used by generate-policy-document/index.ts (Supabase Edge Function).

import {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, AlignmentType, ShadingType, Footer,
} from "npm:docx";

export interface OeMappingEntry {
  oeCode: string;
  requirement: string;
  steps: string;
  evidence?: string;
  responsible?: string;
}

export interface PolicyDocData {
  hospitalName: string;
  docNo: string;
  docTitle: string;
  oeCode: string;
  oeLevel: string;
  chapterName: string;
  abbreviations?: string;
  oeMapping?: OeMappingEntry[];
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

// Parses an oe_mapping "steps" string like "Step 2, Steps 10-14" or
// "Steps 1, 4-11 and 26" into the set of step numbers it refers to.
// Tolerates "Step"/"Steps", comma-separated lists, ranges, and "and" used
// before the final item in the list (a natural way to write it, but one
// that silently dropped the last number until this normalization — e.g.
// "Steps 1, 4-11 and 26" previously lost step 26's inline OE annotation
// even though the OE Cross-Reference table's plain-text "Addressed In"
// column always showed it correctly).
const parseStepNumbers = (stepsStr: string): number[] => {
  const numbers: number[] = [];
  const normalized = stepsStr.replace(/\s+and\s+/gi, ", ");
  const parts = normalized.split(",");
  for (const part of parts) {
    const rangeMatch = part.match(/(\d+)\s*-\s*(\d+)/);
    if (rangeMatch) {
      const start = parseInt(rangeMatch[1], 10);
      const end = parseInt(rangeMatch[2], 10);
      for (let n = start; n <= end; n++) numbers.push(n);
      continue;
    }
    const singleMatch = part.match(/(\d+)/);
    if (singleMatch) numbers.push(parseInt(singleMatch[1], 10));
  }
  return numbers;
};

// Builds a lookup from step number -> OE code(s), so each step's title can be
// annotated directly (e.g. "2. Standard precautions... (HIC.2.a)") instead of
// requiring the reader to cross-reference a separate table to know which OE a
// given step actually answers.
const buildStepToOeLookup = (oeMapping?: OeMappingEntry[]): Map<number, string[]> => {
  const lookup = new Map<number, string[]>();
  if (!oeMapping) return lookup;
  for (const entry of oeMapping) {
    const stepNumbers = parseStepNumbers(entry.steps);
    for (const n of stepNumbers) {
      const existing = lookup.get(n) ?? [];
      existing.push(entry.oeCode);
      lookup.set(n, existing);
    }
  }
  return lookup;
};

// Procedure steps arrive as one fused string per step, e.g.:
//   "4. Choosing between alcohol-based handrub and soap and water\n\nAlcohol-based
//    handrub is the routine method... - hands are visibly dirty...\n- hands feel sticky..."
// Splitting the title from the body (and any "- " sub-list within the body) turns this
// from one dense wall of text into a scannable step: bold title, then body, then real
// bullet points for any embedded list — instead of everything mashed into one bullet.
// stepToOeLookup, if provided, annotates the title with its OE code(s) directly,
// so a reader doesn't have to cross-reference the OE Cross-Reference table to know
// which requirement a given step actually answers.
const renderProcedureStep = (text: string, stepToOeLookup?: Map<number, string[]>): Paragraph[] => {
  // Normalize line endings first: content drafted via different tools (Claude
  // Code sessions vs. a Windows Python build script) can arrive with either
  // \n or \r\n. The title/body split below requires \n\n exactly — without
  // this normalization, \r\n\r\n content silently fails the regex and every
  // step falls through to one unformatted paragraph: no bold title, no real
  // bullets, no OE code annotation. This happened for real on HIC.1's first
  // generation and wasn't obvious until the actual document was inspected.
  const normalizedText = text.replace(/\r\n/g, "\n");
  const titleMatch = normalizedText.match(/^(\d+)\.\s([^\n]+)\n\n([\s\S]*)$/);
  if (!titleMatch) {
    // No recognizable "N. Title\n\nBody" shape — render as-is rather than guess.
    return [new Paragraph({ children: [new TextRun({ text: normalizedText, size: 22 })], spacing: { after: 200 } })];
  }
  const [, stepNumStr, titleText, rest] = titleMatch;
  const stepNum = parseInt(stepNumStr, 10);
  const oeCodes = stepToOeLookup?.get(stepNum);
  const titleWithOe = oeCodes && oeCodes.length > 0
    ? `${stepNumStr}. ${titleText} (${oeCodes.join(", ")})`
    : `${stepNumStr}. ${titleText}`;

  const paragraphs: Paragraph[] = [
    new Paragraph({ children: [new TextRun({ text: titleWithOe, bold: true, size: 23 })], spacing: { before: 240, after: 90 } }),
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

// Abbreviations arrive as one string with one "ABBR — Meaning" entry per line,
// plus sometimes a trailing note (e.g. "Any additional abbreviation... is
// [Hospital to define]"). Splitting these into a real two-column table is far
// more scannable than one dense paragraph — a glossary is a lookup tool, not
// prose meant to be read start to finish.
const renderAbbreviations = (text: string): (Paragraph | Table)[] => {
  const normalizedText = text.replace(/\r\n/g, "\n");
  const lines = normalizedText.split("\n").map((l) => l.trim()).filter(Boolean);
  const rows: { abbr: string; meaning: string }[] = [];
  const otherLines: string[] = [];

  for (const line of lines) {
    const match = line.match(/^(.+?)\s+—\s+(.+)$/);
    if (match) {
      rows.push({ abbr: match[1].trim(), meaning: match[2].trim() });
    } else {
      otherLines.push(line);
    }
  }

  const result: (Paragraph | Table)[] = [];
  if (rows.length > 0) {
    result.push(
      new Table({
        width: { size: 100, type: WidthType.PERCENTAGE },
        rows: [
          new TableRow({
            children: [
              cell("Abbreviation", { bold: true, shade: true, width: 25 }),
              cell("Meaning", { bold: true, shade: true, width: 75 }),
            ],
          }),
          ...rows.map(
            (r) =>
              new TableRow({
                children: [cell(r.abbr, { width: 25 }), cell(r.meaning, { width: 75 })],
              }),
          ),
        ],
      }),
    );
  }
  for (const line of otherLines) {
    result.push(new Paragraph({ children: [new TextRun({ text: line, size: 22, italics: true })], spacing: { before: 120, after: 120 } }));
  }
  return result;
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

  const hasEvidenceData = data.oeMapping?.some((m) => m.evidence || m.responsible) ?? false;

  const oeMappingTable = data.oeMapping && data.oeMapping.length > 0
    ? new Table({
        width: { size: 100, type: WidthType.PERCENTAGE },
        rows: hasEvidenceData
          ? [
              new TableRow({
                children: [
                  cell("OE Code", { bold: true, shade: true, width: 12 }),
                  cell("Requirement", { bold: true, shade: true, width: 33 }),
                  cell("Addressed In", { bold: true, shade: true, width: 18 }),
                  cell("Evidence", { bold: true, shade: true, width: 22 }),
                  cell("Responsible", { bold: true, shade: true, width: 15 }),
                ],
              }),
              ...data.oeMapping.map(
                (m) =>
                  new TableRow({
                    children: [
                      cell(m.oeCode, { width: 12 }),
                      cell(m.requirement, { width: 33 }),
                      cell(m.steps, { width: 18 }),
                      cell(m.evidence ?? "—", { width: 22 }),
                      cell(m.responsible ?? "—", { width: 15 }),
                    ],
                  }),
              ),
            ]
          : [
              new TableRow({
                children: [
                  cell("OE Code", { bold: true, shade: true, width: 15 }),
                  cell("Requirement", { bold: true, shade: true, width: 55 }),
                  cell("Addressed In", { bold: true, shade: true, width: 30 }),
                ],
              }),
              ...data.oeMapping.map(
                (m) =>
                  new TableRow({
                    children: [
                      cell(m.oeCode, { width: 15 }),
                      cell(m.requirement, { width: 55 }),
                      cell(m.steps, { width: 30 }),
                    ],
                  }),
              ),
            ],
      })
    : null;

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
          ...(oeMappingTable
            ? [heading("OE Cross-Reference"), oeMappingTable]
            : []),
          ...(data.abbreviations
            ? [heading("Abbreviations"), ...renderAbbreviations(data.abbreviations)]
            : []),
          heading("1. Purpose"),
          body(data.purpose),
          heading("2. Scope"),
          body(data.scope),
          heading("3. Policy Statement"),
          body(data.policyStatement),
          heading("4. Procedure"),
          ...(() => {
            const stepToOeLookup = buildStepToOeLookup(data.oeMapping);
            return data.procedureSteps.flatMap((step) => renderProcedureStep(step, stepToOeLookup));
          })(),
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
