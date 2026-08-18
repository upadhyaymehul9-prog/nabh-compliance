# Master Policy — Deferred Content TODOs

Topics surfaced while drafting master policies that were deliberately **not** folded into the
standard being drafted, because they belong to a different NABH standard. Pick these up when
the owning standard's master policy is drafted.

Source of the gaps: comparison of the HIC.2 master draft against NABH's own
`E.-HIB_CHECK-04.12_Hospital-Infection-Control-Checklist.docx`.

> Caveat carried forward: that checklist uses an older Entry-Level SHCO edition's OE numbering
> (it maps "HIC 2 c" to pre-/post-exposure prophylaxis, whereas SHCO 3rd Edition HIC.2.c is
> transmission-based precautions). Use it as a topic prompt, never as an OE map.

---

# STANDING RULE: Two-tier depth (added 2026-08-10)

**Read this before drafting any master policy. It is a process rule, not a task — it does not
get ticked off and it does not expire.**

HIC.1–HIC.6 were each drafted at uniform maximum depth. That was the right call for the first
chapter, because it established the house style, the verification loop and the boundary
discipline between standards. It does not scale: at that rate the remaining SHCO Full chapters
would take longer than the programme can wait, and most of the effort lands on objective
elements that will never be the thing an assessor asks a document for.

From the **seventh master policy onward** — that is, every SHCO Full master policy drafted after
HIC.6, whichever chapter it belongs to — depth is allocated per objective element, by tier.

**The tier is decided by `doc_required` in `shco_full_oes`.** That flag is the asterisk in the
official SHCO 3rd Edition PDF and is trustworthy as of the ten-chapter audit of 2026-08-10.
Verify it against the PDF for the standard being drafted anyway — the audit found 14 wrong flags
and the cost of checking five OEs is minutes. If a flag is ever corrected, the OE's tier changes
with it, and an OE promoted to asterisked needs its block rebuilt to Tier 1.

## Tier 1 — full treatment, HIC.6-grade. ONLY for asterisked OEs (`doc_required = true`)

- Full procedure steps carrying the **reasoning**, not just the instruction — why the rule exists,
  what fails without it, and what the common error is.
- Full evidence column detail for that OE.
- **Cross-check against every previously approved standard** for overlaps and contradictions
  *before* drafting, and state the division of responsibility explicitly in Scope.
- **Fact-check against current international standards** (CDC, WHO, ISO, AAMI, CLSI and the
  Indian statutory sources) where the OE is technical or clinical, and record each verified fact
  in `universal_facts_checklist`.
- **Byte-level verification loop**: hash checks against the built draft, chunked SQL where the
  payload exceeds what the tool accepts, and re-verification after every subsequent edit.

## Tier 2 — lighter pass. For non-asterisked OEs

- **Still sourced from the official PDF, still accurate. No shortcuts on correctness.** Tier 2 is
  less prose, never less true.
- Procedure steps state the requirement and the method clearly, **without** the extended
  reasoning and rationale paragraphs Tier 1 carries.
- Evidence column lists the records needed, without the exhaustive multi-clause detail.
- **Skip the deep cross-reference audit.** Do one quick check instead: does this OE's core subject
  matter clearly overlap something already approved? If yes, **flag it in one line** in this file
  for the reconciliation pass and move on. Do not investigate it fully before drafting.
- **Skip external best-practice fact-checking** unless something looks factually wrong on its
  face — in which case check it, because shipping a wrong clinical statement is not a Tier 2
  saving.

## What this rule does not do

- It does **not** retroactively change HIC.1–HIC.6. Those stay exactly as drafted, at uniform
  depth. Do not "downgrade" any of them to match this rule.
- It does **not** apply outside SHCO Full. ELC and HCO programmes are untouched by it; if master
  policies are ever built for those, the tiering question is decided separately for each.
- It does **not** relax any structural requirement. Every standard still gets the full control
  box, OE cross-reference table, abbreviations with the back-pointer, the eight numbered sections,
  the hash-checked disclaimer, `status = 'draft'`, the five optional sections left unset, and
  `policy_placeholder_audit.py` wired in from the first build. Tiering governs **depth of content
  per OE**, nothing else.

## Practical consequence for a standard with no asterisked OE

If a standard carries no asterisked OE at all, the whole standard is Tier 2. Say so explicitly in
its `universal_facts_checklist` so a later reader knows the shallower treatment was a decision
taken under this rule, not an omission.

---

# STANDING RULE: Disclaimer statute-matching (added 2026-08-17)

**Read this before drafting any master policy. It is a process rule, not a task — it does not
get ticked off and it does not expire.** Same standing as the two-tier depth rule above.

Paragraphs 1, 3 and 4 of the shared HIC.3–6 disclaimer stay byte-identical. Only paragraph 2
names statutes, and it names **only statutes that standard actually cites** in References.

- Never inherit Bio-Medical Waste Management Rules, 2016 or the Food Safety and Standards Act,
  2006 into paragraph 2 unless those statutes are genuinely used in that draft.
- Never dump the Consumer Protection Act, 2019, the Clinical Establishments Act, 2010, or the
  Mental Healthcare Act, 2017 onto a standard as a blanket checklist. That is the AAC.1
  defaulted-statute bug. Cite a statute only where that standard's subject actually engages it.
- If the PDF bibliography and the standard's subject support **no named Act**, use
  `make_disclaimer_accreditation_only()` in `policies/build/policy_build_common.py`. Paragraph 2
  then states that the duties are accreditation requirements of the NABH SHCO 3rd Edition, and
  explicitly refuses to import CPA 2019 / CEA 2010 / MHCA 2017 as a checklist.
- `emit_and_verify` hash-checks P1/P3/P4, requires `statute_clause` in P2, and fails if BMW/FSS
  appear in P2 unless they are also in `statute_clause`.

Every master policy's Disclaimer statutory paragraph (paragraph 2 of the four-paragraph block)
must name the statutes actually relevant to THAT standard's subject matter, cited from its own
References section — never inherited wholesale from a different chapter's boilerplate. Before
finalizing any new standard, check that the statutory paragraph names real, applicable law for
that specific document.

The rest of the disclaimer — structure, the four paragraphs, and the non-affiliation statement
including the bodies it names — stays consistent in wording and format across all standards.
Only the specific statutes named in paragraph 2 are checked and corrected per document.

**What this rule does not do**

- It does **not** retrofit HIC.1–HIC.6. Those already carry the Bio-Medical Waste Management
  Rules, 2016 / Food Safety and Standards Act, 2006 paragraph as known, accepted debt (correct
  for HIC.3's BMW content and HIC.3's kitchen/FSSAI content; wrong as a wholesale inherit for
  every HIC standard). Logged separately; not being retrofitted.
- It does **not** authorise rewriting paragraphs 1, 3 or 4 of the shared block in an individual
  file. A change to those paragraphs belongs in a deliberate pass across all masters.
- AAC.1 was drafted before this rule and still carries the HIC boilerplate in its approved row.
  The owner instructed a targeted disclaimer-only fix on 2026-08-17; until that edit lands, AAC.1
  is the one approved non-HIC document whose paragraph 2 names statutes it does not rely on.
  Subsequent AAC drafts (AAC.2 onward) follow this rule from the first build.

---

## Deferred from HIC.2 (drafted 2026-08-01)

### → HIC.1 / HIC.3 / HIC.6 (infection control programme, environment, sterilisation)

- [ ] **Cleaning, disinfection and sterilisation practices.** Disinfectant hierarchy
      (Spaulding critical / semi-critical / non-critical classification), high-level disinfection,
      choice of agent and contact times, validation. Not covered anywhere in the HIC.2 draft.
- [ ] **CSSD processes.** Instrument reprocessing cycle, load validation, biological and chemical
      indicators, sterile storage conditions, shelf life, recall procedure.
      NABH has a dedicated checklist for this: `E.-HIB_CHECK-04.13_CSSD-Checklist.docx`.
- [ ] **Laundry and linen processing.** Collection, segregation of soiled/infected linen, transport,
      wash parameters, storage and distribution of clean linen.
      See `E.-HIB_CHECK-04.19_Housekeeping-Laundry-Kitchen.docx`.
- [ ] **Environmental cleaning schedule.** Routine, enhanced and terminal cleaning frequencies by
      area, agents, responsibility and verification. HIC.2 draft references a Housekeeping SOP but
      does not define it.
- [ ] **Environmental surveillance.** OT air cultures, HEPA filter integrity checks, OT temperature
      and humidity monitoring, surface swab cultures. (Checklist rows 10-11, tagged HIC 1 c.)
- [ ] **The infection control manual itself** — its required contents and its update cycle.
      (Checklist rows 1, 2, 14.)

### → FMS (facility management and safety)

- [ ] **Potable water testing.** Routine water quality testing to confirm safe and potable supply.
      (Checklist row 12, tagged FMS 3 a.) Consider also dialysis water quality and Legionella
      control if the hospital runs dialysis.
- [ ] **Hazardous material spills other than blood/body fluids.** The HIC.2 draft now covers blood
      and body fluid spills only. Chemical, cytotoxic and mercury spills belong with FMS.
      (Checklist row 13 is tagged FMS 1 c, e and spans both.)

### → HIC.5 (surveillance)

- [ ] **Full HAI surveillance methodology.** VAP/VAE, CLABSI, CAUTI and SSI — standard case
      definitions, numerator/denominator collection, device-day counting, rate calculation,
      benchmarking and feedback loops.
      **Owner corrected 2026-08-06: this belongs to HIC.5** ("The organisation performs surveillance
      to capture and monitor infection prevention and control data") under SHCO 3rd Edition, not to
      CQI. The earlier CQI assignment came from the NABH checklist row 9 tag "CQI 2 a", which uses
      the older Entry-Level edition's numbering — the same caveat noted at the top of this file.
      **PSQ pass 2026-08-17:** CQI is the 2nd Edition chapter name. The 3rd Edition replacement is
      PSQ (Patient Safety and Quality Improvement), Chapter 6. They are not interchangeable. HAI
      **surveillance method** remains HIC.5. Hospital-wide **indicators** of infection-control
      activities are PSQ.2.b (drafted UNAPPROVED). `build_hic1.py` / `build_hic3.py` still say the
      method "belongs to CQI" — historical wording, not a 3rd Edition map. Do not patch approved
      HIC.1/HIC.3 in the PSQ insert pass.
      The HIC.2 draft carries a **brief pointer only**, by design — it names the four infection
      types and cites CDC NHSN as the definitions source, then defers method to the owning standard.
      The HIC.4 draft likewise covers bundle-compliance measurement only (a process measure HIC.4
      owns) and hands infection data to surveillance to be counted.
      Existing hook: the app's KPI module already carries SSI at `kpi_no` 52.

---

## Deferred from HIC.4 (drafted 2026-08-06)

- [ ] Reconcile PEP/immunisation content duplicated across HIC.2 and HIC.4 in a later consistency
      pass — not before all 6 HIC standards are drafted.
      Context: HIC.4.e (occupational health and safety practices) and HIC.4.f (post-exposure
      prophylaxis, the asterisked OE of the chapter) are the OEs that own this content, so the
      HIC.4 draft carries the full programme. The approved HIC.2 draft already carries hepatitis B
      immunisation, anti-HBs testing, HIV and HBV PEP timing, HCV management and exposure first aid
      as a spillover from HIC.2.d (safe injection). HIC.2 was deliberately **not** reopened.
      The HIC.4 scope section states the division: HIC.2 governs the practices that prevent an
      exposure, HIC.4 governs worker health and everything after an exposure occurs.

      **Specific divergences to resolve in that pass** (identified 2026-08-06, both documents left
      untouched — do NOT patch one without the other, and HIC.2 is approved so it is not reopened
      until the pass itself):

      **ITEMS 1 AND 2 DONE 2026-08-13** in the reconciliation pass. The antiseptic sentence is now
      byte-identical in HIC.2 step 24 and HIC.4 step 31 and states the CDC position in all three
      parts (verified against Kuhar et al., 2013, not taken from this file's summary). The HIV PEP
      window is now identical in both, HIC.2 having adopted HIC.4's wording as directed. See the
      new 2025-guideline item below for what this did NOT resolve. Original text follows.

      1. **Exposure first-aid: antiseptic wording.** (Was HIC.2 checklist flag 27, still open.)
         HIC.2 step 24: "Do not squeeze, scrub or apply a caustic agent such as bleach or
         antiseptic to the wound."
         HIC.4 step 31: "...no caustic agent, bleach, antiseptic or disinfectant is applied to it."
         Both group *antiseptic* with caustic agents and prohibit it outright. CDC's position is
         narrower and three-part: caustic agents (bleach) are not applied; antiseptic or
         disinfectant is not *injected into* the wound; and antiseptics generally have no evidence
         of reducing transmission — which is "not proven useful", not "prohibited". No clinical
         harm either way, since washing is what matters, but as written both documents may
         contradict local practice (povidone-iodine after washing is common in Indian protocols).
         Fix is roughly one sentence in each, worded identically. NOT drafted yet — deliberately
         deferred to the pass.

      2. **HIV PEP window: differing urgency.** Not a contradiction, but a reader comparing the
         two gets different emphasis.
         HIC.2 step 24: first dose "ideally within a few hours and certainly within 24 hours",
         not later than 72 hours.
         HIC.4 step 34: first dose "as soon as possible, ideally within hours... and preferably
         within two", not started beyond 72 hours.
         Both respect the 72-hour ceiling. HIC.4's is the tighter and better-supported framing and
         is the likely target wording for both.

      3. **HIC.3's placeholder inventory figure is wrong.** Its universal_facts_checklist says
         "HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] — 38 occurrences"; the real
         figure is 40 (39 exact-form plus 1 guidance-bearing variant, the intranet location in
         Distribution). Same class of error as HIC.4's since-corrected 48: the old counter matched
         only the exact string and so could not see "[Hospital to define — guidance]" forms.
         HIC.3 is approved and was deliberately NOT corrected on 2026-08-06 — fix it in this pass.
         `policies/build/policy_placeholder_audit.py` now reports the correct figure for all three;
         run `python policies/build/build_hic3.py` to reproduce it (the build scripts and their
         outputs moved into `policies/` on 2026-08-10; output paths are script-relative, so the
         command works from any working directory). Check HIC.1 at the same time: its checklist
         figure should read 25 (24 exact + 1 variant) — verify before assuming it is right.

      CLOSED 2026-08-06 — no longer part of this pass: HIC.2 checklist flag 26 (hepatitis C: no
      vaccine, no PEP, management is baseline plus follow-up testing with referral for treatment).
      Reviewed against both documents; they already agree and both are correct. The flag existed
      only because the point had not been searched in its own right, not because anything was in
      doubt. No text change required in either document.

- [ ] **Document version and revision history have no working data path.** INFRASTRUCTURE, not
      content — schema migration plus renderer change plus an edge function deploy. Deliberately
      NOT built on 2026-08-06; logged here so it is not lost.

      **The problem.** HIC.4's text was edited after it was approved (the step 7 nested-bracket
      fix and the step 31/34 placeholder normalisation, both on 2026-08-06). A generated document
      cannot show that, because:
      - `shco_policy_masters.version` is `integer NOT NULL DEFAULT 1`, so it cannot hold "1.1";
      - nothing reads or writes it — grep of both edge functions returns no hits, it is a dormant
        column;
      - there is no `revision_history` column at all;
      - `supabase/functions/_shared/policy-doc-template.ts` HARDCODES the version in the two
        places it appears: line ~206 (control box, `cell("1.0")`) and line ~219 (revision history
        row, `cell("1.0"), cell(today), cell("Initial release (AI-generated draft — review before
        use)")`).

      So bumping the integer today would be a no-op in the document — it would still print
      "Version 1.0" and "Initial release", which is the false statement the bump was meant to fix.
      The gap is in the template, not the data. Left at `version = 1` deliberately.

      **NOT URGENT:** no hospital has received a HIC.4 document. Rendering to date has been
      testing only.

      **Decisions already made (2026-08-06) — do not re-litigate when building:**
      - `version` becomes **text**, not numeric. Semantic versions are not numbers; "2.10" sorts
        wrong as numeric.
      - Revision history becomes a **jsonb column on the row**, not a child table. Six documents
        does not justify a separate table.

      **Also fix while in there:** the hardcoded revision-history description "Initial release
      (AI-generated draft — review before use)" is wrong for every human-reviewed master, not just
      HIC.4.

      **AND the author byline — merged into this item 2026-08-07, decision confirmed.** It is the
      same gap in the same file and must not become a second renderer pass: two passes would mean
      two deploys, two local-test cycles, and HIC.1–HIC.4 backfilled twice.

      Requested for HIC.5 on 2026-08-07: `Dr. Mehul Upadhyay · Healthcare Operations Leader`.
      Deliberately NOT built then, and HIC.5 was NOT held up for it. The reasons it cannot simply
      be written into the data today:
      - `shco_policy_masters` has no `byline` / `author` / `prepared_by` column. `approved_by`
        exists but is an approval-workflow field, is NULL across HIC.1–4, and must stay NULL on a
        draft row;
      - `policy-doc-template.ts` has no byline parameter. The control box hardcodes "Prepared By"
        as a blank signature line (~line 209); there is no author slot anywhere in the document;
      - **no master policy has ever carried it** — verified by querying every text column of the
        HIC.1, HIC.2, HIC.3 and HIC.4 live rows for the name. HIC.5 is not the odd one out.

      Storing it without rendering it would reproduce the dormant-`version`-column error described
      above: data present, document unchanged, and a false belief the job was done.

      **AND `updated_at` — merged into this item 2026-08-11, as agreed.** Third dormant column in
      the same row, same pass, same reason: it is the field a revision-history entry should be
      derived from or reconciled against, and today it cannot be trusted to say anything.

      Verified against the live table on 2026-08-11:
      - the column **already exists** — `updated_at timestamptz NOT NULL DEFAULT now()`. Unlike
        `version` (wrong type) and `revision_history` / `author_byline` (absent), nothing needs to
        be added. This one is a behaviour gap, not a schema gap;
      - **there is no trigger on the table at all** — `pg_trigger` returns zero non-internal rows
        for `shco_policy_masters`. So the default fires once on insert and nothing ever moves it;
      - consequently **all six rows have `updated_at` exactly equal to `created_at`**, to the
        microsecond, including HIC.4 — the row whose text was demonstrably edited after approval on
        2026-08-06, which is the very edit that opened this TODO. The column currently asserts that
        no master policy has ever been modified, which is false.

      So `updated_at` is dormant in the same way `version` is, and for a worse reason: `version` is
      at least honest about being untouched, whereas `updated_at` looks like a live audit field and
      is silently wrong. Do not build revision history on top of it until the trigger exists —
      a revision-history entry stamped from a frozen `updated_at` inherits the frozen date.

      **Decision (2026-08-11):** fix it with a `before update` trigger setting
      `new.updated_at = now()`, not by asking every caller to set it. Callers get missed; this
      table is written by SQL scripts, edge functions and hand-run statements alike.

      Two things to settle when building, both deliberately left open here:
      - **backfill.** The six existing rows' `updated_at` values are known-wrong for any row edited
        after insert. There is no record of the true edit timestamps, so either leave them and note
        it in the first revision-history entry, or set them from the revision history being written
        in this same pass. Prefer the latter — the pass is authoring that history anyway.
      - **whether the document renders it.** "Last updated" in the control box is useful, but it
        overlaps the revision-history table's own date column. Decide once; do not render the same
        date twice under two names.

      **To build, in the same pass as version and revision history:**
      1. migration: `alter table public.shco_policy_masters add column author_byline text;`
         (alongside `version` → text and the `revision_history` jsonb column)
      1a. same migration: the `updated_at` trigger — `create trigger ... before update on
         public.shco_policy_masters for each row execute function <set_updated_at>()` — plus the
         backfill decided above. No `add column` needed; the column is already there.
      2. `PolicyDocData` in `_shared/policy-doc-template.ts`: add `authorByline?: string`
      3. render it in the control box or immediately beneath it — not in the footer, which already
         carries hospital name, doc no. and the confidentiality mark
      4. pass it through in `generate-hospital-policy/index.ts` (and check
         `generate-policy-document/index.ts`, which builds its own `docNo` and may need it too)
      5. local test per CLAUDE.md — note the app is auth-gated, so the visual check needs the user
         to sign in
      6. deploy, then backfill HIC.1–HIC.5

      This supersedes the "Amendment Sheet" and "Rev. No." bullets in the cross-cutting section
      below, which describe the same gap in less specific terms, and it also absorbs the
      "Prepared By / Approved By / Responsibility of Updating signature block" bullet there.

---

## Deferred from HIC.5 (drafted 2026-08-07)

- [ ] **Reconcile the three overlaps HIC.5 creates with HIC.1, HIC.2 and HIC.3** in the same
      consistency pass as the HIC.2/HIC.4 item above — not before all 6 HIC standards are drafted.

      Context and instruction: three of HIC.5's OEs require content the approved documents already
      partly carry. On instruction (2026-08-07), following the HIC.4 precedent, **HIC.5 carries the
      full content for all three and HIC.1/HIC.2/HIC.3 were NOT reopened.** The HIC.5 scope section
      states each division explicitly. Do NOT patch one document without the other.

      **ITEMS 1, 2 AND 3 DONE 2026-08-13** in the reconciliation pass.
      Item 1: HIC.5 step 20 adopted HIC.2's "approximately 20 minutes, plus or minus 10", with a
      same-pass lock sentence so the two cannot drift again.
      Item 2: HIC.1 step 26 reduced to a pointer. NOTE two of its three sub-tasks were ALREADY DONE
      and this file was stale on both — the outbreak definitions were already byte-identical, and
      HIC.5 step 31 already read "on the same day it is suspected", not "on the day the suspicion
      arises" as recorded here. Only the pointer was outstanding. The HIC.1.a evidence column was
      re-pointed at the same time, since it had cited step 26's investigation records in full.
      Item 3: see the environmental-swab item below, now closed. Original text follows.

      1. **HIC.5.b (Core) vs approved HIC.2 step 9 — hand hygiene compliance monitoring.**
         HIC.2 step 9 already carries open direct observation, the actions-over-opportunities
         formula, stratification by cadre and area, handrub consumption per 1,000 patient days,
         feedback and re-audit. HIC.5 steps 19–21 add observer validation and revalidation,
         independence of observer from area, a minimum sample size with rate suppression below it,
         breakdown by moment, and dispenser availability as a third indirect measure.
         **Divergence:** HIC.2 states a session length ("approximately 20 minutes, plus or minus
         10"); HIC.5 step 20 deliberately states only "a defined and limited length", to avoid
         creating a second and potentially divergent number. Not a contradiction — one specific,
         one general. Likely target wording is HIC.2's, adopted in both.

      2. **HIC.5.d (Commitment, ASTERISKED) vs approved HIC.1 steps 25–26 — outbreaks.**
         HIC.1 step 26 ("Recognising and responding to an outbreak within the hospital") already
         defines an outbreak and sketches the response; step 25 covers notifiable disease
         reporting. HIC.5 steps 30–35 carry the full identification, investigation, control,
         closure and reporting programme. **HIC.5.d is the asterisked OE of the chapter's
         surveillance standard**, so the documented-evidence anchor must sit in HIC.5.
         **Divergence:** the two outbreak definitions are consistent in substance but separately
         worded — make them identical, and reduce HIC.1 step 26 to a pointer once HIC.5 is
         approved. Also align HIC.1's "report to the ICO on the same day it is suspected" with
         HIC.5 step 31's "on the day the suspicion arises" — same rule, different words.
         Note: HIC.1 owns *community* outbreaks/pandemics (HIC.1.d) and the statutory notification
         route; that split is correct and stays.

      3. **HIC.5.e (Core) vs approved HIC.3 steps 13–19 — housekeeping.**
         HIC.3.c owns adherence to the housekeeping procedure. HIC.5 steps 26–29 own whether it
         worked — three axes of measurement, a pre-defined high-touch surface list, objective
         thoroughness monitoring by fluorescent marker or ATP, the independence requirement, the
         pass-rate calculation, and restriction of environmental culturing to defined triggers.
         **THIS IS THE ONE REAL TENSION OF THE THREE, and the most important to resolve.**
         HIC.3 lists "environmental surface swab results" among its routine housekeeping evidence,
         while HIC.5 step 28 expressly does **not** perform routine untargeted surface culturing
         and restricts it to stated triggers (outbreak hypothesis, defined critical systems,
         post-construction clearance, suspected product contamination, health-authority direction).
         An assessor reading both will find HIC.3 promising a record HIC.5 says the hospital does
         not routinely produce. No clinical safety issue — nobody is harmed by an unnecessary swab
         — but the documents disagree. **HIC.5's position is the better-supported one** (CDC
         environmental infection control guidance: no established relationship to patient infection
         in general areas, no agreed action thresholds for most surfaces). Fix belongs in HIC.3.
         NOT drafted — deliberately deferred to the pass.

- [x] **Author byline — MERGED 2026-08-07 into the version/revision-history TODO above.**
      Decision confirmed: log it, do not build now; HIC.5 is not held up for it. The full context,
      the reasons it cannot be stored without a renderer change, and the six build steps now live
      with the version and revision-history work under "Deferred from HIC.4", because they are the
      same gap in the same file and belong in one pass. Nothing to do here — see that item.

- [x] **DONE 2026-08-13. HIC.3 narrowed to match HIC.5; contradiction closed.**
      Found in FOUR places, not the two logged here: (1) HIC.3.c evidence, (2) HIC.3 step 5's
      routine swab bullet, (3) HIC.3.a evidence "air AND SURFACE sampling", and (4) the
      checklist's own provenance note listing surface swabs as step 5 content. All four fixed.
      Step 5 keeps air, temperature/humidity, pressure and water sampling — HIC.5 step 28 routes
      those parameters back to HIC.3 and this file said "Do not move them". Placeholder count
      moved 40 -> 39 (routine swab interval removed); the checklist had also recorded it wrongly
      as 38, corrected in the same edit, which closes that separate item below.

      Original item retained for context.

- [x] ~~**HIC.3 promises a record the hospital does not routinely produce — environmental surface
      swabs.**~~ Discrete edit to HIC.3, broken out of the reconciliation item above so it is not
      lost inside it. Confirmed for logging 2026-08-07.

      **The contradiction.** HIC.3's OE mapping lists "environmental surface swab results" among
      the routine evidence for HIC.3.c (housekeeping procedures), and HIC.3 step 5 describes
      routine environmental sampling with repeat-sample confirmation. HIC.5 step 28 states that
      {{HOSPITAL_NAME}} does **not** perform routine untargeted environmental culturing, and
      restricts sampling to five defined triggers: an outbreak hypothesis naming the organism
      sought in advance; periodic monitoring of defined critical systems (OT air, dialysis water,
      potable water) on engineering or regulatory grounds; post-construction or post-repair
      clearance; suspected product/device/process contamination; and direction by the competent
      health authority.

      An assessor reading both documents will find HIC.3 offering a routine record that HIC.5 says
      is not routinely generated. Not a clinical safety issue — nobody is harmed by an unnecessary
      swab — but the two documents disagree in front of an assessor, which is the failure mode
      this file exists to prevent.

      **HIC.5's position is the better-supported one** and should win: CDC environmental infection
      control guidance does not recommend routine untargeted surface culturing, there is no
      established relationship to patient infection in general areas, and there are no agreed
      action thresholds for most surfaces. A low colony count is not evidence that cleaning is
      working, which is precisely the inference HIC.3's framing invites.

      **Fix belongs in HIC.3, not HIC.5.** Narrow HIC.3's HIC.3.c evidence list to the objective
      cleaning-outcome monitoring HIC.5 step 27 actually produces (fluorescent marker or ATP pass
      rates), and re-point HIC.3's environmental sampling text at the trigger list in HIC.5 step 28
      rather than describing it as routine. HIC.3 is approved and was deliberately NOT reopened on
      2026-08-07 — do it in the reconciliation pass.

      Note the same care applies in reverse: HIC.5 step 28 deliberately does **not** restate the
      parameters and frequencies for the critical-system monitoring (OT air, dialysis water,
      potable water). Those live in HIC.3 and the facility policies. HIC.5 receives and trends the
      results. Do not move them.

- [ ] **NEW 2026-08-13: the 2025 PHS guideline revision is not reflected in HIC.2 or HIC.4.**
      Found while fact-checking the PEP wording in the reconciliation pass. A 2025 revision exists:
      *2025 US Public Health Service Guidelines for the Management of Occupational Exposures to
      HIV*, Infect Control Hosp Epidemiol.

      **Two consequences, neither acted on, because both are new content rather than reconciliation.**

      1. The "preferably within two [hours]" figure now carried by BOTH documents is not in the 2025
         guideline, which says only "Initiate PEP as soon as possible, up to 72 hours following the
         occupational exposure to HIV". It was adopted across both on instruction to remove a
         divergence, which it did. It is not clinically wrong — earlier is better — but it must not
         be attributed to the current guideline. Both checklists now say so explicitly.
      2. The 2025 revision adds a recommendation NEITHER document carries: where an exposure beyond
         72 hours is thought to represent a high risk of transmission, consult a provider with
         expertise in HIV treatment, rather than treating 72 hours as an absolute cut-off. Both
         documents currently state 72 hours as absolute. Consider adding the consultation route.

      Decide whether to re-source the timing wording to the 2025 guideline and whether to add the
      >72-hour consultation route. Reopens HIC.2 and HIC.4 together — never one without the other.

- [ ] **Stop assuming the asterisked OE is the last one in the standard — check it per standard.**
      Logged 2026-08-07 as a process note for HIC.6 and for any future chapter.

      In HIC.4 the asterisk (`doc_required = true`) sat on the final OE, HIC.4.f. In **HIC.5 it
      sits on HIC.5.d** — "The organisation identifies and takes appropriate action to control
      outbreaks of infections" — and **not** on HIC.5.f. Verified against the official SHCO 3rd
      Edition PDF (printed p.95) and against `shco_full_oes`; both agree, and HIC.5.d is the only
      asterisked OE in the standard.

      **Why it matters for drafting.** The asterisked OE is the documented-evidence anchor of the
      standard, and it decides which block of the procedure gets the deepest treatment and the
      fullest evidence column. HIC.5's draft puts its heaviest content at steps 30–35 (outbreaks)
      for exactly this reason. Had the HIC.4 pattern been assumed, the weight would have landed on
      the analysis-and-feedback block instead and the standard's evidence anchor would have been
      under-built.

      **Do this for HIC.6 before drafting:** query
      `select oe_code, level, doc_required from public.shco_full_oes where oe_code like 'HIC.6%'`
      **and** confirm against the PDF, rather than inferring from position — and rather than
      trusting either source alone. Doing exactly that on 2026-08-07 turned up the next item.

      **Updated 2026-08-10.** The whole table has now been audited against the PDF and corrected,
      so `doc_required` is trustworthy for every chapter with one known exception — `HIC.2.c`, left
      `false` deliberately (see the item under "Deferred from the asterisk audit"). The
      position-inference warning above still stands: the flag now tells you *which* OE anchors the
      evidence, and it is regularly not the last one. **HIC.6 is asterisked on b, c, d and e** —
      four of five OEs — so its draft cannot lean on a single anchor block.

- [x] **CLOSED 2026-08-10 — DATA ERROR: `shco_full_oes` was missing the asterisk on HIC.6.e, and
      on 13 other OEs across six chapters.** Logged 2026-08-07; full ten-chapter audit run and
      applied 2026-08-10.

      **What the audit did.** Every one of the 408 OEs was read from the official SHCO 3rd Edition
      PDF (`C:/Users/SERVER/Desktop/NABH/SHCO-Standards-3rd-Edition.pdf`) as a complete block —
      opening line plus every wrapped continuation line — and its asterisk compared against
      `doc_required`. No flag was inferred from position, level or pattern. Reproducible via
      `python scripts/asterisk_extract.py --sql` (see the note at the end of this item).

      **Result: 14 mismatches, every one in the same direction** — `doc_required = false` where the
      PDF carries an asterisk. **Zero** OEs were flagged `true` without an asterisk to support it.

      | Chapter | OEs | PDF asterisks | DB was `true` | Mismatches |
      |---------|----:|--------------:|--------------:|-----------:|
      | AAC     |  48 |            18 |            16 |          2 |
      | COP     |  82 |            33 |            27 |      **6** |
      | MOM     |  52 |            23 |            21 |          2 |
      | PRE     |  39 |             6 |             6 |          0 |
      | HIC     |  36 |            18 |            16 |          2 |
      | PSQ     |  28 |             6 |             6 |          0 |
      | ROM     |  19 |             6 |             6 |          0 |
      | FMS     |  29 |             9 |             9 |          0 |
      | HRM     |  45 |             4 |             4 |          0 |
      | IMS     |  30 |             9 |             7 |          2 |
      | **Total** | **408** | **132** | **118** | **14** |

      PRE, PSQ, ROM, FMS and HRM are clean in both directions. The three HIC.5 flags and six HIC.4
      flags verified during those drafts were confirmed correct.

      **13 applied 2026-08-10** (`doc_required` false → true), on instruction:

      `AAC.2.d`, `AAC.5.e`, `COP.2.c`, `COP.5.c`, `COP.7.a`, `COP.8.f`, `COP.10.f`, `COP.13.c`,
      `HIC.6.e`, `IMS.2.b`, `IMS.4.e`, `MOM.5.f`, `MOM.7.a`

      Post-state verified: 132 PDF asterisks, 131 rows `doc_required = true`, 0 rows `true` without
      a PDF asterisk, and `HIC.2.c` the single remaining deliberate `false`.

      **1 deliberately NOT applied: `HIC.2.c`** — see its own item below. HIC.2 is approved and was
      drafted against the old flag, so the flip belongs in the reconciliation pass, not here.

      **Two findings worth carrying forward.**

      1. **The wrapped-line theory only explains half of them.** Seven of the 14 had the asterisk on
         a wrapped second or third line (AAC.2.d, COP.8.f, COP.10.f, COP.13.c, HIC.6.e, IMS.2.b,
         IMS.4.e) — the HIC.6.e failure mode. The other seven sat on a single unwrapped line
         (AAC.5.e, COP.2.c, COP.5.c, COP.7.a, HIC.2.c, MOM.5.f, MOM.7.a). The original extraction
         was lossy in more than one way, so **pattern-based spot-checking would have missed them**.
         Whole-table comparison is the only safe method; do not sample.
      2. **`IMS.2.b` is a Core OE** — the only Core element among the 14. Medical-record contents is
         an OE an assessor will always ask a document for, and it carried no documented-evidence
         flag until 2026-08-10. Anything drafted against IMS before that date is under-evidenced
         there.

      **Reproducing it.** `scripts/asterisk_extract.py` (added 2026-08-10) parses the PDF and
      self-validates before its output can be trusted: OE count must be 408, the code set and every
      OE's level must agree with `scripts/shco_oes_data.json`, and no OE block may run long. It
      exits non-zero and refuses to vouch for its output if any check fails. `--sql` emits the
      two-way comparison query against `shco_full_oes`.

      Two parser traps it now guards, both of which produced wrong answers on the first pass:
      - the book's standard headers are inconsistent (`HIC.6.` alone, `MOM.3. <text>`, and
        `COP 1. <text>` — a space, no dot). Matching only the first form silently drops all of COP;
      - each chapter ends with a References list, which the chapter's last OE swallows unless the
        parse is cut there. That produced **false positives on AAC.8.g and IMS.6.e** — both are
        correctly `false` and were not touched.

      Note the stale path in `scripts/extract_shco_book.py` (`/home/ubuntu/...`) does not resolve on
      this machine; `asterisk_extract.py` carries the working path and accepts `--pdf`.

---

## Deferred from the asterisk audit (2026-08-10)

- [x] **DONE 2026-08-13. `HIC.2.c` asterisk/flag divergence closed: anchor built, flag flipped.**
      The anchor was built by EXPANDING steps 15 and 19 in place (no step inserted, so the six
      internal cross-references and every `steps` mapping stayed valid). Step 15 gained the
      consolidated PPE-by-category list and a periodic category-review cadence; step 19 gained
      eleven fact-checked discontinuation criteria from CDC Appendix A (version 2 February 2025),
      recorded as checklist facts 42-52. `doc_required` is now true. Verified: `shco_full_oes`
      and `scripts/shco_oe_asterisks.json` now agree exactly — 132 true / 276 false / 408 total
      on both sides. There is no longer any known OE where the table disagrees with the PDF.
      NOTE: this item OVERSTATED the gap. Isolation signage and the category-assignment register
      already existed in step 15; only the PPE matrix, the review cadence and the durations were
      genuinely missing.

      Original item retained below for context.

- [x] ~~**`HIC.2.c` is asterisked in the PDF but left `doc_required = false` — flip it in the
      reconciliation pass, and add the evidence anchor at the same time.**~~ Broken out of the
      closed audit item above so it is not lost inside it. Deferred on instruction 2026-08-10;
      the other 13 corrections were applied that day.

      **The finding.** The official SHCO 3rd Edition PDF, printed p.93 (PDF page index 99), carries
      an asterisk on HIC.2.c:

      > `Commitment c. The organisation adheres to transmission-based precautions.*`

      Single unwrapped line, asterisk glued to the full stop. `shco_full_oes` has `false`.

      **Why it was held back.** HIC.2 is **approved** and its master policy was drafted on
      2026-08-01 against the old flag. Same rule as everywhere else in this file: an approved
      document is not reopened outside the reconciliation pass, and the flag and the document must
      move together. Flipping the flag alone would leave the app telling a hospital that HIC.2.c
      needs documented evidence while the generated HIC.2 policy contains no anchor for it.

      **What flipping it actually requires — this is the part that is easy to miss.** HIC.2.c needs
      a **documented-evidence anchor in the HIC.2 master that does not exist today.** The approved
      draft treats transmission-based precautions as ordinary Commitment content: it names contact,
      droplet and airborne precautions inside the standard-precautions material, but there is no
      block built to carry an evidence column an assessor can be walked through — no isolation
      signage and category-assignment record, no PPE-by-category matrix, no duration-of-precautions
      and discontinuation criteria, no record of who assigns and reviews the category per patient.
      That block has to be **written**, not merely flagged. Budget it as a HIC.2 content edit, not
      a one-line data change.

      **Do it in the same pass as** the three HIC.5 overlaps and the HIC.2/HIC.4 PEP divergences
      above — all of them reopen HIC.2, and it should be reopened once.

      **The flag itself, when the content is ready:**
      `update public.shco_full_oes set doc_required = true where oe_code = 'HIC.2.c';`

      Until then `HIC.2.c` is the **only** OE in the table that knowingly disagrees with the PDF.
      If a future audit reports exactly one mismatch and it is this one, that is the expected state
      — not a regression.

---

## Deferred from the Required Records / version infrastructure pass (2026-08-11)

- [x] **DONE 2026-08-13. HIC.1 and HIC.2 evidence + responsible authored and applied.**
      HIC.1: 89 records across 6 OEs. HIC.2: 117 records across 7 OEs, HIC.2.c carrying 40 as the
      Tier 1 asterisked element. All six HIC standards now render the Required Records section and
      the four-column OE Cross-Reference table. Every field hash-verified against the live rows
      after applying. Build scripts: `policies/build/hic1_oe_evidence.py`,
      `hic2_oe_evidence.py`, `hic2_tbp_anchor.py`, `apply_oe_evidence.py`, `apply_hic2.py`.

      TWO THINGS WORTH CARRYING FORWARD.
      (a) LINE ENDINGS DIFFER PER ROW. HIC.1 stores CRLF; HIC.2 stores LF. Neither is wrong, but
      a hash comparison against a local draft fails confusingly unless normalised, and writing the
      wrong convention corrupts the row. Check per row before comparing or writing.
      (b) NEVER USE str.format() ON TEMPLATE TEXT. It collapses `{{HOSPITAL_NAME}}` to
      `{HOSPITAL_NAME}`, which the renderer does not substitute and prints literally. This reached
      the local HIC.2 draft and was caught only by the post-apply hash check. `apply_hic2.py` now
      carries a placeholder-integrity guard that fails the build on any single-braced token.

      Original item retained below for context.

- [x] ~~**AUTHORED-CONTENT DEBT: HIC.1 and HIC.2 have no evidence or responsible data at all, so
      they render no Required Records / Evidence Checklist section. This is missing CONTENT, not a
      missing feature.**~~ Confirmed on instruction 2026-08-11. Do it in the reconciliation pass,
      which already reopens HIC.2.

      **Read this before concluding the Required Records feature is "done".** The feature works;
      it is live in `policies/build/render_previews.ts` and in the shipping template. It renders
      for HIC.3, HIC.4, HIC.5 and HIC.6. It renders **nothing** for HIC.1 and HIC.2, and the
      section is omitted entirely rather than printed empty. A reader opening the HIC.1 document
      will not see a gap — they will see a document that simply has no records section, which
      looks deliberate and is not.

      **The actual state of the data.** Every `oe_mapping` entry in HIC.1 and HIC.2 carries only
      three keys — `oe_code`, `requirement`, `steps`. HIC.3-HIC.6 carry five, adding `evidence`
      and `responsible`. Verified against both the live rows and the draft files, so it is how
      those two were authored, not a load or migration fault.

      | Standard | OEs | OEs with evidence | Records rendered |
      |----------|----:|------------------:|-----------------:|
      | HIC.1    |   6 |             **0** |         **none** |
      | HIC.2    |   7 |             **0** |         **none** |
      | HIC.3    |   6 |                 6 |               40 |
      | HIC.4    |   6 |                 6 |               62 |
      | HIC.5    |   6 |                 6 |               73 |
      | HIC.6    |   5 |                 5 |               69 |

      **Second effect, easy to miss:** the same gap also drops the **Responsible** column from
      those two documents' OE Cross-Reference tables. The trimmed table renders four columns when
      `responsible` data exists and falls back to three when it does not, so HIC.1 and HIC.2 lose
      the ownership column as well. Both symptoms have the same single cause and the same fix.

      **Why it was not fixed in that pass.** Authoring evidence and responsible values for 11 OEs
      is writing new content into two approved documents. The pass was explicitly scoped to
      reformatting existing content and to infrastructure, and the standing rule is that an
      approved document is not reopened outside the reconciliation pass.

      **What the fix actually costs.** Roughly 40-70 records per standard judging by HIC.3-HIC.6,
      so 11 OEs is a real authoring job, not a data-entry one — each record has to be the evidence
      an assessor would actually be shown for that OE, traceable to the procedure steps already
      written. Budget it as content work. Note HIC.2 is being reopened in that pass anyway for the
      `HIC.2.c` transmission-based-precautions evidence anchor; **do both in one edit**, since the
      HIC.2.c anchor will itself need evidence records that belong in this same structure.

---

## Deferred from the drafting-order review (2026-08-11)

- [ ] **DATA ERROR: `MOM.5.standard_text` is wrong — it is a verbatim copy of MOM.3's. Fix it
      before anyone drafts MOM.** Found 2026-08-11 while counting OEs and asterisks per standard
      to choose the seventh master policy. Logged, deliberately NOT fixed that day.

      **The error.** Both `scripts/shco_oes_data.json` and the live `public.shco_full_oes` carry:

      > `MOM.3` → "Medications are prescribed safely and rationally."
      > `MOM.5` → "Medications are prescribed safely and rationally."

      Identical strings. MOM.3's is correct. MOM.5's is not: its six objective elements are
      unambiguously about **dispensing**, not prescribing —

      | OE | Level | Text |
      |----|-------|------|
      | MOM.5.a | Commitment | Dispensing of medications is done safely. |
      | MOM.5.b | Commitment | Medication recalls are handled effectively. |
      | MOM.5.c | Commitment | Near-expiry medications are handled effectively. |
      | MOM.5.d | Core | Dispensed medications are labelled. |
      | MOM.5.e | Core | High-risk medication orders are verified before dispensing. |
      | MOM.5.f | Commitment | Return of medications to the pharmacy is addressed. |

      The OE rows themselves are fine. **Only the standard-level text is wrong**, and it is wrong
      in both the JSON and the database, so the two agree with each other and a consistency check
      between them will not catch it. The chapter reads as though it covers prescribing twice and
      dispensing never.

      **Why it matters more than a cosmetic typo.** The standard text is what a master policy
      carries in its header and what the OE cross-reference table restates. Drafting MOM.5 from the
      stored text would produce a dispensing policy titled and scoped as a prescribing policy —
      the same class of failure as the HIC.6.e asterisk, where trusting the stored value produced
      an under-built document. MOM.5 is also **5-of-6 asterisked**, the densest Tier 1 standard in
      the chapter, so it is the last place to start from a wrong premise.

      **PDF read 2026-08-17 (MOM.5 drafted; database still NOT fixed).** The official SHCO 3rd
      Edition PDF (August 2022, md5 `39e3bc86d73d651b9cfef283bbf018a9`) carries TWO headers:

      - Chapter SUMMARY printed p.75 (PDF page index 81): **"MOM.5. Medications are dispensed in
        a safe manner."** — this is the correct subject.
      - Standard+OE listing printed p.78 (PDF page index 84): **"MOM.5. Medications are prescribed
        safely and rationally."** — byte-identical to MOM.3's header on printed p.77. The six OEs
        on that same page are all about dispensing.

      The stored `standard_text` copied the **OE-page typesetting error**, not a unique invention
      in the JSON. The chapter-summary line is the wording the data-fix should apply. The MOM.5
      master was drafted from that summary line plus the six dispensing OEs; it does **not** use
      the corrupted header as its title. Do not treat the OE-page header as authoritative when
      applying the fix.

      **Scope of the fix when it is made:** `scripts/shco_oes_data.json`,
      `scripts/shco_oes_by_chapter.json` (same text, denormalised per OE row) and the
      `standard_text` column on all six `MOM.5.*` rows in `shco_full_oes`. Check the same day
      whether any other standard shares its text with a neighbour — this was found by eye while
      reading a table, not by a check that would have caught a second instance. A one-line
      `group by standard_text having count(distinct standard_code) > 1` over the whole table
      settles it for all 408 OEs at once. The MOM.5 master draft is already titled and scoped as
      dispensing; the data-fix does not reopen that draft unless the stored text is later used
      to regenerate the header.

      The data-fix remains a **separate pass**. The 2026-08-17 MOM drafting pass did not write
      `shco_full_oes`.

---

## Deferred from AAC.1 (drafted 2026-08-17)

- [ ] **When the HRM credentialing standards are drafted, check AAC.1.b for a natural
      cross-reference point.** Flagged by the owner on 2026-08-17 at AAC.1 approval — a note for
      the future, NOT an overlap today, since no HRM master exists yet.

      Context: AAC.1.b requires each defined service to be backed by "suitably qualified
      personnel" providing out-patient, in-patient and emergency cover. The AAC.1 draft (step 2,
      Scope, and the AAC.1.b evidence column) deliberately relies on "the human resource
      policies of {{HOSPITAL_NAME}}" for the verification method and does not restate it — one of
      the three forward references recorded in the AAC.1 universal_facts_checklist item 3.
      When the HRM chapter's credentialing standards are drafted, verify which HRM standard
      actually owns qualification verification against the PDF (do not assume the standard
      numbers), make its scope state the division explicitly — AAC.1 defines the services the
      personnel must stand behind, HRM owns how their qualifications are verified — and check
      whether AAC.1's generic "human resource policies" wording should be sharpened to name the
      real policy title, the same resolution pattern HIC.3/HIC.4's forward references to the
      then-undrafted HIC.6 followed.

---

## Deferred from COP.2 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.2 draft Scope / universal_facts_checklist). Do not patch the approved HIC.1 or the unapproved AAC.2 in this pass — reconcile when the owning document is next opened.

- [ ] **Reconcile AAC.2.e vs COP.2.c — triage ownership (access prioritisation vs emergency care
      initiation)** in a dedicated consistency pass once more COP/AAC chapters are drafted — not in
      this COP insert pass.

      Context and instruction: two unapproved drafts both write a "triage or prioritisation" method
      that applies at the emergency area. AAC.2.e (Achievement, asterisked) owns **ACCESS** —
      prioritisation of access to the organisation's healthcare services according to clinical need.
      COP.2.c (Commitment, asterisked) owns **INITIATION OF APPROPRIATE CARE** in the emergency area
      — a system of triage that guides when and how emergency care starts. On instruction
      (2026-08-17), following the HIC.4/HIC.5 precedent, **COP.2 carries the full ED clinical triage
      block and AAC.2 carries the hospital-wide access-prioritisation block; neither was patched in
      the other's pass.** Both Scope sections state the division. Do NOT patch one without the other,
      and do not approve one without checking the other's live wording.

      **Specific divergences to resolve in that pass** (identified 2026-08-17, both documents left
      untouched):

      1. **Shared tool risk — one poster, two owners.** AAC.2 step 6 requires a triage or
         prioritisation method "at minimum the emergency area and the out-patient department", with
         categories, written criteria, trained appliers, recorded category against the UID, and
         "expected time-to-assessment per category". COP.2 step 3 requires a written triage system
         that "guides initiation of appropriate emergency care", with category, time of assignment,
         and evidence that the category "changed what happened next — pathway, clinician called,
         space used — rather than a stamp followed by a single queue". A hospital that uses one local
         scale for both will be reading one document in the emergency area and another assessor will
         read the other. **Likely resolution:** either (a) one shared local tool referenced
         identically in both, with AAC.2 owning OPD + access order and COP.2 owning ED
         care-initiation pathways, or (b) two explicitly linked documents where the ED system is a
         child of the access method. Either way the cross-reference must be byte-stable in Scope,
         step text and evidence columns.

      2. **OPD queuing vs ED clinical pathways.** AAC.2.e's method determines "the order in which
         patients are seen" at OPD and states expected time-to-assessment. COP.2.c does not set OPD
         queuing and must not be read as taking it over. Conversely, AAC.2.e must not silently own
         ED clinical pathways — life-threatening emergency "is not queued" in AAC.2, but initiation
         of appropriate care (which clinician, which space, which protocol) is COP.2's act.
         **Divergence to watch:** if AAC.2's evidence column lists "sample spanning emergency and
         out-patient" and COP.2's lists "pathway, clinician called, space used", an assessor may ask
         why the ED record satisfies AAC.2 but not COP.2 or vice versa. Align the evidence ask so ED
         records are cited under COP.2 for care initiation and under AAC.2 only for access-order
         proof if the hospital uses a single tool.

      3. **Time-to-assessment is an AAC.2 numeric, not a COP.2 mandate.** AAC.2 step 6 carries
         "[Hospital to define — the expected time-to-assessment for each priority category]". COP.2
         step 3 deliberately does **not** import ESI level times or any other published waiting-time
         table as a NABH mandate, and step 4 states "This document does not set a mandatory number
         of minutes" for waiting reassessment. **Do not let AAC.2's hospital-defined
         time-to-assessment be read back into COP.2 as a numeric compliance target**, and do not let
         COP.2's silence on minutes be read as permission to drop AAC.2's access-time commitment.
         The reconciliation pass should add an explicit lock sentence in both Scopes if needed.

      4. **Re-triage while waiting.** AAC.2 step 6: "re-applied if the patient's condition changes
         while waiting." COP.2 step 4: waiting reassessment with interval "[Hospital to define]",
         re-triage under step 3 if category worsens. Not a contradiction — AAC.2 owns the
         access-priority change, COP.2 owns the waiting patient in the ED — but the intervals and
         record fields should not diverge if one tool is shared.

      CLOSED for this pass: COP.2 Scope and step 3 already state AAC.2.e is hospital-wide access
      prioritisation even when the local tool is shared; AAC.2 Scope hands "life-stabilising
      treatment" and emergency clinical content to emergency-care policies. No text change until the
      dedicated pass.

- [ ] **HIC.1.d vs COP.2.k operational disaster/epidemic plan.** HIC.1 is approved. HIC.1 step 24 already contains operational surge, entrance screening, continuation of essential services, command structure and drill language for community outbreaks/pandemics. COP.2.k now owns the hospital's all-hazards OPERATIONAL plan (activation, command, disaster triage, surge, continuation of essential services). HIC.1.d should keep IPC response, IEC and statutory notification. Do not patch HIC.1 until a dedicated reconciliation pass; the COP.2 Scope states that HIC.1 step 24 is not a substitute and that the two documents must not name two epidemic activators who do not know of each other.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.2.e ED episode note vs AAC.8 leaving-the-organisation summary vs AAC.2.f between-org transfer note.** COP.2 Scope states the split; AAC.8 Scope does not yet name the COP.2 emergency note.

- [ ] **COP.2.d waiting-patient reassessment in ED vs AAC.3.d interval reassessment vs AAC.3.e ward early-warning.** Stated in COP.2 Scope; not a contradiction.

- [ ] **COP.2.a identified emergency area vs AAC.1.b emergency cover of a defined specialty.** Place vs resourcing; stated in COP.2 Scope.

- [ ] **COP.2.g DOA / death within minutes vs AAC.8 death case-summary vs RBD Act statutory certificate.** Step 7 states the split.

- [ ] **COP.2.h–i ambulance vs AAC.2.f transfer vehicle vs AAC.7 internal move vs MOM emergency-medication process vs HIC.6 device reprocessing.** Forward-refs in steps 8–9; pick up when MOM/COP.3/FMS are drafted.

- [ ] **COP.2.j in-transit treatment / ambulance-to-ED receipt vs AAC.7 unit-to-unit handover** (Reay 2019, chapter ref 45). Stated in step 10.

---

## Deferred from COP.8 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.8 draft Scope / universal_facts_checklist). Do not patch approved HIC or AAC in this pass.

- [ ] **COP.7.e neonatal backup vs COP.8.b neonatal care method.** COP.7 owns that obstetric service has human resources and facilities for neonates of high-risk cases. COP.8 owns how neonates and children are cared for against named national/international guidelines. Both Scopes and COP.8 step 3 state the split. Reconcile wording if either document is reopened.

- [ ] **AAC.2 UID vs COP.1 two identifiers vs COP.8 point-of-care ID and neonate-mother matching.** AAC.2 generates the unique identification number. COP.1 owns the two-identifier rule. COP.8 applies those identifiers to the child and adds matching of the neonate to the mother or designated guardian. COP.8 does not issue the number and does not rewrite the two-identifier rule.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.8.c age-specific competency vs HRM credentialing method.** This requires the competency; HRM (undrafted) verifies it.

- [ ] **COP.8.e paediatric nutrition/growth/dev/immunisation assessment vs AAC.3 hospital-wide assessment vs COP.13 nutrition screen vs COP.7.c maternal nutrition vs HIC.3 kitchen.** COP.8 Scope and step 6 state the split.

- [ ] **COP.8.f abduction/abuse care-process vs FMS building security.** COP.8 owns matching, handing-over, nursery access and the missing-child/abuse response; FMS (undrafted) owns locks/cameras/hardware.

- [ ] **HIC.3 BMW of neonatal waste.** Pointed; four colours not restated. Not a method overlap.

---

## Deferred from COP.9 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.9 draft Scope / universal_facts_checklist).

- [ ] **COP.9 procedural sedation vs COP.10 anaesthesia.** Sedation is not general anaesthesia. Both Scopes state: this document does not write the other; unplanned/intended general anaesthesia is COP.10, not a stretched COP.9. Post-sedation recovery is COP.9.e; post-anaesthesia recovery is COP.10.f — sibling recovery processes, not one form unless the hospital writes them so.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.9.b sedation consent before the drug vs PRE general consent method.** PRE.3 (drafted 2026-08-17, UNAPPROVED) now owns how consent is explained, recorded and who may give it. COP.9.b still owns that sedation consent is obtained before the sedative is given. Do not rewrite COP.9; the PRE.3 draft accepts this handoff.

- [ ] **COP.9 vs MOM drug-storage (NDPS / D&C).** Forward-ref. COP.9 does not write cupboard/register/destruction and does not inherit NDPS as a storage statute.

- [ ] **COP.9 vs COP.11 procedure/WHO checklist.** COP.9 owns the sedation given so a procedure can be performed; COP.11 owns the procedure. Stated in COP.9 Scope.

- [ ] **HIC.4 "sedation" hits (ICU ventilator sedation scale / daily interruption).** Incidental; not this document.

---

## Deferred from COP.10 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.10 draft Scope / universal_facts_checklist).

- [ ] **COP.9 sedation vs COP.10 anaesthesia vs COP.11 surgery.** COP.9 owns procedural sedation; COP.10 owns the anaesthetic (plan, monitoring under anaesthesia, post-anaesthesia recovery); COP.11 owns the surgical procedure, site-marking, WHO-framework checklist and operation notes. They meet in the theatre; they are not the same document.

- [ ] **HIC.6 anaesthesia equipment reprocessing.** COP.10 requires processed circuits/masks/blades; HIC.6 owns the cycle, indicators and recall. Stated in COP.10 Scope and step 1.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.10.d anaesthesia consent vs PRE general consent method.** PRE.3 (drafted 2026-08-17, UNAPPROVED) now owns the method. COP.10.d still owns that anaesthesia consent is obtained before induction. Do not rewrite COP.10; the PRE.3 draft accepts this handoff.

- [ ] **COP.10.g type+drugs in the record vs MOM medication process.** MOM (undrafted) owns storage and the medication process; COP.10 owns anaesthetic care and that type and anaesthetic medicines appear in the patient record. MOM must not restate anaesthetic method.

- [ ] **COP.10.e monitoring under anaesthesia vs HIC.4 SSI-bundle temperature/glycaemia.** Bundle stays HIC.4 even when the anaesthetist is the person who maintains those variables.

- [ ] **COP.10.h intra-operative adverse anaesthesia events vs PSQ.5 incident system now landed.** COP.10.h still owns that anaesthesia events are recorded and reviewed in the anaesthetic process. PSQ.5 (drafted 2026-08-17, UNAPPROVED) owns the hospital-wide incident system. Dual entry when the event meets this hospital's incident definition. Do not patch COP.10 in this pass.

---

## Deferred from COP.11 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.11 draft Scope / universal_facts_checklist). Do not patch approved HIC.4/HIC.5/HIC.6 in this pass — reconcile when the owning document is next opened.

- [ ] **HIC.4 SSI bundle vs COP.11 surgical process — shared surgical-safety checklist artefact.** HIC.4 evidence already lists "completed surgical safety checklist" as SSI-bundle evidence. COP.11.d (asterisked Core) owns the checklist as the team's pause (WHO Safe Surgery 2009 as framework; hospital checklist is [Hospital to define]; WHO items not pasted as mandated verbatim). Completing a checklist is not completing the SSI bundle; running the SSI bundle is not marking the site. HIC.4 should keep antibiotic timing, hair, glucose, skin prep, normothermia as IPC process. Do not patch HIC.4 until a dedicated pass.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.11.e standard precautions in OT vs HIC.2.** Follow HIC.2; do not rewrite PPE. Stated in COP.11 Scope and step 5.

- [ ] **COP.11.h process QA vs HIC.5 SSI surveillance.** Process look vs outcome look / NHSN definitions. Stated in step 8.
- [ ] **COP.11.h unit QA vs PSQ.1 hospital-wide QI programme now landed.** Theatre QA remains COP.11.h. PSQ.1 (drafted 2026-08-17, UNAPPROVED) owns the hospital-wide programmes. Unit findings may feed PSQ.1; they do not replace it.

- [ ] **COP.11.g sterile sets available vs HIC.6 instrument reprocessing.** Availability vs the decontamination cycle. Stated in step 7.

- [ ] **COP.11 OT episode vs AAC.7 transfer into/out of OT.** COP.11 owns what happens after the patient is received.

- [ ] **COP.11 vs COP.9 sedation vs COP.10 anaesthesia.** Surgery / site / checklist / notes vs sedation vs the anaesthetic. Stated in all three Scopes.

- [ ] **COP.11.i/j transplant and donation-awareness vs COP.6 brain-death / EOL pathway.** THOA 1994 envelope here; clinical declaration pathway remains COP.6.

- [ ] **COP.11 OT waste vs HIC.3 BMW.** Not named in COP.11 P2. Anatomical/OT waste remains HIC.3.

---

## Deferred from COP.12 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.12 draft Scope / universal_facts_checklist). HIC does not own falls, pressure ulcers, VTE or restraints.

- [ ] **AAC.3 assessment dataset vs COP.12 risk programmes.** AAC.3 may collect risk factors for falls, pressure injury, thrombosis or vulnerability. COP.12 owns the tools, measures and review. Completing an assessment checkbox is not running this programme.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.12.b care-environment for the vulnerable patient vs FMS building security.** Locks, CCTV and fabric remain FMS (undrafted). COP.12.b is bedside observation, call method, accompaniment, noticing a missing patient.

- [ ] **COP.12.c falls / COP.12.d pressure ulcers / COP.12.e DVT vs AAC.3.** Same split as the T1 AAC.3 flag; programmes owned here.

- [ ] **COP.12.d wound-dressing asepsis vs HIC.2 / HIC.4.** HIC owns dressing practice where already written; COP.12 owns the pressure-injury programme.

- [ ] **COP.12.e pharmacological VTE prophylaxis vs MOM anticoagulant-as-medication.** Indication here; drug process remains MOM (undrafted).

- [ ] **COP.12.f chemical restraint vs MOM.** Physical/mechanical restraint and seclusion here; chemical restraint as a medication process is MOM, not an undeclared substitute.

- [ ] **COP.12 vs COP.8 child abduction/abuse.** If children are a vulnerable category, COP.12 still owns the vulnerability programme and does not rewrite COP.8.f.
- [ ] **COP.12 bedside vulnerable/falls/PU/VTE programmes vs PSQ.1.c organisation-level proactive risk analysis now landed.** COP.12 owns the bedside tools. PSQ.1.c is quality-system analysis before harm. PSQ.5 is after-the-fact incidents. ROM.4.a (drafted 2026-08-17, UNAPPROVED on `cursor/draft-rom1-rom4-unapproved-9324`) is management ensuring organisation-wide proactive risk. Do not collapse these four. Do not patch COP.12 in this pass.

---

## Deferred from COP.13 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.13 draft Scope / universal_facts_checklist). Do not patch approved AAC.1 or HIC.3 in this pass.

- [ ] **AAC.1 service directory vs COP.13.c rehabilitation scope.** AAC.1 owns whether rehab is a defined service. COP.13.c (asterisked) requires the COP.13 scope to match that definition, including a recorded absence if the directory has no rehabilitation. A copied rehab SOP must not create a service the directory declined.

- [ ] **HIC.3 kitchen / FSSAI vs COP.13.e/f nutritional screen, assessment and therapeutic-diet prescription.** HIC.3 owns kitchen hygiene and the food-safety licence. COP.13 does not name the Food Safety and Standards Act. A kitchen licence is not a nutritional-risk screen.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.13.a/b pain assessment and titration vs MOM analgesic-as-medication.** Care loop here; prescribing, dispensing, administration and storage remain MOM (undrafted).

- [ ] **COP.13.d collaborative rehab plan vs AAC.7 internal referral method.** AAC.7 owns the referral; COP.13 owns the plan that follows, and only where rehab is a defined service.

- [ ] **COP.13 nutrition vs COP.7.c maternal nutrition vs COP.8.e paediatric nutrition/growth/immunisation assessment.** Admission-wide screen here; those other assessments are not this document and are not ticked off by it.

- [ ] **COP.13 mobilisation-as-rehab-plan vs COP.12 mobilisation as falls/PU/VTE measure.** Coordinated; neither rewrites the other.

---

## Deferred from COP.1 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.1 draft Scope / universal_facts_checklist). Do not patch AAC.1 (approved) or the unapproved AAC.2 in this pass — reconcile when the owning document is next opened.

- [ ] **AAC.2.b vs COP.1.a two identifiers.** AAC.2.b generates the unique identification number at registration. COP.1.a is TWO IDENTIFIERS at the point of care (name + UID, or the hospital-defined pair). The UID is one identifier once issued; COP.1 does not generate it. Both Scopes state the split. Flag so the division is not lost if one is approved without the other.

- [ ] **AAC.1 vs COP.1.d uniform care across settings.** AAC.1 defines which services exist and the department scopes. COP.1 makes care for a given condition the same in every setting in which that care is actually provided (OPD / IPD / OT / ICU / emergency). Not the same requirement. Stated in COP.1 Scope.

T2 one-line flags (standing rule: flag and move on):

- [ ] **AAC.3 assessment vs COP.1.c/d protocols.** Assessment, care plan, reassessment and early-warning are AAC.3. They are not uniform-care protocols. Stated in COP.1 Scope.

- [ ] **AAC.4 specimen identity vs COP.1.a.** AAC.4 applies the two-identifier process at collection; COP.1 owns the hospital-wide process. T2 flag only.

- [ ] **COP.1.c hospital-wide clinical protocols vs COP.4.d nursing CPGs.** Intra-COP: COP.1 owns medical/condition protocols; COP.4 owns nursing standards of practice. Both Scopes state the split. Reconcile if either is approved as if they were the same protocol set.

---

## Deferred from COP.3 (drafted 2026-08-17, UNAPPROVED)

Whole standard is Tier 2 (ZERO asterisks on printed p.62-63). T2 one-line flags only.

- [ ] **AAC.3.e vs COP.3.** AAC.3.e owns recognising deterioration and handing the crashing patient to this protocol. COP.3 owns the resuscitation once started. Stated in both Scopes. Flag so the division is not lost if one is approved without the other.

- [ ] **AAC.2 / COP.2 vs COP.3.** Life-stabilising treatment in the emergency area uses this protocol. COP.2 owns the ED area, triage, ambulance and must not write a second resuscitation algorithm. COP.3 Scope states the split. COP.2.h–i ambulance reprocessing remains a COP.2/HIC.6/MOM flag, not this one.

- [ ] **HIC.6 vs COP.3.c kit availability.** HIC.6 owns reprocessing of resuscitation bags, laryngoscope blades and related airway devices. COP.3 owns having a ready kit in named areas and restoring it after use. Do not rewrite HLD, sterilisation or Spaulding classification into COP.3. Stated in COP.3 Scope.

- [ ] **HIC.2 vs COP.3.** Hand hygiene, PPE and standard precautions during resuscitation remain HIC.2. Point only; not restated.

---

## Deferred from COP.4 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.4 draft Scope / universal_facts_checklist).

- [ ] **AAC.7 handover METHOD vs COP.4.a nursing content of the record.** AAC.7 owns structured handover at shift and at internal transfer. COP.4.a owns the nursing entry in the patient record (observations, actions, alignment with the overall plan). Handover communicates; the record retains; neither substitutes. Both Scopes should keep this split. Flag so the division is not lost if one is approved without the other.

- [ ] **COP.1.c/d vs COP.4.d.** Hospital-wide medical protocols vs nursing clinical practice guidelines. Same intra-COP flag as under COP.1. A medical protocol labelled as a nursing guideline does not satisfy COP.4.d.

T2 one-line flags (standing rule: flag and move on):

- [ ] **HIC.2 HH/PPE/TBP/injection vs COP.4.** Nurses follow HIC.2 in the course of nursing care. COP.4 points and does not restate five moments, PPE donning, isolation categories or injection-safety rules.

- [ ] **HIC.6 vs COP.4.c.** HIC.6 owns reprocessing of reusable nursing equipment. COP.4.c owns that a ready item is available at the point of care.

- [ ] **IMS vs COP.4.a.** IMS (undrafted) owns record structure, retention and confidentiality. COP.4 owns the nursing entries written into that record.

- [ ] **AAC.3 care plan vs COP.4.a alignment.** AAC.3 owns the documented care plan. COP.4 requires nursing care to align with that plan and to make the alignment visible in the nursing entry. Not a rewrite of AAC.3.

- [ ] **HRM vs COP.4.b assignment.** HRM (undrafted) owns credentialing / INC registration verification. COP.4.b uses that verification when assigning care; it does not restate the method. AAC.1.b is roster/resourcing of a specialty, not per-period assignment of a nurse to a patient.

---

## Deferred from COP.5 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.5 draft Scope / universal_facts_checklist). Do not patch approved AAC.4 or HIC.3 in this pass — reconcile when the owning document is next opened.

- [ ] **AAC.4 laboratory testing vs COP.5 transfusion.** AAC.4 owns grouping, screening, compatibility as laboratory work, the specimen pathway, and critical laboratory results to the clinician. COP.5 owns the clinical transfusion: decision, bedside identity check, administration, emergency availability of a unit, and the reaction pathway. A compatibility report is a laboratory result; hanging the unit is COP.5. Flag so AAC.4 is not later read as owning transfusion method.

- [ ] **HIC.3 BMW of used blood bags vs COP.5.b used-bag disposal.** COP.5 requires that a used bag and tubing enter the hospital-wide biomedical-waste programme and are not left on a trolley, in a sink or in general waste. It does not restate colour categories. BMW Rules 2016 are deliberately NOT named in COP.5 P2. Do not patch HIC.3.

- [ ] **MOM (undrafted) vs COP.5 transfusion method.** Blood and blood components are named in the MOM chapter intent. COP.5 owns the transfusion process. When MOM is drafted it must not restate safe-transfusion method (bedside identity check, issue, administration, emergency availability, reaction pathway). Forward-ref only.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.5.a transfusion scope vs AAC.1 service directory.** Align; do not rewrite the directory. Stated in Scope and step 1.

- [ ] **COP.5.d transfusion/donation consent vs PRE consent method.** PRE.3 (drafted 2026-08-17, UNAPPROVED) now owns how consent is explained, recorded and refused. COP.5.d still owns that consent is obtained for transfusion and for donation before the act. Do not rewrite COP.5; the PRE.3 draft accepts this handoff.

- [ ] **COP.5.f haemovigilance / post-transfusion form.** No approved policy owns reaction analysis. Keep it here.

- [ ] **COP.1 two identifiers vs COP.5.b bedside check.** COP.1 owns the identifier pair; COP.5 requires those identifiers before a unit is hung.

---

## Deferred from COP.6 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.6 draft Scope / universal_facts_checklist). CRITICAL: do not rewrite HIC bundles, BMW colours, or NHSN definitions. Do not patch approved HIC.2/HIC.4/HIC.5 in this pass.

- [ ] **COP.6.c infection-control practices in ICU/HDU written guidance vs HIC.2 / HIC.4 / HIC.5.** HIC.2 owns HH/TBP/PPE. HIC.4 owns device bundles (VAP/CLABSI/CAUTI/SSI) and PEP. HIC.5 owns surveillance including VAE and NHSN definitions. COP.6.c (asterisked) requires those practices to be IN the ICU/HDU written guidance and followed there. A local unit SOP that reprints a bundle and then drifts from HIC.4 is a defect. Both documents must keep this split if either is approved without the other.

- [ ] **Reconcile COP.6.a vs AAC.2 vs AAC.3.e — bed-shortage and ICU admission overlap** in the
      same dedicated consistency pass as the AAC.2.e/COP.2.c triage item above — not in this COP
      insert pass.

      Context and instruction: three unapproved drafts touch the moment a deteriorating patient
      needs a higher level of care or a bed that does not exist. AAC.2 step 5 owns the
      **hospital-wide** written mechanism when no **ward** bed is available for a patient who needs
      admission. COP.6.a (Commitment, asterisked) owns **ICU/HDU-specific** admission and discharge
      criteria plus the **unit bed-shortage procedure** when no intensive-care or high-dependency
      bed exists. AAC.3.e (Achievement, asterisked) owns **early-warning signs** on the ward and the
      processes that identify deterioration — which may trigger an ICU **referral** but is not an
      admission decision. On instruction (2026-08-17), **each draft carries its full block; none was
      patched in the others' pass.** COP.6 Scope and step 1, AAC.2 step 5, and AAC.3 Scope state the
      divisions. Do NOT patch one without the other.

      **Specific divergences to resolve in that pass** (identified 2026-08-17):

      1. **Hospital-wide ward bed shortage vs ICU/HDU bed shortage — two procedures, one patient.**
         AAC.2 step 5 names options in order: holding area under observation, earlier safe discharge,
         day-care/observation, transfer/referral — with authority, review interval, and
         bed-management register. COP.6 step 1 names ICU/HDU admission criteria, discharge criteria,
         and a **separate** intensive-care/high-dependency bed-shortage procedure (create bed by
         discharge, escalate within unit, hold in theatre/recovery, transfer to named ICU
         elsewhere, etc.). **Failure mode if merged:** a ventilated patient left in a ward corridor
         because AAC.2's holding-area mechanism was applied without COP.6's unit procedure, or vice
         versa — a hospital-wide diversion that bypasses the ICU lead. **Likely resolution:** COP.6
         step 1 should reference AAC.2 explicitly as the hospital-wide envelope and state that when
         both ward and ICU beds are short, both procedures run with a named coordinator; AAC.2 step 5
         should state it does not substitute for COP.6 when the clinical need is intensive care.

      2. **Early-warning trigger vs admission criteria — referral is not admission.** AAC.3.e lays
         down guidelines to identify early warning signs and implements processes to escalate.
         COP.6 step 1 states admission is against written ICU/HDU criteria and the responsibility
         block names "requesting clinicians do not treat an early-warning trigger as automatic
         admission". **Divergence to watch:** if AAC.3's escalation process names "call ICU" without
         "ICU accepts against criteria", assessors will read automatic admission. If COP.6's criteria
         are silent on what happens when AAC.3 fires, ward staff will improvise. **Likely
         resolution:** AAC.3.e evidence/process names the referral handoff; COP.6.a evidence names
         the accept/refuse decision record — cross-linked, not duplicated.

      3. **Emergency patient waiting for ward bed vs ICU request from ED.** AAC.2 step 5: "An
         emergency patient waiting for a bed remains under the emergency-care policies ... until a
         bed is allocated or a transfer is completed." COP.6 step 1 accepts requests from "ward,
         emergency area or operation theatre". **Not a contradiction** but the reconciliation pass
         should confirm ED→ICU requests use COP.6 criteria and ED→ward waits use AAC.2 mechanism
         without cross-wiring.

      4. **Audit samples cite different registers.** AAC.2 step 9 audits prioritisation and
         bed-non-availability entries. COP.6 step 7 audits "bed-shortage events that used the unit
         procedure rather than the hospital-wide AAC.2 mechanism alone". Keep both audit asks — they
         are deliberately different tests.

      Note: AAC.7 internal transfer into/out of ICU remains a separate deferred item below; it owns
      the move once COP.6 has accepted admission.

      CLOSED for this pass: boundaries stated in all three Scopes; no text change until the
      dedicated pass.

- [ ] **AAC.7 internal transfer into/out of ICU vs COP.6 admission/discharge decision.** COP.6 decides whether the patient meets criteria; AAC.7 owns the unit-to-unit move once that decision is made.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.6.b staff/equipment vs HRM credentialing / AAC.1.b.** Qualifications via HR policies; this document judges adequacy against the care the unit claims. Stated in step 2.

- [ ] **COP.6.e periodic family counselling vs PRE.** PRE.2.p (drafted 2026-08-17, UNAPPROVED) now owns the general multidisciplinary-counselling right and method. COP.6.e still owns that ICU/HDU counselling happens periodically during the stay. Do not rewrite COP.6; landed from the PRE.2 side.

- [ ] **COP.6.f brain-death / EOL pathway vs COP.11.i/j transplant and donation-awareness.** Same THOA 1994 envelope already flagged under COP.11. Clinical declaration pathway remains COP.6; donation programme remains COP.11.

- [ ] **COP.6 unit-to-ward discharge vs AAC.8 leaving the organisation vs COP.2 ED episode note.** Unit discharge criteria are COP.6; hospital discharge summary is AAC.8.

- [ ] **COP.6 uses COP.3 CPR; does not write it.** Point only.

- [ ] **HIC.3 housekeeping / BMW colours and HIC.6 reprocessing in the unit.** Pointed at; not restated.
- [ ] **COP.6.d intensive-care QA vs PSQ.1 hospital-wide QI programme now landed.** Unit QA remains COP.6.d. PSQ.1 owns the hospital-wide programmes. Do not patch COP.6 in this pass.

---

## Deferred from COP.7 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.7 draft Scope / universal_facts_checklist). Do not patch AAC.5 imaging licences in this pass.

- [ ] **AAC.5 USG PC-PNDT registration vs COP.7.a obstetric prohibition on sex determination.** AAC.5 owns imaging licences, statutory imaging records and the licence calendar. COP.7 owns the obstetric process, including that antenatal care does not determine or communicate foetal sex. A PC-PNDT registration is not obstetric care; an obstetric consultation that tells the family the sex is not an imaging-licence problem alone. Both documents are required. AAC.6 owns the statutory notice in imaging.

- [ ] **COP.7.c maternal nutrition in antenatal assessment vs COP.13 in-patient nutritional screen vs COP.8.e paediatric nutrition/growth/immunisation vs HIC.3 kitchen.** Same split already flagged under COP.13. COP.7.c is the antenatal component (not a weight column). An in-patient screen after admission does not complete it. FSS Act is not named in COP.7 P2.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.7.b high-risk identification/referral vs AAC.2 between-organisation transfer.** COP.7 owns the clinical decision that referral is needed; AAC.2 owns the transfer once that decision is made.

- [ ] **COP.7.d peri/post-natal monitoring vs AAC.3.e early-warning.** Escalation of a deteriorating mother uses AAC.3 where that process applies; obstetric emergency response remains in COP.7 written guidance.

- [ ] **COP.7.e neonatal BACKUP vs COP.8.b neonatal CARE.** Standing intra-COP division, mirrored in the COP.8 draft. COP.7 owns that an obstetric service caring for high-risk cases has the human resources and facilities to take care of those neonates. COP.8 owns how neonates/children are then cared for. COP.7 does not write neonatal clinical protocols.

- [ ] **COP.7 live/stillbirth registration (RBD Act 1969) vs AAC.8 discharge of mother/neonate.** Statutory registration is this obstetric process; the clinical discharge summary is AAC.8. Parallel to AAC.8's split between death case-summary and statutory death certificate.

- [ ] **HIC.2/3/4/5/6 labour-room IPC, waste, bundles, surveillance, reprocessing.** Infection control stays HIC. COP.7 requires those practices in obstetric areas and does not rewrite them.

- [ ] **COP.7.a MTP where provided vs PRE consent method.** Statutory MTP opinion and consent records remain this obstetric process where termination is in scope. General consent method is now PRE.3 (drafted 2026-08-17, UNAPPROVED). Do not rewrite COP.7; landed from the PRE.3 side.

---

## Deferred from MOM.1 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the MOM.1 draft Scope / universal_facts_checklist). Do not patch approved HIC or COP.5 in this pass.

- [ ] **COP.5 transfusion vs MOM chapter intent that "medications also include blood & blood components".** The chapter intent on printed p.75 includes blood. COP.5 already owns the clinical transfusion (request, bedside identity, hanging, reaction). MOM.1–9 do not manage blood as ward-stock medicines and do not rewrite hanging a unit. Keep this split if either chapter is approved without the other.

- [ ] **MOM.1.e vs MOM.9 implant criteria.** MOM.1.e (unasterisked) is a pointer only. MOM.9.a (asterisked) owns written procurement and usage guidance. Do not let MOM.1 grow an implant SOP.

T2 one-line flags:

- [ ] **AAC.1 service directory vs MOM.1.a formulary.** Formulary must match defined services; it does not rewrite the directory.
- [ ] **HIC.2 / HIC.3 / HIC.4.** Injection safety, pharmaceutical waste colours, device bundles — pointed, not restated. BMW not in MOM.1 P2.
- [ ] **PRE.4 / IMS.** PRE.4 (drafted 2026-08-17, UNAPPROVED) now owns teaching about medicines and side effects. The medical record itself remains IMS (still undrafted).

---

## Deferred from MOM.2 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags:

- [ ] **COP.3 crash-cart kit vs MOM.2.e/f emergency-medication list.** COP.3 owns that resuscitation kits exist in named areas. MOM.2 owns the hospital-wide emergency-medication list, uniform storage, continuous availability and replenishment. Do not print a kit list in either as a NABH mandate.

- [ ] **MOM.2 general storage vs MOM.8.c secure storage of NDPS / chemo / radioactive.** MOM.2 does not write the NDPS cupboard and does not name NDPS in P2. MOM.8 accepts the COP.9/COP.10 storage handoff.

T2 one-line flags:

- [ ] **COP.2 ambulance/emergency-area stock vs MOM.2.e list.** Stock against this hospital's emergency-med list; COP.2 owns ambulance fitness.
- [ ] **COP.9 / COP.10 sedative and anaesthetic stock.** MOM.2 stores non-NDPS stock; those policies own the clinical act.
- [ ] **LASA / high-risk lists (ISMP, WHO).** Frameworks for MOM.2.c; not mandated lists.

---

## Deferred from MOM.3 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags:

- [ ] **MOM.3 vs MOM.4 — prescription minimum vs uniform order writing.** MOM.3.b owns the determined minimum of a prescription as a clinical document. MOM.4 owns how the order appears in the record (authorised writer, location, name+UID, legibility, dated/timed/signed, name/route/strength/frequency). Do not duplicate MOM.4's four fields inside MOM.3.b so MOM.4 becomes redundant.

- [ ] **AAC.3 assessment vs MOM.3.c allergies before prescribing.** Assessment may collect allergies. Ascertaining them before this prescription is MOM.3.c. A checkbox is not that act.

- [ ] **AAC.7 / AAC.8 vs MOM.3.h reconciliation at transitions.** AAC.7 owns the internal move/handover. AAC.8 owns the discharge summary including medication instructions. Reconciliation is MOM.3.h.

T2 one-line flags:

- [ ] **COP.13 pain titration vs MOM.3 prescribing the analgesic.** Clinical loop is COP.13; the prescription is MOM.3.
- [ ] **WHO rational use / NLEM / EML / NCCMERP / High 5s / AHRQ med rec.** Frameworks, not pasted protocols or mandated tools.
- [ ] **NDPS verbal orders.** A spoken order does not skip MOM.8's register.

---

## Deferred from MOM.4 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags:

- [ ] **MOM.3 verbal orders vs MOM.4 written order artefact.** Once a verbal order is written it is a MOM.4 order. MOM.4.a owns that only authorised personnel write.

T2 one-line flags:

- [ ] **AAC.2 UID vs MOM.4.b name and unique identification number on the order location.** AAC.2 generates the number; MOM.4 requires it.
- [ ] **IMS the record vs MOM.4 location/legibility/content.**
- [ ] **HRM / NMC / INC credentialing vs MOM.4.a authorised writers.** Verification is HRM; this document owns that only those people write.

---

## Deferred from MOM.5 (drafted 2026-08-17; **owner-approved as drafted 2026-08-17**)

Owner confirmed clean: no prescribing-language drift; scope boundary with MOM.3/MOM.4 correctly stated. Database `standard_text` copy-of-MOM.3 error remains the 2026-08-11 item; do not reopen the draft for that.

Drafted as dispensing from the chapter-summary header on printed p.75, not from `shco_full_oes.standard_text` and not from the corrupted OE-page header. Database fix remains the 2026-08-11 item above.

T1 overlap flags:

- [ ] **MOM.2 near-expiry as inventory vs MOM.5.c handling near-expiry at dispensing.** MOM.2 owns stock control. MOM.5.c owns do-not-dispense / quarantine at the hatch. Mixing the two produces an expired pack that "was in date in the cupboard".

- [ ] **COP.5 issue of a blood unit vs MOM.5.d labelling of dispensed medications.** A unit is not a dispensed medicine under this OE.

T2 one-line flags:

- [ ] **MOM.2.c high-risk LIST vs MOM.5.e verification of high-risk ORDERS before dispensing vs MOM.8 NDPS/chemo/radioactive.** Three different acts.
- [ ] **HIC.3 returned/expired waste.** Enters the hospital-wide programme; colours not restated; BMW not in MOM.5 P2.
- [ ] **NDPS register/destruction.** MOM.5 may dispense; MOM.8 owns the account.

---

## Deferred from MOM.6 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags:

- [ ] **COP.1 two identifiers vs MOM.6.c identification before administration.** COP.1 owns the pair. MOM.6.c is the admin-time check using them.

- [ ] **HIC.4 device bundles vs MOM.6.f catheter and tubing mis-connections.** MOM.6.f is a medication-administration connection error (WHO Patient Safety Solution 7, chapter ref 2). It is not VAP/CLABSI/CAUTI. Do not rewrite HIC.4.

T2 one-line flags:

- [ ] **HIC.2 safe injection.** Applied at administration; not rewritten.
- [ ] **COP.9 / COP.10 / COP.11.** Clinical sedation/anaesthesia/surgery method stays those documents; ID / verify / document still apply.
- [ ] **COP.13 pain titration vs MOM.6.g administration documentation.**
- [ ] **AAC.8 discharge-summary medication instructions vs MOM.6.h in-hospital self-admin vs MOM.6.i meds brought from outside.**
- [ ] **MOM.6.b prepared-medication labelling vs MOM.5.d dispensed-pack labelling.** Different acts.
- [ ] **COP.5 / MOM.9.** This document does not hang blood and does not implant devices.

---

## Deferred from MOM.7 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags:

- [ ] **MOM.6 administration record vs MOM.7 after.** MOM.6 owns the dose and the administration entry. MOM.7 owns monitoring, changing therapy, capturing and reporting near-miss / medication error / ADR.

- [ ] **COP.5.f transfusion reaction vs MOM.7 ADR.** Chapter intent includes blood; COP.5 already owns transfusion reactions. A transfusion reaction is not captured as a MOM.7 ADR.

T2 one-line flags:

- [ ] **HIC.5 HAI surveillance vs MOM.7 medication-error capture.** A drug reaction is not an SSI.
- [ ] **HIC.4 PEP.** Occupational exposure, not MOM.7 ADR.
- [ ] **AAC.3.e early-warning vs MOM.7.a post-medication monitoring.** Same vital signs may be used; this is effect and harm of the drug. Not automatic ICU admission (COP.6).
- [ ] **PRE.4.b education about side effects vs MOM.7 still capturing the event.**
- [ ] **Reporting time frame is hospital-defined.** Do not invent a 24-hour NABH mandate.
- [ ] **PSQ.5 incident system now landed.** A medication event that meets the hospital incident definition is dual-entered. MOM.7 still captures NM/ME/ADR. PSQ.5 does not replace MOM.7. Historical MOM.7 checklist wording "not HIC or CQI ownership of all CAPA" meant hospital-wide CAPA; under 3rd Edition that hospital-wide incident CAPA is PSQ.5.d, not a CQI chapter. Do not patch MOM.7 in this pass.

---

## Deferred from MOM.8 (drafted 2026-08-17; **owner-approved 2026-08-17** after the distinct cytotoxic block and chemotherapy-safety citations)

THIS IS THE NDPS STANDARD. COP.9/COP.10 storage handoff is accepted here.

Owner 2026-08-17: approved after (1) chemotherapeutic/cytotoxic handling as a distinct procedure-step block (PPE, spill, CSTD or equivalent, extravasation, hazardous waste) and (2) NIOSH Alert 2004-165, OSHA hazardous-drug occupational-exposure guidance, USP <800>, and ESMO–EONS 2012 added to References as frameworks, not P2 statutes. Insert as `status='draft'` only via `python3 policies/build/apply_mom_drafts_supabase.py --insert`. The 2026-08-17 Cloud Agent VM did not have `SUPABASE_SERVICE_ROLE_KEY`; dry-run of all nine drafts passed; live POST was not executed.

T1 overlap flags:

- [ ] **COP.9 / COP.10 NDPS storage handoff now landed.** Those drafts refused to inherit NDPS as a storage statute. MOM.8 owns cupboard, register and destruction. Clinical sedation/anaesthesia method stays COP. Do not patch COP.9/COP.10 in this pass.

- [ ] **MOM.2 general storage vs MOM.8.c secure storage of the three named classes.**

T2 one-line flags:

- [ ] **MOM.3/4 prescribing vs MOM.8.b appropriate caregivers for these classes.**
- [ ] **MOM.5 dispensing vs MOM.8.e usage/disposal record.**
- [ ] **MOM.6 administration vs MOM.8.d chemo/radioactive preparation and qualified administration.**
- [ ] **COP.11 chemo in OT** is still MOM.8 step-4 handling / qualified person.
- [ ] **AAC.5 / AAC.6 diagnostic radiology licences vs MOM.8 therapeutic radioactive agents.** If none, record absence against AAC.1; do not invent a hot laboratory.
- [ ] **HIC.2 donning/doffing vs extra hazardous-drug PPE named at MOM.8 step 4.** Standard-precaution PPE is not by itself cytotoxic PPE. Blood/body-fluid spill remains HIC.2.
- [ ] **HIC.3 cytotoxic waste colours.** Unused dose, empty vials, contaminated sharps/PPE and spill debris enter that stream; colours not restated; BMW not in MOM.8 P2.
- [ ] **FMS building chemical or mercury spill vs MOM.8 step-4 cytotoxic spill at preparation/administration.** FMS undrafted; flagged for that pass.

---

## Deferred from MOM.9 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags:

- [ ] **AAC.8 discharge summary vs MOM.9.c batch and serial number.** AAC.8 owns that a summary is given and its clinical content list. MOM.9.c owns that batch AND serial number also appear in the medical record, the master logbook, AND the discharge summary. AAC.8 Scope already hands this to MOM; this draft mirrors it.

- [ ] **COP.11 surgical implanting vs MOM.9 procurement, counselling and traceability.** Implanting is the surgical act. MOM.9 owns the criteria, counselling and numbers.

T2 one-line flags:

- [ ] **AAC.1 defined services vs implant types offered.** Unused implant services are a recorded absence, not a copied implant SOP.
- [ ] **MOM.1.e is a pointer only.** Criteria live here.
- [ ] **PRE surgical consent vs MOM.9.b counselling for usage and precautions.** Not the same act. PRE.3 (drafted 2026-08-17, UNAPPROVED) now owns surgical-consent method and accepts that implant counselling is not that consent.
- [ ] **Medical Devices Rules, 2017.** Procure from a licensed source; implanting does not make the hospital a manufacturer.

---

## Deferred from PRE.1 (drafted 2026-08-17, UNAPPROVED)

Source: official SHCO 3rd Edition PDF md5 `39e3bc86d73d651b9cfef283bbf018a9`, Chapter 4 printed pages 85–91 (PDF indices 91–97). PRE.1 printed p.86 / index 92. T1 = PRE.1.a*, PRE.1.b*. P2 names CPA 2019 only insofar as a patient may seek a consumer remedy — not as the source of the NABH rights list. CEA 2010 and MHCA 2017 are not in PRE.1 P2.

Insert PRE.1–PRE.6 as `status='draft'` only via `python3 policies/build/apply_pre_drafts_supabase.py --insert`. The 2026-08-17 Cloud Agent VM did not have `SUPABASE_SERVICE_ROLE_KEY`; dry-run of all six drafts passed; live POST was not executed. No row was approved.

T1 overlap flags (full cross-check done in the PRE.1 draft Scope / universal_facts_checklist). Do not patch approved HIC in this pass.

- [ ] **PRE.1 vs PRE.2 — documented set vs content of the list.** PRE.1 owns that a documented set exists, is displayed, is made known, is promoted and is protected. PRE.2 owns what the set contains. Do not let PRE.1 grow the rights catalogue or PRE.2 write the display board.

- [ ] **PRE.1.d/e vs PRE.6 — rights-violation report vs complaint redressal.** A complaint that is a rights violation is both. PRE.6 owns redressal as a complaint; PRE.1.e owns leadership review of **violations**. The report route must not be only to the alleged actor. Keep both records when the subject is a rights violation.

T2 one-line flags:

- [ ] **PRE.1.a awareness at entry vs AAC.2 registration/UID.** Awareness sits beside registration; this document does not generate the number.
- [ ] **PRE.1 vs AAC.8 discharge-summary advice.** AAC.8 owns the paper; PRE.4 owns teaching method; PRE.1 owns rights at entry.
- [ ] **PRE.3 / COP.5 / COP.9 / COP.10 / COP.11.** Consent method and that consent happened. PRE.1 does not decide whether those consents happened.
- [ ] **IMS / HRM.** The record and the training file. Forward references.

---

## Deferred from PRE.2 (drafted 2026-08-17, UNAPPROVED)

Whole standard is Tier 2 (sixteen OEs a–p, none asterisked; clustered into ten steps). P2 is accreditation-only — CPA/CEA/MHCA are not a checklist here. MHCA capacity is PRE.3.c, not this list.

T2 one-line flags (standing rule: flag and move on):

- [ ] **PRE.1 — display/protection vs this content.** See PRE.1 T1 flag.
- [ ] **PRE.2.g vs PRE.3 and COP.5/9/10/11.** Pointer only. PRE.3 owns method. COP.5/9/10/11 own that the relevant consent happened before the act. Do not rewrite those methods in PRE.2.
- [ ] **PRE.2.e vs PRE.3.** Refusal is the right; PRE.3 records that consent was not given.
- [ ] **PRE.2.h vs PRE.6.** Right vs complaint mechanism.
- [ ] **PRE.2.i vs PRE.5.** Right vs expected-cost method.
- [ ] **PRE.2.j vs IMS and AAC.8.** Access during care vs the record file vs the discharge summary the patient takes away.
- [ ] **PRE.2.o vs AAC.3 and PRE.5.d.** Consultation on the plan vs the clinical care-plan document vs financial implications of a change.
- [ ] **PRE.2.p vs COP.6.e.** General multidisciplinary counselling vs periodic ICU family counselling where ICU exists. COP.6.e's forward-ref to undrafted PRE is now landed from this side.
- [ ] **PRE.2.d vs IMS.** Confidentiality as a patient right vs confidentiality as a record-keeping act.
- [ ] **PRE.2.m/n vs PRE.3.b and PRE.4.d.** Decision-making explanations vs the consent conversation vs disease-process education. Same language may be used; they are not the same act.
- [ ] **Unused research / unused ICU.** Recorded absence against AAC.1, not a copied SOP.

---

## Deferred from PRE.3 (drafted 2026-08-17, UNAPPROVED)

T1 = PRE.3.a*, PRE.3.c*. P2 names NMC Act 2019 (RMP professional consent duty) and MHCA 2017 only when that Act's definition of a person with mental illness is met. Kumar 2015 and Nandimath 2009 (chapter refs 10 and 13) are frameworks. **Samira Kohli v. Dr. Prabha Manchanda is not a numbered PRE chapter reference and is not imported as a NABH case-law mandate. Indian Contract Act 1872 is not a numbered chapter reference and is not in P2.** CPA 2019 and CEA 2010 are not in PRE.3 P2.

T1 overlap flags:

- [ ] **PRE.3 vs COP.5 / COP.9 / COP.10 / COP.11 — CRITICAL HANDOFF ACCEPTED.** Those drafts own that consent happened before the act and forwarded method to PRE. This document accepts method. COP.11 step 3 already requires the performing doctor (or same-team doctor present and responsible). Do not rewrite those "consent happened" steps here, and do not patch COP in this pass.

- [ ] **PRE.2.g — right that consent is obtained before listed acts vs this method.** PRE.2 lists the right; PRE.3 writes the form.

T2 one-line flags:

- [ ] **PRE.3.b vs PRE.4.a.** Same language; consent conversation vs ongoing education.
- [ ] **PRE.2.e.** Refusal as a right; this document records consent not given.
- [ ] **MOM.9.b implant usage/precaution counselling is not surgical consent.** PRE.3 owns surgical consent for the implanting procedure.
- [ ] **COP.7.a MTP where provided.** Statutory MTP opinion/consent records remain COP.7 where termination is in scope; general method is now this document. Lands COP.7's forward-ref.
- [ ] **AAC.1.** Unused research is a recorded absence, not a copied ethics SOP.
- [ ] **IMS.** The consent content in the record. Forward reference.

---

## Deferred from PRE.4 (drafted 2026-08-17, UNAPPROVED)

T1 = PRE.4.f* only (effective communication). P2 is accreditation-only — no named Act in the PRE bibliography for this subject. Readability/communication chapter refs (Badarudeen, Marcus EDUCATE, Nouri/Rudd, Ha/Longnecker) are frameworks, not pasted protocols. FSS Act 2006 is not in P2.

T1 overlap flags:

- [ ] **PRE.4 vs AAC.8.d — CRITICAL HANDOFF ACCEPTED.** AAC.8 owns that follow-up advice is on the discharge summary and already hands teaching method to PRE. This document accepts method during the stay and for that paper. AAC.8 does not write how education is given during the stay.

T2 one-line flags:

- [ ] **PRE.4.b vs MOM.6 administration vs MOM.7 NM/ME/ADR capture.** PRE.4.b is teaching; MOM.6 still administers; MOM.7 still captures the event.
- [ ] **PRE.4.c vs COP.13 nutritional-risk/therapeutic diet vs COP.8 paediatric immunisation vs HIC.3 kitchen.** PRE teaches; those documents own the clinical and kitchen methods.
- [ ] **PRE.4.e vs HIC.2/HIC.4/HIC.5.** PRE teaches the patient how they can help prevent HAI; HIC owns IPC method. Do not rewrite bundles or surveillance.
- [ ] **PRE.4.d vs AAC.3.** Disease-process teaching vs diagnosis and the care plan.
- [ ] **PRE.3.b vs PRE.4.a.** Same language; different acts. See PRE.3.
- [ ] **PRE.1.** Rights at entry vs healthcare-needs teaching.

---

## Deferred from PRE.5 (drafted 2026-08-17, UNAPPROVED)

Whole standard is Tier 2 (no asterisked OE). P2 names CPA 2019 (not misled on price) and CEA 2010 / Clinical Establishments (Central Government) Rules 2012 display-of-rates **only if the State has adopted CEA**. Fence adoption; do not invent a CEA board in a non-adopting State. MHCA is not named. No rupee figures as NABH mandates.

T2 one-line flags:

- [ ] **PRE.2.i right vs this method.** PRE.2 lists the right; PRE.5 writes the tariff and the explanation.
- [ ] **PRE.1.b promotion of the cost right.** Promotion is PRE.1; figures are PRE.5.
- [ ] **AAC.3 / PRE.2.o care-plan change vs PRE.5.d financial implications.** Clinical modification stays AAC.3/PRE.2.o; this document owns only the money of that change.
- [ ] **AAC.8 discharge summary.** Not this explanation unless the hospital has defined putting a bill on that paper.
- [ ] **PRE.3 signed consent is not agreement to an unnamed bill.**
- [ ] **ROM/FMS billing (undrafted).** PRE.5 owns patient-facing expected-cost information, not the billing ledger, GST, or payer contracts. Flagged for the ROM/FMS pass.

---

## Deferred from PRE.6 (drafted 2026-08-17, UNAPPROVED)

Subject **confirmed from the PDF** (do not assume): "The organisation has a mechanism to capture patient's feedback and to redress complaints." T1 = PRE.6.c* (redress + make aware of the procedure). P2 names CPA 2019 for consumer grievance as a framework, not copied District Commission procedure. Reader et al. 2014 (ch 17) is a taxonomy framework. CEA/MHCA are not named.

T1 overlap flags:

- [ ] **PRE.6.c vs PRE.1.d/e — CRITICAL SPLIT.** A rights-violation complaint is both a PRE.6 complaint and a PRE.1.d report; PRE.1.e owns leadership review of violations. Neither record replaces the other. The complaint route must not be only to the person complained of.

T2 one-line flags:

- [ ] **PRE.2.h right vs this mechanism.**
- [ ] **PRE.1.a/b rights display/promotion vs awareness of this procedure.** Awareness of the feedback/complaint procedure is PRE.6.c; it is not the PRE.1.a board counted twice.
- [ ] **PRE.5 cost disputes** are complaints here; the tariff remains PRE.5.
- [ ] **MOM.7.** A family complaint about a medication event is redressed here; the event is still captured under MOM.7.
- [ ] **AAC.8.** A complaint about discharge is redressed here; AAC.8 owns the summary.
- [ ] **ROM/FMS (undrafted)** may own an accounts adjustment; this document owns that the complaint was received and redressed as a patient complaint.
- [ ] **PRE.6.a satisfaction vs PRE.6.b experience.** Two distinct OEs; the standard does not define the difference — hospital method must.

---

## Cross-cutting: CQI (2nd Edition) is not PSQ (3rd Edition) (flagged 2026-08-17)

The SHCO 3rd Edition **forward** (PDF index 2) states that the chapter on Continuous Quality
Improvement is **replaced** by Patient Safety and Quality Improvement. PSQ is Chapter 6 of that
book (printed pages 101–108; PDF indices 107–114). It is not a rename of CQI. Standard count,
OE count and emphasis differ (increased patient-safety focus). Do not treat CQI and PSQ as
interchangeable. Do not title, code or cite a 3rd Edition master as CQI.

Existing repo wording that still says "CQI" as if it were this chapter — **flagged, not patched
in this PSQ insert pass**:

- [ ] **`policies/build/build_hic1.py` (and `hic1_draft.json` / `hic1_insert.sql`)** — HAI
      surveillance method "belongs to CQI". Under 3rd Edition the method is HIC.5; hospital-wide
      IC **indicators** are PSQ.2.b. Approved HIC.1 not reopened.
- [ ] **`policies/build/build_hic3.py` (and drafts)** — same "belongs to CQI" assignment. Approved
      HIC.3 not reopened.
- [ ] **`policies/build/build_hic4.py`** — already corrected the tracker to HIC.5 and notes the
      previous CQI assignment. Keep that correction; do not reverse it into PSQ.
- [ ] **`policies/build/build_mom7.py`** — checklist "not HIC or CQI ownership of all CAPA".
      Hospital-wide incident CAPA is now PSQ.5.d. MOM.7 still owns medication-event CAPA. Do not
      patch MOM.7 in this pass.
- [ ] **`scripts/master-policy-todos.md` HIC.2 section** — historical checklist tag "CQI 2 a"
      (Entry-Level numbering). Keep as history; the 2026-08-17 PSQ-pass note above records that
      CQI ≠ PSQ.
- [ ] **`policies/build/build_mom5.py`** — NCCMERP "CQI on errors" is NCCMERP's own phrase, **not**
      the NABH chapter. Do not rewrite that citation into PSQ.

App/KPI content (`shco_kpi_content.md`, `ai-assistant/index.ts`) already uses **PSQ.2a–d** for
3rd Edition KPIs. That is the correct chapter code.

---

## Deferred from PSQ.1 (drafted 2026-08-17, UNAPPROVED)

Source: official SHCO 3rd Edition PDF md5 `39e3bc86d73d651b9cfef283bbf018a9`, Chapter 6 printed
pages 101–108 (PDF indices 107–114). PSQ.1 printed p.102 / index 108. Header: "The organisation
implements a patient-safety programme and a structured quality improvement programme." T1 =
PSQ.1.a*, PSQ.1.g*, PSQ.1.h*, PSQ.1.i*. P2 is accreditation-only — no named Act in the PSQ
bibliography. WHO Patient Safety Solutions / High 5s / IHI QI toolkit / AHRQ safety-hazard primer
are frameworks, not pasted programmes. This is **not** 2nd Edition CQI.

Insert PSQ.1–PSQ.5 as `status='draft'` only via
`python3 policies/build/apply_psq_drafts_supabase.py --insert`. The 2026-08-17 Cloud Agent VM
did not have `SUPABASE_SERVICE_ROLE_KEY`; dry-run of all five drafts passed; live POST was not
executed. No row was approved.

T1 overlap flags (full cross-check done in the PSQ.1 draft Scope / universal_facts_checklist).
Do not patch approved HIC.1/HIC.3 in this pass.

- [ ] **PSQ.1.h monitoring audits vs PSQ.3 clinical audit.** PSQ.1.h is audit as continuous
      monitoring of the safety and QI programmes. PSQ.3 is clinical audit of patient care against
      defined parameters. Do not use one file for both.

- [ ] **PSQ.1.e comprehensive QI programme vs PSQ.3.e named QI projects.** The programme is this
      document. Named projects sit inside it and are owned by PSQ.3.

- [ ] **PSQ.1.i nursing-care quality monitoring vs COP.4 nursing assignment/process.** COP.4 owns
      how nursing care is assigned and documented. This OE owns monitoring and improving its
      quality as a quality-system process.

T2 one-line flags:

- [ ] **PSQ.1 vs PSQ.2 indicators / PSQ.4 management support / PSQ.5 incidents.** Siblings. This
      document owns the programmes.
- [ ] **COP.6.d / COP.11.h unit QA vs this hospital-wide programme.** Unit findings may feed;
      they do not replace.
- [ ] **PSQ.1.c proactive risk analysis vs COP.12 bedside vulnerable/falls/PU vs ROM.4.a
      management risk now landed vs PSQ.5 after-the-fact incidents.** Four different acts.
      ROM.4.a (drafted 2026-08-17, UNAPPROVED) accepts the handoff and does not rewrite PSQ.1.c.
- [ ] **PSQ.1.d adapted WHO safety goals vs COP.1 / HIC.2 / MOM.6 owning clinical method.**
      Adaptation here; method there.
- [ ] **HIC.5 HAI surveillance method vs this programme.** Historical "belongs to CQI" in
      HIC.1/HIC.3 is a 2nd Edition name. Method stays HIC.5. IC indicators are PSQ.2.b.
- [ ] **MOM.7 medication-event capture.** This programme may review rates; it does not capture
      the event.

---

## Deferred from PSQ.2 (drafted 2026-08-17, UNAPPROVED)

Whole standard is Tier 2 (five OEs a–e, none asterisked). Header: "The organisation identifies
key indicators to monitor the structures, processes and outcomes which are used as tools for
continual improvement." P2 is accreditation-only. Annexure 1 KPIs of the same book are a
**framework, not a mandated paste**. Unused ICU SMR (or any unused service indicator) is a
recorded absence against AAC.1, not a copied ICU SOP.

T2 one-line flags (standing rule: flag and move on):

- [ ] **PSQ.1 programmes vs these indicators.** PSQ.1 owns the programmes that use the data.
- [ ] **PSQ.2.b IC indicators vs HIC.5 surveillance method.** Inputs from HIC.5/HIC.4; no second
      case-definition book. Do not revive "CQI owns surveillance".
- [ ] **PSQ.2.d patient-safety indicators vs COP.12 / MOM.7 / HIC.4 as source rates.** Source
      rates stay with those documents; this OE oversees them as quality indicators.
- [ ] **PSQ.3 audit parameters vs these key indicators.** Data may overlap; they are not the
      same OE.
- [ ] **ROM/FMS managerial ledger (undrafted) vs PSQ.2.c managerial indicators.** Flagged for
      the ROM/FMS pass.
- [ ] **Annexure 1.** Framework. Do not paste as this hospital's mandated set.

---

## Deferred from PSQ.3 (drafted 2026-08-17, UNAPPROVED)

Whole standard is Tier 2 (five OEs a–e, none asterisked). Header: "There is an established
system for clinical audit and quality improvement programmes." P2 is accreditation-only. IHI
QI toolkit is a framework, not a mandated project catalogue.

T2 one-line flags:

- [ ] **PSQ.1.h monitoring audits vs this clinical audit.** See PSQ.1 T1 flag.
- [ ] **PSQ.1.e programme vs PSQ.3.e named QI projects.** See PSQ.1 T1 flag.
- [ ] **PSQ.2 indicators may supply data; they are not the audit.**
- [ ] **COP.6.d / COP.11.h unit QA.** A unit may run clinical audits under this method; those
      unit QA programmes are not this hospital-wide clinical-audit system.
- [ ] **COP.4 nursing process is care; nursing participation in audit is this document.**
- [ ] **HIC.5 / MOM.7 are not clinical audits.** Surveillance and medication-event capture stay
      those documents.

---

## Deferred from PSQ.4 (drafted 2026-08-17, UNAPPROVED)

Whole standard is Tier 2 (four OEs a–d, none asterisked). Header: "The patient safety and
quality improvement programme are supported by the management." Official PSQ.4.b uses
"program" (American spelling) in the OE — preserved in the mapping `requirement`. P2 is
accreditation-only. AHRQ culture-of-safety primers are frameworks.

T2 one-line flags:

- [ ] **PSQ.1 programmes vs this management support.** PSQ.1 owns the programmes; this document
      owns that management supports them.
- [ ] **PSQ.5 incident reporting vs PSQ.4.a culture of safety.** Culture includes that reporting
      is possible; the incident system is PSQ.5.
- [ ] **PSQ.4.d workforce feedback vs PRE.6 patient/family complaints.** PRE.6 is drafted
      UNAPPROVED on sibling branch `cursor/draft-pre1-pre6-unapproved-9324`. This OE is workforce
      feedback, not patient complaints.
- [ ] **PSQ.4.c budget earmark vs ROM.3.a governance budget approval now landed.** This document
      owns that funds are earmarked from the annual budget; ROM.3.a (drafted 2026-08-17,
      UNAPPROVED on `cursor/draft-rom1-rom4-unapproved-9324`) owns governance approval of that
      budget. Do not patch PSQ.4 in this pass.
- [ ] **ROM.4.a management ensuring proactive risk now landed vs PSQ.1.c quality-system analysis.**
      ROM.4 accepts the split; PSQ.1.c remains quality-system analysis.

---

## Deferred from PSQ.5 (drafted 2026-08-17, UNAPPROVED)

T1 = PSQ.5.a*, PSQ.5.b*. Header: "Incidents are collected and analysed to ensure continual
quality improvement" (no terminal period in the book). Official PSQ.5.e uses "organization"
(American spelling) — preserved in the mapping `requirement`. Levels: a Core, b Commitment,
c Commitment, d Commitment, e Excellence. P2 is accreditation-only. WHO 2020 incident-reporting
guidance, AHRQ Reporting Patient Safety Events, Canadian Incident Analysis Framework and RCA2
are frameworks, not a named software mandate or a pasted national sentinel list. No 24-hour
NABH reporting clock.

T1 overlap flags:

- [ ] **PSQ.5 vs MOM.7 — CRITICAL DUAL ENTRY.** MOM.7 owns capture, reporting and CAPA of
      near-miss, medication error and ADR as a **medication process**. A medication event is
      still an incident under this document when it meets this hospital's incident definition.
      Both records exist. Neither replaces the other.

- [ ] **PSQ.5.a/b incident system and sentinel-event identification vs specialty logs.** COP.5
      transfusion-reaction pathway, COP.10.h anaesthesia events, HIC.4 needlestick, HIC.5 HAI
      case-finding, and PRE.6 complaint-described harm remain those documents. Dual entry when
      the subject meets this hospital's incident definition. Do not patch those drafts in this
      pass.

T2 one-line flags:

- [ ] **PSQ.5.c analysis / PSQ.5.d CAPA vs MOM.7 medication-event CAPA.** Hospital-wide incident
      CAPA is here; medication-event CAPA stays MOM.7. Historical "not CQI ownership of all
      CAPA" in MOM.7 is a 2nd Edition name.
- [ ] **PSQ.5.e informing stakeholders vs PRE.6 complaint redressal.** Informing is this OE;
      redressal of a patient/family complaint is PRE.6 (sibling branch).
- [ ] **ROM.4.c governance reporting of system and process failures now landed.** PSQ.5 owns the
      incident SOP; ROM.4.c (drafted 2026-08-17, UNAPPROVED) owns that management ensures
      internal and external reporting systems are implemented. Do not patch PSQ.5 in this pass.
- [ ] **Reporting time frame is hospital-defined.** Same as MOM.7: do not invent a 24-hour
      NABH mandate.

---

## Deferred from ROM.1 (drafted 2026-08-17, UNAPPROVED)

Source: official SHCO 3rd Edition PDF md5 `39e3bc86d73d651b9cfef283bbf018a9`, Chapter 7 printed
pages 109–114 (PDF indices 115–120). TOC printed page 108 is the chapter start in the table of
contents; intent is printed 109. ROM.1 printed p.110 / index 116. Header: "The organisation
identifies those responsible for governance and their roles are defined." T1 = ROM.1.a*,
ROM.1.b*, ROM.1.e*. P2 is accreditation-only. Chapter reference 23 (India Code) is a lookup,
not a named Act. Companies Act 2013 / Societies Registration Act 1860 / MSME registration
are not a checklist. Legal form is hospital-defined. OECD G20 principles and Arnwine are
frameworks, not a mandate that every SHCO is a company.

Insert ROM.1–ROM.4 as `status='draft'` only via
`python3 policies/build/apply_rom_drafts_supabase.py --insert`. The 2026-08-17 Cloud Agent VM
did not have `SUPABASE_SERVICE_ROLE_KEY`; dry-run of all four drafts passed; live POST was not
executed. No row was approved.

T1 overlap flags (full cross-check done in the ROM.1 draft Scope / universal_facts_checklist).

- [ ] **ROM.1 vs ROM.2 — governing entity vs day-to-day head.** ROM.1 identifies those
      responsible for governance and (d) appoints senior leaders. ROM.2 owns that the head has
      administrative qualifications and experience, complies with applicable legislations, and
      is reviewed. Do not use one file for both.

- [ ] **ROM.1.e ethical management framework vs PRE.1/PRE.2 patient rights vs PRE.3 consent vs
      PSQ.4 culture of safety.** Organisational ethics support is this OE. Patient rights,
      consent method and safety-culture-as-PSQ-requirement stay those documents. Do not patch
      PRE/PSQ in this pass.

T2 one-line flags:

- [ ] **ROM.1.c performance against mission vs ROM.3.d service standards vs PSQ.2 indicators vs
      ROM.2.d review of the leader.** Data may overlap; four different acts.
- [ ] **ROM.1.d appointment vs HRM employment file (undrafted).** Governance appoints; HRM files.
- [ ] **PSQ.1 committees are not this governing entity** unless this hospital has recorded that
      they are the same body — they usually are not.
- [ ] **FMS (undrafted)** is not this document.

---

## Deferred from ROM.2 (drafted 2026-08-17, UNAPPROVED)

Whole standard is Tier 2 (four OEs a–d, none asterisked). ROM.2.c is Core and still Tier 2
because it is unasterisked. Header: "The organisation is headed by a leader who shall be
responsible for operating the organisation on a day-to-day basis." P2 is accreditation-only
despite ROM.2.c being about legislation: the bibliography names India Code as a repository,
not an Act. Dumping Companies Act / Societies / CEA / CPA / MHCA as a checklist would be the
AAC.1 defaulted-statute bug. Applicable list is hospital-defined from legal form and AAC.1
services. Clay-Williams / Daly are frameworks, not a mandate that the head is (or is not) a
doctor.

T2 one-line flags:

- [ ] **ROM.1.d appointment vs this qualifications/experience.** See ROM.1 T1 flag.
- [ ] **ROM.1.c organisation-against-mission vs ROM.2.d review of the leader.**
- [ ] **PSQ.4 leader awareness of the safety programme vs this administrative-head OE.**
- [ ] **HRM (undrafted) employment file.** This document names the administrative requirements;
      HRM files certificates.
- [ ] **AAC.1 defined services vs the applicable-legislation register.** Unused services do not
      invent a statute.
- [ ] **Owning documents keep their own statutes** (HIC.3 BMW, MOM.8 NDPS, AAC.5 PC-PNDT). This
      step owns that the leader is responsible for the applicable set as a whole.

---

## Deferred from ROM.3 (drafted 2026-08-17, UNAPPROVED)

T1 = ROM.3.d* only. Header: "The organisation displays professionalism in its functioning."
Official ROM.3.e uses "organization". P2 is accreditation-only. No rupee figure as a NABH
mandate. **PSQ.4.c budget-earmark forward-ref ACCEPTED:** this OE approves the annual budget;
PSQ.4.c earmarks programme funds from it.

T1 overlap flags:

- [ ] **ROM.3.d measurable service standards vs AAC.1 defined services vs PSQ.2 key indicators.**
      AAC.1 names what is offered. PSQ.2 owns indicators as QI tools. This OE owns documented
      measurable service standards and monitoring them. Do not paste Annexure 1 as this set.

T2 one-line flags:

- [ ] **PSQ.4.c earmark vs this budget approval.** Handoff accepted; do not patch PSQ.4.
- [ ] **ROM.3.c committee-effectiveness review vs PSQ.1 / HIC.1 / MOM.1 owning what those
      committees do.** This OE reviews functioning; it does not rewrite those methods.
- [ ] **ROM.3.e staff rights vs PRE.1/PRE.2 patient rights vs HRM (undrafted) employment and
      grievance file.** One poster is not both patient and staff rights.
- [ ] **ROM.1.c mission performance vs this service-standard monitoring.**
- [ ] **FMS (undrafted) facility KPIs** are not this hospital-wide service-standard set counted
      twice.

---

## Deferred from ROM.4 (drafted 2026-08-17, UNAPPROVED)

T1 = ROM.4.a*, ROM.4.c*. Header: "Management ensures that patient-safety aspects and
risk-management issues are an integral part of patient care and hospital management." ROM.4.d
is Core and still Tier 2 (unasterisked). P2 is accreditation-only. ISO 31000:2018 is a
framework, not a certified-system mandate. Indian Contract Act 1872 is not imported.
**PSQ.1.c / COP.12 / PSQ.5 forward-refs ACCEPTED** without absorbing those methods.

T1 overlap flags:

- [ ] **ROM.4.a vs PSQ.1.c vs COP.12 vs PSQ.5 — CRITICAL FOUR-WAY SPLIT ACCEPTED.** PSQ.1.c is
      quality-system proactive analysis of patient-safety risks. COP.12 is bedside
      vulnerable/falls/PU/VTE tools. PSQ.5 is after-the-fact incidents. This OE is management
      ensuring organisation-wide proactive risk across care and hospital management. Do not
      patch PSQ or COP.12 in this pass.

- [ ] **ROM.4.c vs PSQ.5 — CRITICAL SPLIT ACCEPTED.** PSQ.5 is the incident SOP. This OE is
      management ensuring systems for internal and external reporting of system and process
      failures. Dual entry when a clinical incident is also a process failure. PRE.6 remains
      complaint redressal; MOM.7 remains medication-event capture.

T2 one-line flags:

- [ ] **ROM.4.b integration vs PSQ.1 QI programme vs ROM.3.a strategic plan.** This OE owns that
      they talk to each other; it does not rewrite those documents.
- [ ] **PSQ.4 culture of safety vs this risk register.** Culture is PSQ.4.a; the risk duty is here.
- [ ] **ROM.4.d/e outsourcing vs AAC.4/AAC.5/HIC.6 owning method** where the work is laboratory,
      imaging or CSSD. This document owns the agreement with service parameters and monitoring.
- [ ] **AAC.1 unused outsourced services** are a recorded absence, not a copied SLA.
- [ ] **FMS (undrafted) facility inspection rounds / fire plan.** Management risk duty includes
      those domains; FMS writes the facility method.
- [ ] **Reporting time frame is hospital-defined.** Same as PSQ.5 / MOM.7: no 24-hour NABH clock.

---

## Deferred from AAC.2–AAC.8 (drafted 2026-08-17, UNAPPROVED)

These seven drafts are local only. Nothing has been written to Supabase. Flags below are
the overlap / forward-reference notes from that pass, logged so they are not lost if the
standards are approved on different days.

### Intra-chapter divisions (stated in both Scopes; not contradictions)

- [ ] **AAC.2.f vs AAC.7.d.** AAC.2 owns transfer-in from another organisation, transfer-out
      to another organisation, and referral of a patient this hospital cannot accept. AAC.7
      owns transfer of a patient from one unit of this hospital to another. Keep the pair
      if one is approved without the other.
- [ ] **AAC.2.b vs AAC.8.b.** AAC.2 generates the unique identification number at registration.
      AAC.8 requires that number as content of the discharge summary. Not a duplication of method.
- [ ] **AAC.4.e vs AAC.5.e.** Critical laboratory values vs critical imaging findings. Separate
      lists and separate registers, by design.
- [ ] **AAC.5.a vs AAC.6.e.** AAC.5 owns imaging *licences* (AERB, PC-PNDT registration). AAC.6
      owns imaging *safety signage* (trefoil, restricted area, pregnancy caution, PC-PNDT notice).

### Against the approved set (HIC.1–6 + AAC.1)

- [ ] **AAC.6.a vs approved HIC.2** (T2 one-line for AAC.6.b; full statement in AAC.6 Scope
      because AAC.6.a is Tier 1). HIC.2 already applies in laboratory specimen-handling areas
      (hand hygiene, standard/TBP PPE, bloodborne-pathogen sharps). AAC.6 owns the laboratory
      safety programme as a whole (biosafety cabinets, chemical hygiene, fire, reagent spills,
      lab-specific PPE beyond standard precautions). Not a contradiction if both Scopes stay
      as drafted; check on approval that HIC.2 is not reopened.
- [ ] **AAC.4.c / AAC.6.a vs approved HIC.3 BMW.** HIC.3 owns the hospital-wide colour code,
      internal transport, SPCB authorisation and common-facility handover, including that
      microbiological and laboratory waste is pre-treated before disposal where the rules
      require it. AAC.4 owns the laboratory specimen pathway up to placing waste in that
      stream, including the laboratory's own pre-treatment. AAC.6 names pre-treatment as a
      lab-safety duty pointing at HIC.3's stream. Neither AAC draft restates the four colours.
- [x] **AAC.3.e vs approved HIC.5 — shared data point, not a shared process. Checked in full
      2026-08-17; division written into AAC.3 Scope and step 6. HIC.5 not reopened.**
      Shared: the temperature and vital signs record. HIC.5 step 4 reads that chart as one
      case-finding source (new fever after a defined period from admission); step 8 uses
      recorded temperature as a VAE criterion where invasive ventilation is provided. AAC.3.e
      owns taking the observations, the early-warning method, the call and the intervention.
      Two processes, one chart. An escalated deterioration is not an infection report; a
      surveillance case is not an early-warning call. No contradiction; no HIC.5 text change.
- [ ] **AAC.4.e vs approved HIC.5** alert-organism notification. AAC.4 owns critical results
      to the treating clinician. HIC.5 owns notifying the infection control team of isolates
      on the alert-organism list. Same laboratory, two addressees, two purposes.
- [ ] **AAC.7.c vs approved HIC.2** (T2 one-line). HIC.2 requires the precaution category in
      the nursing handover. AAC.7 owns the handover *method*. Infection-control content of
      the handover stays in HIC.2.

### Forward references (undrafted owners)

- COP emergency / critical care / CPR — life-stabilising treatment (AAC.2), deterioration
  response method (AAC.3.e).
- IMS — medical record structure (AAC.2.b, AAC.3, AAC.8).
- PRE — consent and rights at admission (AAC.2); patient-education method (AAC.8.d).
- HRM — credentialing behind lab/imaging personnel (AAC.4.b, AAC.5.c) and the "qualified
  individual" (AAC.7.a). Already flagged from AAC.1.b for HRM.7–9; same pass.
- FMS — hospital-wide equipment programme / fire plans, vs lab and imaging calibration
  and lab fire as named in AAC.4.h / AAC.5.i / AAC.6.

---

## Cross-cutting: document control scaffolding

Not a content gap — a **format** gap found against NABH's sample policy
(`C.-HIB_POLICY-01_Policy-on-Information-Management-System.docx`). Applies to every master policy,
not just HIC.2.

Decide whether these belong in the schema or in the document renderer:

> Partly out of date as of 2026-08-06. The workaround this section originally described — where
> abbreviations lived in `procedure_steps[0]` and the disclaimer was appended to `distribution` —
> is gone: `shco_policy_masters` gained dedicated `abbreviations` and `disclaimer` columns, and
> HIC.1-HIC.4 all use them. What remains genuinely missing is version/revision history; see the
> version-and-revision-history TODO under "Deferred from HIC.4" above, which supersedes the
> "Rev. No." part of the first bullet and the Amendment Sheet bullet below and already records
> the design decisions (version as text, revision history as jsonb on the row).

- [ ] **Document control block** — Doc No., Issue No., Rev. No., No. of Pages, Date Created,
      Date of Implementation, and a `Page X of Y` running header.
- [ ] **Prepared By / Approved By / Responsibility of Updating** signature block
      (Designation / Name / Signature).
- [ ] **Amendment Sheet** — Sr No, Section & Page, Details of Amendment, Reasons, and signatures of
      the preparatory and approving authorities.
- [ ] **Table of contents** with page numbers.

These are all per-hospital values, so the renderer is probably the right home — but nothing in the
pipeline produces them today, so right now they simply do not exist.
