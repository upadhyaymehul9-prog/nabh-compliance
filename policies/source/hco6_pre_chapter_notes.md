# HCO Full Accreditation — PRE chapter OE inventory

## Sources

OE text, counts, levels, CORE/Commitment/Achievement/Excellence, and asterisks:
official portal **Standards** PDF (January 2025), `pdftotext` at
`policies/source/hco6_pre_ocr.txt` (printed pages 101–109 / PDF pages 113–121).

Interpretation depth: scanned **Guidebook** `policies/source/NABH 6th Edition
Standards & Guidebook-1.pdf` (md5 `2c4489ee98de4ae9b49cba168ea9f42a`, 377 pages,
no text layer). Filename has spaces and `&`. Gitignored (`policies/source/*.pdf`).

User-cited guidebook TOC pages 167–186 are **printed** pages. Verified on the
scan: PRE **Intent of the chapter** starts at **PDF page 176** (0-based idx 175);
IPC Intent starts at **PDF page 196** (idx 195). OCR used PDF pages 176–195
(idx 175–194) → `policies/source/hco6_pre_guidebook_ocr.txt`. Cleaned per-OE
notes: `policies/source/hco6_pre_interpretations.json` (52 Interpretation
blocks, 1:1 with inventory OEs).

Do not re-derive OE counts/levels/asterisks from the Guidebook. Portal PDF remains
authoritative for that data.

## Chapter totals (portal summary = body)

- Standards: **8**
- Objective elements: **52**
- CORE 12 / Commitment 32 / Achievement 7 / Excellence 1

| Standard | OEs | letters | CORE | * asterisks |
|---|---|---|---|---|
| PRE.1 | 5 | a–e | c,d,e | a, b |
| PRE.2 | 12 | a–l | d, g | none |
| PRE.3 | 5 | a–e | a | none |
| PRE.4 | 5 | a–e | a,c,e | a, d |
| PRE.5 | 10 | a–j | a | none |
| PRE.6 | 4 | a–d | a | none |
| PRE.7 | 6 | a–f | c | c |
| PRE.8 | 5 | a–e | none | a, b, c |

Matrix in the portal summary table agrees with body levels for every letter.

## Proposed judgment calls (need approval)

### Stop-work

**Proposed default: stop-work on PRE.2 and PRE.4 only.**

- **PRE.2** — neglect/abuse in progress; examination/procedure without privacy and
  dignity; start of transfusion / anaesthesia / surgery / research / other invasive
  or high-risk care without informed consent (PRE.2.g, process owned by PRE.4).
- **PRE.4** — start a listed procedure without valid informed consent from the
  person who may consent; nurse-only signature when the performer has not explained.
- **PRE.1, 3, 5, 6, 7, 8** — no stop-work. PRE.1.d/e is the reporting and CAPA path
  for rights violations; PRE.7 is feedback/complaints; PRE.8.d is conduct, not a
  procedure-start gate.

### Statute P2

**Proposed default: statute P2 on PRE.4 only.**

Guidebook PRE.4.a names MTP Act, PC-PNDT Act, Transplantation of Human Organs Act,
and HIV and AIDS (Prevention and Control) Act 2017 / NACO HIV-testing policy as
examples of statutory requirements that shape the consent list. PRE.4.b OE text
says the consent process “adheres to statutory norms.” Same pattern as MOM.9
(NDPS named in chapter material, not in the OE line).

All other PRE standards stay **accreditation-only**. Mental Healthcare Act and
Consumer Protection Act are **not** imported as checklists. Code of Medical Ethics
(PRE.2.j records access; PRE.2.d privileged communication) stays in the method
note, not as a statute P2 for the whole standard.

### Wording kept as printed (not silently corrected)

- **PRE.2.i** is printed as **“I.”** in the portal body (same as MOM.7.i). Inventory
  letter is `i`.
- **PRE.3** Standard heading has **no terminal period** in the body.
- **PRE.4.c** prints **“it’s risks”** (apostrophe). Kept.
- **PRE.5** Standard: **“Patient and families”** (grammar) in both summary and body.
- **PRE.7** summary table: “capture patient’s feedback and to redress complaints.”
  **Body Standard** (and guidebook body): “capture patient’s feedback, **experience**
  and to redress complaints.” Inventory uses the **body** line (extra word
  “experience”). Flagged, not silently dropped.
- **PRE.8** body uses “patients and/or families”; summary uses “patients and / or
  families.” Inventory uses the body spacing.

## OCR pipe-character note

PRE Guidebook OCR produced **no** token-start `|n` (the MOM bug that turned
`on`/`when`/`taken` into `oIn`/`wheIn`/`takeIn` if replaced globally). The MOM
hardened fix is still applied: only `(^|[.\\n ])\|n\b` → `In`, then leftover `|`
stripped after targeted `detai|` → `detail` and SPIKES `, | for invitation` →
`, I for invitation`. Scan of interpretations: no `oIn` / `wheIn` / `takeIn` /
`informatioIn`.

## File layout

  builders: policies/build/build_hco_pre{N}_v2.py
  drafts: policies/drafts_hco/hco_pre{N}_v2_draft.json
  masters: policies/build/masters_hco/HCO.PRE.{N}_v2_master.docx
  previews: policies/build/preview_hco/HCO.PRE.{N}_v2_preview.docx|.md
  doc_no: «HCO/PRE/POL/{NN}»
  programme: HCO Full Accreditation, 6th Edition
  STANDARDS_OCR: policies/source/hco6_pre_ocr.txt
  GUIDEBOOK_OCR: policies/source/hco6_pre_guidebook_ocr.txt
  INTERP_JSON: policies/source/hco6_pre_interpretations.json

Do not write to policies/drafts/, policies/build/preview/, or
policies/build/masters/ (those are SHCO). Do not overwrite SHCO `pre*_v2_*`.
Do not touch AAC, COP, or MOM.
