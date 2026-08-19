# -*- coding: utf-8 -*-
"""COP.9 v2 — procedural sedation provided consistently and safely.

Shape follows PRE v2 adoptable-policy template. Wording from NABH SHCO 3rd Edition
PDF (md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 72.
Has stop-work section. Five OEs in five What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.9"
CHAPTER = "COP"
OE_CODES = [
    "COP.9.a", "COP.9.b", "COP.9.c", "COP.9.d", "COP.9.e",
]
POLICY_TITLE = "Procedural Sedation"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: adoptable shape, plain English, stop-work authority included.",
    },
]

STATEMENT_OF_INTENT = (
    "Procedural sedation is provided consistently and safely — with informed consent, "
    "competent personnel, intra-procedure monitoring, and objective discharge criteria."
)

PURPOSE = f"""This policy defines how {HOSPITAL} administers procedural sedation consistently and safely, ensuring informed consent is obtained, competent and trained persons perform and monitor sedation, minimum intra-procedure monitoring is maintained, and patients are discharged from recovery based on objective criteria.

Boundaries: PRE.3 owns the consent method; this policy owns that consent was obtained before sedation. COP.10 owns anaesthesia; this policy owns sedation that is not general or regional anaesthesia.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff involved in procedural sedation at {HOSPITAL}: anaesthetists, treating doctors credentialed to sedate, nurses monitoring sedation, and recovery-area staff.

It covers sedation administration, consent, competency, intra-procedure monitoring, and post-procedure monitoring with discharge criteria. It does not cover general or regional anaesthesia (COP.10) or the consent method (PRE.3)."""

POLICY_STATEMENT = f"""{HOSPITAL} administers procedural sedation in a consistent manner with informed consent obtained before every sedation event, competent and trained personnel present, minimum monitoring parameters maintained throughout, and objective discharge criteria applied in recovery.

{HOSPITAL} does not sedate a patient without informed consent, a competent sedationist present, and minimum monitoring equipment ready."""

NON_NEGOTIABLES = f"""1. No sedation is administered without documented informed consent specific to the sedation.
2. No sedation is performed without a competent and trained person present who is dedicated to monitoring the patient.
3. Minimum monitoring (heart rate, cardiac rhythm, respiratory rate, blood pressure, oxygen saturation, level of sedation) is confirmed operational before sedation begins.
4. A patient is not discharged from recovery without meeting documented objective discharge criteria.
5. Emergency resuscitation equipment is present and checked before sedation commences.
6. Staff who see a violation of items 1–5 invoke stop-work authority immediately."""

PROCEDURE_STEPS = [
f"""5.1 Consistent administration of procedural sedation

Procedural sedation at {HOSPITAL} is administered according to a documented protocol that includes pre-sedation assessment, sedation-level selection, drug choice, monitoring parameters, and recovery pathway.

The {D('Anaesthesia In-Charge')} holds the protocol. Sedation levels used at this hospital are {D('minimal, moderate and deep sedation')}. The protocol is reviewed {D('annually')} for currency against current guidelines.""",

f"""5.2 Informed consent for procedural sedation

Informed consent specific to the sedation is obtained before administration. The consent includes explanation of risks, benefits, alternatives, the sedation level planned, and who will monitor.

PRE.3 owns the consent method. This step owns that consent was obtained and documented in the patient record before sedation begins. Consent is taken by the {D('sedationist or treating doctor performing the procedure')}.""",

f"""5.3 Competent and trained personnel

Procedural sedation is performed and monitored by persons who are competent and trained. The {D('Anaesthesia In-Charge')} maintains a credentialling list of staff permitted to sedate and to monitor.

Competency requirements: {D('completion of sedation training module, BLS/ACLS certification current, and supervised sedation cases as per hospital credentialling criteria')}. A dedicated monitoring person is present throughout who does not perform the procedure.""",

f"""5.4 Intra-procedure monitoring

During sedation the following are monitored continuously and documented at intervals of {D('every five minutes')}: heart rate, cardiac rhythm, respiratory rate, blood pressure, oxygen saturation, and level of sedation.

Equipment is confirmed functional before sedation begins. Any deterioration triggers the escalation pathway in the sedation protocol. Records are maintained in the sedation monitoring form.""",

f"""5.5 Post-procedure monitoring and discharge

Post-procedure monitoring is documented using {D('the Modified Aldrete Score or equivalent objective tool')}. Patients are discharged from the recovery area only when objective criteria are met and documented.

Discharge criteria include {D('stable vital signs for at least 30 minutes, return to baseline consciousness, pain controlled, no nausea/vomiting, and a responsible adult available for escort if outpatient')}. The discharging clinician signs the recovery record.""",
]

STOP_WORK = f"""Any staff member shall invoke stop-work authority and halt sedation preparation or administration when:

- Informed consent has not been obtained or documented.
- A competent sedationist or dedicated monitoring person is not present.
- Minimum monitoring equipment (pulse oximeter, ECG, NIBP, capnography where required) is not available or not functional.
- Emergency resuscitation equipment is not present or not checked.

Stop-work is reported to the {D('Anaesthesia In-Charge')} immediately. The procedure does not proceed until all conditions are met. No punitive action is taken against a person who invokes stop-work in good faith."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that procedural sedation is provided safely and consistently.

Anaesthesia In-Charge
- Holds the sedation protocol and credentialling list.
- Reviews protocol annually; maintains equipment readiness.

Anaesthetists and credentialled sedationists
- Perform sedation, obtain consent (that it was obtained), monitor intra-procedure.

Nurses (sedation and recovery areas)
- Monitor patients intra- and post-procedure; apply discharge criteria.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when a sedation safety defect recurs."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers:

- Consent documented before every sedation (sample charts).
- Credentialling list current; no uncredentialled person sedated independently.
- Intra-procedure monitoring records complete (all six parameters).
- Post-procedure discharge criteria documented and met before discharge.
- Stop-work events reviewed; no punitive action taken.
- Equipment checks documented before sedation.

Root-cause analysis is required when a sedation safety defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when sedation guidelines or credentialling criteria change."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff involved in procedural sedation are trained on this policy at induction and {D('once a year')} after that. Training covers the sedation protocol, consent requirements, monitoring parameters, stop-work authority, and discharge criteria.

Staff acknowledgement

I have read this Procedural Sedation policy of {HOSPITAL}. I will administer and monitor sedation only in accordance with this policy and will invoke stop-work authority when safety conditions are not met.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Anaesthesia In-Charge holds signed acknowledgements with the credentialling file.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/09"),
    version=VERSION,
    prepared_by=D("Anaesthesia In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.9.
- American Society of Anesthesiologists (ASA), Practice Guidelines for Sedation and Analgesia by Non-Anesthesiologists — adopted edition for sedation-level definitions and monitoring standards.
- Internal documents of {HOSPITAL}: sedation protocol, credentialling list, sedation monitoring form, Modified Aldrete Score form, equipment-check log, stop-work register."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Anaesthesia In-Charge and Quality Coordinator.

Copies issued to: procedure rooms; endoscopy suite; minor OT; recovery area; emergency department.

The current version is available to all staff at the {D('policy file in the procedure area')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}."""

ABBREVIATIONS = """ACLS — advanced cardiovascular life support
BLS — basic life support
CAPA — corrective and preventive action
ECG — electrocardiogram
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NIBP — non-invasive blood pressure
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "COP.9.a",
        "requirement": "Procedural sedation is administered in a consistent manner.",
        "steps": "Section 3; 5.1 Consistent administration of procedural sedation; Section 4 items 1–6",
        "responsible": "Anaesthesia In-Charge (protocol); sedationists (administer)",
        "records": [
            "Documented sedation protocol with pre-assessment, drug selection and monitoring pathway.",
            "Annual protocol review record.",
            "Sample sedation records showing protocol adherence.",
            "Credentialling list of permitted sedationists.",
        ],
    },
    {
        "oe_code": "COP.9.b",
        "requirement": "Informed consent for administration of procedural sedation is obtained.",
        "steps": "Section 3; 5.2 Informed consent for procedural sedation; Section 4 item 1",
        "responsible": "Sedationist or treating doctor (obtain consent); PRE.3 (method)",
        "records": [
            "Signed consent forms specific to sedation in patient records.",
            "Audit sample confirming consent documented before sedation began.",
            "Recorded boundary that PRE.3 owns consent method.",
        ],
    },
    {
        "oe_code": "COP.9.c",
        "requirement": "Competent and trained persons perform and monitor sedation.",
        "steps": "Section 3; 5.3 Competent and trained personnel; Section 4 item 2",
        "responsible": "Anaesthesia In-Charge (credentialling); HR (training records)",
        "records": [
            "Credentialling list with competency criteria and validity dates.",
            "Training records showing BLS/ACLS and sedation-module completion.",
            "Evidence that a dedicated monitoring person was present (sedation form signature).",
        ],
    },
    {
        "oe_code": "COP.9.d",
        "requirement": "Intra-procedure monitoring includes at a minimum the heart rate, cardiac rhythm, respiratory rate, blood pressure, oxygen saturation, and level of sedation.",
        "steps": "Section 3; 5.4 Intra-procedure monitoring; Section 4 item 3",
        "responsible": "Dedicated monitoring person (record); sedationist (oversight)",
        "records": [
            "Sedation monitoring forms with all six parameters at defined intervals.",
            "Pre-sedation equipment-check log.",
            "Escalation records where deterioration was identified.",
        ],
    },
    {
        "oe_code": "COP.9.e",
        "requirement": "Post procedure monitoring is documented, and patients are discharged from the recovery area based on objective criteria.",
        "steps": "Section 3; 5.5 Post-procedure monitoring and discharge; Section 4 item 4",
        "responsible": "Recovery nurses (monitor); discharging clinician (sign-off)",
        "records": [
            "Post-procedure monitoring records with objective scoring tool.",
            "Documented discharge criteria met before patient left recovery.",
            "Signed recovery discharge record by clinician.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.9 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Procedural sedation is provided consistently and safely." COP.9.a–e PDF index 72. Asterisked OE: a. All Commitment level.

SHAPE: Five What-we-do subsections (5.1–5.5). Stop-work: YES. Disclaimer accreditation-only. COP anaesthesia/sedation roles."""


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
        "subtitle": "Consistent and safe procedural sedation.",
        "doc_no": D("COP/POL/09"),
        "stop_work": STOP_WORK,
    }
    emit_pre_v2(
        draft,
        "cop9_v2_draft.json",
        "COP.9_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
