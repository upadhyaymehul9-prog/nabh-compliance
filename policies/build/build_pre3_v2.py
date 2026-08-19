# -*- coding: utf-8 -*-
"""PRE.3 v2 — informed consent.

Shape follows PRE.1 v2. Wording from PRE.3 OEs (NABH SHCO 3rd Edition PDF,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 88 / PDF index 94.

Does NOT overwrite pre3_draft.json or build_pre3.py. No SQL.
Stop-work section 6 for elective/planned procedures without consent (emergency exception).
Disclaimer P2 names NMC Act 2019 and MHCA 2017 only when that Act's definition applies.
PRE.3.b requirement uses "its risks" (correct grammar).
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "PRE.3"
CHAPTER = "PRE"
OE_CODES = ["PRE.3.a", "PRE.3.b", "PRE.3.c", "PRE.3.d"]
POLICY_TITLE = "Informed Consent"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "PRE v2 template: plain English, PRE roles, stop-work for elective without consent, NMC/MHCA P2.",
    },
]

STATEMENT_OF_INTENT = (
    "Informed consent is obtained from the patient or family about their care — "
    "not a signature on a blank form, and not a clerk collecting consent for a surgeon who is not in the building."
)

PURPOSE = f"""This policy says how {HOSPITAL} obtains informed consent from the patient or family for situations where informed consent is required, in a process that adheres to statutory norms; what information that consent includes; who can give consent when the patient is incapable of independent decision-making; and that consent is taken by the person performing the procedure.

The chapter intent is that informed consent is obtained for specified procedures and care, and that key components include risks, benefits and alternatives.

This document is the general consent method. That a transfusion, sedation, anaesthesia or surgical consent actually happened before the act remains COP.5, COP.9, COP.10 and COP.11.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to every situation at {HOSPITAL} in which informed consent is required: transfusion of blood and blood components, anaesthesia, surgery, initiation of any research protocol this hospital runs, and any other invasive or high-risk procedure or treatment the hospital has named.

It binds the person who performs the procedure, doctors and nurses who explain consent, registration staff who schedule elective work, and the {D('Patient Rights Officer')} who holds the list and process.

Boundaries:

- PRE.2.g lists the right that consent is obtained before those acts. This policy owns the method.
- COP.5, COP.9, COP.10 and COP.11 own that the relevant consent happened before those acts.
- PRE.4 owns ongoing education in a language they can understand. PRE.3.b is the consent conversation.
- PRE.1 and PRE.2.e: refusal is a right; this policy records consent not given.
- MOM.9 implant usage counselling is not surgical consent.
- Capacity under the Mental Healthcare Act, 2017 is PRE.3.c when that Act's definition of a person with mental illness is met — not a blanket for every unconscious patient."""

POLICY_STATEMENT = f"""{HOSPITAL} obtains informed consent from the patient or family for situations where informed consent is required. The process adheres to statutory norms.

{HOSPITAL} includes in that consent the procedure, its risks, benefits, alternatives, and who will perform it, in a language the patient or family can understand.

{HOSPITAL} describes who can give consent when a patient is incapable of independent decision-making, and implements that description.

{HOSPITAL} requires that informed consent is taken by the person performing the procedure.

{HOSPITAL} records a documented emergency that made prior consent impossible; emergency is not a standing exemption for convenience on elective or planned work."""

NON_NEGOTIABLES = f"""The following are prohibited.

1. Starting an elective or planned transfusion, anaesthesia, surgery, research protocol or other invasive or high-risk procedure without valid informed consent (see section 6 stop-work).
2. A signature on a form that does not state the procedure, risks, benefits, alternatives and who will perform it.
3. A clerk, nurse, or doctor who will not perform the procedure taking consent "for" the performer on an elective case.
4. Using one next-of-kin stamp for every incapacity — child, unconscious adult, and MHCA mental illness are not the same rule.
5. Applying a Mental Healthcare Act nominated-representative process to a patient that Act does not cover.
6. Treating emergency as a standing exemption to skip consent on work that was scheduled.

Staff report defects the same shift to the {D('Patient Rights Officer')} or {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Informed consent where required, adhering to statutory norms

The organisation obtains informed consent from the patient or family for situations where informed consent is required. The informed consent process adheres to statutory norms.

Situations where informed consent is required at {HOSPITAL} include at least: transfusion of blood and blood components; anaesthesia; surgery; initiation of any research protocol this hospital actually runs; and any other invasive or high-risk procedure or treatment this hospital has named in {D('the consent situations list held by the Patient Rights Officer')}. A class the service directory does not provide is a recorded absence, not a copied consent SOP.

The consent process — when it is obtained, how it is recorded, how refusal is recorded, and how a documented emergency that made prior consent impossible is recorded — is held by the {D('Patient Rights Officer')}. Emergency means delay would endanger life or limb; it is not a label for convenience on elective work.

The National Medical Commission Act, 2019 governs that a registered medical practitioner obtains consent consistent with professional practice. Kumar et al. (2015) and Nandimath (2009) are frameworks, not pasted protocols. Samira Kohli v. Dr. Prabha Manchanda is not a numbered PRE chapter reference and is not imported here.""",

f"""5.2 Information included in informed consent

Informed consent includes information regarding the procedure, its risks, benefits, alternatives, and as to who will perform the procedure, in a language that they can understand.

The consent form and conversation cover those elements in {D('Hindi and English')} or the language the patient or family can understand. A form that lists only "surgery" without the procedure, or that is silent on who will perform it, is incomplete. PRE.4 owns ongoing education in that language; this step is the consent conversation.""",

f"""5.3 Who can give consent when the patient is incapable

The organisation describes who can give consent when a patient is incapable of independent decision making and implements the same.

The description distinguishes a child, an unconscious or otherwise non-communicating adult, a documented emergency, and a person with mental illness as defined in the Mental Healthcare Act, 2017 where that Act applies. For MHCA mental illness, nominated representative and advance directive under that Act are used without reprinting those sections. For other incapacity, this hospital's written description applies — held by the {D('Patient Rights Officer')}. A single next-of-kin stamp for all three is not enough.""",

f"""5.4 Consent taken by the person performing the procedure

Informed consent is taken by the person performing the procedure.

For surgery, the doctor who will perform the procedure, or a doctor of the same surgical team who will be present and responsible, takes consent — as COP.11 already requires. For other classes in the step-1 list, the named performer is {D('the doctor who will perform the act')}. A clerk or nurse taking consent "for" the performer on an elective case does not meet the standard.""",
]

STOP_WORK = f"""Do not start an elective or planned transfusion, anaesthesia, surgery, research protocol or other invasive or high-risk procedure listed in section 5.1 without valid informed consent from the patient or a person authorised under section 5.3.

Emergency exception: when delay would endanger life or limb, treatment may proceed under the documented emergency method in section 5.1. Record the reason, who decided, and obtain or renew consent as soon as the patient or family can give it. Emergency is not a standing exemption for work that was scheduled.

Stop-work applies to the act, not to stabilisation before the consent conversation can happen in a true emergency.

The person performing tells the {D('Medical Superintendent')} or {D('Patient Rights Officer')} the same shift. Refusing to proceed without consent on an elective case is not a disciplinary matter."""

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that informed consent is obtained where required, by the person performing, under a process that adheres to statutory norms.

Patient Rights Officer
- Authors and keeps current the list of situations, the process, the information method and the incapacity description.

Person performing the procedure
- Takes the consent. Staff who explain or witness do not replace that person on elective work.

Doctors and nurses
- Record refusal as refusal, not as a missing signature to be fetched later.

Quality Coordinator
- Audits consent records {D('quarterly')}."""

MONITORING_AUDIT = f"""The Quality Coordinator audits a sample of consent records {D('quarterly')} for:

- Consent present for situations in the list.
- Information covering procedure, risks, benefits, alternatives and who will perform, in a language they can understand.
- Signer matching the incapacity description, or a documented emergency.
- Consent taken by the person performing.
- No blank signed form on elective work.

Root-cause analysis when an elective procedure in the list was done without consent.

This policy is reviewed {D('annually')}, and sooner when COP.5, COP.9, COP.10, COP.11 or PRE.2 are revised."""

TRAINING_ACKNOWLEDGEMENT = f"""Doctors and nurses who take or witness consent are trained at induction, before first unsupervised consent, and {D('once a year')} after that.

Staff acknowledgement

I have read this Informed Consent policy of {HOSPITAL}. I will not start elective or planned high-risk work without valid consent. I will not take consent for a procedure I will not perform.


Name: ___________________________    Designation: ___________________________

Department: ____________________    Date: ____________

Signature: ___________________________


(The Patient Rights Officer holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("PRE/POL/03"),
    version=VERSION,
    prepared_by=D("Patient Rights Officer"),
    extra_lines=f"Consent situations list location: {D('Patient Rights Officer office and each procedure area')}",
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — standard PRE.3.
- Kumar A et al. (2015) — chapter 10; framework; not pasted as protocol.
- Nandimath O (2009) — chapter 13; framework for statutory norms.
- National Medical Commission Act, 2019 — registered medical practitioners obtain informed consent consistent with professional practice.
- Mental Healthcare Act, 2017 — when a person with mental illness as defined in that Act is incapable of independent decision-making.
- Internal documents of {HOSPITAL}: consent situations list; consent process; incapacity description; transfusion, sedation, anaesthesia and procedures policies."""

DISTRIBUTION = f"""Official master copy: Medical Superintendent, with Patient Rights Officer and Quality Coordinator.

Copies issued to: every location that performs a procedure on the consent list; operation theatre; anaesthesia; emergency; transfusion; nursing administration.

Current version at {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}."""

ABBREVIATIONS = """MHCA — Mental Healthcare Act, 2017
NMC — National Medical Commission
NABH — National Accreditation Board for Hospitals and Healthcare Providers
PRE — Patient Rights and Education
SHCO — Standards for Small Healthcare Organisations"""

STATUTE_CLAUSE = (
    "the National Medical Commission Act, 2019, insofar as registered medical practitioners "
    "obtain informed consent consistent with professional practice, and the Mental Healthcare "
    "Act, 2017, insofar as a person with mental illness as defined in that Act is incapable of "
    "independent decision-making"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "PRE.3.a",
        "requirement": "The organisation obtains informed consent from the patient or family for situations where informed consent is required. Informed consent process adhered to statutory norms.",
        "steps": "Statement of intent; Section 3; 5.1 Informed consent where required; Section 6 stop-work; Section 4 items 1, 6",
        "responsible": "Patient Rights Officer (list and process); person performing (takes consent); Medical Superintendent (accountable)",
        "records": [
            "Written list of situations where informed consent is required, with recorded absences for classes not provided.",
            "Written process showing statutory norms, refusal recording and documented emergency method.",
            "Sample consents against the unique identification number for listed situations.",
            "Quarterly audit sample showing no elective procedure without consent.",
        ],
    },
    {
        "oe_code": "PRE.3.b",
        "requirement": "Informed consent includes information regarding the procedure; its risks, benefits, alternatives and as to who will perform the procedure in a language that they can understand.",
        "steps": "Section 3; 5.2 Information included; Section 4 item 2",
        "responsible": "Person taking consent (gives information); Patient Rights Officer (method)",
        "records": [
            "Written information method covering procedure, risks, benefits, alternatives and who will perform.",
            "Sample consents showing those elements — not a form that says only 'surgery'.",
            "Recorded split that PRE.4 owns ongoing education in that language.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.3.c",
        "requirement": "The organisation describes who can give consent when a patient is incapable of independent decision making and implements the same.",
        "steps": "Section 3; 5.3 Who can give consent when incapable; Section 4 items 3, 5",
        "responsible": "Patient Rights Officer (incapacity description); person taking consent (applies it)",
        "records": [
            "Written description distinguishing child, unconscious adult, documented emergency, and MHCA mental illness.",
            "Sample consents where signer matches description, or documented emergency with reason.",
            "Record that MHCA nominated representative is used only when that Act applies.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.3.d",
        "requirement": "Informed consent is taken by the person performing the procedure.",
        "steps": "Section 3; 5.4 Consent taken by performer; Section 6 stop-work",
        "responsible": "Person performing the procedure; COP.11 (surgical timing and person)",
        "records": [
            "Named person-performing for each class of procedure in use.",
            "Sample consents showing performer (or COP.11 same-team doctor) took consent — not a clerk.",
            "Stop-work records when elective work was refused for lack of consent.",
            "Quarterly audit sample.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """PRE.3 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. PRE.3.a and PRE.3.c asterisked. PRE.3.b uses "its risks". Stop-work section 6. P2: NMC Act 2019 and MHCA 2017 only. No CPA/CEA in P2."""


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
        "stop_work": STOP_WORK,
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
        "template_test": "pre_v2_adoptable_shape",
        "subtitle": "Informed consent before procedures and high-risk care.",
        "doc_no": D("PRE/POL/03"),
    }
    emit_pre_v2(
        draft,
        "pre3_v2_draft.json",
        "PRE.3_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
