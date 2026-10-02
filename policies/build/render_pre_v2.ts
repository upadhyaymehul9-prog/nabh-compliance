// Renders PRE.2–PRE.6 v2 (adoptable-policy shape) to Word.
// PRE.1 uses render_pre1_v2.ts. Does not write to Supabase.
//
// Preview: DRAFT_JSON=pre2_v2_draft.json deno run --allow-read --allow-write --allow-net --allow-env policies/build/render_pre_v2.ts
// Master:  DRAFT_JSON=pre2_v2_draft.json HOSPITAL_PLACEHOLDER='«Hospital Name»' OUT_DIR=policies/build/masters/ OUT_SUFFIX=_v2_master deno run ...

import {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, AlignmentType, ShadingType, Footer, BorderStyle,
} from "npm:docx";

const REPO = new URL("../../", import.meta.url);
const DRAFT_JSON = Deno.env.get("DRAFT_JSON") ?? "pre2_v2_draft.json";
const isHcoDraft = DRAFT_JSON.startsWith("hco_");
const DRAFTS = new URL(
  Deno.env.get("DRAFTS_DIR") ?? (isHcoDraft ? "policies/drafts_hco/" : "policies/drafts/"),
  REPO,
);
const OUT = new URL(
  Deno.env.get("OUT_DIR") ?? (isHcoDraft ? "policies/build/preview_hco/" : "policies/build/preview/"),
  REPO,
);
const OUT_SUFFIX = Deno.env.get("OUT_SUFFIX") ?? "_v2_preview";
const HOSPITAL = Deno.env.get("HOSPITAL_PLACEHOLDER") ?? "Preview Hospital";

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

// Governance-section-only renderer. `d.responsibility` blocks are shaped as
// "Role name\n- duty line\n- duty line", separated by blank lines. The
// generic blocks() above bullets every line in a "- "-containing block,
// including the role-name header line, so a reader sees a flat bullet list
// with no way to tell a role from what it does. This renders the first
// (non-"- ") line of each block as a bold, non-bulleted sub-heading and
// only the following "- " lines as bullets. Deliberately not reused for any
// other field — References/Distribution/Abbreviations etc. keep using the
// generic blocks() unchanged.
function responsibilityBlocks(text: string): Paragraph[] {
  const normalized = text.replace(/\r\n/g, "\n").trim();
  const out: Paragraph[] = [];
  for (const block of normalized.split(/\n\n+/)) {
    const trimmed = block.trim();
    if (!trimmed) continue;
    const lines = trimmed.split("\n").map((l) => l.trim()).filter(Boolean);
    const dutyLines = lines.filter((l) => l.startsWith("- "));
    const roleLines = lines.filter((l) => !l.startsWith("- "));
    // Only treat this as a role/duty pair when the shape actually matches:
    // exactly one role-name line followed by one or more "- " duty lines.
    // Anything else (a block with no "- " line, or "- " lines mixed with
    // more than one non-"- " line) falls back to the generic renderer so
    // this never silently reshapes content it wasn't designed for.
    if (roleLines.length === 1 && dutyLines.length >= 1) {
      out.push(new Paragraph({
        children: [new TextRun({ text: roleLines[0], bold: true, size: 22 })],
        spacing: { before: 100, after: 20 },
      }));
      for (const line of dutyLines) {
        out.push(new Paragraph({
          children: [new TextRun({ text: line.replace(/^- /, ""), size: 22 })],
          bullet: { level: 0 },
          spacing: { after: 60 },
        }));
      }
      continue;
    }
    out.push(...blocks(trimmed));
  }
  return out;
}

interface V2Draft {
  standard_code: string;
  chapter?: string;
  edition_label?: string;
  render_basename?: string;
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
  stop_work?: string;
  oe_mapping: { oe_code: string; requirement: string; steps: string; responsible?: string; records?: string[] }[];
  version?: string;
  doc_no?: string;
  subtitle?: string;
  footer_label?: string;
  acknowledgement_note?: string;
  prepared_by?: string;
  control_extra_rows?: string[][];
}

/** Prefer draft.prepared_by; else parse resources_required; else neutral HCO default. */
function resolvePreparedBy(d: V2Draft): string {
  if (d.prepared_by && d.prepared_by.trim()) return d.prepared_by.trim();
  const rr = d.resources_required ?? "";
  const m = rr.match(/Prepared by \(designation\):\s*(«[^»]+»|[^\n]+?)(?:\s{2,}Name|\s*$)/);
  if (m) return m[1].trim();
  return "«Quality Coordinator»";
}

function sectionAfterWhatWeDo(hasStop: boolean): { n: number; title: string; key: string }[] {
  const rest: { title: string; key: string }[] = [];
  if (hasStop) rest.push({ title: "Stop-work authority", key: "stop" });
  rest.push(
    { title: "Governance and responsibility", key: "gov" },
    { title: "Quality monitoring (RCA → CAPA)", key: "mon" },
    { title: "Training and staff acknowledgement", key: "train" },
    { title: "References", key: "refs" },
    { title: "Distribution", key: "dist" },
    { title: "Abbreviations", key: "abbr" },
  );
  return rest.map((r, i) => ({ n: 6 + i, title: r.title, key: r.key }));
}

function buildV2Document(d: V2Draft): Document {
  const docNo = d.doc_no ?? "«PRE/POL/00»";
  const hasStop = Boolean((d.stop_work ?? "").trim());
  const after = sectionAfterWhatWeDo(hasStop);
  const lastAfter = after[after.length - 1].n;
  const nTrace = lastAfter + 1;
  const nRecords = lastAfter + 2;

  const controlRows: string[][] = [
    ["Document No.", docNo, "Version", d.version ?? "2.0"],
    ["Issue No.", "«01»", "Review due", "«one year from implementation»"],
    ["Date created", "«________»", "Date of implementation", "«________»"],
    ["Prepared by", `${resolvePreparedBy(d)}  Name «________»`, "Signature", "«________»"],
    ["Reviewed by", "«Quality Coordinator»  Name «________»", "Signature", "«________»"],
    ["Approved by", "«Medical Superintendent»  Name «________»", "Signature", "«________»"],
    ...(d.control_extra_rows ?? []),
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
        text: d.subtitle ?? "Patient rights in day-to-day care. Not a commentary on NABH objective elements.",
        italics: true,
        size: 20,
      })],
      alignment: AlignmentType.CENTER,
      spacing: { after: 240 },
    }),
    h1("Document control"),
    new Paragraph({
      children: [new TextRun({
        text: "« » marks an editable default a small hospital can adopt. «________» is a true blank and must be completed before issue.",
        italics: true,
        size: 18,
      })],
      spacing: { after: 120 },
    }),
    controlTable,
    h1("Statement of intent"),
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

  const stepNums: string[] = [];
  for (const step of d.procedure_steps) {
    const normalized = step.replace(/\r\n/g, "\n");
    const m = normalized.match(/^(\d+\.\d+)\s+([^\n]+)\n\n([\s\S]*)$/);
    if (!m) throw new Error(`procedure step is not '5.n Title\\n\\nbody': ${normalized.slice(0, 80)}`);
    stepNums.push(m[1]);
    children.push(h2(`${m[1]} ${m[2]}`));
    children.push(...blocks(sub(m[3])));
  }
  for (let i = 0; i < stepNums.length; i++) {
    if (stepNums[i] !== `5.${i + 1}`) {
      throw new Error(`What-we-do sub-numbers collided or skipped: ${stepNums.join(", ")}`);
    }
  }

  const top: number[] = [1, 2, 3, 4, 5];
  for (const row of after) {
    top.push(row.n);
    if (row.key === "stop") {
      children.push(h1(`${row.n}. ${row.title}`), ...blocks(sub(d.stop_work ?? "")));
    } else if (row.key === "gov") {
      children.push(h1(`${row.n}. ${row.title}`), ...responsibilityBlocks(sub(d.responsibility)));
    } else if (row.key === "mon") {
      children.push(h1(`${row.n}. ${row.title}`), ...blocks(sub(d.monitoring_audit ?? "")));
    } else if (row.key === "train") {
      children.push(
        h1(`${row.n}. ${row.title}`),
        ...blocks(sub(d.training_competency ?? "")),
        ackTable,
        new Paragraph({
          children: [new TextRun({
            text: d.acknowledgement_note ?? "The Nursing Superintendent holds signed acknowledgements with the induction record.",
            italics: true,
            size: 20,
          })],
          spacing: { before: 120, after: 200 },
        }),
      );
    } else if (row.key === "refs") {
      children.push(h1(`${row.n}. ${row.title}`), ...blocks(sub(d.references_text)));
    } else if (row.key === "dist") {
      children.push(h1(`${row.n}. ${row.title}`), ...blocks(sub(d.distribution)));
    } else if (row.key === "abbr") {
      children.push(h1(`${row.n}. ${row.title}`), ...blocks(sub(d.abbreviations)));
    }
  }
  top.push(nTrace, nRecords);
  for (let i = 1; i < top.length; i++) {
    if (top[i] !== top[i - 1] + 1) {
      throw new Error(`top-level numbering not a clean run: ${top.join(", ")}`);
    }
  }

  children.push(
    h1(`${nTrace}. Traceability to ${d.edition_label ?? "NABH SHCO 3rd Edition"} ${d.standard_code}`),
    new Paragraph({
      children: [new TextRun({
        text: "This table is an index. It is not how the policy is organised.",
        italics: true,
        size: 20,
      })],
      spacing: { after: 120 },
    }),
    trace,
    h1(`${nRecords}. Required Records / Evidence Checklist`),
    new Paragraph({
      children: [new TextRun({
        text: "Records the hospital holds under this policy, listed by objective element.",
        italics: true,
        size: 20,
      })],
      spacing: { after: 120 },
    }),
  );

  for (const m of d.oe_mapping) {
    children.push(h2(`${m.oe_code} — ${m.requirement}`));
    for (const rec of m.records ?? []) {
      children.push(new Paragraph({
        children: [new TextRun({ text: rec, size: 22 })],
        bullet: { level: 0 },
        spacing: { after: 60 },
      }));
    }
  }

  children.push(h1("Disclaimer"), ...blocks(sub(d.disclaimer)));

  const footer = d.footer_label ?? sub(d.policy_title);
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
                  text: `${HOSPITAL}  |  ${docNo}  |  Controlled document  |  ${footer}`,
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
  const d: V2Draft = JSON.parse(await Deno.readTextFile(new URL(DRAFT_JSON, DRAFTS)));
  const basename =
    Deno.env.get("OUT_BASENAME") ??
    d.render_basename ??
    (d.chapter === "HCO" ? `HCO.${d.standard_code}` : d.standard_code);
  const outName = `${basename}${OUT_SUFFIX}.docx`;
  const doc = buildV2Document(d);
  await Deno.writeFile(new URL(outName, OUT), await Packer.toBuffer(doc).then((b) => new Uint8Array(b)));
  const outRel = new URL(outName, OUT).pathname.replace(/^\/workspace\/?/, "");
  console.log(`wrote ${outRel || outName}`);
}

await main();
