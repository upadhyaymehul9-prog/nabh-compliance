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
  // Full evidence detail. As of the Required Records change this is rendered ONLY
  // by the Required Records / Evidence Checklist section — it is deliberately no
  // longer a column in the OE Cross-Reference table, so the same list is never
  // printed twice in one document under two headings.
  evidence?: string;
  responsible?: string;
}

export interface RevisionEntry {
  version: string;
  date: string;
  description: string;
}

export interface PolicyDocData {
  hospitalName: string;
  docNo: string;
  docTitle: string;
  oeCode: string;
  oeLevel: string;
  chapterName: string;
  abbreviations?: string;
  definitions?: string;
  oeMapping?: OeMappingEntry[];
  purpose: string;
  scope: string;
  policyStatement: string;
  procedureSteps: string[];
  trainingCompetency?: string;
  responsibility: string;
  resourcesRequired?: string;
  monitoringAudit?: string;
  exceptions?: string;
  references: string;
  distribution: string;
  disclaimer?: string;
  // Document version as TEXT ("1.0", "1.1", "2.10") — semantic versions are not
  // numbers and must not be stored or sorted as such. Falls back to "1.0" so a
  // row that has not been backfilled still renders a sane document.
  version?: string;
  // Real revision history for this master. When absent, a single neutral row is
  // printed. The previous hardcoded "Initial release (AI-generated draft — review
  // before use)" is gone: it was false for every human-reviewed approved master.
  revisionHistory?: RevisionEntry[];
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

// Splits one oe_mapping evidence string into its individual records.
// The evidence fields are authored as semicolon-delimited lists (4-20 records per
// OE across the drafted masters), and semicolons are used ONLY as the top-level
// separator — commas, dashes and parenthetical asides appear inside records and
// must not split them. This reformats existing content; it never adds any.
const splitEvidenceRecords = (evidence: string): string[] =>
  evidence
    .split(";")
    .map((r) => r.trim())
    .filter((r) => r.length > 0);

// Required Records / Evidence Checklist — the single canonical place a reader
// finds the full evidence detail for the standard, grouped by the OE that
// requires it. This exists because the evidence column of the OE Cross-Reference
// table had grown to hold multi-hundred-character lists, which made that table
// unreadable as the navigation index it is meant to be.
//
// Returns [] when no OE carries evidence data, so the section is omitted entirely
// rather than printed empty. That is currently the case for HIC.1 and HIC.2,
// whose oe_mapping entries were authored without evidence or responsible fields.
const renderRequiredRecords = (oeMapping: OeMappingEntry[]): (Paragraph | Table)[] => {
  const withEvidence = oeMapping.filter((m) => m.evidence && m.evidence.trim().length > 0);
  if (withEvidence.length === 0) return [];

  const out: (Paragraph | Table)[] = [
    new Paragraph({
      children: [
        new TextRun({
          text:
            "The records below are the documented evidence for this standard. Each record is " +
            "listed against the objective element that requires it.",
          size: 22,
          italics: true,
        }),
      ],
      spacing: { after: 180 },
    }),
  ];

  for (const entry of withEvidence) {
    out.push(
      new Paragraph({
        children: [new TextRun({ text: `${entry.oeCode} — ${entry.requirement}`, bold: true, size: 22 })],
        spacing: { before: 200, after: 90 },
      }),
    );
    for (const record of splitEvidenceRecords(entry.evidence!)) {
      out.push(
        new Paragraph({
          children: [new TextRun({ text: record, size: 22 })],
          bullet: { level: 0 },
          spacing: { after: 60 },
        }),
      );
    }
  }
  return out;
};

export function buildPolicyDocument(data: PolicyDocData): Document {
  const today = new Date().toLocaleDateString("en-GB").replace(/\//g, "-");

  const controlTable = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({ children: [cell("Document No.", { bold: true, shade: true }), cell(data.docNo), cell("Version", { bold: true, shade: true }), cell(data.version ?? "1.0")] }),
      new TableRow({ children: [cell("Effective Date", { bold: true, shade: true }), cell("[DD-MM-YYYY]"), cell("Review Date", { bold: true, shade: true }), cell("[DD-MM-YYYY]")] }),
      new TableRow({ children: [cell("Applicable OE(s)", { bold: true, shade: true }), cell(data.oeLevel ? `${data.oeCode} (${data.oeLevel})` : data.oeCode), cell("NABH Chapter", { bold: true, shade: true }), cell(data.chapterName)] }),
      new TableRow({ children: [cell("Prepared By", { bold: true, shade: true }), cell("_________________"), cell("Date", { bold: true, shade: true }), cell("________")] }),
      new TableRow({ children: [cell("Reviewed By", { bold: true, shade: true }), cell("_________________"), cell("Date", { bold: true, shade: true }), cell("________")] }),
      new TableRow({ children: [cell("Approved By", { bold: true, shade: true }), cell("_________________"), cell("Date", { bold: true, shade: true }), cell("________")] }),
    ],
  });

  // Revision history comes from the master row. The fallback row is used only when
  // a row carries no history yet; it states the version and today's date without
  // asserting anything about how the content was produced or reviewed, because the
  // template cannot know that and the old hardcoded claim was wrong for every
  // human-reviewed master.
  const revisionRows: RevisionEntry[] =
    data.revisionHistory && data.revisionHistory.length > 0
      ? data.revisionHistory
      : [{ version: data.version ?? "1.0", date: today, description: "Issued." }];

  const revisionHistory = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({ children: [cell("Version", { bold: true, shade: true }), cell("Date", { bold: true, shade: true }), cell("Description of Change", { bold: true, shade: true, width: 50 })] }),
      ...revisionRows.map(
        (r) => new TableRow({ children: [cell(r.version), cell(r.date), cell(r.description, { width: 50 })] }),
      ),
    ],
  });

  // The OE Cross-Reference table is a NAVIGATION INDEX, nothing more: which OE,
  // what it requires in one line, where it is answered, and who owns it. The
  // Evidence column was deliberately removed — full evidence detail now lives in
  // the Required Records / Evidence Checklist section, and printing it in both
  // places made this table unusable for the one job it has.
  //
  // Note this reads m.responsible, NOT m.evidence: HIC.1 and HIC.2 have neither,
  // and they correctly fall through to the three-column form rather than render a
  // Responsible column of dashes.
  const hasResponsibleData = data.oeMapping?.some((m) => m.responsible) ?? false;

  const requiredRecords = data.oeMapping ? renderRequiredRecords(data.oeMapping) : [];

  const oeMappingTable = data.oeMapping && data.oeMapping.length > 0
    ? new Table({
        width: { size: 100, type: WidthType.PERCENTAGE },
        rows: hasResponsibleData
          ? [
              new TableRow({
                children: [
                  cell("OE Code", { bold: true, shade: true, width: 15 }),
                  cell("Requirement", { bold: true, shade: true, width: 45 }),
                  cell("Addressed In", { bold: true, shade: true, width: 20 }),
                  cell("Responsible", { bold: true, shade: true, width: 20 }),
                ],
              }),
              ...data.oeMapping.map(
                (m) =>
                  new TableRow({
                    children: [
                      cell(m.oeCode, { width: 15 }),
                      cell(m.requirement, { width: 45 }),
                      cell(m.steps, { width: 20 }),
                      cell(m.responsible ?? "—", { width: 20 }),
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
          ...(data.definitions
            ? [heading("Definitions"), body(data.definitions)]
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
          ...(data.trainingCompetency
            ? [heading("Training & Competency"), body(data.trainingCompetency)]
            : []),
          heading("5. Responsibility"),
          body(data.responsibility),
          ...(data.resourcesRequired
            ? [heading("Resources Required"), body(data.resourcesRequired)]
            : []),
          ...(data.monitoringAudit
            ? [heading("Monitoring & Audit"), body(data.monitoringAudit)]
            : []),
          ...(data.exceptions
            ? [heading("Exceptions / Special Situations"), body(data.exceptions)]
            : []),
          heading("6. References"),
          body(data.references),
          heading("7. Distribution"),
          body(data.distribution),
          // Required Records sits between Distribution and Revision History: it is
          // content an assessor reads, so it belongs before the document's back
          // matter, not after it. Section numbers are computed rather than literal
          // so that a master with no evidence data (HIC.1, HIC.2) does not print a
          // document that skips from 7 straight to 9.
          ...(requiredRecords.length > 0
            ? [heading("8. Required Records / Evidence Checklist"), ...requiredRecords]
            : []),
          heading(`${requiredRecords.length > 0 ? 9 : 8}. Revision History`),
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
