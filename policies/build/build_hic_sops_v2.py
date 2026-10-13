# -*- coding: utf-8 -*-
"""Builds the 6 HIC (Hospital Infection Control) SOPs -- plus their Records
and manifest.json -- in the plain-body + audit-appendix format used for
FMS, ROM, AAC, HRM, COP, MOM, PRE and PSQ (2026-10-13).

No SOP/Record pack existed for HIC before this script:
policies/build/sop_record_masters/HIC/ is created fresh here. The content
is not invented -- it is drawn directly from the SHCO 3rd Edition HIC
Master Policy pipeline that was already built and approved for this
hospital (policies/drafts/hic{1..6}_v2_draft.json), which carries the
correct SHCO scope (6 standards, 36 OEs across HIC.1-HIC.6), the
already-approved responsibility/record mapping, and already-concrete
procedure detail (bundles, numeric thresholds, named defaults in
«...» brackets). This script recasts that content into the plain-body +
appendix template, removing every bare NABH code that the draft's own
procedure_steps text used as shorthand cross-references (e.g. "(HIC.2.c)",
"under HIC.5.b") -- those become plain descriptive phrases in the body,
and the actual cross-reference moves to each item's Appendix-only
`boundary` field, matching the fix PSQ went through for the same issue.

External technical sources (WHO, CDC/HICPAC, CPCB) were verified live via
WebSearch on 2026-10-13 before being written in here -- see the citation
constants below, each carrying a real, checked URL.

Writes:
  policies/build/sop_record_masters/HIC/SOP_HIC.N...docx   (6 files)
  policies/build/sop_record_masters/HIC/Records/HIC.N_Record_NN_*.docx
  policies/build/sop_record_masters/HIC/manifest.json
"""
from __future__ import annotations

import json
from pathlib import Path

from sop_record_common import (
    PlainItem,
    SOPSpecV2,
    RecordSpec,
    build_sop_v2,
    build_record,
)

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "HIC"
RECORDS_ROOT = OUT_ROOT / "Records"

NABH_HIC_CITE = (
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). "
    "Hospital Infection Control chapter, standard {code}."
)
WHO_CORE_IPC_SRC = (
    "World Health Organization. (2016). [Guidelines on core components of "
    "infection prevention and control programmes at the national and acute "
    "health care facility level](https://www.who.int/publications/i/item/9789241549929). "
    "Geneva: WHO -- the internationally recognised framework this hospital's "
    "infection-control programme, committee and team structure are built on."
)
WHO_HAND_HYGIENE_SRC = (
    "World Health Organization. (2009). [WHO guidelines on hand hygiene in "
    "health care](https://www.who.int/publications/i/item/9789241597906). "
    "Geneva: WHO -- the source of the five-moments method and the "
    "observation-audit approach this hospital's hand-hygiene protocol and "
    "surveillance are built on."
)
CDC_CAUTI_SRC = (
    "Centers for Disease Control and Prevention. (2009, updated 2017). "
    "[Catheter-associated urinary tract infections (CAUTI) prevention "
    "guideline](https://www.cdc.gov/infection-control/hcp/cauti/). Atlanta, "
    "GA: CDC/HICPAC -- the source of the catheter insertion-and-maintenance "
    "bundle this hospital's CAUTI-prevention steps are built on."
)
CDC_CLABSI_SRC = (
    "Centers for Disease Control and Prevention. (2011). [Guidelines for the "
    "prevention of intravascular catheter-related "
    "infections](https://cdc.gov/infection-control/hcp/intravascular-catheter-related-infections/introduction.html). "
    "Atlanta, GA: CDC/HICPAC -- the source of the central-line insertion-and-"
    "maintenance bundle this hospital's CLABSI-prevention steps are built on."
)
WHO_SSI_SRC = (
    "World Health Organization. (2018). [Global guidelines for the "
    "prevention of surgical site "
    "infection](https://www.who.int/publications/i/item/9789241550475) (2nd "
    "ed.). Geneva: WHO -- the source of the pre-/intra-/post-operative "
    "bundle this hospital's SSI-prevention steps are built on."
)
CDC_PEP_SRC = (
    "Centers for Disease Control and Prevention. (2005). [Updated U.S. "
    "Public Health Service guidelines for the management of occupational "
    "exposures to HBV, HCV, and HIV and recommendations for postexposure "
    "prophylaxis](https://stacks.cdc.gov/view/cdc/7305). MMWR Recommendations "
    "and Reports, 54(RR-9). Atlanta, GA: CDC -- the internationally cited "
    "source this hospital's post-exposure-prophylaxis timelines and "
    "follow-up testing schedule are built on."
)
CPCB_BMW_SRC = (
    "Central Pollution Control Board, Ministry of Environment, Forest and "
    "Climate Change, Government of India. (2016). [Bio-Medical Waste "
    "Management Rules, 2016](https://cpcb.nic.in/bio-medical/), as amended. "
    "New Delhi: CPCB -- the legally binding colour-coded segregation and "
    "disposal scheme this hospital's biomedical-waste handling is built on."
)
WHO_DECON_REPROCESS_SRC = (
    "World Health Organization. (2016). [Decontamination and reprocessing "
    "of medical devices for health-care "
    "facilities](https://www.who.int/publications/i/item/9789241549851). "
    "Geneva: WHO -- the source of the cleaning-packing-sterilisation-"
    "storing-issue cycle this hospital's CSSD procedure is built on."
)
CDC_DISINFECTION_STERILIZATION_SRC = (
    "Centers for Disease Control and Prevention. (2008, updated 2019). "
    "[Guideline for disinfection and sterilization in healthcare "
    "facilities](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/summary-recommendations.html). "
    "Atlanta, GA: CDC/HICPAC -- the source of the validation-testing "
    "regimen (biological indicators, Bowie-Dick test) this hospital's "
    "sterilisation-verification steps are built on."
)

SOPS: list[tuple[str, SOPSpecV2]] = []
RECORDS: list[tuple[str, int, str, RecordSpec]] = []


def _add(sop_code: str, idx: int, spec: RecordSpec, slug: str) -> None:
    RECORDS.append((sop_code, idx, slug, spec))


# ============================================================== HIC.1 ====
HIC1 = SOPSpecV2(
    sop_no="SOP-HIC.1",
    title="Hospital Infection Prevention and Control Programme",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» runs one documented "
        "infection-control programme covering every clinical and support "
        "area, scored every year against an assessment tool, overseen by a "
        "multidisciplinary committee and a day-to-day team, backed by "
        "community education and outbreak participation, properly "
        "resourced by management, and backed by isolation/barrier-nursing "
        "facilities for patients who need them."
    ),
    purpose_trigger=(
        "A hospital writes an infection-control manual once, five years "
        "ago, and nobody has looked at it since -- gaps nobody owns pile up "
        "quietly until an outbreak forces someone to notice. This SOP is "
        "what keeps the programme a living document instead of a shelf "
        "copy."
    ),
    purpose_why=(
        "We do this because healthcare-associated infection is not random "
        "-- it follows gaps in exactly the things this programme is meant "
        "to run: a committee that never meets, resources that were never "
        "actually budgeted, an isolation bed that does not exist when the "
        "first infectious patient of the season arrives."
    ),
    purpose_text=(
        "To define how «Hospital Name» establishes and maintains the "
        "hospital infection prevention and control (HIC) programme: the "
        "programme document itself, its annual review against an "
        "assessment tool, the multidisciplinary infection control "
        "committee and team that run it, community education and outbreak "
        "participation, the resources management provides for it, and the "
        "isolation/barrier-nursing facilities it maintains."
    ),
    scope_why=(
        "so every clinical and support department -- not only the "
        "Infection Control Officer -- knows this programme covers their "
        "area and they have a part to play in it."
    ),
    scope_text=(
        "Applies to all clinical and support service areas of «Hospital "
        "Name» and to every staff member, visitor and contractor whose "
        "activities could affect infection risk: the Medical "
        "Superintendent, the Infection Control Officer and Nurse, the "
        "infection control committee, and department heads across "
        "medical, nursing, administration, housekeeping, CSSD, kitchen, "
        "laundry and laboratory services. It covers how the programme "
        "itself is documented, reviewed, governed and resourced, and how "
        "isolation facilities are provided. It does not cover the detailed "
        "clinical precautions used in patient care, support-service "
        "infection control, prevention of specific device- and procedure-"
        "linked infections, or surveillance methodology -- each of those "
        "is set out in its own separate SOP in this chapter."
    ),
    responsibility_why=(
        "a programme with no named committee, no named reviewer and no "
        "named budget-holder exists on paper only -- naming who does what "
        "is what makes it real."
    ),
    responsibilities=[
        ("Medical Superintendent", "Approves the HIC programme document; approves resource allocation and budget; liaises with district health authorities during community outbreak or pandemic response; provides isolation/barrier-nursing facilities."),
        ("Infection Control Officer", "Documents and maintains the HIC programme; plans and implements the IEC programme; defines isolation, de-isolation and transfer criteria."),
        ("Infection Control Committee", "Reviews the programme annually against the assessment tool; submits the annual resource requirement plan; oversees community-outbreak participation."),
        ("Quality Coordinator", "Tracks closure of gaps identified in the annual programme review."),
        ("Nursing In-Charge", "Maintains isolation/barrier-nursing facility readiness; ensures staff assigned to isolation duties are trained."),
    ],
    items=[
        PlainItem(
            heading="Keep one documented infection-control programme for the whole hospital",
            why=(
                "A hospital with no single written programme has no one "
                "place that says what infection control actually covers -- "
                "gaps between departments go unnoticed because nobody owns "
                "the whole picture."
            ),
            body=[
                "The Infection Control Officer and the Infection Control "
                "Committee maintain a documented HIC programme that aims "
                "at preventing and reducing the risk of healthcare-"
                "associated infection at «Hospital Name». The programme "
                "covers all clinical and support service areas.",
                "The programme document includes: objectives, scope, the "
                "surveillance plan, antimicrobial-stewardship references, "
                "biomedical-waste-management references, disinfection and "
                "sterilisation references, the outbreak-response plan, "
                "the training schedule and resource requirements.",
                "The programme is approved by the «Medical Superintendent» "
                "and is made available to all staff at «the infection "
                "control manual / staff intranet».",
            ],
            oe_code="HIC.1.a",
            technical_sources=[WHO_CORE_IPC_SRC],
        ),
        PlainItem(
            heading="Review the programme every year against a scoring tool",
            why=(
                "A programme that is never scored against anything just "
                "repeats last year's gaps -- scoring it is what turns "
                "\"we have a programme\" into \"we know exactly where it "
                "is weak.\""
            ),
            body=[
                "The Infection Control Committee reviews the programme "
                "«annually» using an infection control assessment tool "
                "(such as the NABH infection control assessment checklist "
                "or an equivalent validated tool).",
                "Findings from the review are documented, gaps are "
                "identified, and a corrective action plan with timelines "
                "and named responsibility is prepared. The «Quality "
                "Coordinator» tracks closure of each gap to completion.",
            ],
            oe_code="HIC.1.b",
            technical_sources=[WHO_CORE_IPC_SRC],
        ),
        PlainItem(
            heading="Run a multidisciplinary infection control committee and a day-to-day team",
            why=(
                "Infection control decided by doctors alone misses what "
                "housekeeping, the kitchen, the laundry and CSSD each see "
                "in their own area every day -- the committee exists so "
                "those perspectives are actually in the room."
            ),
            body=[
                "«Hospital Name» maintains a multidisciplinary Infection "
                "Control Committee (ICC) that includes representatives "
                "from medical, nursing, administration, housekeeping, "
                "CSSD, kitchen, laundry and laboratory services. The "
                "committee meets «quarterly» or more often when required.",
                "An Infection Control Team (ICT) -- the Infection Control "
                "Officer (a doctor) and the Infection Control Nurse -- "
                "coordinates day-to-day implementation of every infection "
                "prevention and control activity. The ICT reports to the "
                "ICC.",
                "Minutes of ICC meetings, attendance, decisions and "
                "action items are documented at every meeting.",
            ],
            oe_code="HIC.1.c",
        ),
        PlainItem(
            heading="Educate the community and take part in outbreak and pandemic response",
            why=(
                "An infection-control programme that stops at the "
                "hospital's front door misses that most infections a "
                "patient brings in, and most outbreaks a hospital has to "
                "respond to, start in the community it serves."
            ),
            body=[
                "«Hospital Name» implements an information, education and "
                "communication (IEC) programme for infection prevention "
                "and control directed at the community -- including "
                "patients, visitors and caregivers -- covering hand "
                "hygiene, respiratory etiquette, immunisation awareness "
                "and seasonal infection alerts.",
                "«Hospital Name» participates in managing community "
                "outbreaks and pandemics when requested by local or "
                "district health authorities. The response plan is "
                "documented and reviewed «annually» or after every "
                "activation.",
            ],
            oe_code="HIC.1.d",
        ),
        PlainItem(
            heading="Give the infection-control programme the people, supplies and budget it needs",
            why=(
                "A programme management says it supports but never "
                "actually staffs or funds is a programme that will quietly "
                "run short of PPE or hand-hygiene supplies exactly when it "
                "is needed most."
            ),
            body=[
                "The management of «Hospital Name» makes available the "
                "resources required for the infection-control programme: "
                "trained manpower (an Infection Control Officer and "
                "Nurse), personal protective equipment (PPE), hand-"
                "hygiene consumables, disinfectants, sterilisation "
                "equipment, isolation facilities, signage, and budget "
                "allocation for surveillance and training.",
                "The Infection Control Committee submits a resource "
                "requirement plan «annually» to the «Medical "
                "Superintendent». Any shortfall is escalated formally, "
                "in writing, rather than absorbed silently.",
            ],
            oe_code="HIC.1.e",
        ),
        PlainItem(
            heading="Provide isolation and barrier-nursing facilities",
            why=(
                "A patient with an airborne or highly transmissible "
                "infection nursed in an open bay puts every other patient "
                "and every staff member on that ward at risk -- isolation "
                "capacity has to already exist, not be improvised when the "
                "patient arrives."
            ),
            body=[
                "«Hospital Name» provides isolation/barrier-nursing "
                "facilities for patients with communicable or highly "
                "transmissible infections. Facilities include «a single "
                "room with dedicated toilet, negative-pressure "
                "ventilation where feasible, and PPE supplies at the "
                "entry».",
                "Where a dedicated isolation room is not available, "
                "barrier-nursing precautions are applied at the bedside "
                "under a documented protocol. Criteria for isolation, "
                "de-isolation and transfer are defined in writing.",
                "Staff assigned to isolation areas are trained in "
                "transmission-based precautions as part of this "
                "hospital's clinical infection-control protocol.",
            ],
            oe_code="HIC.1.f",
            boundary=[
                "The transmission-based-precautions technique itself (contact/droplet/airborne, signage, de-escalation) is owned by HIC.2.c; this step is the physical facility and criteria for using it.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the HIC.1 Records folder).",
    related_documents=[
        "Hospital's Infection Prevention and Control in Clinical Areas SOP (HIC.2)",
        "Hospital's Infection Prevention and Control in Support Services SOP (HIC.3)",
        "Hospital's Infection Prevention and Control Surveillance SOP (HIC.5)",
        "Hospital's Patient-Safety Programme and Quality Improvement Programme SOP (PSQ.1)",
    ],
    review_text=(
        "This SOP is reviewed annually, alongside the annual programme "
        "review against the assessment tool, or sooner if the Infection "
        "Control Committee is found not to have met for two consecutive "
        "quarters, or if a related policy named above in this chapter is "
        "revised."
    ),
    full_reference_list=[
        NABH_HIC_CITE.format(code="HIC.1"),
        WHO_CORE_IPC_SRC,
    ],
)

SOPS.append(("SOP_HIC.1.a_to_f_hospital_infection_prevention_control_programme.docx", HIC1))

# ---- HIC.1 Records -------------------------------------------------
_add("HIC.1", 1, RecordSpec(
    oe_code="HIC.1.a",
    oe_requirement="The hospital infection prevention and control programme is documented, which aims at preventing and reducing the risk of healthcare associated infections in the hospital.",
    record_title="HIC.1 Record 01 — HIC programme document and approval register",
    what_is_this="This record is the proof the HIC programme is actually written down with every required element, approved by name, and kept available to staff -- not an idea everyone assumes exists.",
    real_example="The HIC programme manual, version 3.0, approved by the Medical Superintendent on 10-Jan-2026, is placed on the staff intranet and reviewed for currency every January.",
    why_nabh_asks="A hospital with no single written programme has no one place that says what infection control actually covers -- gaps between departments go unnoticed because nobody owns the whole picture.",
    how_to_fill=[
        ("Programme Element", "Which part of the programme (surveillance plan, antimicrobial stewardship references, BMW references, etc.)."),
        ("Document Reference / Version", "Where it lives and which version."),
        ("Approved By / Date", "Medical Superintendent's sign-off."),
        ("Availability Location", "Where staff can access it."),
        ("Next Review Due", "Date of next annual review."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.1"), WHO_CORE_IPC_SRC],
    column_headers=["Programme Element", "Document Reference / Version", "Approved By / Date", "Availability Location", "Next Review Due"],
    worked_example_row=["WORKED EXAMPLE — Surveillance plan", "HIC Manual v3.0, Section 4", "Dr. Rao (MS) — 10-Jan-2026", "Staff intranet / ICC office", "Jan-2027"],
), "hic_programme_document_approval_register")

_add("HIC.1", 2, RecordSpec(
    oe_code="HIC.1.b",
    oe_requirement="The infection prevention and control programme is reviewed based on infection control assessment tool.",
    record_title="HIC.1 Record 02 — Annual infection control assessment and gap-closure tracker",
    what_is_this="This record is the proof the programme was actually scored against an assessment tool each year, with gaps named, owned and tracked to closure -- not a review that produced a score and nothing else.",
    real_example="The 2026 assessment scores the programme at 78%, flags BMW segregation training as a gap, assigns the Infection Control Nurse to close it by March, and the Quality Coordinator confirms closure in April.",
    why_nabh_asks="A programme that is never scored against anything just repeats last year's gaps -- scoring it is what turns \"we have a programme\" into \"we know exactly where it is weak.\"",
    how_to_fill=[
        ("Assessment Date", "When the tool was applied."),
        ("Score / Findings", "Result and key gaps identified."),
        ("Corrective Action / Owner / Target Date", "Who fixes what, by when."),
        ("Closure Confirmed By / Date", "Quality Coordinator's sign-off."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.1"), WHO_CORE_IPC_SRC],
    column_headers=["Assessment Date", "Score / Findings", "Corrective Action / Owner / Target Date", "Closure Confirmed By / Date"],
    worked_example_row=["WORKED EXAMPLE — 15-Jan-2026", "78% — BMW segregation training gap in ward housekeeping staff", "Re-training session; Infection Control Nurse / 15-Mar-2026", "Quality Coordinator — 02-Apr-2026"],
), "annual_infection_control_assessment_gap_closure_tracker")

_add("HIC.1", 3, RecordSpec(
    oe_code="HIC.1.c",
    oe_requirement="The organisation has a multidisciplinary infection control committee and an infection control team, which coordinate the implementation of all infection prevention and control activities.",
    record_title="HIC.1 Record 03 — ICC constitution and meeting minutes",
    what_is_this="This record is the proof the committee actually has members from every required department and actually meets -- not a committee that exists as a name on an organisation chart.",
    real_example="The ICC constitution names nine members across medicine, nursing, housekeeping, CSSD, kitchen, laundry and laboratory; the Q2 2026 minutes record a quorate meeting with three action items.",
    why_nabh_asks="Infection control decided by doctors alone misses what housekeeping, the kitchen, the laundry and CSSD each see in their own area every day -- the committee exists so those perspectives are actually in the room.",
    how_to_fill=[
        ("Meeting Date", "When held."),
        ("Members Present / Quorum (Y/N)", "Attendance."),
        ("Decisions / Action Items", "What was decided."),
        ("Owner / Target Date", "Who does what, by when."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.1")],
    column_headers=["Meeting Date", "Members Present / Quorum (Y/N)", "Decisions / Action Items", "Owner / Target Date"],
    worked_example_row=["WORKED EXAMPLE — 18-Apr-2026", "8 of 9 members — Y", "Approve updated hand-hygiene audit tool", "Infection Control Nurse / 01-May-2026"],
), "icc_constitution_meeting_minutes")

_add("HIC.1", 4, RecordSpec(
    oe_code="HIC.1.d",
    oe_requirement="The organisation implements information, education and communication programme for infection prevention and control activities for the community and participates in managing community outbreaks and pandemics.",
    record_title="HIC.1 Record 04 — Community IEC and outbreak-participation log",
    what_is_this="This record is the proof community education sessions actually happened and that any community outbreak or pandemic request from health authorities was actually acted on -- not a plan that was written and never run.",
    real_example="A hand-hygiene awareness session for 40 outpatient visitors is held in March; in June the hospital provides bed-capacity data to the district health office during a dengue outbreak alert.",
    why_nabh_asks="An infection-control programme that stops at the hospital's front door misses that most infections a patient brings in, and most outbreaks a hospital has to respond to, start in the community it serves.",
    how_to_fill=[
        ("Date", "When the activity took place."),
        ("Activity (IEC Session / Outbreak Participation)", "What happened."),
        ("Audience / Authority Involved", "Who was reached or who requested it."),
        ("Outcome / Lessons Learnt", "What came of it."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.1")],
    column_headers=["Date", "Activity (IEC Session / Outbreak Participation)", "Audience / Authority Involved", "Outcome / Lessons Learnt"],
    worked_example_row=["WORKED EXAMPLE — 14-Mar-2026", "Hand-hygiene IEC session", "40 OPD visitors and caregivers", "Positive feedback; repeat planned quarterly"],
), "community_iec_outbreak_participation_log")

_add("HIC.1", 5, RecordSpec(
    oe_code="HIC.1.e",
    oe_requirement="The management makes available resources required for the infection control programme.",
    record_title="HIC.1 Record 05 — Annual resource plan and shortfall-escalation record",
    what_is_this="This record is the proof the resources the infection-control programme needs were actually planned and funded, and that any shortfall was raised in writing rather than quietly absorbed.",
    real_example="The 2026 resource plan requests budget for N95 respirator restocking; the Medical Superintendent approves 90% of the request and a shortfall in hand-hygiene dispensers is escalated in writing.",
    why_nabh_asks="A programme management says it supports but never actually staffs or funds is a programme that will quietly run short of PPE or hand-hygiene supplies exactly when it is needed most.",
    how_to_fill=[
        ("Resource Item", "What is being requested."),
        ("Requested Quantity / Budget", "How much."),
        ("Approved (Y/N, Amount)", "Management's decision."),
        ("Shortfall Escalated (Y/N, Date)", "If not fully approved."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.1")],
    column_headers=["Resource Item", "Requested Quantity / Budget", "Approved (Y/N, Amount)", "Shortfall Escalated (Y/N, Date)"],
    worked_example_row=["WORKED EXAMPLE — N95 respirator restock", "500 units / ₹________", "Y — full amount", "N"],
), "annual_resource_plan_shortfall_escalation_record")

_add("HIC.1", 6, RecordSpec(
    oe_code="HIC.1.f",
    oe_requirement="Isolation/barrier nursing facilities are available.",
    record_title="HIC.1 Record 06 — Isolation facility readiness and staff-training record",
    what_is_this="This record is the proof an isolation or barrier-nursing facility is actually ready to use -- stocked, criteria-defined, staff trained -- not a room with a sign on the door and nothing behind it.",
    real_example="The isolation room checklist confirms PPE stock, signage and a functioning door seal; the nurse assigned to isolation duty that month completed transmission-based-precaution training in January.",
    why_nabh_asks="A patient with an airborne or highly transmissible infection nursed in an open bay puts every other patient and every staff member on that ward at risk -- isolation capacity has to already exist, not be improvised when the patient arrives.",
    how_to_fill=[
        ("Check Date", "When readiness was verified."),
        ("Facility / Bed", "Which room or bay."),
        ("Readiness Checklist (PPE, Signage, Criteria) Confirmed (Y/N)", "Confirmed."),
        ("Staff Trained on Duty (Y/N, Name)", "Who is trained."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.1")],
    column_headers=["Check Date", "Facility / Bed", "Readiness Checklist (PPE, Signage, Criteria) Confirmed (Y/N)", "Staff Trained on Duty (Y/N, Name)"],
    worked_example_row=["WORKED EXAMPLE — 05-Feb-2026", "Isolation Room 1", "Y", "Y — Nurse S. Iyer"],
), "isolation_facility_readiness_staff_training_record")

# ============================================================== HIC.2 ====
HIC2 = SOPSpecV2(
    sop_no="SOP-HIC.2",
    title="Infection Prevention and Control in Clinical Areas",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» prevents infection "
        "transmission in day-to-day clinical care: standard precautions "
        "used on every patient regardless of diagnosis, hand hygiene, "
        "extra precautions when a specific infection is suspected or "
        "confirmed, safe injection and infusion technique, a written "
        "antimicrobial policy, monitoring of how that policy is actually "
        "followed, and a structured antibiotic stewardship programme."
    ),
    purpose_trigger=(
        "A nurse skips hand hygiene between two patients because the ward "
        "is busy, or a doctor prescribes a broad-spectrum antibiotic out "
        "of habit rather than need -- each one small, each one repeated "
        "often enough across a hospital to drive both infection rates and "
        "antibiotic resistance up. This SOP is what makes the safer "
        "default the easy one to follow."
    ),
    purpose_why=(
        "We do this because most healthcare-associated infection does not "
        "come from one dramatic failure -- it comes from ordinary clinical "
        "moments done slightly wrong, over and over, at scale."
    ),
    purpose_text=(
        "To define how «Hospital Name» implements infection prevention "
        "and control in clinical areas through standard precautions, "
        "hand-hygiene guidelines, transmission-based precautions, safe "
        "injection and infusion practices, a documented antimicrobial "
        "usage policy, monitoring of rational antimicrobial use, and an "
        "antibiotic stewardship programme."
    ),
    scope_why=(
        "so every healthcare provider who touches a patient -- not only "
        "the Infection Control Nurse -- knows these precautions apply to "
        "every patient, every time, not only the ones who look infectious."
    ),
    scope_text=(
        "Applies to all clinical areas of «Hospital Name» and to every "
        "healthcare provider who delivers patient care -- doctors, nurses, "
        "technicians -- along with the Infection Control Officer and "
        "Nurse, the pharmacy, and the Infection Control Committee. It "
        "covers the infection-prevention precautions, injection practices "
        "and antimicrobial stewardship used directly in patient care. It "
        "does not cover the overall infection-control programme and "
        "governance, support-service infection control, prevention of "
        "specific device- and procedure-linked infections, or "
        "surveillance methodology -- each of those is set out in its own "
        "separate SOP in this chapter."
    ),
    responsibility_why=(
        "a precaution that depends on remembering to apply it only to "
        "\"infectious-looking\" patients fails exactly when it matters -- "
        "naming every clinical role as responsible, for every patient, is "
        "what makes it a default instead of a judgement call."
    ),
    responsibilities=[
        ("Medical Superintendent", "Accountable that infection-prevention practices and the antimicrobial stewardship programme are implemented."),
        ("Infection Control Officer", "Oversees transmission-based-precaution criteria; drafts and reviews the antimicrobial usage policy; leads the antibiotic stewardship programme."),
        ("Infection Control Nurse", "Monitors standard-precaution and hand-hygiene compliance; audits safe-injection practice; audits antimicrobial-policy compliance."),
        ("Treating Doctors / Clinicians", "Apply standard and transmission-based precautions; prescribe per the antimicrobial usage policy; initiate transmission-based precautions when indicated."),
        ("Nurses", "Apply standard precautions and hand hygiene; implement transmission-based precautions; administer injections and infusions per protocol."),
        ("Pharmacy / Antimicrobial Stewardship Team", "Implements the antimicrobial formulary and restricted-category controls; supports stewardship rounds."),
        ("Infection Control Committee", "Approves the antimicrobial usage policy; reviews stewardship-programme outcomes."),
    ],
    items=[
        PlainItem(
            heading="Apply standard precautions to every patient, every time",
            why=(
                "Waiting to apply precautions only once a patient \"looks\" "
                "infectious misses the many infections that show no "
                "obvious sign at all -- treating every patient the same "
                "way is what actually protects staff and other patients."
            ),
            body=[
                "All healthcare providers at «Hospital Name» adhere to "
                "standard precautions at all times, regardless of the "
                "patient's diagnosis or presumed infection status. "
                "Standard precautions are:",
                "1. Hand hygiene before and after every patient contact.",
                "2. Personal protective equipment (gloves, gown, mask, "
                "eye protection) matched to the exposure that is "
                "anticipated.",
                "3. Safe handling and disposal of sharps.",
                "4. Respiratory hygiene and cough etiquette.",
                "5. Safe handling of patient-care equipment and linen.",
                "6. Environmental cleaning of the care area.",
                "7. Safe waste management, segregated at the point it is "
                "generated.",
                "PPE is kept available at the point of use in every "
                "clinical area, and the correct order for putting it on "
                "and taking it off is displayed where staff can see it.",
            ],
            oe_code="HIC.2.a",
            boundary=[
                "Waste segregation mechanics themselves are owned by HIC.3.d; this step is the standard-precaution requirement to use them correctly at the point of care.",
            ],
        ),
        PlainItem(
            heading="Follow the WHO five-moments hand-hygiene method",
            why=(
                "Hand hygiene done \"when you remember\" misses the "
                "moments that actually carry the highest risk of passing "
                "an organism from one patient to the next -- the five "
                "moments exist because they were tested, not guessed."
            ),
            body=[
                "«Hospital Name» follows the WHO five moments for hand "
                "hygiene: before touching a patient, before a clean or "
                "aseptic task, after any risk of exposure to body fluid, "
                "after touching a patient, and after touching a patient's "
                "surroundings.",
                "Alcohol-based hand rub dispensers are placed at «every "
                "bed, procedure area entry and nursing station». Soap and "
                "running water are available at every hand-wash sink. "
                "Hand-hygiene technique posters are displayed at every "
                "sink and hand-rub station.",
                "Hand-hygiene compliance is monitored through this "
                "hospital's infection-control surveillance process, with "
                "feedback shared «monthly» with each clinical unit.",
            ],
            oe_code="HIC.2.b",
            boundary=[
                "The audit method, compliance-rate calculation and feedback cadence for hand hygiene are owned by HIC.5.b; this step is the protocol itself and the supplies/signage that support it.",
            ],
            technical_sources=[WHO_HAND_HYGIENE_SRC],
        ),
        PlainItem(
            heading="Add extra precautions when a specific infection is suspected or confirmed",
            why=(
                "Standard precautions alone are not enough once a specific "
                "organism and its way of spreading are known -- an "
                "airborne infection needs a different barrier than a "
                "contact one, and getting that wrong spreads it further."
            ),
            body=[
                "In addition to standard precautions, «Hospital Name» "
                "applies transmission-based precautions -- contact, "
                "droplet, or airborne -- whenever the patient's "
                "condition, culture result or epidemiological assessment "
                "indicates it:",
                "1. Contact precautions: gown and gloves for all contact; "
                "dedicated equipment for that patient; a single room or "
                "cohorting with other patients on the same precaution.",
                "2. Droplet precautions: a surgical mask within «1 metre» "
                "of the patient; a single room where possible.",
                "3. Airborne precautions: an N95 respirator; a negative-"
                "pressure room where one is available; the door kept "
                "closed.",
                "Signage is placed at the room or bed showing which "
                "precaution is in use, and written criteria define when "
                "the precaution can be stepped down.",
            ],
            oe_code="HIC.2.c",
            boundary=[
                "The physical isolation facility and its general readiness are owned by HIC.1.f; this step is the clinical decision and technique for each precaution type.",
            ],
        ),
        PlainItem(
            heading="Follow safe injection and infusion practice every time",
            why=(
                "Reusing a needle, recapping by hand, or leaving a multi-"
                "dose vial open past its safe window are small shortcuts "
                "that can pass bloodborne infection from one patient to "
                "another, or infect the staff member taking the "
                "shortcut."
            ),
            body=[
                "«Hospital Name» follows safe injection and infusion "
                "practice at all times:",
                "1. A new, sterile syringe and needle for every "
                "injection, with no exceptions.",
                "2. Needles are never recapped by hand -- a needle "
                "destroyer or safety-engineered device is used instead.",
                "3. Single-dose vials are used whenever possible; where a "
                "multi-dose vial has to be used, it is handled aseptically, "
                "labelled with the date it was opened, and discarded "
                "after «28 days or the manufacturer's instruction, "
                "whichever is shorter».",
                "4. Injections are prepared in a clean, designated area, "
                "away from any contaminated items.",
                "5. Aseptic technique is used for every intravenous "
                "access and infusion preparation.",
                "6. IV administration sets are changed per protocol -- "
                "«every 72-96 hours for continuous infusions; immediately "
                "after blood products or lipids».",
                "Phlebotomy and IV cannulation follow a written aseptic "
                "insertion-and-maintenance bundle.",
            ],
            oe_code="HIC.2.d",
            boundary=[
                "The central-line-specific insertion bundle is owned by HIC.4.c; this step is general safe injection and peripheral-line practice.",
            ],
        ),
        PlainItem(
            heading="Keep a written antimicrobial usage policy, grounded in this hospital's own resistance data",
            why=(
                "Prescribing on habit rather than on what this hospital's "
                "own organisms are actually resistant to drives resistance "
                "up and leaves the next patient with fewer options that "
                "still work."
            ),
            body=[
                "«Hospital Name» has an antimicrobial usage policy that "
                "is established and documented. The policy is based on:",
                "1. The hospital's own local antibiogram data, updated "
                "«annually» from this hospital's own culture and "
                "sensitivity results, or from regional data where this "
                "hospital's own case volume is too low.",
                "2. National treatment guidelines (ICMR / IDSA or "
                "equivalent).",
                "3. A classification of antimicrobials into unrestricted, "
                "restricted and reserve categories.",
                "The policy sets out empirical-therapy recommendations "
                "for common infections, criteria for escalating or de-"
                "escalating therapy, duration guidance, and surgical-"
                "prophylaxis protocols. It is approved by the Infection "
                "Control Committee and made available to every "
                "prescriber.",
            ],
            oe_code="HIC.2.e",
        ),
        PlainItem(
            heading="Check that the antimicrobial policy is actually being followed, not just written",
            why=(
                "A policy that sits in a folder while prescribing "
                "continues unchanged has achieved nothing -- checking "
                "actual prescriptions against it is what tells this "
                "hospital whether the policy is working."
            ),
            body=[
                "The Infection Control Committee and the antimicrobial "
                "stewardship team monitor rational use of antimicrobial "
                "agents at «Hospital Name»:",
                "1. Prescription audits are conducted «monthly» on a "
                "sample of inpatient records.",
                "2. Compliance with the antimicrobial usage policy -- "
                "empirical choice, de-escalation, duration -- is "
                "measured against that sample.",
                "3. Use of restricted-category antimicrobials is tracked "
                "by volume and by indication.",
                "4. Feedback is given to prescribers «quarterly».",
                "5. A trend of non-compliance is escalated to the Medical "
                "Superintendent rather than left to repeat.",
            ],
            oe_code="HIC.2.f",
        ),
        PlainItem(
            heading="Run a structured antibiotic stewardship programme",
            why=(
                "A policy on paper and occasional audits are not the "
                "same as someone actively reviewing real prescriptions in "
                "real time -- stewardship rounds catch the wrong "
                "antibiotic, the wrong dose, or the unnecessarily long "
                "course while it can still be corrected."
            ),
            body=[
                "«Hospital Name» runs an antibiotic stewardship programme "
                "(ASP) to optimise antimicrobial therapy, improve patient "
                "outcomes and reduce antimicrobial resistance. The "
                "programme includes:",
                "1. Prospective audit with intervention and feedback -- "
                "stewardship rounds held «twice a week».",
                "2. Formulary restriction and pre-authorisation for "
                "reserve antimicrobials.",
                "3. An automatic stop order and mandatory review at «72 "
                "hours» for empirical therapy.",
                "4. Education of prescribers on local resistance patterns "
                "and appropriate prescribing.",
                "5. Monitoring of defined-daily-dose / days-of-therapy "
                "trends.",
                "6. An annual review of the programme's impact on "
                "resistance patterns, consumption and clinical outcomes.",
                "The stewardship team includes, at minimum, the Infection "
                "Control Officer, a clinical pharmacist (or a «senior "
                "nurse trained in antibiotic stewardship» where no "
                "pharmacist is available), and a microbiologist or access "
                "to microbiology consultation.",
            ],
            oe_code="HIC.2.g",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-7 (see the HIC.2 Records folder).",
    related_documents=[
        "Hospital's Hospital Infection Prevention and Control Programme SOP (HIC.1)",
        "Hospital's Prevention of Healthcare Associated Infections in Patients and Staff SOP (HIC.4)",
        "Hospital's Infection Prevention and Control Surveillance SOP (HIC.5)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a prescription audit "
        "finds a sustained compliance gap with the antimicrobial usage "
        "policy, or if a related policy named above in this chapter is "
        "revised."
    ),
    full_reference_list=[
        NABH_HIC_CITE.format(code="HIC.2"),
        WHO_HAND_HYGIENE_SRC,
        WHO_CORE_IPC_SRC,
    ],
)

SOPS.append(("SOP_HIC.2.a_to_g_infection_prevention_control_clinical_areas.docx", HIC2))

# ---- HIC.2 Records -------------------------------------------------
_add("HIC.2", 1, RecordSpec(
    oe_code="HIC.2.a",
    oe_requirement="The organisation adheres to standard precautions at all times.",
    record_title="HIC.2 Record 01 — Standard-precaution PPE availability and compliance observation record",
    what_is_this="This record is the proof PPE was actually available at the point of care and staff were actually observed following standard precautions -- not a protocol that exists only on paper.",
    real_example="A spot check in the medical ward finds gloves, gowns and masks stocked at the nursing station, and direct observation of three staff members shows correct PPE use before a dressing change.",
    why_nabh_asks="Waiting to apply precautions only once a patient \"looks\" infectious misses the many infections that show no obvious sign at all -- treating every patient the same way is what actually protects staff and other patients.",
    how_to_fill=[
        ("Date / Area", "When and where checked."),
        ("PPE Stock Confirmed (Y/N)", "Availability at point of use."),
        ("Staff Observed / Compliant (Y/N)", "Direct observation result."),
        ("Corrective Action (if non-compliant)", "What was done."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.2"), WHO_CORE_IPC_SRC],
    column_headers=["Date / Area", "PPE Stock Confirmed (Y/N)", "Staff Observed / Compliant (Y/N)", "Corrective Action (if non-compliant)"],
    worked_example_row=["WORKED EXAMPLE — 10-Feb-2026 / Medical Ward", "Y", "Y — 3 of 3 observed compliant", "N/A"],
), "standard_precaution_ppe_availability_compliance_observation_record")

_add("HIC.2", 2, RecordSpec(
    oe_code="HIC.2.b",
    oe_requirement="The organisation adheres to hand-hygiene guidelines.",
    record_title="HIC.2 Record 02 — Hand-hygiene supply and signage verification record",
    what_is_this="This record is the proof hand-rub and soap were actually available where they are needed and the five-moments poster was actually displayed -- the physical conditions the hand-hygiene protocol depends on.",
    real_example="The February round confirms ABHR dispensers are filled at every bed in the surgical ward and the five-moments poster is displayed at each station.",
    why_nabh_asks="Hand hygiene done \"when you remember\" misses the moments that actually carry the highest risk of passing an organism from one patient to the next -- the five moments exist because they were tested, not guessed.",
    how_to_fill=[
        ("Date / Unit", "When and where checked."),
        ("ABHR / Soap Available (Y/N)", "Confirmed."),
        ("Five-Moments Poster Displayed (Y/N)", "Confirmed."),
        ("Issue Found / Action", "Any gap and what was done."),
    ],
    verified_sources=[WHO_HAND_HYGIENE_SRC, NABH_HIC_CITE.format(code="HIC.2")],
    column_headers=["Date / Unit", "ABHR / Soap Available (Y/N)", "Five-Moments Poster Displayed (Y/N)", "Issue Found / Action"],
    worked_example_row=["WORKED EXAMPLE — 10-Feb-2026 / Surgical Ward", "Y", "Y", "None"],
), "hand_hygiene_supply_signage_verification_record")

_add("HIC.2", 3, RecordSpec(
    oe_code="HIC.2.c",
    oe_requirement="The organisation adheres to transmission-based precautions.",
    record_title="HIC.2 Record 03 — Transmission-based-precaution assignment and de-escalation record",
    what_is_this="This record is the proof a patient placed on contact, droplet or airborne precautions actually had the right signage and PPE applied, and that de-escalation was a documented decision, not a drift back to normal practice.",
    real_example="A patient with suspected pulmonary TB is placed on airborne precautions with N95 signage at the door; de-escalation to standard precautions follows two negative sputum results, documented by the treating doctor.",
    why_nabh_asks="Standard precautions alone are not enough once a specific organism and its way of spreading are known -- an airborne infection needs a different barrier than a contact one, and getting that wrong spreads it further.",
    how_to_fill=[
        ("Patient / Bed", "Who and where."),
        ("Precaution Type (Contact/Droplet/Airborne)", "Which one."),
        ("Signage / PPE Confirmed (Y/N)", "Applied correctly."),
        ("De-escalation Date / Criteria Met", "When and why stepped down."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.2")],
    column_headers=["Patient / Bed", "Precaution Type (Contact/Droplet/Airborne)", "Signage / PPE Confirmed (Y/N)", "De-escalation Date / Criteria Met"],
    worked_example_row=["WORKED EXAMPLE — Patient UID-00458 / Bed 12", "Airborne", "Y", "22-Feb-2026 — two negative sputum smears"],
), "transmission_based_precaution_assignment_de_escalation_record")

_add("HIC.2", 4, RecordSpec(
    oe_code="HIC.2.d",
    oe_requirement="The organisation adheres to safe injection and infusion practices.",
    record_title="HIC.2 Record 04 — Safe injection and infusion practice audit",
    what_is_this="This record is the proof safe-injection practice was actually observed in the clinical area -- single-use syringes, no manual recapping, correctly labelled multi-dose vials -- not assumed because a protocol exists.",
    real_example="An audit of the injection room finds one multi-dose vial unlabelled with its opening date, corrected on the spot, with no other deviations found.",
    why_nabh_asks="Reusing a needle, recapping by hand, or leaving a multi-dose vial open past its safe window are small shortcuts that can pass bloodborne infection from one patient to another, or infect the staff member taking the shortcut.",
    how_to_fill=[
        ("Audit Date / Area", "When and where."),
        ("Items Checked", "Syringe reuse, recapping, vial labelling, IV set change."),
        ("Deviations Found", "What was wrong, if anything."),
        ("Corrective Action", "What was done."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.2")],
    column_headers=["Audit Date / Area", "Items Checked", "Deviations Found", "Corrective Action"],
    worked_example_row=["WORKED EXAMPLE — 05-Mar-2026 / Injection Room", "Syringe reuse, recapping, vial labelling", "One multi-dose vial unlabelled", "Labelled on the spot; staff reminded at handover"],
), "safe_injection_infusion_practice_audit")

_add("HIC.2", 5, RecordSpec(
    oe_code="HIC.2.e",
    oe_requirement="Appropriate antimicrobial usage policy is established and documented.",
    record_title="HIC.2 Record 05 — Antimicrobial usage policy and local antibiogram record",
    what_is_this="This record is the proof the antimicrobial usage policy actually exists in writing, is actually based on this hospital's own antibiogram, and was actually approved -- not a generic document copied from elsewhere.",
    real_example="The 2026 antibiogram shows rising E. coli resistance to ciprofloxacin, which the ICC uses to revise the empirical therapy recommendation for urinary tract infection in the policy approved that quarter.",
    why_nabh_asks="Prescribing on habit rather than on what this hospital's own organisms are actually resistant to drives resistance up and leaves the next patient with fewer options that still work.",
    how_to_fill=[
        ("Policy Version / Date", "Which version."),
        ("Antibiogram Reference Date", "Which year's data it is based on."),
        ("Key Changes This Revision", "What changed and why."),
        ("ICC Approval Date", "When approved."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.2")],
    column_headers=["Policy Version / Date", "Antibiogram Reference Date", "Key Changes This Revision", "ICC Approval Date"],
    worked_example_row=["WORKED EXAMPLE — v2.1 / Apr-2026", "2026 antibiogram", "UTI empirical therapy revised off ciprofloxacin", "15-Apr-2026"],
), "antimicrobial_usage_policy_local_antibiogram_record")

_add("HIC.2", 6, RecordSpec(
    oe_code="HIC.2.f",
    oe_requirement="The organisation implements the antimicrobial usage policy and monitors the rational use of antimicrobial agents.",
    record_title="HIC.2 Record 06 — Monthly antimicrobial-prescription audit report",
    what_is_this="This record is the proof real prescriptions were actually checked against the antimicrobial policy every month, with feedback actually given to prescribers -- not a policy left to enforce itself.",
    real_example="The March audit of 20 inpatient charts finds 85% compliance with empirical-therapy recommendations, with feedback shared at the department meeting.",
    why_nabh_asks="A policy that sits in a folder while prescribing continues unchanged has achieved nothing -- checking actual prescriptions against it is what tells this hospital whether the policy is working.",
    how_to_fill=[
        ("Month", "Which month."),
        ("Sample Size", "Charts reviewed."),
        ("Compliance Rate", "Percentage compliant."),
        ("Feedback Given (Y/N, Date)", "To prescribers."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.2")],
    column_headers=["Month", "Sample Size", "Compliance Rate", "Feedback Given (Y/N, Date)"],
    worked_example_row=["WORKED EXAMPLE — March 2026", "20 charts", "85%", "Y — 10-Apr-2026 department meeting"],
), "monthly_antimicrobial_prescription_audit_report")

_add("HIC.2", 7, RecordSpec(
    oe_code="HIC.2.g",
    oe_requirement="The organisation implements an antibiotic stewardship programme.",
    record_title="HIC.2 Record 07 — Antibiotic stewardship round and annual outcome report",
    what_is_this="This record is the proof stewardship rounds actually happened twice a week with real interventions, and that the programme's yearly impact was actually measured -- not a charter that was written and shelved.",
    real_example="A stewardship round flags an unnecessarily prolonged course of a reserve antimicrobial, intervenes to stop it at day 5 instead of day 10, and the annual report shows a 12% drop in reserve-antimicrobial days of therapy.",
    why_nabh_asks="A policy on paper and occasional audits are not the same as someone actively reviewing real prescriptions in real time -- stewardship rounds catch the wrong antibiotic, the wrong dose, or the unnecessarily long course while it can still be corrected.",
    how_to_fill=[
        ("Round Date", "When held."),
        ("Cases Reviewed / Interventions Made", "What was found and changed."),
        ("Acceptance Rate", "Prescriber acceptance of intervention."),
        ("Annual DDD/DOT Trend (at year-end)", "Outcome measure."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.2")],
    column_headers=["Round Date", "Cases Reviewed / Interventions Made", "Acceptance Rate", "Annual DDD/DOT Trend (at year-end)"],
    worked_example_row=["WORKED EXAMPLE — 12-Mar-2026", "6 cases reviewed; 1 course shortened", "100% — intervention accepted", "12% reduction in reserve-antimicrobial DOT (year-end)"],
), "antibiotic_stewardship_round_annual_outcome_report")

# ============================================================== HIC.3 ====
HIC3 = SOPSpecV2(
    sop_no="SOP-HIC.3",
    title="Infection Prevention and Control in Support Services",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» controls infection risk in "
        "the support services that keep the hospital running: building "
        "engineering controls like ventilation and water quality, "
        "infection-control planning before any construction or "
        "renovation, housekeeping, biomedical-waste handling, laundry and "
        "linen, and kitchen sanitation and food handling."
    ),
    purpose_trigger=(
        "A renovation starts next to a ward with no dust barrier, or a "
        "sharps box is left overflowing in a corridor -- neither looks "
        "like a clinical failure, but both can put an infection straight "
        "into a patient who never went near the construction site or the "
        "waste bin. This SOP is what makes support-service areas as "
        "accountable for infection control as the wards are."
    ),
    purpose_why=(
        "We do this because infection does not only travel through "
        "clinical contact -- contaminated water, dust from a renovation, "
        "poorly handled waste, improperly washed linen, or food held at "
        "the wrong temperature can each put a patient at risk just as "
        "directly."
    ),
    purpose_text=(
        "To define how «Hospital Name» implements infection prevention "
        "and control in support services: engineering controls, infection "
        "risk during construction and renovation, housekeeping, "
        "biomedical-waste management, laundry and linen management, and "
        "kitchen sanitation and food handling."
    ),
    scope_why=(
        "so every support department -- maintenance, housekeeping, "
        "laundry, kitchen, the biomedical-waste handler -- knows its own "
        "work is part of infection control, not separate from it."
    ),
    scope_text=(
        "Applies to all support-service areas of «Hospital Name»: "
        "maintenance and engineering, housekeeping, biomedical-waste "
        "handling, laundry, kitchen and dietetics, along with the "
        "Infection Control Officer and Nurse who oversee them. It covers "
        "the infection-control requirements for how each of these "
        "services is run. It does not cover the facilities-engineering "
        "infrastructure itself, clinical precautions used in direct "
        "patient care, or prevention of specific device- and procedure-"
        "linked infections -- each of those is set out in its own "
        "separate SOP in this chapter or in the facilities-management "
        "chapter."
    ),
    responsibility_why=(
        "support-service infection control that depends on \"someone will "
        "notice\" rather than a named owner for ventilation, waste, "
        "linen and food is exactly how a contamination risk goes "
        "unnoticed until a patient is affected."
    ),
    responsibilities=[
        ("Infection Control Officer", "Specifies engineering-control requirements; completes the infection-control risk assessment before construction/renovation; approves the biomedical-waste and laundry protocols."),
        ("Maintenance / Facilities Team", "Implements and maintains engineering controls; complies with infection-control risk-assessment precautions during projects."),
        ("Housekeeping In-Charge", "Implements the area-wise cleaning schedule; maintains colour-coded equipment allocation."),
        ("Biomedical-Waste Handler / Coordinator", "Manages day-to-day segregation, storage and handover of biomedical waste; all staff segregate waste at the point it is generated."),
        ("Laundry In-Charge", "Runs the laundry and linen process per the thermal/chemical disinfection protocol."),
        ("Kitchen / Dietetics In-Charge", "Implements kitchen sanitation and food-handling practice."),
        ("Medical Superintendent", "Approves infection-control risk assessments before construction begins; oversees medical-fitness clearance for food handlers."),
    ],
    items=[
        PlainItem(
            heading="Maintain engineering controls that prevent infection",
            why=(
                "Air that does not change often enough in an operating "
                "theatre, or water that is never tested, can carry "
                "infection to a patient with nobody in the room doing "
                "anything wrong at all -- the building itself has to be "
                "part of infection control."
            ),
            body=[
                "«Hospital Name» maintains appropriate engineering "
                "controls, including:",
                "1. Adequate ventilation and air changes in clinical "
                "areas, following national or ASHRAE/ISHRAE guidance -- "
                "«minimum 6 air changes per hour in general wards, 12 in "
                "the operating theatre, negative pressure in isolation "
                "rooms».",
                "2. HEPA filtration where required (operating theatre, "
                "isolation areas).",
                "3. Potable water quality monitoring and storage-tank "
                "cleaning «quarterly».",
                "4. Sewage treatment and effluent management, so the "
                "hospital does not contaminate its own surroundings.",
                "The Infection Control Officer and the maintenance team "
                "conduct a joint round «monthly» to verify these controls "
                "are actually functioning. Any deficiency found is "
                "reported for correction and tracked through to closure.",
            ],
            oe_code="HIC.3.a",
        ),
        PlainItem(
            heading="Assess and control infection risk before any construction or renovation",
            why=(
                "Dust and vibration from a renovation can carry fungal "
                "spores straight into a ward's air supply -- the risk has "
                "to be assessed and controlled before the first wall "
                "comes down, not noticed afterward."
            ),
            body=[
                "Before any construction or renovation in or next to a "
                "patient-care area, the Infection Control Officer "
                "completes an infection-control risk assessment (ICRA). "
                "The ICRA classifies the project type and the patient-"
                "risk group of the area affected, to decide what "
                "precautions are required:",
                "1. Dust barriers, negative pressure in the construction "
                "zone, sealed windows.",
                "2. A separate traffic route for construction workers and "
                "debris, away from clinical areas.",
                "3. Air monitoring during and after the project.",
                "4. Terminal cleaning of the area before it is returned "
                "to clinical use.",
                "The ICRA and its mitigation plan are approved by the "
                "«Medical Superintendent» before work begins. Compliance "
                "is monitored by the Infection Control Nurse for as long "
                "as the project runs.",
            ],
            oe_code="HIC.3.b",
        ),
        PlainItem(
            heading="Follow housekeeping procedures that actually prevent cross-contamination",
            why=(
                "A mop used in an isolation room and then carried "
                "straight into the next ward carries the infection with "
                "it -- the colour-coding and separate schedules exist "
                "because \"clean enough\" cleaning still spreads germs."
            ),
            body=[
                "«Hospital Name» follows housekeeping procedures that "
                "prevent cross-contamination between areas:",
                "1. A cleaning schedule defines the frequency for every "
                "area, with high-risk areas cleaned «three times a day "
                "plus terminal cleaning after every discharge».",
                "2. Colour-coded cleaning equipment -- mops, buckets, "
                "cloths -- stops equipment moving between areas and "
                "spreading contamination.",
                "3. Disinfectant choice and dilution follow the list the "
                "Infection Control Committee has approved.",
                "4. A spill-management protocol: contain, disinfect, "
                "clean, dispose.",
                "5. Terminal cleaning follows every discharge from "
                "isolation or barrier nursing.",
                "6. Housekeeping staff are trained in infection-control "
                "cleaning methods at induction and «annually».",
                "How effective this actually is gets checked separately, "
                "as part of this hospital's infection-control "
                "surveillance.",
            ],
            oe_code="HIC.3.c",
            boundary=[
                "How housekeeping effectiveness is objectively monitored (visual audits, ATP/microbiological testing) is owned by HIC.5.e; this step is the procedure itself.",
            ],
        ),
        PlainItem(
            heading="Handle biomedical waste safely, from the point it is generated to final disposal",
            why=(
                "Mixing a used needle in with ordinary waste, or letting "
                "waste sit unsegregated past its safe storage window, "
                "turns an everyday bin into a sharps or infection hazard "
                "for the next person who handles it -- often someone with "
                "no idea what is inside."
            ),
            body=[
                "Biomedical waste at «Hospital Name» is segregated at "
                "the point it is generated into colour-coded categories, "
                "following the Bio-Medical Waste Management Rules, 2016:",
                "1. Yellow: human anatomical waste, soiled waste, "
                "expired medicines, and chemical (cytotoxic) waste.",
                "2. Red: contaminated recyclable waste -- tubing, "
                "syringes without needles, gloves.",
                "3. White, puncture-proof: sharps -- needles, blades, "
                "glass.",
                "4. Blue: glassware waste, where applicable.",
                "Waste is stored in a designated, secured intermediate "
                "storage area for no longer than «48 hours». Collection, "
                "transport, treatment and disposal are carried out by the "
                "«authorised common biomedical waste treatment facility» "
                "under a valid agreement. Daily segregation logs, "
                "transport manifests, monthly returns and the annual "
                "report to the State Pollution Control Board are all "
                "kept on record.",
            ],
            oe_code="HIC.3.d",
            technical_sources=[CPCB_BMW_SRC],
        ),
        PlainItem(
            heading="Manage laundry and linen so washing itself does not spread infection",
            why=(
                "Soiled linen carried through a clean corridor, or "
                "washed without reaching a disinfecting temperature, can "
                "move an infection from one patient's bed to the next "
                "patient who gets that linen."
            ),
            body=[
                "«Hospital Name» follows laundry and linen management "
                "that prevents infection transmission:",
                "1. Soiled linen is collected in leak-proof bags or "
                "containers at the point it is used; colour coding keeps "
                "infectious linen separate from routine soiled linen.",
                "2. Transport to the laundry uses covered trolleys on a "
                "defined route that avoids clean areas.",
                "3. Washing uses thermal disinfection -- «65°C for 10 "
                "minutes or 71°C for 3 minutes» -- or chemical "
                "disinfection for heat-sensitive items.",
                "4. Clean linen is stored in a covered, designated area, "
                "kept separate from soiled holding.",
                "5. A linen inventory and replacement schedule keep any "
                "visibly damaged or stained linen out of circulation.",
                "The laundry area's layout follows a one-way dirty-to-"
                "clean flow, and staff handling infectious linen wear "
                "PPE -- heavy-duty gloves, gown, mask.",
            ],
            oe_code="HIC.3.e",
        ),
        PlainItem(
            heading="Keep kitchen sanitation and food handling safe enough to prevent foodborne infection",
            why=(
                "A patient already fighting illness is far more "
                "vulnerable to foodborne infection than a healthy person "
                "would be -- the kitchen is feeding people with the least "
                "margin for error."
            ),
            body=[
                "«Hospital Name» follows kitchen sanitation and food-"
                "handling practice that prevents foodborne infection:",
                "1. Kitchen staff undergo medical-fitness screening -- "
                "stool culture and skin examination -- before "
                "employment and «annually» after.",
                "2. Personal hygiene: hand washing before handling food, "
                "hair covering, a clean uniform, and no jewellery in "
                "food-preparation areas.",
                "3. Food storage keeps the cold chain intact -- «below "
                "5°C for perishables» -- with dry stores kept above "
                "floor level and rotated first-in-first-out.",
                "4. Cooking brings the core temperature of food to "
                "«74°C».",
                "5. Food is served within «2 hours» of cooking, or kept "
                "hot at or above 63°C; therapeutic diets are labelled "
                "and dispatched per the dietitian's order.",
                "6. Kitchen surfaces and equipment are sanitised «after "
                "every meal service»; pest control is carried out "
                "«monthly».",
                "7. Water used in the kitchen is tested for potability "
                "«quarterly».",
            ],
            oe_code="HIC.3.f",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the HIC.3 Records folder).",
    related_documents=[
        "Hospital's Hospital Infection Prevention and Control Programme SOP (HIC.1)",
        "Hospital's Infection Prevention and Control Surveillance SOP (HIC.5)",
        "Hospital's facilities-management engineering-controls SOP (FMS)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a biomedical-waste "
        "segregation breach, a construction-related infection-control "
        "deviation, or a food-safety non-conformance is identified, or if "
        "a related policy named above in this chapter is revised."
    ),
    full_reference_list=[
        NABH_HIC_CITE.format(code="HIC.3"),
        CPCB_BMW_SRC,
    ],
)

SOPS.append(("SOP_HIC.3.a_to_f_infection_prevention_control_support_services.docx", HIC3))

# ---- HIC.3 Records -------------------------------------------------
_add("HIC.3", 1, RecordSpec(
    oe_code="HIC.3.a",
    oe_requirement="The organisation has appropriate engineering controls to prevent infections.",
    record_title="HIC.3 Record 01 — Engineering-control joint verification round",
    what_is_this="This record is the proof ventilation, water quality and effluent controls were actually checked together by infection control and maintenance every month -- not assumed to be working because nobody complained.",
    real_example="The February joint round confirms air-change rates in the OT meet the 12-per-hour target and flags a water-tank cleaning that is two weeks overdue, closed out by the first week of March.",
    why_nabh_asks="Air that does not change often enough in an operating theatre, or water that is never tested, can carry infection to a patient with nobody in the room doing anything wrong at all -- the building itself has to be part of infection control.",
    how_to_fill=[
        ("Round Date", "When held."),
        ("Area / Control Checked", "Ventilation, water quality, effluent, etc."),
        ("Finding", "Within spec or deficient."),
        ("Closure Date / Action", "If deficient, what was done and when."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.3")],
    column_headers=["Round Date", "Area / Control Checked", "Finding", "Closure Date / Action"],
    worked_example_row=["WORKED EXAMPLE — 10-Feb-2026", "OT air changes / water tank cleaning", "Air changes within spec; tank cleaning overdue", "Tank cleaned 05-Mar-2026"],
), "engineering_control_joint_verification_round")

_add("HIC.3", 2, RecordSpec(
    oe_code="HIC.3.b",
    oe_requirement="The organisation designs and implements a plan to reduce the risk of infection during construction and renovation.",
    record_title="HIC.3 Record 02 — Infection-control risk assessment (ICRA) for construction/renovation",
    what_is_this="This record is the proof an ICRA was actually completed and approved before a construction project began, and that compliance was actually monitored during the work -- not a project that started on the contractor's schedule alone.",
    real_example="The ICRA for a ward bathroom renovation classifies it as medium risk, requires dust barriers and a dedicated debris route, approved by the Medical Superintendent before demolition starts.",
    why_nabh_asks="Dust and vibration from a renovation can carry fungal spores straight into a ward's air supply -- the risk has to be assessed and controlled before the first wall comes down, not noticed afterward.",
    how_to_fill=[
        ("Project / Area", "What is being built or renovated."),
        ("Risk Classification", "Low/medium/high per the ICRA."),
        ("Precautions Required", "Dust barriers, traffic route, air monitoring, etc."),
        ("MS Approval Date", "Before work begins."),
        ("Terminal Cleaning Confirmed (Y/N)", "Before return to clinical use."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.3")],
    column_headers=["Project / Area", "Risk Classification", "Precautions Required", "MS Approval Date", "Terminal Cleaning Confirmed (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — Ward bathroom renovation", "Medium", "Dust barrier, dedicated debris route", "02-Feb-2026", "Y — 20-Feb-2026"],
), "icra_construction_renovation")

_add("HIC.3", 3, RecordSpec(
    oe_code="HIC.3.c",
    oe_requirement="The organisation adheres to housekeeping procedures.",
    record_title="HIC.3 Record 03 — Area-wise cleaning schedule and spill/terminal-cleaning log",
    what_is_this="This record is the proof each area was actually cleaned on schedule, with colour-coded equipment, and that spills and post-isolation terminal cleans actually happened -- not a schedule that exists only as a wall chart.",
    real_example="The ICU cleaning log shows the scheduled three-times-daily clean completed each shift in March, plus one documented spill response and one terminal clean after an isolation discharge.",
    why_nabh_asks="A mop used in an isolation room and then carried straight into the next ward carries the infection with it -- the colour-coding and separate schedules exist because \"clean enough\" cleaning still spreads germs.",
    how_to_fill=[
        ("Date / Area", "When and where."),
        ("Scheduled Clean Completed (Y/N)", "Confirmed."),
        ("Spill or Terminal Clean (if any)", "What triggered it."),
        ("Colour-Coded Equipment Used (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.3")],
    column_headers=["Date / Area", "Scheduled Clean Completed (Y/N)", "Spill or Terminal Clean (if any)", "Colour-Coded Equipment Used (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 14-Mar-2026 / ICU", "Y", "Terminal clean after isolation discharge, Bed 4", "Y"],
), "area_wise_cleaning_schedule_spill_terminal_cleaning_log")

_add("HIC.3", 4, RecordSpec(
    oe_code="HIC.3.d",
    oe_requirement="Biomedical waste (BMW) is handled appropriately and safely.",
    record_title="HIC.3 Record 04 — Daily biomedical-waste segregation log and CBWTF handover",
    what_is_this="This record is the proof biomedical waste was actually segregated into the right colour categories every day, and actually handed over to the authorised treatment facility within the storage window -- not waste that sat unaccounted for.",
    real_example="The daily log shows 4.2 kg of yellow-category waste and 1.1 kg of sharps collected and handed to the CBWTF collection vehicle within the 48-hour storage limit, with a signed manifest.",
    why_nabh_asks="Mixing a used needle in with ordinary waste, or letting waste sit unsegregated past its safe storage window, turns an everyday bin into a sharps or infection hazard for the next person who handles it -- often someone with no idea what is inside.",
    how_to_fill=[
        ("Date", "Day of collection."),
        ("Category / Weight (Yellow/Red/White/Blue)", "Segregated amounts."),
        ("Storage Duration (Hours)", "Within 48-hour limit."),
        ("CBWTF Handover / Manifest No.", "Collection confirmation."),
    ],
    verified_sources=[CPCB_BMW_SRC, NABH_HIC_CITE.format(code="HIC.3")],
    column_headers=["Date", "Category / Weight (Yellow/Red/White/Blue)", "Storage Duration (Hours)", "CBWTF Handover / Manifest No."],
    worked_example_row=["WORKED EXAMPLE — 14-Mar-2026", "Yellow 4.2 kg; White (sharps) 1.1 kg", "22 hours", "Manifest #CB-2026-0314"],
), "daily_biomedical_waste_segregation_log_cbwtf_handover")

_add("HIC.3", 5, RecordSpec(
    oe_code="HIC.3.e",
    oe_requirement="The organisation adheres to laundry and linen management processes.",
    record_title="HIC.3 Record 05 — Laundry wash-cycle temperature log",
    what_is_this="This record is the proof linen was actually washed at a temperature that disinfects it -- not just washed clean-looking without the disinfection step actually happening.",
    real_example="The March wash-cycle log shows every load reaching 65°C for at least 10 minutes, with one load using chemical disinfection for a heat-sensitive item logged separately.",
    why_nabh_asks="Soiled linen carried through a clean corridor, or washed without reaching a disinfecting temperature, can move an infection from one patient's bed to the next patient who gets that linen.",
    how_to_fill=[
        ("Date / Load No.", "When and which load."),
        ("Method (Thermal/Chemical)", "Which disinfection method."),
        ("Temperature / Duration Achieved", "Actual reading."),
        ("Within Spec (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.3")],
    column_headers=["Date / Load No.", "Method (Thermal/Chemical)", "Temperature / Duration Achieved", "Within Spec (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 14-Mar-2026 / Load 3", "Thermal", "65°C for 12 minutes", "Y"],
), "laundry_wash_cycle_temperature_log")

_add("HIC.3", 6, RecordSpec(
    oe_code="HIC.3.f",
    oe_requirement="The organisation adheres to kitchen sanitation and food-handling issues.",
    record_title="HIC.3 Record 06 — Food-handler medical clearance and daily temperature log",
    what_is_this="This record is the proof kitchen staff were actually medically cleared to handle food, and that storage/cooking/serving temperatures were actually checked every day -- not a kitchen running on assumption.",
    real_example="The annual medical clearance for the head cook is current; the daily log shows cooked food reaching 76°C core temperature and perishables stored at 4°C.",
    why_nabh_asks="A patient already fighting illness is far more vulnerable to foodborne infection than a healthy person would be -- the kitchen is feeding people with the least margin for error.",
    how_to_fill=[
        ("Date", "Day of record."),
        ("Food-Handler Medical Clearance Current (Y/N)", "Confirmed."),
        ("Storage / Cooking Temperature Readings", "Actual values."),
        ("Within Spec (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.3")],
    column_headers=["Date", "Food-Handler Medical Clearance Current (Y/N)", "Storage / Cooking Temperature Readings", "Within Spec (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 14-Mar-2026", "Y", "Storage 4°C; cooked food core 76°C", "Y"],
), "food_handler_medical_clearance_daily_temperature_log")

# ============================================================== HIC.4 ====
HIC4 = SOPSpecV2(
    sop_no="SOP-HIC.4",
    title="Prevention of Healthcare Associated Infections in Patients and Staff",
    purpose_plain=(
        "This SOP sets out the specific, evidence-based bundles «Hospital "
        "Name» uses to prevent four of the most common device- and "
        "procedure-linked infections -- catheter-associated urinary tract "
        "infection, ventilator-associated pneumonia, catheter-linked "
        "blood stream infection, and surgical site infection -- plus how "
        "the hospital protects its own staff from occupational infection "
        "risk and provides post-exposure prophylaxis after a significant "
        "exposure."
    ),
    purpose_trigger=(
        "A urinary catheter stays in three days longer than it needed to "
        "because nobody asked whether it was still needed, and the "
        "patient develops a urinary tract infection that was entirely "
        "preventable. This SOP is what makes asking \"does this device "
        "still need to be in?\" a daily habit, not an afterthought."
    ),
    purpose_why=(
        "We do this because each of these infections has a well-studied "
        "bundle of simple steps that measurably reduces its risk -- the "
        "evidence already exists; what is left is actually doing the "
        "bundle every time, for every patient, on every shift."
    ),
    purpose_text=(
        "To define the actions «Hospital Name» takes to prevent catheter-"
        "associated urinary tract infection (CAUTI), infection-related "
        "ventilator-associated complication / ventilator-associated "
        "pneumonia (IVAC/VAP), catheter-linked blood stream infection "
        "(CLABSI) and surgical site infection (SSI) in patients, and to "
        "implement occupational health and safety practices and post-"
        "exposure prophylaxis to reduce infection risk to staff."
    ),
    scope_why=(
        "so every clinician who inserts a device or performs surgery, and "
        "every staff member at risk of occupational exposure, knows "
        "exactly which bundle applies to them and that reporting an "
        "exposure immediately is expected, not something to downplay."
    ),
    scope_text=(
        "Applies to all staff at «Hospital Name» who insert, maintain or "
        "remove invasive devices, who perform surgical procedures, or who "
        "are at risk of occupational exposure to blood or body fluid: "
        "treating doctors, surgeons, nurses, the Infection Control Officer "
        "and Nurse, and the pharmacy. It covers the specific prevention "
        "bundles for CAUTI, VAP, CLABSI and SSI, and the occupational-"
        "health response to a significant exposure. It does not cover "
        "general clinical infection-prevention precautions, support-"
        "service infection control, or surveillance methodology -- each "
        "of those is set out in its own separate SOP in this chapter. "
        "Where «Hospital Name» does not provide a service referred to in "
        "a bundle below (such as mechanical ventilation or central-line "
        "insertion), that is recorded as an absence against this "
        "hospital's own service directory, not treated as a gap."
    ),
    responsibility_why=(
        "a prevention bundle that nobody is named to actually perform, "
        "every time, quietly becomes a bundle that is only partly "
        "followed -- and a partial bundle protects nobody."
    ),
    responsibilities=[
        ("Treating Doctors", "Decide and document catheter/line indications; lead CLABSI and SSI insertion bundles; initiate antibiotic prophylaxis timing."),
        ("Nurses / ICU Staff", "Perform daily device-necessity reassessment; maintain CAUTI, VAP and CLABSI maintenance bundles; apply post-operative wound care."),
        ("Surgeons", "Lead the pre-/intra-/post-operative SSI-prevention bundle."),
        ("Infection Control Nurse", "Monitors CAUTI/VAP/CLABSI/SSI rates and gives unit-level feedback."),
        ("Infection Control Officer", "Runs the occupational-health-and-safety programme; assesses and initiates post-exposure prophylaxis, or delegates to the duty medical officer."),
        ("Medical Superintendent", "Ensures resources for occupational health and safety; approves work-restriction decisions for staff with a transmissible infection."),
        ("Pharmacy", "Stocks post-exposure-prophylaxis medicines, available 24 hours a day, 7 days a week."),
    ],
    items=[
        PlainItem(
            heading="Prevent catheter-associated urinary tract infection (CAUTI)",
            why=(
                "A urinary catheter left in a day longer than it needs to "
                "be is the single biggest reason CAUTI happens at all -- "
                "the infection is preventable mainly by taking the "
                "catheter out on time, not by anything exotic."
            ),
            body=[
                "«Hospital Name» prevents CAUTI through an insertion-and-"
                "maintenance bundle:",
                "1. Insert a urinary catheter only for an accepted "
                "indication, documented in the clinical record.",
                "2. Use aseptic technique for insertion: hand hygiene, "
                "sterile gloves, a sterile drape, antiseptic peri-"
                "urethral cleaning, and a sterile closed drainage system.",
                "3. Secure the catheter to prevent movement and "
                "urethral trauma.",
                "4. Maintain a closed drainage system; do not "
                "disconnect it unless clinically necessary.",
                "5. Reassess the continued need for the catheter every "
                "day, and remove it as soon as the indication no longer "
                "applies.",
                "6. Document the insertion date, the indication, and "
                "every daily reassessment in the patient record.",
                "The Infection Control Nurse monitors CAUTI rates "
                "through this hospital's surveillance process and gives "
                "unit-level feedback «monthly».",
            ],
            oe_code="HIC.4.a",
            technical_sources=[CDC_CAUTI_SRC],
        ),
        PlainItem(
            heading="Prevent ventilator-associated pneumonia and related complications",
            why=(
                "A patient on a ventilator cannot clear their own airway "
                "the way they normally would -- the bundle exists to do, "
                "deliberately, the protective things the patient's own "
                "body cannot do for itself right now."
            ),
            body=[
                "Where mechanical ventilation is provided, «Hospital "
                "Name» prevents ventilator-associated pneumonia (VAP) "
                "and infection-related ventilator-associated "
                "complication (IVAC) through:",
                "1. Head-of-bed elevation to «30-45 degrees», unless "
                "medically contraindicated.",
                "2. A daily sedation vacation and assessment of "
                "readiness to extubate.",
                "3. Oral care with «chlorhexidine 0.12%» per protocol.",
                "4. Peptic-ulcer prophylaxis where clinically indicated.",
                "5. Deep-vein-thrombosis prophylaxis where clinically "
                "indicated.",
                "6. Subglottic secretion drainage, where that equipment "
                "is available.",
                "7. Hand hygiene before and after any contact with the "
                "ventilator circuit.",
                "Where «Hospital Name» does not provide mechanical "
                "ventilation, this bundle is a recorded absence against "
                "the service directory -- it is not copied into this "
                "SOP as if the service existed.",
            ],
            oe_code="HIC.4.b",
        ),
        PlainItem(
            heading="Prevent catheter-linked blood stream infection (CLABSI)",
            why=(
                "A central line gives bacteria a direct route into the "
                "bloodstream -- every extra day it stays in without being "
                "needed, and every time it is accessed without a clean "
                "hub, is another chance for that route to be used."
            ),
            body=[
                "Where central lines are inserted, «Hospital Name» "
                "prevents CLABSI through a central-line insertion-and-"
                "maintenance bundle:",
                "1. Hand hygiene and maximal sterile barrier precautions "
                "for insertion.",
                "2. Chlorhexidine-based skin antisepsis at the insertion "
                "site.",
                "3. Careful site selection -- the subclavian site is "
                "preferred where clinically appropriate, and the "
                "femoral site is avoided where possible.",
                "4. A daily review of whether the line is still "
                "necessary, with removal as soon as it is not.",
                "5. Standardised dressing changes using aseptic "
                "technique.",
                "6. A hub or port scrub before every access.",
                "Where «Hospital Name» does not insert central lines, "
                "this is a recorded absence against the service "
                "directory. Peripheral IV lines follow this hospital's "
                "general aseptic insertion-and-maintenance bundle used "
                "for safe injection and infusion practice.",
            ],
            oe_code="HIC.4.c",
            boundary=[
                "General peripheral-IV and injection safe-practice is owned by HIC.2.d; this step is specific to central-line insertion and maintenance.",
            ],
            technical_sources=[CDC_CLABSI_SRC],
        ),
        PlainItem(
            heading="Prevent surgical site infection (SSI)",
            why=(
                "SSI prevention is not one decision made in the "
                "operating theatre -- it is a chain of small decisions "
                "before, during and after surgery, and the chain only "
                "holds if every link is actually done."
            ),
            body=[
                "«Hospital Name» prevents SSI through measures taken "
                "before, during and after surgery.",
                "Pre-operative: antibiotic prophylaxis is given within "
                "«60 minutes» before incision, following this hospital's "
                "antimicrobial usage policy; the surgical site is "
                "prepared with «chlorhexidine-alcohol or povidone-"
                "iodine»; the patient bathes or showers before surgery "
                "where feasible; and routine hair removal is avoided, "
                "using clippers rather than razors if it is required.",
                "Intra-operative: normothermia is maintained (core "
                "temperature at or above 36°C); glycaemic control is "
                "maintained in diabetic patients; sterile technique is "
                "used throughout, with instrument sterility following "
                "this hospital's sterilisation procedure.",
                "Post-operative: wound dressings are changed using "
                "aseptic, non-touch technique with hand hygiene; "
                "surveillance for SSI continues for «30 days» after "
                "surgery, or «90 days» for implant surgery; and SSI "
                "rates are reported to the Infection Control Committee.",
            ],
            oe_code="HIC.4.d",
            boundary=[
                "Instrument sterilisation itself is owned by HIC.6; this step is the surgical bundle that depends on instruments already being sterile.",
            ],
            technical_sources=[WHO_SSI_SRC],
        ),
        PlainItem(
            heading="Protect staff from infection risk in their own work",
            why=(
                "A staff member exposed to a patient's blood or body "
                "fluid is not a bystander in infection control -- they "
                "are themselves at risk, and protecting them is as much "
                "this hospital's job as protecting patients."
            ),
            body=[
                "«Hospital Name» implements occupational health and "
                "safety practices to reduce the risk of transmitting "
                "microorganisms among healthcare providers:",
                "1. Standard precautions and PPE use, as in this "
                "hospital's clinical infection-control protocol.",
                "2. Staff immunisation: hepatitis B vaccination with "
                "titre confirmation, annual influenza vaccination where "
                "available, and any outbreak-specific vaccination.",
                "3. Sharps safety: needle-free systems where feasible, "
                "safety-engineered devices, and no manual recapping.",
                "4. Fit-testing for N95 respirators for staff who work "
                "in airborne-precaution areas.",
                "5. A staff member with a transmissible infection -- "
                "active tuberculosis, chickenpox, measles, "
                "conjunctivitis -- is restricted from patient contact "
                "under written guidance.",
                "A sharps injury or a significant mucocutaneous exposure "
                "triggers the stop-work authority described below.",
            ],
            oe_code="HIC.4.e",
        ),
        PlainItem(
            heading="Provide post-exposure prophylaxis to every staff member who needs it",
            why=(
                "The window for post-exposure prophylaxis to actually "
                "work is measured in hours, not days -- a staff member "
                "who hesitates to report an exposure, or a hospital that "
                "cannot provide PEP immediately, can lose that window "
                "entirely."
            ),
            body=[
                "«Hospital Name» provides appropriate post-exposure "
                "prophylaxis (PEP) to every staff member after a "
                "significant exposure -- a needlestick, a sharps injury, "
                "or a splash to a mucous membrane or non-intact skin "
                "from a source patient's blood or body fluid:",
                "1. Immediate first aid: wash the wound with soap and "
                "water, without squeezing it; flush an exposed mucous "
                "membrane with water.",
                "2. Report the incident to the «Infection Control "
                "Officer or the duty medical officer» within «1 hour».",
                "3. A risk assessment covers the source patient's status "
                "(HIV, hepatitis B, hepatitis C), the nature of the "
                "exposure, and the staff member's own vaccination "
                "status.",
                "4. PEP is started within «2 hours» for HIV (and no "
                "later than 72 hours); hepatitis B immunoglobulin or a "
                "booster dose is given where indicated.",
                "5. Counselling, a baseline blood draw, and follow-up "
                "testing at «6 weeks, 3 months and 6 months».",
                "6. Everything is documented confidentially in the "
                "staff member's own occupational-health record.",
                "PEP medicines are kept available «24 hours a day, 7 "
                "days a week», stocked in the «emergency pharmacy or the "
                "emergency department».",
            ],
            oe_code="HIC.4.f",
            technical_sources=[CDC_PEP_SRC],
        ),
        PlainItem(
            heading="Stop work immediately after a needlestick, sharps injury or significant exposure",
            why=(
                "Finishing the task first and reporting an exposure "
                "later throws away exactly the hours in which first aid "
                "and PEP actually work -- the task can wait; the exposure "
                "cannot."
            ),
            body=[
                "Any staff member who sustains a needlestick injury, a "
                "sharps injury, or a significant splash exposure to "
                "blood or body fluid must stop the task immediately.",
                "Work does not resume until: first aid has been "
                "completed (washing with soap and water; flushing an "
                "exposed mucous membrane); the incident has been "
                "reported to the «Infection Control Officer or duty "
                "medical officer»; and PEP assessment has begun.",
                "The exposed staff member's patient-care responsibility "
                "is handed over to another qualified person for the "
                "duration of first aid and reporting. No disciplinary "
                "action follows from invoking this stop-work authority "
                "for a genuine exposure.",
                "The Infection Control Officer may also invoke this "
                "stop-work authority on their own initiative if a "
                "pattern of sharps injuries in one unit points to an "
                "unsafe device or procedure that needs investigating "
                "before it is used again.",
            ],
            oe_code="HIC.4.e / HIC.4.f (stop-work authority)",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-7 (see the HIC.4 Records folder).",
    related_documents=[
        "Hospital's Infection Prevention and Control in Clinical Areas SOP (HIC.2)",
        "Hospital's Sterilisation and Disinfection SOP (HIC.6)",
        "Hospital's Infection Prevention and Control Surveillance SOP (HIC.5)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a CAUTI, VAP, CLABSI "
        "or SSI rate exceeds this hospital's own benchmark for two "
        "consecutive quarters, if a PEP timeline is found to have been "
        "missed, or if a related policy named above in this chapter is "
        "revised."
    ),
    full_reference_list=[
        NABH_HIC_CITE.format(code="HIC.4"),
        CDC_CAUTI_SRC,
        CDC_CLABSI_SRC,
        WHO_SSI_SRC,
        CDC_PEP_SRC,
    ],
)

SOPS.append(("SOP_HIC.4.a_to_f_prevention_healthcare_associated_infections_patients_staff.docx", HIC4))

# ---- HIC.4 Records -------------------------------------------------
_add("HIC.4", 1, RecordSpec(
    oe_code="HIC.4.a",
    oe_requirement="The organisation takes action to prevent catheter-associated urinary tract infections.",
    record_title="HIC.4 Record 01 — CAUTI bundle insertion checklist and daily reassessment record",
    what_is_this="This record is the proof a urinary catheter was actually inserted for a real indication, with aseptic technique, and actually reassessed every day for continued need -- not a catheter left in by default.",
    real_example="A catheter inserted for acute urinary retention is documented with indication, aseptic insertion steps checked off, and removed on day 3 once retention resolves, confirmed by daily reassessment entries.",
    why_nabh_asks="A urinary catheter left in a day longer than it needs to be is the single biggest reason CAUTI happens at all -- the infection is preventable mainly by taking the catheter out on time, not by anything exotic.",
    how_to_fill=[
        ("Patient / Insertion Date", "Who and when."),
        ("Indication", "Documented reason."),
        ("Aseptic Insertion Confirmed (Y/N)", "Technique followed."),
        ("Daily Reassessment (Date, Still Needed Y/N)", "Each day's check."),
        ("Removal Date", "When taken out."),
    ],
    verified_sources=[CDC_CAUTI_SRC, NABH_HIC_CITE.format(code="HIC.4")],
    column_headers=["Patient / Insertion Date", "Indication", "Aseptic Insertion Confirmed (Y/N)", "Daily Reassessment (Date, Still Needed Y/N)", "Removal Date"],
    worked_example_row=["WORKED EXAMPLE — UID-00512 / 10-Mar-2026", "Acute urinary retention", "Y", "11-Mar Y; 12-Mar N", "12-Mar-2026"],
), "cauti_bundle_insertion_checklist_daily_reassessment_record")

_add("HIC.4", 2, RecordSpec(
    oe_code="HIC.4.b",
    oe_requirement="The organisation takes action to prevent infection-related ventilator associated complication/ventilator-associated pneumonia.",
    record_title="HIC.4 Record 02 — VAP-prevention bundle compliance checklist",
    what_is_this="This record is the proof each element of the VAP-prevention bundle -- head elevation, oral care, sedation vacation -- was actually done on a ventilated patient each day, or, where this hospital does not ventilate patients, that this is a recorded absence rather than a copied form.",
    real_example="A ventilated ICU patient's daily checklist confirms 30-degree head elevation, chlorhexidine oral care twice daily, and a sedation vacation trial, all signed by the ICU nurse.",
    why_nabh_asks="A patient on a ventilator cannot clear their own airway the way they normally would -- the bundle exists to do, deliberately, the protective things the patient's own body cannot do for itself right now.",
    how_to_fill=[
        ("Patient / Date", "Who and when."),
        ("Head Elevation 30-45° (Y/N)", "Confirmed."),
        ("Oral Care Given (Y/N)", "Confirmed."),
        ("Sedation Vacation Attempted (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.4")],
    column_headers=["Patient / Date", "Head Elevation 30-45° (Y/N)", "Oral Care Given (Y/N)", "Sedation Vacation Attempted (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — UID-00519 / 12-Mar-2026", "Y", "Y — twice", "Y"],
), "vap_prevention_bundle_compliance_checklist")

_add("HIC.4", 3, RecordSpec(
    oe_code="HIC.4.c",
    oe_requirement="The organisation takes action to prevent catheter linked blood stream infections.",
    record_title="HIC.4 Record 03 — CLABSI bundle insertion checklist and line-necessity review",
    what_is_this="This record is the proof a central line was actually inserted with maximal barrier precautions and actually reviewed every day for continued need -- or, where no central lines are inserted, a recorded absence.",
    real_example="A central line inserted for a patient needing long-term IV access is documented with maximal sterile barrier precautions, subclavian site, and daily necessity review confirming it is still required on day 4.",
    why_nabh_asks="A central line gives bacteria a direct route into the bloodstream -- every extra day it stays in without being needed, and every time it is accessed without a clean hub, is another chance for that route to be used.",
    how_to_fill=[
        ("Patient / Insertion Date", "Who and when."),
        ("Site / Maximal Barrier Precautions (Y/N)", "Confirmed."),
        ("Daily Necessity Review (Date, Still Needed Y/N)", "Each day's check."),
        ("Removal Date", "When taken out."),
    ],
    verified_sources=[CDC_CLABSI_SRC, NABH_HIC_CITE.format(code="HIC.4")],
    column_headers=["Patient / Insertion Date", "Site / Maximal Barrier Precautions (Y/N)", "Daily Necessity Review (Date, Still Needed Y/N)", "Removal Date"],
    worked_example_row=["WORKED EXAMPLE — UID-00527 / 08-Mar-2026", "Subclavian / Y", "09-Mar Y; 10-Mar Y; 11-Mar N", "11-Mar-2026"],
), "clabsi_bundle_insertion_checklist_line_necessity_review")

_add("HIC.4", 4, RecordSpec(
    oe_code="HIC.4.d",
    oe_requirement="The organisation takes action to prevent surgical site infections.",
    record_title="HIC.4 Record 04 — SSI-prevention bundle checklist and 30/90-day surveillance record",
    what_is_this="This record is the proof prophylactic antibiotics, skin preparation and post-operative surveillance actually happened for a surgical patient -- not assumed because the surgery itself went well.",
    real_example="A hernia-repair patient's checklist confirms prophylactic antibiotic given 45 minutes before incision and chlorhexidine-alcohol skin prep; 30-day follow-up finds no SSI.",
    why_nabh_asks="SSI prevention is not one decision made in the operating theatre -- it is a chain of small decisions before, during and after surgery, and the chain only holds if every link is actually done.",
    how_to_fill=[
        ("Patient / Procedure / Date", "Who, what, when."),
        ("Antibiotic Timing (Within 60 min, Y/N)", "Confirmed."),
        ("Skin Prep Used", "Chlorhexidine-alcohol or povidone-iodine."),
        ("Surveillance Follow-up (30/90 Days, SSI Y/N)", "Outcome."),
    ],
    verified_sources=[WHO_SSI_SRC, NABH_HIC_CITE.format(code="HIC.4")],
    column_headers=["Patient / Procedure / Date", "Antibiotic Timing (Within 60 min, Y/N)", "Skin Prep Used", "Surveillance Follow-up (30/90 Days, SSI Y/N)"],
    worked_example_row=["WORKED EXAMPLE — UID-00533 / Hernia repair / 05-Mar-2026", "Y — 45 min before incision", "Chlorhexidine-alcohol", "30-day follow-up — N (no SSI)"],
), "ssi_prevention_bundle_checklist_surveillance_record")

_add("HIC.4", 5, RecordSpec(
    oe_code="HIC.4.e",
    oe_requirement="The organisation implements occupational health and safety practices to reduce the risk of transmitting microorganisms among health care providers.",
    record_title="HIC.4 Record 05 — Staff immunisation and sharps-injury register",
    what_is_this="This record is the proof staff immunisation status and sharps injuries are actually tracked -- not a programme that exists in policy only.",
    real_example="The register shows 38 of 40 clinical staff with confirmed hepatitis B titres, and one sharps injury in February linked to manual recapping, leading to a ward-wide reminder.",
    why_nabh_asks="A staff member exposed to a patient's blood or body fluid is not a bystander in infection control -- they are themselves at risk, and protecting them is as much this hospital's job as protecting patients.",
    how_to_fill=[
        ("Staff Name / Role", "Who."),
        ("Immunisation Status (HepB Titre, Influenza)", "Confirmed."),
        ("Sharps Injury (Date, if any)", "If applicable."),
        ("Corrective Action (if injury)", "What was done."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.4")],
    column_headers=["Staff Name / Role", "Immunisation Status (HepB Titre, Influenza)", "Sharps Injury (Date, if any)", "Corrective Action (if injury)"],
    worked_example_row=["WORKED EXAMPLE — Nurse P. Shah", "HepB titre confirmed; influenza — Y", "12-Feb-2026 — manual recapping", "Ward reminder on safety-engineered devices"],
), "staff_immunisation_sharps_injury_register")

_add("HIC.4", 6, RecordSpec(
    oe_code="HIC.4.f",
    oe_requirement="Appropriate post-exposure prophylaxis is provided to all staff members concerned.",
    record_title="HIC.4 Record 06 — Exposure incident and post-exposure-prophylaxis record",
    what_is_this="This record is the proof a reported exposure actually got a risk assessment and PEP within the right timeline, with follow-up testing actually scheduled -- not an incident report that was filed and forgotten.",
    real_example="A needlestick exposure reported within 20 minutes gets a risk assessment, HIV PEP started within 90 minutes, and follow-up blood draws scheduled at 6 weeks, 3 months and 6 months.",
    why_nabh_asks="The window for post-exposure prophylaxis to actually work is measured in hours, not days -- a staff member who hesitates to report an exposure, or a hospital that cannot provide PEP immediately, can lose that window entirely.",
    how_to_fill=[
        ("Date/Time of Exposure", "When it happened."),
        ("Time Reported", "Within 1 hour target."),
        ("Risk Assessment / PEP Initiated (Time)", "What was decided and when started."),
        ("Follow-up Testing Dates (6wk/3mo/6mo)", "Scheduled."),
    ],
    verified_sources=[CDC_PEP_SRC, NABH_HIC_CITE.format(code="HIC.4")],
    column_headers=["Date/Time of Exposure", "Time Reported", "Risk Assessment / PEP Initiated (Time)", "Follow-up Testing Dates (6wk/3mo/6mo)"],
    worked_example_row=["WORKED EXAMPLE — 18-Mar-2026, 2:10 PM", "2:30 PM", "HIV PEP started 3:40 PM", "29-Apr; 18-Jun; 18-Sep 2026"],
), "exposure_incident_post_exposure_prophylaxis_record")

_add("HIC.4", 7, RecordSpec(
    oe_code="HIC.4.e / HIC.4.f (stop-work authority)",
    oe_requirement="Any staff member who sustains a needlestick, sharps injury or significant splash exposure stops the task immediately; work resumes only after first aid, reporting and the start of PEP assessment.",
    record_title="HIC.4 Record 07 — Exposure stop-work log",
    what_is_this="This record is the proof a sharps or splash exposure actually stopped the task on the spot, with care handed over, rather than the exposed staff member finishing the task first and reporting later.",
    real_example="A nurse drawing blood sustains a needlestick, stops immediately, hands the remaining draw to a colleague, and reports within 15 minutes.",
    why_nabh_asks="Finishing the task first and reporting an exposure later throws away exactly the hours in which first aid and PEP actually work -- the task can wait; the exposure cannot.",
    how_to_fill=[
        ("Date/Time", "When stopped."),
        ("Staff Member / Task", "Who and what they were doing."),
        ("Task Handed Over To", "Who continued the task."),
        ("Time to First Aid / Reporting", "How quickly."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.4")],
    column_headers=["Date/Time", "Staff Member / Task", "Task Handed Over To", "Time to First Aid / Reporting"],
    worked_example_row=["WORKED EXAMPLE — 18-Mar-2026, 2:10 PM", "Nurse R. Fernandes / blood draw", "Nurse A. Kulkarni", "First aid immediate; reported 2:25 PM"],
), "exposure_stop_work_log")

# ============================================================== HIC.5 ====
HIC5 = SOPSpecV2(
    sop_no="SOP-HIC.5",
    title="Infection Prevention and Control Surveillance",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» runs infection-control "
        "surveillance: tracking and analysing infection rates and "
        "trends, monitoring hand-hygiene compliance, catching multi-drug-"
        "resistant organisms and highly virulent infections early, "
        "identifying and controlling outbreaks, checking that "
        "housekeeping is actually effective, and turning all of that "
        "data into corrective action and feedback to the people who can "
        "act on it."
    ),
    purpose_trigger=(
        "A CAUTI rate quietly climbs for three months because nobody was "
        "tracking it against the previous quarter -- by the time anyone "
        "notices, the pattern has already repeated dozens of times. This "
        "SOP is what makes sure the data is actually looked at often "
        "enough to catch a rising trend while it is still small."
    ),
    purpose_why=(
        "We do this because infection prevention without surveillance is "
        "guesswork -- without rates, trends and a way to catch an "
        "outbreak early, this hospital would have no way of knowing "
        "whether any of its prevention bundles are actually working."
    ),
    purpose_text=(
        "To define how «Hospital Name» performs infection prevention and "
        "control surveillance: tracking and analysing infection risks, "
        "rates and trends; monitoring hand-hygiene compliance; capturing "
        "multi-drug-resistant organisms and highly virulent infections; "
        "identifying and controlling outbreaks; monitoring housekeeping "
        "effectiveness; and analysing data for corrective and preventive "
        "action, with feedback to the healthcare team."
    ),
    scope_why=(
        "so the Infection Control Team, every unit lead who receives "
        "feedback, and the laboratory that flags resistant organisms all "
        "know surveillance is a shared, ongoing activity, not a once-a-"
        "year report."
    ),
    scope_text=(
        "Applies to the Infection Control Team, the Infection Control "
        "Committee, the Quality Coordinator and all clinical and support "
        "staff who generate surveillance data at «Hospital Name», "
        "including the microbiology laboratory and unit leads who receive "
        "feedback. It covers how surveillance data is tracked, analysed "
        "and acted on. It does not cover the clinical prevention bundles "
        "themselves, the overall infection-control programme and "
        "governance, or support-service infection control -- each of "
        "those is set out in its own separate SOP in this chapter. This "
        "surveillance data feeds this hospital's quality-indicator "
        "framework, but the indicator framework itself is owned "
        "elsewhere."
    ),
    responsibility_why=(
        "surveillance that nobody is named to actually calculate, review "
        "and feed back becomes a folder of raw numbers nobody ever reads "
        "as a trend."
    ),
    responsibilities=[
        ("Infection Control Team", "Collects and calculates infection rates; compiles MDRO line-lists; analyses surveillance data monthly."),
        ("Infection Control Officer", "Investigates and controls outbreaks; reviews MDRO notifications; escalates highly virulent-infection alerts."),
        ("Infection Control Nurse", "Conducts hand-hygiene observation audits; monitors housekeeping effectiveness objectively."),
        ("Microbiology Laboratory", "Flags multi-drug-resistant organisms and notifies the Infection Control Officer the same day."),
        ("Infection Control Committee", "Reviews trends quarterly; oversees outbreak response."),
        ("Quality Coordinator", "Tracks CAPA arising from surveillance findings to closure."),
        ("Medical Superintendent", "Allocates resources for outbreak response; receives the consolidated quarterly surveillance report."),
    ],
    items=[
        PlainItem(
            heading="Track and analyse infection risks, rates and trends across the hospital",
            why=(
                "A single month's infection count means little on its "
                "own -- it is the trend over several months, compared "
                "against a target, that actually tells this hospital "
                "whether something is getting better or worse."
            ),
            body=[
                "The Infection Control Team maintains surveillance that "
                "tracks and analyses infection risks, rates and trends "
                "at «Hospital Name»:",
                "1. Numerator data: laboratory-confirmed infections and "
                "clinically diagnosed infections, using standard case "
                "definitions.",
                "2. Denominator data: patient-days, and device-days "
                "(catheter-days, ventilator-days, line-days) where "
                "applicable.",
                "3. Rates calculated: CAUTI, CLABSI, SSI, VAP where "
                "applicable, and the overall healthcare-associated-"
                "infection rate per 1,000 patient-days.",
                "4. Trends analysed «monthly» and presented to the "
                "Infection Control Committee «quarterly».",
                "5. High-risk areas -- the operating theatre, ICU, "
                "labour room -- receive targeted surveillance rather "
                "than the same general-ward level of attention.",
                "Data sources include microbiology laboratory reports, "
                "clinical records, nursing documentation and discharge "
                "summaries.",
            ],
            oe_code="HIC.5.a",
        ),
        PlainItem(
            heading="Monitor hand-hygiene compliance with a validated observation method",
            why=(
                "Asking staff whether they wash their hands produces an "
                "optimistic answer; actually observing hand-hygiene "
                "moments is what produces a number this hospital can "
                "trust and act on."
            ),
            body=[
                "Surveillance includes monitoring compliance with this "
                "hospital's hand-hygiene guidelines:",
                "1. Direct observation audits, using the WHO hand-"
                "hygiene observation tool or an equivalent, are "
                "conducted «monthly» in each clinical unit.",
                "2. Observers are trained and validated using the WHO "
                "training module before they audit independently.",
                "3. The compliance rate is calculated as hand-hygiene "
                "actions performed divided by opportunities observed, "
                "multiplied by 100.",
                "4. Results are reported by unit, by professional "
                "category and by moment.",
                "5. Feedback is shared with unit leads «within one "
                "week» of the audit.",
                "6. Trends are analysed and benchmarked against this "
                "hospital's own target of «80% or higher».",
                "Alcohol-based hand-rub consumption, measured in litres "
                "per 1,000 patient-days, is tracked alongside direct "
                "observation as a second, supporting indicator.",
            ],
            oe_code="HIC.5.b",
            technical_sources=[WHO_HAND_HYGIENE_SRC],
        ),
        PlainItem(
            heading="Catch multi-drug-resistant organisms and highly virulent infections early",
            why=(
                "A resistant organism that spreads silently for weeks "
                "before anyone notices is far harder to contain than one "
                "flagged and acted on the same day it is identified."
            ),
            body=[
                "Surveillance includes mechanisms to capture multi-drug-"
                "resistant organisms (MDRO) and highly virulent "
                "infections:",
                "1. The microbiology laboratory flags MDRO results -- "
                "MRSA, VRE, ESBL, CRE, multi-drug-resistant "
                "Acinetobacter, and any others on the Infection Control "
                "Committee's own MDRO list -- and communicates them to "
                "the Infection Control Officer «on the same day».",
                "2. Alert organisms and notifiable diseases are reported "
                "to public health authorities as required by law.",
                "3. A line-list of MDRO cases is maintained with patient "
                "demographics, organism, resistance pattern, location "
                "and date.",
                "4. A highly virulent infection -- novel influenza, "
                "viral haemorrhagic fever, a suspected outbreak pathogen "
                "-- triggers immediate notification to the Infection "
                "Control Officer and activation of transmission-based "
                "precautions.",
                "5. Antibiogram data is compiled «annually» and shared "
                "with prescribers, to keep this hospital's antimicrobial "
                "policy grounded in its own actual resistance pattern.",
            ],
            oe_code="HIC.5.c",
        ),
        PlainItem(
            heading="Identify and control outbreaks of infection",
            why=(
                "An outbreak that is caught at two or three cases can be "
                "contained with cohorting and enhanced cleaning -- the "
                "same outbreak caught at twenty cases has already spread "
                "far beyond what those measures can undo."
            ),
            body=[
                "«Hospital Name» identifies and takes appropriate action "
                "to control outbreaks of infection:",
                "1. An outbreak is suspected when the number of "
                "infections of a similar type in a defined area or time "
                "exceeds the baseline -- or when two or more cases of an "
                "unusual organism appear in one unit within «7 days».",
                "2. The Infection Control Officer investigates: "
                "confirming cases, identifying the likely source, "
                "putting control measures in place -- cohorting, "
                "enhanced cleaning, contact tracing -- and communicating "
                "with the Infection Control Committee and hospital "
                "administration.",
                "3. An outbreak log documents the timeline, case count, "
                "source hypothesis, control measures taken and the "
                "eventual outcome.",
                "4. The outbreak is declared over when no new case "
                "occurs for two full incubation periods.",
                "5. A post-outbreak report with lessons learned and "
                "preventive recommendations is submitted to the "
                "Infection Control Committee within «2 weeks» of "
                "closure.",
                "«Hospital Name» also takes part in community outbreak "
                "investigation when requested by district health "
                "authorities, as this hospital's own community-"
                "engagement and pandemic-preparedness work describes.",
            ],
            oe_code="HIC.5.d",
        ),
        PlainItem(
            heading="Check that housekeeping is actually working, not just scheduled",
            why=(
                "A cleaning schedule that is followed to the letter can "
                "still leave a surface contaminated if the technique or "
                "the disinfectant is not actually doing the job -- "
                "objective testing is what tells the difference between "
                "\"cleaned\" and \"clean\"."
            ),
            body=[
                "Surveillance activities include monitoring the "
                "effectiveness of housekeeping services:",
                "1. Visual inspection audits of cleanliness are "
                "conducted «daily» by the Housekeeping In-Charge and "
                "«weekly» by the Infection Control Nurse.",
                "2. Objective monitoring -- «ATP bioluminescence testing "
                "or microbiological swab cultures» on high-touch "
                "surfaces -- is carried out «monthly» in high-risk areas "
                "and «quarterly» in general areas.",
                "3. Results are compared against defined benchmarks: "
                "«below 250 RLU for ATP testing; below 5 CFU per cm² for "
                "aerobic colony count».",
                "4. A result outside those benchmarks triggers re-"
                "cleaning, a root-cause analysis if it keeps repeating, "
                "and a corrective and preventive action.",
                "5. Housekeeping-effectiveness trends are reported to "
                "the Infection Control Committee «quarterly».",
            ],
            oe_code="HIC.5.e",
            boundary=[
                "The housekeeping procedure itself (schedules, colour-coding, spill management) is owned by HIC.3.c; this step is checking whether that procedure is actually working.",
            ],
        ),
        PlainItem(
            heading="Turn surveillance data into corrective action and feedback, every time",
            why=(
                "A trend chart that is produced every month and never "
                "acted on is surveillance in name only -- the entire "
                "point of tracking a rate is to do something when it "
                "moves the wrong way."
            ),
            body=[
                "Surveillance data is analysed, and appropriate "
                "corrective and preventive action is taken, with "
                "feedback provided regularly to the healthcare team:",
                "1. The Infection Control Team compiles and analyses "
                "surveillance data «monthly».",
                "2. Analysis includes comparing trends, benchmarking, "
                "and identifying clusters or rising rates.",
                "3. When a rate exceeds its threshold or a trend "
                "worsens, a root-cause analysis is started and a "
                "corrective and preventive action is defined, with a "
                "timeline and a named owner.",
                "4. Feedback is given to unit heads and the healthcare "
                "team «monthly», through unit-specific dashboards or "
                "reports.",
                "5. A consolidated surveillance report is presented to "
                "the Infection Control Committee «quarterly» and to the "
                "Medical Superintendent.",
                "6. The effectiveness of each corrective and preventive "
                "action is checked by watching the same metric in later "
                "periods -- it is only closed once the rate has actually "
                "returned to an acceptable level, not simply because the "
                "action was completed.",
            ],
            oe_code="HIC.5.f",
            boundary=[
                "The hospital's broader quality-indicator framework (dashboards, committee cadence across all indicator domains) is owned by PSQ.2; this step is the surveillance-specific data generation and CAPA cycle that feeds it.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the HIC.5 Records folder).",
    related_documents=[
        "Hospital's Hospital Infection Prevention and Control Programme SOP (HIC.1)",
        "Hospital's Infection Prevention and Control in Clinical Areas SOP (HIC.2)",
        "Hospital's Key Indicators SOP (PSQ.2)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if an outbreak "
        "investigation finds a surveillance gap that delayed detection, "
        "or if a related policy named above in this chapter is revised."
    ),
    full_reference_list=[
        NABH_HIC_CITE.format(code="HIC.5"),
        WHO_HAND_HYGIENE_SRC,
    ],
)

SOPS.append(("SOP_HIC.5.a_to_f_infection_prevention_control_surveillance.docx", HIC5))

# ---- HIC.5 Records -------------------------------------------------
_add("HIC.5", 1, RecordSpec(
    oe_code="HIC.5.a",
    oe_requirement="The scope of surveillance incorporates tracking and analysing of infection risks, rates and trends.",
    record_title="HIC.5 Record 01 — Monthly infection-rate calculation and trend report",
    what_is_this="This record is the proof infection rates were actually calculated every month with real numerator and denominator data, and actually compared over time -- not a single snapshot number with nothing to compare it to.",
    real_example="March's CAUTI rate is calculated at 2.1 per 1,000 catheter-days, compared against February's 2.8, and presented as a declining trend to the ICC in the Q1 review.",
    why_nabh_asks="A single month's infection count means little on its own -- it is the trend over several months, compared against a target, that actually tells this hospital whether something is getting better or worse.",
    how_to_fill=[
        ("Month", "Which month."),
        ("Infection Type / Numerator / Denominator", "Rate calculation basis."),
        ("Rate", "Per 1,000 patient-days or device-days."),
        ("Trend vs Prior Month", "Up/down/stable."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.5")],
    column_headers=["Month", "Infection Type / Numerator / Denominator", "Rate", "Trend vs Prior Month"],
    worked_example_row=["WORKED EXAMPLE — March 2026", "CAUTI / 2 cases / 950 catheter-days", "2.1 per 1,000 catheter-days", "Down from 2.8"],
), "monthly_infection_rate_calculation_trend_report")

_add("HIC.5", 2, RecordSpec(
    oe_code="HIC.5.b",
    oe_requirement="Surveillance includes monitoring compliance with hand-hygiene guidelines.",
    record_title="HIC.5 Record 02 — Hand-hygiene observation audit and feedback record",
    what_is_this="This record is the proof hand-hygiene compliance was actually observed directly, by trained observers, and the result actually fed back to the unit within a week -- not an assumed percentage.",
    real_example="A March audit of the surgical ward observes 60 hand-hygiene opportunities, finds 48 performed correctly (80% compliance), and shares the result with the unit lead within three days.",
    why_nabh_asks="Asking staff whether they wash their hands produces an optimistic answer; actually observing hand-hygiene moments is what produces a number this hospital can trust and act on.",
    how_to_fill=[
        ("Audit Date / Unit", "When and where."),
        ("Opportunities Observed / Actions Performed", "Raw counts."),
        ("Compliance Rate", "Calculated percentage."),
        ("Feedback Given (Date)", "Within one week."),
    ],
    verified_sources=[WHO_HAND_HYGIENE_SRC, NABH_HIC_CITE.format(code="HIC.5")],
    column_headers=["Audit Date / Unit", "Opportunities Observed / Actions Performed", "Compliance Rate", "Feedback Given (Date)"],
    worked_example_row=["WORKED EXAMPLE — 10-Mar-2026 / Surgical Ward", "60 observed / 48 performed", "80%", "13-Mar-2026"],
), "hand_hygiene_observation_audit_feedback_record")

_add("HIC.5", 3, RecordSpec(
    oe_code="HIC.5.c",
    oe_requirement="Surveillance includes mechanisms to capture the occurrence of multi-drug-resistant organisms and highly virulent infections.",
    record_title="HIC.5 Record 03 — MDRO line-list and same-day notification record",
    what_is_this="This record is the proof a resistant organism result was actually flagged by the laboratory and actually reached the Infection Control Officer the same day -- not a result that sat in a report nobody read for a week.",
    real_example="A CRE-positive culture from a ward patient is flagged by the laboratory at 2 PM and reaches the Infection Control Officer by 4 PM the same day, logged on the MDRO line-list with isolation initiated.",
    why_nabh_asks="A resistant organism that spreads silently for weeks before anyone notices is far harder to contain than one flagged and acted on the same day it is identified.",
    how_to_fill=[
        ("Patient / Date", "Who and when."),
        ("Organism / Resistance Pattern", "What was found."),
        ("Location", "Ward or unit."),
        ("Lab Flag Time / ICO Notified Time", "Same-day confirmation."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.5")],
    column_headers=["Patient / Date", "Organism / Resistance Pattern", "Location", "Lab Flag Time / ICO Notified Time"],
    worked_example_row=["WORKED EXAMPLE — UID-00541 / 14-Mar-2026", "CRE (carbapenem-resistant Enterobacteriaceae)", "General Ward, Bed 7", "Flagged 2:00 PM / ICO notified 4:00 PM"],
), "mdro_line_list_same_day_notification_record")

_add("HIC.5", 4, RecordSpec(
    oe_code="HIC.5.d",
    oe_requirement="The organisation identifies and takes appropriate action to control outbreaks of infections.",
    record_title="HIC.5 Record 04 — Outbreak log and post-outbreak report",
    what_is_this="This record is the proof a suspected outbreak was actually investigated, controlled and closed with lessons learned -- not a cluster of cases that was noticed and then left uninvestigated.",
    real_example="Three cases of an unusual organism in the ICU within five days trigger an outbreak investigation; cohorting and enhanced cleaning are implemented, and the outbreak is declared closed after two incubation periods with no new cases.",
    why_nabh_asks="An outbreak that is caught at two or three cases can be contained with cohorting and enhanced cleaning -- the same outbreak caught at twenty cases has already spread far beyond what those measures can undo.",
    how_to_fill=[
        ("Suspected Date / Trigger", "What raised the alarm."),
        ("Case Count / Source Hypothesis", "Investigation findings."),
        ("Control Measures Taken", "What was done."),
        ("Closure Date / Lessons Learnt", "When declared over and what was learned."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.5")],
    column_headers=["Suspected Date / Trigger", "Case Count / Source Hypothesis", "Control Measures Taken", "Closure Date / Lessons Learnt"],
    worked_example_row=["WORKED EXAMPLE — 20-Mar-2026 / 3 cases in 5 days", "3 cases / suspected contaminated equipment", "Cohorting, enhanced cleaning, equipment withdrawn", "05-Apr-2026 — equipment disinfection protocol revised"],
), "outbreak_log_post_outbreak_report")

_add("HIC.5", 5, RecordSpec(
    oe_code="HIC.5.e",
    oe_requirement="Surveillance activities include monitoring the effectiveness of the housekeeping services.",
    record_title="HIC.5 Record 05 — Objective housekeeping-effectiveness monitoring record",
    what_is_this="This record is the proof housekeeping effectiveness was actually tested objectively -- ATP or microbiological swabs against a defined benchmark -- not judged only by whether a surface looks clean.",
    real_example="ATP testing on the ICU nursing station counter reads 180 RLU, within the 250 RLU benchmark; a corridor handrail reads 310 RLU, triggering re-cleaning and a repeat test.",
    why_nabh_asks="A cleaning schedule that is followed to the letter can still leave a surface contaminated if the technique or the disinfectant is not actually doing the job -- objective testing is what tells the difference between \"cleaned\" and \"clean\".",
    how_to_fill=[
        ("Test Date / Area", "When and where."),
        ("Method (ATP/Microbiological)", "Which test."),
        ("Result", "Reading."),
        ("Within Benchmark (Y/N) / Action", "Confirmed and any re-clean."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.5")],
    column_headers=["Test Date / Area", "Method (ATP/Microbiological)", "Result", "Within Benchmark (Y/N) / Action"],
    worked_example_row=["WORKED EXAMPLE — 15-Mar-2026 / Corridor handrail", "ATP", "310 RLU", "N — re-cleaned and re-tested; 2nd reading 140 RLU"],
), "objective_housekeeping_effectiveness_monitoring_record")

_add("HIC.5", 6, RecordSpec(
    oe_code="HIC.5.f",
    oe_requirement="Surveillance data is analysed, and appropriate corrective and preventive actions are taken and feedback regarding the same is provided regularly to the appropriate health care team.",
    record_title="HIC.5 Record 06 — Monthly surveillance analysis, CAPA and feedback register",
    what_is_this="This record is the proof a rate that crossed its threshold actually triggered a root-cause analysis and a tracked corrective action, closed only once the rate itself improved -- not closed just because a meeting discussed it.",
    real_example="A rising SSI rate in the orthopaedic unit triggers an RCA that finds inconsistent antibiotic-prophylaxis timing; a CAPA retrains the team on timing, and the rate is confirmed back within benchmark two months later before the CAPA is closed.",
    why_nabh_asks="A trend chart that is produced every month and never acted on is surveillance in name only -- the entire point of tracking a rate is to do something when it moves the wrong way.",
    how_to_fill=[
        ("Month", "Which month's analysis."),
        ("Finding (Threshold Exceeded / Trend)", "What was identified."),
        ("CAPA / Owner / Target Date", "Action and accountability."),
        ("Closure Confirmed (Rate Improved, Date)", "Verified outcome."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.5")],
    column_headers=["Month", "Finding (Threshold Exceeded / Trend)", "CAPA / Owner / Target Date", "Closure Confirmed (Rate Improved, Date)"],
    worked_example_row=["WORKED EXAMPLE — Feb 2026", "SSI rate rising in orthopaedics", "Retrain on prophylaxis timing; Infection Control Nurse / 15-Mar-2026", "Confirmed improved — 10-May-2026"],
), "monthly_surveillance_analysis_capa_feedback_register")

# ============================================================== HIC.6 ====
HIC6 = SOPSpecV2(
    sop_no="SOP-HIC.6",
    title="Sterilisation and Disinfection of Instruments, Equipment and Devices",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» cleans, packs, sterilises "
        "or disinfects, stores and issues every instrument, piece of "
        "equipment and device used in patient care: the physical space "
        "and zoning the work is done in, the written cycle each item "
        "goes through, how single-use items are reprocessed where that "
        "is approved, how sterilisation itself is validated as working, "
        "and what happens when something in that system breaks down."
    ),
    purpose_trigger=(
        "A failed biological-indicator test is noticed, but the "
        "instruments from that load have already been used on three "
        "patients -- because nobody had a clear recall procedure ready "
        "before the failure happened. This SOP exists so that recall "
        "procedure is already written down, before it is ever needed."
    ),
    purpose_why=(
        "We do this because a single instrument that was not actually "
        "sterile can carry infection into a procedure meant to heal, not "
        "harm -- and the only way to be sure an instrument is sterile is "
        "to validate the process that made it that way, every cycle, not "
        "just trust that the autoclave is working."
    ),
    purpose_text=(
        "To define how «Hospital Name» ensures the sterilisation and/or "
        "disinfection of instruments, equipment and devices used in "
        "patient care: adequate space and zoning, the cleaning-packing-"
        "disinfection/sterilisation-storing-issue cycle, reprocessing of "
        "single-use items under written guidance, regular validation "
        "testing, and the recall procedure used when a sterilisation "
        "breakdown is identified."
    ),
    scope_why=(
        "so every CSSD technician, OT nurse and clinician knows exactly "
        "what to do -- and who has the authority to refuse a suspect "
        "instrument -- the moment something about sterilisation looks "
        "wrong."
    ),
    scope_text=(
        "Applies to the central sterile services department (CSSD) or "
        "designated sterilisation area at «Hospital Name», and to all "
        "staff who handle, sterilise, store or issue instruments, "
        "equipment or devices: the CSSD or Sterilisation In-Charge, CSSD "
        "technicians, the Infection Control Officer and Nurse, and the "
        "Medical Superintendent. It covers sterilisation and reprocessing "
        "themselves. It does not cover instrument procurement and "
        "traceability for implants, or operating-theatre housekeeping -- "
        "each of those is set out in its own separate document."
    ),
    responsibility_why=(
        "a sterilisation system with no one clearly in charge of each "
        "zone, each validation test and each recall decision is a system "
        "where a failure can slip through unnoticed until it reaches a "
        "patient."
    ),
    responsibilities=[
        ("Medical Superintendent", "Provides adequate CSSD space; authorises re-qualification of a steriliser after a recall."),
        ("CSSD / Sterilisation In-Charge", "Maintains zoning and workflow; manages the cleaning-packing-sterilisation-storing-issue cycle; performs validation tests; executes the recall procedure."),
        ("CSSD Technicians", "Carry out cleaning, packing, sterilisation, load recording and issue under the In-Charge's supervision."),
        ("Infection Control Committee", "Approves and annually reviews the list of single-use items approved for reprocessing."),
        ("Infection Control Officer", "Oversees reprocessing decisions; investigates recalls and assesses patient risk."),
        ("Infection Control Nurse", "Audits CSSD practice and reprocessing-cycle compliance."),
    ],
    items=[
        PlainItem(
            heading="Keep CSSD space properly zoned, dirty to clean to sterile, one way only",
            why=(
                "A clean instrument that passes back through a dirty "
                "zone, even briefly, is no longer clean -- the zoning and "
                "one-way flow exist because contamination does not "
                "announce itself; it just happens quietly if the layout "
                "allows it."
            ),
            body=[
                "«Hospital Name» provides adequate space and appropriate "
                "zoning for sterilisation activities in the CSSD or "
                "designated sterilisation area:",
                "1. Three distinct zones: dirty (receiving and "
                "cleaning), clean (packing and sterilisation), and "
                "sterile (storage and issue).",
                "2. A one-way workflow from dirty to clean to sterile -- "
                "never in reverse.",
                "3. Physical barriers or clear demarcation between "
                "zones.",
                "4. Adequate ventilation: «negative pressure in the "
                "dirty zone relative to the clean zone; positive "
                "pressure in the sterile store relative to the "
                "corridor».",
                "5. Pass-through hatches or autoclaves between the "
                "dirty and clean zones, where the layout allows it.",
                "6. A staff change area between the dirty and clean "
                "zones, with PPE requirements defined for each zone.",
                "7. Environmental monitoring: temperature and humidity "
                "in the sterile store kept at «24°C or below, and 70% "
                "relative humidity or below».",
            ],
            oe_code="HIC.6.a",
        ),
        PlainItem(
            heading="Follow the written cycle for cleaning, packing, sterilising, storing and issuing every item",
            why=(
                "Skipping a step in this cycle -- an incomplete clean, a "
                "missing chemical indicator, an expired pack issued "
                "anyway -- can look identical to doing it right, right up "
                "until the moment the instrument is used on a patient."
            ),
            body=[
                "Cleaning, packing, disinfection and/or sterilisation, "
                "storing and issue of every item follows written "
                "guidance at «Hospital Name».",
                "Cleaning: instruments are pre-cleaned or soaked "
                "immediately after use in the clinical area; cleaning in "
                "the dirty zone is manual and/or automated using an "
                "ultrasonic or washer-disinfector; every item is "
                "visually inspected under magnification for residual "
                "soil before it is packed.",
                "Packing: items are wrapped or placed in pouches or "
                "containers suited to the sterilisation method; a "
                "chemical integrator is placed inside each pack and a "
                "process indicator on the outside; each pack is labelled "
                "with its contents, steriliser load number, date of "
                "sterilisation, and expiry date.",
                "Sterilisation: the method is matched to the item -- "
                "steam (autoclave at «134°C for 3.5 minutes or 121°C "
                "for 15 minutes»), dry heat, ethylene oxide, or low-"
                "temperature hydrogen peroxide plasma where available. A "
                "load record is kept for every single cycle: time, "
                "temperature, pressure and operator.",
                "Storing: sterile packs are stored on enclosed, dust-"
                "free shelving in the sterile zone, rotated first-in-"
                "first-out, with a shelf life per packaging type -- "
                "«wrapped packs 30 days; sealed pouches 180 days; "
                "event-related where the facility qualifies for it».",
                "Issue: a pack is issued only against a valid request, "
                "with its integrity and expiry verified before release, "
                "and transported in covered, clean containers to the "
                "point of use.",
            ],
            oe_code="HIC.6.b",
            technical_sources=[WHO_DECON_REPROCESS_SRC],
        ),
        PlainItem(
            heading="Reprocess single-use items only when a written list says it is approved",
            why=(
                "A single-use device was designed and validated to be "
                "used once -- reprocessing one that was never approved "
                "for it, or reprocessing it beyond a safe number of "
                "cycles, risks the item failing or no longer being "
                "sterile when it matters most."
            ),
            body=[
                "Reprocessing of single-use instruments, equipment and "
                "devices at «Hospital Name» follows written guidance:",
                "1. A written list, approved by the Infection Control "
                "Committee, identifies exactly which single-use items "
                "may be reprocessed -- an item not on this list is never "
                "reprocessed.",
                "2. A maximum number of reprocessing cycles is defined "
                "for each approved item.",
                "3. Reprocessing follows the same cleaning-packing-"
                "sterilisation-validation cycle used for reusable items.",
                "4. Functional testing after reprocessing confirms the "
                "item's integrity, sharpness or calibration, as "
                "applicable.",
                "5. Each reprocessed item is labelled with the number of "
                "cycles it has completed, for traceability.",
                "6. The decision to reprocess is reviewed «annually» by "
                "the Infection Control Committee, based on safety "
                "evidence and cost.",
                "Where «Hospital Name» does not reprocess any single-use "
                "device, that is documented as a deliberate policy "
                "decision, and no reprocessing list exists.",
            ],
            oe_code="HIC.6.c",
        ),
        PlainItem(
            heading="Run regular validation tests to prove sterilisation is actually working",
            why=(
                "A steriliser that looks like it is running normally can "
                "still be failing to actually sterilise -- physical, "
                "chemical and biological indicators each catch a "
                "different kind of failure the others would miss."
            ),
            body=[
                "Regular validation tests for sterilisation are carried "
                "out and documented at «Hospital Name»:",
                "1. Physical monitoring: every single cycle -- time, "
                "temperature and pressure, read from the steriliser's "
                "own gauges or printout.",
                "2. Chemical indicators: every pack -- a Class 5 or 6 "
                "integrator inside, a Class 1 process indicator outside.",
                "3. Biological indicators: «weekly» for steam "
                "sterilisers, every load for implant items, and per "
                "manufacturer guidance for ethylene-oxide or plasma "
                "sterilisers.",
                "4. A Bowie-Dick test: daily, on the first cycle, for "
                "pre-vacuum steam sterilisers.",
                "5. Records are kept in the sterilisation validation log "
                "and retained for «3 years».",
                "A failed biological indicator or a failed Bowie-Dick "
                "test triggers both the recall procedure below and the "
                "stop-work authority described below. Items from the "
                "affected load are not used until the investigation "
                "confirms they are safe, or the load is re-sterilised.",
            ],
            oe_code="HIC.6.d",
            technical_sources=[CDC_DISINFECTION_STERILIZATION_SRC],
        ),
        PlainItem(
            heading="Run the recall procedure the moment a sterilisation breakdown is identified",
            why=(
                "The time between a sterilisation failure being "
                "discovered and items from that load being used on a "
                "patient is exactly the window the recall procedure "
                "exists to close -- the procedure has to already be "
                "written down, not improvised after the failure is "
                "found."
            ),
            body=[
                "The established recall procedure is implemented "
                "whenever a breakdown in the sterilisation system is "
                "identified:",
                "1. Trigger: a positive biological indicator, a failed "
                "Bowie-Dick test, a steriliser malfunction alarm, or the "
                "discovery of a compromised pack after it has already "
                "been issued.",
                "2. Immediate action: every item from the suspect load "
                "is quarantined and not used.",
                "3. Notification: the CSSD or Sterilisation In-Charge "
                "notifies the Infection Control Officer, the operating "
                "theatre or clinical area that received the items, and "
                "the Medical Superintendent.",
                "4. Trace-back: every item from the affected load is "
                "identified using the load number and distribution "
                "records.",
                "5. Retrieval: items already distributed but not yet "
                "used are retrieved and quarantined.",
                "6. For items already used on a patient: the Infection "
                "Control Officer assesses the patient's risk, starts "
                "surveillance for infection, and documents the "
                "assessment.",
                "7. Investigation: the root cause of the steriliser "
                "failure is identified, and corrective action is put in "
                "place before the steriliser returns to service.",
                "8. Re-qualification: the steriliser must pass «three "
                "consecutive empty-chamber biological-indicator tests» "
                "before patient loads resume.",
                "9. Documentation: a recall log records the timeline, "
                "affected items, patient-impact assessment, corrective "
                "action and re-qualification results.",
            ],
            oe_code="HIC.6.e",
        ),
        PlainItem(
            heading="Stop using any instrument from a failed or unapproved load",
            why=(
                "Using an instrument \"just this once\" while the recall "
                "investigation is still under way defeats the entire "
                "purpose of running the investigation in the first "
                "place -- the stop has to hold until the load is cleared, "
                "not until it is convenient."
            ),
            body=[
                "No instrument, equipment or device is used from a load "
                "whose biological indicator has returned positive, "
                "whose Bowie-Dick test has failed, or whose steriliser "
                "alarmed mid-cycle.",
                "No single-use device is reprocessed if it is not on "
                "the written approved-for-reprocessing list, or if it "
                "has already exceeded its maximum number of reprocessing "
                "cycles.",
                "When either situation is identified: all items from "
                "the affected load (or the non-approved device) are "
                "quarantined; the CSSD or Sterilisation In-Charge and "
                "the Infection Control Officer are notified immediately; "
                "and no item is released for patient use until the "
                "recall procedure is complete and the steriliser is re-"
                "qualified.",
                "No disciplinary action follows from invoking this stop-"
                "work authority for a genuine sterilisation concern. Any "
                "staff member -- a CSSD technician, an OT nurse, or a "
                "clinician -- has the authority to refuse a suspect "
                "instrument.",
            ],
            oe_code="HIC.6.c / HIC.6.d (stop-work authority)",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-5 (see the HIC.6 Records folder).",
    related_documents=[
        "Hospital's Prevention of Healthcare Associated Infections in Patients and Staff SOP (HIC.4)",
        "Hospital's Infection Prevention and Control in Support Services SOP (HIC.3)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a recall procedure "
        "is activated, if a validation test is found to have been "
        "missed, or if a related policy named above in this chapter is "
        "revised."
    ),
    full_reference_list=[
        NABH_HIC_CITE.format(code="HIC.6"),
        WHO_DECON_REPROCESS_SRC,
        CDC_DISINFECTION_STERILIZATION_SRC,
    ],
)

SOPS.append(("SOP_HIC.6.a_to_e_sterilisation_disinfection_instruments_equipment_devices.docx", HIC6))

# ---- HIC.6 Records -------------------------------------------------
_add("HIC.6", 1, RecordSpec(
    oe_code="HIC.6.a",
    oe_requirement="The organisation provides adequate space and appropriate zoning for sterilisation activities.",
    record_title="HIC.6 Record 01 — CSSD zoning and environmental-monitoring record",
    what_is_this="This record is the proof the three CSSD zones actually exist with the right pressure differentials and the sterile store's temperature and humidity were actually monitored -- not a layout that looks right but was never checked.",
    real_example="The February environmental check confirms the sterile store at 22°C and 65% relative humidity, within the defined limits, with zone pressure readings also within spec.",
    why_nabh_asks="A clean instrument that passes back through a dirty zone, even briefly, is no longer clean -- the zoning and one-way flow exist because contamination does not announce itself; it just happens quietly if the layout allows it.",
    how_to_fill=[
        ("Check Date", "When monitored."),
        ("Sterile Store Temp / Humidity", "Readings."),
        ("Zone Pressure Readings", "Dirty/clean/sterile differentials."),
        ("Within Spec (Y/N)", "Confirmed."),
    ],
    verified_sources=[WHO_DECON_REPROCESS_SRC, NABH_HIC_CITE.format(code="HIC.6")],
    column_headers=["Check Date", "Sterile Store Temp / Humidity", "Zone Pressure Readings", "Within Spec (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 10-Feb-2026", "22°C / 65% RH", "Dirty negative, sterile positive — as specified", "Y"],
), "cssd_zoning_environmental_monitoring_record")

_add("HIC.6", 2, RecordSpec(
    oe_code="HIC.6.b",
    oe_requirement="Cleaning, packing, disinfection and/or sterilisation, storing and the issue of items is done as per the written guidance.",
    record_title="HIC.6 Record 02 — Sterilisation load record",
    what_is_this="This record is the proof every sterilisation cycle actually had its time, temperature and pressure recorded, and every pack actually carried its chemical indicators -- not a cycle run and assumed successful.",
    real_example="Load 14 on 12-March ran at 134°C for 4 minutes with a passed Class 5 integrator inside every pack and a Class 1 indicator outside, operator initials recorded.",
    why_nabh_asks="Skipping a step in this cycle -- an incomplete clean, a missing chemical indicator, an expired pack issued anyway -- can look identical to doing it right, right up until the moment the instrument is used on a patient.",
    how_to_fill=[
        ("Load No. / Date", "Which cycle, when."),
        ("Method / Time / Temperature / Pressure", "Cycle parameters."),
        ("Chemical Indicator Result (Pass/Fail)", "Confirmed."),
        ("Operator", "Who ran it."),
    ],
    verified_sources=[WHO_DECON_REPROCESS_SRC, NABH_HIC_CITE.format(code="HIC.6")],
    column_headers=["Load No. / Date", "Method / Time / Temperature / Pressure", "Chemical Indicator Result (Pass/Fail)", "Operator"],
    worked_example_row=["WORKED EXAMPLE — Load 14 / 12-Mar-2026", "Steam / 134°C for 4 min", "Pass", "CSSD Technician K. Pillai"],
), "sterilisation_load_record")

_add("HIC.6", 3, RecordSpec(
    oe_code="HIC.6.c",
    oe_requirement="Reprocessing of single-use instruments, equipment and devices are done as per written guidance.",
    record_title="HIC.6 Record 03 — Approved-for-reprocessing list and cycle-count tracking record",
    what_is_this="This record is the proof reprocessing only ever happens to an item on the written approved list, and that each item's cycle count was actually tracked against its defined maximum -- not reprocessing done by habit without a limit.",
    real_example="A laparoscopic trocar on the approved list, maximum 5 cycles, is tracked at cycle 3 with functional testing passed, and withdrawn from service at cycle 5.",
    why_nabh_asks="A single-use device was designed and validated to be used once -- reprocessing one that was never approved for it, or reprocessing it beyond a safe number of cycles, risks the item failing or no longer being sterile when it matters most.",
    how_to_fill=[
        ("Item / Approved (Y/N)", "On the ICC list or not."),
        ("Maximum Cycles Defined", "Limit set."),
        ("Current Cycle Count", "Running total."),
        ("Functional Test Result", "Pass/fail at this cycle."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.6")],
    column_headers=["Item / Approved (Y/N)", "Maximum Cycles Defined", "Current Cycle Count", "Functional Test Result"],
    worked_example_row=["WORKED EXAMPLE — Laparoscopic trocar / Y", "5", "3", "Pass"],
), "approved_reprocessing_list_cycle_count_tracking_record")

_add("HIC.6", 4, RecordSpec(
    oe_code="HIC.6.d",
    oe_requirement="Regular validation tests for sterilisation are carried out and documented.",
    record_title="HIC.6 Record 04 — Biological-indicator and Bowie-Dick validation log",
    what_is_this="This record is the proof the steriliser itself was actually validated with a biological indicator and a Bowie-Dick test on schedule -- the test that confirms the autoclave is genuinely achieving sterilisation, not just running.",
    real_example="The weekly biological-indicator test for the autoclave reads negative (pass) on 10-March, and the daily Bowie-Dick test passes on every working day that week.",
    why_nabh_asks="A steriliser that looks like it is running normally can still be failing to actually sterilise -- physical, chemical and biological indicators each catch a different kind of failure the others would miss.",
    how_to_fill=[
        ("Test Date / Type (BI/Bowie-Dick)", "Which test, when."),
        ("Steriliser ID", "Which machine."),
        ("Result (Pass/Fail)", "Outcome."),
        ("Action If Failed", "Recall triggered or not applicable."),
    ],
    verified_sources=[CDC_DISINFECTION_STERILIZATION_SRC, NABH_HIC_CITE.format(code="HIC.6")],
    column_headers=["Test Date / Type (BI/Bowie-Dick)", "Steriliser ID", "Result (Pass/Fail)", "Action If Failed"],
    worked_example_row=["WORKED EXAMPLE — 10-Mar-2026 / BI (weekly)", "Autoclave 1", "Pass", "N/A"],
), "biological_indicator_bowie_dick_validation_log")

_add("HIC.6", 5, RecordSpec(
    oe_code="HIC.6.e",
    oe_requirement="The established recall procedure is implemented when a breakdown in the sterilisation system is identified.",
    record_title="HIC.6 Record 05 — Sterilisation recall and re-qualification log",
    what_is_this="This record is the proof a sterilisation failure actually triggered the full recall procedure -- quarantine, trace-back, patient-risk assessment and re-qualification -- not a failure that was noted and the steriliser simply restarted.",
    real_example="A failed biological indicator on Load 22 triggers quarantine of all items from that load; two items already issued to the OT are retrieved before use; root-cause investigation finds a loading error; the steriliser passes three consecutive empty-chamber BIs before resuming patient loads.",
    why_nabh_asks="The time between a sterilisation failure being discovered and items from that load being used on a patient is exactly the window the recall procedure exists to close -- the procedure has to already be written down, not improvised after the failure is found.",
    how_to_fill=[
        ("Trigger / Date", "What failed, when."),
        ("Affected Items / Trace-back", "Load number and distribution."),
        ("Patient Impact Assessment", "If any item was used."),
        ("Root Cause / Corrective Action", "What caused it and what was fixed."),
        ("Re-qualification Result (3 Consecutive BIs)", "Before resuming patient loads."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.6")],
    column_headers=["Trigger / Date", "Affected Items / Trace-back", "Patient Impact Assessment", "Root Cause / Corrective Action", "Re-qualification Result (3 Consecutive BIs)"],
    worked_example_row=["WORKED EXAMPLE — Failed BI, Load 22 / 18-Mar-2026", "6 instrument sets; 2 already issued to OT, retrieved unused", "No items used on a patient", "Loading error; retraining on load configuration", "Pass — 3 consecutive empty-chamber BIs, 22-Mar-2026"],
), "sterilisation_recall_requalification_log")

_add("HIC.6", 6, RecordSpec(
    oe_code="HIC.6.c / HIC.6.d (stop-work authority)",
    oe_requirement="No instrument is used from a load with a failed biological indicator, a failed Bowie-Dick test, or a steriliser alarm mid-cycle; no single-use device is reprocessed outside the approved list or beyond its maximum cycles.",
    record_title="HIC.6 Record 06 — Instrument stop-work and refusal log",
    what_is_this="This record is the proof a suspect instrument was actually refused on the spot by whoever noticed it -- a CSSD technician, an OT nurse, a clinician -- rather than used because the case was already under way.",
    real_example="An OT nurse notices a pack's chemical indicator did not change colour and refuses to open it on the operating table, calling for a replacement set from a verified load instead.",
    why_nabh_asks="Using an instrument \"just this once\" while the recall investigation is still under way defeats the entire purpose of running the investigation in the first place -- the stop has to hold until the load is cleared, not until it is convenient.",
    how_to_fill=[
        ("Date/Time", "When identified."),
        ("Staff Member / Role", "Who refused it."),
        ("Item / Issue Identified", "What was wrong."),
        ("Replacement Used / Outcome", "What happened next."),
    ],
    verified_sources=[NABH_HIC_CITE.format(code="HIC.6")],
    column_headers=["Date/Time", "Staff Member / Role", "Item / Issue Identified", "Replacement Used / Outcome"],
    worked_example_row=["WORKED EXAMPLE — 18-Mar-2026, 9:40 AM", "Nurse T. George (OT)", "Chemical indicator did not change colour", "Replacement set opened from a verified load; suspect set quarantined"],
), "instrument_stop_work_refusal_log")


def main() -> None:
    for fname, spec in SOPS:
        out_path = OUT_ROOT / fname
        build_sop_v2(spec, out_path)
        print(f"built {out_path}")

    manifest: list[dict] = []
    for fname, spec in SOPS:
        manifest.append({
            "file": fname,
            "document_type": "sop",
            "standard_code": spec.sop_no.replace("SOP-", ""),
            "title": f"SOP — {spec.title} ({spec.sop_no.replace('SOP-', '')})",
        })
        sop_records = [r for r in RECORDS if r[0] == spec.sop_no.replace("SOP-", "")]
        for sop_code, idx, slug, rspec in sorted(sop_records, key=lambda r: r[1]):
            rel_path = f"Records/{sop_code}_Record_{idx:02d}_{slug}.docx"
            out_path = RECORDS_ROOT.parent / rel_path
            build_record(rspec, out_path)
            print(f"built {out_path}")
            manifest.append({
                "file": rel_path,
                "document_type": "record",
                "standard_code": sop_code,
                "record_index": idx,
                "title": rspec.record_title.split("—", 1)[-1].strip(),
            })

    manifest_path = OUT_ROOT / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {manifest_path} ({len(manifest)} entries)")


if __name__ == "__main__":
    main()
