# -*- coding: utf-8 -*-
"""Hospital-facing What-we-do methods for HCO HRM.1–HRM.13.

HCO 6th Edition chapter name is Human Resource Management (HRM). Method
notes from the Guidebook are attached separately by the generator.
"""
from __future__ import annotations


def method_bodies(*, D, HOSPITAL, BLANK) -> dict[str, str]:
    """Return method body text keyed by oe_code (without the 5.N title)."""
    hr = D("HR In-Charge / Personnel Officer")
    ms = D("Medical Superintendent")
    qc = D("Quality Coordinator")
    ns = D("Nursing Superintendent")
    gb = D("governing body")
    annually = D("annually")
    monthly = D("monthly")
    yearly_check = D("once a year")

    return {
        # ---------------- HRM.1 — Human resource planning ----------------
        "HRM.1.a": f"""Human resource planning at {HOSPITAL} supports the organisation's current and future ability to meet the care, treatment and service needs of the patient. The {hr} prepares a workforce plan {annually} that compares current staff numbers and skill mix against the hospital's mission, patient volume and mix, services offered and medical technology in use, with input from department heads and other stakeholders.

Recognised methods are used to set staffing levels against the strategic and operational plan. Where the year's actuals vary from plan, the {hr} records the corrective action taken and carries it into the next plan.""",

        "HRM.1.b": f"""{HOSPITAL} maintains an adequate number and mix of staff to meet the care, treatment and service needs of the patient, commensurate with workload and clinical requirement. Nursing staffing follows published guidelines (the WHO Workload Indicators of Staffing Need — WISN — method is a recognised reference).

Where a shortfall exists, the contingency plan at HRM.1.c is triggered, covering support staff as well as clinical staff. The {hr} compares sanctioned versus actual strength {monthly} and escalates unresolved shortfalls to the {ms}.""",

        "HRM.1.c": f"""{HOSPITAL} has contingency plans to manage long- and short-term workforce shortages, including unplanned shortages (a shift-by-shift gap, a short-term crisis or a sustained long-term shortfall). The plan may include reprioritising tasks, reallocating tasks across available staff, and drawing on a pool of filler staff — previous employees and agency-sourced casual staff are named by the Guidebook as a typical source.

Each shortage event is logged with cause, measure used and outcome. The plan is tested at a defined interval (default {D('twice a year')}).""",

        "HRM.1.d": f"""The job specification and job description are defined for each category of staff at {HOSPITAL}, including full-time, part-time, employed, honorary, voluntary and temporary staff. Each job description lays down the content of the job and the qualifications, skills and experience required, commensurate with the qualification set for that role.

For a role requiring the skills of a doctor or a nurse, the minimum qualification is an MBBS or GNM degree respectively, unless government or statutory exemption has been granted. The {hr} holds the current job-description set; new hires sign that they have received and understood theirs.""",

        "HRM.1.e": f"""{HOSPITAL} performs a background check of new staff, using a defined methodology, either before the person joins or within one month of joining. The {hr} maintains a background-check register recording the method used, date completed and outcome for each new hire.

A staff member with no background check on file is escalated to the {ms}; this is not a box left for later.""",

        "HRM.1.f": f"""Reporting relationships are defined for each category of staff at {HOSPITAL}, documented as an organisation structure or chart showing hierarchy, line of control and functions at each level. The chart is transparent and disseminated to all stakeholders, and the reporting relationship is also defined at department or service level.

The {hr} holds the current chart; a role with no defined reporting line is incomplete under this element.""",

        "HRM.1.g": f"""{HOSPITAL} conducts exit interviews and uses them as a tool to improve human resource practices. A personal interview is the default method; the exercise is voluntary for the departing staff member.

The {hr} compiles findings at a defined interval (default {D('quarterly')}) into a trend report for the {ms} and, where the hospital has one, the {gb}, with proposed HR improvements tracked to closure.""",

        # ---------------- HRM.2 — Staff recruitment ----------------
        "HRM.2.a": f"""Written guidance governs the process of recruitment at {HOSPITAL}, based on defined criteria for each staff category, ensuring an adequate number and skill mix to provide the organisation's services. The procedure confirms that a candidate has the necessary registration, qualifications, skills and experience before appointment, and follows statutory requirements where they apply.

The process is documented and carried out transparently; the {hr} maintains a recruitment register logging vacancy, candidates considered, selection rationale and fill date. This is a CORE, asterisked element.""",

        "HRM.2.b": f"""A pre-employment medical examination is conducted on staff at {HOSPITAL} to confirm fitness to provide safe care. The scope of diagnostic testing is guided by the nature of the role, but any test performed follows the law of the land — for example, pre-employment HIV testing without the candidate's consent is illegal and is not this hospital's practice.

The {hr} holds the examination record with the personnel file.""",

        "HRM.2.c": f"""{HOSPITAL} defines and implements a code of conduct for its staff, outlining the do's and don'ts of workplace behaviour, aligned with the organisation's values and ethics framework and including protection of patient confidentiality. Staff sign the code at the time of joining; it may form part of the hospital's service rules.

This is a CORE element. The {hr} holds signed acknowledgements with the personnel file.""",

        "HRM.2.d": f"""Administrative procedures for human resource management are documented at {HOSPITAL} — at minimum attendance, leave, conduct and replacement. The {hr} maintains the current procedure set and covers it during induction (HRM.3.h). This is an asterisked element.""",

        # ---------------- HRM.3 — Induction training ----------------
        "HRM.3.a": f"""{HOSPITAL} provides induction training to its staff, including doctors, consultants (including visiting), outsourced staff, volunteers, students and trainees, oriented to the hospital and to their specific assignment or responsibilities. Induction is completed within one month of joining and covers objective elements HRM.3.b–h, along with any other requirement this hospital defines.

The contents may be issued as a booklet; separate induction may run at organisational and departmental level. The {hr} keeps the training record. This is a CORE element.""",

        "HRM.3.b": f"""Induction training at {HOSPITAL} includes orientation to the organisation's vision, mission and values, so that staff (including outsourced staff) are aware of and can correctly interpret them.""",

        "HRM.3.c": f"""Induction training at {HOSPITAL} includes awareness of staff rights and responsibilities and of patient rights and responsibilities, so that staff can comprehend the implications of both and can identify and report a violation of patient rights when it occurs.""",

        "HRM.3.d": f"""Induction training at {HOSPITAL} includes training on safety — patient, visitor and staff safety, including the hospital's emergency 'codes'.""",

        "HRM.3.e": f"""Induction training at {HOSPITAL} includes training on cardio-pulmonary resuscitation for staff. At minimum, doctors, nursing staff, technologists and rehabilitation staff are trained to at least basic life support (BLS); doctors and nurses working in intensive-care or high-dependency units undergo appropriate advanced training (for example ACLS, PALS or NRP, or an equivalent programme).

A staff member with a valid current training certificate does not repeat the training. Trainers may be internal or external, using established evidence-based protocols.""",

        "HRM.3.f": f"""Induction training at {HOSPITAL} includes training in hospital infection prevention and control — the policies, procedures and practices of the infection prevention and control programme.""",

        "HRM.3.g": f"""Induction training at {HOSPITAL} includes orientation to the organisation's service standards, so that staff are trained to implement them.""",

        "HRM.3.h": f"""Induction training at {HOSPITAL} includes an orientation on administrative procedures — attendance, leave, conduct and similar matters (HRM.2.d) — and awareness of organisation-wide policies and procedures.""",

        "HRM.3.i": f"""Induction training at {HOSPITAL} includes an orientation on the policies and procedures of the specific department, unit, service or programme the staff member will work in, delivered at that department/unit/service/programme level.""",

        "HRM.3.j": f"""Staff at {HOSPITAL} are trained on information systems, information security, information use and management, according to their job responsibility, job description and data and information needs. Where the hospital uses electronic health records, staff who access, review or document in the EMR are trained to ensure it is used correctly.""",

        # ---------------- HRM.4 — Professional training and development ----------------
        "HRM.4.a": f"""Written guidance governs training and development policy for staff at {HOSPITAL}: a training manual covering identification of training needs, methodology, documentation, assessment, impact evaluation and a training calendar. At minimum, staff are trained on occupational safety and soft skills, and educated on patient-centred care — respecting patient preferences, shared decision-making and integrated care.

Training covers all staff categories, including doctors and outsourced staff where applicable; learning-management systems or e-learning may be used. This is a CORE, asterisked element.""",

        "HRM.4.b": f"""The {hr} maintains the training record for {HOSPITAL}, covering every training session: at minimum the title, trainer(s), date, duration and list of trainees with signatures. Contents are captured where possible; records may be kept digitally.""",

        "HRM.4.c": f"""Training at {HOSPITAL} also occurs when job responsibilities change or new equipment is introduced, focused on the revised responsibilities or the newly introduced equipment and technology. For new equipment, operating staff are trained on both operational use and daily maintenance.""",

        "HRM.4.d": f"""Feedback mechanisms are in place at {HOSPITAL} for improving the training and development programme, covering both internal and external training — appropriateness of course material, training facilities and trainer capability.""",

        "HRM.4.e": f"""{HOSPITAL} evaluates training effectiveness immediately after training (for example a pre- and post-test) and again after a defined period has lapsed, to confirm the training improved workplace competency. The time frame for the later check may vary by training type; incident reports and assessment non-conformities are useful inputs.

The evaluation covers knowledge, skills and attitude; retraining is provided where the evaluation shows it is needed.""",

        "HRM.4.f": f"""{HOSPITAL} supports continuing professional development and learning, so staff can keep up with advancements in their field — encouraging and resourcing attendance at courses or conferences, and providing access to distance learning or e-learning. The hospital specifies minimum mandatory training hours every staff member attends each year.""",

        # ---------------- HRM.5 — Job-specific training ----------------
        "HRM.5.a": f"""Staff involved in blood transfusion services at {HOSPITAL} are trained in handling blood and blood products — safe transport, obtaining informed consent, required documentation, identifying and handling transfusion reactions, and educating the patient and family on donation. Relevant staff (doctors, nurses, technicians and staff transporting blood from the blood bank or storage unit) are trained on the aspects that apply to them. Cross-reference: COP.8 owns blood transfusion service practice; this element is the staff training layer.""",

        "HRM.5.b": f"""Relevant staff at {HOSPITAL} are trained in identifying and rendering care to vulnerable patients, per the hospital's written guidance. Cross-reference: COP.16.a owns the vulnerable-patient care process; this element is the staff training layer.""",

        "HRM.5.c": f"""Relevant staff at {HOSPITAL} are trained in the appropriate use of control and restraint techniques, per the hospital's written guidance. Cross-reference: COP.16.e owns the control-and-restraint process; this element is the staff training layer.""",

        "HRM.5.d": f"""Staff at {HOSPITAL} are trained in healthcare communication techniques, including handling challenging situations and good communication practice. Training needs may be identified from patient complaints, incident reports, appraisals and employee feedback. Cross-reference: PRE.8.e owns patient-facing communication practice; this element is the staff training layer.""",

        "HRM.5.e": f"""Staff involved in direct patient care at {HOSPITAL} are provided training on cardio-pulmonary resuscitation periodically, at the level (basic or advanced) appropriate to their role. Doctors, nurses and rehabilitation staff refresh at least once in two years, or sooner if protocol changes; staff in emergency, intensive care or high-dependency units undergo appropriate advanced training (for example ACLS, ATLS, PALS or NRP, or an equivalent). Trainers may be internal or external, using updated evidence-based protocols. This is a CORE element.""",

        "HRM.5.f": f"""{HOSPITAL} provides staff training on infection prevention and control through in-service sessions at least {yearly_check}, including antimicrobial policy and antimicrobial stewardship content for medical professionals, infection-prevention-and-control nurses, the clinical pharmacist and support staff.""",

        # ---------------- HRM.6 — Safety and quality training ----------------
        "HRM.6.a": f"""Staff at {HOSPITAL} are trained in the organisation's safety programme, including patient safety, through a regular training programme or printed materials. Staff working in laboratory and imaging services are additionally trained in their respective safety programmes. Cross-reference: PSQ.1.a owns the safety programme itself; this element is the staff training layer.""",

        "HRM.6.b": f"""Staff at {HOSPITAL} are trained in detecting, handling, minimising and eliminating identified risks in the organisation's environment — physical (poor lighting, slippery floors, blind corners, open electrical points, exposed wiring), chemical (mishandling, spills, aerosolisation), environmental (noise, smoke, dampness, heat) and process-related (needle-stick injury, blood and body-fluid exposure, cytotoxic drugs, soiled linen). Staff can practically demonstrate actions such as managing a blood spill or handling hazardous materials.""",

        "HRM.6.c": f"""Staff at {HOSPITAL} are made aware of the procedure to follow in the event of an incident, able to describe the sequence of events they will undertake if one occurs.""",

        "HRM.6.d": f"""Staff at {HOSPITAL} are trained in occupational safety aspects for the areas with identified occupational hazards — for example needle-stick injury and blood/body-fluid exposure, radiation exposure, laser exposure, medical-gas exposure, chemotherapy exposure and noise in utility areas — and in the preventive actions to avoid each risk. Cross-reference: IPC.8.a owns occupational-exposure IPC practice; this element is the staff training layer.""",

        "HRM.6.e": f"""Staff at {HOSPITAL} are trained in the organisation's disaster management plan, including their specific role in managing an internal or external disaster. This is a CORE element.""",

        "HRM.6.f": f"""Staff at {HOSPITAL} are trained in handling fire and non-fire emergencies: classes of fire, use of fire extinguishers, evacuation plans and fire procedures, plus the hospital's identified non-fire emergencies and each staff member's specific role in them. This is a CORE element.""",

        "HRM.6.g": f"""Staff at {HOSPITAL} are trained in the organisation's quality improvement programme — its structure and their own role in contributing to it. Staff working in laboratory, imaging, emergency, intensive care, the blood centre and surgical services are additionally trained on their respective quality assurance programmes.""",

        # ---------------- HRM.7 — Performance appraisal ----------------
        "HRM.7.a": f"""Performance appraisal is done for all categories of staff at {HOSPITAL}, starting with the person heading the organisation and including doctors, and includes competency assessment where appropriate. For outsourced staff, the appraisal may be done by the contractor. This is an asterisked element.""",

        "HRM.7.b": f"""Staff at {HOSPITAL} are made aware of the appraisal system at the time of induction — for example through the service booklet and as part of induction training (HRM.3).""",

        "HRM.7.c": f"""Performance is evaluated against pre-determined criteria at {HOSPITAL}, based on key performance indicators or key result areas derived from the job description.""",

        "HRM.7.d": f"""{HOSPITAL} uses the appraisal system as a tool for further development — identifying training requirements and providing for them where possible, with key result areas set for each staff member and a training-need assessment done. Written guidance covers effective management of underperformance.""",

        "HRM.7.e": f"""Performance appraisal at {HOSPITAL} is carried out at a defined interval and documented, at least {yearly_check}.""",

        # ---------------- HRM.8 — Disciplinary and grievance handling ----------------
        "HRM.8.a": f"""Written guidance governs disciplinary and grievance handling mechanisms at {HOSPITAL}, covering HRM.8.c–e, and including workplace grievances such as bullying and harassment. This is an asterisked element.""",

        "HRM.8.b": f"""The disciplinary and grievance handling mechanism at {HOSPITAL} is known to all categories of staff, who are aware of the procedure to follow if they feel aggrieved.""",

        "HRM.8.c": f"""The disciplinary policy and procedure at {HOSPITAL} are based on the principles of natural justice — both parties (employee and employer) are allowed to present their case before a decision is taken.""",

        "HRM.8.d": f"""The disciplinary and grievance procedure at {HOSPITAL} is in consonance with the prevailing laws — the applicable labour laws for this hospital's staff. An Internal Complaints Committee is established to handle complaints of sexual harassment. This is a CORE element.

Method note: keep the written procedure current against the labour law actually applicable to this hospital's staff category; do not import Central Civil Services rules as a blanket checklist unless this hospital's staff are in fact covered by them.""",

        "HRM.8.e": f"""{HOSPITAL} provides for appeals in all disciplinary cases, through a designated appellate authority higher than the disciplinary authority that issued the original decision.""",

        "HRM.8.f": f"""{HOSPITAL} takes action to redress grievances through the written redress procedure; actions taken are documented and communicated to the aggrieved staff member.""",

        # ---------------- HRM.9 — Staff health and safety ----------------
        "HRM.9.a": f"""{HOSPITAL} has written guidance on staff health and safety addressing physical and mental health and safe working conditions across all shifts, in consonance with the law of the land and good work practice. The hospital runs a staff vaccination and immunisation programme, provides appropriate personal protective equipment with training on its use, and supports staff (as "second victim") involved in unanticipated adverse events, medical error or patient-related injury. This is an asterisked element.""",

        "HRM.9.b": f"""Health checks for staff dealing with direct patient care are done at least {yearly_check} at {HOSPITAL}, with findings and results documented in the personal file. Parameters may differ by staff category; competent individuals may be identified to perform the checks. The staff member is not charged for the check; more frequent checks may be done where needed.""",

        "HRM.9.c": f"""{HOSPITAL} provides treatment to staff who sustain workplace-related injuries — for example needle-stick injuries, back injuries from patient transport, or noise-related hearing impairment — including counselling where appropriate. Injuries from workplace violence are included.""",

        "HRM.9.d": f"""{HOSPITAL} has measures in place for prevention and handling of workplace violence, using an integrative and participative approach: workplace risk assessment identifying situations of special risk, workplace interventions (information and communication), environmental interventions (signage, security, restricted access) and individual interventions (training). A mechanism handles these situations, including liaison with law enforcement where applicable and counselling for affected staff, as part of the hospital's written security guidance. This is a CORE, asterisked element.

Cross-reference: FMS.3.a owns the extra-security-area operational planning this measure sits alongside; this element is the workplace-violence prevention-and-handling programme itself.""",

        # ---------------- HRM.10 — Personal information ----------------
        "HRM.10.a": f"""Personal files are maintained for all staff at {HOSPITAL}, kept current and updated (electronic format is acceptable), with confidentiality maintained and access restricted.""",

        "HRM.10.b": f"""Each staff member's personal file at {HOSPITAL} contains their qualification, job description, verification of credentials and health status.""",

        "HRM.10.c": f"""Records of in-service training and education are maintained for staff at {HOSPITAL}. For internal training, an annual summary may be filed, with a supporting document verifying attendance. Where training records are held elsewhere, the personal file carries traceability to them; electronic training records are acceptable.""",

        "HRM.10.d": f"""Personal files at {HOSPITAL} contain the results of all evaluations and remarks — performance appraisals, training assessments, health-check outcomes, and records of achievement, appreciation, complaint, warning or memo.""",

        # ---------------- HRM.11 — Credentialing/privileging: medical ----------------
        "HRM.11.a": f"""{HOSPITAL} identifies medical professionals permitted by law, regulation and the organisation to provide patient care without supervision — individuals with the required qualification(s), training and experience, in consonance with the law. Providing unsupervised care outside this identified list is a stop-work trigger (section 6). This is a CORE element.""",

        "HRM.11.b": f"""The education, registration, training and experience of identified medical professionals at {HOSPITAL} are documented and updated periodically — after acquisition of new skills or qualification — and maintained in each professional's personal file.""",

        "HRM.11.c": f"""Information about medical professionals at {HOSPITAL} is appropriately verified when possible, by checking with the organisation that awarded the qualification or training. The National Medical Commission's website is a useful reference for verification.""",

        "HRM.11.d": f"""{HOSPITAL} grants medical professionals privileges to admit and care for patients in consonance with their qualification, training, experience and registration — identifying the clinical services each is authorised to perform (for example, radiotherapy only by a radiation oncologist). Privileges are reviewed at least {annually} and revised where necessary. Granting or exercising privileges outside this record is a stop-work trigger (section 6). This is a CORE element.""",

        "HRM.11.e": f"""The requisite services a medical professional at {HOSPITAL} is authorised to provide are known to that professional and to the relevant departments — for example OP consultation rights, admission rights and rights to specific procedures or surgeries (inclusion or exclusion). Concerned departments (for example, front desk for admission rights, the operation theatre for surgical rights) are informed of the relevant privileging.""",

        "HRM.11.f": f"""Medical professionals at {HOSPITAL} admit and care for patients as per their privileging, using a standardised format applied uniformly. New faculty may work under proctorship until independent privileges are granted; the hospital maintains a mechanism confirming professionals provide only the services they are privileged for.""",

        # ---------------- HRM.12 — Credentialing/privileging: nursing ----------------
        "HRM.12.a": f"""{HOSPITAL} identifies nursing staff permitted by law, regulation and the organisation to provide patient care without supervision — individuals with the required qualification(s), training and experience, in consonance with the law (Indian Nursing Council Act, 1947). Providing unsupervised care outside this identified list is a stop-work trigger (section 6). This is a CORE element.""",

        "HRM.12.b": f"""The education, registration, training and experience of nursing staff at {HOSPITAL} are documented and updated periodically, after acquisition of new skills or qualification.""",

        "HRM.12.c": f"""Information about nursing staff at {HOSPITAL} is appropriately verified when possible, by checking with the organisation that awarded the qualification or training.""",

        "HRM.12.d": f"""{HOSPITAL} grants nursing staff privileges in consonance with their qualification, training, experience and registration — identifying what each nurse is authorised to do (for example, an infection-prevention-and-control nurse needs the requisite in-house or external training, experience, aptitude and knowledge for that role). Privileges are reviewed at least {annually} and revised where necessary. Granting or exercising privileges outside this record is a stop-work trigger (section 6). This is a CORE element.""",

        "HRM.12.e": f"""The requisite services a nursing professional at {HOSPITAL} is authorised to provide are known to that professional, to nursing services and to the concerned departments, communicated internally.""",

        "HRM.12.f": f"""Nursing professionals at {HOSPITAL} care for patients as per their privileging. New staff may work under supervision until independent privileges are granted; the hospital maintains a mechanism confirming nursing professionals provide only the services they are privileged for.""",

        # ---------------- HRM.13 — Credentialing/privileging: para-clinical ----------------
        "HRM.13.a": f"""{HOSPITAL} identifies para-clinical professionals (for example physiotherapist, rehabilitation therapist, dietician, pharmacist, clinical pharmacist, technologist) permitted by law, regulation and the organisation to provide patient care without supervision — individuals with the required qualification(s), training and experience, in consonance with the law. Providing unsupervised care outside this identified list is a stop-work trigger (section 6). This is a CORE element.""",

        "HRM.13.b": f"""The education, registration, training and experience of para-clinical professionals at {HOSPITAL} are appropriately verified, documented and updated periodically, after acquisition of new skills or qualification, by checking with the organisation that awarded the qualification or training.""",

        "HRM.13.c": f"""{HOSPITAL} grants para-clinical professionals privileges in consonance with their qualification, training, experience and registration — specifying what each is authorised to do, with the requisite registration or licence held where applicable. Granting or exercising privileges outside this record is a stop-work trigger (section 6). This is a CORE element.""",

        "HRM.13.d": f"""The requisite services a para-clinical professional at {HOSPITAL} is authorised to provide are known to that professional and to the concerned departments, communicated internally.""",

        "HRM.13.e": f"""Para-clinical professionals at {HOSPITAL} care for patients as per their privileging. New staff may work under supervision until independent privileges are granted; the hospital maintains a mechanism confirming para-clinical professionals provide only the services they are privileged for.""",
    }
