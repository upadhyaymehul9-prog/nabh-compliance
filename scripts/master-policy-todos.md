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

- [ ] **AAC.2.e vs COP.2.c triage.** AAC.2.e already writes a triage or prioritisation method at the emergency area and OPD for ACCESS (including expected time-to-assessment per category as a hospital-defined value). COP.2.c (asterisked) owns ED triage that guides INITIATION OF APPROPRIATE CARE. The COP.2 draft states they may share a local tool and are not the same act. Reconcile so AAC.2.e does not silently own ED clinical pathways and COP.2.c does not take over OPD queuing. AAC.2.e's time-to-assessment must not be read as a COP.2 numeric mandate.

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

- [ ] **COP.9.b sedation consent before the drug vs PRE general consent method.** PRE (undrafted) owns how consent is explained/recorded/witnessed; COP.9.b owns that sedation consent is obtained before the sedative is given.

- [ ] **COP.9 vs MOM drug-storage (NDPS / D&C).** Forward-ref. COP.9 does not write cupboard/register/destruction and does not inherit NDPS as a storage statute.

- [ ] **COP.9 vs COP.11 procedure/WHO checklist.** COP.9 owns the sedation given so a procedure can be performed; COP.11 owns the procedure. Stated in COP.9 Scope.

- [ ] **HIC.4 "sedation" hits (ICU ventilator sedation scale / daily interruption).** Incidental; not this document.

---

## Deferred from COP.10 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.10 draft Scope / universal_facts_checklist).

- [ ] **COP.9 sedation vs COP.10 anaesthesia vs COP.11 surgery.** COP.9 owns procedural sedation; COP.10 owns the anaesthetic (plan, monitoring under anaesthesia, post-anaesthesia recovery); COP.11 owns the surgical procedure, site-marking, WHO-framework checklist and operation notes. They meet in the theatre; they are not the same document.

- [ ] **HIC.6 anaesthesia equipment reprocessing.** COP.10 requires processed circuits/masks/blades; HIC.6 owns the cycle, indicators and recall. Stated in COP.10 Scope and step 1.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.10.d anaesthesia consent vs PRE general consent method.** PRE (undrafted) owns the method; COP.10.d owns that anaesthesia consent is obtained before induction.

- [ ] **COP.10.g type+drugs in the record vs MOM medication process.** MOM (undrafted) owns storage and the medication process; COP.10 owns anaesthetic care and that type and anaesthetic medicines appear in the patient record. MOM must not restate anaesthetic method.

- [ ] **COP.10.e monitoring under anaesthesia vs HIC.4 SSI-bundle temperature/glycaemia.** Bundle stays HIC.4 even when the anaesthetist is the person who maintains those variables.

- [ ] **COP.10.h intra-operative adverse anaesthesia events vs a future PSQ incident policy.** This requires anaesthesia events to be recorded and reviewed; it does not write the hospital-wide incident system.

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

- [ ] **COP.9.b sedation consent before the drug vs PRE general consent method.** PRE (undrafted) owns how consent is explained/recorded/witnessed; COP.9.b owns that sedation consent is obtained before the sedative is given.

- [ ] **COP.9 vs MOM drug-storage (NDPS / D&C).** Forward-ref. COP.9 does not write cupboard/register/destruction and does not inherit NDPS as a storage statute.

- [ ] **COP.9 vs COP.11 procedure/WHO checklist.** COP.9 owns the sedation given so a procedure can be performed; COP.11 owns the procedure. Stated in COP.9 Scope and in the COP.11 flag below.

- [ ] **HIC.4 "sedation" hits (ICU ventilator sedation scale / daily interruption).** Incidental; not this document.

---

## Deferred from COP.10 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.10 draft Scope / universal_facts_checklist).

- [ ] **COP.9 sedation vs COP.10 anaesthesia vs COP.11 surgery.** COP.9 owns procedural sedation; COP.10 owns the anaesthetic (plan, monitoring under anaesthesia, post-anaesthesia recovery); COP.11 owns the surgical procedure, site-marking, WHO-framework checklist and operation notes. They meet in the theatre; they are not the same document.

- [ ] **HIC.6 anaesthesia equipment reprocessing.** COP.10 requires processed circuits/masks/blades; HIC.6 owns the cycle, indicators and recall. Stated in COP.10 Scope and step 1.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.10.d anaesthesia consent vs PRE general consent method.** PRE (undrafted) owns the method; COP.10.d owns that anaesthesia consent is obtained before induction.

- [ ] **COP.10.g type+drugs in the record vs MOM medication process.** MOM (undrafted) owns storage and the medication process; COP.10 owns anaesthetic care and that type and anaesthetic medicines appear in the patient record. MOM must not restate anaesthetic method.

- [ ] **COP.10.e monitoring under anaesthesia vs HIC.4 SSI-bundle temperature/glycaemia.** Bundle stays HIC.4 even when the anaesthetist is the person who maintains those variables.

- [ ] **COP.10.h intra-operative adverse anaesthesia events vs a future PSQ incident policy.** This requires anaesthesia events to be recorded and reviewed; it does not write the hospital-wide incident system.

---

## Deferred from COP.11 (drafted 2026-08-17, UNAPPROVED)

T1 overlap flags (full cross-check done in the COP.11 draft Scope / universal_facts_checklist). Do not patch approved HIC.4/HIC.5/HIC.6 in this pass — reconcile when the owning document is next opened.

- [ ] **HIC.4 SSI bundle vs COP.11 surgical process — shared surgical-safety checklist artefact.** HIC.4 evidence already lists "completed surgical safety checklist" as SSI-bundle evidence. COP.11.d (asterisked Core) owns the checklist as the team's pause (WHO Safe Surgery 2009 as framework; hospital checklist is [Hospital to define]; WHO items not pasted as mandated verbatim). Completing a checklist is not completing the SSI bundle; running the SSI bundle is not marking the site. HIC.4 should keep antibiotic timing, hair, glucose, skin prep, normothermia as IPC process. Do not patch HIC.4 until a dedicated pass.

T2 one-line flags (standing rule: flag and move on):

- [ ] **COP.11.e standard precautions in OT vs HIC.2.** Follow HIC.2; do not rewrite PPE. Stated in COP.11 Scope and step 5.

- [ ] **COP.11.h process QA vs HIC.5 SSI surveillance.** Process look vs outcome look / NHSN definitions. Stated in step 8.

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
