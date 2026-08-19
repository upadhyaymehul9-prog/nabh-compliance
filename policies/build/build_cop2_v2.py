# -*- coding: utf-8 -*-
"""COP.2 v2 — emergency services, ambulance and disaster management.

Shape follows PRE.1 v2 (section list and order only). Wording from COP.2 OEs
(NABH SHCO 3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9),
printed pages 67–68 / PDF indices 67–68.

Stop-work section present. Disclaimer P2 names medico-legal and Disaster Management Act.
Eleven OEs (COP.2.a–k).
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.2"
CHAPTER = "COP"
OE_CODES = [
    "COP.2.a", "COP.2.b", "COP.2.c", "COP.2.d", "COP.2.e", "COP.2.f",
    "COP.2.g", "COP.2.h", "COP.2.i", "COP.2.j", "COP.2.k",
]
POLICY_TITLE = "Emergency Services, Ambulance and Disaster Management"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: plain English, COP roles, eleven OEs, stop-work, medico-legal/DMA disclaimer.",
    },
]

STATEMENT_OF_INTENT = (
    "Emergency services including ambulance, and management of disasters, are provided "
    "in accordance with written guidance, applicable laws and regulations — not a poster "
    "on the emergency-department wall that no one has drilled."
)

PURPOSE = f"""This policy says how {HOSPITAL} provides emergency services including ambulance, and manages disasters, in accordance with written guidance, applicable laws and regulations.

It covers eleven elements: an identified, accessible emergency area with adequate resources; medico-legal case management in consonance with statutory requirements; triage-guided initiation of care; reassessment of waiting patients; admission, discharge or transfer documentation; a quality-assurance programme; management of patients dead on arrival or dying within minutes; access to ambulance services; ambulance fitness, equipment and medications; early treatment initiation during transit; and disaster and epidemic management.

This policy owns emergency clinical care, triage and ambulance. AAC.2 owns the registration, admission, transfer and discharge process. FMS.5 owns fire and non-fire facility emergencies. COP.3 owns CPR.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the emergency department of {HOSPITAL} and to every staff member who provides emergency care: emergency doctors, emergency nurses, triage nurses, ambulance personnel, the Medical Superintendent, and the {D('Quality Coordinator')}.

It covers the eleven elements COP.2.a–k name. It does not cover fire or non-fire facility emergencies (FMS.5), the registration or transfer process (AAC.2), or CPR (COP.3).

Boundaries with other policies of {HOSPITAL}:

- AAC.2 owns registration, admission, transfer and discharge process. This policy owns emergency clinical care, triage and ambulance.
- FMS.5 owns fire and non-fire facility emergencies. This policy owns clinical disaster and epidemic response.
- COP.3 owns CPR. This policy owns that CPR-trained staff are available in the emergency department.
- COP.1 owns uniform care. This policy owns that uniform care extends to emergency patients.
- PRE.3 owns informed consent method. This policy owns that medico-legal cases receive emergency care in consonance with statutory requirements."""

POLICY_STATEMENT = f"""{HOSPITAL} maintains an identified area that is easily accessible to receive and manage emergency patients, with adequate and appropriate resources including staff, equipment and medications available {D('24 hours a day, 7 days a week')}.

{HOSPITAL} manages medico-legal cases and provides emergency care in consonance with statutory requirements and in accordance with written guidance. No emergency patient is refused stabilisation because of a medico-legal concern.

{HOSPITAL} uses a system of triage to guide initiation of appropriate care. Patients waiting in the emergency are reassessed as appropriate for the change in status at intervals defined by the triage category.

Admission, discharge to home or transfer to another organisation is documented, and a discharge note is given to the patient.

{HOSPITAL} implements a quality-assurance programme for the emergency department.

{HOSPITAL} has systems for managing patients found dead on arrival and patients who die within a few minutes of arrival.

{HOSPITAL} has access to ambulance services commensurate with the scope of services provided. Ambulances are fit for purpose, operated by trained personnel, appropriately equipped, and carry emergency medications.

Where resources allow, the emergency department identifies opportunities to initiate treatment at the earliest when the patient is in transit to the organisation.

{HOSPITAL} manages potential community emergencies, epidemics and other disasters as per a documented plan.

{HOSPITAL} does not treat any of these as meeting this policy: an emergency department that locks its door at night; a medico-legal case refused stabilisation; a triage tag that is never followed up; or a disaster plan that has never been drilled."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no shift convenience exception.

1. Refusing stabilisation of an emergency patient for any reason, including inability to pay or a medico-legal concern.
2. Leaving a triaged patient unmonitored beyond the triage reassessment interval assigned to that category.
3. Discharging or transferring an emergency patient without documented stabilisation and a discharge or transfer note given to the patient.
4. Operating the emergency department without the minimum staff, equipment and medications needed for the scope of services this hospital offers.
5. Transporting a patient by ambulance without trained personnel, working equipment and emergency medications on board.
6. Declaring a patient dead on arrival without following the hospital's written system for dead-on-arrival management.
7. Ignoring a documented disaster plan during a community emergency, epidemic or disaster, or having a plan that has never been drilled.
8. Initiating triage without following the adopted triage system, or using triage categories that have no defined reassessment intervals.

Staff who see one of these acts report it the same shift to the {D('emergency department in-charge')} or the Medical Superintendent."""

PROCEDURE_STEPS = [
f"""5.1 Identified and accessible emergency area with adequate resources

{HOSPITAL} maintains an identified area that is easily accessible to receive and manage emergency patients. The area is signposted from the main entrance and from the road. It is accessible to ambulances without obstruction.

Resources include: {D('at least one emergency doctor and one emergency nurse on duty at all times')}; resuscitation equipment and crash cart (COP.3 owns CPR); essential medications as per the emergency drug list reviewed {D('annually')}; and diagnostic support commensurate with the scope of services.

The {D('emergency department in-charge')} holds the resource inventory and reviews it {D('quarterly')}.""",

f"""5.2 Medico-legal cases and statutory emergency care

{HOSPITAL} manages medico-legal cases and provides emergency care in consonance with statutory requirements. No emergency patient is refused stabilisation. Medico-legal documentation follows written guidance that includes: recording of injuries and their probable cause; informing the police as required; chain-of-custody procedures for evidence; and protection of the patient's rights throughout.

The written guidance is reviewed {D('annually')} by the Medical Superintendent. Staff are trained on medico-legal documentation at induction and {D('annually')}.

This policy does not rewrite the applicable medico-legal provisions. It requires that {HOSPITAL} has written guidance that is followed.""",

f"""5.3 Triage-guided initiation of care

{HOSPITAL} uses a system of triage to guide initiation of appropriate care. The triage system is {D('a colour-coded or numbered system adopted by the hospital')} that assigns a category and a reassessment interval to every patient who presents to the emergency department.

Triage is performed by a {D('trained triage nurse')} at presentation. The triage category, time of triage and reassessment interval are recorded. Initiation of care follows the triage category — the most urgent patients are seen first.

The triage system is reviewed {D('annually')} and staff are trained on it at induction and {D('annually')}.""",

f"""5.4 Reassessment of waiting emergency patients

Patients waiting in the emergency are reassessed as appropriate for the change in status. The reassessment interval is defined by the triage category. A patient whose condition worsens is re-triaged and escalated.

The triage nurse or the emergency nurse monitors waiting patients. A waiting patient who has not been reassessed within the interval is a finding.

Reassessment is documented in the patient record.""",

f"""5.5 Admission, discharge or transfer documentation

Admission to in-patient, discharge to home, or transfer to another organisation is documented. A discharge note is given to the patient at discharge. A transfer note accompanies the patient during transfer.

The discharge note includes: diagnosis or provisional diagnosis; treatment given in the emergency; follow-up instructions; and medications prescribed. The transfer note includes: reason for transfer; condition at transfer; treatment given; and the receiving organisation's acceptance.

AAC.2 owns the transfer process. This policy owns that the documentation is completed before the patient leaves.""",

f"""5.6 Emergency department quality-assurance programme

{HOSPITAL} implements a quality-assurance programme for the emergency department. The programme includes: monitoring of triage-to-doctor time; monitoring of left-without-being-seen rates; monitoring of unplanned re-visits within {D('72 hours')}; and review of adverse events.

The {D('Quality Coordinator')} collects and analyses the indicators {D('monthly')}. The emergency department in-charge reviews findings and implements corrective actions.

Results are reported to the Medical Superintendent {D('quarterly')}.""",

f"""5.7 Dead on arrival and early death management

{HOSPITAL} has systems in place for the management of patients found dead on arrival and patients who die within a few minutes of arrival. The system includes: confirmation of death by a doctor; documentation; informing the police where required; informing the family; and handling of the body with dignity.

The written guidance is held by the {D('emergency department in-charge')} and reviewed {D('annually')}.""",

f"""5.8 Access to ambulance services

{HOSPITAL} has access to ambulance services commensurate with the scope of services provided. Access means: {D('own ambulance or documented tie-up with an ambulance provider')} with a response time agreed in writing.

The ambulance service is available {D('24 hours a day, 7 days a week')}. The agreement or internal arrangement is reviewed {D('annually')} by the Medical Superintendent.""",

f"""5.9 Ambulance fitness, equipment, personnel and medications

Ambulances used by or on behalf of {HOSPITAL} are fit for purpose, operated by trained personnel, appropriately equipped, and carry emergency medications.

Fitness includes: roadworthiness certificate current; insurance current; cleanliness and infection-control compliance. Equipment includes: stretcher, oxygen, suction, basic airway management, first-aid kit, and communication equipment. Medications follow the {D('emergency ambulance drug list reviewed annually')}.

Personnel are trained in basic life support and ambulance operation. Training records are held by the {D('emergency department in-charge')}.""",

f"""5.10 Early treatment initiation during transit

Where resources allow, the emergency department identifies opportunities to initiate treatment at the earliest when the patient is in transit to the organisation. This may include: telephonic triage and advice to the ambulance crew; remote monitoring where equipment allows; and pre-alerting the emergency team.

The written guidance for early treatment initiation is held by the {D('emergency department in-charge')} and reviewed {D('annually')}.

If this hospital does not have the resources for early treatment during transit, record that as a written limitation.""",

f"""5.11 Disaster, epidemic and community emergency management

{HOSPITAL} manages potential community emergencies, epidemics and other disasters as per a documented plan. The plan includes: activation criteria; command structure; communication plan; surge capacity; resource mobilisation; staff recall; and deactivation criteria.

The plan is drilled {D('annually')} with a documented after-action review. Lessons learned are incorporated into the plan.

FMS.5 owns fire and non-fire facility emergencies. This policy owns clinical disaster and epidemic response. The two plans must not contradict each other.

The plan is reviewed {D('annually')} and after every activation or drill by the Medical Superintendent.""",
]

STOP_WORK = f"""Do not go ahead if you are about to do any of the following:

- transfer an emergency patient without documented stabilisation;
- leave a triaged patient unmonitored beyond the triage reassessment interval;
- transport a patient in an ambulance without trained personnel and working equipment;
- refuse stabilisation of an emergency patient for any reason.

If you can do so safely, keep the patient monitored. Tell the {D('emergency department in-charge')} the same shift. If that person is not on site, tell the Medical Superintendent.

Refusing in good faith to transfer an unstabilised patient is not a disciplinary matter."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that emergency services, ambulance and disaster management operate as this policy requires.
- Holds the register of applicable medico-legal provisions.
- Approves the disaster plan and names the command structure.

{D('Emergency department in-charge')}
- Holds the resource inventory, triage system, medico-legal guidance, dead-on-arrival system, ambulance arrangements, and early-treatment and disaster plans.
- Reviews emergency department operations and implements corrective actions.

Emergency doctors and nurses
- Deliver emergency care in consonance with triage, statutory requirements and adopted guidelines.

{D('Triage nurse')}
- Performs triage at presentation, assigns category and reassessment interval, monitors waiting patients.

Ambulance personnel
- Operate the ambulance safely, maintain equipment and medications, hold current training in basic life support.

Quality Coordinator
- Collects and analyses emergency department quality indicators {D('monthly')}.
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when findings recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at records and at the emergency department floor.

What is monitored each quarter:

- Emergency area is accessible, signposted, and resourced as this policy requires.
- Medico-legal guidance is current and staff are trained.
- Triage system is applied to every patient, with reassessment intervals followed.
- Admission, discharge and transfer documentation is complete, and discharge notes are given.
- Quality-assurance indicators (triage-to-doctor time, left-without-being-seen, unplanned re-visits, adverse events) are collected and acted upon.
- Dead-on-arrival and early-death system is current.
- Ambulance fitness, equipment, medications and personnel training are current.
- Disaster plan has been drilled within the last twelve months.

Root-cause analysis is required when: an emergency patient is transferred without documented stabilisation; a triaged patient is found unmonitored beyond the interval; or the disaster plan fails during a drill or activation.

This policy is reviewed {D('annually')}, and sooner when the disaster plan is activated, the scope of services changes, or an applicable medico-legal provision changes."""

TRAINING_ACKNOWLEDGEMENT = f"""All emergency department staff, ambulance personnel and triage nurses are trained on this policy at induction and {D('once a year')} after that. Training covers triage, medico-legal documentation, stop-work authority, ambulance readiness, dead-on-arrival management, and the disaster plan.

Staff acknowledgement

I have read this Emergency Services, Ambulance and Disaster Management policy of {HOSPITAL}. I will not transfer an emergency patient without documented stabilisation. I will not leave a triaged patient unmonitored beyond the reassessment interval.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The emergency department in-charge holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/02"),
    version=VERSION,
    prepared_by=D("Emergency department in-charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.2.
- Disaster Management Act, 2005 — insofar as the organisation participates in managing community emergencies and disasters.
- Internal documents of {HOSPITAL}: emergency department resource inventory; triage system; medico-legal written guidance; dead-on-arrival system; ambulance arrangements; disaster plan; quality-assurance programme indicators; FMS.5 fire and non-fire emergency plan; AAC.2 transfer process; COP.3 CPR policy."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the emergency department in-charge and the Quality Coordinator.

Copies issued to: emergency department; ambulance crew; nursing administration; registration (for transfer documentation).

The current version is available to all staff at the {D('emergency department policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
COP — Care of Patients (NABH SHCO chapter 5)
CPR — cardiopulmonary resuscitation
DMA — Disaster Management Act, 2005
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
RCA — root-cause analysis
SHCO — Standards for Small Healthcare Organisations"""

STATUTE_CLAUSE = (
    "the applicable medico-legal provisions insofar as emergency care is provided "
    "in consonance with statutory requirements, and the Disaster Management Act, 2005, "
    "insofar as the organisation participates in managing community emergencies and disasters"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "COP.2.a",
        "requirement": "There shall be an identified area in the organization, which is easily accessible to receive and manage emergency patients, with adequate and appropriate resources.",
        "steps": "Section 3; 5.1 Identified and accessible emergency area with adequate resources",
        "responsible": "Emergency department in-charge (resource inventory); Medical Superintendent (accountable)",
        "records": [
            "Resource inventory reviewed quarterly.",
            "Signposting from main entrance and road.",
            "Staff roster showing coverage at all times.",
        ],
    },
    {
        "oe_code": "COP.2.b",
        "requirement": "The organization manages medico-legal cases and provides emergency care in consonance with statutory requirements and in accordance with written guidance.",
        "steps": "Section 3; 5.2 Medico-legal cases and statutory emergency care; Section 4 item 1",
        "responsible": "Medical Superintendent (statutory register); emergency doctors (documentation); emergency department in-charge (guidance)",
        "records": [
            "Written medico-legal guidance reviewed annually.",
            "Training records for medico-legal documentation at induction and annually.",
            "Sample medico-legal case documentation.",
            "Quarterly audit sample of medico-legal case management.",
        ],
    },
    {
        "oe_code": "COP.2.c",
        "requirement": "Initiation of appropriate care is guided by a system of triage.",
        "steps": "Section 3; 5.3 Triage-guided initiation of care; Section 4 item 8",
        "responsible": "Triage nurse (perform triage); emergency department in-charge (system owner)",
        "records": [
            "Written triage system with categories and reassessment intervals.",
            "Triage records for every emergency patient showing category, time and interval.",
            "Annual review record of triage system.",
            "Training records for triage at induction and annually.",
        ],
    },
    {
        "oe_code": "COP.2.d",
        "requirement": "Patients waiting in the emergency are reassessed as appropriate for the change in status.",
        "steps": "Section 3; 5.4 Reassessment of waiting emergency patients; Section 4 item 2",
        "responsible": "Triage nurse or emergency nurse (reassess); emergency department in-charge (monitor compliance)",
        "records": [
            "Reassessment records in patient record at intervals defined by triage category.",
            "Re-triage records when a patient's condition worsens.",
            "Quarterly audit of reassessment interval compliance.",
        ],
    },
    {
        "oe_code": "COP.2.e",
        "requirement": "Admission, discharge to home or transfer to another organization is documented, and a discharge note shall be given to the patient.",
        "steps": "Section 3; 5.5 Admission, discharge or transfer documentation; Section 4 item 3",
        "responsible": "Emergency doctors (document); emergency nurses (ensure note given); AAC.2 (transfer process)",
        "records": [
            "Discharge note given to patient at discharge.",
            "Transfer note accompanying patient during transfer.",
            "Quarterly audit of documentation completeness.",
        ],
    },
    {
        "oe_code": "COP.2.f",
        "requirement": "The organization shall implement a quality assurance programme.",
        "steps": "Section 3; 5.6 Emergency department quality-assurance programme",
        "responsible": "Quality Coordinator (collect and analyse); emergency department in-charge (corrective actions); Medical Superintendent (review)",
        "records": [
            "Monthly indicator data: triage-to-doctor time, left-without-being-seen, unplanned re-visits, adverse events.",
            "Quarterly report to Medical Superintendent.",
            "Corrective action records for findings.",
            "CAPA records when findings recur.",
        ],
    },
    {
        "oe_code": "COP.2.g",
        "requirement": "The organization has systems in place for the management of patients found dead on arrival and patients who die within a few minutes of arrival.",
        "steps": "Section 3; 5.7 Dead on arrival and early death management; Section 4 item 6",
        "responsible": "Emergency department in-charge (written guidance); emergency doctors (confirm death and document)",
        "records": [
            "Written guidance for dead-on-arrival and early-death management reviewed annually.",
            "Records of dead-on-arrival and early-death cases.",
            "Police notification records where required.",
        ],
    },
    {
        "oe_code": "COP.2.h",
        "requirement": "The organization has access to ambulance services commensurate with the scope of services provided by it.",
        "steps": "Section 3; 5.8 Access to ambulance services",
        "responsible": "Medical Superintendent (arrangement); emergency department in-charge (operations)",
        "records": [
            "Written ambulance arrangement or tie-up with response time.",
            "Annual review of ambulance arrangement.",
            "Availability records showing 24/7 access.",
        ],
    },
    {
        "oe_code": "COP.2.i",
        "requirement": "The ambulance(s) is fit for purpose, is operated by trained personnel, is appropriately equipped, and ensures that emergency medications are available in the ambulance.",
        "steps": "Section 3; 5.9 Ambulance fitness, equipment, personnel and medications; Section 4 item 5",
        "responsible": "Emergency department in-charge (fitness and training records); ambulance personnel (operate)",
        "records": [
            "Roadworthiness and insurance certificates current.",
            "Equipment checklist verified regularly.",
            "Emergency ambulance drug list reviewed annually.",
            "Personnel training records in basic life support and ambulance operation.",
        ],
    },
    {
        "oe_code": "COP.2.j",
        "requirement": "The emergency department identifies opportunities to initiate treatment at the earliest, when the patient is in transit to the organization.",
        "steps": "Section 3; 5.10 Early treatment initiation during transit",
        "responsible": "Emergency department in-charge (written guidance); emergency doctors (telephonic triage)",
        "records": [
            "Written guidance for early treatment initiation during transit reviewed annually.",
            "Records of telephonic triage or remote advice to ambulance crew.",
            "Written limitation record if resources do not allow early treatment during transit.",
        ],
    },
    {
        "oe_code": "COP.2.k",
        "requirement": "The organization manages potential community emergencies, epidemics and other disasters as per a documented plan.",
        "steps": "Section 3; 5.11 Disaster, epidemic and community emergency management; Section 4 item 7",
        "responsible": "Medical Superintendent (plan owner and command structure); emergency department in-charge (operational execution)",
        "records": [
            "Documented disaster plan with activation criteria, command structure, communication, surge capacity, staff recall and deactivation.",
            "Annual drill record with after-action review.",
            "Plan review record annually and after every activation or drill.",
            "FMS.5 non-contradiction check record.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.2 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Emergency services including ambulance, and management of disasters, are provided in accordance with written guidance, applicable laws and regulations." COP.2.a–e PDF page 67; COP.2.f–k PDF page 68. COP.2.b asterisked (Commitment). COP.2.c asterisked (Core). COP.2.f asterisked (Achievement). COP.2.k asterisked (Commitment). COP.2.j Excellence.

SHAPE: Eleven What-we-do subsections (5.1–5.11). Stop-work present. Disclaimer P2 names medico-legal provisions and Disaster Management Act, 2005. COP roles only."""


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
        "template_test": "cop_v2_adoptable_shape",
        "subtitle": "Emergency care, ambulance and disaster management in day-to-day work.",
        "doc_no": D("COP/POL/02"),
    }
    emit_pre_v2(
        draft,
        "cop2_v2_draft.json",
        "COP.2_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
