# HCO Full Accreditation — ROM chapter OE inventory

## Sources

OE text, counts, levels, CORE/Commitment/Achievement/Excellence, and asterisks:
official portal **Standards** PDF (January 2025), `pdftotext` at
`policies/source/hco6_rom_ocr.txt` (printed pages 132–137 / PDF pages 143–148
for body; summary 143–144; references 149–150).

Interpretation depth: scanned **Guidebook** `policies/source/NABH 6th Edition
Standards & Guidebook-1.pdf` (md5 `2c4489ee98de4ae9b49cba168ea9f42a`).
**Verified ROM Intent at PDF page 239** (idx 238). **FMS Intent at PDF page 255**
(idx 254). OCR PDF pages 239–254 (idx 238–253, inclusive of ROM references) →
`policies/source/hco6_rom_guidebook_ocr.txt`.
Cleaned notes: `policies/source/hco6_rom_interpretations.json` (37 blocks, 1:1).

Official chapter name is **Responsibilities of Management (ROM)** (plural).
HCO output uses ROM only (`HCO/ROM/POL/xx`, `HCO.ROM.n`, `hco_rom{n}_v2_draft.json`).

Do not re-derive OE counts/levels/asterisks from the Guidebook.

## Chapter totals (portal summary = body)

- Standards: **6**
- Objective elements: **37**
- CORE 4 / Commitment 23 / Achievement 8 / Excellence 2

| Standard | OEs | letters | CORE | * asterisks |
|---|---|---|---|---|
| ROM.1 | 9 | a–i | a | a, b, c, f |
| ROM.2 | 4 | a–d | a | a, b |
| ROM.3 | 7 | a–g | none | b |
| ROM.4 | 5 | a–e | b | none |
| ROM.5 | 6 | a–f | none | b, e, f |
| ROM.6 | 6 | a–f | a | a, d |

Matrix agrees with body levels for every letter.

## Proposed judgment calls (need approval)

### Stop-work

**Proposed default: stop-work on ROM.6 only.** None on ROM.1–5 (governance,
ethics, ESG, leadership, professionalism — no procedure-start gate).

- **ROM.6** — start or continue an outsourced service without a documented
  agreement that includes service parameters; skip required internal/external
  reporting of a system or process failure.

### Statute P2

**Proposed default: accreditation-only on all ROM.1–6.**

- **ROM.2.c** Guidebook lists Companies Act, Charitable Trust Act, Societies
  Registration Act, LLP Act as *ownership vehicles for disclosure*, not as a
  checklist for the whole standard.
- **ROM.4.b** is CORE “applicable legislations, regulations and notifications”
  without naming an Act. Method: keep an applicable-legislation register (India
  Code as lookup). Research/clinical trials “in accordance with statutory
  norms” stay in the method note.
- **ROM.6.d** names **AERB** as the example external agency for a radiation-source
  failure. Kept in the method note, not as statute P2 (same pattern as IPC.8 PEP).
- **ROM.3.c** “corporate social responsibility” as a regulatory example. Not a
  named Act on the whole standard.

### Wording kept as printed / flagged

- **ROM.1.i** printed as **“I.”** Inventory letter is `i`.
- **ROM.3** Standard: summary “sustainability in **hospital**” vs body
  “**hospitals**”. Inventory uses the **body**.
- **ROM.6** Standard: summary “**Management** ensures” vs body “**Leadership**
  ensures”. Intent says “Leaders ensure”. Inventory uses the **body**.
- **ROM.3.c** “organisations social responsibility” (no apostrophe). Kept.
- **ROM.6.b** body wrap “risk- reduction”; **ROM.6.c** “risk- management”.
  Inventory keeps the joined body form.
- Official chapter title is **Responsibilities** (plural), not “Responsibility”.
- **ROM.1.g** Guidebook OCR bleed `il CORE ty.` (chrome from the next page)
  stripped after approval — interpretation now ends at “education and research.”
- **ROM.4.b** OCR tilde `ensure ~ continuity` stripped after approval —
  now `ensure continuity`.

### Prepared by

Proposed default: **Medical Superintendent** for ROM.1, 2, 3, 4, 6;
**Quality Coordinator** for ROM.5 (plans, committees, service standards,
change management).

## OCR pipe-character note

ROM Guidebook OCR produced **no** token-start `|n`. MOM hardened fix still
applied. No `oIn` / `wheIn` / `takeIn` / `informatioIn` in interpretations.

## File layout

  builders: policies/build/build_hco_rom{N}_v2.py
  drafts: policies/drafts_hco/hco_rom{N}_v2_draft.json
  masters: policies/build/masters_hco/HCO.ROM.{N}_v2_master.docx
  previews: policies/build/preview_hco/HCO.ROM.{N}_v2_preview.docx|.md
  doc_no: «HCO/ROM/POL/{NN}»
  programme: HCO Full Accreditation, 6th Edition

Do not write to SHCO folders.
Do not touch AAC, COP, MOM, PRE, IPC, or PSQ.
