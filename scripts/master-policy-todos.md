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

- [ ] **HIC.3 promises a record the hospital does not routinely produce — environmental surface
      swabs.** Discrete edit to HIC.3, broken out of the reconciliation item above so it is not
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

- [ ] **`HIC.2.c` is asterisked in the PDF but left `doc_required = false` — flip it in the
      reconciliation pass, and add the evidence anchor at the same time.** Broken out of the
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

- [ ] **AUTHORED-CONTENT DEBT: HIC.1 and HIC.2 have no evidence or responsible data at all, so
      they render no Required Records / Evidence Checklist section. This is missing CONTENT, not a
      missing feature.** Confirmed on instruction 2026-08-11. Do it in the reconciliation pass,
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

      **What has NOT been done, and must be, before the fix is applied:** the correct wording has
      not been read out of the official SHCO 3rd Edition PDF. Do not write it from memory or infer
      it from the OE list — read the standard header on the page, the same discipline the asterisk
      audit used. `scripts/asterisk_extract.py` already parses these headers and can be pointed at
      the MOM chapter to produce the authoritative string.

      **Scope of the fix when it is made:** `scripts/shco_oes_data.json`,
      `scripts/shco_oes_by_chapter.json` (same text, denormalised per OE row) and the
      `standard_text` column on all six `MOM.5.*` rows in `shco_full_oes`. Check the same day
      whether any other standard shares its text with a neighbour — this was found by eye while
      reading a table, not by a check that would have caught a second instance. A one-line
      `group by standard_text having count(distinct standard_code) > 1` over the whole table
      settles it for all 408 OEs at once.

      No app-facing urgency: nothing renders `standard_text` for MOM today, because no MOM master
      policy exists. It becomes urgent the moment MOM drafting starts.

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
