# HCO Full Accreditation — PSQ chapter OE inventory

## Sources

OE text, counts, levels, CORE/Commitment/Achievement/Excellence, and asterisks:
official portal **Standards** PDF (January 2025), `pdftotext` at
`policies/source/hco6_psq_ocr.txt` (printed pages 119–125 / PDF pages 130–136
for body; summary 130–131; references 137–142).

Interpretation depth: scanned **Guidebook** `policies/source/NABH 6th Edition
Standards & Guidebook-1.pdf` (md5 `2c4489ee98de4ae9b49cba168ea9f42a`).
IPC guidebook OCR ended PDF page 215. **Verified PSQ Intent at PDF page 216**
(0-based idx 215). **ROM Intent at PDF page 239** (idx 238). OCR PDF pages
216–238 (idx 215–237, inclusive of PSQ references) →
`policies/source/hco6_psq_guidebook_ocr.txt`.
Cleaned notes: `policies/source/hco6_psq_interpretations.json` (46 blocks, 1:1).

HCO 6th Edition chapter name is **PSQ** (Patient Safety and Quality Improvement).
HCO output uses PSQ only (`HCO/PSQ/POL/xx`, `HCO.PSQ.n`, `hco_psq{n}_v2_draft.json`).

Do not re-derive OE counts/levels/asterisks from the Guidebook.

## Chapter totals (portal summary = body)

- Standards: **7**
- Objective elements: **46**
- CORE 8 / Commitment 28 / Achievement 7 / Excellence 3

| Standard | OEs | letters | CORE | * asterisks |
|---|---|---|---|---|
| PSQ.1 | 7 | a–g | a, g | a |
| PSQ.2 | 9 | a–i | a, i | a, b, e, f, h, i |
| PSQ.3 | 8 | a–h | b, d | none |
| PSQ.4 | 4 | a–d | a | none |
| PSQ.5 | 6 | a–f | none | none |
| PSQ.6 | 6 | a–f | none | none |
| PSQ.7 | 6 | a–f | a | a, b |

Matrix agrees with body levels for every letter. Summary table: Standard 7,
Objective elements 46, CORE 8, Commitment 28, Achievement 7, Excellence 3.

## Proposed judgment calls (need approval)

### Stop-work

**Proposed default: stop-work on PSQ.7 only.** None on PSQ.1–6 (programme
governance, indicators, projects, audit, management support — no procedure-start
gate).

- **PSQ.7** — leave a recognised sentinel event unidentified or unreported;
  skip required analysis; continue a process that analysis showed caused a
  sentinel event before agreed controls are in place (except immediate
  life-saving care). Guidebook PSQ.7.c: correction within 24 working hours;
  analysis within seven working days.

### Statute P2

**Proposed default: accreditation-only on all PSQ.1–7.** Guidebook names no Act.
PSQ.2.e says the designated individual has “knowledge of statutory
requirements” without naming an Act (same pattern as PRE.2 privileged
communication). PSQ.3.a–d require any indicator mandated by GOI / State / NABH
— that is an accreditation/mandate note, not a statute P2. PSQ.7.f stakeholder
notification sits beside any statutory notification in other hospital documents.

### Wording kept as printed / flagged

- **PSQ.2.i** printed as **“I.”** Inventory letter is `i`.
- **PSQ.1.g** body wrap produced **“patient- safety”** (hyphen + line break).
  Intent and summary use **“patient-safety”**. Inventory keeps the joined body
  form (`patient- safety`). Not silently dehyphenated.
- **PSQ.4.b** body capital **“The Quality improvement projects”**. Kept.
- **PSQ.6** Standard: “the patient safety and quality improvement programme
  **are** supported” (subject-verb as printed). Kept.
- **PSQ.1.g** Guidebook OCR `COR1.b.` repaired to **COP.1.b.** (adjacent COP
  refs in the same list). Flagged.
- **PSQ.1.a** Guidebook cross-ref **PRE.5.j** and **HRM.6.a.** kept as printed
  from the Guidebook. HCO PRE.5 lettering may not include `.j` — do not silently
  retarget.
- **PSQ.5.c** interpretation: OCR split “core” / “committee” across Commitment
  column headers. Reconstructed to “core committee / quality assurance
  committee” from the following lines. Flagged.

### Prepared by

Proposed default:

- PSQ.1, PSQ.7 — **Patient Safety Officer** (OE 1.d designates the PSO;
  incidents/sentinel sit with the PSO).
- PSQ.2, 3, 4, 5 — **Quality Coordinator**.
- PSQ.6 — **Medical Superintendent** (management support).

If this hospital has no designated Patient Safety Officer, reassign PSQ.1 and
PSQ.7 to the Quality Coordinator.

## OCR pipe-character note

PSQ Guidebook OCR produced **no** token-start `|n`. MOM hardened fix still
applied. No `oIn` / `wheIn` / `takeIn` / `informatioIn` in interpretations.

## File layout

  builders: policies/build/build_hco_psq{N}_v2.py
  drafts: policies/drafts_hco/hco_psq{N}_v2_draft.json
  masters: policies/build/masters_hco/HCO.PSQ.{N}_v2_master.docx
  previews: policies/build/preview_hco/HCO.PSQ.{N}_v2_preview.docx|.md
  doc_no: «HCO/PSQ/POL/{NN}»
  programme: HCO Full Accreditation, 6th Edition

Do not write to SHCO folders.
Do not touch AAC, COP, MOM, PRE, or IPC.
