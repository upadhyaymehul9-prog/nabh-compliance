// Local preview renderer — LOCAL-FIRST TESTING, no Supabase, no deploy, no network
// call to any edge function.
//
// Imports the REAL shipping template (supabase/functions/_shared/policy-doc-template.ts)
// and renders each local draft to a .docx you can open in Word. This is how the
// Required Records section, the trimmed OE Cross-Reference table and the version /
// revision-history rendering get reviewed BEFORE anything is deployed or written to
// the database.
//
// Run:  deno run --allow-read --allow-write --allow-net policies/build/render_previews.ts
//   (--allow-net is needed once, so Deno can fetch the `npm:docx` dependency.)
//
// Output: policies/build/preview/<STANDARD>_preview.docx
//
// NOTE ON HIC.2: it has no local draft file, because it exists only as a row in
// shco_policy_masters (RLS on, zero policies, so only the service role can read it —
// and the service role key deliberately never enters this terminal). It is skipped
// with a warning rather than silently omitted.

import { buildPolicyDocument, documentToBuffer, type RevisionEntry } from "../../supabase/functions/_shared/policy-doc-template.ts";

const REPO = new URL("../../", import.meta.url);
const DRAFTS = new URL("policies/drafts/", REPO);
const OUT = new URL("policies/build/preview/", REPO);

const HOSPITAL = "Preview Hospital";

// Revision history for the preview only — NOT written to the database by this
// script. These are the values the backfill will apply, so the preview shows
// exactly what the backfilled document will look like.
// Dates are each row's created_at from shco_policy_masters; HIC.4's 1.1 entry is
// the post-approval edit documented in scripts/master-policy-todos.md.
const PREVIEW_REVISIONS: Record<string, { version: string; history: RevisionEntry[] }> = {
  "HIC.1": {
    version: "1.0",
    history: [{ version: "1.0", date: "03-08-2026", description: "Initial release." }],
  },
  // Pre-registered so that HIC.2 renders automatically as soon as a local
  // hic2_draft.json exists — see the note at the top of this file.
  "HIC.2": {
    version: "1.0",
    history: [{ version: "1.0", date: "01-08-2026", description: "Initial release." }],
  },
  "HIC.3": {
    version: "1.0",
    history: [{ version: "1.0", date: "03-08-2026", description: "Initial release." }],
  },
  "HIC.4": {
    version: "1.1",
    history: [
      { version: "1.0", date: "06-08-2026", description: "Initial release." },
      {
        version: "1.1",
        date: "06-08-2026",
        description:
          "Step 7 nested-bracket correction; step 31 and step 34 placeholder normalisation.",
      },
    ],
  },
  "HIC.5": {
    version: "1.0",
    history: [{ version: "1.0", date: "07-08-2026", description: "Initial release." }],
  },
  "HIC.6": {
    version: "1.0",
    history: [{ version: "1.0", date: "10-08-2026", description: "Initial release." }],
  },
};

interface Draft {
  standard_code: string;
  chapter: string;
  oe_codes: string[];
  policy_title: string;
  purpose: string;
  scope: string;
  policy_statement: string;
  procedure_steps: string[];
  responsibility: string;
  references_text: string;
  distribution: string;
  abbreviations?: string;
  definitions?: string;
  disclaimer?: string;
  oe_mapping?: { oe_code: string; requirement: string; steps: string; evidence?: string; responsible?: string }[];
  training_competency?: string;
  resources_required?: string;
  monitoring_audit?: string;
  exceptions?: string;
  // Drafts built after migration 20260812 carry these themselves (AAC.1 onward).
  // When present they take precedence over PREVIEW_REVISIONS, which exists only
  // for the HIC.1-6 drafts that predate the migration and were backfilled.
  version?: string;
  revision_history?: RevisionEntry[];
}

const sub = (t: string) => t.replaceAll("{{HOSPITAL_NAME}}", HOSPITAL);

const EXPECTED = [
  "AAC.1",
  "COP.1", "COP.2", "COP.3", "COP.4", "COP.5", "COP.6", "COP.7",
  "COP.8", "COP.9", "COP.10", "COP.11", "COP.12", "COP.13",
  "HIC.1", "HIC.2", "HIC.3", "HIC.4", "HIC.5", "HIC.6",
  "MOM.1", "MOM.2", "MOM.3", "MOM.4", "MOM.5", "MOM.6",
  "MOM.7", "MOM.8", "MOM.9",
  "ROM.1", "ROM.2", "ROM.3", "ROM.4",
];

async function main() {
  await Deno.mkdir(OUT, { recursive: true });

  const files: string[] = [];
  for await (const e of Deno.readDir(DRAFTS)) {
    if (e.isFile && e.name.endsWith("_draft.json")) files.push(e.name);
  }
  files.sort();

  const rendered: string[] = [];

  for (const name of files) {
    const draft: Draft = JSON.parse(await Deno.readTextFile(new URL(name, DRAFTS)));
    const code = draft.standard_code;
    // Prefer the draft's own version/revision_history (AAC.1 onward); fall back
    // to the PREVIEW_REVISIONS map for the pre-migration HIC drafts.
    const rev =
      draft.version && draft.revision_history && draft.revision_history.length > 0
        ? { version: draft.version, history: draft.revision_history }
        : PREVIEW_REVISIONS[code];

    const oeMapping = draft.oe_mapping?.map((m) => ({
      oeCode: m.oe_code,
      requirement: sub(m.requirement),
      steps: m.steps,
      evidence: m.evidence ? sub(m.evidence) : undefined,
      responsible: m.responsible ? sub(m.responsible) : undefined,
    }));

    const doc = buildPolicyDocument({
      hospitalName: HOSPITAL,
      docNo: `PREVIEW/${draft.chapter}/POL-${code.split(".").slice(1).join("")}`,
      docTitle: sub(draft.policy_title),
      oeCode: draft.oe_codes.join(", "),
      oeLevel: "",
      chapterName: draft.chapter,
      abbreviations: draft.abbreviations ? sub(draft.abbreviations) : undefined,
      definitions: draft.definitions ? sub(draft.definitions) : undefined,
      oeMapping,
      purpose: sub(draft.purpose),
      scope: sub(draft.scope),
      policyStatement: sub(draft.policy_statement),
      procedureSteps: draft.procedure_steps.map(sub),
      trainingCompetency: draft.training_competency ? sub(draft.training_competency) : undefined,
      responsibility: sub(draft.responsibility),
      resourcesRequired: draft.resources_required ? sub(draft.resources_required) : undefined,
      monitoringAudit: draft.monitoring_audit ? sub(draft.monitoring_audit) : undefined,
      exceptions: draft.exceptions ? sub(draft.exceptions) : undefined,
      references: sub(draft.references_text),
      distribution: sub(draft.distribution),
      disclaimer: draft.disclaimer ? sub(draft.disclaimer) : undefined,
      version: rev?.version,
      revisionHistory: rev?.history,
    });

    const buf = await documentToBuffer(doc);
    const outPath = new URL(`${code}_preview.docx`, OUT);
    await Deno.writeFile(outPath, buf);

    const recordCount = (draft.oe_mapping ?? [])
      .filter((m) => m.evidence)
      .reduce((n, m) => n + m.evidence!.split(";").filter((r) => r.trim()).length, 0);
    const oesWithEvidence = (draft.oe_mapping ?? []).filter((m) => m.evidence).length;

    console.log(
      `${code.padEnd(6)} v${(rev?.version ?? "1.0").padEnd(4)} ` +
        `steps=${String(draft.procedure_steps.length).padStart(2)} ` +
        `OEs=${draft.oe_codes.length} ` +
        `requiredRecords=${oesWithEvidence > 0 ? `${recordCount} across ${oesWithEvidence} OEs` : "SECTION OMITTED (no evidence data)"}`,
    );
    rendered.push(code);
  }

  const missing = EXPECTED.filter((c) => !rendered.includes(c));
  console.log(`\nRendered ${rendered.length} of ${EXPECTED.length} → policies/build/preview/`);
  if (missing.length > 0) {
    console.log(`NOT RENDERED: ${missing.join(", ")} — no local draft file (see header note).`);
  }
}

await main();
