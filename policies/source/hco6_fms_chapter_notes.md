# HCO Full Accreditation — FMS chapter OE inventory

## Sources

OE text, counts, levels, CORE/Commitment/Achievement/Excellence, and asterisks:
official portal **Standards** PDF (January 2025), `pdftotext` at
`policies/source/hco6_fms_ocr.txt` (printed pages 140–149 / PDF pages 151–161
for body; summary 151–152; references through printed 149). HRM starts printed
page 150 / PDF page 162.

Interpretation depth: scanned **Guidebook** `policies/source/NABH 6th Edition
Standards & Guidebook-1.pdf` (md5 `2c4489ee98de4ae9b49cba168ea9f42a`).
**Verified FMS Intent at PDF page 255** (idx 254). **HRM Intent at PDF page 274**
(idx 273). OCR PDF pages 255–273 (idx 254–272, inclusive of FMS references) →
`policies/source/hco6_fms_guidebook_ocr.txt`.
Cleaned notes: `policies/source/hco6_fms_interpretations.json` (43 blocks, 1:1).

Official chapter name is **Facility Management and Safety (FMS)**.
HCO output uses FMS only (`HCO/FMS/POL/xx`, `HCO.FMS.n`, `hco_fms{n}_v2_draft.json`).

Do not re-derive OE counts/levels/asterisks from the Guidebook.

## Chapter totals (portal summary = body)

- Standards: **7**
- Objective elements: **43**
- CORE 11 / Commitment 29 / Achievement 2 / Excellence 1

| Standard | OEs | letters | CORE | * asterisks |
|---|---|---|---|---|
| FMS.1 | 5 | a–e | a, c | none |
| FMS.2 | 6 | a–f | c, d | none |
| FMS.3 | 6 | a–f | e | a, d, e, f |
| FMS.4 | 8 | a–h | c | c, h |
| FMS.5 | 8 | a–h | c | c, f, g |
| FMS.6 | 5 | a–e | b, d | a, c |
| FMS.7 | 5 | a–e | a, b | a, b, e |

Matrix agrees with body levels for every letter.

## Proposed judgment calls (defaults **written** into drafts)

### Stop-work

**Proposed default: stop-work on FMS.2, 3, 4, 5, 6, 7. None on FMS.1**
(inspection rounds and device lists — no procedure-start gate).

- **FMS.2** — start or continue clinical care in an area without potable water or electricity (unless the FMS.7 continuity plan is running).
- **FMS.3** — use a hazardous material that is not identified, or for which there is no implemented spill plan.
- **FMS.4** — run critical utility equipment with no implemented operational/maintenance plan, or known unsafe.
- **FMS.5** — use medical equipment past due PM/calibration, or under an open recall/hazard notice.
- **FMS.6** — use a medical-gas outlet/manifold with a live leak, silenced required alarm, or no required alternate source.
- **FMS.7** — occupy a patient-care floor without required fire detection/abatement/evacuation provision, or without a displayed exit plan.

### Statute P2

**Proposed default: statute P2 on FMS.5 and FMS.6. Accreditation-only on FMS.1–4 and FMS.7.**

- **FMS.5** Guidebook names Gazette of India GSR 78(E) 2023 / Medical Devices Rules 2023 and Materiovigilance Programme of India. **Written as P2.**
- **FMS.6** Guidebook names Indian Explosives Act, Gas Cylinder Rules and Static and Mobile Pressure Vessels (Unfired) Rules. **Written as P2.**
- **FMS.2.b** “as per statutory requirements” with no named Act. Method keeps drawings as required by the registering authority (same pattern as ROM.4.b).
- **FMS.2.a** names AERB as an example for radiation infrastructure. Method note only.
- **FMS.2.d/e** IS 10500 and National Building Code as water/power references. Not P2.
- **FMS.3.b** Indian Seismic Code IS 1893 (Part 1). Code, not an Act. Method note only.
- **FMS.3.c** National Electrical Code of India 2023 as a reference. Not P2.
- **FMS.7** NABH fire-safety advisory, NBC, NDMA/SDMA/DDMA. Method notes, not P2.

### Wording kept as printed / flagged

- **FMS.1.e** wrap “risk- assessment”. Kept.
- **FMS.2** Standard: “operate … and **promotes**” (grammar as printed).
- **FMS.4.d** “Utility equipment, are” (comma as printed).
- **FMS.5.h** “breakdown” (singular) vs **FMS.4.g** “breakdowns”. Each kept.
- **FMS.7.b** “identification, and management” (comma as printed).
- TOC on portal PDF printed page 9 uses “Responsibility of Management” (singular) for ROM — not an FMS issue; already flagged on ROM.

### Prepared by

**Written default: Engineering In-Charge** for FMS.1–7. Biomedical competence sits in FMS.5 methods (Guidebook: biomedical / instrumentation engineer or technologist). Not “Maintenance In-Charge” (banned PRE leftover).

## OCR strips **written** into `hco6_fms_interpretations.json` before generate

Not flagged-and-left. Applied as the proposed default:

- Chrome tails stripped (CORE/Commitment/Excellence row leftovers on FMS.2.c, 3.c, 4.c, 4.g, 5.b, 5.g, 6.d, 7.a, 7.c).
- Page-break reconstructions **written**: FMS.4.a (DG sets, Chiller plant + collaborative process); FMS.5.f (strategic **plans**, …); FMS.2.f “Refer to FMS.2.d.”
- Pipe-OCR `|S: 1893` reconstructed as **IS: 1893**.
- Letter repairs: Ata→At a, anq/ang→and, The_organisation→The organisation, prescribeq→prescribed, ¢ display→* display, case offire→case of fire, tillthe→till the, etc.

## File layout

  builders: policies/build/build_hco_fms{N}_v2.py
  drafts: policies/drafts_hco/hco_fms{N}_v2_draft.json
  masters: policies/build/masters_hco/HCO.FMS.{N}_v2_master.docx
  previews: policies/build/preview_hco/HCO.FMS.{N}_v2_preview.docx|.md
  doc_no: «HCO/FMS/POL/{NN}»
  programme: HCO Full Accreditation, 6th Edition

Do not write to SHCO folders.
Do not touch AAC, COP, MOM, PRE, IPC, PSQ, or ROM.
