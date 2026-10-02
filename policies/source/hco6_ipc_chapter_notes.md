# HCO Full Accreditation — IPC chapter OE inventory

## Sources

OE text, counts, levels, CORE/Commitment/Achievement/Excellence, and asterisks:
official portal **Standards** PDF (January 2025), `pdftotext` at
`policies/source/hco6_ipc_ocr.txt` (printed pages 110–118 / PDF pages 122–129).

Interpretation depth: scanned **Guidebook** `policies/source/NABH 6th Edition
Standards & Guidebook-1.pdf` (md5 `2c4489ee98de4ae9b49cba168ea9f42a`).
Printed TOC is around page 187; verified **IPC Intent at PDF page 196**
(0-based idx 195); **PSQ Intent at PDF page 216** (idx 215). OCR PDF pages
196–215 (idx 195–214) → `policies/source/hco6_ipc_guidebook_ocr.txt`.
Cleaned notes: `policies/source/hco6_ipc_interpretations.json` (49 blocks, 1:1).

HCO 6th Edition chapter name is **IPC** (Infection Prevention and Control).
SHCO 3rd Edition uses HIC for the equivalent chapter. HCO output uses IPC only
(`HCO/IPC/POL/xx`, `HCO.IPC.n`, `hco_ipc{n}_v2_draft.json`). SHCO HIC files
were not touched.

Do not re-derive OE counts/levels/asterisks from the Guidebook.

## Chapter totals (portal summary = body)

- Standards: **8**
- Objective elements: **49**
- CORE 13 / Commitment 33 / Achievement 3 / Excellence 0

| Standard | OEs | letters | CORE | * asterisks |
|---|---|---|---|---|
| IPC.1 | 10 | a–j | a | a, b, e, f, g, h |
| IPC.2 | 4 | a–d | a, c | none |
| IPC.3 | 6 | a–f | a, b, d, f | a, b, c, d, e |
| IPC.4 | 6 | a–f | c, d | a, b, c, e, f |
| IPC.5 | 4 | a–d | none | none |
| IPC.6 | 9 | a–i | a, d, f | h |
| IPC.7 | 5 | a–e | b | b, c, d, e |
| IPC.8 | 5 | a–e | none | a, b, e |

Matrix agrees with body levels for every letter.

## Proposed judgment calls (need approval)

### Stop-work

**Proposed default: stop-work on IPC.3, 4, 5, 7, 8.** None on IPC.1 (programme
governance) or IPC.2 (resources — PPE-not-available is gated via IPC.3).

- **IPC.3** — procedure without standard precautions / hand hygiene / safe
  injection; restricted antimicrobial off the stewardship path.
- **IPC.4** — BMW without segregation or PPE; construction/renovation without
  the infection-risk plan.
- **IPC.5** — insert Foley / central line / start ventilation / incision without
  the matching HAI bundle.
- **IPC.7** — issue from sterile store when validation failed or recall is in
  effect.
- **IPC.8** — work against a restriction; skip PEP after a blood/body-fluid
  exposure.

### Statute P2

**Proposed default: statute P2 on IPC.4 only**, for Biomedical Waste Management
Rules (Guidebook IPC.4.d: colour-coded bags, storage, authorised vendor,
monitoring “as per statutory provisions”). Kitchen “statutory requirements”
(IPC.4.f) stay in the method note, not as a second Act on the whole standard.

IPC.8 immunisation “applicable statutory requirements” and PEP “national and/or
international guidelines” stay accreditation-only (NACO/national PEP named in
the method note, not as a statute P2). Same pattern as PRE.2 privileged
communication.

### Wording kept as printed

- **IPC.1.i** and **IPC.6.i** printed as **“I.”** Inventory letter is `i`.
- **IPC.1.f** body: “infection **P**revention and control team” (capital P).
- **IPC.3.e** has **no terminal period** before the asterisk (“documented *”).
- **IPC.5** Standard: summary “Infections (HAI)” vs body “infections (HAI)”.
  Inventory uses the **body** (lowercase).
- **IPC.5.a** OE: “urinary tract **I**nfections” (capital I). Kept.
- **IPC.5.b** “ventilator- associated” (space after hyphen). Kept.
- **IPC.7** Standard: summary “**sterilization**” vs body “**sterilisation**”.
  Inventory uses the **body** (British spelling).
- **IPC.8** heading: two-column bleed from IPC.6.h in `pdftotext`. Title
  reconstructed from the summary table + remaining body lines so it matches
  “prevent or reduce healthcare associated infections in its staff.” Flagged,
  not invented.

### Prepared by IPC.8

Proposed default **Occupational Health Physician**. If this hospital has no OH
physician, reassign to the Infection Prevention and Control Officer.

## OCR pipe-character note

IPC Guidebook OCR produced **no** token-start `|n`. MOM hardened fix still
applied. No `oIn` / `wheIn` / `takeIn` / `informatioIn` in interpretations.

## File layout

  builders: policies/build/build_hco_ipc{N}_v2.py
  drafts: policies/drafts_hco/hco_ipc{N}_v2_draft.json
  masters: policies/build/masters_hco/HCO.IPC.{N}_v2_master.docx
  previews: policies/build/preview_hco/HCO.IPC.{N}_v2_preview.docx|.md
  doc_no: «HCO/IPC/POL/{NN}»
  programme: HCO Full Accreditation, 6th Edition

Do not write to SHCO folders. Do not overwrite SHCO `hic*_v2_*`.
Do not touch AAC, COP, MOM, or PRE.
