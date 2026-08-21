# HCO Full Accreditation — MOM chapter OE inventory

Source: NABH Accreditation Standards for Hospitals, 6th Edition (January 2025),
official portal PDF:
https://portal.nabh.co/images/Standards/NABH%20Hospital%20Accreditation%20Standard%206th%20Edition%20January%202025.pdf

OCR: `policies/source/hco6_mom_ocr.txt` (pdftotext of the portal PDF, MOM chapter
starts printed page 89 / PDF page 101).

This is the **Standards** book (OE text + chapter intent). The scanned **Guidebook**
used for AAC/COP (md5 2c4489ee98de4ae9b49cba168ea9f42a, with per-OE Interpretation
paragraphs) is not available in this environment. MOM drafts are therefore
written from official OE wording + chapter intent, not from Guidebook
Interpretation blocks. That is a judgment-call flag, not a silent substitution.

## Judgment call — 11 standards, not 9

The task asked for 9 MOM standards. The official portal PDF chapter summary is:

- Standard **11**
- Objective elements **68**
- CORE **13** / Commitment **48** / Achievement **6** / Excellence **1**

SHCO 3rd Edition MOM is 9 standards. That is a different programme. These HCO
drafts cover **MOM.1–MOM.11**. MOM.10 (implantable prosthesis and medical
devices) and MOM.11 (medical supplies and consumables) are not dropped.

## Title discrepancies (body Standard line vs summary table)

Inventory titles use the **Standard** heading in the body, not the summary table,
where they differ:

- MOM.5 Standard: "Medications orders are written in a uniform manner."
  Summary: "Medication orders are written in a uniform manner."
- MOM.9 Standard: "...are used in a safe manner."
  Summary: "...are used safely."
- MOM.10 Standard: "...shall be used in accordance with laid down criteria."
  Summary: "...are used in accordance with laid down criteria."

MOM.7.i is printed as **"I."** in the portal PDF; treated as letter `i`.

## Asterisks

Asterisks are taken from `*` markers on the body OE lines (the summary matrix
does not show asterisks). `*` means the OE requires documentation.

## File layout

  builders: policies/build/build_hco_mom{N}_v2.py
  drafts: policies/drafts_hco/hco_mom{N}_v2_draft.json
  masters: policies/build/masters_hco/HCO.MOM.{N}_v2_master.docx
  previews: policies/build/preview_hco/HCO.MOM.{N}_v2_preview.docx|.md
  doc_no: «HCO/MOM/POL/{NN}»
  programme: HCO Full Accreditation, 6th Edition
  shape: same PRE/SHCO v2 14-section skeleton via pre_v2_common.emit_pre_v2
  OCR_SOURCE: policies/source/hco6_mom_ocr.txt
  PDF: official portal Standards PDF (January 2025)

Do not write to policies/drafts/, policies/build/preview/, or
policies/build/masters/ (those are SHCO). Do not overwrite SHCO `mom*_v2_*`.
