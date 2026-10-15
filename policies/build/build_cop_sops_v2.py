# -*- coding: utf-8 -*-
"""Rebuilds the 13 existing COP SOPs in the plain-body + audit-appendix
format approved for FMS.2 and already applied to FMS, ROM, AAC and HRM
(2026-10-12).

No build script existed for COP -- every fact, citation and URL below is
read directly off the live committed .docx (dumped via python-docx,
including hyperlink relationships) on 2026-10-12. No new citation or
number is introduced.

COP is the chapter that originally triggered this whole redesign (Mk's
screenshot showed up to six NABH/chapter cross-reference codes inside a
single Scope sentence). The live COP SOPs already use good
patient-safety-framed "Why this step matters:" reasoning per step and
already avoid "NABH requires" framing -- the actual jargon problem here
is narrower than in other chapters: (1) every item heading carries its
own OE code suffix, e.g. "(COP.10.a)"; (2) Scope and body paragraphs are
full of bracketed cross-references to OTHER chapters/SOPs, e.g.
"(AAC.2.b)", "(COP.4)", "(HIC.2)" -- exactly what Mk's original
screenshot complained about. Both are stripped from the body and moved
to the Appendix as boundary notes; the codes themselves, and the
legitimate statutory citations (Indian Acts, Supreme Court judgments),
are kept -- citing Indian law is not NABH jargon and stays in the body
exactly as before, since a staff member needs to know a legal duty
applies to them even in plain language.

"«Hospital to define ...»" placeholders are hospital-configuration
markers, not NABH jargon, and are kept as-is throughout.

Writes over the existing committed paths in place; does not touch Records.
"""
from __future__ import annotations

from pathlib import Path

from sop_record_common import PlainItem, SOPSpecV2, build_sop_v2

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "COP"

NABH_COP_CITE = (
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). "
    "Care of Patients chapter, standard {code}."
)

TELEMEDICINE_SRC = (
    "Board of Governors (in supersession of the Medical Council of India). "
    "(2020). [Telemedicine Practice Guidelines, 2020](https://covid19dashboard.mohfw.gov.in/pdf/Telemedicine.pdf). "
    "Appendix 5 of the Indian Medical Council (Professional Conduct, "
    "Etiquette and Ethics) Regulations, 2002, Ministry of Health and "
    "Family Welfare. The statutory basis for who may provide a "
    "telemedicine consultation, identity and consent requirements, "
    "prescription handling, emergency escalation, and record-keeping."
)
NMC_ACT_S34_SRC = (
    "Government of India. (2019). [The National Medical Commission Act, "
    "2019](https://PRSINDIA.org/files/bills_acts/bills_parliament/2019/National%20Medical%20Commission%20Act,%202019.pdf) "
    "(Act No. 30 of 2019), s. 34 (Bar to practice), under which no person "
    "other than one enrolled in the State Register or the National "
    "Register may practise medicine as a qualified medical practitioner, "
    "with contravention punishable by imprisonment up to one year, a "
    "fine up to five lakh rupees, or both."
)
THOA_SRC = (
    "Government of India. (1994). [The Transplantation of Human Organs "
    "and Tissues Act, 1994](https://www.indiacode.nic.in/bitstream/123456789/19260/1/thoa_act_1994.pdf) "
    "(Act No. 42 of 1994). ss. 9, 10(1)(a), 14(1) and 19: no hospital may "
    "commence organ-removal, storage or transplantation activity unless "
    "registered; a living-donor transplant requires the donor to be a "
    "near relative or Authorisation Committee approval; commercial "
    "dealing in human organs is a punishable offence. s. 2(d) and s. "
    "3(6) separately define brain-stem death and require its "
    "certification by a Board of medical experts."
)
MHA_SRC = (
    "Government of India, Ministry of Health and Family Welfare. (2017). "
    "[The Mental Healthcare Act, 2017](https://www.indiacode.nic.in/handle/123456789/2249) "
    "(Act No. 10 of 2017), s. 97 (Restraints and seclusion), under which "
    "seclusion is prohibited and physical restraint of a person with "
    "mental illness is permitted only as the sole means to prevent "
    "imminent, immediate harm, authorised by the treating psychiatrist, "
    "for no longer than necessary, promptly recorded, never used as "
    "punishment or for staff convenience, with the nominated "
    "representative informed within 24 hours."
)
RPWD_SRC = (
    "Government of India. (2016). [The Rights of Persons with "
    "Disabilities Act, 2016](https://indiacode.nic.in/bitstream/123456789/19406/1/rpwd_act_2016.pdf) "
    "(Act No. 49 of 2016), ss. 3 and 25: persons with disability may not "
    "be discriminated against and are entitled to barrier-free access in "
    "all parts of hospitals and healthcare institutions, and to priority "
    "in attendance and treatment."
)
BNSS_397_SRC = (
    "Government of India. (2023). [The Bharatiya Nagarik Suraksha "
    "Sanhita, 2023](https://indiacode.nic.in/bitstream/123456789/20099/3/A2023-46.pdf) "
    "(Act No. 46 of 2023), s. 397 (\"Treatment of victims\"), the "
    "criminal-procedure provision in force from 1 July 2024 governing a "
    "hospital's duty to treat and document medico-legal cases, in "
    "supersession of the Code of Criminal Procedure, 1973."
)
BNSS_194_SRC = (
    "Government of India. (2023). [The Bharatiya Nagarik Suraksha "
    "Sanhita, 2023](https://indiacode.nic.in/bitstream/123456789/20099/3/A2023-46.pdf) "
    "(Act No. 46 of 2023), s. 194 (\"Police to enquire and report on "
    "suicide, etc.\"), the current provision governing police intimation "
    "and reporting for deaths brought to, or occurring at, the hospital, "
    "in supersession of the Code of Criminal Procedure, 1973."
)
DISASTER_ACT_SRC = (
    "Government of India. (2005). [The Disaster Management Act, "
    "2005](https://www.indiacode.nic.in/bitstream/123456789/2045/1/A200553.pdf) "
    "(Act No. 53 of 2005), establishing the National, State and District "
    "Disaster Management Authorities and their power to direct "
    "departments, agencies and officials -- hospitals among them -- to "
    "carry out disaster-management measures."
)
EPIDEMIC_ACT_SRC = (
    "Government of India. (1897, as amended 2020). [The Epidemic "
    "Diseases Act, 1897, as amended by the Epidemic Diseases (Amendment) "
    "Act, 2020](https://prsindia.org/files/bills_acts/acts_parliament/2020/Epidemic%20Diseases%20(Amendment)%20Act,%202020.pdf) "
    "(Act No. 34 of 2020), empowering Central and State Governments to "
    "take special measures during epidemics and prohibiting acts of "
    "violence against healthcare service personnel."
)
CTAS_SRC = (
    "Murray, M., Bullard, M., & Grafstein, E., for the CTAS and CEDIS "
    "National Working Groups. (2004). Revisions to the Canadian "
    "Emergency Department Triage and Acuity Scale implementation "
    "guidelines. Canadian Journal of Emergency Medicine, 6(6), 421-427. "
    "https://doi.org/10.1017/S1481803500009428 -- the triage scale named "
    "as an available option and its reassessment intervals, verified "
    "directly against this source, not assumed. NABH does not mandate "
    "this specific scale."
)
BLOOD_BANK_SRC = (
    "Government of India, Ministry of Health and Family Welfare. (1999). "
    "[The Drugs and Cosmetics (2nd Amendment) Rules, 1999](https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2022/drug_rules/DR_G.S.R.%20245(E)%20dt_05.04.1999_Amendment%20to%20Rule%20122_Requirements%20of%20blood%20bank.pdf) "
    "(G.S.R. 245(E), dated 5 April 1999), amending the Drugs and "
    "Cosmetics Rules, 1945 under the Drugs and Cosmetics Act, 1940, which "
    "requires every blood bank to hold a licence (Form 28-C) before "
    "issuing blood or blood components."
)
COMMON_CAUSE_SRC = (
    "Supreme Court of India. (2018). [Common Cause (A Regd. Society) v "
    "Union of India](https://www.scobserver.in/cases/common-cause-euthanasia-and-the-right-to-die-with-dignity-case-background/), "
    "Writ Petition (Civil) No. 215 of 2005 (decided 9 March 2018), which "
    "held that the right to die with dignity -- including the right to "
    "execute an advance medical directive and to have life-sustaining "
    "treatment withheld or withdrawn under safeguards -- is part of the "
    "right to life under Article 21 of the Constitution of India."
)
PCPNDT_SRC = (
    "Government of India, Ministry of Health and Family Welfare. (1994). "
    "[The Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition "
    "of Sex Selection) Act, 1994](https://pndt.mohfw.gov.in/WriteReadData/l892s/PC-PNDT%20ACT-1994.pdf), "
    "ss. 3A, 5(2) and 6, which prohibit sex selection, prohibit "
    "communicating the sex of a foetus to the pregnant woman, her "
    "relatives, or anyone else by any means, and prohibit sex "
    "determination through pre-natal diagnostic techniques including "
    "ultrasonography."
)
MTP_SRC = (
    "Government of India. (2021). [The Medical Termination of Pregnancy "
    "(Amendment) Act, 2021](https://PRSINDIA.org/files/bills_acts/acts_parliament/2021/Medical%20Termination%20of%20Pregnancy%20Amendment%20Act%202021.pdf) "
    "(Act No. 8 of 2021), amending the Medical Termination of Pregnancy "
    "Act, 1971, which sets the current gestational limits and opinion "
    "requirements for termination, requires a Medical Board for cases "
    "beyond those limits involving substantial foetal abnormality, and "
    "makes it an offence for a registered medical practitioner to reveal "
    "the identity of a woman whose pregnancy was terminated."
)
BIRTHS_DEATHS_SRC = (
    "Government of India. (1969). [The Registration of Births and "
    "Deaths Act, 1969](https://www.indiacode.nic.in/bitstream/123456789/1682/1/A1969-18.pdf) "
    "(Act No. 18 of 1969), which defines 'birth' to include still-birth, "
    "places the duty to report a birth occurring in a hospital on the "
    "medical officer in charge (or someone they authorise), and "
    "separately requires any midwife or attendant present at the birth "
    "to notify the Registrar."
)
JJ_ACT_SRC = (
    "Government of India. (2016). [The Juvenile Justice (Care and "
    "Protection of Children) Act, 2015](https://lddashboard.legislative.gov.in/sites/default/files/A2016-2_0.pdf) "
    "(Act No. 2 of 2016, in force 15 January 2016), which defines a "
    "'child in need of care and protection' (including a missing or "
    "run-away child), establishes the district Child Welfare Committee, "
    "and requires such a child to be produced before the Committee "
    "within 24 hours."
)
POCSO_SRC = (
    "Government of India. (2012). [The Protection of Children from "
    "Sexual Offences Act, 2012](https://www.indiacode.nic.in/bitstream/123456789/14753/1/pocso.pdf) "
    "(Act No. 32 of 2012), ss. 19 and 21, which require any person who "
    "knows or believes a sexual offence against a child is likely or has "
    "been committed to report it to the Special Juvenile Police Unit or "
    "local police, and make failure to report a punishable offence, "
    "including for a person in charge of an institution who fails to "
    "report an offence by a subordinate."
)

# --------------------------------------------------------------- COP.1 ---
COP1 = SOPSpecV2(
    sop_no="SOP-COP.1",
    title="Uniform Care Across Settings and Telemedicine",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» gives the same standard of "
        "care for a given clinical condition wherever that care is "
        "provided -- identifying every patient with at least two "
        "identifiers before an act of care, applying evidence-based "
        "clinical protocols the same way in every setting, and either "
        "running a telemedicine facility under written guidance or "
        "stating in writing that none is provided."
    ),
    purpose_trigger=(
        "A protocol is revised on the ward but the emergency area keeps "
        "using the old version. This SOP is what requires every setting "
        "to receive the new version and withdraw the old one on the same "
        "date -- not a revision that quietly reaches one room and not "
        "another."
    ),
    purpose_why=(
        "We do this because a bed number identifies a location, not a "
        "person, and a location can be occupied by someone else between "
        "an order being written and the act of care being given -- and "
        "because a protocol known on the ward and unknown in day-care "
        "means a patient's care depends on which room they happen to be "
        "in, rather than on their condition."
    ),
    purpose_text=(
        "To define how «Hospital Name» gives uniform care across every "
        "setting: two-identifier confirmation before every act of care, "
        "an applicable-law list kept current, evidence-based protocols "
        "applied consistently, and telemedicine under written guidance or "
        "a recorded decision not to provide it."
    ),
    scope_why="so every setting that provides care -- OPD, day-care, wards, theatre, telemedicine -- works from the same identification and protocol standard.",
    scope_text=(
        "Applies to every setting in which «Hospital Name» provides care "
        "-- out-patient department, day-care, in-patient wards, "
        "intensive or high-dependency areas, the emergency area, "
        "procedure rooms, the operation theatre, and any location from "
        "which a telemedicine consultation is given or received."
    ),
    responsibility_why="care that depends on which room a patient is in, rather than on their condition, is exactly what uniform care exists to prevent.",
    responsibilities=[
        ("Head of the Institution", "Is accountable for two-identifier patient identification, care that stays inside applicable laws, protocols that are actually used and consistent across settings, and telemedicine that is either guided in writing or not provided."),
        ("Heads of Each Setting", "Keep the current clinical protocol version in their setting, withdraw the previous version on the same date as every other setting, and report a contradiction between settings."),
        ("Clinicians and Nursing Staff", "Apply the two-identifier process before every act of care and apply the adopted protocol for the condition without running a personal version that differs by setting."),
        ("Registered Medical Practitioners (Telemedicine)", "Provide telemedicine consultations only under the written guidance, never as informal remote advice."),
        ("Administration", "Maintains the applicable-law list against the service directory and, where telemedicine is provided, the platform and privacy arrangement."),
        ("Quality/Accreditation Coordinator", "Audits the records produced by this SOP and reports findings to the Head of the Institution."),
    ],
    items=[
        PlainItem(
            heading="Confirm two identifiers before every act of care",
            why="A bed number, room number or tray position identifies a location, not a person -- and a location can be occupied by someone else between the order being written and the act of care being given.",
            body=[
                "The two identifiers used at «Hospital Name» are the "
                "patient's name and the unique identification number "
                "issued at registration, or another pair the hospital "
                "defines. Bed, room, cubicle, trolley or tray position is "
                "never used as an identifier.",
                "Staff confirm both identifiers against the patient (or "
                "identifier band) and against the record, requisition or "
                "order, before medication, a procedure, specimen "
                "collection, transfusion, transfer, or any other act of "
                "care.",
            ],
            oe_code="COP.1.a",
        ),
        PlainItem(
            heading="Keep the applicable-law list current against the service directory",
            why="A law list copied from another hospital's chapter, or one that was never updated when a service changed, tells staff they are compliant with laws that may no longer be the ones that actually govern what this hospital does.",
            body=[
                "Administration maintains a written list of the laws and "
                "regulations that apply to the care «Hospital Name» "
                "actually provides.",
                "When a service is added, suspended or withdrawn, the "
                "applicable-law list is reviewed for that service and "
                "updated if needed.",
                "The review is dated and signed by the person who "
                "performed it.",
            ],
            oe_code="COP.1.b",
            boundary=[
                "Services are added, suspended or withdrawn under the "
                "service-definition policy (AAC.1), which this step does "
                "not restate.",
            ],
        ),
        PlainItem(
            heading="Adopt and maintain evidence-based clinical protocols",
            why="A protocol that was adopted once and never dated, version-controlled or withdrawn when superseded leaves staff unable to tell a current instruction from an old one -- which is the same failure as having no protocol at all.",
            body=[
                "Clinicians and heads of department adopt evidence-based "
                "clinical protocols or practice guidelines for the "
                "conditions this hospital treats, drawing on recognised "
                "evidence-based sources such as the Ministry of Health "
                "and Family Welfare's Standard Treatment Guidelines.",
                "Each protocol is dated, version-controlled, and marked "
                "as either in use or withdrawn; a withdrawn protocol is "
                "removed from every point of use the same day.",
            ],
            oe_code="COP.1.c",
            boundary=[
                "Nursing clinical practice guidelines remain owned by "
                "the nursing-care policy (COP.4.d) and are not "
                "duplicated here.",
            ],
        ),
        PlainItem(
            heading="Apply the same protocol in every setting that provides that care",
            why="A protocol known on the ward and unknown in day-care, or a consultant's personal variant that differs between the out-patient clinic and the theatre, means a patient's care depends on which room they happen to be in rather than on their condition -- which is exactly what uniform care exists to stop.",
            body=[
                "For each adopted protocol, the settings in which that "
                "condition is cared for, and the current version in use "
                "in each setting, are mapped and kept current.",
                "When a protocol is revised, every listed setting "
                "receives the new version and withdraws the old one on "
                "the same date -- a revision that reaches the ward and "
                "not the emergency area is a break in uniform care.",
                "Intensity of care may vary with clinical need (higher "
                "monitoring in intensive care, for example); the "
                "protocol's indications, contraindications and safety "
                "checks may not vary by setting.",
                "A contradiction found between settings is reported to "
                "the Quality/Accreditation Coordinator the same day it "
                "is found.",
            ],
            oe_code="COP.1.d",
        ),
        PlainItem(
            heading="Provide telemedicine under written guidance, or state in writing that none is offered",
            why="Without a written decision either way, informal remote advice happens anyway -- a message, an unsigned prescription sent as a photo, a telephone instruction with no record -- and the hospital discovers it only after something has already gone wrong.",
            body=[
                "Whether «Hospital Name» provides a telemedicine "
                "facility is a hospital-defined decision. If none is "
                "provided, that decision is written and displayed at "
                "points of contact, and informal remote advice is "
                "explicitly not treated as a telemedicine consultation.",
                "If a facility is provided, written guidance covers "
                "eight things:",
                "1. Who may provide a consultation (a Registered "
                "Medical Practitioner only).",
                "2. How practitioner and patient identity are "
                "confirmed.",
                "3. How informed consent is obtained and recorded.",
                "4. Which modes and platform are used.",
                "5. Which services may and may not be provided "
                "remotely.",
                "6. How a prescription is produced, transmitted and "
                "filed.",
                "7. How an emergency presenting remotely is given "
                "first-aid advice and directed to in-person care "
                "rather than completed on the call.",
                "8. How the consultation is filed against the "
                "patient's unique identification number.",
                "Every telemedicine consultation, or the absence of one "
                "under the written decision, is logged.",
            ],
            oe_code="COP.1.e",
            technical_sources=[TELEMEDICINE_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-5 (see the COP.1 Records folder).",
    related_documents=[
        "Policy on Uniform Care Across Settings and Telemedicine (COP.1)",
        "Registration, Admission and Transfer SOP (AAC.2)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality/"
        "Accreditation Coordinator, and sooner when a misidentification, "
        "a contradiction between settings, or an unofficial remote "
        "consultation exposes a gap, or when the registration, service-"
        "definition, assessment or nursing-care policies this SOP "
        "depends on are revised."
    ),
    full_reference_list=[NABH_COP_CITE.format(code="COP.1"), TELEMEDICINE_SRC],
)

# --------------------------------------------------------------- COP.2 ---
COP2 = SOPSpecV2(
    sop_no="SOP-COP.2",
    title="Emergency Services, Ambulance and Management of Disasters",
    purpose_plain=(
        "This SOP sets out how every emergency patient is identified, "
        "triaged, treated, reassessed while waiting, and discharged or "
        "admitted with a proper note; how medico-legal cases and deaths "
        "are handled and documented; how the hospital's ambulance "
        "arrangement is kept available and fit for use; and how the "
        "hospital plans and prepares for disasters, epidemics and "
        "community emergencies."
    ),
    purpose_trigger=(
        "A patient triaged as stable starts to deteriorate while waiting. "
        "This SOP is what requires them to be reassessed at a fixed "
        "interval and escalated to the duty doctor the moment that "
        "deterioration shows -- not caught only when someone happens to "
        "walk past."
    ),
    purpose_why=(
        "We do this because not every patient who arrives can be seen in "
        "arrival order -- the sickest patient has to be seen first, not "
        "the one who happened to arrive first -- and because an "
        "ambulance, or a disaster plan, that is never actually checked or "
        "drilled is not real readiness, just a document."
    ),
    purpose_text=(
        "To define how every emergency patient is identified, triaged, "
        "treated, reassessed, and discharged or admitted with a proper "
        "note; how medico-legal cases and deaths are handled; how the "
        "ambulance arrangement is kept available and fit for use; and how "
        "the hospital plans for disasters, epidemics and community "
        "emergencies."
    ),
    scope_why="so emergency-area staff, ambulance staff and the whole hospital's disaster preparedness all follow the same standard, not a scope beyond what this hospital has declared it can do.",
    scope_text=(
        "Applies to all patients presenting to, or treated within, the "
        "hospital's emergency area, to the ambulance service used to "
        "bring patients to or move them from the hospital, and to the "
        "hospital's organisation-wide disaster/epidemic/community-"
        "emergency preparedness. It does not extend the hospital's "
        "declared scope of services -- an emergency beyond that scope is "
        "stabilised and referred, not undertaken."
    ),
    responsibility_why="a patient left unreassessed, an MLC left undocumented, or an ambulance nobody checked is a gap that only shows up in the moment it matters most.",
    responsibilities=[
        ("Medical Officer / Duty Doctor", "Examines and treats every emergency patient, decides and documents disposition, certifies death where applicable, and initiates medico-legal documentation."),
        ("Triage Nurse / Emergency Area Staff", "Performs triage at the point of arrival, reassesses waiting patients at the defined interval, and escalates any deterioration immediately."),
        ("Ambulance Driver / EMT", "Keeps the ambulance fit for use, checks its equipment and medications on the defined schedule, and begins appropriate treatment during transit."),
        ("Quality/Accreditation Coordinator", "Maintains the Records under this SOP, runs the periodic emergency-care audit, and keeps the disaster/epidemic plan current and drilled."),
        ("Medical Superintendent", "Approves this SOP and the disaster/epidemic plan, and is informed of every death-within-minutes-of-arrival case and every disaster-plan activation."),
    ],
    items=[
        PlainItem(
            heading="Identified emergency area",
            why="A patient arriving as an emergency must be able to find, and staff must be able to point to, one clearly identified place where emergency care happens -- confusion about location costs minutes that matter.",
            body=[
                "The hospital designates and signs the hospital's "
                "defined emergency area as the single point for "
                "receiving emergency patients.",
                "Signage to the emergency area is visible from the main "
                "entrance and approach road, in Hindi and English (and "
                "any other language the hospital serves).",
                "The area is staffed and equipped on a 24x7 basis, or on "
                "the hospital's defined hours of emergency coverage if "
                "the hospital does not run a round-the-clock emergency "
                "service -- in which case this is displayed publicly so "
                "patients are not misled.",
            ],
            oe_code="COP.2.a",
        ),
        PlainItem(
            heading="Medico-legal cases and statutory emergency care",
            why="Certain emergencies are medico-legal cases (MLCs) by law -- assault, accident, poisoning, burns, suspected foul play, and similar -- and every hospital, regardless of ability to pay, is statutorily obliged to provide emergency care and stabilise such patients before any other consideration.",
            body=[
                "The Duty Doctor identifies whether the presenting case "
                "is an MLC using the hospital's defined MLC criteria "
                "list.",
                "Emergency treatment and stabilisation is provided "
                "first, in every case, regardless of the patient's "
                "ability to pay or produce identification or police "
                "clearance.",
                "For an identified MLC, the required documentation (MLC "
                "register entry, intimation to the police where the law "
                "requires it, preservation of evidence such as clothing) "
                "is completed before or alongside treatment, never "
                "instead of it.",
            ],
            oe_code="COP.2.b",
            technical_sources=[BNSS_397_SRC],
        ),
        PlainItem(
            heading="System of triage",
            why="Not every patient who arrives can be seen in arrival order -- triage sorts patients by clinical urgency so the sickest patient is seen first, not the one who happened to arrive first.",
            body=[
                "Every patient entering the emergency area is triaged "
                "against a structured, published triage scale before "
                "being made to wait -- never an ad hoc or invented "
                "category list. The Canadian Triage and Acuity Scale "
                "(CTAS), a five-level scale, is one verified, published "
                "scale a hospital may adopt. NABH does not mandate a "
                "specific scale, so a hospital may instead adopt a "
                "different named, published scale in its place -- but a "
                "scale with no published criteria behind it is not "
                "sufficient.",
                "The triage category is recorded, visible to staff, and "
                "re-checked if the patient's condition changes while "
                "waiting.",
                "Staff performing triage are trained on the adopted "
                "scale's categories and criteria.",
            ],
            oe_code="COP.2.c",
            technical_sources=[CTAS_SRC],
        ),
        PlainItem(
            heading="Reassessment of waiting patients",
            why="A patient triaged as stable can deteriorate while waiting -- reassessment at a fixed interval catches that before it becomes an emergency within an emergency.",
            body=[
                "Every patient waiting in the emergency area is "
                "reassessed at the interval set by the adopted triage "
                "scale. Under CTAS, this is: Level 1 (Resuscitation) -- "
                "continuous care, not a periodic check; Level 2 "
                "(Emergent) -- every 15 minutes; Level 3 (Urgent) -- "
                "every 30 minutes; Level 4 (Less Urgent) -- every 60 "
                "minutes; Level 5 (Non-Urgent) -- every 120 minutes.",
                "Any deterioration found on reassessment is escalated to "
                "the Duty Doctor immediately and the patient's triage "
                "category is upgraded if warranted.",
                "Each reassessment, including a nil-change reassessment, "
                "is time-stamped and recorded.",
            ],
            oe_code="COP.2.d",
            technical_sources=[CTAS_SRC],
        ),
        PlainItem(
            heading="Disposition and emergency discharge note",
            why="Every emergency visit must end with a clear decision -- admit, refer, or discharge -- and a written note the patient (or the next provider) can actually use.",
            body=[
                "The Duty Doctor records the final disposition (admitted "
                "/ referred out / discharged / left against medical "
                "advice / absconded / brought dead) for every emergency "
                "patient.",
                "A discharged patient receives a written emergency "
                "discharge note, in a language the patient "
                "understands, covering four things:",
                "1. The diagnosis.",
                "2. The treatment given.",
                "3. The condition at discharge.",
                "4. Follow-up or red-flag instructions.",
                "A referred-out patient's note additionally states the "
                "reason for referral and the receiving facility.",
            ],
            oe_code="COP.2.e",
        ),
        PlainItem(
            heading="Emergency-care quality programme",
            why="The hospital has to know, not just assume, that its emergency care is actually working -- a periodic look at its own numbers and cases is how it finds out.",
            body=[
                "The hospital's defined emergency QA indicators (such as "
                "triage-to-doctor time, MLC documentation completeness, "
                "brought-dead rate) are tracked on the hospital's "
                "defined review frequency.",
                "Findings are reviewed by the hospital's defined quality "
                "forum and any corrective action is tracked to closure.",
                "A sample of emergency records, including every "
                "brought-dead and death-within-minutes case, is reviewed "
                "as part of this programme.",
            ],
            oe_code="COP.2.f",
        ),
        PlainItem(
            heading="Dead on arrival and death within minutes of arrival",
            why="A patient who is brought dead, or who dies within minutes of arrival, needs its own clear process -- for the family's sake, for medico-legal correctness, and so the hospital can honestly review whether anything could have gone differently.",
            body=[
                "The Duty Doctor certifies death following the "
                "hospital's defined death-certification process, noting "
                "the time of arrival and time of death (or that the "
                "patient was brought dead).",
                "Where the death is unnatural, unexplained, or otherwise "
                "meets the hospital's MLC criteria, the police are "
                "informed and the case is documented as an MLC.",
                "Every brought-dead and death-within-minutes case is "
                "logged and reviewed as part of the emergency-care "
                "quality programme, with the family informed and "
                "supported per the hospital's defined breaking-bad-news "
                "process.",
            ],
            oe_code="COP.2.g",
            technical_sources=[BNSS_194_SRC],
        ),
        PlainItem(
            heading="Ambulance access commensurate with the hospital's scope",
            why="An ambulance only helps if it is actually available when needed, matched to the kind of patients and distances the hospital realistically has to move.",
            body=[
                "The hospital provides ambulance access -- owned, "
                "shared, or through a verified tie-up arrangement -- "
                "commensurate with the hospital's defined scope of "
                "services and typical transfer distances.",
                "The arrangement (owned vehicle details, or the tie-up "
                "agreement and contact details) is documented and kept "
                "current.",
                "Response-time expectations for the arrangement are "
                "defined and tracked.",
            ],
            oe_code="COP.2.h",
        ),
        PlainItem(
            heading="Ambulance fitness, equipment and medications",
            why="An ambulance that cannot start, or that is missing its oxygen or emergency drugs, is not actually ambulance access -- it has to be checked, not assumed.",
            body=[
                "The ambulance (where hospital-owned) is checked for "
                "roadworthiness, fuel, and cleanliness on the hospital's "
                "defined checking frequency (each shift or each day, for "
                "example).",
                "Required equipment (oxygen, suction, stretcher, "
                "resuscitation equipment) and medications are checked "
                "present, in date, and functional on the same schedule.",
                "Any defect or expired item found is replaced or "
                "repaired before the ambulance is next used, and this is "
                "recorded.",
            ],
            oe_code="COP.2.i",
        ),
        PlainItem(
            heading="Treatment initiated during transit",
            why="Transit time is treatment time -- a patient's condition should not simply be monitored on the way to or from the hospital when something can be started for them instead.",
            body=[
                "Staff accompanying a transfer are trained and equipped "
                "to begin appropriate treatment (oxygen, IV fluids, "
                "basic life support, for example) during transit, within "
                "their scope of training.",
                "Treatment initiated in transit, and the patient's "
                "condition en route, is documented on a transit/run "
                "sheet and handed over to the receiving team.",
                "Any deterioration in transit is escalated per the "
                "hospital's defined in-transit escalation process.",
            ],
            oe_code="COP.2.j",
        ),
        PlainItem(
            heading="Documented plan for disaster, epidemic and community emergencies",
            why="A hospital that only plans for the patients walking in on an ordinary day will not cope the day a flood, fire, epidemic, or mass-casualty event sends many more at once -- a written, drilled plan is what prevents chaos on that day.",
            body=[
                "The hospital maintains a written disaster/epidemic/"
                "community-emergency management plan covering the "
                "hospital's defined hazard list (fire, flood, mass-"
                "casualty influx, epidemic/outbreak, for example), "
                "consistent with directions issued by the National, "
                "State or District Disaster Management Authority and, "
                "during a notified epidemic, by the Central or State "
                "Government under the Epidemic Diseases Act.",
                "The plan defines surge capacity, roles, an internal and "
                "external communication tree, and how the hospital "
                "receives and acts on official disaster or epidemic "
                "directions.",
                "The plan is tested through a mock drill at least "
                "annually, the drill is documented, and the plan is "
                "revised based on what the drill or a real activation "
                "showed.",
            ],
            oe_code="COP.2.k",
            technical_sources=[DISASTER_ACT_SRC, EPIDEMIC_ACT_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-10 (see the COP.2 Records folder).",
    related_documents=[
        "Policy on Emergency Services, Ambulance and Management of Disasters (COP.2)",
        "SOP — Uniform Care Across Settings and Telemedicine (COP.1)",
        "Hospital's Disaster/Epidemic/Community-Emergency Management Plan",
    ],
    review_text=(
        "This SOP is reviewed annually, after any disaster-plan drill or "
        "activation, or sooner if a brought-dead/death-within-minutes "
        "review or an emergency-QA finding shows it needs to change."
    ),
    full_reference_list=[
        NABH_COP_CITE.format(code="COP.2"),
        BNSS_397_SRC,
        BNSS_194_SRC,
        DISASTER_ACT_SRC,
        EPIDEMIC_ACT_SRC,
        CTAS_SRC,
    ],
)

# --------------------------------------------------------------- COP.3 ---
COP3 = SOPSpecV2(
    sop_no="SOP-COP.3",
    title="Cardio-Pulmonary Resuscitation",
    purpose_plain=(
        "This SOP sets out how the hospital provides a resuscitation "
        "service at every hour, how assigned roles and the event record "
        "work during a resuscitation, how resuscitation equipment and "
        "medications are kept ready in the areas that need them, and how "
        "every resuscitation is analysed by a multidisciplinary committee "
        "with corrective and preventive action taken on the findings."
    ),
    purpose_trigger=(
        "A patient arrests at 3 a.m. This SOP is what guarantees a "
        "trained team responds with assigned roles and a working, fully "
        "stocked trolley, exactly as it would at 3 p.m. -- not a thinner, "
        "improvised response because it's the night shift."
    ),
    purpose_why=(
        "We do this because a resuscitation service that only exists "
        "during the day shift is not a resuscitation service, and because "
        "if everyone who runs to a crash does whatever they personally "
        "think is useful, the team works against itself -- assigned "
        "roles, actually followed, are what make a crash team a team."
    ),
    purpose_text=(
        "To define how the hospital provides a resuscitation service at "
        "every hour, assigns roles and records the event, keeps "
        "resuscitation equipment and medications ready, and analyses "
        "every resuscitation for corrective and preventive action."
    ),
    scope_why="so every location where a patient may need resuscitation, and every staff member who might respond, follows the same standard.",
    scope_text=(
        "Applies to every location in the hospital where a patient may "
        "require cardio-pulmonary resuscitation, to the staff who "
        "respond and who record the event, to the staff who check and "
        "restore the resuscitation kit, and to the multidisciplinary "
        "committee that reviews every event."
    ),
    responsibility_why="a trolley nobody checked, or an event nobody reviewed, is the gap that turns a close call into an actual loss next time.",
    responsibilities=[
        ("Head of the Institution", "Is accountable for a resuscitation service existing at all times, for kits actually present in every named area, and for every event being analysed."),
        ("Named Responders", "Attend when summoned at any hour, fill the assigned role given to them at the event, and complete the event record."),
        ("Nursing / Clinical Staff in Each Named Area", "Check the resuscitation kit on the defined schedule, send used reusable items for reprocessing, and restore the kit to ready before the next event."),
        ("Multidisciplinary Resuscitation-Review Committee", "Analyses every resuscitation event, including ones that did not restore circulation, and assigns corrective and preventive actions."),
        ("Quality/Accreditation Coordinator", "Audits a sample of resuscitation records, kit checks and committee actions on the defined interval and reports findings to the Head of the Institution."),
    ],
    items=[
        PlainItem(
            heading="Resuscitation service available at all times",
            why="A resuscitation service that only exists during the day shift is not a resuscitation service -- a patient can deteriorate at 3 a.m. just as easily as at 3 p.m.",
            body=[
                "The hospital's defined response arrangement -- who "
                "responds, how they are summoned (code announcement, "
                "emergency extension), and the arrangement when the "
                "ordinary responding team is already occupied -- applies "
                "at every hour of every day, including nights, weekends "
                "and holidays.",
                "Every named responder's professional registration is "
                "verified under the hospital's human-resource "
                "credentialing process before they are placed on the "
                "responder list.",
            ],
            oe_code="COP.3.a",
            boundary=[
                "Where the cardiac-arrest recognition and the initial "
                "call come from the hospital's early-warning/"
                "deterioration process, this SOP owns what happens once "
                "the call is made -- it does not restate how "
                "deterioration is recognised.",
            ],
        ),
        PlainItem(
            heading="Assigned roles during the event, and the event record",
            why="If everyone who runs to a crash does whatever they personally think is useful, the team works against itself -- assigned roles, actually followed, are what make a crash team a team.",
            body=[
                "The hospital's defined resuscitation roles (team "
                "leader, airway, compressions, medications, documenter, "
                "timekeeper, for example) and how a role is allocated to "
                "a specific person are followed at every resuscitation.",
                "The event is recorded against the patient's unique "
                "identification number as it happens or immediately "
                "after, covering seven things:",
                "1. The time the event was recognised.",
                "2. The time the team was summoned.",
                "3. The time the team arrived.",
                "4. Roles filled.",
                "5. Interventions performed.",
                "6. Medications given (as given, not as a printed dose "
                "table).",
                "7. The outcome.",
                "The completed event record is filed within the same "
                "shift.",
            ],
            oe_code="COP.3.b",
        ),
        PlainItem(
            heading="Resuscitation equipment and medications ready in named areas",
            why="A resuscitation trolley is only useful if it is actually complete and in the room when it is needed -- checking it has to be routine, not assumed.",
            body=[
                "A resuscitation kit is held in every hospital-defined "
                "area (emergency area, every in-patient ward, day-care, "
                "OT and recovery, any high-dependency area, for "
                "example).",
                "Each kit's contents are checked against the defined "
                "contents list on the defined checking frequency, and "
                "any missing, expired or non-functional item is replaced "
                "before the next shift.",
                "After an event, used reusable items (resuscitation "
                "bags, laryngoscope blades and handles, related airway "
                "devices) are sent for reprocessing and are not returned "
                "to the trolley until reprocessing is complete; the kit "
                "is then restored to ready and the restoration is "
                "recorded.",
            ],
            oe_code="COP.3.c",
        ),
        PlainItem(
            heading="Multidisciplinary post-event analysis and corrective action",
            why="An unreviewed resuscitation -- even a successful one -- is a missed chance to find out what almost went wrong before it actually does.",
            body=[
                "The resuscitation-review committee reviews every "
                "cardio-pulmonary resuscitation event, including events "
                "that did not restore circulation.",
                "The review uses the event record and the kit-check "
                "record for that event, and identifies any gap in "
                "response time, role compliance, documentation, or kit "
                "readiness.",
                "Corrective and preventive actions are assigned to a "
                "named person with a due date, and are tracked to "
                "closure; an action that is written down but not done is "
                "not treated as complete.",
            ],
            oe_code="COP.3.d",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the COP.3 Records folder).",
    related_documents=[
        "Policy on Cardio-Pulmonary Resuscitation (COP.3)",
        "SOP — Emergency Services, Ambulance and Management of Disasters (COP.2)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a failed call, an "
        "incomplete kit, or an unreviewed event exposes a gap, or if the "
        "assessment, emergency-care, sterilisation or infection-control "
        "processes this SOP hands work to are revised."
    ),
    full_reference_list=[NABH_COP_CITE.format(code="COP.3")],
)

# --------------------------------------------------------------- COP.4 ---
COP4 = SOPSpecV2(
    sop_no="SOP-COP.4",
    title="Nursing Care",
    purpose_plain=(
        "This SOP sets out how nursing care is aligned with the overall "
        "patient-care plan and documented in the patient record; how "
        "patient care is assigned to a nurse for a given period; how the "
        "equipment nurses need is kept available; and how nursing "
        "clinical practice guidelines -- distinct from the hospital's "
        "medical protocols -- are developed, issued and actually used."
    ),
    purpose_trigger=(
        "A patient has no nurse clearly assigned to them for the current "
        "shift. This SOP is what makes that gap visible immediately -- "
        "the assignment is recorded and visible on the ward -- rather "
        "than discovered only when something goes wrong."
    ),
    purpose_why=(
        "We do this because nursing care that happens but is never "
        "written down is invisible to the next shift, the treating "
        "doctor, and anyone reviewing the case later -- and a nurse who "
        "has to search another ward for a working thermometer or infusion "
        "pump is not providing efficient care, whatever the written "
        "guidance says."
    ),
    purpose_text=(
        "To define how nursing care is aligned, integrated and "
        "documented in the patient record; how patient care is assigned; "
        "how nursing equipment is kept available; and how nursing "
        "clinical practice guidelines are developed, issued and used."
    ),
    scope_why="so every setting a nurse works in -- OPD, wards, theatre, ICU -- follows the same documentation and assignment standard.",
    scope_text=(
        "Applies to every setting in which a nurse of the hospital "
        "provides care: the out-patient department, day-care, every "
        "in-patient ward, the emergency area, the operation theatre and "
        "recovery, intensive or high-dependency areas, and any procedure "
        "or labour room."
    ),
    responsibility_why="nursing care that is given but never documented, or equipment that nobody tracks, is a gap that surfaces only when a patient is harmed by it.",
    responsibilities=[
        ("Head of the Institution", "Is accountable for nursing care being documented, assigned by current good practice, properly equipped, and guided by nursing clinical practice guidelines that are actually used."),
        ("Nursing Administration", "Authors and keeps current the nursing clinical practice guidelines, holds the assignment method, and tracks nursing-equipment shortfalls to closure."),
        ("Nurse in Charge of Each Area", "Assigns nursing care for the current period, keeps the current nursing guideline available in that area, and does not count missing or un-reprocessed equipment as available."),
        ("Nurses", "Write the nursing entry in the patient record for every patient they care for, follow the current nursing guideline, and do not treat handover as a substitute for the entry."),
        ("Quality/Accreditation Coordinator", "Audits nursing entries, assignment records, equipment reports and guideline currency on the defined interval and reports findings to the Head of the Institution."),
    ],
    items=[
        PlainItem(
            heading="Nursing care aligned, integrated and documented in the patient record",
            why="Nursing care that happens but is never written down is invisible to the next shift, the treating doctor, and anyone reviewing the case later -- the record is the only place it actually survives.",
            body=[
                "Every nurse writes a nursing entry in the patient record "
                "-- against the patient's unique identification number "
                "-- stating the observations made, the care given, the "
                "patient's response, and how that care connects to the "
                "current overall care plan and to the condition-specific "
                "clinical protocol, where one applies.",
                "The hospital's defined nursing-entry content, form or "
                "fields, and expected timing are followed for every "
                "entry.",
                "A Kardex, whiteboard, or messaging-app update is never "
                "treated as the patient record, and copying forward "
                "yesterday's entry as if it were today's observation is "
                "not permitted.",
            ],
            oe_code="COP.4.a",
        ),
        PlainItem(
            heading="Assignment of patient care",
            why="A patient without a nurse clearly assigned to them for the current period is a gap in care that nobody notices until something goes wrong.",
            body=[
                "The hospital's defined assignment process -- who "
                "assigns nursing care, for which period, and on what "
                "basis -- is followed for every patient, using current "
                "good clinical and nursing practice as the basis for "
                "assignment, not a fixed roster that ignores the "
                "patient's current condition or the nurse's skill.",
                "Assignment uses the nurse's professional registration "
                "as already verified under the hospital's human-resource "
                "credentialing process.",
                "The assignment for the current period is recorded and "
                "is visible to staff on the ward.",
            ],
            oe_code="COP.4.b",
        ),
        PlainItem(
            heading="Equipment for safe and efficient nursing services",
            why="A nurse who has to search another ward for a working thermometer or an infusion pump is not providing efficient care -- the equipment has to actually be there.",
            body=[
                "The hospital's defined nursing equipment, by area, and "
                "how its absence or failure is reported, is followed in "
                "every area that provides nursing care.",
                "A reusable item is counted as available only after it "
                "has been reprocessed; an item that is missing, failed, "
                "or still awaiting reprocessing is not counted as "
                "available.",
                "Any equipment shortfall reported by a nurse is logged "
                "and tracked to resolution.",
            ],
            oe_code="COP.4.c",
        ),
        PlainItem(
            heading="Nursing clinical practice guidelines reflecting current standards",
            why="A nurse following the medical diagnosis protocol with no nursing-specific guidance has a pathway for the disease but no standard for the nursing work around it -- that gap is what this step closes.",
            body=[
                "The hospital's defined nursing clinical practice "
                "guidelines in current use, the nursing problems or "
                "processes each one covers, and where they are held, is "
                "followed -- each guideline is distinct from the "
                "hospital-wide medical protocols, and a medical protocol "
                "relabelled as a nursing guideline does not satisfy this "
                "step.",
                "A new or revised guideline is issued to every setting "
                "that gives that care, and the previous version is "
                "withdrawn from those settings on the same date.",
                "A nurse applying an undated or personal routine instead "
                "of the current guideline is treated as a defect to be "
                "corrected.",
            ],
            oe_code="COP.4.d",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the COP.4 Records folder).",
    related_documents=[
        "Policy on Nursing Care (COP.4)",
        "SOP — Cardio-Pulmonary Resuscitation (COP.3)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a missing nursing "
        "entry, an unassigned patient, a missing piece of equipment, or "
        "an unused guideline exposes a gap, or if the continuity-of-care, "
        "assessment, uniform-care, infection-control or information-"
        "management processes this SOP hands work to are revised."
    ),
    full_reference_list=[NABH_COP_CITE.format(code="COP.4")],
)

# --------------------------------------------------------------- COP.5 ---
COP5 = SOPSpecV2(
    sop_no="SOP-COP.5",
    title="Transfusion of Blood and Blood Components",
    purpose_plain=(
        "This SOP sets out how transfusion services are kept aligned with "
        "the hospital's defined scope and governed by law; how a unit is "
        "safely matched and administered to the correct patient at the "
        "bedside; how blood and blood components are used rationally "
        "rather than by habit; how consent for transfusion and for "
        "donation is obtained; how emergency availability of blood is "
        "defined, measured and acted on; and how every reaction is "
        "captured and analysed."
    ),
    purpose_trigger=(
        "A nurse at the bedside checks the two identifiers against the "
        "issue slip and finds a mismatch. This SOP is what makes that an "
        "automatic stop -- the unit is not hung, and the mismatch is "
        "recorded as an incident -- not a judgement call under time "
        "pressure."
    ),
    purpose_why=(
        "We do this because a correctly grouped unit given to the wrong "
        "patient is, in every way that matters, an incompatible "
        "transfusion -- the blood bank cannot see the vein; only the "
        "person at the bedside can, and that is why this check is "
        "non-negotiable."
    ),
    purpose_text=(
        "To define how transfusion services stay aligned with scope and "
        "law, how a unit is safely matched at the bedside, how blood is "
        "used rationally, how consent is obtained, how emergency "
        "availability is measured, and how reactions are captured and "
        "analysed."
    ),
    scope_why="so every location where blood is requested, issued, stored, administered or followed up follows the same safety standard.",
    scope_text=(
        "Applies to every location in the hospital where blood or a "
        "blood component is requested, issued, transported, stored "
        "pending transfusion, administered, or followed up after "
        "administration."
    ),
    responsibility_why="an unlicensed source, a missed bedside check, or an unanalysed reaction is a direct risk to the patient, not a documentation shortfall.",
    responsibilities=[
        ("Person in Charge of Transfusion Services", "Keeps the transfusion scope and blood bank licence evidence current, holds the safe-transfusion and rational-use guidance, holds the emergency-availability arrangement, and stops issue of any non-emergency unit with no recorded indication."),
        ("Requesting Clinician", "Records the clinical indication for every non-emergency request, considers non-transfusion alternatives, obtains transfusion consent, and remains responsible for the decision to transfuse."),
        ("Staff Who Administer the Transfusion", "Perform the bedside identity check before hanging any unit, monitor the patient, stop the transfusion immediately if a reaction is suspected, and complete the administration record and the post-transfusion form."),
        ("Quality/Accreditation Coordinator", "Audits transfusion records, bedside identity-check compliance, emergency-availability performance, and reaction analysis on the defined interval, and reports findings to the Head of the Institution."),
        ("Head of the Institution", "Is accountable for transfusion services matching the hospital's defined scope, for every unit coming from a licensed source, and for emergency availability that is both defined and actually measured."),
    ],
    items=[
        PlainItem(
            heading="Transfusion services commensurate with defined services, governed by law",
            why="A hospital that transfuses blood without a licensed source behind it is not running a transfusion service -- it is taking an uncontrolled risk with a human tissue product.",
            body=[
                "The hospital's defined transfusion scope -- the "
                "components used, the clinical areas in which "
                "transfusion is performed, the hours a unit can be "
                "obtained, and whether supply is from a licensed "
                "in-house blood centre, a documented arrangement with a "
                "licensed blood bank, or both -- is kept current and "
                "aligned with the hospital's defined service directory.",
                "Every unit transfused is issued by a blood bank or "
                "blood centre licensed under the Drugs and Cosmetics "
                "Act, 1940 and the Drugs and Cosmetics Rules, 1945; "
                "current licence evidence for that source is kept on "
                "file and checked before renewal expiry.",
                "An unlicensed source is never used, even in an "
                "emergency; the emergency-availability arrangement only "
                "ever points to a licensed source.",
            ],
            oe_code="COP.5.a",
            technical_sources=[BLOOD_BANK_SRC],
        ),
        PlainItem(
            heading="Safe transfusion — the bedside identity check",
            why="A correctly grouped unit given to the wrong patient is, in every way that matters, an incompatible transfusion -- the blood bank cannot see the vein; only the person at the bedside can, and that is why this check is non-negotiable.",
            body=[
                "A transfusion request carries six things:",
                "1. The patient's unique identification number.",
                "2. The patient's name.",
                "3. The component requested.",
                "4. The recorded indication.",
                "5. The date/time.",
                "6. The requesting clinician.",
                "A unit is not issued against a nameless verbal "
                "request except through the documented emergency "
                "pathway.",
                "The pre-transfusion sample is collected and identified "
                "with the unique identification number on the sample "
                "matching the request; a unit that is leaking, clotted, "
                "discoloured, expired, or stored outside the defined "
                "conditions is never transfused -- it is returned to the "
                "issuing source with the reason recorded.",
                "Before hanging any unit, the person administering it "
                "checks, in the presence of the patient, the hospital's "
                "two identifiers against the issue slip and the bag "
                "label -- never against a bed number alone and never "
                "from the nursing station; a mismatch means the unit is "
                "not hung, and the mismatch is recorded as an incident, "
                "not filed away as paperwork.",
            ],
            oe_code="COP.5.b",
        ),
        PlainItem(
            heading="Rational use of blood and blood components",
            why="A safely hung unit the patient never needed is still a unit of real risk -- infection, overload, alloimmunisation -- given for no reason, and it is a unit another patient may have needed instead.",
            body=[
                "Every non-emergency request carries a recorded clinical "
                "indication, written before the unit is issued, drawn "
                "from the hospital's own written clinical-indication "
                "list for each component -- no haemoglobin, platelet or "
                "INR number is treated here as a national mandate; this "
                "hospital's own reviewed list is what is used.",
                "Before a non-emergency request is sent, the requesting "
                "clinician records whether a non-transfusion alternative "
                "was considered, and a further unit is not requested "
                "without reviewing whether the first unit achieved its "
                "purpose.",
                "A non-emergency unit with no recorded indication is "
                "refused by the person releasing it from the clinical "
                "side, and the refusal is recorded; a standing order to "
                "simply 'keep the haemoglobin up' is not accepted as an "
                "indication.",
            ],
            oe_code="COP.5.c",
        ),
        PlainItem(
            heading="Informed consent for transfusion and for donation",
            why="A patient who is transfused without having agreed to it, or a donor who is bled without having agreed to it, has had a decision about their own body made for them -- consent is what prevents that.",
            body=[
                "Consent for transfusion is obtained before the unit is "
                "hung; where a documented emergency makes prior consent "
                "impossible, the record states why, and consent is "
                "completed as soon as the emergency allows.",
                "If donation is performed on this site, consent for "
                "donation is obtained before blood is collected from the "
                "donor; if donation is not performed on this site, that "
                "is this hospital's documented position and the "
                "licensed blood centre's own act, not this hospital's.",
                "Transfusion consent and donation consent are never "
                "treated as the same form or the same act.",
            ],
            oe_code="COP.5.d",
        ),
        PlainItem(
            heading="Emergency availability within a defined time frame",
            why="An emergency unit that arrives after the bleeding has already cost the patient their chance has not been 'made available' in any sense that matters -- a time frame that is defined but never measured is just a sentence in a policy.",
            body=[
                "The hospital's defined time frame within which blood or "
                "a blood component is available in an emergency, by "
                "component, and the clock it is measured from, is "
                "written down -- not stated as 'as soon as possible' "
                "with no number, and not borrowed from another "
                "hospital.",
                "The hospital's defined emergency-availability "
                "arrangement is followed; the bedside identity check "
                "still happens before the unit is hung, even in this "
                "pathway -- an emergency never cancels that check.",
                "Actual emergency-availability time is measured against "
                "the defined time for every emergency unit issued, and "
                "reviewed at the defined interval; if the defined time "
                "will be missed, the treating clinician is told before "
                "it elapses, with the reason and the next action.",
            ],
            oe_code="COP.5.e",
        ),
        PlainItem(
            heading="Post-transfusion form, reactions and analysis",
            why="A reaction that is treated at the bedside and never written up or reviewed teaches the hospital nothing, and the next patient gets no benefit from what almost went wrong this time.",
            body=[
                "The post-transfusion form is collected for every unit "
                "transfused; a unit whose form is not collected is "
                "treated as a unit whose outcome is unknown.",
                "A suspected reaction -- identified from monitoring, the "
                "patient's own report, or a later finding -- is "
                "immediately managed (transfusion stopped, set retained "
                "until the work-up is decided, treating clinician "
                "called) and is then captured on the form.",
                "Every identified reaction is analysed, with a recorded "
                "conclusion and, where needed, a corrective or "
                "preventive action with an owner and due date; a serious "
                "reaction is analysed when it occurs, not held for a "
                "later meeting.",
            ],
            oe_code="COP.5.f",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the COP.5 Records folder).",
    related_documents=[
        "Policy on Transfusion of Blood and Blood Components (COP.5)",
        "SOP — Uniform Care Across Settings and Telemedicine (COP.1)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a wrong-unit event, "
        "a missed emergency unit, or an unanalysed reaction exposes a "
        "gap, or if the laboratory, biomedical-waste, infection-control, "
        "uniform-care or registration processes this SOP hands work to "
        "are revised."
    ),
    full_reference_list=[NABH_COP_CITE.format(code="COP.5"), BLOOD_BANK_SRC],
)

# --------------------------------------------------------------- COP.6 ---
COP6 = SOPSpecV2(
    sop_no="SOP-COP.6",
    title="Care in Intensive Care and High Dependency Units",
    purpose_plain=(
        "This SOP sets out how the ICU and HDU admit and discharge "
        "patients against written criteria, how a bed shortage in those "
        "units is handled, how care is backed by written guidance, "
        "adequate staff and equipment, how infection-control practices "
        "are applied in these units, how a quality-assurance programme is "
        "run, how patients and families are counselled through the stay, "
        "and how end-of-life care is provided consistently and lawfully."
    ),
    purpose_trigger=(
        "A family has heard nothing from the ICU team except at "
        "admission, and now a decision about withdrawing treatment is "
        "being raised for the first time. This SOP is what requires "
        "periodic counselling through the whole stay -- so the family is "
        "never ambushed by a decision they were never prepared for."
    ),
    purpose_why=(
        "We do this because an ICU or HDU bed is a scarce resource, not a "
        "location -- a patient admitted who cannot benefit occupies the "
        "bed of one who can -- and because an end-of-life decision made "
        "as an unwritten corridor agreement, with no record of who "
        "decided or why, is a decision the hospital cannot later show was "
        "lawful, consistent, or even made at all."
    ),
    purpose_text=(
        "To define how the ICU and HDU admit and discharge patients "
        "against written criteria, handle a bed shortage, apply "
        "infection-control practices, run a quality-assurance programme, "
        "counsel patients and families, and provide end-of-life care."
    ),
    scope_why="so every staff member who admits to, cares for, discharges from, or counsels a family about these units follows the same standard.",
    scope_text=(
        "Applies to the intensive care unit and the high dependency "
        "unit, where the hospital operates them, and to every staff "
        "member who admits to, cares for a patient in, discharges from, "
        "or counsels a family about those units."
    ),
    responsibility_why="a bed occupied by the wrong patient, an infection practice never actually applied, or an undocumented end-of-life decision are each a failure the hospital cannot defend later.",
    responsibilities=[
        ("Person in Charge of the ICU/HDU", "Holds and applies the admission/discharge criteria and the bed-shortage procedure, keeps the unit's written guidance (including its infection-control section) current, keeps staffing and equipment adequate, and applies the end-of-life pathway."),
        ("Named Quality Lead for Critical Care", "Operates the unit's quality-assurance programme, receives infection figures as inputs rather than re-defining them, and reports findings to the defined forum."),
        ("Requesting/Treating Clinicians", "Apply the admission criteria rather than treating an early-warning trigger as automatic admission, counsel the patient/family periodically, and follow the written end-of-life pathway rather than an undocumented conversation."),
        ("Nursing Staff of the Unit", "Follow the unit's written guidance and the hospital's infection-control practices as documented in that guidance, and complete counselling and end-of-life documentation."),
        ("Quality/Accreditation Coordinator", "Audits admission/discharge decisions, infection-control documentation, QA review records, counselling notes and end-of-life records on the defined interval, reporting to the Head of the Institution."),
    ],
    items=[
        PlainItem(
            heading="Admission/discharge criteria and the bed-shortage procedure",
            why="An ICU or HDU bed is a scarce resource, not a location -- a patient admitted who cannot benefit occupies the bed of one who can, and a patient refused without the shortage procedure is a refusal of care the hospital holds out.",
            body=[
                "The hospital's written admission criteria for the ICU "
                "and, separately, for the HDU are the criteria actually "
                "used to decide every request from a ward, the emergency "
                "area, or the operation theatre -- not a courtesy "
                "admission because a bed happens to be free.",
                "The hospital's written discharge criteria from the ICU "
                "and HDU to a lower level of care govern every unit "
                "discharge; a patient leaves the unit because the "
                "criteria are met, not because a new admission needs the "
                "bed with no reason written.",
                "When the unit has no bed for a patient who meets the "
                "admission criteria, the hospital's defined bed-shortage "
                "procedure -- who decides, the options in order, and how "
                "the decision is recorded -- is followed; this is never "
                "left to an unnamed corridor arrangement.",
            ],
            oe_code="COP.6.a",
        ),
        PlainItem(
            heading="Written guidance, adequate staff and equipment",
            why="Care in a critical-care unit that is not actually backed by written guidance, enough trained staff, and working equipment is a claim, not a service.",
            body=[
                "The hospital's written guidance for care in the ICU and "
                "HDU, covering at least monitoring, equipment use, and "
                "nursing/medical work, is held and followed in each "
                "unit.",
                "The hospital's defined staffing of each unit, including "
                "out of hours, is maintained at a level adequate for the "
                "care the unit's own admission criteria claim, using "
                "registration already verified under human-resource "
                "credentialing.",
                "The hospital's defined equipment inventory of each unit "
                "is kept current; equipment that is out of service is "
                "never counted as backing a service the unit still "
                "claims, and if a claimed service genuinely cannot be "
                "delivered it is suspended and requesting clinicians are "
                "told.",
            ],
            oe_code="COP.6.b",
        ),
        PlainItem(
            heading="Infection-control practices documented in the unit's own guidance and followed",
            why="A hospital can have excellent infection-control policies and still infect its ventilated patients if the ICU's own guidance never actually names and applies them -- this step closes that gap without creating a second, drifting bundle book.",
            body=[
                "The unit's written guidance contains an infection-"
                "control section that names -- and does not reprint "
                "-- the hospital's existing requirements. It covers "
                "three things:",
                "1. Hand hygiene, standard and transmission-based "
                "precautions and PPE requirements.",
                "2. The device bundles that apply to patients in "
                "this unit (ventilator, central-line, "
                "urinary-catheter, and surgical-site where "
                "relevant).",
                "3. The surveillance the unit cooperates with.",
                "Those practices are actually followed in this unit -- "
                "hand hygiene at the required moments, transmission-"
                "based precautions when assigned, every eligible "
                "device's bundle elements performed, and device-day and "
                "other surveillance inputs supplied rather than guessed.",
                "If a practice this unit needs is missing from the "
                "hospital's infection-control policies, the gap is "
                "raised to the Infection Prevention and Control "
                "Committee for those policies to close -- it is never "
                "filled by inventing a local bundle in this unit's own "
                "guidance.",
            ],
            oe_code="COP.6.c",
            boundary=[
                "The hospital's infection-control SOPs (hand hygiene/"
                "PPE, device bundles, surveillance) are owned elsewhere "
                "(HIC chapter); this step owns only how this unit "
                "applies them, not how they are written.",
            ],
        ),
        PlainItem(
            heading="Quality-assurance programme for intensive and high-dependency care",
            why="A folder of critical-care indicators nobody discusses is a display, not assurance -- a programme has to actually have an owner, a forum, and actions that get closed.",
            body=[
                "The hospital's named quality lead for intensive and "
                "high-dependency care is accountable for the programme "
                "running and for reporting its findings.",
                "The hospital's defined quality indicators for the ICU/"
                "HDU are collected; infection rates, bundle-compliance "
                "figures and device-day denominators are received from "
                "the hospital's existing infection-control policies as "
                "inputs, never re-collected or re-defined under a second "
                "definition here.",
                "Indicators are reviewed at the defined forum and "
                "interval, and every review that identifies a problem "
                "produces a corrective or preventive action with an "
                "owner and a due date.",
            ],
            oe_code="COP.6.d",
        ),
        PlainItem(
            heading="Periodic counselling of the patient and/or family",
            why="A family that only hears from the unit when a decision to withdraw treatment is being asked for has not been counselled -- it has been ambushed.",
            body=[
                "The hospital's defined counselling arrangement -- who "
                "counsels, how often, and what is covered at a minimum "
                "-- is followed for every ICU/HDU stay, with counselling "
                "offered periodically through the stay -- not only at "
                "admission and not only when a withdrawal decision is "
                "being discussed.",
                "Where the patient can participate, the patient is "
                "included directly; where the patient cannot, the family "
                "is counselled in the patient's place.",
                "Each counselling episode is recorded against the "
                "patient's unique identification number, distinct from "
                "any end-of-life discussion.",
            ],
            oe_code="COP.6.e",
        ),
        PlainItem(
            heading="End-of-life care, consistent and legally consonant",
            why="An end-of-life decision made as an unwritten corridor agreement, with no record of who decided or why, is a decision the hospital cannot later show was lawful, consistent, or even made at all.",
            body=[
                "The hospital's written end-of-life pathway -- who may "
                "decide, how the decision is recorded, and where it is "
                "held -- is the single pathway used across the ICU, the "
                "HDU, and every other location of the hospital where a "
                "patient dies under its care -- not an intensive-care "
                "speciality invented at the last bed.",
                "Withholding or withdrawal of life-sustaining treatment, "
                "and the status of any advance directive, are handled in "
                "consonance with Common Cause v Union of India (2018); "
                "an informal family request or an undocumented 'comfort "
                "only' note is never treated as completing that legal "
                "process.",
                "Where brain-stem death declaration forms part of this "
                "hospital's pathway, it is certified by a Board of "
                "medical experts under the Transplantation of Human "
                "Organs and Tissues Act, 1994; counselling accompanies "
                "every application of this pathway, and a decision that "
                "resuscitation will not be attempted is recorded here "
                "rather than left unwritten.",
            ],
            oe_code="COP.6.f",
            technical_sources=[COMMON_CAUSE_SRC, THOA_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the COP.6 Records folder).",
    related_documents=[
        "Policy on Care in Intensive Care and High Dependency Units (COP.6)",
        "SOP — Transfusion of Blood and Blood Components (COP.5)",
        "Hospital's Infection-Control SOPs (hand hygiene/PPE, device bundles, surveillance)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if an off-criteria "
        "admission, a shortage handled without the procedure, an "
        "infection-control drift into a local bundle, or an undocumented "
        "end-of-life decision exposes a gap, or if the infection-control, "
        "bed-management, assessment, or continuity-of-care processes this "
        "SOP hands work to are revised."
    ),
    full_reference_list=[
        NABH_COP_CITE.format(code="COP.6"),
        COMMON_CAUSE_SRC,
        THOA_SRC,
    ],
)

# --------------------------------------------------------------- COP.7 ---
COP7 = SOPSpecV2(
    sop_no="SOP-COP.7",
    title="Safe Obstetric Care",
    purpose_plain=(
        "This SOP sets out how the hospital organises and safely provides "
        "antenatal, labour, birth and postnatal care; how high-risk "
        "obstetric cases are identified, cared for, and referred when "
        "needed; how maternal nutrition is included in every antenatal "
        "assessment; how peri-natal and post-natal monitoring is "
        "performed; and how neonatal backup and birth/stillbirth "
        "registration are handled for every birth at this hospital."
    ),
    purpose_trigger=(
        "A family asks an imaging technician to reveal the sex of the "
        "foetus. This SOP is what requires that request to be refused as "
        "a clinical act, with the refusal recorded -- never told, hinted "
        "at, or let slip, whatever the family asks."
    ),
    purpose_why=(
        "We do this because a labour room with a beautiful protocol on "
        "the wall and no one rostered to deliver that protocol at 3 a.m. "
        "is not a safe obstetric service, and because a woman's nutrition "
        "is not a lifestyle extra during pregnancy -- unaddressed anaemia "
        "and poor intake show up later as a haemorrhage or a low-"
        "birth-weight baby."
    ),
    purpose_text=(
        "To define how the hospital organises and safely provides "
        "antenatal, labour, birth and postnatal care; identifies, cares "
        "for and refers high-risk cases; includes maternal nutrition in "
        "antenatal assessment; monitors peri- and post-natally; and "
        "handles neonatal backup and birth registration."
    ),
    scope_why="so antenatal, labour, birth and postnatal staff all work from the same safety, nutrition and registration standard.",
    scope_text=(
        "Applies to the antenatal clinic, the labour room, the postnatal "
        "ward, the operation theatre insofar as a caesarean birth or "
        "obstetric procedure is performed there, the emergency area "
        "insofar as an obstetric emergency is received, and any "
        "high-dependency or intensive-care area that receives an "
        "obstetric patient."
    ),
    responsibility_why="a high-risk case handled by whoever is on duty, or a birth nobody registered, is a gap that surfaces only when it's too late to fix.",
    responsibilities=[
        ("Person in Charge of Obstetric Services", "Keeps the obstetric scope and written guidance current, holds the high-risk criteria and competent roster, holds the maternal-nutrition component, and holds the neonatal-backup arrangement."),
        ("Obstetric Doctors and Nurses", "Apply the written guidance, never determine or communicate a foetus's sex, include maternal nutrition in every antenatal assessment, identify high-risk cases, and do not conduct a high-risk birth the hospital cannot back with neonatal resources."),
        ("Staff Performing Antenatal Assessment", "Record a real maternal-nutrition history and risk assessment at every antenatal visit, not just a weight."),
        ("Neonatal Backup Team", "Is present and ready to receive the neonate at every high-risk obstetric birth that takes place at this hospital."),
        ("Quality/Accreditation Coordinator", "Audits obstetric scope alignment, sex-determination-prohibition compliance, high-risk identification/referral, antenatal nutrition records, monitoring records, neonatal-backup attendance, and birth/stillbirth registration on the defined interval."),
    ],
    items=[
        PlainItem(
            heading="Obstetric services organised and provided safely",
            why="A labour room with a beautiful protocol on the wall and no one rostered to deliver that protocol at 3 a.m. is not a safe obstetric service -- and a service that determines or lets slip the sex of a foetus has broken the law, not just a hospital rule.",
            body=[
                "The hospital's defined obstetric scope of services -- "
                "whether antenatal care, labour and birth (including "
                "instrumental and caesarean birth), postnatal care, and "
                "termination of pregnancy are provided, and the hours of "
                "each -- is kept aligned with the hospital's service "
                "directory, and the hospital's written obstetric "
                "guidance is the guidance actually followed in the "
                "labour room, not a poster.",
                "Antenatal care never determines or communicates the sex "
                "of a foetus -- not as an imaging report, not as an "
                "informal aside, and not on a family's request; a "
                "request to be told the sex is refused as a clinical "
                "act, and the refusal is recorded.",
                "Where termination of pregnancy is provided, it follows "
                "the hospital's defined MTP arrangement; where it is not "
                "provided, that is stated in the obstetric scope and the "
                "patient is referred.",
            ],
            oe_code="COP.7.a",
            technical_sources=[PCPNDT_SRC, MTP_SRC],
        ),
        PlainItem(
            heading="High-risk obstetric cases: identify, care, refer",
            why="A high-risk pregnancy that is never written down as high-risk gets the same casual handling as a routine one -- until it isn't routine anymore.",
            body=[
                "The hospital's written high-risk obstetric criteria are "
                "applied to every pregnancy and labour, and the "
                "identification is recorded in the antenatal or labour "
                "record, whichever comes first.",
                "A high-risk case that remains at this hospital is cared "
                "for only by the hospital's named competent roster of "
                "doctors and nurses for high-risk obstetric care -- "
                "never left to whoever happens to be on duty if they are "
                "not on that roster.",
                "Where this hospital cannot meet the need -- including "
                "where neonatal backup is not available -- the patient "
                "is referred to another appropriate centre before the "
                "need becomes an emergency, not after.",
            ],
            oe_code="COP.7.b",
        ),
        PlainItem(
            heading="Antenatal assessment includes maternal nutrition",
            why="A woman's nutrition is not a lifestyle extra during pregnancy -- unaddressed anaemia and poor intake show up later as a haemorrhage or a low-birth-weight baby, not as a line item someone forgot to fill in.",
            body=[
                "Every antenatal assessment includes the hospital's "
                "defined maternal-nutrition component -- at least "
                "dietary history, nutritional risk including anaemia "
                "risk, and the advice or supplementation offered; a "
                "recorded weight on its own is never treated as "
                "satisfying this requirement.",
                "The hospital's defined recording process is followed "
                "at every visit, distinct from any in-patient nutritional "
                "screen performed after admission, which does not "
                "substitute for it.",
                "Where the woman is referred to dietetics, the referral "
                "is recorded alongside, not instead of, the antenatal "
                "nutrition component.",
            ],
            oe_code="COP.7.c",
        ),
        PlainItem(
            heading="Peri-natal and post-natal monitoring",
            why="Labour and the hours right after birth are when a mother's condition can change fastest -- monitoring on a schedule, not on a hunch, is what catches that in time.",
            body=[
                "The hospital's defined peri-natal monitoring of the "
                "mother in labour and at birth, and post-natal "
                "monitoring after birth, are followed and recorded "
                "against the patient's unique identification number.",
                "The hospital's defined labour record (a partograph or "
                "other labour record, if used) documents the course of "
                "labour.",
                "Where the neonate is this hospital's patient, the "
                "neonatal backup team performs peri-natal and immediate "
                "post-natal monitoring of the neonate until paediatric "
                "care takes over; deterioration of the mother is "
                "escalated per the hospital's early-warning process and, "
                "where resuscitation is needed, the resuscitation SOP.",
            ],
            oe_code="COP.7.d",
        ),
        PlainItem(
            heading="Neonatal backup for high-risk cases, and birth registration",
            why="Taking on a high-risk birth without anyone able to receive the baby is not a shortcut -- it is a decision made for the neonate without the resources to back it.",
            body=[
                "Where this hospital cares for high-risk obstetric "
                "cases, the hospital's named human resources and "
                "facilities for neonates of high-risk cases are present "
                "and ready at the birth; if that backup is not available "
                "for a given case, the case is referred before birth "
                "whenever time allows.",
                "The hospital's defined process for registering live "
                "births and stillbirths is followed for every birth "
                "occurring at this hospital, distinct from the mother's "
                "and neonate's clinical discharge summary.",
                "This step does not write neonatal clinical care -- once "
                "the neonatal backup has received the baby, the "
                "hospital's paediatric-care SOP governs how the neonate "
                "is cared for.",
            ],
            oe_code="COP.7.e",
            technical_sources=[BIRTHS_DEATHS_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-5 (see the COP.7 Records folder).",
    related_documents=[
        "Policy on Safe Obstetric Care (COP.7)",
        "SOP — Care in Intensive Care and High Dependency Units (COP.6)",
        "Hospital's Imaging-Services Process (PC-PNDT registration)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a sex-determination "
        "incident, a high-risk birth without backup, a missing nutrition "
        "component, or an unregistered stillbirth exposes a gap, or if "
        "the imaging, paediatric, transfer, discharge or infection-"
        "control processes this SOP hands work to are revised."
    ),
    full_reference_list=[
        NABH_COP_CITE.format(code="COP.7"),
        MTP_SRC,
        PCPNDT_SRC,
        BIRTHS_DEATHS_SRC,
    ],
)

# --------------------------------------------------------------- COP.8 ---
COP8 = SOPSpecV2(
    sop_no="SOP-COP.8",
    title="Paediatric and Neonatal Services",
    purpose_plain=(
        "This SOP sets out how paediatric and neonatal services are "
        "organised honestly against what the hospital can actually "
        "deliver; how neonatal care follows a named guideline; how "
        "age-specific competency gates every assignment; what special-"
        "care provisions children actually receive; how nutrition, "
        "growth, development and immunisation are assessed at every "
        "paediatric encounter; and how the hospital matches every neonate "
        "to the right mother and responds immediately to a missing child "
        "or suspected abuse."
    ),
    purpose_trigger=(
        "Someone unfamiliar approaches the nursery to collect a newborn. "
        "This SOP is what requires staff to challenge that person and "
        "match the neonate to the mother or designated guardian before "
        "handover -- never handing a baby to whoever is simply standing "
        "closest to the cot."
    ),
    purpose_why=(
        "We do this because a neonate handed to whoever is standing "
        "closest to the cot, or a missing-child report that waits for "
        "staff to 'check again,' is exactly the failure this SOP exists "
        "to make impossible -- and professional registration alone does "
        "not make someone competent to care for a neonate; that "
        "competency has to be specifically verified."
    ),
    purpose_text=(
        "To define how paediatric and neonatal services are organised "
        "against actual capability; how neonatal care follows a named "
        "guideline; age-specific competency; special-care provisions; "
        "nutrition/growth/development/immunisation assessment; and "
        "abduction and abuse prevention and response."
    ),
    scope_why="so every location that cares for a child or neonate -- OPD, ward, nursery, labour room, emergency -- follows the same identification and safety standard.",
    scope_text=(
        "Applies to every location where the hospital cares for a child "
        "or neonate: the paediatric out-patient clinic, the paediatric "
        "ward or designated paediatric beds, the nursery or neonatal "
        "area, the labour room and postnatal ward insofar as the neonate "
        "is under care after birth, the emergency area when a child or "
        "neonate presents, and any procedure or day-care area that "
        "accepts a paediatric patient."
    ),
    responsibility_why="a child handed to the wrong person, or a missing child whose report waits for certainty, is a failure measured in minutes, not meetings.",
    responsibilities=[
        ("Person in Charge of Paediatric Services", "Keeps the paediatric/neonatal scope and written guidance current, names the neonatal guideline set, and holds the abduction-prevention and abuse-response methods."),
        ("Clinicians and Nurses Who Care for Children", "Apply the two identifiers and neonate-matching, apply the named neonatal guideline, complete the four-part paediatric assessment, and never hand a child to an unidentified person."),
        ("Human Resource Function", "Verifies age-specific paediatric/neonatal competency before any assignment and informs the person in charge of any lapse."),
        ("All Staff in Paediatric/Neonatal/Labour/Postnatal Areas", "Challenge an unidentified person before letting them near a child or neonate, and immediately escalate a missing child or a suspected-abuse concern -- never wait for certainty."),
        ("Quality/Accreditation Coordinator", "Audits scope alignment, identification/matching, neonatal-guideline consonance, competency assignment, special-care provisions, paediatric assessment completeness, and abduction/abuse records on the defined interval."),
    ],
    items=[
        PlainItem(
            heading="Organisation of paediatric services",
            why="A paediatric service that never says what it can't do forces a duty doctor to improvise at 2 a.m. instead of following a written plan.",
            body=[
                "The hospital's defined paediatric and neonatal scope "
                "of services names five things:",
                "1. The age range accepted.",
                "2. Whether, and at what level, neonates are cared "
                "for.",
                "3. Hours of availability.",
                "4. Conditions/procedures provided.",
                "5. Conditions stabilised and referred, with the "
                "destination.",
                "This scope is kept aligned with the hospital's "
                "service directory; a service not provided is named "
                "as not provided, with the referral destination.",
                "The hospital's defined paediatric and neonatal care "
                "areas and backing equipment are followed; adult "
                "equipment used on a child because the paediatric size "
                "is missing is treated as a defect, not a workaround.",
                "A child whose needs exceed the paediatric scope is "
                "stabilised and referred, with the decision, reason and "
                "destination recorded -- never held because transfer is "
                "inconvenient.",
            ],
            oe_code="COP.8.a",
        ),
        PlainItem(
            heading="Neonatal care in consonance with a named guideline",
            why="A laminated WHO poster on the nursery wall is not a guideline being followed -- if staff can't name which guideline governs their practice, they aren't practising in consonance with one.",
            body=[
                "The hospital's named national or international "
                "neonatal-care guideline set is the set staff can "
                "actually name and produce, not a general claim to "
                "'follow national guidelines.'",
                "The hospital's defined level of neonatal care provided "
                "-- routine newborn care, care of the sick neonate, or a "
                "stated limit -- and what is referred, matches the "
                "paediatric and neonatal scope; a level the guideline "
                "set and staffing cannot support is never claimed.",
                "Every neonate's care is recorded against the hospital's "
                "written local neonatal method derived from the named "
                "guideline, not left to whoever happens to be on duty "
                "that shift.",
            ],
            oe_code="COP.8.b",
        ),
        PlainItem(
            heading="Age-specific competency of those who care for children",
            why="Professional registration alone does not make someone competent to care for a neonate -- that competency has to be specifically verified for the age group they're assigned to.",
            body=[
                "The hospital's defined roles requiring age-specific "
                "paediatric or neonatal competency, and how that "
                "competency is demonstrated and recorded, is checked "
                "before anyone is assigned to care for a child or "
                "neonate.",
                "A person without the required age-specific competency "
                "is never assigned as the carer of that age group, even "
                "temporarily.",
                "The hospital's defined cover arrangement is used when a "
                "competent person is absent, rather than assigning "
                "whoever is available.",
            ],
            oe_code="COP.8.c",
        ),
        PlainItem(
            heading="Provisions for special care of children",
            why="A child left in an unmodified adult ward, with no family presence and no age-appropriate equipment, is being treated as a small adult -- which is exactly what this step exists to prevent.",
            body=[
                "The hospital's defined provisions for special care of "
                "children are actually provided, not just written "
                "down. These cover at least five things:",
                "1. The environment.",
                "2. Family presence.",
                "3. Feeding.",
                "4. Play or occupation.",
                "5. Privacy.",
                "Plus any other age-appropriate arrangement the "
                "hospital has defined.",
                "Where a child is placed in an adult ward because no "
                "dedicated paediatric ward exists, the provisions that "
                "still apply -- identification, family presence, "
                "age-appropriate equipment, and the abduction/abuse "
                "measures -- remain in force.",
                "Special-care provisions are checked periodically to "
                "confirm they are in actual use, not only on paper.",
            ],
            oe_code="COP.8.d",
        ),
        PlainItem(
            heading="Nutritional, growth, developmental and immunisation assessment",
            why="A child's growth curve, developmental milestones, and immunisation status are clinical findings, not optional extras to the main reason they came in.",
            body=[
                "Every paediatric assessment includes the hospital's "
                "defined tools for nutritional, growth, developmental "
                "and immunisation assessment, and the age groups to "
                "which each applies, recorded against the patient's "
                "unique identification number.",
                "A finding that requires action -- faltering growth, a "
                "missed immunisation, a developmental concern, "
                "nutritional risk -- is written into the care plan, not "
                "just noted and left there.",
                "Where the encounter is a brief emergency presentation, "
                "any element that cannot be completed is recorded as not "
                "done, with the reason, rather than left blank as if it "
                "had been done.",
            ],
            oe_code="COP.8.e",
        ),
        PlainItem(
            heading="Prevention of and response to child/neonate abduction and abuse",
            why="A neonate handed to whoever is standing closest to the cot, or a missing-child report that waits for staff to 'check again,' is exactly the failure this step exists to make impossible.",
            body=[
                "Every neonate is matched to the mother or designated "
                "guardian using the hospital's defined matching method "
                "in addition to the hospital's two identifiers -- a "
                "neonate is handed only to the matched mother/guardian, "
                "or to staff for a documented clinical reason, never to "
                "whoever is standing by the cot.",
                "A child is never handed to a person who has not been "
                "identified as entitled to take that child; access to "
                "the nursery and any restricted paediatric area follows "
                "the hospital's defined access-control rules, and staff "
                "challenge any unidentified person before they reach a "
                "child.",
                "If a child or neonate is missing, or an abduction "
                "attempt is suspected, the response is immediate and "
                "follows the hospital's defined missing-child response; "
                "when abuse or neglect is suspected, the concern is "
                "escalated and reported under the Juvenile Justice (Care "
                "and Protection of Children) Act, 2015 and, where a "
                "sexual offence is suspected, additionally under the "
                "Protection of Children from Sexual Offences Act, 2012 "
                "-- certainty is never the threshold for making that "
                "report.",
            ],
            oe_code="COP.8.f",
            technical_sources=[JJ_ACT_SRC, POCSO_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the COP.8 Records folder).",
    related_documents=[
        "Policy on Paediatric and Neonatal Services (COP.8)",
        "SOP — Safe Obstetric Care (COP.7)",
        "Hospital's Uniform-Care SOP (two identifiers) (COP.1)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a mismatched "
        "neonate, a missing child, a suspected-abuse case, or a late "
        "neonatal referral exposes a gap, or if the obstetric, "
        "assessment, discharge, infection-control or facility processes "
        "this SOP hands work to are revised."
    ),
    full_reference_list=[
        NABH_COP_CITE.format(code="COP.8"),
        JJ_ACT_SRC,
        POCSO_SRC,
    ],
)

# --------------------------------------------------------------- COP.9 ---
COP9 = SOPSpecV2(
    sop_no="SOP-COP.9",
    title="Procedural Sedation",
    purpose_plain=(
        "This SOP sets out how procedural sedation is administered in a "
        "consistent manner across every location in which it is given; "
        "how informed consent for sedation is obtained before the drug; "
        "how competence to administer and to monitor sedation is "
        "verified; how the six required intra-procedure parameters are "
        "monitored and recorded; and how post-procedure monitoring and "
        "objective, criteria-based discharge from the recovery area are "
        "documented."
    ),
    purpose_trigger=(
        "A patient's sedation unexpectedly deepens toward general "
        "anaesthesia during a procedure. This SOP is what hands that "
        "patient immediately to the anaesthesia or resuscitation process "
        "-- it is never managed as if it were still routine sedation just "
        "because that's what the consent form said."
    ),
    purpose_why=(
        "We do this because sedation that is a habit of the operator in "
        "one room and a written method in another is not a consistent "
        "service -- the patient cannot tell which room's habit they have "
        "walked into -- and because current registration to practise "
        "medicine is the legal floor, not the whole answer to whether "
        "someone is actually competent to sedate."
    ),
    purpose_text=(
        "To define how procedural sedation is administered consistently "
        "across locations, how consent is obtained before the drug, how "
        "competence is verified, how the six intra-procedure parameters "
        "are monitored, and how recovery discharge is documented."
    ),
    scope_why="so every location that administers sedation -- theatre, endoscopy, emergency, imaging -- follows the same safety standard.",
    scope_text=(
        "Applies to every location in which «Hospital Name» administers "
        "procedural sedation -- the operation theatre, endoscopy or "
        "other procedure rooms, the emergency area, day-care, and the "
        "imaging suite -- and to the person who administers, the person "
        "who monitors, the clinician who obtains consent, and recovery-"
        "area staff."
    ),
    responsibility_why="a room missing basic equipment, or a monitor who is also the one performing the procedure, is exactly how a routine sedation turns into an emergency nobody was ready for.",
    responsibilities=[
        ("Named Procedural-Sedation Lead", "Authors and keeps current the written sedation guidance, the named locations and depths, the room-readiness list, and the recovery discharge criteria."),
        ("Registered Medical Practitioner Administering Sedation", "Confirms identity and consent before the drug, sedates only within the depth the location is written to provide, and hands any unplanned deepening to the anaesthesia or resuscitation policy."),
        ("Person Monitoring the Patient", "Records all six intra-procedure parameters continuously and does not leave the patient unmonitored."),
        ("Person Judging Recovery Discharge", "Applies the objective discharge criteria and records the judgement -- never discharges a patient from recovery because the list has moved on."),
        ("Human Resource Function", "Verifies current National Medical Commission Act / State Medical Council registration and the hospital-defined sedation competence before any assignment to administer or monitor."),
        ("Quality/Accreditation Coordinator", "Audits sedation-location compliance, consent timing, competence, the six monitoring parameters, and recovery-discharge criteria on the defined interval."),
    ],
    items=[
        PlainItem(
            heading="Written guidance that makes sedation consistent across every location",
            why="Sedation that is a habit of the operator in one room and a written method in another is not a consistent service -- the patient cannot tell which room's habit they have walked into.",
            body=[
                "The hospital's defined locations for procedural "
                "sedation, and the depth of sedation provided in each, "
                "is the same written guidance used in every one of those "
                "locations -- not an anaesthesia-department document "
                "unused where most sedation actually happens.",
                "A depth expected to reach general anaesthesia is never "
                "given under this SOP; that patient is sedated and "
                "managed under the hospital's anaesthesia policy "
                "instead.",
                "The written guidance, and any revision to the named "
                "locations or depths, is logged so that every sedating "
                "location can show it is working from the current "
                "version.",
            ],
            oe_code="COP.9.a",
        ),
        PlainItem(
            heading="Room readiness before sedation starts",
            why="A pulse oximeter that is required in theatre and forgotten in the endoscopy room is the same drug given in a less safe room.",
            body=[
                "The hospital's defined room-readiness list is "
                "checked before the sedative is given. It covers six "
                "things:",
                "1. Airway equipment.",
                "2. Oxygen.",
                "3. Suction.",
                "4. Monitoring able to produce the six parameters.",
                "5. Resuscitation medicines.",
                "6. A means of calling help.",
                "A room missing any item on that list does not start "
                "sedation until the gap is corrected.",
                "The readiness check is logged against the room and the "
                "date, not assumed from the last time the room was "
                "checked.",
            ],
            oe_code="COP.9.a",
        ),
        PlainItem(
            heading="Informed consent for administration of procedural sedation",
            why="A procedure consent that is silent on sedation, or a signature taken after the drug, is not consent for the sedation that was actually given.",
            body=[
                "The hospital's defined method for recording informed "
                "consent for procedural sedation is completed before the "
                "sedative is given, in every case including a child or a "
                "patient who cannot consent, following the hospital's "
                "patient-rights consent method for who signs.",
                "A sedative is never given against a consent that is "
                "silent on sedation or that was signed after the drug.",
                "Consent timing is recorded against the unique "
                "identification number for every sedation episode.",
            ],
            oe_code="COP.9.b",
        ),
        PlainItem(
            heading="Competent and trained persons perform and monitor sedation",
            why="Current registration to practise medicine is the legal floor, not the whole answer -- the hospital's own training for the depth and location being sedated is what actually makes a person competent to administer or monitor.",
            body=[
                "A person administers procedural sedation only if their "
                "registration under the National Medical Commission Act, "
                "2019 and the State Medical Council is current, and only "
                "within the hospital-defined competence it has verified "
                "for that depth and location.",
                "The hospital's defined monitoring arrangement is "
                "followed; the default is that the monitor is not the "
                "person performing the procedure, and any written "
                "exception names the depths and locations it applies "
                "to.",
                "A person without the required registration or the "
                "hospital-defined training is never assigned to "
                "administer or monitor, even temporarily.",
            ],
            oe_code="COP.9.c",
            technical_sources=[NMC_ACT_S34_SRC],
        ),
        PlainItem(
            heading="Intra-procedure monitoring of the six required parameters",
            why="A pulse-oximetry trace with no recorded level of sedation, or a blood pressure taken once and never again, is an incomplete monitoring record even if it looks busy.",
            body=[
                "Six parameters are monitored throughout the "
                "procedure, and all six are recorded -- not a "
                "subset:",
                "1. Heart rate.",
                "2. Cardiac rhythm.",
                "3. Respiratory rate.",
                "4. Blood pressure.",
                "5. Oxygen saturation.",
                "6. Level of sedation.",
                "If any parameter cannot be obtained, the reason is "
                "recorded; sedation does not continue as if a missing "
                "parameter were present without a documented clinical "
                "reason from the person administering sedation.",
                "The six parameters are recorded against the unique "
                "identification number for every sedation episode.",
            ],
            oe_code="COP.9.d",
        ),
        PlainItem(
            heading="Post-procedure monitoring and objective discharge from recovery",
            why="Discharging a sedated patient from recovery because the next case is waiting, rather than because the patient actually meets the criteria, is how a sedation service loses a patient after the procedure went perfectly.",
            body=[
                "Every sedated patient remains in a defined recovery "
                "area -- not a corridor or an unmonitored waiting chair "
                "-- where the hospital's defined post-procedure "
                "observations are documented.",
                "The patient is discharged from the recovery area only "
                "against the hospital's defined objective discharge "
                "criteria, judged and recorded by the hospital's defined "
                "person -- never against the theatre list.",
                "Recovery observations and the discharge judgement are "
                "recorded against the unique identification number.",
            ],
            oe_code="COP.9.e",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the COP.9 Records folder).",
    related_documents=[
        "Policy on Procedural Sedation (COP.9)",
        "Hospital's Anaesthesia SOP (COP.10)",
        "Hospital's Cardio-Pulmonary Resuscitation SOP (COP.3)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if an unplanned "
        "deepening, sedation in an unnamed location, a missing "
        "monitoring parameter, or a recovery discharge that did not meet "
        "the criteria exposes a gap, or if the anaesthesia, medication, "
        "paediatric, resuscitation or patient-rights processes this SOP "
        "hands work to are revised."
    ),
    full_reference_list=[NABH_COP_CITE.format(code="COP.9"), NMC_ACT_S34_SRC],
)

# --------------------------------------------------------------- COP.10 ---
COP10 = SOPSpecV2(
    sop_no="SOP-COP.10",
    title="Anaesthesia Services",
    purpose_plain=(
        "This SOP sets out how anaesthesia services are administered "
        "consistently and safely across every named location; how the "
        "pre-anaesthesia assessment produces a documented plan and the "
        "pre-induction assessment confirms it; how informed consent for "
        "anaesthesia is obtained before induction; how the patient is "
        "monitored contemporaneously while under anaesthesia; how "
        "post-anaesthesia monitoring and objective, criteria-based "
        "discharge from recovery are documented; how the type of "
        "anaesthesia and the anaesthetic medicines are recorded; and how "
        "intra-operative adverse anaesthesia events are recorded and "
        "reviewed."
    ),
    purpose_trigger=(
        "A monitoring chart is found to have been filled in from memory "
        "at the end of a case, rather than as the case went along. This "
        "SOP is what treats that as reconstruction, not monitoring -- and "
        "requires every parameter to be recorded contemporaneously, with "
        "a documented reason whenever one genuinely cannot be obtained."
    ),
    purpose_why=(
        "We do this because a folder of downloaded anaesthesia standards "
        "in the office, unused by a visiting practitioner's private "
        "habit, is not a consistent and safe service -- it is a document "
        "and a habit, coexisting -- and because a recovery discharge "
        "timed to the porter's arrival, rather than to the patient "
        "actually meeting the criteria, returns an unstable patient to a "
        "ward that believes recovery has already happened."
    ),
    purpose_text=(
        "To define how anaesthesia is administered consistently and "
        "safely; how the pre-anaesthesia plan and pre-induction check "
        "work; how consent is obtained before induction; how the patient "
        "is monitored contemporaneously; how recovery discharge is "
        "judged; how type and medicines are recorded; and how adverse "
        "events are recorded and reviewed."
    ),
    scope_why="so every location that administers anaesthesia -- theatre, any other named location, recovery -- follows the same safety standard.",
    scope_text=(
        "Applies to every location in which «Hospital Name» administers "
        "anaesthesia -- the operation theatre, any other named "
        "anaesthesia location, and the recovery area -- and to the "
        "registered medical practitioner who administers, the person who "
        "assists and monitors, the clinician who performs the "
        "assessments and obtains consent, and recovery-area staff."
    ),
    responsibility_why="a plan never written, a consent taken after induction, or a monitoring chart reconstructed from memory are each a failure that only shows up when something has already gone wrong.",
    responsibilities=[
        ("Person in Charge of Anaesthesia", "Authors and keeps current the written anaesthesia guidance, the pre-anaesthesia assessment method and plan fields, the monitoring record, and the recovery criteria."),
        ("Registered Medical Practitioner Administering Anaesthesia", "Uses the documented plan, performs the pre-induction assessment, confirms consent, monitors the patient contemporaneously, records type/medicines and adverse events, and does not start anaesthesia where the guidance cannot be met."),
        ("Person Assisting/Recording Monitoring", "Records monitoring as it happens -- never reconstructs the chart at the end of the case."),
        ("Person Judging Recovery Discharge", "Applies the objective discharge criteria and records the judgement -- never discharges because the next case is waiting."),
        ("Human Resource Function", "Verifies current National Medical Commission Act / State Medical Council registration and hospital-defined anaesthesia competence before any assignment to administer anaesthesia."),
        ("Quality/Accreditation Coordinator", "Audits location compliance, the documented plan, pre-induction timing, consent, contemporaneous monitoring, type/medicines documentation, adverse-event review, and recovery discharge on the defined interval."),
    ],
    items=[
        PlainItem(
            heading="Anaesthesia administered in a consistent and safe manner",
            why="A folder of downloaded anaesthesia standards in the office, unused by the visiting practitioner's private habit, is not a consistent and safe service -- it is a document and a habit, coexisting.",
            body=[
                "The hospital's defined locations in which anaesthesia "
                "may be administered, and the types of anaesthesia "
                "provided, is the written guidance every one of those "
                "locations actually works from; a type not provided is "
                "named as not provided.",
                "A person administers anaesthesia only if their "
                "registration under the National Medical Commission Act, "
                "2019 and the State Medical Council is current, and only "
                "within the hospital-defined competence it has verified "
                "for that type and location.",
                "The hospital's defined pre-anaesthesia checklist is "
                "checked before anaesthesia begins, and a location "
                "missing any item does not start until the gap is "
                "corrected.",
            ],
            oe_code="COP.10.a",
            technical_sources=[NMC_ACT_S34_SRC],
        ),
        PlainItem(
            heading="Pre-anaesthesia assessment resulting in a documented plan",
            why="A note that says 'fit for anaesthesia' with nothing under a heading titled 'plan' is an opinion, not the plan this step requires.",
            body=[
                "The hospital's defined process for who performs the "
                "pre-anaesthesia assessment and when is followed. The "
                "assessment covers at least six things:",
                "1. Identity against the two identifiers.",
                "2. The planned procedure so far as known.",
                "3. Relevant history and examination.",
                "4. Airway and fasting information.",
                "5. Relevant investigation findings.",
                "6. The risks that shape the plan.",
                "The assessment produces a documented plan, written "
                "before anaesthesia is given, stating four things:",
                "1. The intended type.",
                "2. The intended airway or regional strategy.",
                "3. The planned monitoring.",
                "4. The fallback if that strategy cannot be used.",
                "Where the anaesthetic is an emergency, the assessment "
                "that was possible and the plan for that emergency are "
                "recorded before induction so far as the emergency "
                "allows; the plan is never skipped because the case is "
                "urgent.",
            ],
            oe_code="COP.10.b",
        ),
        PlainItem(
            heading="Pre-induction assessment performed and documented",
            why="Repeating the full history at the door of theatre is not a substitute for the plan; skipping the immediate pre-induction check because a plan already exists is not a substitute for this step.",
            body=[
                "The hospital's defined person performs the pre-"
                "induction assessment immediately before induction, "
                "confirming identity, that anaesthesia consent is "
                "present, and that the documented plan still applies.",
                "Any change since the pre-anaesthesia assessment that "
                "alters the plan is written before induction proceeds.",
                "The pre-induction assessment is recorded against the "
                "unique identification number, distinct from the earlier "
                "pre-anaesthesia assessment.",
            ],
            oe_code="COP.10.c",
        ),
        PlainItem(
            heading="Informed consent for administration of anaesthesia",
            why="A surgical consent that never mentions anaesthesia, when anaesthesia is then given, is not consent for the anaesthetic that was actually administered.",
            body=[
                "The hospital's defined method for recording informed "
                "consent for anaesthesia is completed before induction, "
                "in every case including a child or a patient who cannot "
                "consent, following the hospital's patient-rights "
                "consent method for who signs.",
                "A signature obtained after induction, or a surgical "
                "consent silent on anaesthesia, is never treated as "
                "consent for administration of anaesthesia.",
                "Consent timing is recorded against the unique "
                "identification number for every anaesthetic.",
            ],
            oe_code="COP.10.d",
        ),
        PlainItem(
            heading="Monitoring the patient while under anaesthesia",
            why="A monitor that was switched on in the room, with the chart filled in from memory at the end of the case, is reconstruction -- not monitoring while under anaesthesia.",
            body=[
                "The hospital's defined parameters monitored while under "
                "anaesthesia are recorded contemporaneously for the "
                "whole period from induction until handover to recovery "
                "-- never filled in afterward from memory.",
                "If a parameter cannot be obtained, the reason is "
                "recorded; anaesthesia does not continue as if the "
                "parameter were present without a documented clinical "
                "reason.",
                "Where regional anaesthesia is provided, identity and "
                "site checks are applied before the block is performed. "
                "All monitoring is recorded against the unique "
                "identification number.",
            ],
            oe_code="COP.10.e",
        ),
        PlainItem(
            heading="Post-anaesthesia monitoring and objective discharge from recovery",
            why="A recovery discharge timed to the porter's arrival, rather than to the patient actually meeting the criteria, returns an unstable patient to a ward that believes recovery has already happened.",
            body=[
                "Every patient is transferred to the hospital's defined "
                "recovery area after anaesthesia -- not a corridor or an "
                "unmonitored waiting chair -- where the hospital's "
                "defined post-anaesthesia observations are documented.",
                "The patient is discharged from the recovery area only "
                "against the hospital's defined objective discharge "
                "criteria, judged and recorded by the hospital's defined "
                "person -- never because the theatre list has moved on.",
                "Recovery observations and the discharge judgement are "
                "recorded against the unique identification number; this "
                "is post-anaesthesia recovery, a sibling process to "
                "post-sedation recovery, not automatically the same "
                "form.",
            ],
            oe_code="COP.10.f",
        ),
        PlainItem(
            heading="Type of anaesthesia and anaesthetic medicines in the patient record",
            why="A medicine that was given but never entered in the record is an incomplete anaesthetic-care record, whatever actually happened in the theatre.",
            body=[
                "The type of anaesthesia actually given, and every "
                "anaesthetic medicine used, are documented in the "
                "patient record against the unique identification "
                "number.",
                "Where the type actually given differs from the type "
                "planned, the record says so.",
            ],
            oe_code="COP.10.g",
            boundary=[
                "This record does not restate the medication policies' "
                "storage or controlled-drug account -- it owns only that "
                "the anaesthetic care record names the type and the "
                "medicines given.",
            ],
        ),
        PlainItem(
            heading="Intra-operative adverse anaesthesia events recorded and monitored",
            why="An adverse event that is managed and then only remembered is not recorded; an event that is recorded and never reviewed is not monitored.",
            body=[
                "The hospital's defined list of what counts as an "
                "intra-operative adverse anaesthesia event is recorded "
                "in the patient record and in the event register or "
                "equivalent as soon as it occurs.",
                "Events are reviewed at the hospital's defined forum, "
                "and corrective action from that review is recorded.",
            ],
            oe_code="COP.10.h",
            boundary=[
                "This step feeds anaesthesia events into a recorded and "
                "reviewed stream -- it does not write the hospital-wide "
                "incident-reporting policy.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-8 (see the COP.10 Records folder).",
    related_documents=[
        "Policy on Anaesthesia Services (COP.10)",
        "Hospital's Procedural Sedation SOP (COP.9)",
        "Hospital's Cardio-Pulmonary Resuscitation SOP (COP.3)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a missing plan, a "
        "reconstructed monitoring chart, an unplanned deepening from "
        "sedation that was not handed here, or a recovery discharge that "
        "did not meet the criteria exposes a gap, or if the sedation, "
        "procedures, medication, sterilisation or patient-rights "
        "processes this SOP hands work to are revised."
    ),
    full_reference_list=[NABH_COP_CITE.format(code="COP.10"), NMC_ACT_S34_SRC],
)

# --------------------------------------------------------------- COP.11 ---
COP11 = SOPSpecV2(
    sop_no="SOP-COP.11",
    title="Clinical Procedures and Operation Theatre Practice",
    purpose_plain=(
        "This SOP sets out how clinical procedures and operations are "
        "performed in a consistent and safe manner; how the pre-"
        "operative assessment produces a documented diagnosis and "
        "instructions; how consent is obtained by the operating doctor; "
        "how wrong site, wrong patient and wrong surgery are prevented "
        "through identity confirmation, site-marking and a real "
        "surgical-safety pause; how standard precautions, operation "
        "notes, facilities and equipment are maintained; how a theatre "
        "quality-assurance programme looks at whether the process "
        "actually ran; and how the organ-transplant programme (where one "
        "exists) and organ-donation awareness (always) are conducted."
    ),
    purpose_trigger=(
        "A surgical-safety checklist is found to have been ticked in "
        "recovery, after the patient had already left the table. This SOP "
        "is what treats that as a pause that did not happen -- the three "
        "WHO moments have to be completed out loud as each one actually "
        "occurs, never filled in later from memory."
    ),
    purpose_why=(
        "We do this because a theatre manual in a cupboard and a list "
        "that runs on habit is not a method -- a locum or a night "
        "emergency cannot consult habit -- and because a checklist ticked "
        "after the fact is exactly how the next wrong-site event gets "
        "documented as having been prevented."
    ),
    purpose_text=(
        "To define how clinical procedures and operations are performed "
        "consistently and safely; the pre-operative diagnosis and "
        "instructions; consent by the operating doctor; wrong-site/"
        "wrong-patient/wrong-surgery prevention; standard precautions; "
        "operation notes; theatre facilities and equipment; the theatre "
        "quality-assurance programme; and organ transplant/donation."
    ),
    scope_why="so every procedure and operation -- main theatre, day-care theatre, endoscopy, any procedure room -- follows the same safety standard.",
    scope_text=(
        "Applies to every clinical procedure and operation performed "
        "at «Hospital Name» -- the main operating theatre, any day-care "
        "or minor-procedure theatre, endoscopy or other procedure rooms, "
        "and the recovery area immediately afterwards. It binds the "
        "operating surgeon, theatre nursing and technical staff, and any "
        "visiting or honorary surgeon."
    ),
    responsibility_why="a missed site mark, a checklist filled in afterward, or a transplant performed without statutory registration are each a failure that is both a document defect and a legal one.",
    responsibilities=[
        ("Person in Charge of the Operating Theatre", "Holds the written guidance, the equipment and supply inventory, and supports the surgical-safety pauses."),
        ("Operating Surgeon", "Obtains consent, marks the site, leads or participates in the pauses, writes or ensures the operation note and post-operative plan, and does not start when identity, site, consent or sterility is in doubt."),
        ("Named Theatre Quality Lead", "Operates the quality-assurance programme and reports findings to the defined forum."),
        ("Theatre Nursing and Technical Staff", "Apply the written guidance, complete the checklist as a real pause, apply standard precautions, and never open an unsterile or overdue set."),
        ("Named Transplant-Programme Lead (where a programme exists)", "Holds the statutory registration and Authorisation Committee records."),
        ("Person Responsible for Organ-Donation Awareness", "Holds the awareness measures and records, whether or not a transplant programme exists."),
        ("Quality/Accreditation Coordinator", "Audits guidance use, pre-operative diagnosis timing, consent, checklist timing, operation notes, facilities/equipment, quality-assurance findings, transplant-programme status and donation-awareness records on the defined interval."),
    ],
    items=[
        PlainItem(
            heading="Written guidance that makes procedures consistent and safe",
            why="A theatre manual in a cupboard and a list that runs on habit is not a method -- a locum or a night emergency cannot consult habit.",
            body=[
                "The hospital's defined guidance -- which procedures may "
                "be performed in which theatre or procedure room, who "
                "may perform them, how a list is scheduled and how an "
                "emergency case is inserted -- is the written guidance "
                "every list, routine or emergency, employed or visiting "
                "surgeon, actually works from.",
                "The hospital's defined pre-move checklist is checked "
                "every time before the patient is moved into the "
                "operating room; a case missing a required element is "
                "stopped or postponed, never started from habit.",
                "The guidance in use, and where it is held, is confirmed "
                "current at the defined interval.",
            ],
            oe_code="COP.11.a",
        ),
        PlainItem(
            heading="Pre-operative assessment, diagnosis and instructions",
            why="A diagnosis first written in the operation note after the procedure is not a pre-operative diagnosis -- it is a post-operative one wearing the wrong label.",
            body=[
                "The hospital's defined person performs and records the "
                "pre-operative assessment against the unique "
                "identification number, distinct from the pre-"
                "anaesthesia assessment.",
                "A documented pre-operative diagnosis is written before "
                "the patient is moved into the operating room, and the "
                "hospital's defined pre-operative instructions are "
                "completed.",
                "For an emergency that cannot wait for a full elective "
                "work-up, the working diagnosis and the instructions "
                "that were possible are still recorded -- absence of "
                "time is recorded; absence of a diagnosis is not.",
            ],
            oe_code="COP.11.b",
        ),
        PlainItem(
            heading="Informed consent obtained by the doctor prior to the procedure",
            why="A consent taken by a clerk, a nurse, or a doctor who will not be in the theatre does not meet this step, however complete the form looks.",
            body=[
                "The doctor who will perform the procedure, or a doctor "
                "of the same surgical team who will be present and "
                "responsible for it, obtains consent before the "
                "procedure starts, naming the procedure, the side where "
                "laterality applies, and the unique identification "
                "number.",
                "The hospital's defined method for recording procedural "
                "consent is followed; a consent for 'surgery' without "
                "the procedure or the side is treated as incomplete.",
                "An emergency that makes prior consent impossible is "
                "recorded with the reason and the person who decided to "
                "proceed, per the patient-rights policies.",
            ],
            oe_code="COP.11.c",
        ),
        PlainItem(
            heading="Preventing wrong site, wrong patient and wrong surgery",
            why="A checklist ticked in recovery, after the patient has left the table, is a record of a pause that did not happen -- and it is exactly how the next wrong-site event gets documented as having been prevented.",
            body=[
                "Identity is confirmed at the first pause using the two "
                "identifiers of the uniform-care policy, matched to "
                "consent, the operating list and the unique "
                "identification number, with the patient participating "
                "while able.",
                "Where the procedure has a side or a level, the site is "
                "marked before the patient is moved into the operating "
                "room, visible after draping, using the hospital's "
                "defined site-marking method; marking after the drape is "
                "down, or marking the wrong side as a reminder, is "
                "forbidden.",
                "The hospital's defined surgical-safety checklist -- "
                "built on the three WHO moments (before induction, "
                "before incision, before the patient leaves the "
                "operating room) as a framework, not a pasted script -- "
                "is completed out loud as each pause actually happens; "
                "completing it later from memory is forbidden, and any "
                "near-miss caught at a pause is recorded and fed to the "
                "quality-assurance programme.",
            ],
            oe_code="COP.11.d",
        ),
        PlainItem(
            heading="Standard precautions during the procedure",
            why="Standard precautions are not looser in theatre than anywhere else in the hospital -- the same rules apply where the exposure is greater.",
            body=[
                "Standard precautions -- hand hygiene, PPE selection, "
                "safe injection and sharps handling -- are applied by "
                "every person in the operating theatre and procedure "
                "room, for every patient, without reference to "
                "diagnosis.",
                "Theatre staff are briefed that standard precautions "
                "govern here as they govern everywhere else in the "
                "hospital.",
                "A breach of standard precautions during a procedure is "
                "reported and handled under the hospital's infection-"
                "control process, not under a parallel theatre-only "
                "rule.",
            ],
            oe_code="COP.11.e",
            boundary=[
                "Standard precautions themselves (hand hygiene, PPE, "
                "sharps handling) are owned by the infection-prevention-"
                "and-control-practices policy (HIC.2); this step owns "
                "only that they are applied in the operating theatre.",
            ],
        ),
        PlainItem(
            heading="Procedure notes, post-procedure monitoring and the post-operative care plan",
            why="A post-operative plan that exists only as a verbal instruction to the receiving nurse is not documented -- and it is the plan most likely to be followed inconsistently on the next shift.",
            body=[
                "The hospital's defined person writes the operation or "
                "procedure note by the hospital-defined deadline, "
                "covering at least seven things:",
                "1. The procedure actually performed.",
                "2. The side.",
                "3. Findings.",
                "4. Implants or specimens with identification.",
                "5. Estimated blood loss.",
                "6. Intra-operative complications.",
                "7. The names of the surgeon and assistants.",
                "Post-procedure surgical observations continued in "
                "recovery are recorded, distinct from the anaesthesia "
                "policy's recovery criteria.",
                "The post-operative care plan is written before the "
                "patient leaves recovery, against the unique "
                "identification number, covering five things:",
                "1. Wound.",
                "2. Drains.",
                "3. Mobilisation.",
                "4. Diet.",
                "5. Review.",
            ],
            oe_code="COP.11.f",
        ),
        PlainItem(
            heading="Facilities, equipment, instruments and supplies in the operating theatre",
            why="Discovering the implant is not in the hospital after induction is a preventable cancellation, not an unlucky one.",
            body=[
                "The hospital's defined list of operating theatres and "
                "procedure rooms in use, and the procedures each may "
                "hold, aligned with the service directory, is the list a "
                "case is checked against before it is scheduled there.",
                "Instruments used on sterile tissue are confirmed "
                "sterile, in-date, with intact indicators before the "
                "list starts; a missing or unsterile set stops the case "
                "rather than being substituted from an unchecked tray.",
                "The hospital's defined equipment inventory, and any "
                "required implant, is confirmed present before the "
                "patient is anaesthetised; out-of-service equipment is "
                "labelled and not counted as available.",
            ],
            oe_code="COP.11.g",
        ),
        PlainItem(
            heading="Quality-assurance programme for procedural and theatre practice",
            why="A quality-assurance file of theatre statistics nobody reads is not an implemented programme -- and a hospital can have a low counted infection rate while being one skipped pause away from the wrong kidney.",
            body=[
                "The hospital's named theatre quality lead is "
                "accountable for a programme that measures use of the "
                "pause -- not possession of the checklist form -- "
                "covering six things:",
                "1. Checklist completion in real time.",
                "2. Consent before incision.",
                "3. A documented pre-operative diagnosis.",
                "4. Operation notes within the stated time.",
                "5. Postponements and cancellations after arrival, "
                "with reason.",
                "6. Near-misses or actual wrong-site, wrong-patient "
                "or wrong-procedure events.",
                "Findings that require change produce a corrective and "
                "preventive action with an owner and a due date -- never "
                "only a reminder to be careful -- reviewed at the "
                "hospital's defined forum.",
            ],
            oe_code="COP.11.h",
            boundary=[
                "This programme is a separate process look from the "
                "infection-surveillance policy's surgical-site-infection "
                "counting; it does not duplicate NHSN case definitions "
                "or infection rates.",
            ],
        ),
        PlainItem(
            heading="Organ transplant programme — legal and ethical, or a recorded absence",
            why="A transplant service the hospital's own directory does not name, or a transplant performed without the statutory registration, is a document defect and a legal one at the same time.",
            body=[
                "Whether «Hospital Name» conducts an organ transplant "
                "programme is recorded and kept aligned with the service "
                "directory; if it does not, that fact is recorded and "
                "staff do not hold the hospital out as a transplant "
                "centre.",
                "If a programme exists, it operates only as registered "
                "under the Transplantation of Human Organs and Tissues "
                "Act, 1994, with living-donor transplants limited to "
                "near relatives or to donors approved by the "
                "Authorisation Committee, and with commercial dealing in "
                "human organs forbidden.",
                "The hospital's named transplant-programme lead, where a "
                "programme exists, holds the statutory registration and "
                "Authorisation Committee records for audit.",
            ],
            oe_code="COP.11.i",
            technical_sources=[THOA_SRC],
        ),
        PlainItem(
            heading="Awareness of organ donation",
            why="A hospital that never transplants still sees deaths, still sees families, and still sits inside a community that can donate -- awareness is not something only a transplant centre owes.",
            body=[
                "The hospital's defined organ-donation awareness "
                "measures are in force whether or not a transplant "
                "programme exists, and are additional to that programme "
                "where one does exist.",
                "Where a patient or family asks about donation, the "
                "hospital's defined responder responds and makes a "
                "referral to the organ-transplant network where "
                "appropriate -- staff never pressure a family.",
                "Records of the measures -- materials, session dates, "
                "display -- are kept by the hospital's defined "
                "recordkeeper.",
            ],
            oe_code="COP.11.j",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-10 (see the COP.11 Records folder).",
    related_documents=[
        "Policy on Clinical Procedures and Operation Theatre Practice (COP.11)",
        "Hospital's Anaesthesia SOP (COP.10)",
        "Hospital's Infection-Prevention-and-Control-Practices Policy (HIC.2)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a wrong-site or "
        "wrong-patient event or near-miss occurs, if the service "
        "directory adds or removes a procedure or a transplant "
        "programme, or if the infection-control, anaesthesia, sedation, "
        "internal-transfer or intensive-care processes this SOP hands "
        "work to are revised."
    ),
    full_reference_list=[NABH_COP_CITE.format(code="COP.11"), THOA_SRC],
)

# --------------------------------------------------------------- COP.12 ---
COP12 = SOPSpecV2(
    sop_no="SOP-COP.12",
    title="Identification and Management of Patients at Higher Risk of Morbidity and Mortality",
    purpose_plain=(
        "This SOP sets out how vulnerable patients are identified and "
        "managed; how a safe and secure care-environment is provided at "
        "the bedside; how patients at risk of fall, pressure ulcers and "
        "deep vein thrombosis are identified and managed; and how "
        "restraint is used only as a last-resort, time-limited, "
        "documented measure, with the additional statutory layer that "
        "applies where the patient has mental illness."
    ),
    purpose_trigger=(
        "A nurse applies a restraint 'for safety' with no doctor's order, "
        "no clock and no record. This SOP is what forbids that outright "
        "-- restraint is used only on a recorded doctor's order stating "
        "the reason, the type, the start time and the latest review time, "
        "every single time, with no informal exception."
    ),
    purpose_why=(
        "We do this because a flag that nobody reads is a label, not "
        "identification -- and a vulnerable patient left on an unattended "
        "trolley in a corridor as a holding pattern is exactly the "
        "ordinary-hospital-day harm this SOP exists to prevent, whether "
        "the risk is a fall, a pressure ulcer, or an undocumented "
        "restraint."
    ),
    purpose_text=(
        "To define how vulnerable patients are identified and managed; "
        "how a safe care-environment is provided; how fall, pressure-"
        "ulcer and thrombosis risk are identified and managed; and how "
        "restraint is used only as a last-resort, time-limited, "
        "documented measure."
    ),
    scope_why="so every clinical setting where a patient may be vulnerable -- wards, day-care, emergency, ICU, theatre -- follows the same identification and safety standard.",
    scope_text=(
        "Applies to every clinical setting of «Hospital Name» in which a "
        "patient may be vulnerable or at higher risk -- in-patient wards, "
        "day-care, the emergency area, intensive or high-dependency "
        "areas, and the operating theatre and recovery insofar as these "
        "risks arise there."
    ),
    responsibility_why="a flag nobody applies, or a restraint applied with no order and no clock, is exactly the kind of undocumented harm this SOP exists to catch.",
    responsibilities=[
        ("Named Vulnerable-Patient Programme Lead", "Keeps the vulnerable-patient category list current and reviews that flags are actually applied, not just ticked."),
        ("Treating Clinicians", "Identify risk, order prophylaxis or restraint when indicated, and review restraint at the stated interval."),
        ("Nursing Staff", "Apply identification tools and management measures, apply restraint only under a doctor's order, observe the restrained patient continuously, and record falls, ulcers and restraint episodes."),
        ("Facility Function", "Provides building security under its own policies; the bedside care-environment remains this SOP's responsibility."),
        ("Quality/Accreditation Coordinator", "Audits vulnerable-patient flags, falls/pressure-ulcer/thrombosis identification and measures, and restraint episodes for a doctor's order, review time, observations and stop time, on the defined interval."),
    ],
    items=[
        PlainItem(
            heading="Identifying and managing vulnerable patients",
            why="A flag that nobody reads is a label, not identification -- and so is a flag applied to every single patient, because then it means nothing.",
            body=[
                "The hospital's defined categories of vulnerable patient "
                "are applied at first clinical contact and repeated on "
                "change of condition, using the hospital's defined "
                "identification and recording method.",
                "The hospital's defined management measures once a "
                "patient is identified as vulnerable actually change "
                "what happens next -- observations, accompaniment, "
                "environment -- not just the paperwork.",
                "The category list and the pattern of flags applied are "
                "reviewed by the hospital's named lead, who investigates "
                "a period where nobody or everybody was flagged.",
            ],
            oe_code="COP.12.a",
        ),
        PlainItem(
            heading="Safe and secure care-environment for the vulnerable patient",
            why="A vulnerable patient left on an unattended trolley in a corridor as a holding pattern is exactly the ordinary-hospital-day harm this step exists to prevent.",
            body=[
                "The hospital's defined care-environment measures for "
                "vulnerable patients are in force at the bedside, "
                "covering four things:",
                "1. A call method the patient can use.",
                "2. Accompaniment when leaving the unit.",
                "3. Lighting/toileting access matched to ability.",
                "4. How a missing vulnerable patient is noticed and "
                "who is called.",
                "A vulnerable patient is never left in a public "
                "corridor, an unlocked bathroom, or an unattended "
                "trolley as a holding pattern.",
            ],
            oe_code="COP.12.b",
            boundary=[
                "Building security (locks, cameras, access control) is "
                "owned by the facility-management policies; this step "
                "does not duplicate them.",
            ],
        ),
        PlainItem(
            heading="Patients at risk of fall",
            why="A falls score calculated once at admission and never looked at again is not managing fall risk -- it is filing it.",
            body=[
                "The hospital's defined method for identifying patients "
                "at risk of fall is applied at first contact and "
                "repeated when condition, medication or mobility "
                "changes, recorded against the unique identification "
                "number.",
                "The hospital's defined measures for a patient "
                "identified at risk of fall are in place for every "
                "patient so identified.",
                "Any fall that occurs is recorded and reported per the "
                "hospital's defined process, the patient is assessed, "
                "and the identification and measures are reviewed.",
            ],
            oe_code="COP.12.c",
        ),
        PlainItem(
            heading="Patients at risk of pressure ulcers",
            why="A patient who already has a pressure ulcer is at risk of it worsening -- this programme does not stop at patients with intact skin.",
            body=[
                "The hospital's defined method for identifying patients "
                "at risk of developing or worsening pressure ulcers is "
                "applied to every patient, including one who already has "
                "an ulcer.",
                "The hospital's defined measures to prevent developing "
                "or worsening pressure ulcers, including skin inspection "
                "and repositioning, are in place once a patient is "
                "identified at risk.",
                "Any existing ulcer is described using the hospital's "
                "defined method and reassessed at the defined interval.",
            ],
            oe_code="COP.12.d",
        ),
        PlainItem(
            heading="Patients at risk of deep vein thrombosis",
            why="Identifying thrombosis risk without a prophylaxis decision to go with it is half this step -- the identification is only the trigger for the measure.",
            body=[
                "The hospital's defined method for identifying patients "
                "at risk of developing or worsening deep vein thrombosis "
                "is applied and recorded against the unique "
                "identification number.",
                "The hospital's defined measures for a patient at risk, "
                "including mechanical and, where indicated, "
                "pharmacological options, are put in place; "
                "pharmacological prophylaxis is prescribed and "
                "administered under the medication policies.",
                "Any contraindication to a chosen measure is recorded "
                "rather than silently skipped.",
            ],
            oe_code="COP.12.e",
        ),
        PlainItem(
            heading="Patients who need restraints",
            why="A device applied by a nurse 'for safety', with no order, no clock and no record, is forbidden here -- that is exactly the practice that remains undiscovered until the next shift or until the patient is injured by it.",
            body=[
                "Where the patient has mental illness, restraint and "
                "seclusion follow the Mental Healthcare Act, 2017: "
                "seclusion is prohibited outright; physical restraint is "
                "used only when it is the only means to prevent "
                "imminent, immediate harm to the person or others, is "
                "authorised by the psychiatrist in charge, lasts no "
                "longer than necessary, and is never used as punishment "
                "or because the ward is short-staffed.",
                "Where the patient does not have mental illness, "
                "restraint is still last-resort, time-limited and "
                "documented: used only when less restrictive measures "
                "have been tried or are not possible, only to prevent "
                "imminent harm, never as punishment or for staff "
                "convenience, and only on a recorded doctor's order "
                "stating the reason, the type, the start time and the "
                "latest review time.",
                "Every episode -- for either group -- is recorded "
                "against the unique identification number, covering "
                "eight things:",
                "1. The indication.",
                "2. Less-restrictive measures tried.",
                "3. The type.",
                "4. Start and stop times.",
                "5. Continuous observations.",
                "6. The ordering/authorising clinician.",
                "7. The nominated representative or family informed.",
                "8. Any injury.",
                "The episode is then reviewed at the hospital's "
                "defined forum and interval.",
            ],
            oe_code="COP.12.f",
            technical_sources=[MHA_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the COP.12 Records folder).",
    related_documents=[
        "Policy on Identification and Management of Patients at Higher Risk of Morbidity and Mortality (COP.12)",
        "Hospital's Assessment SOP (AAC.3)",
        "Hospital's Paediatric and Neonatal Services SOP (COP.8)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a serious fall, a "
        "stage-worsened pressure ulcer, a hospital-acquired thrombosis, a "
        "restraint injury, or an unauthorised restraint occurs, or if the "
        "assessment, facility, paediatric, medication or patient-rights "
        "processes this SOP hands work to are revised."
    ),
    full_reference_list=[NABH_COP_CITE.format(code="COP.12"), MHA_SRC],
)

# --------------------------------------------------------------- COP.13 ---
COP13 = SOPSpecV2(
    sop_no="SOP-COP.13",
    title="Pain Management, Rehabilitation Services and Nutritional Therapy",
    purpose_plain=(
        "This SOP sets out how patients in pain are identified and "
        "effectively managed, with alleviation titrated to need and "
        "response; how the rehabilitation scope matches the services this "
        "hospital has actually defined, and is planned collaboratively "
        "where it exists; and how every admitted patient is screened for "
        "nutritional risk, assessed if flagged, and served the "
        "therapeutic diet that was actually planned with dietetics."
    ),
    purpose_trigger=(
        "A patient's pain score field is left blank on the chart. This "
        "SOP is what treats that blank as an incomplete assessment -- "
        "never as silent evidence that the patient has no pain."
    ),
    purpose_why=(
        "We do this because a recorded zero that was never actually asked "
        "about is a false record, and it is exactly how unmanaged pain "
        "comes to look like managed pain -- and because a hospital that "
        "lists a service on the board with no one actually able to "
        "deliver it is holding out care it cannot provide."
    ),
    purpose_text=(
        "To define how patients in pain are identified and managed with "
        "titration; how rehabilitation scope matches actual services and "
        "is planned collaboratively; and how nutritional screening, "
        "assessment and therapeutic-diet planning work for every "
        "admission."
    ),
    scope_why="so every setting where a patient may be in pain, need rehabilitation, or is admitted and therefore screened for nutrition follows the same standard.",
    scope_text=(
        "Applies to every clinical setting of «Hospital Name» in which a "
        "patient may be in pain, may need rehabilitation, or is admitted "
        "and therefore screened for nutritional risk -- in-patient "
        "wards, day-care, the emergency area, relevant out-patient "
        "encounters, intensive or high-dependency areas, and the "
        "dietetics function."
    ),
    responsibility_why="unmanaged pain, a service held out that nobody can deliver, or a swallowing risk nobody screened for, are each a gap that reaches the patient directly.",
    responsibilities=[
        ("Named Pain-Assessment Method Lead", "Keeps the pain-assessment method current and confirms it is used rather than waited on."),
        ("Treating Clinicians", "Assess pain, prescribe alleviation, indicate rehabilitation where the service exists, and indicate a therapeutic diet."),
        ("Nurses", "Apply the pain-assessment method, reassess and titrate within a prescribed range, screen every admission for nutritional risk, and confirm the planned diet was served."),
        ("Rehabilitation Professionals (where the service exists)", "Participate in collaborative plans and deliver only the therapy the service directory actually resources."),
        ("Dietetics", "Assesses patients screened at risk and plans the therapeutic diet with the treating clinician."),
        ("Quality/Accreditation Coordinator", "Audits pain assessment and titration, rehabilitation-scope alignment with the directory, collaborative plans, nutritional screening and assessment, and therapeutic-diet planning on the defined interval."),
    ],
    items=[
        PlainItem(
            heading="Patients in pain are effectively managed",
            why="A recorded zero that was never asked about is a false record -- and it is exactly how unmanaged pain comes to look like managed pain.",
            body=[
                "The hospital's defined pain-assessment method, "
                "including the scale or description method and which "
                "settings it applies in, is used to ask every in-patient, "
                "and every other patient in a setting this hospital has "
                "included, about pain -- not inferred from whether they "
                "complain loudly.",
                "The assessment is recorded against the unique "
                "identification number, with the time; a blank field is "
                "treated as an incomplete assessment, never as evidence "
                "of no pain.",
                "A written plan -- pharmacological, non-pharmacological, "
                "or both -- is produced for every patient found in pain, "
                "using the hospital's defined non-pharmacological pain "
                "measures where applicable; pharmacological measures are "
                "prescribed under the medication policies.",
            ],
            oe_code="COP.13.a",
        ),
        PlainItem(
            heading="Titration according to need and response",
            why="A measure given once and never reassessed is a standing dose, not titration.",
            body=[
                "Pain is reassessed after a measure is given, using the "
                "same method, at the hospital's defined interval.",
                "The hospital's defined rule for who may titrate within "
                "a prescribed range, and when the treating clinician is "
                "called, governs who adjusts the measure; administration "
                "of the medicine itself remains the medication "
                "policies.",
                "A patient whose pain is not responding is never left on "
                "the same plan by default -- the reason for a change, or "
                "for holding the plan, is recorded.",
            ],
            oe_code="COP.13.b",
        ),
        PlainItem(
            heading="Rehabilitation scope commensurate with the services of this hospital",
            why="A hospital that lists physiotherapy on the board with a visiting therapist on Tuesdays only, and says nothing else, is holding out a service it cannot deliver on Wednesday.",
            body=[
                "Whether rehabilitation is a defined healthcare service "
                "of this hospital, and which disciplines it includes, "
                "matches the current service directory and department "
                "scopes -- never a copied rehabilitation SOP for a "
                "department this hospital does not have.",
                "Where rehabilitation is a defined service, this "
                "hospital does not exclude a person with disability from "
                "it on the ground of disability, provides barrier-free "
                "access to the areas where it is delivered, and gives "
                "priority in attendance and treatment where the Rights "
                "of Persons with Disabilities Act, 2016 requires it.",
                "Where rehabilitation is not a defined service, that "
                "fact is recorded and the hospital does not display, "
                "advertise or verbally hold out a rehabilitation service "
                "it does not provide; a patient who needs rehabilitation "
                "is referred using the referral route the relevant "
                "department scope already names.",
            ],
            oe_code="COP.13.c",
            technical_sources=[RPWD_SRC],
        ),
        PlainItem(
            heading="Collaborative rehabilitation planning",
            why="A doctor's order that just says 'physio', with no goal and no therapist named, is not collaborative planning -- it is a referral dressed up as a plan.",
            body=[
                "This step operates only where rehabilitation is a "
                "defined service; where it is not, this step is recorded "
                "as not operating, and no plan is invented to imply a "
                "service that does not exist.",
                "Where it operates, the hospital's defined process "
                "captures a plan made with the treating clinician, the "
                "rehabilitation professional, nursing, and the patient "
                "or family as far as they can take part, stating the "
                "goal, the therapy, the frequency this hospital can "
                "actually deliver, and the review.",
                "Internal referral into rehabilitation uses the "
                "continuity policy's referral method; this step owns "
                "only the plan that follows.",
            ],
            oe_code="COP.13.d",
        ),
        PlainItem(
            heading="Nutritional-risk screening and at-risk assessment",
            why="A safe, licensed kitchen can still serve a full diet to a person who cannot swallow it -- this step is what finds that person before the kitchen is asked to.",
            body=[
                "Every admitted patient is screened using the hospital's "
                "defined nutritional-risk screening method, who performs "
                "it, and by when after admission -- never a meal-order "
                "slip treated as a screen.",
                "A patient flagged by the screen is assessed by the "
                "hospital's defined assessor, who records four "
                "things:",
                "1. Intake.",
                "2. Nutritional findings.",
                "3. Swallowing concern, if present.",
                "4. The problem the therapeutic diet must address.",
                "This admission screen is distinct from antenatal "
                "maternal nutrition and paediatric growth/nutrition "
                "assessment -- both still run on their own patients, "
                "but neither substitutes for this screen.",
            ],
            oe_code="COP.13.e",
        ),
        PlainItem(
            heading="Therapeutic diet planned and provided collaboratively",
            why="A 'soft diet' shouted down a corridor, or changed at the bedside by a relative, is not a collaborative plan -- it is the plan failing at the last step.",
            body=[
                "The treating clinician, dietetics and nursing agree the "
                "diet for a patient who needs one -- including every "
                "patient assessed at risk -- using the hospital's "
                "defined collaborative-planning and kitchen-"
                "communication process.",
                "The kitchen prepares under the support-services "
                "infection-control policy; this step does not restate "
                "food-handler health or holding temperatures.",
                "Provision is confirmed using the hospital's defined "
                "confirmation method, and any refusal by the patient is "
                "recorded and the plan reviewed rather than silently "
                "replaced.",
            ],
            oe_code="COP.13.f",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the COP.13 Records folder).",
    related_documents=[
        "Policy on Pain Management, Rehabilitation Services and Nutritional Therapy (COP.13)",
        "Hospital's Higher-Risk-Patient SOP (COP.12)",
        "Hospital's Support-Services Infection-Control Policy (HIC.3)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if the service "
        "directory adds or removes rehabilitation, if unmanaged pain, an "
        "unscreened admission, or a therapeutic diet that did not reach "
        "the patient exposes a gap, or if the definition-and-display, "
        "kitchen, obstetric, paediatric, medication or assessment "
        "processes this SOP hands work to are revised."
    ),
    full_reference_list=[NABH_COP_CITE.format(code="COP.13"), RPWD_SRC],
)

SOPS = [
    ("SOP_COP.1.a_to_e_uniform_care_telemedicine.docx", COP1),
    ("SOP_COP.2.a_to_k_emergency_ambulance_disaster.docx", COP2),
    ("SOP_COP.3.a_to_d_cardio_pulmonary_resuscitation.docx", COP3),
    ("SOP_COP.4.a_to_d_nursing_care.docx", COP4),
    ("SOP_COP.5.a_to_f_transfusion_blood_blood_components.docx", COP5),
    ("SOP_COP.6.a_to_f_icu_hdu_care.docx", COP6),
    ("SOP_COP.7.a_to_e_safe_obstetric_care.docx", COP7),
    ("SOP_COP.8.a_to_f_paediatric_neonatal_services.docx", COP8),
    ("SOP_COP.9.a_to_e_procedural_sedation.docx", COP9),
    ("SOP_COP.10.a_to_h_anaesthesia_services.docx", COP10),
    ("SOP_COP.11.a_to_j_procedures_operation_theatre.docx", COP11),
    ("SOP_COP.12.a_to_f_higher_risk_patients.docx", COP12),
    ("SOP_COP.13.a_to_f_pain_rehabilitation_nutrition.docx", COP13),
]


def main() -> None:
    for fname, spec in SOPS:
        out_path = OUT_ROOT / fname
        build_sop_v2(spec, out_path)
        print(f"built {out_path} (v2: plain body + audit appendix)")


if __name__ == "__main__":
    main()
