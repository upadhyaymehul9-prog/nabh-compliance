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

### → CQI (continuous quality improvement)

- [ ] **Full HAI surveillance methodology.** VAP/VAE, CLABSI, CAUTI and SSI — standard case
      definitions, numerator/denominator collection, device-day counting, rate calculation,
      benchmarking and feedback loops. (Checklist row 9, tagged CQI 2 a.)
      The HIC.2 draft carries a **brief pointer only**, by design — it names the four infection
      types and cites CDC NHSN as the definitions source, then defers method to the owning standard.
      Existing hook: the app's KPI module already carries SSI at `kpi_no` 52.

---

## Cross-cutting: document control scaffolding

Not a content gap — a **format** gap found against NABH's sample policy
(`C.-HIB_POLICY-01_Policy-on-Information-Management-System.docx`). Applies to every master policy,
not just HIC.2.

`shco_policy_masters` has no columns for these, and the HIC.2 draft works around it
(abbreviations live in `procedure_steps[0]`, the disclaimer is appended to `distribution`).
Decide whether these belong in the schema or in the document renderer:

- [ ] **Document control block** — Doc No., Issue No., Rev. No., No. of Pages, Date Created,
      Date of Implementation, and a `Page X of Y` running header.
- [ ] **Prepared By / Approved By / Responsibility of Updating** signature block
      (Designation / Name / Signature).
- [ ] **Amendment Sheet** — Sr No, Section & Page, Details of Amendment, Reasons, and signatures of
      the preparatory and approving authorities.
- [ ] **Table of contents** with page numbers.

These are all per-hospital values, so the renderer is probably the right home — but nothing in the
pipeline produces them today, so right now they simply do not exist.
