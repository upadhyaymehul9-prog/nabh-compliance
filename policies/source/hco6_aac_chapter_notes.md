# HCO Full Accreditation — AAC chapter OE inventory
# Source: NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition
# (effective 1 Jan 2025). OCR from scanned PDF (md5 2c4489ee98de4ae9b49cba168ea9f42a).
# Wording cleaned from OCR; asterisks from PDF * markers.
# Chapter: 13 standards, 87 objective elements (Core 6 / Commitment 68 / Achievement 9 / Excellence 4).

CHAPTER_INTENT: |
  Patients are informed of the services provided by the organisation. Scope of each
  healthcare service including diagnostic and therapeutic services shall be well defined
  and made available to patients and families. Only those patients who can be cared for
  by the organisation are admitted. Emergency patients receive life-stabilising treatment
  and are then either admitted or transferred appropriately. Patients undergo initial
  assessment and periodic reassessments resulting in a care plan. Laboratory and
  imaging services are provided by competent staff in a safe environment. Patient care
  is continuous and multi-disciplinary. Preventive and promotive healthcare services are
  part of patient care. Transfer and discharge protocols are well defined. Continuity of
  care is extended to the community through home health care services.

STANDARDS:
  AAC.1: The organisation defines and displays the healthcare services that it provides. (a–d, 4) * on c
  AAC.2: The organisation has a well-defined registration and admission process. (a–e, 5) * on a,d,e; Core b
  AAC.3: There is an appropriate mechanism for transfer (in and out) or referral of patients. (a–d, 4) * on a,b
  AAC.4: Patients cared for by the organisation undergo an established initial assessment. (a–g, 7) * on a,b,c; Core a,e
  AAC.5: Patients cared for by the organisation undergo a regular re-assessment. (a–e, 5) * on e; Core a
  AAC.6: Laboratory services are provided as per the scope of services of the organisation. (a–j, 10) * on e,f,g,i,j
  AAC.7: There is an established laboratory quality assurance and safety programme. (a–g, 7) * on a,b,e
  AAC.8: Imaging services are provided as per the scope of services of the organisation. (a–i, 9) Core a; * on f,g,h
  AAC.9: There is an established quality assurance and safety programme for imaging services. (a–k, 11) * on a,e,f,i
  AAC.10: Patient care is continuous and multi-disciplinary. (a–h, 8) Core d; * on f
  AAC.11: The preventive and promotive health services are provided in a safe, collaborative and consistent manner. (a–e, 5) * on a
  AAC.12: The organisation has an established discharge process. (a–g, 7) * on b,c
  AAC.13: The organisation defines the content of the discharge summary. (a–e, 5)

FILE_LAYOUT:
  builders: policies/build/build_hco_aac{N}_v2.py
  drafts: policies/drafts/hco_aac{N}_v2_draft.json
  masters: policies/build/masters/HCO.AAC.{N}_v2_master.docx
  previews: policies/build/preview/HCO.AAC.{N}_v2_preview.docx|.md
  doc_no: «HCO/AAC/POL/{NN}»
  programme: HCO Full Accreditation, 6th Edition
  shape: same PRE/SHCO v2 14-section skeleton via pre_v2_common.emit_pre_v2
  OCR_SOURCE: policies/source/hco6_aac_ocr.txt
  PDF: policies/source/NABH-HCO-6th-Edition-Standards-Guidebook.pdf
