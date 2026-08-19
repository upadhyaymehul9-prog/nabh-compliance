# -*- coding: utf-8 -*-
"""HRM.9 v2 — credentialing and privileging of para-clinical professionals.

Shape follows PRE v2 adoptable-policy shape. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 133.
Chapter intent: PDF index 130.

HAS stop-work section. Four OEs mapped to four What-we-do subsections.
Disclaimer P2 names Pharmacy Act, 1948 and applicable council/board registration
for laboratory technicians, radiographers and physiotherapists.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HRM.9"
CHAPTER = "HRM"
OE_CODES = ["HRM.9.a", "HRM.9.b", "HRM.9.c", "HRM.9.d"]
POLICY_TITLE = (
    "Credentialing and Privileging of Para-Clinical Professionals Permitted to Provide "
    "Patient Care Without Supervision"
)
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HRM v2 template: adoptable shape, plain English, workforce roles, four steps, stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Para-clinical professionals — laboratory technicians, radiographers, "
    "physiotherapists, pharmacists and others — permitted to provide patient care "
    "without supervision are identified, credentialed, privileged and known to the "
    "departments they serve."
)

PURPOSE = f"""This policy describes how {HOSPITAL} credentials and privileges para-clinical professionals who are permitted by law, regulation and the organisation to provide patient care without supervision.

It covers laboratory technicians, radiographers, physiotherapists, pharmacists and other allied health professionals whose statutory registration or council enrolment is required for independent practice. The four elements are: identifying those professionals; verifying and documenting their education, registration, training and experience with periodic updates; granting privileges consonant with qualification, training, experience and registration; and ensuring requisite services are known to the professionals and to departments/units.

Boundaries: HRM.6 owns the staff personal file. This policy owns the para-clinical credentialing and privileging process and register. HRM.7 owns medical credentialing; HRM.8 owns nursing credentialing. AAC.4.b and AAC.5.c use credentialing outcomes when assigning qualified laboratory and imaging personnel; they do not restate this method.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every para-clinical professional at {HOSPITAL} who provides patient care or patient-facing services without supervision — laboratory technicians, radiographers, physiotherapists, pharmacists, dieticians, respiratory therapists and other allied health staff whose role requires independent practice authority.

It covers the four elements HRM.9.a–d. It does not cover medical credentialing (HRM.7), nursing credentialing (HRM.8), personal files (HRM.6), or department-specific technical SOPs (AAC.4, AAC.5, AAC.6, MOM).

Boundaries with other policies of {HOSPITAL}:

- HRM.6 owns the personal file. This policy owns the para-clinical credentialing file, privileging register and privilege letter.
- HRM.7 owns medical credentialing; HRM.8 owns nursing credentialing. This policy is specific to para-clinical professionals.
- MOM.4 owns authorised medication prescribers (doctors). MOM.8 owns safe handling of narcotics and cytotoxics. This policy credentials the pharmacist; those policies govern what the pharmacist may dispense or handle.
- AAC.4.b and AAC.5.c require qualified laboratory and imaging personnel; this policy verifies the qualification."""

POLICY_STATEMENT = f"""{HOSPITAL} identifies para-clinical professionals permitted by law, regulation and the organisation to provide patient care without supervision. Their education, registration, training and experience are verified, documented and updated periodically. Privileges are granted in consonance with their qualification, training, experience and registration. The requisite services they provide are known to them and to the departments/units of the organisation.

A para-clinical professional without completed credentialing and privileging does not provide unsupervised patient care or patient-facing services at {HOSPITAL}."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Permitting a para-clinical professional to provide unsupervised patient care who is not listed in the para-clinical privileging register.
2. Granting privileges beyond the professional's verified qualification, training, experience or current statutory registration — including Pharmacy Council registration for pharmacists, State Medical Faculty or equivalent board registration for laboratory technicians, AERB authorisation for radiographers, and State Council of Physiotherapy registration for physiotherapists.
3. Continuing unsupervised practice when registration or council enrolment has lapsed without suspension from the privileging register.
4. Allowing a laboratory technician to perform tests, a radiographer to operate equipment, a physiotherapist to treat patients, or a pharmacist to dispense medications beyond the scope listed in the privilege letter.
5. Assigning a para-clinical professional to a department whose scope is not reflected in the privilege letter.

Staff who cannot confirm completed credentialing and privileging do not permit unsupervised para-clinical practice. They report to the {D('department head')} or {D('HR Manager')} immediately."""

PROCEDURE_STEPS = [
f"""5.1 Identify para-clinical professionals permitted for unsupervised patient care

Para-clinical professionals permitted by law, regulation and the organisation to provide patient care without supervision are identified.

{HOSPITAL} maintains a Credentialing and Privileging SOP for para-clinical professionals. The SOP defines which categories may practise independently at this hospital — {D('registered pharmacists, DMLT or B.Sc. MLT laboratory technicians, diploma or degree radiographers with AERB authorisation where required, registered physiotherapists, and other allied health staff with defined scope')}.

The {D('HR Manager')}, in consultation with relevant department heads, maintains the para-clinical privileging register listing every independently practising para-clinical professional with:

- name and employee ID;
- profession category (pharmacist, laboratory technician, radiographer, physiotherapist, other);
- statutory registration number and issuing body (State Pharmacy Council, State Medical Faculty or board, AERB, State Council of Physiotherapy, or equivalent);
- qualification;
- date of initial credentialing and date of last re-credentialing;
- specific privileges granted and any restrictions.

The register is available to department heads. A current extract is displayed in {D('each para-clinical department (laboratory, radiology, pharmacy, physiotherapy)')}.""",

f"""5.2 Verify education, registration, training and experience — document and update

The education, registration, training and experience of para-clinical professionals are appropriately verified, documented and updated periodically.

At credentialing (initial appointment or privilege renewal), the {D('HR Manager')} collects and verifies credentials according to profession:

- **Pharmacists** — pharmacy degree or diploma; registration with the State Pharmacy Council under the Pharmacy Act, 1948.
- **Laboratory technicians** — DMLT, B.Sc. MLT or equivalent; registration or enrolment with the applicable State Medical Faculty, Paramedical Board or council recognised in the state.
- **Radiographers** — diploma or degree in radiography; AERB authorisation where the person operates radiation-generating equipment; registration with the applicable state board where required.
- **Physiotherapists** — BPT or MPT; registration with the State Council of Physiotherapy or Indian Association of Physiotherapists state chapter as applicable.
- **Other allied health** — qualification and registration as required by the applicable council or board for that profession in the state.

Verification is documented in the credentialing file with date, source contacted and verifying officer. Registration renewal dates are tracked; re-verification begins {D('sixty days')} before expiry.

Re-credentialing is conducted {D('every two years')} or sooner when scope of practice changes, registration is renewed, or a significant event requires review.""",

f"""5.3 Grant privileges consonant with qualification, training, experience and registration

Para-clinical professionals are granted privileges in consonance with their qualification, training, experience and registration.

The {D('Credentialing Committee')} — chaired by the {D('Medical Superintendent')} with the {D('HR Manager')} and the relevant department head (Laboratory In-Charge, Radiology In-Charge, Pharmacy In-Charge, Physiotherapy In-Charge) — reviews each application and grants privileges by written privilege letter. The letter specifies:

- tests, procedures, equipment or services the professional may perform independently;
- patient categories where applicable;
- any restrictions or supervision requirements;
- validity period (maximum {D('two years')}).

Examples of profession-specific privileges:

- Pharmacist: dispensing categories, IV admixture, cytotoxic preparation (if additionally trained per MOM.8).
- Laboratory technician: test panels and analyser categories the technician may run and report.
- Radiographer: modalities and AERB-authorised equipment the radiographer may operate.
- Physiotherapist: treatment modalities and patient categories the therapist may treat independently.

Privileges not supported by verified credentials are not granted. A professional whose registration lapses is suspended from the register pending renewal verification.""",

f"""5.4 Requisite services known to para-clinical professionals and departments/units

The requisite services to be provided by the para-clinical professionals are known to them as well as the various departments/units of the organisation.

Each privilege letter is cross-referenced to the service directory (AAC.1) and the department scope statement. The department head confirms that the professional's privileges match the services the department claims to provide.

At each department induction or when a new para-clinical professional joins, the department head briefs the person on:

- services, tests, procedures or treatments the department provides and those referred elsewhere;
- quality standards, turnaround times and reporting requirements;
- safety requirements (radiation safety, biosafety, cytotoxic handling as applicable);
- escalation pathways to the treating doctor or consultant.

The briefing is recorded and filed in the credentialing file. Department heads maintain a current list of credentialed para-clinical staff for their unit, matched to the central privileging register {D('quarterly')}.""",
]

STOP_WORK = f"""Any staff member who cannot confirm that a para-clinical professional has completed credentialing and privileging:

1. Does not permit that professional to provide unsupervised patient care or patient-facing services — including independent test reporting, radiation exposure, physiotherapy treatment or medication dispensing beyond verified privileges.
2. Ensures the service continues under another credentialed professional or under supervised care as clinically appropriate.
3. Reports to the {D('department head')} or {D('HR Manager')} immediately — the same shift.

For a professional whose statutory registration or council enrolment has lapsed:

1. Suspends the professional from the privileging register pending verification.
2. Does not assign unsupervised duties until registration is confirmed current.
3. Notifies the {D('Medical Superintendent')} and the relevant department head the same working day.

No approval is needed to invoke stop-work. Patient safety and statutory registration requirements override convenience."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Chairs the Credentialing Committee; accountable for the para-clinical privileging register.

HR Manager
- Collects and verifies credentials; maintains credentialing files and the privileging register.
- Tracks registration renewal dates and initiates re-credentialing.

Credentialing Committee
- Reviews applications and grants, restricts or denies para-clinical privileges by written decision.

Department heads (Laboratory, Radiology, Pharmacy, Physiotherapy and others)
- Confirm privileges match department scope; brief new staff; maintain unit staff lists.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 8).
- Tracks CAPA when credentialing gaps or lapsed registrations recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Para-clinical privileging register is current — every unsupervised professional is listed.
- Sample credentialing files checked for primary-source verification by profession.
- Registration renewal dates — no professional practising with lapsed registration.
- Privilege letters within validity period and matched to department scope.
- Unit staff lists match the central register.
- Stop-work invocations and their outcomes.

Root-cause analysis is required when an uncredentialed or unprivileged para-clinical professional is found providing unsupervised services, or when registration lapses are detected after the fact.

This policy is reviewed {D('annually')}, and sooner when statutory registration requirements for any para-clinical profession change."""

TRAINING_ACKNOWLEDGEMENT = f"""Department heads, the HR Manager and para-clinical staff are trained on this policy at induction and {D('once a year')} after that. Training covers the privileging register, profession-specific registration requirements, stop-work authority and how to verify credentials.

Staff acknowledgement

I have read this Para-Clinical Professionals Credentialing and Privileging policy of {HOSPITAL}. I understand the privileging register, stop-work authority and that unsupervised para-clinical practice requires completed credentialing.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per person. The HR Manager holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HRM/POL/09"),
    version=VERSION,
    prepared_by=D("HR Manager"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Human Resource Management chapter, standard HRM.9.
- Pharmacy Act, 1948 — registration of pharmacists with the State Pharmacy Council.
- Applicable State Medical Faculty, Paramedical Board or council registration for laboratory technicians.
- Atomic Energy (Radiation Protection) Rules, 2004 — authorisation for radiographers operating radiation-generating equipment.
- Applicable State Council of Physiotherapy registration for physiotherapists.
- Internal documents of {HOSPITAL}: para-clinical privileging register; credentialing files; privilege letters; Credentialing Committee minutes."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the HR Manager and the Quality Coordinator.

Copies issued to: laboratory; radiology; pharmacy; physiotherapy; other allied health departments; HR office.

The current version is available to all staff at the {D('HR office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AERB — Atomic Energy Regulatory Board
CAPA — corrective and preventive action
DMLT — Diploma in Medical Laboratory Technology
HRM — Human Resource Management (NABH SHCO chapter)
MLT — Medical Laboratory Technology
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations
SPC — State Pharmacy Council"""

STATUTE_CLAUSE = (
    "the respective statutory registration requirements for para-clinical professionals, "
    "including the Pharmacy Act, 1948 for pharmacists and the applicable council or board "
    "registration for laboratory technicians, radiographers and physiotherapists"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "HRM.9.a",
        "requirement": "Para-clinical professionals permitted by law, regulation and the organisation to provide patient care without supervision are identified.",
        "steps": "Statement of intent; Section 3; 5.1 Identify para-clinical professionals; Section 4 item 1",
        "responsible": "HR Manager (maintain register); department heads (confirm categories)",
        "records": [
            "Credentialing and Privileging SOP for para-clinical professionals.",
            "Para-clinical privileging register with profession, registration body and number.",
            "Department display or extract of credentialed para-clinical staff.",
            "Quarterly audit sample showing register matches practising staff.",
        ],
    },
    {
        "oe_code": "HRM.9.b",
        "requirement": "The education, registration, training and experience of para-clinical professionals are appropriately verified, documented and updated periodically.",
        "steps": "Section 3; 5.2 Verify education, registration, training and experience; Section 4 items 2, 3",
        "responsible": "HR Manager (collect and verify by profession); Credentialing Committee (review at re-credentialing)",
        "records": [
            "Credentialing file with profession-specific primary-source verification.",
            "State Pharmacy Council registration for pharmacists.",
            "State Medical Faculty or board registration for laboratory technicians.",
            "AERB authorisation and state board registration for radiographers where applicable.",
            "State Council of Physiotherapy registration for physiotherapists.",
            "Registration renewal tracking log with re-verification dates.",
        ],
    },
    {
        "oe_code": "HRM.9.c",
        "requirement": "Para-clinical professionals are granted privileges in consonance with their qualification, training, experience and registration.",
        "steps": "Section 3; 5.3 Grant privileges; Section 4 items 2, 4, 5; Section 6 (stop-work)",
        "responsible": "Credentialing Committee (grant privileges); Medical Superintendent (suspend on lapse)",
        "records": [
            "Written privilege letters specifying tests, procedures, equipment or services and validity period.",
            "Credentialing Committee minutes recording grant, restriction or denial.",
            "Suspension records for lapsed registration pending renewal.",
            "Stop-work invocation and outcome records.",
        ],
    },
    {
        "oe_code": "HRM.9.d",
        "requirement": "The requisite services to be provided by the para-clinical professionals are known to them as well as the various departments/units of the organisation.",
        "steps": "Section 3; 5.4 Requisite services known to professionals and departments",
        "responsible": "Department heads (brief staff and maintain unit lists); HR Manager (cross-reference to service directory)",
        "records": [
            "Privilege letters cross-referenced to service directory and department scope.",
            "Department induction or joining briefing records for each para-clinical professional.",
            "Unit staff list matched to central register quarterly.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HRM.9 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "There is a process for credentialing and privileging of para-clinical professionals, permitted to provide patient care without supervision." HRM.9.a–d PDF index 133. No asterisked OEs. HRM.9.a and HRM.9.c are Core; HRM.9.b and HRM.9.d are Commitment.

SHAPE: Four What-we-do subsections (5.1–5.4). Stop-work YES (no unsupervised care without credentialing/privileging). Disclaimer names Pharmacy Act 1948 and council/board registration for lab techs, radiographers and physiotherapists. Workforce roles. Distinct from HRM.7 (NMC) and HRM.8 (INC)."""


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
        "template_test": "hrm_v2_adoptable_shape",
        "subtitle": "Credentialing and privileging para-clinical professionals for unsupervised care.",
        "doc_no": D("HRM/POL/09"),
        "stop_work": STOP_WORK,
    }
    emit_pre_v2(
        draft,
        "hrm9_v2_draft.json",
        "HRM.9_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
