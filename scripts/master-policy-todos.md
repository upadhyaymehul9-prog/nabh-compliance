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

      This supersedes the "Amendment Sheet" and "Rev. No." bullets in the cross-cutting section
      below, which describe the same gap in less specific terms.

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
