# -*- coding: utf-8 -*-
"""COP.11 v2 — clinical procedures and operation theatre safety.

Shape follows PRE v2 adoptable-policy template. Wording from NABH SHCO 3rd Edition
PDF (md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 73.
Has stop-work section. Ten OEs in ten What-we-do subsections.
Disclaimer P2 names the Transplantation of Human Organs and Tissues Act, 1994.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.11"
CHAPTER = "COP"
OE_CODES = [
    "COP.11.a", "COP.11.b", "COP.11.c", "COP.11.d", "COP.11.e",
    "COP.11.f", "COP.11.g", "COP.11.h", "COP.11.i", "COP.11.j",
]
POLICY_TITLE = "Clinical Procedures and Operation Theatre Safety"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: adoptable shape, plain English, stop-work authority, organ transplant scoped.",
    },
]

STATUTE_CLAUSE = (
    "the Transplantation of Human Organs and Tissues Act, 1994, insofar as the "
    "organisation operates an organ transplant programme under that Act"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

STATEMENT_OF_INTENT = (
    "Clinical procedures and procedures in the operation theatre are performed in a safe "
    "and consistent manner — with preoperative assessment, consent, wrong-site/wrong-patient "
    "prevention, standard precautions, accurate documentation, appropriate facilities, "
    "a quality assurance programme, ethical organ transplant where applicable, and "
    "organ-donation awareness."
)

PURPOSE = f"""This policy defines how {HOSPITAL} performs clinical procedures and operation-theatre procedures safely and consistently, covering preoperative assessment and instructions, informed consent, wrong-site/wrong-patient/wrong-surgery prevention, standard precautions, procedure and post-operative documentation, equipment and facilities, quality assurance, organ transplant (where applicable), and organ-donation awareness.

Boundaries: PRE.3 owns the consent method; this policy owns that consent was obtained before the procedure. PSQ owns the quality programme; this policy owns the surgical safety checklist and OT quality assurance. COP.11.i and COP.11.j apply only if {HOSPITAL} operates an organ transplant programme.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff involved in clinical procedures and OT procedures at {HOSPITAL}: surgeons, treating doctors performing procedures, OT nurses, anaesthetists (for surgical safety checklist participation), and support staff.

It covers the procedure lifecycle from preoperative assessment through post-operative documentation, OT facilities, quality assurance, and organ transplant/donation where applicable. It does not cover the consent method (PRE.3), the overall patient safety programme (PSQ), or anaesthesia services (COP.10).

COP.11.i and COP.11.j (organ transplant and organ-donation awareness) are scoped only where {HOSPITAL} operates an organ transplant programme. If not, those elements are recorded absences against the service directory."""

POLICY_STATEMENT = f"""{HOSPITAL} performs clinical procedures and OT procedures in a consistent and safe manner. Every surgical patient has a preoperative assessment, documented pre-operative diagnosis, and pre-operative instructions. Consent is obtained before every procedure. The surgical safety checklist prevents wrong site, wrong patient and wrong surgery. Standard precautions are adhered to. Procedure notes, post-procedure monitoring and post-operative care plans are documented accurately. Appropriate facilities, equipment, instruments and supplies are available. A quality assurance programme operates. Organ transplant, where provided, is lawful and ethical. Organ-donation awareness is promoted where applicable.

{HOSPITAL} does not proceed with surgery or a procedure without the surgical safety checklist completed (site marking, patient ID, consent confirmed); surgery is stopped if wrong site or wrong patient is identified."""

NON_NEGOTIABLES = f"""1. No procedure proceeds without a documented preoperative assessment and pre-operative diagnosis.
2. No procedure proceeds without documented informed consent obtained by the doctor.
3. The surgical safety checklist (sign-in, time-out, sign-out) is completed for every OT procedure; site marking and patient identification are verified before incision.
4. Surgery is stopped immediately if wrong site, wrong patient, or wrong surgery is identified at any point.
5. Standard precautions are not optional; a procedure performed without them is a reportable defect.
6. Procedure/operation notes are completed before the surgeon leaves the OT complex.
7. The organ transplant programme, where it exists, does not proceed without lawful authorisation under the Transplantation of Human Organs and Tissues Act, 1994.
8. Staff who see a violation of items 1–4 invoke stop-work authority immediately."""

PROCEDURE_STEPS = [
f"""5.1 Consistent and safe clinical procedures

Clinical procedures and OT procedures at {HOSPITAL} are performed following documented protocols that ensure consistency. The {D('Surgeon In-Charge / OT In-Charge')} holds the operational method.

Procedures are performed only in locations with appropriate infrastructure and by credentialled practitioners.""",

f"""5.2 Preoperative assessment and instructions

Surgical patients have a preoperative assessment documented before surgery. The assessment includes a documented pre-operative diagnosis and pre-operative instructions (fasting, skin preparation, medication adjustment, consent status).

Pre-operative instructions are provided to the patient and/or family and documented in the record. The assessment is completed by the {D('treating surgeon or designated doctor')}.""",

f"""5.3 Informed consent before the procedure

Informed consent is obtained by the doctor prior to the procedure. The consent documents the procedure planned, risks, benefits, alternatives, expected outcomes, and who will perform.

PRE.3 owns the consent method. This step owns that consent was obtained and documented in the patient record before the procedure begins.""",

f"""5.4 Prevention of wrong site, wrong patient, wrong surgery

Care is taken to prevent adverse events including wrong site, wrong patient and wrong surgery. The surgical safety checklist (WHO-adapted) is used for every OT procedure with three phases:

- Sign-in: patient identity confirmed, site marked, consent verified, known allergy confirmed.
- Time-out: entire team pauses; procedure, patient, site, laterality confirmed verbally.
- Sign-out: instrument/sponge count correct, specimen labelled, post-operative plan confirmed.

Site marking is performed by the operating surgeon with the patient awake where possible. Any discrepancy halts the procedure (stop-work).""",

f"""5.5 Standard precautions during procedures

Every procedure is performed adhering to standard precautions: hand hygiene, appropriate PPE, aseptic technique, sharps safety, and waste segregation per Bio-Medical Waste Management Rules, 2016.

Breaches are reported as defects to the {D('Infection Control Nurse')} within the same shift.""",

f"""5.6 Procedure notes, post-procedure monitoring and post-operative care plan

Procedure/operation notes are documented accurately in the patient record before the surgeon leaves the OT complex. Notes include findings, procedure performed, complications if any, specimens sent, and post-operative orders.

Post-procedure monitoring is documented. A post-operative care plan is written and communicated to the receiving ward/recovery team.""",

f"""5.7 Facilities, equipment, instruments and supplies

Appropriate facilities, equipment, instruments and supplies are available in the operating theatre. The {D('OT In-Charge')} maintains the OT inventory, equipment maintenance schedule, and instrument sterilisation records.

Equipment functionality is verified before the first case of the day. Instrument sets are verified complete before and after each procedure (count reconciliation).""",

f"""5.8 Quality assurance programme

{HOSPITAL} implements a quality assurance programme for clinical procedures and OT services. PSQ owns the overall patient safety programme; this step owns the OT-specific quality assurance activities.

QA activities include: {D('surgical safety checklist compliance audit, surgical-site infection surveillance, unplanned return-to-OT tracking, near-miss reporting, morbidity and mortality review, and equipment failure reporting')}. Results are reported {D('quarterly')} to the quality committee.""",

f"""5.9 Organ transplant programme (where applicable)

The organ transplant programme, where {HOSPITAL} operates one, is in consonance with the legal requirements of the Transplantation of Human Organs and Tissues Act, 1994 and is conducted ethically.

If {HOSPITAL} does not operate an organ transplant programme, this section is a recorded absence against the service directory. Where the programme exists: {D('the transplant coordinator holds the protocol, authorisation committee is constituted as per the Act, donor consent and brain-death certification follow statutory requirements, and records are maintained as required by the appropriate authority')}.""",

f"""5.10 Organ donation awareness (where applicable)

{HOSPITAL} takes measures to create awareness regarding organ donation where it operates an organ transplant programme. If no programme exists, this section is a recorded absence.

Where applicable, awareness measures include {D('display material in public areas, staff training on discussing donation sensitively, and coordination with the regional organ and tissue transplant organisation (ROTTO/SOTTO)')}.""",
]

STOP_WORK = f"""Any staff member shall invoke stop-work authority and halt procedure preparation or the procedure itself when:

- The surgical safety checklist has not been completed (site marking, patient ID, consent not confirmed).
- Wrong site, wrong patient, or wrong surgery is identified at any point before or during the procedure.
- Informed consent is not documented.
- Preoperative assessment is not documented.

Stop-work is reported to the {D('Surgeon In-Charge / OT In-Charge')} immediately. The procedure does not proceed or is halted until all conditions are resolved. No punitive action is taken against a person who invokes stop-work in good faith."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that procedures are performed safely and consistently; that the QA programme operates.

Surgeon In-Charge / OT In-Charge
- Holds OT protocols; maintains surgical safety checklist compliance; manages facilities and equipment.

Surgeons and treating doctors performing procedures
- Perform preoperative assessment, obtain consent (that it was obtained), mark site, complete checklist, document procedure notes.

OT nurses
- Participate in checklist; maintain instrument counts; verify equipment; report breaches.

Anaesthetists
- Participate in surgical safety checklist (sign-in, time-out).

Transplant coordinator (where programme exists)
- Holds transplant protocol; ensures legal compliance under THOTA 1994.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when a surgical safety defect recurs."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers:

- Preoperative assessment and diagnosis documented (sample charts).
- Consent documented before procedures.
- Surgical safety checklist completed for every OT case (compliance rate).
- Site marking verified before incision.
- Procedure notes completed before surgeon left OT.
- Post-operative care plan documented and communicated.
- Equipment and instrument checks documented.
- QA programme reports produced quarterly.
- Organ transplant legal compliance (where applicable).
- Stop-work events reviewed; no punitive action taken.

Root-cause analysis is required when a surgical safety defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when surgical guidelines, the service directory, or THOTA regulations change."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff involved in clinical procedures and OT are trained on this policy at induction and {D('once a year')} after that. Training covers preoperative assessment, consent requirements, the surgical safety checklist, standard precautions, documentation requirements, stop-work authority, and organ transplant ethics (where applicable).

Staff acknowledgement

I have read this Clinical Procedures and Operation Theatre Safety policy of {HOSPITAL}. I will perform and participate in procedures only in accordance with this policy and will invoke stop-work authority when safety conditions are not met.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The OT In-Charge holds signed acknowledgements with the credentialling file.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/11"),
    version=VERSION,
    prepared_by=D("Surgeon In-Charge / OT In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.11.
- World Health Organization (WHO), Surgical Safety Checklist — 2009 edition or later adaptation.
- Transplantation of Human Organs and Tissues Act, 1994 (as amended 2011) — applicable where {HOSPITAL} operates an organ transplant programme.
- Bio-Medical Waste Management Rules, 2016 — standard precautions context.
- Internal documents of {HOSPITAL}: surgical safety checklist, OT protocol, preoperative assessment form, procedure-notes template, QA reports, transplant protocol (where applicable), equipment maintenance schedule, stop-work register."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the OT In-Charge and Quality Coordinator.

Copies issued to: operation theatre; minor OT; procedure rooms; surgical wards; day-care surgery unit (where it exists); transplant coordinator office (where applicable).

The current version is available to all staff at the {D('policy file in the OT')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}."""

ABBREVIATIONS = """CAPA — corrective and preventive action
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
OT — operation theatre
PPE — personal protective equipment
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter)
QA — quality assurance
ROTTO — Regional Organ and Tissue Transplant Organisation
SHCO — Standards for Small Healthcare Organisations
SOTTO — State Organ and Tissue Transplant Organisation
THOTA — Transplantation of Human Organs and Tissues Act
WHO — World Health Organization"""

OE_MAPPING = [
    {
        "oe_code": "COP.11.a",
        "requirement": "Clinical procedures as well as procedures done in operation theatres are done in a consistent and safe manner.",
        "steps": "Section 3; 5.1 Consistent and safe clinical procedures; Section 4 items 1–8",
        "responsible": "Surgeon In-Charge / OT In-Charge (protocol); surgeons (perform)",
        "records": [
            "Documented OT and procedure protocols with annual review.",
            "Credentialling list of practitioners permitted to perform procedures.",
            "Location verification for procedure capability.",
            "Sample procedure records showing protocol adherence.",
        ],
    },
    {
        "oe_code": "COP.11.b",
        "requirement": "Surgical patients have a preoperative assessment, a documented pre-operative diagnosis, and pre-operative instructions provided before surgery and documented.",
        "steps": "Section 3; 5.2 Preoperative assessment and instructions; Section 4 item 1",
        "responsible": "Treating surgeon or designated doctor (assess and instruct)",
        "records": [
            "Preoperative assessment forms with diagnosis documented.",
            "Pre-operative instructions documented and provided to patient/family.",
            "Audit sample confirming assessment completed before surgery.",
        ],
    },
    {
        "oe_code": "COP.11.c",
        "requirement": "Informed consent is obtained by the doctor prior to the procedure.",
        "steps": "Section 3; 5.3 Informed consent; Section 4 item 2",
        "responsible": "Doctor performing procedure (obtain consent); PRE.3 (method)",
        "records": [
            "Signed consent forms in patient records before procedure.",
            "Audit sample confirming consent documented before procedure start.",
            "Recorded boundary that PRE.3 owns consent method.",
        ],
    },
    {
        "oe_code": "COP.11.d",
        "requirement": "Care is taken to prevent adverse events like wrong site, wrong patient and wrong surgery.",
        "steps": "Section 3; 5.4 Prevention of wrong site, wrong patient, wrong surgery; Section 4 items 3–4",
        "responsible": "Operating surgeon (site mark); entire OT team (checklist participation)",
        "records": [
            "Completed surgical safety checklists (sign-in, time-out, sign-out) for every OT case.",
            "Site-marking records by operating surgeon.",
            "Near-miss and adverse-event reports related to wrong site/patient/surgery.",
            "Stop-work event records where discrepancy was identified.",
        ],
    },
    {
        "oe_code": "COP.11.e",
        "requirement": "The procedure is done adhering to standard precautions.",
        "steps": "Section 3; 5.5 Standard precautions during procedures; Section 4 item 5",
        "responsible": "All procedure staff (adhere); Infection Control Nurse (breach reports)",
        "records": [
            "Standard-precautions protocol for procedures.",
            "Breach reports filed within same shift.",
            "Audit sample showing PPE, hand hygiene and aseptic technique compliance.",
        ],
    },
    {
        "oe_code": "COP.11.f",
        "requirement": "Procedures / operation notes, post procedure monitoring and post-operative care plan are documented accurately in the patient record.",
        "steps": "Section 3; 5.6 Procedure notes, post-procedure monitoring and post-operative care plan; Section 4 item 6",
        "responsible": "Operating surgeon (notes); ward/recovery team (post-op monitoring and care plan)",
        "records": [
            "Procedure/operation notes completed before surgeon left OT.",
            "Post-procedure monitoring records.",
            "Post-operative care plan documented and communicated to receiving team.",
        ],
    },
    {
        "oe_code": "COP.11.g",
        "requirement": "Appropriate facilities, equipment, instruments and supplies are available in the operating theatre.",
        "steps": "Section 3; 5.7 Facilities, equipment, instruments and supplies",
        "responsible": "OT In-Charge (inventory, maintenance, sterilisation); biomedical engineer (equipment)",
        "records": [
            "OT inventory list with maintenance schedule.",
            "Equipment functionality verification records (daily first-case check).",
            "Instrument sterilisation records and count reconciliation logs.",
        ],
    },
    {
        "oe_code": "COP.11.h",
        "requirement": "The organization shall implement a quality assurance programme.",
        "steps": "Section 3; 5.8 Quality assurance programme",
        "responsible": "Quality Coordinator (reports); Surgeon In-Charge (OT QA activities)",
        "records": [
            "Quarterly QA reports with checklist compliance, SSI rates, return-to-OT data.",
            "Near-miss and adverse-event register for procedures.",
            "Morbidity and mortality review minutes.",
            "CAPA records where defects recurred.",
        ],
    },
    {
        "oe_code": "COP.11.i",
        "requirement": "The organ transplant program shall be in consonance with the legal requirements and shall be conducted ethically.",
        "steps": "Section 3; 5.9 Organ transplant programme; Section 4 item 7",
        "responsible": "Transplant coordinator (protocol and legal compliance); authorisation committee",
        "records": [
            "Transplant protocol aligned with THOTA 1994.",
            "Authorisation committee constitution and meeting minutes.",
            "Donor consent and brain-death certification records per statute.",
            "Recorded absence against service directory if no programme exists.",
        ],
    },
    {
        "oe_code": "COP.11.j",
        "requirement": "The organization shall take measures to create awareness regarding organ donation.",
        "steps": "Section 3; 5.10 Organ donation awareness",
        "responsible": "Transplant coordinator or designated person (awareness); Medical Superintendent (accountable)",
        "records": [
            "Display material and awareness activities documented.",
            "Staff training records on discussing organ donation.",
            "Coordination records with ROTTO/SOTTO where applicable.",
            "Recorded absence against service directory if no programme exists.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.11 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Clinical procedures, as well as procedures in the operation theatre are performed in a safe and consistent manner." COP.11.a–j PDF index 73. Asterisked OEs: a, d, h. Levels: h/i/j Core, d Achievement, rest Commitment.

SHAPE: Ten What-we-do subsections (5.1–5.10). Stop-work: YES. Disclaimer names THOTA 1994. COP surgical/OT roles."""


def main() -> int:
    draft = {
        "standard_code": STANDARD_CODE,
        "chapter": CHAPTER,
        "oe_codes": OE_CODES,
        "policy_title": POLICY_TITLE,
        "purpose": PURPOSE,
        "scope": SCOPE,
        "policy_statement": POLICY_STATEMENT,
        "procedure_steps": PROCEDURE_STEPS,
        "responsibility": RESPONSIBILITY,
        "references_text": REFERENCES,
        "distribution": DISTRIBUTION,
        "abbreviations": ABBREVIATIONS,
        "disclaimer": DISCLAIMER,
        "oe_mapping": OE_MAPPING,
        "universal_facts_checklist": UNIVERSAL_FACTS_CHECKLIST,
        "version": VERSION,
        "revision_history": REVISION_HISTORY,
        "status": "draft",
        "definitions": STATEMENT_OF_INTENT,
        "exceptions": NON_NEGOTIABLES,
        "monitoring_audit": MONITORING_AUDIT,
        "training_competency": TRAINING_ACKNOWLEDGEMENT,
        "resources_required": DOCUMENT_CONTROL,
        "template_test": "cop_v2_adoptable_shape",
        "subtitle": "Safe and consistent clinical procedures and OT services.",
        "doc_no": D("COP/POL/11"),
        "stop_work": STOP_WORK,
    }
    emit_pre_v2(
        draft,
        "cop11_v2_draft.json",
        "COP.11_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
