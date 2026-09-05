# HCO Full Accreditation — MOM chapter OE inventory

## Sources

OE text, counts, levels, CORE/Commitment/Achievement/Excellence, and asterisks:
official portal **Standards** PDF (January 2025), OCR at `policies/source/hco6_mom_ocr.txt`
(printed page 89 / PDF page 101).

Interpretation depth: scanned **Guidebook** `policies/source/NABH 6th Edition
Standards & Guidebook-1.pdf` (md5 `2c4489ee98de4ae9b49cba168ea9f42a`, 377 pages,
no text layer). Filename has spaces and `&`. Gitignored (`policies/source/*.pdf`).
OCR: pytesseract + pypdfium2 scale 2.2, PDF pages 149–175 (0-based 148–174) →
`policies/source/hco6_mom_guidebook_ocr.txt`. Cleaned per-OE notes:
`policies/source/hco6_mom_interpretations.json` (68 Interpretation blocks, 1:1
with inventory OEs).

Do not re-derive OE counts/levels/asterisks from the Guidebook. Portal PDF remains
authoritative for that data.

## Resolved judgment calls (2026-08-21)

- **11 vs 9**: keep all 11 (68 OEs). The earlier “9” instruction was an error.
  SHCO 3rd Edition MOM is a different programme.
- **Stop-work**: keep MOM.3, 4, 6, 7, 9. No stop-work on MOM.8 (monitoring/reporting).
- **MOM.9 statute P2**: approved (NDPS + applicable chemo/radio rules).
- **Title/letter as printed**: MOM.5 “Medications orders”; MOM.7.i printed as “I.”
  (same precedent as COP.13 CORE/Commitment).

## Title discrepancies (body Standard line vs summary table)

Inventory titles use the **Standard** heading in the body:

- MOM.5 Standard: "Medications orders are written in a uniform manner."
- MOM.9 Standard: "...are used in a safe manner."
- MOM.10 Standard: "...shall be used in accordance with laid down criteria."

## File layout

  builders: policies/build/build_hco_mom{N}_v2.py
  drafts: policies/drafts_hco/hco_mom{N}_v2_draft.json
  masters: policies/build/masters_hco/HCO.MOM.{N}_v2_master.docx
  previews: policies/build/preview_hco/HCO.MOM.{N}_v2_preview.docx|.md
  doc_no: «HCO/MOM/POL/{NN}»
  programme: HCO Full Accreditation, 6th Edition
  STANDARDS_OCR: policies/source/hco6_mom_ocr.txt
  GUIDEBOOK_OCR: policies/source/hco6_mom_guidebook_ocr.txt
  INTERP_JSON: policies/source/hco6_mom_interpretations.json

Do not write to policies/drafts/, policies/build/preview/, or
policies/build/masters/ (those are SHCO). Do not overwrite SHCO `mom*_v2_*`.
