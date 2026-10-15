# -*- coding: utf-8 -*-
"""Rebuilds the 11 existing AAC SOPs in the plain-body + audit-appendix
format approved for FMS.2 and already applied to the full FMS and ROM
chapters (2026-10-12).

No build script existed for AAC (same situation as ROM) -- every fact,
citation and URL below is read directly off the live committed .docx
(dumped via python-docx, including hyperlink relationships) on
2026-10-12. No new citation or number is introduced.

AAC SOPs already carried a "Why this step matters:" line per procedure
step in the live version -- that reasoning is kept and reused, just
reframed to the approved one-line "Why:" format and stripped of inline
NABH codes (e.g. "(AAC.1.c)", "(AAC.2.f)"), which move to the appendix
as boundary notes. "(Record N)" inline pointers are dropped from body
text since the records_note at the end of each SOP already covers which
records it produces.

Writes over the existing committed paths in place; does not touch Records.
"""
from __future__ import annotations

from pathlib import Path

from sop_record_common import PlainItem, SOPSpecV2, build_sop_v2

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "AAC"

NABH_AAC_CITE = (
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). "
    "Access, Assessment and Care of Patients chapter, standard {code}."
)

JOINT_COMMISSION_SRC = (
    "The Joint Commission. (2025). [National Patient Safety Goals, Goal 1 — "
    "use at least two patient identifiers (NPSG.01.01.01)](https://digitalassets.jointcommission.org/api/public/content/94389f1cc45940fd90d7954147cac4c4). "
    "Referenced as an external benchmark for patient-identification practice; "
    "SHCO accreditation does not itself require Joint Commission accreditation."
)
ESI_SRC = (
    "Agency for Healthcare Research and Quality. (2012). [Emergency Severity "
    "Index (ESI): A Triage Tool for Emergency Department Care, Version 4, "
    "Implementation Handbook](https://www.govinfo.gov/content/pkg/GOVPUB-HE20_6500-PURL-gpo23161/pdf/GOVPUB-HE20_6500-PURL-gpo23161.pdf) "
    "(AHRQ Pub. No. 12-0014). A five-level triage scale offered as an "
    "adoptable external benchmark for clinical-urgency categorisation; NABH "
    "does not itself mandate a specific triage scale."
)
WHO_HANDOVER_SRC = (
    "World Health Organization. (2007). [Patient Safety Solutions, Volume 1, "
    "Solution 3: Communication During Patient Hand-Overs](https://www.pslhub.org/learn/improving-patient-safety/design-for-safety/processes/who-communication-during-patient-handovers-may-2007-r1248/) "
    "(May 2007). Referenced as an external benchmark for structured handover "
    "communication; SHCO accreditation does not itself mandate a specific "
    "handover tool such as SBAR."
)
BMW_SRC = (
    "Ministry of Environment, Forest and Climate Change, Government of India. "
    "(2016). [Bio-Medical Waste Management Rules, 2016](https://cpcb.nic.in/bio-medical/) "
    "(G.S.R. 343(E), 28-Mar-2016). Statutory requirement for segregation, "
    "handling and disposal of specimens and biomedical waste, administered "
    "by the Central Pollution Control Board."
)
NABL_SRC = (
    "National Accreditation Board for Testing and Calibration Laboratories. "
    "(2025). [NABL 112B — Guidance Document: Medical Laboratories](https://nabl-india.org/) "
    "(Issue 01, Amdt. 01, 04-Nov-2025). Referenced as an external benchmark "
    "for laboratory quality-assurance programme design; SHCO accreditation "
    "does not itself require NABL accreditation."
)
AERB_SRC = (
    "Government of India, Department of Atomic Energy. (2004). [Atomic "
    "Energy (Radiation Protection) Rules, 2004](https://mgw3.aerb.gov.in/images/PDF/RPR2004.pdf) "
    "(G.S.R. 303, 25-Aug-2004). Statutory radiation-safety requirement "
    "administered by the Atomic Energy Regulatory Board (AERB); applies to "
    "diagnostic X-ray and imaging equipment."
)
NMC_RECORDS_SRC = (
    "National Medical Commission (formerly Medical Council of India). (2002, "
    "amended 2016). [Indian Medical Council (Professional Conduct, Etiquette "
    "and Ethics) Regulations, 2002](https://www.nmc.org.in/rules-regulations/code-of-medical-ethics-regulations-2002/1000/), "
    "Appendix 3 (format of medical records). Statutory basis in India for "
    "the minimum content of a patient's medical record, including the "
    "discharge card/summary."
)
MCCD_SRC = (
    "Office of the Registrar General, India, Ministry of Home Affairs, "
    "Government of India. (2012). [Physicians' Manual on Medical "
    "Certification of Cause of Death (MCCD), 5th ed.](https://censusindia.gov.in/nada/index.php/catalog/40073/download/43743/Physician_Manual_MCCD.pdf) "
    "Issued under the Registration of Births and Deaths Act, 1969, Sections "
    "10(2)-10(3); governs how the treating doctor certifies and records the "
    "cause of death."
)

# --------------------------------------------------------------- AAC.1.c ---
AAC1C = SOPSpecV2(
    sop_no="SOP-AAC.1.c",
    title="Definition of Scope of Healthcare Services per Department",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» defines, documents and "
        "communicates the scope of healthcare services each department "
        "offers -- including what happens when a presenting patient's "
        "need falls outside that scope -- so staff, patients and "
        "referring practitioners all work from the same written statement "
        "of what a department does and does not provide."
    ),
    purpose_trigger=(
        "A patient needing a procedure the ward doesn't actually perform "
        "is brought to registration late at night. This SOP is what gets "
        "them checked against another department or referred out "
        "immediately, with the reason logged -- not accepted on a "
        "judgement call that turns out to be wrong."
    ),
    purpose_why=(
        "We do this because a department whose real capability was never "
        "written down can end up accepting a patient it cannot safely "
        "manage. Writing down what a department can and cannot do is what "
        "keeps that decision from being made in the moment, under "
        "pressure, by whoever happens to be on duty."
    ),
    purpose_text=(
        "To define how «Hospital Name» defines, documents and communicates "
        "the scope of healthcare services offered by each department, "
        "including how an out-of-scope presentation is handled."
    ),
    scope_why="so registration staff and every clinical/diagnostic department work from the same written statement, not an assumption.",
    scope_text=(
        "Applies to every clinical and diagnostic department, the "
        "admission/registration desk, and the Medical Superintendent who "
        "approves each scope statement."
    ),
    responsibility_why="a scope statement nobody drafted, approved or checked at the door is a guess, not a safeguard.",
    responsibilities=[
        ("Department Heads", "Draft their department's scope-of-service statement, flag any change in capability, and confirm every out-of-scope presentation is logged."),
        ("Medical Superintendent", "Approves each scope statement, keeps the master list current, and decides how an uncovered out-of-scope presentation is handled."),
        ("Registration Staff", "Check the current scope-of-service register before accepting a non-emergency patient."),
    ],
    items=[
        PlainItem(
            heading="Define and document scope",
            why="A department whose actual capability was never written down can end up accepting a patient it cannot safely manage -- the scope statement is what stops that from being a judgement call made in the moment.",
            body=[
                "Each department head documents the services the "
                "department provides, including any defined limits (age "
                "range, case complexity, procedures not offered in-house).",
                "The Medical Superintendent approves the statement before "
                "it takes effect.",
            ],
            oe_code="AAC.1.c",
        ),
        PlainItem(
            heading="Communicate and review",
            why="A scope statement the registration desk has never seen does not actually prevent a mismatched admission -- it has to reach the people making the day-to-day decision.",
            body=[
                "The approved scope is communicated to registration/"
                "admission staff and displayed or made available within "
                "the department.",
                "Scope statements are reviewed at least annually, or "
                "immediately when a department's capability changes, "
                "including a temporary reduction such as equipment down "
                "or a specialist on leave.",
            ],
            oe_code="AAC.1.c",
        ),
        PlainItem(
            heading="Handle a presentation that falls outside current scope",
            why="A patient who needs something the department genuinely cannot provide still has to leave with a documented plan, not just a verbal 'we don't do that here' -- otherwise the scope statement protects the hospital's paperwork without protecting the patient.",
            body=[
                "When a presenting patient's need is outside the "
                "department's documented scope, registration or the "
                "treating clinician checks whether any other department "
                "can provide it before referring out.",
                "If the organisation genuinely cannot provide the "
                "service, the patient is referred or transferred per the "
                "hospital's transfer and referral procedure, and the "
                "presentation is logged with the reason and the referral "
                "given.",
            ],
            oe_code="AAC.1.c",
            boundary=[
                "A referral or transfer carried out under this step "
                "follows the Transfer-In, Transfer-Out and Referral SOP "
                "(AAC.2.f) -- this SOP owns the scope decision, not the "
                "transfer mechanics.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-2 (see the AAC.1 Records folder).",
    related_documents=[
        "Policy on Access, Registration, Admission and Continuity of Care (AAC.1)",
        "SOP — Transfer-In, Transfer-Out and Referral of Patients (AAC.2.f)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner if a "
        "department's capability changes or an out-of-scope presentation "
        "reveals a gap."
    ),
    full_reference_list=[NABH_AAC_CITE.format(code="AAC.1")],
)

# --------------------------------------------------------------- AAC.2.a ---
AAC2A = SOPSpecV2(
    sop_no="SOP-AAC.2.a",
    title="Patient Registration, Identification and Admission",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» registers and admits every "
        "patient -- including an unidentified patient -- through a "
        "consistent, documented process, so every patient is uniquely and "
        "correctly identified, a non-emergency admission is accepted only "
        "when the organisation can actually provide the needed service, "
        "and an emergency admission is never delayed for that decision."
    ),
    purpose_trigger=(
        "An unconscious patient with no ID is brought in by police at "
        "2 a.m. This SOP is what gets them registered immediately under a "
        "temporary descriptive identifier and treated without delay -- not "
        "left waiting while someone tries to work out who they are first."
    ),
    purpose_why=(
        "We do this because two patients sharing one loosely-kept record "
        "is how the wrong result ends up in the wrong file, and a patient "
        "who cannot state their name must never be left unregistered and "
        "untreated while someone tries to identify them first."
    ),
    purpose_text=(
        "To define how «Hospital Name» registers and admits every patient, "
        "including an unidentified patient, ensuring unique identification "
        "and that emergency care is never delayed for an acceptance "
        "decision."
    ),
    scope_why="so every registration and admission point -- not just the front desk -- follows the same identification and acceptance rules.",
    scope_text=(
        "Applies to every registration and admission point -- front "
        "office, OPD registration, emergency, day-care and in-patient "
        "admission desks -- and every patient presenting, identified or "
        "not."
    ),
    responsibility_why="an unverified identity or a missed scope check at registration becomes a patient-safety problem later, not a paperwork one now.",
    responsibilities=[
        ("Registration Staff", "Verify patient identity using at least two identifiers, register every patient including unidentified ones, and check the scope-of-service register before accepting a non-emergency patient."),
        ("Treating Clinician", "Authorises every admission, begins emergency treatment before any acceptance decision, and decides acceptance only after stabilisation."),
        ("Medical Records", "Maintains the unique-number master index, runs the periodic duplicate-number check, and reconciles a temporary unidentified-patient entry once identity is confirmed."),
    ],
    items=[
        PlainItem(
            heading="Register the patient, including an unidentified patient",
            why="Two patients sharing one loosely-kept record is how the wrong result ends up in the wrong file, and a patient who cannot state their name cannot simply be left unregistered until someone identifies them.",
            body=[
                "Identity is verified using a government photo ID where "
                "available, or at least two identifiers stated by the "
                "patient or an accompanying person (name and date of "
                "birth, for example).",
                "For an unidentified patient -- found unconscious, no ID, "
                "brought in by police or a bystander -- registration "
                "proceeds using a temporary descriptive identifier (for "
                "example 'Unknown Male, approx. 40 yrs, brought by "
                "police'). Registration is never withheld or delayed "
                "waiting for identity to be established.",
                "Once the patient's real identity becomes known, Medical "
                "Records updates the record and cross-references it to "
                "the unique number already issued, rather than issuing a "
                "second number.",
                "General consent for treatment is obtained at the point "
                "of entry, and its scope is explained to the patient or "
                "family before proceeding.",
            ],
            oe_code="AAC.2.a",
            technical_sources=[JOINT_COMMISSION_SRC],
        ),
        PlainItem(
            heading="Assign and protect the unique identification number",
            why="A patient who already has a hospital record but is issued a second number on a later visit ends up with their history split across two files -- exactly the kind of gap that produces a wrong-result or wrong-treatment error later.",
            body=[
                "At the end of a patient's first-ever registration, one "
                "unique identification number is generated.",
                "Before issuing a new number, the master index is "
                "searched by name, date of birth and other identifiers to "
                "confirm the patient does not already have one.",
                "A later visit may create an additional visit/encounter "
                "number, but it is linked to the existing unique number, "
                "never a replacement for it.",
                "Medical Records runs a duplicate-number check "
                "periodically and logs the result.",
            ],
            oe_code="AAC.2.a",
        ),
        PlainItem(
            heading="Confirm the service can be provided before accepting a non-emergency patient",
            why="Accepting a non-emergency patient the organisation cannot actually treat just moves the problem downstream to a worse moment -- checking capability at the door is what prevents that.",
            body=[
                "Before accepting a non-emergency patient, registration "
                "staff check the current department scope-of-service "
                "register to confirm the required service is available.",
                "If the required service is not available, the patient "
                "is not accepted; the presentation, the reason, and the "
                "advice or referral given are logged.",
            ],
            oe_code="AAC.2.a",
            boundary=[
                "The scope-of-service register checked here is "
                "maintained under AAC.1.c; this step covers the "
                "registration-desk check, not how the register itself is "
                "built or approved.",
            ],
        ),
        PlainItem(
            heading="Never delay emergency care for the acceptance decision",
            why="Checking whether the hospital 'can accept' an emergency patient before starting treatment gets the sequence backwards -- stabilise first, decide after, every time.",
            body=[
                "For an emergency presentation, life-saving treatment "
                "begins immediately; the acceptance decision is made only "
                "after the patient is stabilised, never before.",
                "If, after stabilisation, the hospital cannot continue "
                "care, the patient is transferred per the hospital's "
                "transfer and referral procedure.",
            ],
            oe_code="AAC.2.a",
            boundary=[
                "A transfer arising from this step follows the "
                "Transfer-In, Transfer-Out and Referral SOP (AAC.2.f).",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the AAC.2 Records folder).",
    related_documents=[
        "Policy on Access, Registration, Admission and Continuity of Care (AAC.2)",
        "SOP — Definition of Scope of Healthcare Services per Department (AAC.1.c)",
        "SOP — Transfer-In, Transfer-Out and Referral of Patients (AAC.2.f)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner if a "
        "registration error, duplicate-number case, or non-acceptance "
        "complaint recurs."
    ),
    full_reference_list=[NABH_AAC_CITE.format(code="AAC.2"), JOINT_COMMISSION_SRC],
)

# ----------------------------------------------------------- AAC.2.d/e ---
AAC2DE = SOPSpecV2(
    sop_no="SOP-AAC.2.d",
    title="Management of Bed Non-Availability and Clinical Prioritization of Access",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» manages patients when beds "
        "are not available -- including escalation when the first "
        "alternative also fails -- and how access to services is "
        "prioritized by clinical need using a named, documented urgency "
        "criterion, rather than order of arrival, payment ability, or any "
        "other non-clinical factor."
    ),
    purpose_trigger=(
        "No bed is available and the one alternate facility the admission "
        "desk tries also can't take the patient. This SOP is what gets "
        "that escalated to the Medical Superintendent for a next-best "
        "option immediately, instead of the same failed call being "
        "repeated."
    ),
    purpose_why=(
        "We do this because a patient turned away with no documented "
        "protocol is a decision made case-by-case under pressure, and "
        "first-come-first-served breaks down the moment a genuinely "
        "urgent patient arrives behind a routine one. A written protocol "
        "and a named urgency criterion are what keep that decision "
        "consistent and fair."
    ),
    purpose_text=(
        "To define how «Hospital Name» manages bed non-availability, "
        "including escalation when the first alternative fails, and "
        "prioritizes access to services by documented clinical urgency."
    ),
    scope_why="so the admission desk and every clinician making a prioritization call use the same documented criteria, not individual judgement alone.",
    scope_text="Applies to the admission desk, the Medical Superintendent, and every clinician or triage staff member making an admission or prioritization decision.",
    responsibility_why="a bed-shortage decision made without a documented protocol, or an urgency call made without a named criterion, cannot be reviewed or defended later.",
    responsibilities=[
        ("Medical Superintendent", "Maintains the bed-non-availability protocol and the clinical-prioritization criteria, and is the final escalation point when the first alternative also fails."),
        ("Treating Clinician / Triage Staff", "Apply the documented clinical-urgency criteria when deciding who is seen or admitted first."),
        ("Admission Desk Staff", "Follow the documented bed-non-availability protocol, inform the patient or family of the situation and the options, and log every instance."),
    ],
    items=[
        PlainItem(
            heading="Manage bed non-availability, including when the first alternative fails",
            why="A patient turned away or diverted with no documented protocol is a decision made case-by-case under pressure -- a written protocol, including what happens if the first option doesn't work either, is what makes the response consistent and defensible.",
            body=[
                "When no bed is available, the admission desk follows "
                "the documented protocol, in order of preference: hold "
                "in a designated observation/waiting area with "
                "appropriate clinical oversight, arrange transfer to an "
                "identified alternate facility, or escalate to the "
                "Medical Superintendent.",
                "If the identified alternate facility also cannot accept "
                "the patient, the admission desk escalates to the "
                "Medical Superintendent immediately for a next-best "
                "option, rather than repeating the same call to the same "
                "facility.",
                "The patient or family is told what is happening and the "
                "options available; if they decline a proposed "
                "alternative and choose to wait, that is recorded as an "
                "informed decision, not left undocumented.",
                "Every instance of bed non-availability and the action "
                "taken is logged.",
            ],
            oe_code="AAC.2.d",
        ),
        PlainItem(
            heading="Prioritize access by clinical need",
            why="First-come-first-served breaks down the moment a genuinely urgent patient arrives behind a routine one -- clinical urgency, assessed against a named criterion rather than individual judgement alone, is the standard this requirement sets.",
            body=[
                "Access to services is prioritized using a documented "
                "clinical-urgency criterion -- the hospital's own "
                "three-tier Emergency / Urgent / Routine criterion, or an "
                "adopted external scale such as the Emergency Severity "
                "Index (ESI) -- applied by the treating clinician or "
                "triage staff.",
                "The prioritization decision and its clinical basis are "
                "recorded for emergency and urgent cases.",
                "The prioritization criterion itself is reviewed at "
                "least annually to confirm it is still being applied "
                "consistently.",
            ],
            oe_code="AAC.2.e",
            technical_sources=[ESI_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-2 (see the AAC.2 Records folder).",
    related_documents=[
        "Policy on Access, Registration, Admission and Continuity of Care (AAC.2)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner after any "
        "bed-non-availability event that was not handled per protocol."
    ),
    full_reference_list=[NABH_AAC_CITE.format(code="AAC.2"), ESI_SRC],
)

# --------------------------------------------------------------- AAC.2.f ---
AAC2F = SOPSpecV2(
    sop_no="SOP-AAC.2.f",
    title="Transfer-In, Transfer-Out and Referral of Patients",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» transfers patients in from, "
        "and out to, other facilities, and how referrals are made -- "
        "including confirming the receiving facility can actually accept "
        "the patient, choosing an appropriate transport mode, and what to "
        "do if the first receiving facility is unreachable or declines -- "
        "so clinical information and responsibility for the patient pass "
        "across the handover without a gap."
    ),
    purpose_trigger=(
        "A patient needs a transfer but the first facility contacted "
        "doesn't answer. This SOP is what gets the next alternative "
        "contacted and the attempt logged immediately -- not the case "
        "quietly stalling while everyone assumes someone else is handling "
        "it."
    ),
    purpose_why=(
        "We do this because a patient sent elsewhere without first "
        "confirming the receiving facility can actually take them risks "
        "arriving to find there is no bed and no one expecting them -- and "
        "a patient arriving with no accompanying clinical information "
        "forces the receiving team to start from zero."
    ),
    purpose_text=(
        "To define how «Hospital Name» transfers patients in, transfers "
        "patients out, and makes referrals, so clinical information and "
        "responsibility pass across the handover without a gap."
    ),
    scope_why="so the treating clinician and nursing staff involved in any transfer or referral -- in either direction -- follow the same process.",
    scope_text="Applies to the treating clinician, nursing staff, and any patient being transferred or referred to or from «Hospital Name».",
    responsibility_why="a transfer decided without a named accepting clinician, or a handover without a written summary, is not actually a safe handover.",
    responsibilities=[
        ("Treating Clinician", "Decides on and documents the clinical justification for a transfer or referral, confirms the receiving facility can accept the patient and names the accepting clinician, and determines the transport mode and whether an accompanying staff member is required."),
        ("Nursing Staff", "Prepare the transfer summary, monitor the patient until transfer, and accompany an unstable patient where required."),
    ],
    items=[
        PlainItem(
            heading="Transfer-in",
            why="A patient arriving from another facility with no accompanying clinical information forces the receiving team to start from zero -- this step is what prevents that.",
            body=[
                "On transfer-in, the receiving clinician reviews and "
                "documents the referring facility's summary, provisional "
                "diagnosis, and treatment given so far.",
                "Any information gap is flagged and followed up with the "
                "referring facility.",
            ],
            oe_code="AAC.2.f",
        ),
        PlainItem(
            heading="Stabilise and confirm before transfer-out or referral",
            why="A patient sent elsewhere without first confirming the receiving facility can actually take them, with a named clinician agreeing to accept, risks arriving to find there is no bed and no one expecting them.",
            body=[
                "Before transfer-out or referral, the patient is "
                "stabilised to the extent possible for the planned "
                "transport.",
                "The receiving facility's ability to accept the patient "
                "is confirmed by phone (or equivalent), with the name "
                "and designation of the accepting clinician recorded -- "
                "not just that 'the hospital was called'.",
                "The transport mode -- own vehicle, basic ambulance, "
                "advanced life-support ambulance -- is decided based on "
                "the patient's clinical condition, and an accompanying "
                "staff member is assigned for any unstable patient.",
            ],
            oe_code="AAC.2.f",
        ),
        PlainItem(
            heading="Hand over with a written summary",
            why="A verbal heads-up that doesn't survive the handover is functionally the same as no handover at all -- the written summary is what actually travels with the patient.",
            body=[
                "A written transfer summary -- diagnosis, treatment "
                "given, reason for transfer, vitals at the time of "
                "transfer -- accompanies the patient.",
                "The patient or attendant is informed of the reason for "
                "transfer or referral.",
            ],
            oe_code="AAC.2.f",
            technical_sources=[WHO_HANDOVER_SRC],
        ),
        PlainItem(
            heading="If the receiving facility is unreachable or declines",
            why="A single failed call cannot be where this process stops -- the patient still needs somewhere to go, and that has to be tracked, not left to whoever is on shift to remember to try again.",
            body=[
                "If the first receiving facility cannot be reached, or "
                "declines, the next identified alternative is contacted, "
                "and every attempt -- facility, time, outcome -- is "
                "logged.",
                "If no facility can be confirmed within a clinically "
                "reasonable time, the case is escalated to the Medical "
                "Superintendent.",
            ],
            oe_code="AAC.2.f",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-2 (see the AAC.2 Records folder).",
    related_documents=[
        "Policy on Access, Registration, Admission and Continuity of Care (AAC.2)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner if a "
        "transfer summary is found incomplete or a receiving-facility "
        "confirmation was skipped."
    ),
    full_reference_list=[NABH_AAC_CITE.format(code="AAC.2"), WHO_HANDOVER_SRC],
)

# --------------------------------------------------------------- AAC.3.a ---
AAC3A = SOPSpecV2(
    sop_no="SOP-AAC.3.a",
    title="Initial Assessment of Patients",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» performs and documents the "
        "initial assessment of every patient -- out-patient, day-care, "
        "in-patient and emergency -- including what happens if a "
        "patient's condition changes before documentation is complete, or "
        "if a patient refuses assessment, so care from the first "
        "encounter onward is based on a recorded clinical picture, not an "
        "undocumented impression."
    ),
    purpose_trigger=(
        "A patient's condition changes while the clinician is still "
        "writing up the initial assessment. This SOP is what requires the "
        "assessment to be updated to reflect the patient's current state "
        "before it's signed off -- not left as an accurate record of a "
        "patient who no longer exists."
    ),
    purpose_why=(
        "We do this because an initial assessment that exists only in the "
        "clinician's memory cannot be handed over, reviewed, or checked -- "
        "writing it down, completely and in real time, is what makes it a "
        "clinical record the next person can actually rely on."
    ),
    purpose_text=(
        "To define how «Hospital Name» performs and documents the initial "
        "assessment of every patient, including a condition change before "
        "documentation is complete, and a patient refusal."
    ),
    scope_why="so every clinician performing a first assessment -- across all patient categories -- follows the same standard.",
    scope_text="Applies to every clinician performing a first assessment of a patient, across out-patient, day-care, in-patient and emergency categories.",
    responsibility_why="an assessment left undocumented, late, or not updated after a condition change is a gap nobody downstream can see.",
    responsibilities=[
        ("Treating Clinician", "Performs and documents the initial assessment within the defined time frame for the patient's category, updates it if the patient's condition changes before documentation is complete, and manages a refusal appropriately."),
        ("Medical Superintendent", "Ensures initial-assessment compliance is audited periodically and gaps are corrected."),
    ],
    items=[
        PlainItem(
            heading="Perform the initial assessment",
            why="An initial assessment that exists only in the clinician's memory cannot be handed over, reviewed, or checked -- writing it down, with every required element present, is what makes it a clinical record rather than an impression.",
            body=[
                "The initial assessment covers, at minimum, six things:",
                "1. The presenting complaint.",
                "2. Relevant history.",
                "3. Vital signs.",
                "4. Physical examination findings.",
                "5. Known allergies.",
                "6. A provisional diagnosis or working impression.",
                "For emergency patients, initial assessment includes a "
                "documented triage category reflecting urgency, recorded "
                "concurrently with the clinical picture.",
            ],
            oe_code="AAC.3.a",
        ),
        PlainItem(
            heading="Document within the defined time frame",
            why="An assessment documented a day after the encounter is reconstructed from memory, not recorded in real time -- the time frame exists so the record reflects what was actually found, not what was later recalled.",
            body=[
                "Out-patient and day-care assessments are documented at "
                "the time of the consultation.",
                "In-patient assessments are documented within the "
                "hospital-defined time frame (the hospital states this as "
                "a specific number of hours in its own SOP; no external "
                "body prescribes it).",
                "Emergency assessments are documented immediately, "
                "concurrent with triage.",
            ],
            oe_code="AAC.3.a",
        ),
        PlainItem(
            heading="Update the assessment if the patient's condition changes",
            why="An assessment that was accurate when started but was overtaken by a deterioration before it was finished is not actually a record of the patient's current state -- leaving it as originally written would be misleading, not just incomplete.",
            body=[
                "If the patient's clinical condition changes materially "
                "before the initial assessment is documented, the "
                "clinician records the change and updates the assessment "
                "to reflect the patient's current status before signing "
                "it off as complete.",
            ],
            oe_code="AAC.3.a",
        ),
        PlainItem(
            heading="Manage a patient who refuses assessment",
            why="A refusal that is simply left unrecorded looks, from the file, like an assessment that was never attempted -- the record has to show the attempt was made and why it stopped.",
            body=[
                "If a patient refuses part or all of the initial "
                "assessment, the clinician documents what was refused, "
                "explains the clinical implications to the patient, and "
                "records the refusal.",
                "If the refusal materially compromises patient safety "
                "(an emergency patient refusing a necessary examination, "
                "for example), the clinician escalates to the Medical "
                "Superintendent rather than simply recording the refusal "
                "and moving on.",
            ],
            oe_code="AAC.3.a",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-2 (see the AAC.3 Records folder).",
    related_documents=[
        "Policy on Assessment of Patients (AAC.3)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner if an audit "
        "finds initial assessments missing, late, or not updated after a "
        "condition change."
    ),
    full_reference_list=[NABH_AAC_CITE.format(code="AAC.3")],
)

# ----------------------------------------------------------- AAC.4.c/d/e ---
AAC4CDE = SOPSpecV2(
    sop_no="SOP-AAC.4.c",
    title="Laboratory Specimen Handling, Turnaround Time and Critical Result Reporting",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» handles laboratory "
        "specimens from requisition through to disposal -- including "
        "rejecting an unsuitable specimen rather than testing it -- "
        "ensures results are available within a defined time frame, and "
        "ensures critical results reach the treating clinician at the "
        "earliest, with escalation if the first attempt fails."
    ),
    purpose_trigger=(
        "A critically abnormal lab result comes back and the first call to "
        "the treating clinician goes unanswered. This SOP is what gets it "
        "escalated to the next person on the on-call list immediately, "
        "with every attempt logged -- not sitting in a report queue until "
        "someone happens to check it."
    ),
    purpose_why=(
        "We do this because a haemolysed, clotted or mislabelled specimen "
        "tested anyway can produce a result that looks normal but is "
        "wrong, and a critical result that isn't escalated when the first "
        "call fails is a patient-safety failure waiting to happen."
    ),
    purpose_text=(
        "To define how «Hospital Name» handles laboratory specimens, "
        "rejects unsuitable ones, meets a defined turnaround time, and "
        "communicates critical results with escalation if the first "
        "attempt fails."
    ),
    scope_why="so laboratory staff, sample-collection staff and every ordering clinician handle a specimen the same way from requisition to result.",
    scope_text="Applies to laboratory staff, phlebotomy/sample-collection staff, and every clinician who orders a laboratory test.",
    responsibility_why="a specimen mishandled or a critical result sitting unescalated is a mistake that reaches the patient, not just the paperwork.",
    responsibilities=[
        ("Laboratory In-Charge", "Maintains the written specimen-handling and specimen-rejection guidance and the critical-value list, and monitors turnaround time."),
        ("Collecting Staff", "Follow the written guidance for requisition, collection, identification, handling and transport of every specimen, and recollect a rejected specimen."),
    ],
    items=[
        PlainItem(
            heading="Requisition, collection and handling",
            why="A specimen that is mislabelled or mishandled between collection and testing can produce a result for the wrong patient -- written guidance at every step is what closes that gap.",
            body=[
                "Every specimen is collected against a documented "
                "requisition, labelled with the patient's unique "
                "identifier at the bedside or point of collection, and "
                "transported to the laboratory per written guidance on "
                "handling and timing.",
                "Specimens are disposed of per the organisation's "
                "biomedical waste procedure once testing is complete.",
            ],
            oe_code="AAC.4.c",
            technical_sources=[BMW_SRC],
        ),
        PlainItem(
            heading="Reject an unsuitable specimen rather than testing it",
            why="A haemolysed, clotted, mislabelled or insufficient specimen can produce a result that looks normal but is wrong -- testing it anyway, to avoid the delay of a redraw, trades a known problem for an invisible one.",
            body=[
                "A specimen is rejected, not tested, if it is "
                "mislabelled, unlabelled, clotted or haemolysed where "
                "this affects the test, of insufficient quantity, or "
                "received outside the stability window for that test.",
                "Every rejection is logged with the reason, and "
                "collecting staff are notified immediately to recollect.",
                "For a medico-legal or forensic specimen, chain-of-"
                "custody documentation -- who collected, who "
                "transported, who received, with signatures and times "
                "at each handoff -- accompanies the specimen in addition "
                "to normal handling.",
            ],
            oe_code="AAC.4.d",
        ),
        PlainItem(
            heading="Turnaround time",
            why="A result that takes three days to reach the ward for a test the clinician needed same-day isn't actually usable -- a defined turnaround time, tracked test by test, is what makes the lab result clinically useful.",
            body=[
                "Each test category has a defined turnaround time, from "
                "specimen receipt to result availability, with a shorter "
                "defined time for tests ordered as STAT/urgent.",
                "Turnaround time is tracked and reviewed against the "
                "defined target.",
            ],
            oe_code="AAC.4.d",
        ),
        PlainItem(
            heading="Critical results, with escalation if the first attempt fails",
            why="A critical result sitting in a report queue until someone happens to check it is a patient-safety failure waiting to happen -- and a single unanswered call cannot be where the process stops either.",
            body=[
                "Critical values are defined on a written list, agreed "
                "with clinicians.",
                "A critical result is communicated directly -- phone or "
                "equivalent -- to the treating clinician or nurse at the "
                "earliest, and the communication is logged with date, "
                "time and recipient.",
                "If the treating clinician cannot be reached within the "
                "hospital-defined escalation time (a specific number of "
                "minutes the hospital states in its own SOP; no external "
                "body prescribes it), the laboratory escalates to the "
                "next person on the facility's on-call or escalation "
                "list, and every attempt is logged, not just the one "
                "that finally succeeded.",
            ],
            oe_code="AAC.4.e",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the AAC.4 Records folder).",
    related_documents=[
        "Policy on Laboratory and Diagnostic Services (AAC.4)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Laboratory In-Charge, and sooner if a "
        "critical-result delay, specimen-handling error, or repeated "
        "rejection pattern occurs."
    ),
    full_reference_list=[NABH_AAC_CITE.format(code="AAC.4"), BMW_SRC],
)

# ----------------------------------------------------------- AAC.4.f/g/h ---
AAC4FGH = SOPSpecV2(
    sop_no="SOP-AAC.4.f",
    title="Laboratory Outsourcing, Quality Assurance and Equipment Calibration",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» selects outsourced "
        "laboratories based on their quality assurance system and "
        "specimen-transport conditions, runs its own in-house laboratory "
        "quality assurance programme, calibrates and maintains laboratory "
        "equipment on a defined schedule, and manages equipment downtime "
        "so testing is not simply paused when an instrument fails."
    ),
    purpose_trigger=(
        "A key lab analyser fails mid-shift. This SOP is what gets a "
        "documented backup -- a second instrument, a manual method, or an "
        "approved outsourced lab -- arranged immediately, instead of "
        "testing simply stopping until someone gets around to fixing it."
    ),
    purpose_why=(
        "We do this because a result produced on an instrument that was "
        "never checked against a known reference is only as trustworthy "
        "as the last time someone happened to service it, and sending a "
        "sample to whichever outside lab is cheapest or closest, with no "
        "check on its own quality system, passes that risk straight "
        "through to the patient."
    ),
    purpose_text=(
        "To define how «Hospital Name» selects outsourced laboratories, "
        "runs its own laboratory QA programme, calibrates and maintains "
        "equipment, and manages equipment downtime."
    ),
    scope_why="so the Laboratory In-Charge and any outsourced laboratory used by the hospital are both held to the same documented standard.",
    scope_text="Applies to the Laboratory In-Charge, the Medical Superintendent, and any external laboratory to which «Hospital Name» outsources testing.",
    responsibility_why="an unverified outside lab or an uncalibrated instrument produces a result nobody can actually trust.",
    responsibilities=[
        ("Laboratory In-Charge", "Verifies outsourced laboratories' quality assurance credentials and transport arrangements, runs the in-house QA programme, maintains the equipment calibration schedule, and arranges a contingency when equipment is down."),
        ("Medical Superintendent", "Approves the list of outsourced laboratories and reviews the QA programme at least annually."),
    ],
    items=[
        PlainItem(
            heading="Select, verify and contract outsourced laboratories",
            why="Sending a sample to whichever lab is cheapest or closest, with no check on its own quality system or how the specimen will actually get there intact, passes the risk straight through to the patient.",
            body=[
                "Before a test category is outsourced, the receiving "
                "laboratory's quality assurance credentials -- "
                "accreditation status, or equivalent documented QA "
                "evidence -- are verified and kept on file.",
                "Specimen transport conditions to the outsourced "
                "laboratory -- temperature control where required, and a "
                "maximum transit time consistent with the test's "
                "stability window -- are agreed and documented.",
                "A written agreement or service-level understanding with "
                "the outsourced laboratory states expected turnaround "
                "time and how a result discrepancy is handled.",
                "The approved outsourced-laboratory list is reviewed at "
                "least annually.",
            ],
            oe_code="AAC.4.f",
            technical_sources=[NABL_SRC],
        ),
        PlainItem(
            heading="Run the in-house QA programme",
            why="A laboratory that never checks its own results against a known standard has no way of knowing whether its results are actually reliable -- internal and external quality control is what answers that question.",
            body=[
                "Internal quality control is run and documented for "
                "each applicable test, per a defined schedule.",
                "The laboratory participates in an external quality "
                "assessment scheme (proficiency testing) and documents "
                "the results.",
                "QA programme results are reviewed by the Laboratory "
                "In-Charge, with a documented root cause and corrective "
                "action for any out-of-range result.",
            ],
            oe_code="AAC.4.g",
            technical_sources=[NABL_SRC],
        ),
        PlainItem(
            heading="Calibrate, maintain and manage downtime",
            why="A result produced on an instrument that was never checked against a known reference is only as trustworthy as the last time someone happened to service it, and an instrument simply taken offline with no backup plan turns an equipment problem into a patient-care gap.",
            body=[
                "Every laboratory instrument has a defined calibration "
                "and preventive-maintenance schedule, carried out and "
                "logged.",
                "Any instrument found out of calibration is taken out of "
                "service immediately until corrected, and this is logged "
                "alongside the calibration record, not treated as a "
                "separate undocumented event.",
                "For the period an instrument is out of service, the "
                "Laboratory In-Charge arranges a documented contingency "
                "-- a backup instrument, manual method, or outsourcing to "
                "an approved laboratory -- so testing is not simply "
                "paused.",
                "An instrument is only returned to service once the "
                "Laboratory In-Charge confirms and signs off that it has "
                "passed calibration.",
            ],
            oe_code="AAC.4.h",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-3 (see the AAC.4 Records folder).",
    related_documents=[
        "Policy on Laboratory and Diagnostic Services (AAC.4)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Laboratory In-Charge, and sooner if a QA result "
        "or calibration check is out of range, or an equipment-downtime "
        "contingency is used."
    ),
    full_reference_list=[NABH_AAC_CITE.format(code="AAC.4"), NABL_SRC],
)

# --------------------------------------------------------- AAC.5.d/e/f/g/i ---
AAC5 = SOPSpecV2(
    sop_no="SOP-AAC.5.d",
    title="Imaging Services — Turnaround Time, Critical Results, Outsourcing, Quality Assurance and Calibration",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» ensures imaging results are "
        "available within a defined time frame, critical imaging findings "
        "are intimated immediately with escalation if the first attempt "
        "fails, outsourced imaging services are selected on quality "
        "assurance grounds, patients are screened for imaging-specific "
        "safety risks before the study, an imaging quality assurance "
        "programme is implemented, and imaging equipment is calibrated "
        "and maintained -- including statutory radiation-safety "
        "compliance and a documented contingency when equipment is down."
    ),
    purpose_trigger=(
        "A patient of childbearing age is due for an X-ray and nobody has "
        "asked about pregnancy. This SOP is what requires that screen to "
        "happen and be documented before the study goes ahead -- not "
        "discovered as a problem afterward."
    ),
    purpose_why=(
        "We do this because an imaging study that goes ahead without "
        "checking whether it's actually safe for this particular patient "
        "-- an unnecessary radiation exposure, a contrast study on someone "
        "with a known allergy -- turns a diagnostic step into the injury "
        "it was meant to help prevent."
    ),
    purpose_text=(
        "To define how «Hospital Name» manages imaging turnaround time, "
        "critical results, outsourcing, quality assurance, equipment "
        "calibration and radiation-safety compliance."
    ),
    scope_why="so the Imaging In-Charge and every ordering or outsourcing clinician follow the same safety and quality standard.",
    scope_text="Applies to the Imaging/Radiology In-Charge, radiology staff, and every clinician ordering or outsourcing an imaging study.",
    responsibility_why="an unscreened patient, an unescalated critical finding, or an uncalibrated scanner each turns a diagnostic step into a risk.",
    responsibilities=[
        ("Imaging In-Charge", "Monitors turnaround time, maintains the critical-finding list, runs the pre-imaging safety screen, runs the imaging QA programme, and maintains the equipment calibration schedule including statutory radiation-safety compliance and downtime contingency."),
        ("Medical Superintendent", "Approves outsourced imaging providers and reviews the QA programme at least annually."),
    ],
    items=[
        PlainItem(
            heading="Screen the patient before imaging",
            why="An imaging study that goes ahead without checking whether it's actually safe for this particular patient -- an unnecessary radiation exposure to a pregnant patient, a contrast study on someone with a known allergy -- turns a diagnostic step into the injury it was meant to help prevent.",
            body=[
                "Before any radiation-based study, pregnancy status is "
                "screened and documented for a patient of childbearing "
                "age, following the ALARA (as low as reasonably "
                "achievable) principle.",
                "Before any contrast-enhanced study, known allergy and "
                "relevant renal history are screened and documented.",
            ],
            oe_code="AAC.5.d",
        ),
        PlainItem(
            heading="Turnaround time and critical results, with escalation",
            why="An imaging finding that could change immediate management -- a pneumothorax, a fracture needing urgent reduction -- is only useful if it reaches the clinician fast, and a single unanswered call cannot be where that process stops.",
            body=[
                "Each imaging modality has a defined turnaround time "
                "from study completion to report availability, tracked "
                "against the target.",
                "Critical imaging findings are defined on a written list "
                "and communicated directly to the treating clinician "
                "immediately, with the communication logged.",
                "If the treating clinician cannot be reached within a "
                "defined time, the Imaging In-Charge escalates to the "
                "next person on the on-call list, with every attempt "
                "logged.",
            ],
            oe_code="AAC.5.e",
        ),
        PlainItem(
            heading="Outsourcing imaging services",
            why="Sending a patient to an external imaging centre with no check on its quality assurance or radiation-safety compliance passes that risk straight to the patient.",
            body=[
                "Before imaging is outsourced, the receiving facility's "
                "quality assurance credentials and radiation-safety "
                "compliance are verified and kept on file.",
                "The approved outsourced-imaging list is reviewed at "
                "least annually.",
            ],
            oe_code="AAC.5.f",
            technical_sources=[AERB_SRC],
        ),
        PlainItem(
            heading="Quality assurance, calibration, radiation safety, and downtime",
            why="Imaging equipment that is neither quality-checked nor calibrated can produce a misleading image, unmanaged radiation output is a statutory safety failure on top of a clinical one, and equipment taken offline with no plan turns a technical fault into an access gap.",
            body=[
                "The imaging QA programme includes periodic "
                "image-quality checks against a defined standard, "
                "documented and reviewed.",
                "Every imaging equipment item has a defined calibration "
                "and preventive-maintenance schedule, carried out and "
                "logged, with equipment taken out of service immediately "
                "if found out of calibration.",
                "Radiation-safety compliance -- shielding, personnel "
                "dosimetry, equipment registration/licensing as "
                "applicable -- is checked and documented per statutory "
                "requirement.",
                "For the period equipment is out of service, the "
                "Imaging In-Charge arranges a documented contingency "
                "(referral to an approved outsourced provider, or an "
                "alternate in-house modality where clinically "
                "appropriate).",
            ],
            oe_code="AAC.5.g",
            technical_sources=[AERB_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the AAC.5 Records folder).",
    related_documents=[
        "Policy on Imaging and Diagnostic Services (AAC.5)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Imaging In-Charge, and sooner if a "
        "critical-result delay, QA finding, radiation-safety compliance "
        "gap, or equipment-downtime contingency is used."
    ),
    full_reference_list=[NABH_AAC_CITE.format(code="AAC.5"), AERB_SRC],
)

# --------------------------------------------------------------- AAC.6.a ---
AAC6A = SOPSpecV2(
    sop_no="SOP-AAC.6.a",
    title="Laboratory Safety Programme",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» implements a laboratory "
        "safety programme covering personal protective equipment, "
        "biosafety practice, staff immunisation against occupational "
        "exposure, and safe handling and disposal of biomedical waste, "
        "so laboratory staff and patients are protected from the "
        "specific hazards of laboratory work."
    ),
    purpose_trigger=(
        "A lab staff member gets a needlestick injury during specimen "
        "handling. This SOP is what gets it reported and logged "
        "immediately, with post-exposure follow-up documented -- not "
        "treated as something to mention informally and move on from."
    ),
    purpose_why=(
        "We do this because a laboratory where PPE use depends on "
        "individual habit, not a written programme, and where staff "
        "immunisation against occupational exposure is not tracked, is "
        "one lapse away from an avoidable exposure incident -- to a staff "
        "member, not just a specimen."
    ),
    purpose_text=(
        "To define how «Hospital Name» implements a laboratory safety "
        "programme covering PPE, biosafety practice, staff immunisation, "
        "and biomedical waste handling and disposal."
    ),
    scope_why="so every laboratory staff member -- not just the person in charge -- follows the same safety practice.",
    scope_text="Applies to every laboratory staff member and to the Laboratory In-Charge.",
    responsibility_why="a safety incident nobody reports, or an immunisation gap nobody tracks, leaves staff exposed without anyone knowing.",
    responsibilities=[
        ("Laboratory In-Charge", "Implements and documents the laboratory safety programme, tracks staff immunisation status, and ensures PPE and biosafety practice are followed."),
        ("Laboratory Staff", "Follow PPE and biosafety requirements, maintain their immunisation status, and report any safety incident immediately."),
    ],
    items=[
        PlainItem(
            heading="Implement PPE, biosafety practice and staff immunisation",
            why="A laboratory where PPE use depends on individual habit, not a written programme, and where staff immunisation against occupational exposure (such as Hepatitis B) is not tracked, is one lapse away from an avoidable exposure incident.",
            body=[
                "Personal protective equipment -- gloves, coats, eye "
                "protection as applicable -- is provided and its use is "
                "checked periodically.",
                "Biosafety practice for specimen handling, spill "
                "response, and sharps disposal follows written guidance, "
                "and a spill kit is checked and restocked on a defined "
                "schedule.",
                "Every laboratory staff member's occupational "
                "immunisation status (Hepatitis B, for example) is "
                "recorded, and staff found non-immune are offered "
                "vaccination.",
            ],
            oe_code="AAC.6.a",
            technical_sources=[BMW_SRC],
        ),
        PlainItem(
            heading="Manage biomedical waste",
            why="Laboratory waste is biohazardous by nature -- segregating and disposing of it correctly is a statutory obligation, not a housekeeping preference.",
            body=[
                "Laboratory waste is segregated at source per the "
                "categories defined under the Bio-Medical Waste "
                "Management Rules, 2016, and disposed of through an "
                "authorised route.",
                "Any safety incident -- needlestick, spill, exposure -- "
                "is reported immediately and logged, with post-exposure "
                "follow-up (source-patient screening, prophylaxis where "
                "indicated) documented.",
            ],
            oe_code="AAC.6.a",
            technical_sources=[BMW_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-2 (see the AAC.6 Records folder).",
    related_documents=[
        "Policy on Laboratory and Diagnostic Services (AAC.6)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Laboratory In-Charge, and sooner after any "
        "laboratory safety incident."
    ),
    full_reference_list=[NABH_AAC_CITE.format(code="AAC.6"), BMW_SRC],
)

# --------------------------------------------------------- AAC.7.a/b/c/d ---
AAC7 = SOPSpecV2(
    sop_no="SOP-AAC.7.a",
    title="Continuity and Multidisciplinary Care",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» keeps every patient under "
        "the care of an identified responsible clinician at every phase "
        "of care, shares information about the patient's care and "
        "response to treatment among the treating team, uses standardised "
        "handover communication at every shift change and transfer, and "
        "moves patients safely between wards, units and departments "
        "within the hospital."
    ),
    purpose_trigger=(
        "A doctor goes off duty without a covering doctor being named in "
        "the file. This SOP is what a nurse catches at the next round and "
        "escalates immediately -- rather than a patient quietly having no "
        "one actually responsible for them until the gap is noticed by "
        "accident."
    ),
    purpose_why=(
        "We do this because a patient who is never formally handed off "
        "from one doctor to another is a patient nobody is actually "
        "watching -- gaps in continuity are where delayed diagnoses and "
        "missed deterioration happen. An unstructured, rushed handover is "
        "exactly where a pending task or an early-warning sign gets "
        "silently dropped between one shift and the next."
    ),
    purpose_text=(
        "To define how «Hospital Name» maintains an identified "
        "responsible clinician at every phase of care, shares information "
        "among the treating team, uses standardised handover "
        "communication, and transfers patients safely within the "
        "hospital."
    ),
    scope_why="so doctors, nurses and allied health staff at every phase of care -- not just at admission -- all follow the same continuity process.",
    scope_text=(
        "Applies to treating doctors, nurses, allied health staff, the "
        "Medical Superintendent and the Quality Coordinator, for every "
        "phase of care -- out-patient, emergency, in-patient, day-care, "
        "internal transfer and discharge."
    ),
    responsibility_why="a patient with no named responsible clinician, or a handover nobody acknowledged, is a gap that only gets caught by luck.",
    responsibilities=[
        ("Treating Doctor", "Is the identified responsible clinician during their phase of care, hands over to the covering doctor when off duty, and documents clinical status before any internal transfer."),
        ("Nurse", "Performs standardised shift handover, accompanies patients during internal transfer, and documents the handover and transfer."),
        ("Medical Superintendent", "Is accountable that continuity, information-sharing and handover processes are defined and followed."),
        ("Quality Coordinator", "Audits responsible-clinician documentation, referral completeness and handover/transfer records, and tracks corrective action on recurring gaps."),
    ],
    items=[
        PlainItem(
            heading="Identify the responsible individual at every phase of care",
            why="A patient who is never formally handed off from one doctor to another is a patient nobody is actually watching -- gaps in continuity are where delayed diagnoses and missed deterioration happen.",
            body=[
                "At the start of every phase of care -- registration, "
                "emergency triage, admission, transfer, day-care -- "
                "record in the patient file the name, contact number and "
                "expected availability of the doctor responsible for "
                "that phase.",
                "When the treating doctor goes off duty, identify the "
                "covering doctor by name and record the handover of "
                "responsibility in the patient file before the treating "
                "doctor leaves.",
                "At every nursing round, confirm that the patient file "
                "shows a current, named responsible clinician; escalate "
                "to the Medical Superintendent immediately if it does "
                "not.",
            ],
            oe_code="AAC.7.a",
        ),
        PlainItem(
            heading="Share information among care-providers, including referrals",
            why="Medical, nursing and allied-health notes written in isolation, with referrals that never get a documented answer, mean each discipline is treating its own partial picture of the patient rather than one coordinated plan.",
            body=[
                "Write all nursing notes, doctor's progress notes and "
                "allied-health entries in the shared patient file (or "
                "linked system) so every authorised member of the "
                "treating team can read them.",
                "When referring a patient to another department, the "
                "referring doctor states the clinical question, relevant "
                "history and urgency in the file; the referred "
                "department records its opinion in the same file within "
                "the agreed turnaround time.",
                "Document every verbal order immediately in the patient "
                "file and have the ordering doctor countersign it within "
                "the hospital-defined countersignature window (a "
                "specific number of hours the hospital states in its own "
                "SOP; no external body prescribes it), flagging any "
                "order not countersigned within that window to the "
                "Quality Coordinator.",
                "Where multidisciplinary input is needed, discuss the "
                "patient at the scheduled team meeting or ward round and "
                "record the outcome in the file.",
            ],
            oe_code="AAC.7.b",
        ),
        PlainItem(
            heading="Carry out standardised handover communication",
            why="An unstructured, rushed handover is where a pending task, an abnormal result or an early-warning trigger gets silently dropped between one shift and the next.",
            body=[
                "Use the hospital's chosen standardised handover tool "
                "(for example SBAR -- Situation, Background, Assessment, "
                "Recommendation) at every shift change and at every "
                "transfer between units or departments.",
                "Cover five things for each patient:",
                "1. Identification.",
                "2. Current diagnosis and condition.",
                "3. Key events since the last handover.",
                "4. Pending tasks and follow-up required.",
                "5. Any safety concern or early-warning-score trigger.",
                "Document the handover in the handover register, "
                "patient file or electronic system, and have the "
                "receiving team acknowledge receipt before the outgoing "
                "team leaves.",
                "Minimise interruptions during handover; if interrupted, "
                "confirm at the end that every patient on the list was "
                "actually covered.",
            ],
            oe_code="AAC.7.c",
            technical_sources=[WHO_HANDOVER_SRC],
        ),
        PlainItem(
            heading="Transfer patients safely within the hospital",
            why="A transfer with no documented clinical status, no confirmed receiving unit and no accompanying staff member turns a routine ward move into an unmonitored gap in care.",
            body=[
                "Before transferring a patient between wards, units or "
                "departments, document the reason for transfer and "
                "assess and document the patient's clinical status "
                "immediately before the move.",
                "Inform the receiving unit and obtain its confirmation "
                "of readiness before the patient leaves.",
                "Send the patient accompanied by a nurse or trained "
                "attendant with monitoring and equipment appropriate to "
                "the patient's condition; send critical or unstable "
                "patients accompanied by a doctor.",
                "Continue medications, infusions and oxygen during "
                "transfer, complete the standardised handover between "
                "the transferring and receiving teams, and record the "
                "time of departure and arrival in the patient file.",
            ],
            oe_code="AAC.7.d",
            technical_sources=[WHO_HANDOVER_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the AAC.7 Records folder).",
    related_documents=[
        "Policy on Continuity and Multidisciplinary Care (AAC.7)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner when "
        "staffing patterns, ward layout or the handover tool change."
    ),
    full_reference_list=[NABH_AAC_CITE.format(code="AAC.7"), WHO_HANDOVER_SRC],
)

# ----------------------------------------------------------- AAC.8.a-g ---
AAC8 = SOPSpecV2(
    sop_no="SOP-AAC.8.a",
    title="Discharge Process and Discharge Summary",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» gives a discharge summary "
        "to every patient leaving the organisation, including patients "
        "leaving against medical advice (LAMA); what identification, "
        "clinical content, follow-up and urgent-care instructions the "
        "summary must contain; how a death summary is prepared when a "
        "patient dies; and how planned discharge and special needs are "
        "identified before the patient leaves."
    ),
    purpose_trigger=(
        "A patient insists on leaving against medical advice. This SOP is "
        "what still gets them a discharge summary -- what was advised, the "
        "risks explained, that they left against advice -- before they "
        "walk out, instead of leaving with nothing written down at all."
    ),
    purpose_why=(
        "We do this because a patient who leaves without a written "
        "summary -- especially one who leaves against medical advice -- "
        "takes an undocumented, unexplained set of risks out the door "
        "with them, and a patient discharged with medicines but no "
        "explanation of warning signs or who to call is a readmission "
        "waiting to happen."
    ),
    purpose_text=(
        "To define how «Hospital Name» issues a discharge summary to "
        "every patient including LAMA, its required content, death "
        "summary preparation, and discharge planning and special-needs "
        "identification."
    ),
    scope_why="so every patient discharged, transferred out, or who dies in the organisation leaves with the same documented process behind them.",
    scope_text=(
        "Applies to treating doctors, nurses, registration/front-office "
        "staff, the Medical Superintendent and the Quality Coordinator, "
        "for every patient discharged, transferred out, or who dies in "
        "the organisation."
    ),
    responsibility_why="a discharge summary nobody checked for completeness, or a death summary that doesn't match the civil-registration record, creates problems long after the patient has left.",
    responsibilities=[
        ("Treating Doctor", "Prepares or supervises preparation of the discharge summary, writes the death summary where applicable, discusses expected discharge date and special needs with the patient and family."),
        ("Nurse", "Assists with discharge planning, explains instructions, confirms patient/family understanding, and identifies special needs."),
        ("Registration/Front-Office Staff", "Verify identification and dates on the discharge summary and coordinate the administrative discharge process."),
        ("Quality Coordinator", "Audits discharge-summary completeness and issuance rate, and tracks corrective action on recurring gaps."),
    ],
    items=[
        PlainItem(
            heading="Issue a discharge summary to every patient, including LAMA",
            why="A patient who leaves without a written summary -- especially one who leaves against medical advice -- takes an undocumented, unexplained set of risks out the door with them.",
            body=[
                "Prepare a discharge summary for every patient leaving "
                "«Hospital Name», with no exception for patients leaving "
                "against medical advice (LAMA).",
                "For a LAMA patient, record in the summary what was "
                "advised, the risks of leaving explained to the patient, "
                "and that the patient left against medical advice; the "
                "separate informed-consent/LAMA acknowledgement itself "
                "is handled under the informed-consent policy -- this "
                "step covers the summary content only.",
                "Give the discharge summary to the patient or the "
                "patient's representative before or at the time of "
                "leaving.",
            ],
            oe_code="AAC.8.a",
            technical_sources=[NMC_RECORDS_SRC],
        ),
        PlainItem(
            heading="Complete identification, dates and clinical content",
            why="A discharge summary missing a date of admission, a diagnosis, or the results of a key investigation is not a summary the next treating doctor can actually rely on.",
            body=[
                "Enter these four identification fields on every "
                "discharge summary:",
                "1. The patient's name.",
                "2. The unique identification number.",
                "3. The date of admission.",
                "4. The date of discharge.",
                "The registration/front-office team verifies these four "
                "fields before release.",
                "Enter these eight clinical-content items:",
                "1. The reasons for admission.",
                "2. Significant findings.",
                "3. The provisional and/or final diagnosis.",
                "4. The patient's condition at discharge.",
                "5. Investigation results.",
                "6. Any procedure performed.",
                "7. Medication administered.",
                "8. Other treatment given.",
                "Write the clinical content in language the patient or "
                "family can understand, using plain-language explanation "
                "alongside any medical terminology.",
            ],
            oe_code="AAC.8.b",
            technical_sources=[NMC_RECORDS_SRC],
        ),
        PlainItem(
            heading="Give follow-up, medication and urgent-care instructions",
            why="A patient discharged with medicines but no explanation of warning signs or who to call is a readmission waiting to happen.",
            body=[
                "Include five things in the discharge summary:",
                "1. The follow-up date or timeframe.",
                "2. Medications prescribed at discharge, with dose, "
                "frequency, route and duration.",
                "3. Diet/activity/wound-care instructions where "
                "applicable.",
                "4. Warning signs that should prompt an earlier visit.",
                "5. A contact number for queries.",
                "Include instructions on when and how to obtain urgent "
                "care: symptoms requiring immediate return, how to reach "
                "«Hospital Name»'s emergency department, and an "
                "alternative emergency contact if «Hospital Name» is "
                "unreachable.",
                "Explain all of the above verbally to the patient and/or "
                "family in the language they understand -- «Hindi and "
                "English» -- and document that this was done.",
            ],
            oe_code="AAC.8.c",
        ),
        PlainItem(
            heading="Prepare the death summary when a patient dies",
            why="The cause of death recorded in a hospital's own summary and the cause certified for civil registration must be the same fact, recorded consistently, not two different accounts of how the patient died.",
            body=[
                "When a patient dies, prepare a death summary containing "
                "all the fields of the discharge summary (identification, "
                "dates, clinical content) plus the cause of death as "
                "determined by the treating doctor, time of death, "
                "whether a post-mortem was advised and the family's "
                "decision, and any medico-legal reporting done.",
                "Certify the cause of death following the format and "
                "cause-of-death classification set out in the national "
                "Medical Certification of Cause of Death (MCCD) scheme, "
                "so the hospital's own record and the civil-registration "
                "certificate state the same cause.",
                "Give the death summary to the next of kin and retain a "
                "copy in the patient file.",
            ],
            oe_code="AAC.8.d",
            technical_sources=[MCCD_SRC],
        ),
        PlainItem(
            heading="Plan discharge in advance and identify special needs",
            why="Special needs discovered for the first time on the day of discharge -- a wheelchair not arranged, a family not trained in wound care -- turn a planned departure into a last-minute scramble that risks readmission.",
            body=[
                "Discuss the expected date of discharge with the patient "
                "and family early in the stay, and update it as the "
                "clinical situation changes.",
                "Before discharge, identify special needs affecting care "
                "after discharge -- wound care, physiotherapy, mobility "
                "aids, home nursing, dietary needs, oxygen, follow-up "
                "investigations, referral to another facility.",
                "Where a special need is identified, include in the "
                "discharge plan how it will be met -- written "
                "instructions, referral letter, equipment arranged, or "
                "family trained.",
                "Before the patient leaves, confirm that the patient and "
                "family understand the discharge plan and the "
                "special-needs arrangements.",
            ],
            oe_code="AAC.8.e",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-5 (see the AAC.8 Records folder).",
    related_documents=[
        "Policy on Discharge Process and Discharge Summary (AAC.8)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner when the "
        "discharge process, summary template or clinical protocols "
        "change."
    ),
    full_reference_list=[
        NABH_AAC_CITE.format(code="AAC.8"),
        NMC_RECORDS_SRC,
        MCCD_SRC,
    ],
)

SOPS = [
    ("SOP_AAC.1.c_scope_of_services.docx", AAC1C),
    ("SOP_AAC.2.a_registration_admission.docx", AAC2A),
    ("SOP_AAC.2.d_e_bed_availability_and_prioritization.docx", AAC2DE),
    ("SOP_AAC.2.f_transfer_referral.docx", AAC2F),
    ("SOP_AAC.3.a_initial_assessment.docx", AAC3A),
    ("SOP_AAC.4.c_d_e_lab_specimen_tat_critical_results.docx", AAC4CDE),
    ("SOP_AAC.4.f_g_h_lab_outsourcing_qa_calibration.docx", AAC4FGH),
    ("SOP_AAC.5.d_e_f_g_i_imaging_services.docx", AAC5),
    ("SOP_AAC.6.a_laboratory_safety_programme.docx", AAC6A),
    ("SOP_AAC.7.a_b_c_d_continuity_multidisciplinary_care.docx", AAC7),
    ("SOP_AAC.8.a_to_g_discharge_process_summary.docx", AAC8),
]


def main() -> None:
    for fname, spec in SOPS:
        out_path = OUT_ROOT / fname
        build_sop_v2(spec, out_path)
        print(f"built {out_path} (v2: plain body + audit appendix)")


if __name__ == "__main__":
    main()
