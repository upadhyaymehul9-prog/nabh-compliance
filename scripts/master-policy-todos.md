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
         `policy_placeholder_audit.py` now reports the correct figure for all three; run
         `python build_hic3.py` to reproduce it. Check HIC.1 at the same time: its checklist
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

      **To build, in the same pass as version and revision history:**
      1. migration: `alter table public.shco_policy_masters add column author_byline text;`
         (alongside `version` → text and the `revision_history` jsonb column)
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

- [ ] **DATA ERROR: `shco_full_oes` is missing the asterisk on HIC.6.e.** Found 2026-08-07 while
      verifying the asterisk-position note above. **Not fixed — this is a production write to a
      table the app reads, so it needs your go-ahead.**

      **The discrepancy.** The official SHCO 3rd Edition PDF, printed p.96 (PDF page index 102),
      carries an asterisk on **four** HIC.6 objective elements — b, c, d **and e**:

      > `Commitment e. The established recall procedure is implemented when a breakdown in the`
      > `sterilisation system is identified. *`

      `shco_full_oes` has `doc_required = true` for HIC.6.b, c and d, but **`false` for HIC.6.e**.
      Verified twice: once by reading the extracted page and once by re-extracting with the
      asterisk-bearing lines marked, to rule out a stray footnote glyph. The asterisk is on the
      wrapped second line of OE e, exactly as it is for b and c.

      **Why it matters.** HIC.6.e is the recall procedure — the OE that requires documented
      evidence of what the hospital does when a sterilisation failure is discovered after items
      have been issued. If HIC.6 is drafted against the DB rather than the PDF, that OE will be
      built as an ordinary Commitment element and will be under-evidenced in the one place an
      assessor is most likely to ask for a document.

      **Also check the rest of the table.** One wrong flag suggests the extraction that populated
      `doc_required` mishandled asterisks on wrapped lines generally. Before drafting HIC.6, spot
      -check every chapter's asterisks against the PDF, not just HIC. The three HIC.5 flags and the
      six HIC.4 flags were verified during those drafts and are correct.

      **Fix:** `update public.shco_full_oes set doc_required = true where oe_code = 'HIC.6.e';`
      — after confirming the wider audit, so it is done once rather than piecemeal.

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
