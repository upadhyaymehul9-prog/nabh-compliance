# -*- coding: utf-8 -*-
"""Rebuilds the 11 existing HRM SOPs in the plain-body + audit-appendix
format approved for FMS.2 and already applied to FMS, ROM and AAC
(2026-10-12).

No build script existed for HRM -- every fact, citation and URL below is
read directly off the live committed .docx (dumped via python-docx,
including hyperlink relationships) on 2026-10-12. No new citation or
number is introduced.

HRM.7/8/9 each carry a "Stop-Work Authority" block in the live SOP (a
staff member who cannot confirm credentialing does not let that
professional work unsupervised). There is no dedicated field for this in
SOPSpecV2, so it is folded in as a final plain-language procedure item
("Know when to stop care") -- which is exactly what it is: a step staff
take, with a safety-framed reason, not an appendix technicality.

Writes over the existing committed paths in place; does not touch Records.
"""
from __future__ import annotations

from pathlib import Path

from sop_record_common import PlainItem, SOPSpecV2, build_sop_v2

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "HRM"

NABH_HRM_CITE = (
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). "
    "Human Resource Management chapter, standard {code}."
)

NMC_PRACTICE_SRC = (
    "National Medical Commission. (2023, May 10). [Registration of Medical "
    "Practitioners and Licence to Practice Medicine Regulations, "
    "2023](https://nmc.org.in/page/rules-regulations-rules-regulations-nmc). "
    "Under Regulation 8(iii), a practitioner whose registration lapses "
    "(renewal not applied for in time, for example) is not entitled to "
    "practise medicine -- referenced here for verifying a doctor's "
    "current, active registration before appointment."
)
INC_ACT_SRC = (
    "Government of India. (1947). [The Indian Nursing Council Act, "
    "1947](https://nhsrcindia.org/sites/default/files/2021-05/Indian%20Nursing%20Council%20Act-1947.pdf). "
    "Section 11(1)(b) provides that no person may be enrolled on a State "
    "nursing register without a recognised nursing qualification -- "
    "referenced here for verifying a nurse's current State/Indian "
    "Nursing Council registration."
)
ISO_ROLES_SRC = (
    "International Organization for Standardization. (2026). [ISO "
    "9001:2026, Quality management systems — "
    "Requirements](https://www.iso.org/standard/88464.html), clause 5.3 "
    "(Organizational roles, responsibilities and authorities). Referenced "
    "as an external benchmark for what a role description should define; "
    "SHCO accreditation does not itself require ISO 9001 certification."
)
POSH_ACT_SRC = (
    "Government of India. (2013). [The Sexual Harassment of Women at "
    "Workplace (Prevention, Prohibition and Redressal) Act, "
    "2013](https://ncte.gov.in/Website/PDF/A2013-14.pdf), Section 11(4), "
    "requires an Internal Committee to complete its inquiry within ninety "
    "days. Cited as the real statutory basis for a bounded Indian "
    "workplace investigation deadline for harassment complaints "
    "specifically; this SOP applies the same discipline -- a stated, "
    "enforced timeline -- to disciplinary and grievance matters "
    "generally, not as a claim that the 90-day figure governs every case "
    "type."
)
BCLS_SRC = (
    "Garg, R., Ahmed, S. M., Kapoor, M. C., Mishra, B. B., Rao, S. S. C., "
    "Kalandoor, M. V., Divatia, J. V., & Singh, B. (2017). Basic "
    "cardiopulmonary life support (BCLS) for cardiopulmonary resuscitation "
    "by trained paramedics and medics outside the hospital. [Indian "
    "Journal of Anaesthesia, 61(11), 874–882](https://doi.org/10.4103/ija.ija_637_17). "
    "Part of the Indian Society of Anaesthesiologists' national CPR "
    "practice-guideline series; referenced as the Indian clinical "
    "benchmark for CPR training content and refresher intervals, not as "
    "an NABH mandate."
)
OSH_CODE_SRC = (
    "Government of India. (2020). [The Occupational Safety, Health and "
    "Working Conditions Code, 2020](https://www.indiacode.nic.in/bitstream/123456789/22041/1/2020-37.pdf) "
    "(Act No. 37 of 2020). Section 6(2)(c) requires an employer to "
    "provide information, instruction, training and supervision necessary "
    "to ensure employee health and safety at work -- the statutory basis "
    "for occupational safety training, alongside the NABH requirement."
)
COMPENSATION_ACT_SRC = (
    "Government of India. (1923, amended 2017). [The Employee's "
    "Compensation Act, 1923](https://labour.gov.in/sites/default/files/ec_act.pdf). "
    "Section 3(1) makes an employer liable to pay compensation for a "
    "personal injury caused by an accident in the course of employment; "
    "Section 4(2A) requires reimbursement of actual medical expenditure. "
    "Referenced as the statutory basis for the injury-treatment duty, "
    "alongside the NABH requirement."
)
WHO_VIOLENCE_SRC = (
    "World Health Organization, International Labour Organization, "
    "International Council of Nurses, & Public Services International. "
    "(2002). [Framework Guidelines for Addressing Workplace Violence in "
    "the Health Sector](https://www.who.int/publications/i/item/9221134466). "
    "The international framework the prevention and handling measures "
    "(de-escalation training, access control, zero-tolerance policy, "
    "post-event review) follow; referenced as an external benchmark, not "
    "an NABH mandate."
)
DPDP_ACT_SRC = (
    "Government of India. (2023). [The Digital Personal Data Protection "
    "Act, 2023](https://www.indiacode.nic.in/bitstream/123456789/22037/2/a2023-22.pdf) "
    "(Act No. 22 of 2023). Section 8(5) requires a Data Fiduciary to "
    "protect personal data through reasonable security safeguards; "
    "Section 7(i) permits processing personal data for employment "
    "purposes. Referenced as the statutory basis for securing and "
    "controlling access to staff personal files, alongside the NABH "
    "requirement."
)
NMC_ACT_SRC = (
    "Government of India. (2019). [The National Medical Commission Act, "
    "2019](https://www.indiacode.nic.in/handle/123456789/11820) (Act No. "
    "30 of 2019). Section 34(1) (\"Bar to practice\") prohibits anyone not "
    "enrolled in the State Register or National Register from practising "
    "medicine or holding a post as a physician or surgeon; Section 34(2) "
    "sets criminal penalties for contravention. This is the statutory "
    "basis the entire credentialing, privileging and stop-work structure "
    "in this SOP enforces."
)
PHARMACY_ACT_SRC = (
    "Government of India. (1948, amended 2026). [The Pharmacy Act, "
    "1948](https://www.indiacode.nic.in/bitstream/123456789/1364/1/a194808.pdf) "
    "(Act No. 8 of 1948). Section 42 restricts compounding, preparing, "
    "mixing or dispensing medicine on prescription to a registered "
    "pharmacist. Referenced as the statutory basis for verifying a "
    "pharmacist's State Pharmacy Council registration before granting "
    "dispensing privileges."
)
AERB_RULES_SRC = (
    "Department of Atomic Energy, Government of India. (2004). [The "
    "Atomic Energy (Radiation Protection) Rules, 2004](https://mgw3.aerb.gov.in/images/PDF/RPR2004.pdf) "
    "(G.S.R. 303). Rule 3(2) requires radiation-generating equipment to "
    "be operated only under a licence's terms; Rule 12(2) requires the "
    "licensee to ensure only individuals named in the licence handle the "
    "source; Rule 7(2)(e)(ii) conditions the licence on workers having "
    "appropriate radiation-safety training. Referenced as the statutory "
    "basis for naming and training-verifying a radiographer before "
    "granting equipment-operation privileges."
)

# --------------------------------------------------------------- HRM.1.b ---
HRM1B = SOPSpecV2(
    sop_no="SOP-HRM.1.b",
    title="Staff Recruitment",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» recruits staff against "
        "written, approved guidance, verifies a clinical candidate's "
        "professional registration before appointment, and manages an "
        "urgent vacancy filled under interim arrangements -- so every "
        "hire follows the same transparent process, including the "
        "exceptions, rather than an informal decision written up "
        "afterward."
    ),
    purpose_trigger=(
        "A ward loses a nurse overnight and the shift genuinely cannot "
        "wait for a full recruitment cycle. This SOP is what lets the "
        "Medical Superintendent approve a documented interim appointment "
        "-- with registration still verified before the person starts -- "
        "rather than the gap being filled off the books."
    ),
    purpose_why=(
        "We do this because a doctor whose registration has lapsed, or a "
        "nurse who was never enrolled on a State nursing register, is not "
        "legally entitled to practise -- an interview score alone says "
        "nothing about this, and finding out after appointment is too "
        "late, for the patient and for the organisation."
    ),
    purpose_text=(
        "To define how «Hospital Name» recruits staff against written "
        "guidance, verifies professional registration before appointing a "
        "clinical candidate, and manages an urgent vacancy filled under "
        "interim arrangements. It does not cover job descriptions, code "
        "of conduct, or induction."
    ),
    scope_why="so every category of staff being recruited -- including doctors and nurses whose registration must be checked -- goes through the same gate.",
    scope_text=(
        "Applies to the HR In-Charge, the Medical Superintendent, and "
        "department heads, for every category of staff being recruited, "
        "including doctors and nurses whose professional registration "
        "must be verified before appointment."
    ),
    responsibility_why="a vacancy filled without a documented reason, or a registration nobody actually checked, is a gap that only surfaces after someone is already working.",
    responsibilities=[
        ("HR In-Charge / Personnel Officer", "Owns the recruitment register, runs the process end to end, verifies professional registration for clinical candidates, and keeps the register current."),
        ("Medical Superintendent", "Approves the recruitment procedure, is the escalation point for any step that cannot be completed as written, and approves any interim appointment made under urgent-vacancy provisions."),
        ("Department Heads", "Raise the vacancy requisition, sit on or nominate the interview panel, and confirm the role's requirements before advertising starts."),
        ("Quality Coordinator", "Audits the recruitment register periodically and flags any vacancy filled without a documented rationale, or an interim appointment not regularised within the defined period."),
    ],
    items=[
        PlainItem(
            heading="Raise and approve the vacancy",
            why="A vacancy filled without a documented reason is the first point where recruitment stops being transparent.",
            body=[
                "The department head raises a vacancy requisition "
                "stating the role, department, and justification "
                "(replacement, new service, workload).",
                "The Medical Superintendent approves the requisition "
                "before advertising or sourcing begins.",
                "The HR In-Charge opens a new entry in the recruitment "
                "register against the approved requisition.",
            ],
            oe_code="HRM.1.b",
        ),
        PlainItem(
            heading="Shortlist and interview against defined criteria",
            why="Deciding who gets shortlisted or selected without a stated reason is exactly how an unqualified or unverified candidate can be chosen informally.",
            body=[
                "Candidates are shortlisted against the qualifications "
                "and experience stated in the requisition, not by "
                "informal preference.",
                "An interview panel of at least two people, including "
                "the relevant department head, interviews shortlisted "
                "candidates.",
                "The panel records its selection rationale in the "
                "register at the time of decision, not reconstructed "
                "afterward.",
            ],
            oe_code="HRM.1.b",
        ),
        PlainItem(
            heading="Verify professional registration before appointing a doctor or nurse",
            why="A doctor whose registration has lapsed, or a nurse who was never enrolled on a State nursing register, is not legally entitled to practise -- an interview score alone says nothing about this, and finding out after appointment is too late.",
            body=[
                "For any candidate for a doctor's post, the HR In-Charge "
                "verifies current, active registration on the National "
                "Medical Register or the relevant State Medical Council "
                "before an offer is made.",
                "For any candidate for a nurse's post, the HR In-Charge "
                "verifies current enrolment on the Indian Nursing "
                "Council's register or the relevant State Nursing "
                "Council before an offer is made.",
                "Where registration cannot be verified, or is found "
                "lapsed or suspended, the offer is withheld and the "
                "reason is logged; the candidate is not appointed to a "
                "clinical role until registration is confirmed current.",
            ],
            oe_code="HRM.1.b",
            technical_sources=[NMC_PRACTICE_SRC, INC_ACT_SRC],
        ),
        PlainItem(
            heading="Offer, log, and close the vacancy",
            why="A register that is updated only when someone asks for it is not evidence of a transparent process -- closing the loop in writing, at the time it happens, is what makes the record trustworthy.",
            body=[
                "The HR In-Charge issues the offer and records the "
                "candidates considered and the fill date in the "
                "register.",
                "The vacancy is marked closed in the register once the "
                "candidate joins, or reopened if the offer is declined.",
                "The Medical Superintendent reviews the recruitment "
                "procedure annually and signs off any changes.",
            ],
            oe_code="HRM.1.b",
        ),
        PlainItem(
            heading="Fill an urgent vacancy under interim arrangements",
            why="A vacancy that genuinely cannot wait for the full process -- a sudden resignation leaving a shift uncovered -- cannot be allowed to bypass recruitment altogether; it has to be filled on a documented interim basis and then regularised, not left as an undocumented exception.",
            body=[
                "Where a vacancy must be filled before the full "
                "recruitment process can be completed, the Medical "
                "Superintendent approves an interim appointment in "
                "writing, stating the reason and the maximum interim "
                "period.",
                "Credential and, for clinical roles, registration "
                "verification is still completed before the interim "
                "appointee starts work -- this step is never skipped, "
                "even under urgency.",
                "The full recruitment process (shortlisting, panel "
                "interview, selection rationale) is completed within the "
                "stated interim period, and the appointment is either "
                "regularised or ended.",
            ],
            oe_code="HRM.1.b",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-3 (see the HRM.1 Records folder).",
    related_documents=[
        "Policy on Human Resource Planning, Recruitment and Staff Governance (HRM.1)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the HR In-Charge, and sooner if an audit or a "
        "hiring decision finds it is not being followed as written, or an "
        "interim appointment is not regularised within its stated period."
    ),
    full_reference_list=[NABH_HRM_CITE.format(code="HRM.1"), NMC_PRACTICE_SRC, INC_ACT_SRC],
)

# --------------------------------------------------------------- HRM.1.e ---
HRM1E = SOPSpecV2(
    sop_no="SOP-HRM.1.e",
    title="Reporting Relationships, Job Specification and Job Description",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» defines, documents, and "
        "keeps current the reporting relationship, job specification and "
        "job description for every category of staff, including what "
        "happens if an employee refuses to sign and how a reporting-line "
        "change is propagated to every job description it affects -- so "
        "every employee knows who they report to, what the role requires, "
        "and what they are accountable for, in writing rather than by "
        "custom."
    ),
    purpose_trigger=(
        "A department is restructured and one role's reporting line "
        "changes. This SOP is what gets every other job description that "
        "names that role as a reporting line reissued together -- not "
        "just the one role that actually changed, leaving the rest "
        "quietly out of date."
    ),
    purpose_why=(
        "We do this because a job description that is missing the "
        "reporting line, qualifications, or performance indicators cannot "
        "be used to settle a dispute about who is accountable for what -- "
        "and an employee who first learns what their role requires only "
        "when something goes wrong was never actually told."
    ),
    purpose_text=(
        "To define how «Hospital Name» defines, documents and keeps "
        "current the reporting relationship, job specification and job "
        "description for every category of staff, including a signature "
        "refusal and propagating a reporting-line change."
    ),
    scope_why="so every department head -- not just HR -- is responsible for keeping their own roles' job descriptions accurate.",
    scope_text="Applies to the HR In-Charge and every department head, for every category of staff: clinical, nursing, administrative and support.",
    responsibility_why="a job description nobody drafted, signed or kept current is not actually in force, whatever the file says.",
    responsibilities=[
        ("HR In-Charge / Personnel Officer", "Owns the job description template, files the signed copy in each employee's personnel file, tracks the annual review, and escalates an unsigned job description."),
        ("Department Heads", "Draft and keep current the job description for roles in their department, confirm the stated reporting line is accurate, and identify every job description affected when a reporting line changes."),
        ("Medical Superintendent", "Approves the job description template, any change to a reporting relationship above department level, and decides the outcome where a staff member refuses to sign."),
    ],
    items=[
        PlainItem(
            heading="Define the template",
            why="A job description that is missing the reporting line, qualifications, or performance indicators cannot be used to settle a dispute about who is accountable for what -- the template has to carry all of it, every time.",
            body=[
                "The HR In-Charge maintains one job description template "
                "covering: designation, department, reporting line, key "
                "responsibilities, qualifications required, and "
                "performance indicators.",
                "The Medical Superintendent approves the template and "
                "any structural change to it.",
            ],
            oe_code="HRM.1.e",
            technical_sources=[ISO_ROLES_SRC],
        ),
        PlainItem(
            heading="Issue and sign at joining",
            why="A job description that is never signed cannot later prove the employee was ever told what the role required -- the signature at joining is what makes the record usable if a dispute comes up.",
            body=[
                "The department head completes the job description for "
                "the specific role before the new hire's start date.",
                "The new hire signs the job description at induction, "
                "confirming they have received and understood it.",
                "The HR In-Charge files the signed copy in the "
                "employee's personnel file.",
            ],
            oe_code="HRM.1.e",
        ),
        PlainItem(
            heading="Handle a refusal to sign",
            why="An employee who refuses to sign cannot simply be left unsigned indefinitely -- an unsigned job description is functionally the same gap as never having issued one at all, so the refusal itself has to be documented and escalated, not quietly dropped.",
            body=[
                "Where an employee declines to sign, the department head "
                "records the refusal and the stated reason, and "
                "escalates to the HR In-Charge the same day.",
                "The Medical Superintendent reviews the refusal and "
                "decides the outcome -- clarifying the job description, "
                "formally noting the employee's objection on file, or "
                "another resolution -- within a defined period.",
                "The personnel file records both the refusal and how it "
                "was resolved; it is never left as simply 'not signed' "
                "with no explanation.",
            ],
            oe_code="HRM.1.e",
        ),
        PlainItem(
            heading="Review annually, and propagate a reporting-line change",
            why="A job description that is never revisited drifts away from what the person actually does -- and a reporting-line change made for one role often affects several other job descriptions that reference it, not just the one role that changed.",
            body=[
                "Department heads review every job description in their "
                "department annually, or immediately when a role "
                "changes.",
                "When a reporting line changes, the department head "
                "identifies every other job description that names the "
                "changed role as a reporting line, and reissues all of "
                "them together, not just the one role that changed.",
                "Any change is re-signed by the employee and re-filed; "
                "the HR In-Charge tracks which job descriptions are due "
                "for review and escalates overdue ones to the department "
                "head.",
            ],
            oe_code="HRM.1.e",
        ),
    ],
    records_note="This SOP produces and maintains Records 4-6 (see the HRM.1 Records folder).",
    related_documents=[
        "Policy on Human Resource Planning, Recruitment and Staff Governance (HRM.1)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the HR In-Charge, and sooner if an audit finds a "
        "job description missing or unsigned in a personnel file, or a "
        "reporting-line change was not propagated to every job "
        "description it affected."
    ),
    full_reference_list=[NABH_HRM_CITE.format(code="HRM.1"), ISO_ROLES_SRC],
)

# --------------------------------------------------------------- HRM.1.i ---
HRM1I = SOPSpecV2(
    sop_no="SOP-HRM.1.i",
    title="Disciplinary and Grievance Handling",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» handles staff misconduct "
        "and staff grievances against written guidance, including interim "
        "action to protect patients or staff while a serious matter is "
        "investigated, protection of a complainant from retaliation, and "
        "escalation if an investigation breaches its stated timeline -- "
        "so both are investigated, decided and closed consistently rather "
        "than handled case by case with no documented process."
    ),
    purpose_trigger=(
        "A staff member reports a serious safety concern about a "
        "colleague and worries about retaliation for speaking up. This SOP "
        "is what puts in writing, immediately, that retaliation will "
        "itself be treated as a disciplinary matter -- not left as an "
        "unspoken risk the complainant has to weigh alone."
    ),
    purpose_why=(
        "We do this because leaving a staff member accused of a serious "
        "matter in their normal role while the investigation runs can "
        "itself cause harm, and a complainant who fears retaliation for "
        "having raised the matter may not come forward at all -- which "
        "undermines the investigation before it starts."
    ),
    purpose_text=(
        "To define how «Hospital Name» handles staff misconduct and "
        "grievances, including interim action, complainant protection, "
        "and escalation of a timeline breach."
    ),
    scope_why="so every staff member who raises a grievance or is the subject of a disciplinary matter is handled through the same process.",
    scope_text="Applies to the HR In-Charge, the Medical Superintendent, and department heads, for every staff member who raises a grievance or is the subject of a disciplinary matter.",
    responsibility_why="a case with no deadline and no named decision-maker drifts indefinitely, which is unfair to everyone involved.",
    responsibilities=[
        ("HR In-Charge / Personnel Officer", "Maintains the grievance register and the disciplinary proceedings register, assigns a case number to every new complaint on receipt, and tracks every case against its stated timeline."),
        ("Medical Superintendent", "Approves the disciplinary and grievance procedure, decides any interim action needed to protect patients or staff during an investigation, chairs or nominates the hearing for serious matters, decides the appeal route, and personally reviews any case that breaches its investigation timeline."),
        ("Department Heads", "Receive and escalate grievances raised in their department within the stated timeline, and cooperate with any investigation."),
    ],
    items=[
        PlainItem(
            heading="Receive and log",
            why="A grievance or a disciplinary matter that is handled verbally, with no case number and no date, cannot later be shown to have followed any consistent process at all.",
            body=[
                "Every grievance is logged in the grievance register "
                "with a unique case number and the date received, on the "
                "same day it is reported.",
                "Every disciplinary matter is logged in the disciplinary "
                "proceedings register with the same day's date and a "
                "brief statement of the alleged conduct.",
                "The HR In-Charge confirms confidentiality applies to "
                "both registers from the point of logging.",
            ],
            oe_code="HRM.1.i",
        ),
        PlainItem(
            heading="Take interim action for a serious allegation",
            why="Leaving a staff member accused of a serious matter -- one that could put a patient or colleague at risk -- in their normal role while the investigation runs can itself cause harm; interim action has to be a deliberate decision made at the point of logging, not an afterthought.",
            body=[
                "Where the alleged conduct could put a patient or staff "
                "member at risk if it continued, the Medical "
                "Superintendent decides, at the point the matter is "
                "logged, whether interim action -- reassignment, "
                "restricted duties, or administrative leave -- is needed "
                "pending investigation.",
                "Any interim action taken, and the reason for it, is "
                "recorded against the case number; interim action is not "
                "a finding of guilt and is stated as such in writing to "
                "the staff member.",
                "Interim action is reviewed if the investigation "
                "timeline is extended, rather than left in place "
                "indefinitely by default.",
            ],
            oe_code="HRM.1.i",
        ),
        PlainItem(
            heading="Investigate within a defined timeline, and protect the complainant",
            why="An investigation with no deadline tends to drift indefinitely, which is itself unfair to both the complainant and the person being investigated -- and a complainant who fears retaliation may not come forward honestly, or at all.",
            body=[
                "The procedure states the investigation timeline and who "
                "conducts it for each type of matter.",
                "The investigator records the steps taken and the "
                "evidence gathered against the case number.",
                "The complainant is informed in writing that retaliation "
                "for raising the matter in good faith will itself be "
                "treated as a disciplinary matter, and any report of "
                "retaliation during the investigation is logged and "
                "acted on immediately, separately from the original "
                "case.",
                "Where a hearing is required, the Medical Superintendent "
                "or nominee convenes it within the stated timeline.",
            ],
            oe_code="HRM.1.i",
            technical_sources=[POSH_ACT_SRC],
        ),
        PlainItem(
            heading="Escalate a timeline breach",
            why="A case that silently runs past its stated deadline, with nobody above the investigator noticing, defeats the entire point of having a stated timeline in the first place.",
            body=[
                "Where an investigation is not completed within its "
                "stated timeline, the HR In-Charge escalates the case to "
                "the Medical Superintendent before the deadline lapses, "
                "not after.",
                "The Medical Superintendent either approves a documented "
                "extension with a new deadline, or directs that the "
                "investigation be concluded immediately on the evidence "
                "available.",
            ],
            oe_code="HRM.1.i",
        ),
        PlainItem(
            heading="Decide, close, and allow appeal",
            why="A case that is decided but never closed in writing, with no stated appeal route, leaves both the organisation and the staff member with no record of how the matter actually ended.",
            body=[
                "The outcome -- including any penalty, or the grievance "
                "resolution, and the closure or continuation of any "
                "interim action -- is recorded against the case number "
                "with the closure date.",
                "The staff member is informed in writing of the outcome "
                "and of the appeal route available to them.",
                "The HR In-Charge confirms the register entry is marked "
                "closed only once the appeal window has passed or the "
                "appeal is decided.",
            ],
            oe_code="HRM.1.i",
        ),
    ],
    records_note="This SOP produces and maintains Records 7-10 (see the HRM.1 Records folder).",
    related_documents=[
        "Policy on Human Resource Planning, Recruitment and Staff Governance (HRM.1)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the HR In-Charge, and sooner if a case reveals the "
        "timeline or the appeal route was not followed as written, or an "
        "interim-action decision was not made or reviewed as this SOP "
        "requires."
    ),
    full_reference_list=[NABH_HRM_CITE.format(code="HRM.1"), POSH_ACT_SRC],
)

# --------------------------------------------------------------- HRM.2 ---
HRM2 = SOPSpecV2(
    sop_no="SOP-HRM.2.a",
    title="Induction, Training and Development",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» inducts every new staff "
        "member, runs an ongoing training and development programme "
        "against written guidance, trains staff against their own job "
        "description, delivers CPR training to direct patient care staff "
        "at induction and on a refresher cycle, and evaluates whether "
        "training actually changes practice -- so training is a tracked, "
        "scheduled programme with evidence of effect, not a one-off "
        "session remembered only as attendance on a sheet."
    ),
    purpose_trigger=(
        "A direct patient care staff member's CPR certification quietly "
        "expires without anyone noticing. This SOP is what sends a "
        "reminder 30 days beforehand and stops that person working "
        "unsupervised past expiry -- not a certificate that goes stale on "
        "file until a resuscitation reveals the gap."
    ),
    purpose_why=(
        "We do this because a staff member who starts working before "
        "induction is complete has had no structured introduction to "
        "safety reporting or patient rights, and a direct patient care "
        "staff member whose CPR certification has quietly expired is, in "
        "the moment a patient needs resuscitation, no different from one "
        "who was never trained."
    ),
    purpose_text=(
        "To define how «Hospital Name» inducts new staff, runs training "
        "and development against written guidance, trains staff against "
        "their job description, delivers CPR training and refreshers, and "
        "evaluates training effectiveness."
    ),
    scope_why="so every staff category -- clinical, nursing, administrative and support -- is covered by the same tracked training programme.",
    scope_text=(
        "Applies to the Training Coordinator, the HR In-Charge, "
        "department heads, the Medical Superintendent and the Quality "
        "Coordinator, for every staff category."
    ),
    responsibility_why="training nobody tracks, or a lapsed CPR certification nobody catches, is a gap that only shows up when it's too late.",
    responsibilities=[
        ("Medical Superintendent", "Approves the training and development policy and the annual training calendar, and reviews the annual training effectiveness report."),
        ("Training Coordinator", "Maintains the induction checklist, the training calendar, the job-description training matrix, and the master CPR competency register; coordinates sessions and evaluates effectiveness."),
        ("HR In-Charge / Personnel Officer", "Confirms induction is completed for every new hire within the stated period and files completion forms and training certificates in personnel files."),
        ("Department Heads", "Confirm role-specific induction items and job-description-based training are actually covered for staff in their department, and supervise the practice change training is meant to produce."),
        ("Quality Coordinator", "Audits this SOP quarterly, in particular whether any new hire worked unsupervised before induction was complete, and whether any direct patient care staff member's CPR certification lapsed."),
    ],
    items=[
        PlainItem(
            heading="Induct every new staff member within the stated period",
            why="A staff member who starts working before induction is complete has had no structured introduction to hospital policy, infection control, patient rights or safety reporting -- induction has to close before unsupervised work starts, not run alongside it.",
            body=[
                "The induction checklist covers hospital mission and "
                "policies (including the code of conduct and grievance "
                "mechanism), department orientation, role-specific "
                "briefing, infection-control basics, patient rights, and "
                "safety reporting.",
                "Induction is completed within the first week of "
                "joining, before the new hire works unsupervised.",
                "The new hire and their supervisor sign an induction "
                "completion form, filed in the personnel file.",
            ],
            oe_code="HRM.2.a",
        ),
        PlainItem(
            heading="Run training and development against written, approved guidance",
            why="Training delivered only as ad-hoc sessions when a problem has already occurred is reactive, not a programme -- written guidance and a published annual calendar are what make training something staff can plan around rather than something sprung on them.",
            body=[
                "A written training and development policy covers "
                "training needs assessment, mandatory training "
                "frequencies, nomination and approval, budget provision, "
                "documentation requirements, and external training "
                "approval.",
                "The Training Coordinator maintains an annual training "
                "calendar -- topics, target groups, trainers, dates and "
                "venues -- shared with every department.",
                "The Medical Superintendent approves the policy and the "
                "calendar, and reviews both at least annually.",
            ],
            oe_code="HRM.2.b",
        ),
        PlainItem(
            heading="Train every staff member against their own job description",
            why="A single training lecture delivered identically to every department cannot actually close the specific competency gaps a billing clerk, a staff nurse and a lab technician each have -- training has to be mapped to what the role's own job description actually requires.",
            body=[
                "The Training Coordinator maintains a training matrix "
                "mapping each staff category's job description to its "
                "mandatory competencies and the training programmes that "
                "deliver them.",
                "Before each training cycle, HR cross-checks completed "
                "training against the matrix and schedules any gap "
                "found.",
                "Department heads confirm role-specific competencies are "
                "actually met quarterly, not assumed from attendance "
                "alone.",
            ],
            oe_code="HRM.2.c",
        ),
        PlainItem(
            heading="Deliver CPR training at induction and on a refresher cycle",
            why="A direct patient care staff member whose CPR certification has quietly expired is, in the moment a patient needs resuscitation, no different from one who was never trained -- the expiry date is the point this step exists to never let pass unnoticed.",
            body=[
                "Every direct patient care staff member receives CPR "
                "training at induction and on a periodic refresher cycle "
                "-- every 12 months -- covering adult basic life support "
                "and AED use where equipment is available.",
                "The master CPR competency register tracks each "
                "person's certification date and expiry date.",
                "Reminders are sent 30 days before expiry, and no direct "
                "patient care staff member continues to work with an "
                "expired CPR certification.",
            ],
            oe_code="HRM.2.d",
            technical_sources=[BCLS_SRC],
        ),
        PlainItem(
            heading="Evaluate whether training actually changed practice",
            why="Attendance at a training session proves someone was in the room, not that they learned anything or do their job differently afterward -- evaluation is what tells the hospital whether the training programme is actually working, or just running.",
            body=[
                "Training effectiveness is evaluated through "
                "post-training knowledge checks, supervisor observation "
                "of practice change, and training feedback forms.",
                "The Training Coordinator reviews training completion "
                "rates against the matrix at least annually and prepares "
                "an annual training effectiveness report for the Medical "
                "Superintendent and governing body.",
                "Findings from the report drive actual changes to the "
                "training calendar, curriculum or delivery method -- not "
                "just a filed report with no follow-up action.",
            ],
            oe_code="HRM.2.e",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-5 (see the HRM.2 Records folder).",
    related_documents=[
        "Policy on Induction, Training and Development (HRM.2)",
        "SOP — Reporting Relationships, Job Specification and Job Description (HRM.1.e)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Training Coordinator, and sooner if the "
        "quarterly audit finds a new hire who worked unsupervised before "
        "induction was complete, a direct patient care staff member with "
        "an expired CPR certification, or a training effectiveness report "
        "with no follow-up action taken on its findings."
    ),
    full_reference_list=[NABH_HRM_CITE.format(code="HRM.2"), BCLS_SRC],
)

# --------------------------------------------------------------- HRM.3 ---
HRM3 = SOPSpecV2(
    sop_no="SOP-HRM.3.a",
    title="Safety, Disaster, Fire and Quality-Improvement Training",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» delivers training on the "
        "safety programme, risk detection and handling, incident "
        "procedures, occupational safety, the disaster management plan, "
        "fire and non-fire emergencies, and the quality improvement "
        "programme. This SOP owns training delivery only -- the "
        "programmes themselves are defined elsewhere."
    ),
    purpose_trigger=(
        "A fire drill reveals that several staff on a ward don't know the "
        "evacuation route or the assembly point. This SOP is what gets "
        "that training refreshed immediately after the drill -- not left "
        "until the next scheduled annual session, by which point the gap "
        "has already been tested for real."
    ),
    purpose_why=(
        "We do this because a staff member who has never been told what "
        "the hospital's safety structure is, or what their own role in a "
        "fire or disaster is, cannot be expected to respond correctly "
        "when it matters most -- and a disaster plan that exists only as "
        "a document, never rehearsed, fails exactly when it is needed."
    ),
    purpose_text=(
        "To define how «Hospital Name» delivers safety, risk, incident, "
        "occupational safety, disaster, fire/non-fire and quality-"
        "improvement training."
    ),
    scope_why="so every staff member -- not just department heads -- actually receives this training, since every staff member has a role in an emergency.",
    scope_text="Applies to the Training Coordinator, department heads, the Medical Superintendent, the Quality Coordinator, and every staff member.",
    responsibility_why="training that only department heads understand is training that misses the person most likely to actually witness or respond to the event.",
    responsibilities=[
        ("Medical Superintendent", "Ensures safety, disaster and emergency training is resourced and conducted, and participates in disaster and fire drills."),
        ("Training Coordinator", "Schedules and records every training session covered by this SOP and coordinates with the Quality Coordinator for QI and incident-awareness training."),
        ("Quality Coordinator", "Delivers or coordinates QI programme and incident-awareness training content, and audits this SOP quarterly."),
        ("Department Heads", "Ensure unit-specific risk and occupational safety content is covered and confirm all staff in their department complete required training."),
        ("All Staff", "Complete safety, incident, disaster, fire and QI training at induction and on every refresher cycle."),
    ],
    items=[
        PlainItem(
            heading="Deliver safety-programme training",
            why="A staff member who has never been told what the hospital's safety structure actually is, or what their own role in it is, cannot be expected to follow it when it matters.",
            body=[
                "Safety-programme training is scheduled at induction and "
                "annually, covering the hospital safety structure, staff "
                "roles in safety, reporting channels, and key safety "
                "policies the hospital has adopted.",
                "Training attendance is recorded in the training matrix.",
            ],
            oe_code="HRM.3.a",
        ),
        PlainItem(
            heading="Train staff to detect, handle, minimise and eliminate identified risks",
            why="Generic risk-awareness training that ignores what is actually dangerous on a specific ward or in a specific department teaches nothing a staff member can actually use.",
            body=[
                "Training covers hazard identification in the "
                "workplace, near-miss reporting, basic risk assessment, "
                "and escalation paths.",
                "Department heads tailor content to unit-specific risks "
                "(medication errors in pharmacy, falls in wards, sharps "
                "in procedure areas, for example).",
                "Training is refreshed annually or immediately when a "
                "new risk is identified through the incident system or "
                "the risk register.",
            ],
            oe_code="HRM.3.b",
        ),
        PlainItem(
            heading="Make every staff member aware of incident procedures",
            why="An incident reporting system that only department heads understand misses the person most likely to actually witness the incident -- the front-line staff member.",
            body=[
                "Induction training covers incident definition, the "
                "reporting form or channel, immediate patient-safety "
                "actions, preservation of evidence, and non-retaliation "
                "for reporting.",
                "Refresher training is conducted annually.",
                "Incident reporting posters are displayed in clinical "
                "areas, as a standing reminder between training "
                "sessions.",
            ],
            oe_code="HRM.3.c",
        ),
        PlainItem(
            heading="Train staff in occupational safety aspects relevant to their role",
            why="A generic safety lecture that never mentions manual handling, chemical exposure, electrical hazards or workplace violence leaves staff unprepared for the hazards they will actually encounter in a healthcare setting.",
            body=[
                "Training covers hazards relevant to healthcare workers: "
                "manual handling and ergonomics, chemical exposure, "
                "electrical safety, workplace violence, and infection-"
                "control occupational practices (exposure response).",
                "The Training Coordinator maintains role-specific "
                "occupational safety modules, and department heads "
                "confirm unit hazards are actually covered.",
            ],
            oe_code="HRM.3.d",
            technical_sources=[OSH_CODE_SRC],
        ),
        PlainItem(
            heading="Train staff in the disaster management plan",
            why="A disaster plan that exists only as a document, never rehearsed with the staff who would have to execute it, fails exactly when it is needed most.",
            body=[
                "Disaster training is conducted at induction and "
                "annually, covering the plan's activation triggers, each "
                "staff member's role, evacuation or shelter procedures, "
                "and communication channels.",
                "A tabletop exercise or drill is conducted once a year "
                "per the current disaster management plan.",
                "Attendance and drill outcomes are recorded.",
            ],
            oe_code="HRM.3.e",
        ),
        PlainItem(
            heading="Train staff in fire and non-fire emergency response",
            why="Staff who do not know the alarm signal, the evacuation route or the assembly point cannot respond safely in the first minutes of a fire, when those minutes matter most.",
            body=[
                "Training covers alarm signals, evacuation routes, "
                "assembly points, use of fire extinguishers where "
                "trained, and non-fire emergency responses such as "
                "utility failure or gas leak.",
                "Training is conducted at induction and refreshed after "
                "each fire/non-fire drill or annually, whichever is "
                "sooner.",
                "Drill attendance is cross-checked against the "
                "facility's drill records.",
            ],
            oe_code="HRM.3.f",
        ),
        PlainItem(
            heading="Train staff in the quality improvement programme",
            why="A quality improvement programme that only the Quality Coordinator understands produces reports nobody else acts on; QI only works when the staff who do the work can actually participate in it.",
            body=[
                "Training covers the purpose of QI, how to identify "
                "improvement opportunities, how to participate in "
                "audits, and how the hospital's corrective and "
                "preventive action process works.",
                "Department heads and clinical staff receive QI training "
                "at induction and annually, delivered or coordinated by "
                "the Quality Coordinator.",
                "Training covers the indicator dashboard at a level "
                "appropriate to each role.",
            ],
            oe_code="HRM.3.g",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-7 (see the HRM.3 Records folder).",
    related_documents=[
        "Policy on Safety, Disaster, Fire and Quality-Improvement Training (HRM.3)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Training Coordinator, and sooner when the "
        "disaster management plan, fire/non-fire emergency plans, or the "
        "QI/incident programmes are revised, or the quarterly audit finds "
        "a staff member who could not describe the incident reporting "
        "procedure."
    ),
    full_reference_list=[NABH_HRM_CITE.format(code="HRM.3"), OSH_CODE_SRC],
)

# --------------------------------------------------------------- HRM.4.a ---
HRM4A = SOPSpecV2(
    sop_no="SOP-HRM.4.a",
    title="Performance Appraisal",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» makes every staff member "
        "aware of the performance appraisal system at induction, runs the "
        "appraisal cycle against pre-determined criteria, and manages an "
        "appraisal that finds unsatisfactory performance through a "
        "documented improvement plan, rather than filing a low score away "
        "with no follow-up."
    ),
    purpose_trigger=(
        "An appraisal finds a staff member's performance unsatisfactory. "
        "This SOP is what opens a documented improvement plan the same "
        "day, naming the specific gaps and a follow-up date -- not a low "
        "score filed away with no next step for the employee."
    ),
    purpose_why=(
        "We do this because a staff member who first hears about "
        "appraisal at their first review has had no chance to understand "
        "what they are being measured against, and an unsatisfactory "
        "appraisal with no follow-up gives the employee no real chance to "
        "improve."
    ),
    purpose_text=(
        "To define how «Hospital Name» covers appraisal awareness at "
        "induction, runs the appraisal cycle against pre-determined "
        "criteria, and opens a performance improvement plan where "
        "performance is unsatisfactory."
    ),
    scope_why="so every staff category knows the same appraisal process applies to them from day one.",
    scope_text=(
        "Applies to the HR In-Charge, department heads, and the Medical "
        "Superintendent, for every staff category except the person "
        "heading the organisation, whose performance review is owned by "
        "the governing body."
    ),
    responsibility_why="an appraisal that nobody tracks, or a low score with no improvement plan, helps neither the employee nor the organisation.",
    responsibilities=[
        ("HR In-Charge / Personnel Officer", "Confirms appraisal awareness is covered at every induction, maintains the appraisal schedule, tracks overdue appraisals, and escalates an appraisal overdue by more than one month to the Medical Superintendent."),
        ("Department Heads", "Conduct appraisals for staff in their department against the pre-determined criteria, sign off the completed form, and open a performance improvement plan where the appraisal finds unsatisfactory performance."),
        ("Medical Superintendent", "Approves the appraisal form template, conducts appraisal of department heads, and personally reviews any performance improvement plan that does not show improvement at its follow-up review."),
    ],
    items=[
        PlainItem(
            heading="Cover appraisal awareness at induction",
            why="A staff member who first hears about appraisal at their first review has had no chance to understand what they are being measured against -- awareness has to start at induction, not at the review meeting.",
            body=[
                "Induction includes the purpose of appraisal, the "
                "appraisal cycle, who conducts it, and how criteria are "
                "set.",
                "The new hire signs an induction acknowledgement that "
                "explicitly includes appraisal-system awareness.",
                "The HR In-Charge files the signed acknowledgement in "
                "the personnel file.",
            ],
            oe_code="HRM.4.a",
        ),
        PlainItem(
            heading="Set criteria before the cycle begins",
            why="Criteria decided at the review meeting itself, rather than beforehand, turns the appraisal into a judgment call rather than a measurement against something the employee already knew they'd be assessed on.",
            body=[
                "Appraisal criteria are drawn from the job description "
                "and documented on the appraisal form template before "
                "the cycle starts.",
                "The appraiser and appraisee discuss the criteria at the "
                "start of the cycle, not for the first time at the "
                "review itself.",
            ],
            oe_code="HRM.4.a",
        ),
        PlainItem(
            heading="Conduct, document and schedule",
            why="An appraisal cycle with no tracked schedule is how staff end up going a year or more with no appraisal on file at all -- the schedule is what makes the interval enforceable rather than aspirational.",
            body=[
                "The appraisal cycle runs annually for all staff "
                "categories, with an additional appraisal for "
                "probationary staff at three and six months.",
                "The completed form -- criteria scores, narrative "
                "comments, development plan, and both signatures -- is "
                "filed in the personnel file within two weeks of the "
                "review meeting.",
                "The HR In-Charge maintains the appraisal schedule and "
                "reviews it monthly for any staff member overdue, "
                "escalating an appraisal overdue by more than one month "
                "to the Medical Superintendent.",
            ],
            oe_code="HRM.4.a",
        ),
        PlainItem(
            heading="Open a performance improvement plan where performance is unsatisfactory",
            why="An appraisal that records a low score and simply files it away, with no defined next step, gives the employee no actual chance to improve and gives the organisation no documented basis for any later action if performance doesn't improve.",
            body=[
                "Where an appraisal finds performance unsatisfactory "
                "against the stated criteria, the department head opens "
                "a performance improvement plan the same day, naming the "
                "specific gaps, the support or training to be provided, "
                "and a follow-up review date within the hospital-defined "
                "review period (a specific number of days the hospital "
                "states in its own SOP; no external body prescribes it).",
                "The employee signs the improvement plan, confirming "
                "they have discussed and understood it; a refusal to "
                "sign is recorded the same way as a job description "
                "refusal, and escalated to the Medical Superintendent.",
                "At the follow-up review, the outcome -- improved, "
                "partially improved, or not improved -- is recorded; "
                "where performance has not improved, the Medical "
                "Superintendent reviews the case personally before any "
                "further action is taken.",
            ],
            oe_code="HRM.4.a",
            boundary=[
                "The person heading the organisation is reviewed by the "
                "governing body under ROM.2.d, not under this SOP.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the HRM.4 Records folder).",
    related_documents=[
        "Policy on Performance Appraisal (HRM.4)",
        "SOP — Reporting Relationships, Job Specification and Job Description (HRM.1.e)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the HR In-Charge, and sooner if the monthly "
        "overdue-appraisal review finds a gap of more than one month, or "
        "a performance improvement plan is not opened where an appraisal "
        "found unsatisfactory performance."
    ),
    full_reference_list=[NABH_HRM_CITE.format(code="HRM.4")],
)

# --------------------------------------------------------------- HRM.5 ---
HRM5 = SOPSpecV2(
    sop_no="SOP-HRM.5.a",
    title="Staff Well-Being and Occupational Health",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» identifies staff health "
        "problems and occupational hazards, runs an annual health check "
        "for every active staff member with documented findings, provides "
        "treatment for workplace-related injuries, and prevents and "
        "handles workplace violence. Infection-specific exposure "
        "(needlestick, sharps, splash, post-exposure prophylaxis) is "
        "owned elsewhere and is not duplicated here."
    ),
    purpose_trigger=(
        "A staff member is injured by an aggressive visitor. This SOP is "
        "what guarantees immediate first aid, medical assessment and "
        "documentation at the hospital's own expense -- not a staff "
        "member paying for their own treatment because the incident was "
        "never formally logged."
    ),
    purpose_why=(
        "We do this because a hazard that is never written down is a "
        "hazard the hospital has no way of proving it ever addressed, and "
        "a staff member injured on the job who has to pay for their own "
        "treatment has no protection and the hospital has no record to "
        "learn from."
    ),
    purpose_text=(
        "To define how «Hospital Name» identifies staff health problems "
        "and occupational hazards, conducts annual health checks, "
        "provides treatment for workplace injuries, and prevents and "
        "handles workplace violence."
    ),
    scope_why="so every staff member -- not just those in known high-exposure roles -- is covered by the same occupational health programme.",
    scope_text="Applies to the HR In-Charge, the Medical Superintendent, department heads and the Quality Coordinator, for every staff member.",
    responsibility_why="an injury or hazard nobody documents is one the hospital has no way of learning from or protecting staff against next time.",
    responsibilities=[
        ("Medical Superintendent", "Approves the occupational health policy and workplace violence measures, ensures treatment is provided for workplace injuries, and reviews violence incidents and prevention effectiveness."),
        ("HR In-Charge / Personnel Officer", "Maintains the occupational health hazard register and health-check schedule, coordinates annual health checks, and documents workplace injuries and violence incidents."),
        ("Department Heads", "Report occupational hazards in their areas, ensure staff attend annual health checks, and support the immediate response to a violence incident."),
        ("Quality Coordinator", "Audits this SOP quarterly."),
        ("All Staff", "Attend annual health checks, report workplace injuries and violence immediately, and follow the infection-control exposure procedure for infection-specific exposure."),
    ],
    items=[
        PlainItem(
            heading="Identify staff health problems and occupational hazards",
            why="A hazard that is never written down is a hazard the hospital has no way of proving it ever addressed, and a health problem that is never identified cannot be acted on before it becomes an injury.",
            body=[
                "The occupational health programme covers hazard "
                "identification in each department, health surveillance "
                "for roles with known exposure (radiology, laboratory, "
                "operating areas, for example), immunisation status "
                "tracking, and mental well-being awareness.",
                "The occupational health hazard register is updated "
                "annually or immediately when a new hazard is "
                "identified.",
                "Department heads report new hazards as they arise; "
                "infection-specific exposure is handled per the "
                "infection-control exposure procedure and is not "
                "duplicated in this register.",
            ],
            oe_code="HRM.5.a",
        ),
        PlainItem(
            heading="Conduct an annual health check for every active staff member",
            why="A health check that happens once at hiring and never again cannot catch a condition that develops on the job -- the annual cycle is what makes this a genuine ongoing safeguard rather than a one-time formality.",
            body=[
                "Every active staff member receives an annual health "
                "check: general physical examination, vision and "
                "hearing screening where the role requires it, chest "
                "X-ray or PPD for high-risk roles, vaccination status "
                "review, and any role-specific test defined in the "
                "hazard register.",
                "Results are recorded on a standard health-check form "
                "and filed in the personnel file.",
                "Abnormal findings are referred for follow-up treatment; "
                "a staff member who cannot perform patient-facing duties "
                "due to a health finding is reassigned per medical "
                "advice until cleared.",
            ],
            oe_code="HRM.5.b",
        ),
        PlainItem(
            heading="Provide treatment for workplace-related injuries",
            why="A staff member injured on the job who has to pay for their own treatment, or whose injury is never documented, has no legal protection and the hospital has no record to learn from.",
            body=[
                "Workplace injuries covered include slips and falls, "
                "manual handling injuries, chemical exposure "
                "(non-infection), and injuries from workplace violence.",
                "The procedure runs immediate first aid, medical "
                "assessment, treatment at the hospital's own emergency "
                "service or a designated panel doctor, documentation of "
                "the injury, and a return-to-work assessment.",
                "Injury records are filed in the personnel file and "
                "reported to the Medical Superintendent; a repeat injury "
                "in the same area triggers a review of the hazard "
                "register.",
            ],
            oe_code="HRM.5.c",
            technical_sources=[COMPENSATION_ACT_SRC],
        ),
        PlainItem(
            heading="Prevent and handle workplace violence",
            why="Waiting for a violent incident to happen before deciding how to respond to it means the response is improvised in the moment it matters most -- prevention and handling measures have to be decided and communicated in advance.",
            body=[
                "Prevention measures include staff training on "
                "de-escalation, visible security measures, restricted "
                "access to high-risk areas, and a zero-tolerance policy "
                "communicated to patients and visitors.",
                "Handling measures cover an immediate safety response, "
                "reporting to the Medical Superintendent and local "
                "police where applicable, medical treatment for the "
                "injured staff member, incident documentation, support "
                "and counselling for affected staff, and a review of "
                "prevention measures after every event.",
            ],
            oe_code="HRM.5.d",
            technical_sources=[WHO_VIOLENCE_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the HRM.5 Records folder).",
    related_documents=[
        "Policy on Staff Well-Being and Occupational Health (HRM.5)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the HR In-Charge, and sooner if the quarterly audit "
        "finds a health check overdue by more than three months, a "
        "workplace injury not treated promptly, or the infection-control "
        "exposure procedures change."
    ),
    full_reference_list=[
        NABH_HRM_CITE.format(code="HRM.5"),
        COMPENSATION_ACT_SRC,
        WHO_VIOLENCE_SRC,
    ],
)

# --------------------------------------------------------------- HRM.6 ---
HRM6 = SOPSpecV2(
    sop_no="SOP-HRM.6.a",
    title="Documented Personal Information for Each Staff Member",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» maintains a confidential "
        "personal file for every staff member, what each file must "
        "contain, how in-service training records are filed, and how "
        "evaluation results and remarks are filed -- so every staff "
        "member's complete employment record exists in one place, is kept "
        "confidential, and can be produced on demand for an audit or a "
        "credentialing decision."
    ),
    purpose_trigger=(
        "A credentialing decision needs to confirm a doctor's "
        "qualifications were actually verified, not just claimed. This SOP "
        "is what makes sure the personal file holds the certified copies "
        "and the verification record, ready to produce -- not scattered "
        "across whichever department happened to collect them."
    ),
    purpose_why=(
        "We do this because a staff member with no personal file is a "
        "staff member whose qualifications, credentials and health status "
        "cannot be proven to have ever been checked -- and a file anyone "
        "can open without a reason logged is not actually confidential, "
        "whatever the policy on paper says."
    ),
    purpose_text=(
        "To define how «Hospital Name» maintains a confidential personal "
        "file for every staff member, its mandatory contents, in-service "
        "training records, and evaluation results."
    ),
    scope_why="so every staff member -- clinical, nursing, para-clinical, administrative and support -- has the same complete, confidential record.",
    scope_text="Applies to the HR Manager, department heads, the Medical Superintendent and the Quality Coordinator, for every staff member.",
    responsibility_why="a file that's incomplete, or that anyone can open without a reason logged, defeats the purpose of keeping one at all.",
    responsibilities=[
        ("Medical Superintendent", "Is accountable that every staff member has a complete personal file, and may access files for governance and credentialing decisions."),
        ("HR Manager", "Creates and maintains personal files, ensures confidentiality and access control, conducts quarterly file-completeness audits and annual evaluation-record reviews, and maintains the central training register."),
        ("Department Heads", "Submit signed evaluation records and training attendance to HR within ten working days, and notify HR when a staff member's role, qualification or registration changes."),
        ("Quality Coordinator", "Audits this SOP quarterly and tracks corrective action when file gaps recur."),
    ],
    items=[
        PlainItem(
            heading="Maintain a confidential personal file for every staff member",
            why="A staff member with no personal file is a staff member whose qualifications, credentials and health status cannot be proven to have ever been checked -- and a file anyone can open without a reason logged is not actually confidential, whatever the policy on paper says.",
            body=[
                "A personal file is maintained for every staff member -- "
                "permanent, contract, locum and part-time -- with a "
                "unique personnel file number assigned at joining.",
                "Files are stored in a locked cabinet or a secured HR "
                "module, with access limited to authorised HR staff and "
                "the Medical Superintendent for governance purposes; an "
                "access log records who opened each file, when and why.",
                "Every person who handles personal files signs a "
                "confidentiality undertaking, and personal information "
                "is never disclosed except as required by law, for "
                "credentialing, or with the staff member's written "
                "consent.",
                "The HR Manager verifies quarterly that every person on "
                "the payroll has a corresponding file in the master "
                "register.",
            ],
            oe_code="HRM.6.a",
            technical_sources=[DPDP_ACT_SRC],
        ),
        PlainItem(
            heading="File the mandatory contents in every personal file",
            why="An appointment letter alone is not a personal file -- without qualification proof, a signed job description, credential verification and a health status record, the file cannot actually answer the question of whether this person is who, and what, the hospital believes them to be.",
            body=[
                "Each personal file contains certified copies of "
                "qualification, degree, diploma, registration and "
                "licence documents; the signed job description for the "
                "current role; proof of formal engagement (appointment "
                "letter or contract, joining date, renewals); evidence "
                "that credentials were verified with the issuing body or "
                "council; and pre-employment and periodic health check "
                "reports.",
                "A personnel file index at the front of each file lists "
                "every mandatory document and its date of filing, used "
                "by the HR Manager during file audits.",
            ],
            oe_code="HRM.6.b",
        ),
        PlainItem(
            heading="File in-service training and education records",
            why="A training certificate kept in a department drawer instead of the personal file is, from the file's point of view, the same as training that never happened -- the record has to actually live where it can be found.",
            body=[
                "For every training event -- induction, mandatory "
                "refresher, skill update, external course -- the "
                "personal file holds the topic, date, duration, trainer "
                "or institution, the attendance register entry or "
                "completion certificate, and any competency assessment "
                "result.",
                "A dedicated training section within each file holds "
                "these records in chronological order, mirrored in the "
                "HR Manager's central training register, which can "
                "produce any staff member's training history within one "
                "working day.",
                "A mandatory training gap found during register review "
                "is closed within thirty days and recorded in the file.",
            ],
            oe_code="HRM.6.c",
        ),
        PlainItem(
            heading="File evaluation results and remarks",
            why="An appraisal result that is completed but never filed cannot later be used to show the hospital actually evaluated this person, or to support any decision -- positive or negative -- that depends on that history.",
            body=[
                "Every completed performance appraisal, probation "
                "review, commendation, disciplinary action, counselling "
                "note and improvement plan is filed in a chronological "
                "evaluation section, signed by the appraiser and "
                "countersigned by the department head where applicable, "
                "dated before filing.",
                "The HR Manager verifies annually that evaluation "
                "records are complete and that appraisals have been "
                "conducted at the stated frequency.",
                "A summary sheet at the front of the evaluation section "
                "lists the date and outcome of every appraisal to date.",
            ],
            oe_code="HRM.6.d",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the HRM.6 Records folder).",
    related_documents=[
        "Policy on Documented Personal Information for Each Staff Member (HRM.6)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the HR Manager, and sooner if a staff member's "
        "file is found incomplete at credentialing, more than ten percent "
        "of a sampled audit batch lacks a mandatory document, or "
        "evaluation records are overdue for two consecutive quarters."
    ),
    full_reference_list=[NABH_HRM_CITE.format(code="HRM.6"), DPDP_ACT_SRC],
)

# --------------------------------------------------------------- HRM.7 ---
HRM7 = SOPSpecV2(
    sop_no="SOP-HRM.7.a",
    title="Credentialing and Privileging of Medical Professionals Permitted to Provide Patient Care Without Supervision",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» identifies which medical "
        "professionals are permitted to provide patient care without "
        "supervision, verifies and documents their education, "
        "registration, training and experience, grants privileges matched "
        "to those credentials, and makes sure both the professional and "
        "the department know what services they are actually authorised "
        "to provide -- so unsupervised care is given only by a doctor "
        "whose registration is current and verified, not assumed."
    ),
    purpose_trigger=(
        "A doctor's registration lapses without anyone noticing. This SOP "
        "is what any staff member -- not just HR -- can act on directly: "
        "stop that doctor from providing unsupervised care, make sure "
        "care continues under someone credentialed, and notify the "
        "Medical Superintendent the same shift. No approval is needed to "
        "do this."
    ),
    purpose_why=(
        "We do this because a doctor providing unsupervised care who is "
        "not actually listed anywhere as authorised to do so is "
        "practising on an assumption, not a verified fact -- and the law "
        "does not accept a claim the hospital took on faith as a "
        "substitute for a current, confirmed registration."
    ),
    purpose_text=(
        "To define how «Hospital Name» identifies medical professionals "
        "permitted for unsupervised care, verifies and documents their "
        "credentials, grants matched privileges, and makes services known "
        "to the professional and the department."
    ),
    scope_why="so every medical professional providing unsupervised care -- not just new hires -- is covered by the same verified register.",
    scope_text=(
        "Applies to every medical professional who provides patient care "
        "without supervision: treating doctors, consultants, resident "
        "medical officers, and any doctor whose orders or procedures do "
        "not require a supervising physician."
    ),
    responsibility_why="a privilege granted without verified credentials, or a lapsed registration nobody catches, is a legal and patient-safety failure, not a paperwork gap.",
    responsibilities=[
        ("Medical Superintendent", "Chairs the Credentialing Committee, is accountable for the privileging register, and suspends or restores privileges based on the Committee's recommendation."),
        ("HR Manager", "Collects and verifies credentials, maintains credentialing files and the privileging register, and tracks registration renewal dates to initiate re-credentialing."),
        ("Credentialing Committee", "Reviews every credentialing application and grants, restricts or denies privileges by written decision."),
        ("Department Heads", "Confirm privileges match department scope, brief new doctors on services the department provides, and maintain unit doctor lists."),
        ("Quality Coordinator", "Audits this SOP quarterly and tracks corrective action when credentialing gaps or lapsed registrations recur."),
    ],
    items=[
        PlainItem(
            heading="Identify medical professionals permitted for unsupervised care",
            why="A doctor providing unsupervised care who is not actually listed anywhere as authorised to do so is practising on an assumption, not on a verified fact -- the register is what turns that assumption into something checkable.",
            body=[
                "The HR Manager, in consultation with the Medical "
                "Superintendent, maintains the medical privileging "
                "register listing every independently practising medical "
                "professional, with name and employee/consultant ID, "
                "National Medical Commission and State Medical Council "
                "registration numbers, qualification, dates of initial "
                "and last re-credentialing, and privileges granted.",
                "The register is available to department heads and "
                "nursing supervisors, with a current extract displayed "
                "in each clinical department and at the nursing station "
                "so staff know who is authorised to provide unsupervised "
                "care.",
            ],
            oe_code="HRM.7.a",
            technical_sources=[NMC_ACT_SRC],
        ),
        PlainItem(
            heading="Verify, document and periodically update credentials",
            why="A registration number copied from a candidate's CV, never actually checked against the issuing council, is not verification -- it is a claim the hospital took on faith, and the law does not accept faith as a substitute for a current, confirmed registration.",
            body=[
                "At credentialing or privilege renewal, the HR Manager "
                "collects and verifies medical degree and speciality "
                "qualification certificates, National Medical Commission "
                "and State Medical Council registration, post-graduate "
                "and continuing medical education records, experience "
                "letters, and any disclosed malpractice or disciplinary "
                "history.",
                "Verification is documented with the date, the source "
                "contacted, and the verifying officer. Registration "
                "renewal dates are tracked, and re-verification begins "
                "sixty days before expiry.",
                "Re-credentialing is conducted every two years or sooner "
                "when scope of practice changes, registration is "
                "renewed, or a significant clinical event requires "
                "review.",
            ],
            oe_code="HRM.7.b",
        ),
        PlainItem(
            heading="Grant privileges matched to verified credentials",
            why="Granting a doctor privileges beyond what their actual qualification and registration support is not a convenience exception -- it is the exact failure this entire standard exists to prevent.",
            body=[
                "The Credentialing Committee -- chaired by the Medical "
                "Superintendent with the HR Manager and the relevant "
                "department head -- reviews each application and grants "
                "privileges by written privilege letter stating "
                "procedures and services the doctor may perform "
                "independently, patient categories where applicable, "
                "admission authority if granted, any restrictions, and a "
                "validity period of maximum two years.",
                "Privileges not supported by verified credentials are "
                "not granted; a doctor whose registration lapses is "
                "suspended from the register pending renewal "
                "verification.",
                "Privilege letters are filed in the credentialing file, "
                "with a copy held by the doctor and the department head.",
            ],
            oe_code="HRM.7.c",
        ),
        PlainItem(
            heading="Make requisite services known to the professional and the department",
            why="A doctor who holds a valid privilege but was never told, and whose department never confirmed, exactly which services that privilege covers can end up practising outside what the department actually claims to provide -- the privilege letter has to connect to the real service list, not sit on file disconnected from it.",
            body=[
                "Each privilege letter is cross-referenced to the "
                "service directory and the department scope statement; "
                "the department head confirms the doctor's privileges "
                "match the services the department claims to provide.",
                "At department induction or when a new doctor joins a "
                "unit, the department head briefs the doctor on the "
                "department's services and procedures, referral "
                "pathways, on-call and emergency cover expectations, and "
                "documentation requirements.",
                "The briefing is recorded and filed in the credentialing "
                "file; department heads match their unit doctor list to "
                "the central privileging register quarterly.",
            ],
            oe_code="HRM.7.d",
        ),
        PlainItem(
            heading="Know when to stop — and who is responsible for acting",
            why="A doctor whose registration has lapsed and who keeps providing unsupervised care anyway is a real, immediate patient-safety risk, not a paperwork backlog -- this step is deliberately written so any staff member can act on it, not just the department head.",
            body=[
                "Any staff member who cannot confirm that a medical "
                "professional has completed credentialing and "
                "privileging does not allow that professional to provide "
                "unsupervised patient care -- including writing "
                "independent orders, performing procedures or admitting "
                "patients.",
                "They make sure patient care continues under another "
                "credentialed professional or under supervised care as "
                "clinically appropriate, and report to the Medical "
                "Superintendent or HR Manager immediately, the same "
                "shift.",
                "For a doctor whose State Medical Council or National "
                "Medical Commission registration has lapsed: the doctor "
                "is suspended from the privileging register pending "
                "verification, is not assigned unsupervised clinical "
                "duties until registration is confirmed current, and the "
                "Medical Superintendent is notified the same working "
                "day.",
                "No approval is needed to take this step. Patient safety "
                "and statutory registration requirements override "
                "convenience.",
            ],
            oe_code="HRM.7.a",
            technical_sources=[NMC_ACT_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the HRM.7 Records folder).",
    related_documents=[
        "Policy on Credentialing and Privileging of Medical Professionals (HRM.7)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the HR Manager, and sooner when the National "
        "Medical Commission or a State Medical Council changes its "
        "registration requirements, or an uncredentialed or unprivileged "
        "doctor is found providing unsupervised care."
    ),
    full_reference_list=[NABH_HRM_CITE.format(code="HRM.7"), NMC_ACT_SRC],
)

# --------------------------------------------------------------- HRM.8 ---
HRM8 = SOPSpecV2(
    sop_no="SOP-HRM.8.a",
    title="Credentialing and Privileging of Nursing Professionals Permitted to Provide Patient Care Without Supervision",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» identifies which nursing "
        "professionals are permitted to provide patient care without "
        "supervision, verifies and documents their education, "
        "registration, training and experience, grants privileges matched "
        "to those credentials, and makes sure both the nurse and the unit "
        "know what services they are actually authorised to provide -- so "
        "unsupervised nursing care is given only by someone whose "
        "registration is current and verified, not assumed."
    ),
    purpose_trigger=(
        "A nurse's State Nursing Council registration lapses without "
        "anyone noticing. This SOP is what any staff member can act on "
        "immediately: that nurse does not continue unsupervised duties, "
        "care continues under another credentialed nurse, and the Nursing "
        "Superintendent is notified the same working day -- no approval "
        "needed."
    ),
    purpose_why=(
        "We do this because a nurse providing unsupervised care who is "
        "not actually listed anywhere as authorised to do so is "
        "practising on an assumption, not a verified fact -- a "
        "registration number copied from a file and never actually "
        "checked against the issuing council is a claim the hospital took "
        "on faith."
    ),
    purpose_text=(
        "To define how «Hospital Name» identifies nursing professionals "
        "permitted for unsupervised care, verifies and documents their "
        "credentials, grants matched privileges, and makes services known "
        "to the nurse and the unit."
    ),
    scope_why="so every nursing professional providing unsupervised care -- staff nurses, supervisors, ward in-charges -- is covered by the same verified register.",
    scope_text=(
        "Applies to every nursing professional who provides patient care "
        "without supervision: staff nurses, nursing supervisors, ward "
        "in-charges, and any nurse whose clinical actions do not require "
        "direct physician supervision for the privilege granted."
    ),
    responsibility_why="a nursing privilege granted without verified credentials, or a lapsed registration nobody catches, is a legal and patient-safety failure, not a paperwork gap.",
    responsibilities=[
        ("Nursing Superintendent", "Chairs the Credentialing Committee for nursing, is accountable for the nursing privileging register, and suspends or restores privileges based on the Committee's recommendation."),
        ("HR Manager", "Collects and verifies nursing credentials, maintains credentialing files and the privileging register, and tracks registration renewal dates to initiate re-credentialing."),
        ("Credentialing Committee", "Reviews every credentialing application and grants, restricts or denies nursing privileges by written decision."),
        ("Ward In-Charges / Unit Nursing Leads", "Confirm privileges match unit scope, brief new nurses, and maintain unit nurse lists."),
        ("Medical Superintendent", "Participates in the Credentialing Committee for governance oversight."),
        ("Quality Coordinator", "Audits this SOP quarterly and tracks corrective action when credentialing gaps or lapsed registrations recur."),
    ],
    items=[
        PlainItem(
            heading="Identify nursing staff permitted for unsupervised care",
            why="A nurse providing unsupervised care who is not actually listed anywhere as authorised to do so is practising on an assumption, not a verified fact -- the register is what turns that assumption into something checkable.",
            body=[
                "The HR Manager, in consultation with the Nursing "
                "Superintendent, maintains the nursing privileging "
                "register listing every independently practising nurse, "
                "with name and employee ID, Indian Nursing Council and "
                "State Nursing Council registration numbers, "
                "qualification (GNM, B.Sc. Nursing, Post Basic B.Sc. "
                "Nursing or equivalent), dates of initial and last "
                "re-credentialing, and privileges granted.",
                "The register is available to ward in-charges and "
                "department heads, with a current extract displayed at "
                "each nursing station so staff know who is authorised "
                "for unsupervised nursing care.",
            ],
            oe_code="HRM.8.a",
            technical_sources=[INC_ACT_SRC],
        ),
        PlainItem(
            heading="Verify, document and periodically update credentials",
            why="A registration number copied from a candidate's file, never actually checked against the issuing council, is not verification -- it is a claim the hospital took on faith.",
            body=[
                "At credentialing or privilege renewal, the HR Manager "
                "collects and verifies nursing diploma or degree "
                "certificates, Indian Nursing Council and State Nursing "
                "Council registration, post-basic speciality training "
                "certificates where applicable, experience letters, and "
                "continuing nursing education records.",
                "Verification is documented with the date, the source "
                "contacted, and the verifying officer. Registration "
                "renewal dates are tracked, and re-verification begins "
                "sixty days before expiry.",
                "Re-credentialing is conducted every two years or sooner "
                "when scope of practice changes, registration is "
                "renewed, or a significant clinical event requires "
                "review.",
            ],
            oe_code="HRM.8.b",
        ),
        PlainItem(
            heading="Grant privileges matched to verified credentials",
            why="Allowing a nurse to perform a procedure -- IV cannulation, medication administration, advanced wound care -- that is not actually listed in their privilege letter is the exact failure this standard exists to prevent, whatever the time pressure on the ward.",
            body=[
                "The Credentialing Committee -- chaired by the Nursing "
                "Superintendent with the HR Manager and Medical "
                "Superintendent -- reviews each application and grants "
                "privileges by written privilege letter stating nursing "
                "procedures and care activities the nurse may perform "
                "independently, patient categories where applicable, "
                "ward or unit assignment authority if granted, any "
                "restrictions, and a validity period of maximum two "
                "years.",
                "Privileges not supported by verified credentials are "
                "not granted; a nurse whose registration lapses is "
                "suspended from the register pending renewal "
                "verification.",
                "Privilege letters are filed in the credentialing file, "
                "with a copy held by the nurse and the ward in-charge.",
            ],
            oe_code="HRM.8.c",
        ),
        PlainItem(
            heading="Make requisite services known to the nurse and the unit",
            why="A nurse who holds a valid privilege but was never actually briefed on the unit's own care standards, medication documentation requirements or escalation pathway can end up practising outside what the ward really expects, even while holding a technically valid privilege letter.",
            body=[
                "Each privilege letter is cross-referenced to the "
                "service directory and the ward or unit scope; the ward "
                "in-charge confirms the nurse's privileges match the "
                "services the unit provides.",
                "At unit induction or when a new nurse joins a ward, the "
                "ward in-charge briefs the nurse on nursing care "
                "standards and procedures, medication administration and "
                "documentation requirements, escalation pathways to the "
                "treating doctor, handover and shift-reporting "
                "requirements, and infection-control and safety "
                "practices for the unit.",
                "The briefing is recorded and filed in the credentialing "
                "file; ward in-charges match their unit nurse list to "
                "the central privileging register quarterly.",
            ],
            oe_code="HRM.8.d",
        ),
        PlainItem(
            heading="Know when to stop — and who is responsible for acting",
            why="A nurse whose registration has lapsed and who keeps providing unsupervised care anyway is a real, immediate patient-safety risk, not a paperwork backlog -- this step is deliberately written so any staff member can act on it, not just the ward in-charge.",
            body=[
                "Any staff member who cannot confirm that a nursing "
                "professional has completed credentialing and "
                "privileging does not allow that nurse to provide "
                "unsupervised patient care -- including independent "
                "medication administration, procedures or ward "
                "supervision beyond their verified privileges.",
                "They make sure patient care continues under another "
                "credentialed nurse or under supervised care as "
                "clinically appropriate, and report to the Nursing "
                "Superintendent or HR Manager immediately, the same "
                "shift.",
                "For a nurse whose State Nursing Council or Indian "
                "Nursing Council registration has lapsed: the nurse is "
                "suspended from the privileging register pending "
                "verification, is not assigned unsupervised nursing "
                "duties until registration is confirmed current, and the "
                "Nursing Superintendent is notified the same working "
                "day.",
                "No approval is needed to take this step. Patient safety "
                "and statutory registration requirements override "
                "convenience.",
            ],
            oe_code="HRM.8.a",
            technical_sources=[INC_ACT_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the HRM.8 Records folder).",
    related_documents=[
        "Policy on Credentialing and Privileging of Nursing Professionals (HRM.8)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the HR Manager, and sooner when the Indian Nursing "
        "Council or a State Nursing Council changes its registration "
        "requirements, or an uncredentialed or unprivileged nurse is "
        "found providing unsupervised care."
    ),
    full_reference_list=[NABH_HRM_CITE.format(code="HRM.8"), INC_ACT_SRC],
)

# --------------------------------------------------------------- HRM.9 ---
HRM9 = SOPSpecV2(
    sop_no="SOP-HRM.9.a",
    title="Credentialing and Privileging of Para-Clinical Professionals Permitted to Provide Patient Care Without Supervision",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» identifies which "
        "para-clinical professionals -- pharmacists, laboratory "
        "technicians, radiographers, physiotherapists and other allied "
        "health staff -- are permitted to provide patient care or "
        "patient-facing services without supervision, verifies and "
        "documents their education, registration, training and "
        "experience, grants privileges matched to those credentials, and "
        "makes sure both the professional and the department know what "
        "services they are actually authorised to provide."
    ),
    purpose_trigger=(
        "A radiographer's AERB authorisation is never actually confirmed "
        "before they start operating radiation equipment. This SOP is "
        "what any staff member can act on directly: that person does not "
        "operate the equipment unsupervised until the authorisation is "
        "verified -- no approval needed to stop and check."
    ),
    purpose_why=(
        "We do this because a pharmacist's registration number that was "
        "never checked with the State Pharmacy Council, or a "
        "radiographer's AERB authorisation that was never confirmed, are "
        "both claims the hospital took on faith -- and for dispensing "
        "medicine or operating radiation equipment, faith is not a "
        "substitute for a verified, current authorisation."
    ),
    purpose_text=(
        "To define how «Hospital Name» identifies para-clinical "
        "professionals permitted for unsupervised care, verifies and "
        "documents profession-specific credentials, grants matched "
        "privileges, and makes services known to the professional and the "
        "department."
    ),
    scope_why="so every para-clinical professional providing unsupervised, patient-facing services -- not just doctors and nurses -- is covered by the same verified register.",
    scope_text=(
        "Applies to every para-clinical professional who provides patient "
        "care or patient-facing services without supervision: "
        "pharmacists, laboratory technicians, radiographers, "
        "physiotherapists, dieticians, respiratory therapists and other "
        "allied health staff whose role requires independent practice "
        "authority."
    ),
    responsibility_why="a privilege granted without verified credentials, or a lapsed statutory authorisation nobody catches, is a legal and patient-safety failure, not a paperwork gap.",
    responsibilities=[
        ("Medical Superintendent", "Chairs the Credentialing Committee and is accountable for the para-clinical privileging register."),
        ("HR Manager", "Collects and verifies credentials by profession, maintains credentialing files and the privileging register, and tracks registration renewal dates to initiate re-credentialing."),
        ("Credentialing Committee", "Reviews every application and grants, restricts or denies para-clinical privileges by written decision."),
        ("Department Heads (Laboratory, Radiology, Pharmacy, Physiotherapy and others)", "Confirm privileges match department scope, brief new staff, and maintain unit staff lists."),
        ("Quality Coordinator", "Audits this SOP quarterly and tracks corrective action when credentialing gaps or lapsed registrations recur."),
    ],
    items=[
        PlainItem(
            heading="Identify para-clinical professionals permitted for unsupervised care",
            why="A pharmacist, lab technician, radiographer or physiotherapist providing unsupervised, patient-facing care with no entry in any register is practising on assumption, and for a radiographer operating radiation equipment that assumption carries a real licensing risk, not just a documentation gap.",
            body=[
                "The HR Manager, in consultation with relevant "
                "department heads, maintains the para-clinical "
                "privileging register listing every independently "
                "practising professional, with name and employee ID, "
                "profession category, statutory registration number and "
                "issuing body, qualification, dates of initial and last "
                "re-credentialing, and privileges granted.",
                "The register is available to department heads, with a "
                "current extract displayed in each para-clinical "
                "department (laboratory, radiology, pharmacy, "
                "physiotherapy).",
            ],
            oe_code="HRM.9.a",
        ),
        PlainItem(
            heading="Verify, document and periodically update credentials by profession",
            why="A pharmacist's registration number that was never checked with the State Pharmacy Council, or a radiographer's AERB authorisation that was never confirmed, are both claims the hospital took on faith -- and for dispensing medicine or operating radiation equipment, faith is not a substitute for a verified, current authorisation.",
            body=[
                "At credentialing or privilege renewal, the HR Manager "
                "collects and verifies credentials specific to each "
                "profession: pharmacy degree/diploma and State Pharmacy "
                "Council registration for pharmacists; DMLT/B.Sc. MLT or "
                "equivalent and State Medical Faculty or board "
                "registration for laboratory technicians; radiography "
                "qualification and AERB authorisation for radiographers "
                "operating radiation-generating equipment; and BPT/MPT "
                "and State Council of Physiotherapy registration for "
                "physiotherapists.",
                "Verification is documented with the date, the source "
                "contacted, and the verifying officer. Registration "
                "renewal dates are tracked, and re-verification begins "
                "sixty days before expiry.",
                "Re-credentialing is conducted every two years or sooner "
                "when scope of practice changes, registration is "
                "renewed, or a significant event requires review.",
            ],
            oe_code="HRM.9.b",
            technical_sources=[PHARMACY_ACT_SRC, AERB_RULES_SRC],
        ),
        PlainItem(
            heading="Grant privileges matched to verified credentials",
            why="Allowing a lab technician to run a test panel they were never privileged for, or a radiographer to operate a modality outside their AERB authorisation, is the exact failure this standard exists to prevent -- the privilege letter has to say exactly what each professional may do, not leave it to be inferred from their job title.",
            body=[
                "The Credentialing Committee -- chaired by the Medical "
                "Superintendent with the HR Manager and the relevant "
                "department head -- reviews each application and grants "
                "privileges by written privilege letter stating the "
                "tests, procedures, equipment or services the "
                "professional may perform independently, patient "
                "categories where applicable, any restrictions, and a "
                "validity period of maximum two years.",
                "Profession-specific privileges are named explicitly: "
                "dispensing categories for a pharmacist; test panels and "
                "analyser categories for a laboratory technician; "
                "AERB-authorised modalities and equipment for a "
                "radiographer; treatment modalities and patient "
                "categories for a physiotherapist.",
                "Privileges not supported by verified credentials are "
                "not granted; a professional whose registration lapses "
                "is suspended from the register pending renewal "
                "verification.",
            ],
            oe_code="HRM.9.c",
        ),
        PlainItem(
            heading="Make requisite services known to the professional and the department",
            why="A professional who holds a valid privilege letter but was never actually briefed on the department's own quality standards, turnaround times or safety requirements can end up working outside what the department really expects, even while technically privileged.",
            body=[
                "Each privilege letter is cross-referenced to the "
                "service directory and the department scope statement; "
                "the department head confirms the professional's "
                "privileges match the services the department claims to "
                "provide.",
                "At department induction or when a new professional "
                "joins, the department head briefs the person on "
                "services, tests, procedures or treatments the "
                "department provides and those referred elsewhere, "
                "quality standards and turnaround times, safety "
                "requirements (radiation safety, biosafety, cytotoxic "
                "handling as applicable), and escalation pathways to the "
                "treating doctor.",
                "The briefing is recorded and filed in the credentialing "
                "file; department heads match their unit staff list to "
                "the central privileging register quarterly.",
            ],
            oe_code="HRM.9.d",
        ),
        PlainItem(
            heading="Know when to stop — and who is responsible for acting",
            why="A professional whose statutory registration has lapsed and who keeps providing unsupervised, patient-facing services anyway is a real, immediate risk -- not a paperwork backlog -- and this step is deliberately written so any staff member can act on it.",
            body=[
                "Any staff member who cannot confirm that a "
                "para-clinical professional has completed credentialing "
                "and privileging does not allow that professional to "
                "provide unsupervised patient care or patient-facing "
                "services -- including independent test reporting, "
                "radiation exposure, physiotherapy treatment or "
                "medication dispensing beyond verified privileges.",
                "They make sure the service continues under another "
                "credentialed professional or under supervised care as "
                "clinically appropriate, and report to the department "
                "head or HR Manager immediately, the same shift.",
                "For a professional whose statutory registration or "
                "council enrolment has lapsed: the professional is "
                "suspended from the privileging register pending "
                "verification, is not assigned unsupervised duties until "
                "registration is confirmed current, and the Medical "
                "Superintendent and the relevant department head are "
                "notified the same working day.",
                "No approval is needed to take this step. Patient safety "
                "and statutory registration requirements override "
                "convenience.",
            ],
            oe_code="HRM.9.a",
            technical_sources=[AERB_RULES_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the HRM.9 Records folder).",
    related_documents=[
        "Policy on Credentialing and Privileging of Para-Clinical Professionals (HRM.9)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the HR Manager, and sooner when statutory "
        "registration requirements for any para-clinical profession "
        "change, or an uncredentialed or unprivileged professional is "
        "found providing unsupervised services."
    ),
    full_reference_list=[
        NABH_HRM_CITE.format(code="HRM.9"),
        PHARMACY_ACT_SRC,
        AERB_RULES_SRC,
    ],
)

SOPS = [
    ("SOP_HRM.1.b_recruitment.docx", HRM1B),
    ("SOP_HRM.1.e_job_description.docx", HRM1E),
    ("SOP_HRM.1.i_disciplinary_grievance.docx", HRM1I),
    ("SOP_HRM.2.a_to_e_induction_training_development.docx", HRM2),
    ("SOP_HRM.3.a_to_g_safety_disaster_fire_qi_training.docx", HRM3),
    ("SOP_HRM.4.a_performance_appraisal.docx", HRM4A),
    ("SOP_HRM.5.a_to_d_staff_wellbeing_occupational_health.docx", HRM5),
    ("SOP_HRM.6.a_to_d_personal_files.docx", HRM6),
    ("SOP_HRM.7.a_to_d_medical_credentialing_privileging.docx", HRM7),
    ("SOP_HRM.8.a_to_d_nursing_credentialing_privileging.docx", HRM8),
    ("SOP_HRM.9.a_to_d_paraclinical_credentialing_privileging.docx", HRM9),
]


def main() -> None:
    for fname, spec in SOPS:
        out_path = OUT_ROOT / fname
        build_sop_v2(spec, out_path)
        print(f"built {out_path} (v2: plain body + audit appendix)")


if __name__ == "__main__":
    main()
