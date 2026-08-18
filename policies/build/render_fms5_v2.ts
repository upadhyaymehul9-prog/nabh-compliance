// Renders FMS.5 v1 (shipping template) and FMS.5 v2 (adoptable-policy shape)
// side by side. Does not write to Supabase. Does not overwrite other previews
// except FMS.5_v1_compare.docx and FMS.5_v2_preview.docx.
//
// Run: deno run --allow-read --allow-write --allow-net policies/build/render_fms5_v2.ts

import {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, AlignmentType, ShadingType, Footer, BorderStyle,
} from "npm:docx";
import { buildPolicyDocument, documentToBuffer, type RevisionEntry } from "../../supabase/functions/_shared/policy-doc-template.ts";

const REPO = new URL("../../", import.meta.url);
const DRAFTS = new URL("policies/drafts/", REPO);
const OUT = new URL("policies/build/preview/", REPO);
const HOSPITAL = "Preview Hospital";

const sub = (t: string) => t.replaceAll("{{HOSPITAL_NAME}}", HOSPITAL);

const thin = { style: BorderStyle.SINGLE, size: 4, color: "999999" };
const borders = { top: thin, bottom: thin, left: thin, right: thin };

function cell(text: string, opts: { bold?: boolean; shade?: boolean; width?: number; italics?: boolean } = {}) {
  return new TableCell({
    width: { size: opts.width ?? 25, type: WidthType.PERCENTAGE },
    borders,
    shading: opts.shade ? { type: ShadingType.CLEAR, fill: "E8E8E8" } : undefined,
    children: [new Paragraph({
      children: [new TextRun({ text, bold: opts.bold ?? false, italics: opts.italics, size: 18 })],
    })],
  });
}

const h1 = (text: string) =>
  new Paragraph({ text, heading: HeadingLevel.HEADING_1, spacing: { before: 280, after: 120 } });
const h2 = (text: string) =>
  new Paragraph({ text, heading: HeadingLevel.HEADING_2, spacing: { before: 220, after: 100 } });

function blocks(text: string): Paragraph[] {
  const normalized = text.replace(/\r\n/g, "\n").trim();
  const out: Paragraph[] = [];
  for (const block of normalized.split(/\n\n+/)) {
    const trimmed = block.trim();
    if (!trimmed) continue;
    if (/^- /.test(trimmed) || trimmed.includes("\n- ")) {
      for (const line of trimmed.split(/\n(?=- )/)) {
        const cleaned = line.trim().replace(/^- /, "");
        if (!cleaned) continue;
        out.push(new Paragraph({
          children: [new TextRun({ text: cleaned, size: 22 })],
          bullet: { level: 0 },
          spacing: { after: 60 },
        }));
      }
      continue;
    }
    if (/^\d+\.\s/.test(trimmed) && trimmed.includes("\n")) {
      for (const line of trimmed.split("\n")) {
        const t = line.trim();
        if (!t) continue;
        out.push(new Paragraph({
          children: [new TextRun({ text: t, size: 22 })],
          spacing: { after: 80 },
        }));
      }
      continue;
    }
    out.push(new Paragraph({
      children: [new TextRun({ text: trimmed, size: 22 })],
      spacing: { after: 140 },
    }));
  }
  return out;
}

interface V2Draft {
  policy_title: string;
  purpose: string;
  scope: string;
  policy_statement: string;
  procedure_steps: string[];
  responsibility: string;
  references_text: string;
  distribution: string;
  abbreviations: string;
  disclaimer: string;
  definitions?: string;
  exceptions?: string;
  monitoring_audit?: string;
  training_competency?: string;
  resources_required?: string;
  oe_mapping: { oe_code: string; requirement: string; steps: string; responsible?: string }[];
  version?: string;
  revision_history?: RevisionEntry[];
}

function buildV2Document(d: V2Draft): Document {
  const controlRows = [
    ["Document No.", "«FMS/POL/05»", "Version", d.version ?? "2.0"],
    ["Issue No.", "«01»", "Review due", "«one year from implementation»"],
    ["Date created", "«________»", "Date of implementation", "«________»"],
    ["Prepared by", "«Maintenance In-Charge»  Name «________»", "Signature", "«________»"],
    ["Reviewed by", "«Quality Coordinator»  Name «________»", "Signature", "«________»"],
    ["Approved by", "«Medical Superintendent»  Name «________»", "Signature", "«________»"],
    ["Fire NOC No.", "«________»", "Issuing authority / valid until", "«________»"],
    ["Assembly point", "«________»", "Receiving hospital", "«________»"],
  ];
  const controlTable = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: controlRows.map((r) =>
      new TableRow({
        children: [
          cell(r[0], { bold: true, shade: true, width: 22 }),
          cell(r[1], { width: 28 }),
          cell(r[2], { bold: true, shade: true, width: 22 }),
          cell(r[3], { width: 28 }),
        ],
      }),
    ),
  });

  const ackTable = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({
        children: [
          cell("Name", { bold: true, shade: true, width: 22 }),
          cell("Designation", { bold: true, shade: true, width: 18 }),
          cell("Department / floor", { bold: true, shade: true, width: 20 }),
          cell("Date", { bold: true, shade: true, width: 12 }),
          cell("Signature", { bold: true, shade: true, width: 28 }),
        ],
      }),
      ...[1, 2, 3, 4, 5].map(() =>
        new TableRow({
          children: [
            cell(" ", { width: 22 }),
            cell(" ", { width: 18 }),
            cell(" ", { width: 20 }),
            cell(" ", { width: 12 }),
            cell(" ", { width: 28 }),
          ],
        }),
      ),
    ],
  });

  const trace = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({
        children: [
          cell("OE", { bold: true, shade: true, width: 12 }),
          cell("Requirement", { bold: true, shade: true, width: 32 }),
          cell("Where this policy addresses it", { bold: true, shade: true, width: 32 }),
          cell("Responsible", { bold: true, shade: true, width: 24 }),
        ],
      }),
      ...d.oe_mapping.map((m) =>
        new TableRow({
          children: [
            cell(m.oe_code, { width: 12 }),
            cell(m.requirement, { width: 32 }),
            cell(m.steps, { width: 32 }),
            cell(m.responsible ?? "—", { width: 24 }),
          ],
        }),
      ),
    ],
  });

  const children: (Paragraph | Table)[] = [
    new Paragraph({
      children: [new TextRun({ text: HOSPITAL, bold: true, size: 32 })],
      alignment: AlignmentType.CENTER,
      spacing: { after: 60 },
    }),
    new Paragraph({
      children: [new TextRun({ text: sub(d.policy_title), bold: true, size: 28 })],
      alignment: AlignmentType.CENTER,
      spacing: { after: 60 },
    }),
    new Paragraph({
      children: [new TextRun({
        text: "Standards the hospital requires of its staff. Not a drill script and not a commentary on NABH objective elements.",
        italics: true,
        size: 20,
      })],
      alignment: AlignmentType.CENTER,
      spacing: { after: 240 },
    }),
    h1("Document control"),
    new Paragraph({
      children: [new TextRun({
        text: "« » marks an editable default a small hospital can adopt. «________» is a true blank and must be completed before issue. Template-test rebuild — not an approved master.",
        italics: true,
        size: 18,
      })],
      spacing: { after: 120 },
    }),
    controlTable,
    h1("Safety objective"),
    ...blocks(sub(d.definitions ?? "")),
    h1("1. Purpose"),
    ...blocks(sub(d.purpose)),
    h1("2. Scope"),
    ...blocks(sub(d.scope)),
    h1("3. Policy standards"),
    ...blocks(sub(d.policy_statement)),
    h1("4. Non-negotiable rules"),
    ...blocks(sub(d.exceptions ?? "")),
    h1("5. What we do"),
  ];

  for (const step of d.procedure_steps) {
    const normalized = step.replace(/\r\n/g, "\n");
    const m = normalized.match(/^(\d+)\.\s([^\n]+)\n\n([\s\S]*)$/);
    if (!m) {
      children.push(...blocks(sub(normalized)));
      continue;
    }
    children.push(h2(`${m[1]}. ${m[2]}`));
    children.push(...blocks(sub(m[3])));
  }

  children.push(
    h1("6. Governance and responsibility"),
    ...blocks(sub(d.responsibility)),
    h1("7. Quality monitoring (RCA → CAPA)"),
    ...blocks(sub(d.monitoring_audit ?? "")),
    h1("8. Training and staff acknowledgement"),
    ...blocks(sub(d.training_competency ?? "")),
    ackTable,
    new Paragraph({
      children: [new TextRun({
        text: "A staff member who has not signed does not work a night shift on an occupied floor. The Nursing Superintendent holds signed acknowledgements with the induction record.",
        italics: true,
        size: 20,
      })],
      spacing: { before: 120, after: 200 },
    }),
    h1("9. References"),
    ...blocks(sub(d.references_text)),
    h1("10. Distribution"),
    ...blocks(sub(d.distribution)),
    h1("11. Abbreviations"),
    ...blocks(sub(d.abbreviations)),
    h1("12. Traceability to NABH SHCO 3rd Edition FMS.5"),
    new Paragraph({
      children: [new TextRun({
        text: "This table is an index. It is not how the policy is organised.",
        italics: true,
        size: 20,
      })],
      spacing: { after: 120 },
    }),
    trace,
    h1("Disclaimer"),
    ...blocks(sub(d.disclaimer)),
  );

  return new Document({
    sections: [{
      properties: { page: { size: { width: 11906, height: 16838 } } },
      footers: {
        default: new Footer({
          children: [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [
                new TextRun({
                  text: `${HOSPITAL}  |  «FMS/POL/05»  |  Controlled document  |  Fire and non-fire emergencies`,
                  size: 16,
                  italics: true,
                }),
              ],
            }),
          ],
        }),
      },
      children,
    }],
  });
}

async function main() {
  await Deno.mkdir(OUT, { recursive: true });

  const v1 = JSON.parse(await Deno.readTextFile(new URL("fms5_draft.json", DRAFTS)));
  const v2: V2Draft = JSON.parse(await Deno.readTextFile(new URL("fms5_v2_draft.json", DRAFTS)));

  const v1Doc = buildPolicyDocument({
    hospitalName: HOSPITAL,
    docNo: `PREVIEW/FMS/POL-5`,
    docTitle: sub(v1.policy_title),
    oeCode: v1.oe_codes.join(", "),
    oeLevel: "",
    chapterName: v1.chapter,
    abbreviations: v1.abbreviations ? sub(v1.abbreviations) : undefined,
    oeMapping: v1.oe_mapping?.map((m: { oe_code: string; requirement: string; steps: string; evidence?: string; responsible?: string }) => ({
      oeCode: m.oe_code,
      requirement: sub(m.requirement),
      steps: m.steps,
      evidence: m.evidence ? sub(m.evidence) : undefined,
      responsible: m.responsible ? sub(m.responsible) : undefined,
    })),
    purpose: sub(v1.purpose),
    scope: sub(v1.scope),
    policyStatement: sub(v1.policy_statement),
    procedureSteps: v1.procedure_steps.map(sub),
    responsibility: sub(v1.responsibility),
    references: sub(v1.references_text),
    distribution: sub(v1.distribution),
    disclaimer: v1.disclaimer ? sub(v1.disclaimer) : undefined,
    version: v1.version,
    revisionHistory: v1.revision_history,
  });

  const v2Doc = buildV2Document(v2);

  await Deno.writeFile(new URL("FMS.5_v1_compare.docx", OUT), await documentToBuffer(v1Doc));
  await Deno.writeFile(new URL("FMS.5_v2_preview.docx", OUT), await Packer.toBuffer(v2Doc).then((b) => new Uint8Array(b)));
  console.log("wrote policies/build/preview/FMS.5_v1_compare.docx  (current OE-skeleton, shipping template)");
  console.log("wrote policies/build/preview/FMS.5_v2_preview.docx  (adoptable-policy shape)");
}

await main();
