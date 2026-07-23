import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const CORS = {
  "Access-Control-Allow-Origin": "https://accredready.in",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};

// ── SHCO General Reference Content ────────────────────────────────────────────
// Source: NABH Accreditation Standards for Small Healthcare Organizations,
// 3rd Edition, August 2022, ISBN 978-81-959676-1-2
const GENERAL_INFO = `
WHAT IS NABH?
National Accreditation Board for Hospitals and Healthcare Providers (NABH) is a constituent board of the Quality Council of India (QCI), set up to establish and operate accreditation programs for healthcare organisations. NABH is accredited by the International Society for Quality in Healthcare (ISQua).

ASSESSMENT MODES — THE THREE POINTS IN THE ACCREDITATION CYCLE:

Final Assessment — The initial assessment before first accreditation is granted. A team of assessors conducts an on-site evaluation. At this stage, only objective elements at Core and Commitment level are scored (357 of 408 total OEs). Accreditation is awarded for 4 years if criteria are met.

Surveillance Assessment — Conducted 14–18 months after accreditation is granted (midterm check during the 4-year cycle). At this stage, Core, Commitment, AND Achievement level OEs are scored (392 of 408 total OEs). This checks whether the hospital is improving and maintaining standards.

Renewal/Re-accreditation Assessment — Conducted before the 4-year accreditation expires (apply at least 6 months prior to expiry). At this stage, ALL OE levels are scored — Core, Commitment, Achievement, AND Excellence (all 408 OEs).

ACCREDITATION DECISION CRITERIA:

Final Assessment criteria: Overall compliance ≥80%; every Core OE score ≥4; average score per standard ≥4; average score per chapter ≥4; no standard with more than 1 OE scored ≤2; every OE scored ≤3 must have an accepted action plan with timelines.

Surveillance Assessment adds: Commitment level compliance ≥80%; Achievement level compliance ≥80%; improvement required on any OE that scored ≤2 in the previous assessment.

Re-accreditation Assessment adds: Excellence level compliance ≥80%; improvement required on any OE that scored ≤2 in the previous assessment; NOTE — the book's body text (p.22) states no standard should have ANY OE scored ≤2 (stricter than Final/Surveillance), though the book's own summary table (p.23) shows the same "1" limit for all three types — the conservative interpretation for Re-accreditation preparation is to aim for zero OEs ≤2 per standard.

OE LEVELS (Core / Commitment / Achievement / Excellence):
CORE — Standards the organisation MUST have in place to ensure quality of care and safety. Mandatorily assessed at every assessment stage. Score must never be below 4.
Commitment — Most objective elements sit here. These form the basis for accreditation at the Final Assessment.
Achievement — Reflects ongoing improvement beyond the basics. First assessed at the Surveillance stage (14–18 months post-accreditation).
Excellence — The highest level, reflecting a mature quality system. Only assessed at Re-accreditation (end of the 4-year cycle).
SHCO 3rd Edition breakdown: 408 total OEs = 100 Core + 257 Commitment + 35 Achievement + 16 Excellence, across 71 standards and 10 chapters.

SCORING SCALE (5-point, used in both self-assessment and official assessment):
Score 1 — No compliance: No systems in place; ≤20% of samples meet requirement; non-conformity exists.
Score 2 — Poor compliance: Elementary systems in place; 21–40% of samples meet requirement; non-conformity exists.
Score 3 — Partial compliance: Systems partially in place; 41–60% of samples meet requirement; non-conformity exists.
Score 4 — Good compliance: Systems in place with evidence of implementation; 61–80% of samples meet requirement; non-conformity could exist.
Score 5 — Full compliance: Systems fully implemented across the organisation; 81–100% of samples meet requirement; no non-conformity.
Note: the basis for scoring is implementation. If documentation is inadequate even when implementation is good, the score can be downgraded by one point.

WHAT IS A KPI?
KPI = Key Performance Indicator. Per Annexure 1 of the official SHCO 3rd Edition standards book: KPIs help to systematically monitor, evaluate, and continually improve service performance. By themselves, KPIs do not improve performance — they provide signposts that signal progress toward goals and opportunities for improvement. Each KPI has a standardised definition, formula (numerator/denominator), unit, and defined monitoring frequency. KPIs are separate from OE scoring — they are tracked on an ongoing basis (not scored 1–5 like OEs) and reviewed for trends over time.

WHAT IS A STANDARD vs AN OBJECTIVE ELEMENT (OE)?
Standard — A statement of expectation defining structures/processes that must be in place. Numbered serially: first 3 letters = chapter code, number = order within chapter (e.g. AAC.1 = first standard of the AAC chapter).
Objective Element (OE) — The measurable component of a standard, scored on the 1–5 scale during assessment. Numbered with a letter after the standard number (e.g. AAC.1.c = third OE of the first AAC standard).

THE 10 SHCO CHAPTERS (Total: 71 standards, 408 OEs):
1. AAC — Access, Assessment and Continuity of Care (8 standards, 48 OEs)
2. COP — Care of Patients (13 standards, 82 OEs)
3. MOM — Management of Medication (9 standards, 52 OEs)
4. PRE — Patient Rights and Education (6 standards, 39 OEs)
5. HIC — Hospital Infection Control (6 standards, 36 OEs)
6. PSQ — Patient Safety and Quality Improvement (5 standards, 28 OEs)
7. ROM — Responsibilities of Management (4 standards, 19 OEs)
8. FMS — Facility Management and Safety (5 standards, 29 OEs)
9. HRM — Human Resource Management (9 standards, 45 OEs)
10. IMS — Information Management System (6 standards, 30 OEs)
`.trim();

// ── NABH Official Glossary ─────────────────────────────────────────────────────
// Source: SHCO 3rd Edition Standards Book, pp.138–150
// PDF ligature artifacts (fi/fl) corrected during embedding.
const GLOSSARY: Record<string, string> = {
  "accreditation": "Accreditation is a self-assessment and external peer review process used by healthcare organisations to accurately assess their level of performance in relation to established standards and to implement ways to improve the healthcare system continuously.",
  "accreditation assessment": "The evaluation process for assessing the compliance of an organisation with the applicable standards for determining its accreditation status.",
  "advance life support": "Emergency medical care for sustaining life, including defibrillation, airway management, and drugs and medications.",
  "adverse drug reaction": "A response to a drug which is noxious and unintended and which occurs at doses normally used in man for prophylaxis, diagnosis, or therapy of disease or for the modification of physiologic function.",
  "adverse event": "An injury related to medical management, in contrast to complications of the disease. Medical management includes all aspects of care, including diagnosis and treatment, failure to diagnose or treat, and the systems and equipment used to deliver care. Adverse events may be preventable or non-preventable. (WHO Draft Guidelines for Adverse Event Reporting and Learning Systems)",
  "anaesthesia death": "Defined as death occurring within 24 hours of administration of anaesthesia due to cases related to anaesthesia. However, death may occur even afterwards due to the complications.",
  "assessment": "All activities including history taking, physical examination, laboratory investigations that contribute towards determining the prevailing clinical status of the patient.",
  "barrier nursing": "The nursing of patients with infectious diseases in isolation to prevent the spread of infection. The aim is to erect a barrier to the passage of infectious pathogenic organisms between the contagious patient and other patients and staff in the hospital, and thence to the outside world. The nurses wear gowns, masks, and gloves, and observe strict rules that minimise the risk of passing on infectious agents.",
  "basic life support": "Basic life support (BLS) is the level of medical care which is used for patients with life-threatening illnesses or injuries until the patient can be given full medical care.",
  "breakdown maintenance": "Activities which are associated with the repair and servicing of site infrastructure, buildings, plant or equipment within the site's agreed building capacity allocation which have become inoperable or unusable because of the failure of component parts.",
  "byelaws": "A rule governing the internal management of an organisation. It can supplement or complement the government law but cannot countermand it, e.g. municipal by-laws for construction of hospitals/nursing homes, for disposal of hazardous and/or infectious waste.",
  "calibration": "Set of operations that establish, under specified conditions, the relationship between values of quantities indicated by a measuring instrument or measuring system, or values represented by a material measure or a reference material, and the corresponding values realised by standards.",
  "care plan": "A plan that identifies patient care needs, lists the strategy to meet those needs, documents treatment goals and objectives, outlines the criteria for ending interventions, and documents the individual's progress in meeting specified goals and objectives. The format of the plan may be guided by specific policies and procedures, protocols, practice guidelines or a combination of these. It includes preventive, promotive, curative and rehabilitative aspects of care.",
  "citizen's charter": "A document which represents a systematic effort to focus on the commitment of the organisation towards its citizens in respects of standard of services, information, choice and consultation, non-discrimination and accessibility, grievance redress, courtesy and value for money.",
  "clinical audit": "A quality improvement process that seeks to improve patient care and outcomes through systematic review of care against explicit criteria and the implementation of change. (Reference: Principles for Best Practice in Clinical Audit 2002, NICE/CHI)",
  "clinical autopsy": "A surgical procedure that consists of an examination of a corpse by dissection to identify the cause, mode and manner of death or to evaluate any disease or injury that may be present for research or educational purposes.",
  "clinical care pathway": "Standardised evidence-based, multidisciplinary management plans. They identify an appropriate sequence of clinical interventions, timeframes, milestones and expected outcomes for a homogenous patient group.",
  "clinical practice guidelines": "Systematically developed statements to assist practitioner and patient decisions about appropriate health care for specific clinical circumstances.",
  "competence": "Demonstrated ability to apply knowledge and skills (para 3.9.2 of ISO 9000:2015). Knowledge is the understanding of facts and procedures. Skill is the ability to perform a specific action.",
  "confidentiality": "Restricted access to information to individuals who have a need, a reason and permission for such access. It also includes an individual's right to personal privacy as well as the privacy of information related to his/her healthcare records.",
  "consent": "1. The willingness of a party to undergo examination/procedure/treatment by a healthcare provider. It may be implied (e.g. patient registering in OPD), expressed which may be written or verbal. Informed consent is a type of consent in which the healthcare provider has a duty to inform his/her patient about the procedure, its potential risk and benefits, alternative procedure with their risk and benefits so as to enable the patient to make an informed decision of his/her healthcare. 2. In law, it means active acquiescence or silent compliance by a person legally capable of consenting. In India, the legal age of consent is 18 years.",
  "control charts": "The statistical tool used in quality control to (1) analyse and understand process variables, (2) determine process capabilities, and to (3) monitor effects of the variables on the difference between target and actual performance. Control charts indicate upper and lower control limits, and often include a central (average) line, to help detect the trend of plotted values.",
  "correction": "Action to eliminate the detected non-conformity. (Reference: ISO 9000:2015)",
  "corrective action": "Action to eliminate the cause of a non-conformity and to prevent recurrence. (Reference: ISO 9000:2015)",
  "credentialing": "The process of obtaining, verifying and assessing the qualifications of a healthcare provider.",
  "data": "A record of the event.",
  "discharge summary": "A part of a patient record that summarises the reasons for admission, significant clinical findings, procedures performed, treatment rendered, patient's condition on discharge and any specific instructions given to the patient or family (for example follow-up medications).",
  "disciplinary procedure": "A sequence of activities to be carried out when staff does not conform to the laid-down norms, rules and regulations of the healthcare organisation.",
  "drug dispensing": "The preparation, packaging, labelling, record keeping, and transfer of a prescription drug to a patient or an intermediary, who is responsible for the administration of the drug. (Reference: Mosby's Medical Dictionary, 9th edition, 2009, Elsevier.)",
  "drug administration": "The giving of a therapeutic agent to a patient, e.g. by infusion, inhalation, injection, paste, pessary, suppository or tablet.",
  "effective communication": "Communication between two or more persons wherein the intended message is successfully delivered, received and understood. It also includes several other skills such as non-verbal communication, engaged listening, ability to speak assertively, etc.",
  "employees": "All members of the healthcare organisation who are employed full time and are paid suitable remuneration for their services as per the laid-down policy.",
  "end-of-life care": "Helps all those with an advanced, progressive, incurable illness to live as well as possible until they die. It enables the supportive and palliative care needs of both patient and family to be identified and met throughout the last phase of life and into bereavement. It includes management of pain and other symptoms and provision of psychological, social, spiritual and practical support.",
  "enhanced communication": "Using the methods of communication to ensure meaning and understanding through the recognition of the limitations of others. The intent is to ensure purposeful, timely and reliable communication. The communication must be sensitive, empathetic and inclusive.",
  "ethics": "Moral principles that govern a person's or group's behaviour.",
  "evidence-based medicine": "The conscientious, explicit, and judicious use of current best evidence in making decisions about the care of individual patients.",
  "family": "The person(s) with a significant role in the patient's life. It mainly includes spouse, children and parents. It may also include a person not legally related to the patient but can make healthcare decisions for a patient if the patient loses decision-making ability.",
  "failure mode and effect analysis": "A method used to prospectively identify error risks within a particular process.",
  "fmea": "A method used to prospectively identify error risks within a particular process. (Failure Mode and Effect Analysis)",
  "formulary": "An approved list of drugs. Drugs contained in the formulary are generally those that are determined to be cost-effective and medically effective.",
  "goal": "A broad statement describing a desired future condition or achievement without being specific about how much and when. Goals can be both short- and longer-term. Goals are ends that guide actions. (Reference: Malcolm Baldridge National Quality Award)",
  "grievance-handling procedures": "The sequence of activities carried out to address the grievances of patients, visitors, relatives and staff.",
  "hazardous materials": "Substances dangerous to human and other living organisms. They include radioactive or chemical materials.",
  "hazardous waste": "Waste materials dangerous to living organisms. Such materials require special precautions for disposal. They include the biologic waste that can transmit disease (for example, blood, tissues) radioactive materials, and toxic chemicals. Other examples are infectious waste such as used needles, used bandages and fluid soaked items.",
  "healthcare-associated infection": "An infection occurring in a patient during the process of care in a hospital or other healthcare facility which was not present or incubating at the time of admission. Also referred to as 'nosocomial' or 'hospital' infection. (Reference: World Health Organization)",
  "healthcare organisation": "The generic term used to describe the various types of organisation that provide healthcare services. This includes ambulatory care centres, hospitals, laboratories, etc.",
  "high-dependency unit": "An area for patients who require more intensive observation, treatment and nursing care than are usually provided for in a ward. It is a standard of care between the ward and full intensive care.",
  "high risk medications": "Medications involved in a high percentage of medication errors or sentinel events and medications that carry a high risk for abuse, error, or other adverse outcomes. Examples include medications with a low therapeutic index, controlled substances, psychotherapeutic medications, and look-alike and sound-alike medications.",
  "high alert medications": "Medications involved in a high percentage of medication errors or sentinel events and medications that carry a high risk for abuse, error, or other adverse outcomes. Examples include medications with a low therapeutic index, controlled substances, psychotherapeutic medications, and look-alike and sound-alike medications.",
  "incident reporting": "Written or verbal reporting of any event in the process of patient care, that is inconsistent with the deserved patient outcome or routine operations of the healthcare facility.",
  "in-service education": "Organised education/training usually provided in the workplace for enhancing the skills of staff members or for teaching them new skills relevant to their jobs/tasks.",
  "in-service training": "Organised education/training usually provided in the workplace for enhancing the skills of staff members or for teaching them new skills relevant to their jobs/tasks.",
  "indicator": "A statistical measure of the performance of functions, systems or processes over time. For example, hospital acquired infection rate, mortality rate, caesarean section rate, absence rate, etc.",
  "information": "Processed data which lends meaning to the raw data.",
  "intent": "A brief explanation of the rationale, meaning and significance of the standards laid down in a particular chapter.",
  "inventory control": "The method of supervising the intake, use and disposal of various goods in hands. It relates to supervision of the supply, storage and accessibility of items in order to ensure an adequate supply without stock-outs/excessive storage. It is also the process of balancing ordering costs against carrying costs of the inventory so as to minimise total costs.",
  "isolation": "Separation of an ill person who has a communicable disease (e.g., measles, chickenpox, mumps, SARS) from those who are healthy. Isolation prevents transmission of infection to others and also allows the focused delivery of specialised health care to ill patients.",
  "job description": "An explanation pertaining to duties, responsibilities and conditions required to perform a job. A summary of the most important features of a job, including the general nature of the work performed (duties and responsibilities) and level (i.e., skill, effort, responsibility and working conditions) of the work performed.",
  "job specification": "The qualifications/physical requirements, experience and skills required to perform a particular job/task. A statement of the minimum acceptable qualifications that an incumbent must possess to perform a given job successfully.",
  "maintenance": "The combination of all technical and administrative actions, including supervision actions, intended to retain an item in, or restore it to, a state in which it can perform a required function. (Reference: British Standard 3811:1993)",
  "medical equipment": "Any fixed or portable non-drug item or apparatus used for diagnosis, treatment, monitoring and direct care of a patient.",
  "medication error": "Any preventable event that may cause or lead to inappropriate medication use or patient harm while the medication is in the control of the health care professional, patient, or consumer. Such events may be related to professional practice, health care products, procedures, and systems, including prescribing; order communication; product labelling, packaging, and nomenclature; compounding; dispensing; distribution; administration; education; monitoring; and use. (Reference: The National Coordinating Council for Medication Error Reporting and Prevention)",
  "medication order": "A written order by a physician, dentist, or other designated health professionals for a medication to be dispensed by a pharmacy for administration to a patient. (Reference: Mosby's Medical Dictionary, 10th edition, Elsevier)",
  "mission": "An organisation's purpose. This refers to the overall function of an organisation. The mission answers the question, 'What is this organisation attempting to accomplish?' The mission might define patients, stakeholders, or markets served, distinctive or core competencies or technologies used.",
  "monitoring": "The performance and analysis of routine measurements aimed at identifying and detecting changes in the health status or the environment. It requires careful planning and use of standardised procedures and methods of data collection.",
  "multidisciplinary": "A generic term which includes representatives from various disciplines, professions or service areas.",
  "near-miss": "An unplanned event that did not result in injury, illness, or damage — but had the potential to do so. Errors that did not result in patient harm, but could have, can be categorised as near-misses.",
  "no harm": "Used synonymously with a near miss. A near-miss is defined when an error is realised just in the nick of time, and abortive action is instituted to cut short its translation. In a no-harm scenario, the error is not recognised, and the deed is done, but fortunately the expected adverse event does not occur.",
  "notifiable disease": "Certain specified diseases which are required by law to be notified to the public health authorities. Under WHO's International Health Regulations 2005, diseases always notifiable to WHO include: Smallpox, Poliomyelitis due to wild-type poliovirus, Human influenza caused by a new subtype, and Severe acute respiratory syndrome (SARS). In India, diseases such as Polio, Influenza, Malaria, Rabies, HIV/AIDS, Tuberculosis, Leprosy, Dengue fever are also notifiable (may vary by state).",
  "nursing empowerment": "Empowerment for nurses may consist of three components: a workplace that has the requisite structures to promote empowerment; a psychological belief in one's ability to be empowered; and acknowledgement that there is power in the relationships and caring that nurses provide. It includes structural empowerment (access to information, resources, support, and opportunity) and psychological empowerment (meaning, competence, self-determination, and impact).",
  "objective": "A specific statement of a desired short-term condition or achievement; includes measurable end-results to be accomplished by specific teams or individuals within time limits. (Reference: American Society for Quality)",
  "objective element": "That component of standard which can be measured objectively on a rating scale. Acceptable compliance with the measurable elements will determine the overall compliance with the standard.",
  "occupational health hazard": "The hazards to which an individual is exposed during the course of the performance of his job. These include physical, chemical, biological, mechanical and psychosocial hazards.",
  "operational plan": "The operational plan is the part of your strategic plan. It defines how you will operate in practice to implement your action and monitoring plans — what your capacity needs are, how you will engage resources, how you will deal with risks, and how you will ensure the sustainability of the organisation's achievements.",
  "organogram": "A graphic representation of the reporting relationship in an organisation.",
  "outsourcing": "Hiring of services and facilities from other organisations based upon one's own requirement in areas where such facilities are either not available or are not cost-effective. When an activity is outsourced, there should be a memorandum of understanding that clearly lays down the obligations of both organisations.",
  "patient-care setting": "The location where a patient is provided health care as per his needs, e.g. ICU, speciality ward, private ward and general ward.",
  "patient record": "A document which contains the chronological sequence of events that a patient undergoes during his stay in the healthcare organisation. It includes demographic data of the patient, assessment findings, diagnosis, consultations, procedures undergone, progress notes and discharge summary.",
  "medical record": "A document which contains the chronological sequence of events that a patient undergoes during his stay in the healthcare organisation. It includes demographic data, assessment findings, diagnosis, consultations, procedures undergone, progress notes and discharge summary.",
  "clinical record": "A document which contains the chronological sequence of events that a patient undergoes during his stay in the healthcare organisation. It includes demographic data, assessment findings, diagnosis, consultations, procedures undergone, progress notes and discharge summary.",
  "prems": "Patient-reported experience measures — questionnaires measuring the patients' perceptions of their experience whilst receiving care.",
  "patient-reported experience measures": "Questionnaires measuring the patients' perceptions of their experience whilst receiving care.",
  "proms": "Patient-reported outcome measures — questionnaires measuring the patients' views of their health status.",
  "patient-reported outcome measures": "Questionnaires measuring the patients' views of their health status.",
  "patient satisfaction": "A measure of the extent to which a patient is content with the health care which they received from their health care provider. Patient satisfaction is a proxy but a very effective indicator to measure the success of healthcare providers.",
  "patient experience": "The sum of all interactions, shaped by an organisation's culture, that influence patient perceptions across the continuum of care. It is a holistic perception that the patient forms about the healthcare provider based on the overall interactions/care touchpoints.",
  "performance appraisal": "The process of evaluating the performance of staff during a defined period of time with the aim of ascertaining their suitability for the job, the potential for growth as well as determining training needs.",
  "point of care equipment": "Medical equipment that is used to deliver care/intervene at or near the site of patient care. These are primarily Point-of-care testing (POCT), or bedside testing equipment that helps in reducing turn-around times. Examples: Glucometer, ABG Analyser, Stat Lab at ICU/ER, portable USG.",
  "policies": "Guidelines for decision-making, e.g. admission, discharge policies, antibiotic policy, etc.",
  "preventive action": "Action to eliminate the cause of a potential non-conformity. (Reference ISO 9000:2015)",
  "preventive maintenance": "A set of activities performed on plant equipment, machinery, and systems before the occurrence of a failure in order to protect them and to prevent or eliminate any degradation in their operating conditions. The maintenance carried out at predetermined intervals or according to prescribed criteria and intended to reduce the probability of failure or the degradation of the functioning of an item.",
  "prescription": "A document given by a physician or other healthcare practitioner in the form of instructions that govern the care plan for an individual patient. Legally, it is a written directive, for compounding or dispensing and administration of drugs, or for other service to a particular patient. (Reference: Miller-Keane Encyclopedia and Dictionary of Medicine, Nursing, and Allied Health, Seventh Edition, Saunders)",
  "privileging": "The process for authorising all medical professionals to admit and treat patients and provide other clinical services commensurate with their qualifications and skills.",
  "privileged communication": "Confidential information furnished (to facilitate diagnosis and treatment) by the patient to a professional authorised by law to provide care and treatment.",
  "procedural sedation": "A technique of administering sedatives or dissociative agents with or without analgesics to induce a state that allows the patient to tolerate unpleasant procedures while maintaining cardiorespiratory function. Procedural sedation and analgesia (PSA) is intended to result in a depressed level of consciousness that allows the patient to maintain oxygenation and airway control independently. (Reference: The American College of Emergency Physicians)",
  "procedure": "1. A specified way to carry out an activity or a process (ISO 9000:2015). 2. A series of activities for carrying out work which when observed by all help to ensure the maximum use of resources and efforts to achieve the desired output.",
  "process": "A set of interrelated or interacting activities which transforms inputs into outputs. (ISO 9000:2015)",
  "programme": "A sequence of activities designed to implement policies and accomplish objectives.",
  "protocol": "A plan or a set of steps to be followed in a study, an investigation or an intervention.",
  "quality": "1. Degree to which a set of inherent characteristics fulfil requirements (ISO 9000:2015). 2. Degree of adherence to pre-established criteria or standards.",
  "quality assurance": "Part of quality management focused on providing confidence that quality requirements will be fulfilled. (ISO 9000:2015)",
  "quality improvement": "Ongoing response to quality assessment data about a service in ways that improve the process by which services are provided to consumers/patients.",
  "radiation safety": "Safety issues and protection from radiation hazards arising from the handling of radioactive materials or chemicals and exposure to Ionizing and Non-Ionizing Radiation. In a healthcare setting, this commonly refers to X-ray machines, CT/PET CT Scans, Electron microscopes, Particle accelerators, Cyclotron, etc.",
  "re-assessment": "Implies a continuous and ongoing assessment of the patient, which is recorded in the medical records as progress notes.",
  "reconciliation of medications": "The process of creating the most accurate list possible of all medications a patient is taking — including drug name, dosage, frequency, and route — and comparing that list against the physician's admission, transfer, and/or discharge orders, with the goal of providing correct medications to the patient at all transition points within the hospital. (Reference: Institute for Healthcare Improvement)",
  "resources": "All inputs in terms of men, material, money, machines, minutes (time), methods, metres (space), skills, knowledge and information that are needed for the efficient and effective functioning of an organisation.",
  "restraints": "Devices used to ensure safety by restricting and controlling a person's movement. Restraint may be physical or chemical (by use of sedatives).",
  "risk abatement": "Minimising the risk or minimising the impact of that risk.",
  "risk assessment": "The determination of the quantitative or qualitative value of risk related to a concrete situation and a recognised threat (also called hazard). Risk assessment is a step in a risk management procedure.",
  "risk management": "Clinical and administrative activities to identify, evaluate and reduce the risk of injury.",
  "risk mitigation": "A strategy to prepare for and lessen the effects of threats and disasters. Risk mitigation takes steps to reduce the negative effects of threats and disasters.",
  "risk reduction": "The decrease in the risk of a healthcare facility, given activity, and treatment process with respect to patient, staff, visitors and community.",
  "root cause analysis": "A structured process that uncovers the physical, human, and latent causes of any undesirable event in the workplace. RCA is a method of problem-solving that tries to identify the root causes of faults or problems that cause operating events. By focusing correction on root causes, problem recurrence can be prevented.",
  "rca": "Root Cause Analysis — A structured process that uncovers the physical, human, and latent causes of any undesirable event in the workplace. By focusing correction on root causes, problem recurrence can be prevented.",
  "safety": "The degree to which the risk of an intervention/procedure, in the care environment is reduced for a patient, visitors and healthcare providers.",
  "safety programme": "A programme focused on patient, staff and visitor safety.",
  "scope of services": "Range of clinical and supportive activities that are provided by a healthcare organisation.",
  "security": "Protection from loss, destruction, tampering, and unauthorised access or use.",
  "sedation": "The administration to an individual, in any setting for any purpose, by any route, moderate or deep sedation. There are three levels: Minimal sedation (anxiolysis) — a drug-induced state during which patients respond normally to verbal commands; Moderate sedation/analgesia (conscious sedation) — a drug-induced depression of consciousness during which patients respond purposefully to verbal commands; Deep sedation/analgesia — a drug-induced depression of consciousness during which patients cannot be easily aroused but respond purposefully after repeated or painful stimulation.",
  "sentinel events": "A relatively infrequent, unexpected incident, related to system or process deficiencies, which leads to death or major and enduring loss of function for a recipient of healthcare services. Major and enduring loss of function refers to sensory, motor, physiological, or psychological impairment not present at the time services were sought or begun. The impairment lasts for a minimum period of two weeks and is not related to an underlying condition.",
  "social responsibility": "A balanced approach for an organisation to address economic, social and environmental issues in a way that aims to benefit people, communities and society, e.g. adoption of villages for providing health care, holding of medical camps and proper disposal of hospital wastes.",
  "sound clinical practice": "Practitioner decisions based on available knowledge, principles and practices for specific clinical situations.",
  "special educational needs of the patient": "In addition to routine care carried by healthcare professionals, patients and family have special educational needs depending on the situation. These are greatly influenced by literacy, educational level, language, emotional barriers and physical and cognitive limitations.",
  "staff": "All personnel working in the organisation including employees, 'fee-for-service' medical professionals, part-time workers, contractual personnel and volunteers.",
  "standard precautions": "1. A method of infection control in which all human blood and other bodily fluids are considered infectious for HIV, HBV and other blood-borne pathogens, regardless of patient history. It encompasses the use of personal protective equipment (PPE), disposal of sharps and safe housekeeping. 2. Standard Precautions apply to blood, all body fluids, secretions, and excretions (except sweat) regardless of whether or not they contain visible blood, non-intact skin and mucous membranes.",
  "standards": "A statement of expectation that defines the structures and processes that must be substantially in place in an organisation to enhance the quality of care.",
  "sterilisation": "The process of killing or removing microorganisms including their spores by thermal, chemical or irradiation means.",
  "strategic plan": "An organisation's process of defining its strategy or direction and making decisions on allocating its resources to pursue this strategy, including its capital and people. The process by which an organisation envisions its future and develops strategies, goals, objectives and action plans to achieve that future.",
  "surveillance": "The continuous scrutiny of factors that determines the occurrence and distribution of diseases and other conditions of ill health. It implies watching over with great attention, authority and often with suspicion. It requires professional analysis and sophisticated interpretation of data leading to recommendations for control activities.",
  "table-top exercise": "An activity in which key personnel assigned emergency management roles and responsibilities are gathered to discuss, in a non-threatening environment, various simulated emergency situations.",
  "traceability": "The ability to trace the history, application, use and location of an item or its characteristics through recorded identification data. (Reference: ISO 9000:2015)",
  "transfusion reaction": "A problem that occurs after a patient receives a transfusion of blood.",
  "triage": "A process of prioritising patients based on the severity of their condition so as to treat as many as possible when resources are insufficient for all to be treated immediately.",
  "turn-around-time": "The amount of time taken to complete a process or fulfil a request.",
  "tat": "Turn-around-time — the amount of time taken to complete a process or fulfil a request.",
  "unstable patient": "A patient whose vital parameters need external assistance for their maintenance.",
  "validated tool": "A questionnaire/scale that has been developed to be administered among the intended respondents. The validation processes should have been completed using a representative sample, demonstrating adequate reliability (the ability of the instrument to produce consistent results) and validity (the ability of the instrument to produce true results).",
  "validation": "Verification, where the specified requirements are adequate for the intended use.",
  "values": "The fundamental beliefs that drive organisational behaviour and decision-making. This refers to the guiding principles and behaviours that embody how an organisation and its people are expected to operate. Values reflect and reinforce the desired culture of an organisation.",
  "verbal order": "Orders given by a physician with prescriptive authority to a licensed person who is authorised by the organisation.",
  "verification": "The provision of objective evidence that a given item fulfils specified requirements.",
  "vision": "An overarching statement of the way an organisation wants to be, an ideal state of being at a future point. This refers to the desired future state of an organisation — where the organisation is headed, what it intends to be, or how it wishes to be perceived in the future.",
  "vulnerable patient": "Those patients who are prone to injury and disease by virtue of their age, sex, physical, mental and immunological status, e.g. infants, elderly, physically- and mentally-challenged, semiconscious/unconscious, those on immunosuppressive and/or chemotherapeutic agents.",
  "workplace violence": "Incidents where staff are abused, threatened or assaulted in circumstances related to their work, including commuting to and from work, involving an explicit or implicit challenge to their safety, well-being or health. (Adapted from European Commission)",
};

// ── SHCO KPI Content ──────────────────────────────────────────────────────────
// Source: NABH Accreditation Standards for Small Healthcare Organizations,
// 3rd Edition, August 2022, Annexure 1 (pp.151–159)
const SHCO_KPI_CONTENT = `
SHCO FULL — THE 15 MANDATORY KPIs
Source: NABH SHCO 3rd Edition, Annexure 1, pages 151–159

KPIs must be tracked monthly. Assessors verify at least 3 months of data before accreditation is granted. KPIs are separate from OE scoring — they are not rated 1–5, they are tracked as numbers/rates over time.

SAMPLING METHODOLOGY (applies to KPIs 1, 2, and 10 only):
Stratified random sampling is required — NOT convenience sampling. Sample size is calculated using Solvin's formula: n = N / (1 + Ne²) at 95% confidence interval, where N is the average of the preceding 3 months for the relevant metric.

SAMPLE SIZE TABLE (Solvin's formula, 95% CI):
Screening population 50 → required sample 44
Screening population 100 → required sample 79
Screening population 150 → required sample 108
Screening population 200 → required sample 132
Screening population 500 → required sample 217
Screening population 1000 → required sample 278
Screening population 2000 → required sample 322
Screening population 5000 → required sample 357
Screening population 10000 → required sample 370
Screening population 20000 → required sample 377

---

PSQ.2a — Patient Safety Quality Indicators (KPIs 1–5):

KPI 1: Time for initial assessment of indoor patients
Formula: Sum of time taken for assessment (minutes) / Total number of admissions (sample)
Unit: Minutes
Frequency: Monthly
Sampling required: YES — stratified random sample

KPI 2: Incidence of medication errors
Formula: Total number of medication errors / Total number of opportunities × 100
Unit: % (percentage)
Frequency: Monthly
Sampling required: YES — stratified random sample

KPI 3: Percentage of transfusion reactions
Formula: Number of transfusion reactions / Number of units transfused × 100
Unit: % (percentage)
Frequency: Monthly
Sampling required: No

KPI 4: Standardised Mortality Ratio for ICU (SMR-ICU)
Formula: Actual ICU deaths / Predicted ICU deaths
Unit: Ratio
Frequency: Monthly
Sampling required: No

KPI 5: Incidence of hospital-associated pressure ulcers after admission
Formula: Number of new or worsening pressure ulcers after admission / Total patient days × 1000
Unit: Per 1000 patient days
Frequency: Monthly
Sampling required: No

---

PSQ.2b — Infection Control & Safety Indicators (KPIs 6–11):

KPI 6: Catheter-associated UTI rate (CAUTI)
Formula: Number of UTIs associated with urinary catheter in the month / Number of urinary catheter days in that month × 1000
Unit: Per 1000 catheter days
Frequency: Monthly
Sampling required: No

KPI 7: Ventilator-associated Pneumonia rate (VAP)
Formula: Number of VAP cases in the month / Number of ventilator days in that month × 1000
Unit: Per 1000 ventilator days
Frequency: Monthly
Sampling required: No

KPI 8: Central line-associated Blood Stream Infection rate (CLABSI)
Formula: Number of CLABSI cases in the month / Number of central line days in that month × 1000
Unit: Per 1000 central line days
Frequency: Monthly
Sampling required: No

KPI 9: Surgical site infection rate (SSI)
Formula: Number of SSIs in a given month / Number of surgeries performed in that month × 100
Unit: Per 100 procedures
Frequency: Monthly
Sampling required: No
IMPORTANT SPECIAL NOTE: SSI has a rolling/cumulative surveillance methodology. The numerator updates over a 30-day and then 90-day window after the reporting month — SSIs can manifest up to 90 days post-surgery. This means the "final" SSI rate for any given month is not fully known until approximately 90 days later. When presenting SSI data to NABH assessors, explain this lag — the current month's rate may still be preliminary.

KPI 10: Compliance to hand hygiene practice
Formula: Total number of hand hygiene actions performed (compliant) / Total number of hand hygiene opportunities × 100
Unit: % (percentage)
Frequency: Monthly
Sampling required: YES — stratified random sample

KPI 11: Percentage of cases receiving appropriate prophylactic antibiotics within specified timeframe
Formula: Number of patients who received appropriate prophylactic antibiotic (correct dose and timing) / Number of patients who underwent surgery × 100
Unit: % (percentage)
Frequency: Monthly
Sampling required: No

---

PSQ.2c — Waiting Time Indicators (KPIs 12–13):

KPI 12: Waiting time for diagnostics
Formula: Sum total waiting time (minutes) / Number of patients reported in diagnostics
Unit: Minutes
Frequency: Monthly
Sampling required: No

KPI 13: Time taken for discharge
Formula: Sum of time taken for discharge (minutes) / Number of patients discharged
Unit: Minutes
Frequency: Monthly
Sampling required: No

---

PSQ.2d — Safety Event Indicators (KPIs 14–15):

KPI 14: Incidence of patient falls
Formula: Number of patient falls / Total patient days × 1000
Unit: Per 1000 patient days
Frequency: Monthly
Sampling required: No

KPI 15: Rate of needlestick injuries
Formula: Number of needlestick injuries / Number of occupied beds × 100
Unit: Per 100 occupied beds (cumulative year-to-date)
Frequency: Monthly — reported as cumulative YTD
Sampling required: No
IMPORTANT SPECIAL NOTE: Unlike all other KPIs which are monthly snapshots, needlestick injury rate is reported cumulatively year-to-date. For example, the February report includes January + February combined data. The denominator uses occupied beds for the cumulative period, not just the reporting month.
`.trim();

// ── SHCO Medication Error Monitoring Content ──────────────────────────────────
// Source: NABH SHCO 3rd Edition, Annexure 2 "Guidance on Monitoring Medication
// Errors" (pp.160–165). NCC-MERP categorization © 2001 NCC-MERP.
const MEDICATION_ERROR_CONTENT = `
SHCO FULL — MEDICATION ERROR MONITORING (Annexure 2, pp.160–165)
Categorization framework: NCC-MERP (National Coordinating Council for Medication Error Reporting and Prevention)

DEFINITION OF A MEDICATION ERROR (NCC-MERP):
A medication error is any preventable event that may cause or lead to inappropriate medication use or patient harm while the medication is in the control of the healthcare professional, patient, or consumer. Such events may relate to professional practice, healthcare products, procedures, and systems — including prescribing, order communication, product labelling, packaging and nomenclature, compounding, dispensing, distribution, administration, education, monitoring, and use.

---

CATEGORIES OF MEDICATION ERROR — 4 HARM LEVELS, 9 CATEGORIES (A through I):

NO ERROR:
Category A — Circumstances or events that have the capacity to cause error (but no error occurred)

ERROR, NO HARM:
Category B — An error occurred, but it did NOT reach the patient (note: an "error of omission" DOES reach the patient and is NOT Category B)
Category C — An error occurred that reached the patient but did NOT cause harm
Category D — An error reached the patient and required monitoring to confirm no harm resulted, and/or required intervention to preclude harm

ERROR, HARM:
Category E — An error that may have contributed to or resulted in TEMPORARY harm, requiring intervention
Category F — An error that may have contributed to or resulted in TEMPORARY harm, requiring INITIAL OR PROLONGED HOSPITALIZATION
Category G — An error that may have contributed to or resulted in PERMANENT patient harm
Category H — An error that required intervention NECESSARY TO SUSTAIN LIFE (e.g. CPR, defibrillation, intubation)

ERROR, DEATH:
Category I — An error that may have contributed to or resulted in the patient's DEATH

---

KEY DEFINITIONS:
Harm — Impairment of the physical, emotional, or psychological function or structure of the body, and/or pain resulting therefrom.
Monitoring — To observe or record relevant physiological or psychological signs.
Intervention — May include change in therapy or active medical/surgical treatment.
Intervention Necessary to Sustain Life — Includes cardiovascular and respiratory support (e.g. CPR, defibrillation, intubation).

---

CLASSIFICATION ALGORITHM (work through these questions in order):
1. Did an actual error occur? → NO = Category A
2. Did the error reach the patient? → NO = Category B
3. Did the error contribute to or result in patient DEATH? → YES = Category I
4. Was the patient harmed? → NO branch:
   - Was extra monitoring or intervention to preclude harm required? → YES = Category D; NO = Category C
5. If patient WAS harmed:
   - Did the error require intervention necessary to sustain life? → YES = Category H
   - Was the harm permanent? → YES = Category G
   - Was the harm temporary?
     - Did the error require initial or prolonged hospitalization? → YES = Category F; NO = Category E

---

MONITORING METHODOLOGY:
Preferred methods: Chart Review, Audit, and Self-Reporting (for manually documented charts). Software programmes can be used where prescriptions are generated online.
Formula: Total number of errors identified / Total number of opportunities × 100
(This is KPI #2 — see KPI Annexure 1 for formula details and sampling requirements.)

Important principles:
- Personnel identification is for ROOT CAUSE ANALYSIS and corrective/preventive action — NOT for punitive action.
- Sample population = running average of the previous 3 months of admissions.
- Files from ALL clinical specialities must be included; stratified sampling helps achieve this.
- Self-reported errors, errors found during audits, and errors found by any other methodology are ALL added to the numerator.

---

IMMEDIATE CORRECTION (before full root-cause analysis):
For Category A and B → Administer the drug within a reasonable timeframe.
For Category C and D → Consult the clinician and follow orders accordingly.

---

ROOT CAUSE ANALYSIS — 4 CAUSE GROUPS:

People: Casual attitude, inexperienced/new staff, untrained staff, shift-change/hurry, emotionally or physically unfit, wrong indent/receiving, patient identification error.

Environment: Pharmacy poor drug storage (ventilation/lighting/humidity), space constraints for storage, manpower constraints for dispensing.

Equipment: Defective syringe pumps, inappropriate syringe/diluent.

Process: "Ten rights" not observed, wrong stocking, wrong labelling, no cross-checking, stock-outs, unauthorized drug replacement, LASA (look-alike sound-alike) medicine error, wrong dispensing, wrong distribution, illegible handwriting.

Common corrective actions: Training, manpower recruitment, pharmacy stock rectification, equipment replacement/rectification.
`.trim();

// ── SHCO Quality Tools + Medication Chart Review Checklist ────────────────────
// Source: NABH SHCO 3rd Edition —
//   Medication Chart Review Checklist: Annexure 2 (pp.166–169)
//   Quality Tools: Annexure 3 (pp.170–172)
const QUALITY_TOOLS_CONTENT = `
SHCO FULL — MEDICATION CHART REVIEW CHECKLIST (Annexure 2, pp.166–169)

A structured audit form for reviewing medication charts. For each drug (up to 10 per sheet), the auditor marks each parameter with the error category (A–I), or 0 for no error, or NA if not applicable. Multiple errors can be recorded per cell.

Header fields: Auditor, Date of Audit, Location, UHID, Date of Admission, Primary Consultant, Drug allergies documented (Yes/No).

PARAMETERS — DOCTORS (1–13):
1. Incorrect drug selection
2. No/wrong dose
3. No/wrong unit of measurement
4. No/wrong frequency
5. No/wrong route
6. No/wrong concentration
7. No/wrong rate of administration
8. Illegible handwriting
9. Non-approved abbreviations used
10. Non-usage of capital letters for drug names
11. Non-usage of generic names
12. Non-modification of drug dose keeping in mind drug-drug interaction
13. Non-modification of time of drug administration/dose/drug keeping in mind food-drug interaction

PARAMETERS — DOCTOR AND/OR NURSE (14–16):
14. Wrong formulation transcribed/indented
15. Wrong drug transcribed/indented
16. Wrong strength transcribed/indented

PARAMETERS — PHARMACIST (17–23):
17. Wrong drug dispensed
18. Wrong dose dispensed
19. Wrong formulation dispensed
20. Expired/near-expiry drugs dispensed
21. No/wrong labelling
22. Delay in dispense beyond defined time
23. Generic or class substitute done without consulting the prescribing doctor

PARAMETERS — NURSES (24–35):
24. Wrong Patient
25. Dose Omission
26. Improper Dose
27. Wrong Drug
28. Wrong Formulation Administered
29. Wrong Route of Administration
30. Wrong Rate
31. Wrong Duration
32. Wrong Time (deviation from the organisation's defined timeframe; basis must be evidence-based — org may adopt/adapt ISMP Acute Care Guidelines)
33. No documentation of drug administration
34. Incomplete/Improper documentation by nursing staff (Incomplete = missing date, time, or signature; Improper = wrong dose notation or not stating actual brand in cases of brand substitution)
35. Documentation without administration

HOW TO COUNT ERRORS AND OPPORTUNITIES (for KPI #2 numerator/denominator):

Number of ERRORS = number of cells with a value between A and I.
Example: drug 1 has a category-C error (doctors) and a category-B error (pharmacists), and drug 4 has a category-C error (nurses) → numerator = 3.

Number of OPPORTUNITIES = number of cells with EITHER 0 OR a value A–I (i.e. all filled cells, excluding NA cells).
Example: 10 drugs × 35 parameters = 350 total cells = 350 opportunities (if all filled).
If 6 drugs and 24 cells marked NA → opportunities = (35 × 6) − 24 = 186.

SELECTING A CATEGORY: Choose only ONE category per error — the one that best fits. Select the HIGHEST severity level that applies during the event. Example: if a patient suffers a severe anaphylactic reaction (Category H) requiring treatment (Category F) but recovers fully, code it as Category H (highest severity reached).

---

SHCO FULL — QUALITY TOOLS (Annexure 3, pp.170–172)

QI data should be analysed using statistical/quality tools to assess compliance with targets and identify areas for improvement. NABH recognises the following six tools:

ROOT CAUSE ANALYSIS (RCA):
A systematic, extensive, in-depth analysis of a problem to get to its underlying cause. Used to establish causality when adverse trends are noted for any parameter, or in the case of errors/incidents. Carried out using either the 5 Whys tool or the Cause and Effect Diagram.

5 WHYS (Taiichi Ohno):
Asks "Why?" five times sequentially, each in response to the previous answer, until reaching the root cause. Shifts focus (blame) from individuals to the process. A problem may have multiple root causes; different people seeing different parts of the system may answer differently. The 5 Whys has been criticised for over-simplifying complex problems — best used in conjunction with a Cause and Effect Diagram.

CAUSE AND EFFECT DIAGRAM (Ishikawa / Fishbone):
Graphically displays the relationship of many causes to an effect and to each other. A horizontal line runs from tail to head of the "fish," where the effect is written. Causes are grouped under categories such as Materials, Methods, Equipment, Environment, and People (or as required). Used extensively to reach the root cause of deviations from any policy/procedure/protocol, for outliers in indicator data, and for detailed analysis of incidents and adverse events.

AFFINITY DIAGRAM:
Serves the same purpose as the Ishikawa chart, but the visual presentation differs.

HISTOGRAM:
A bar chart displaying variation in continuous data (time, weight, size, temperature). Helps recognise and analyse patterns not apparent in data tables or from averages/medians, and highlights the most frequently occurring interval.

FAILURE MODES AND EFFECTS ANALYSIS (FMEA):
A tool for systematic, PROACTIVE analysis of a process where harm may occur — preventing it by correcting processes proactively rather than reacting to adverse events after failures. FMEA prompts teams to review, evaluate, and record:
- Steps in the process
- Failure modes (what could go wrong?)
- Failure causes (why would the failure happen?)
- Failure effects (consequences — severity and frequency — of each failure)
- How the failure can be prevented
FMEA forms the core of risk assessment and risk mitigation.
`.trim();

// ── Detection helpers ──────────────────────────────────────────────────────────

// Patterns that detect SPECIFIC KPI questions (formula, rate, calculation, PSQ.2x standard).
// Must run BEFORE the general-info check so these don't fall into the generic "what is a KPI"
// branch — they need the full KPI annexure content, not just the KPI definition.
const KPI_SPECIFIC_PATTERNS: RegExp[] = [
  // PSQ KPI standard codes (PSQ.2a / PSQ.2b / PSQ.2c / PSQ.2d — without a trailing dot)
  /\bPSQ[.\-\s]?2\s*[abcd]\b/i,
  // Sample size / sampling methodology
  /\bsample\s+size\b/i,
  /\bsolvin'?s?\b/i,
  /\bstratified\s+random\b/i,
  // Formula / calculation intent
  /\bformula\s+(for|of|to)\b/i,
  /\bhow\s+(do\s+I|to)\s+(calculate|compute|measure|work\s+out)\b/i,
  // Specific KPI indicator names (rate / formula context)
  /\bmedication\s+error\s+rate\b/i,
  /\bincidence\s+of\s+medication\s+error\b/i,
  /\btransfusion\s+reaction\s+rate\b/i,
  /\bpressure\s+ulcer\s+(rate|incidence|kpi)\b/i,
  /\bcauti\b/i,
  /\bcatheter.{0,20}uti\b/i,
  /\bcatheter.{0,20}urinary\s+tract\s+infection\s+rate\b/i,
  /\bvap\s+rate\b/i,
  /\bventilator.{0,20}pneumonia\s+rate\b/i,
  /\bclabsi\b/i,
  /\bcentral\s+line.{0,20}(blood\s*stream|bsi)\s+infection\s+rate\b/i,
  /\bssi\s+rate\b/i,
  /\bsurgical\s+site\s+infection\s+rate\b/i,
  /\bhand\s+hygiene\s+(compliance|rate|kpi)\b/i,
  /\bantibiotic\s+prophylaxis\s+(compliance|rate|kpi)\b/i,
  /\bpatient\s+falls?\s+rate\b/i,
  /\bneedlestick\s+injur(y|ies)\s+rate\b/i,
  /\bwaiting\s+time\s+(for\s+)?diagnostics?\b/i,
  /\btime\s+(taken\s+)?for\s+discharge\b/i,
  /\b(standardis[e]?d|standardized)\s+mortality\s+ratio\b/i,
  /\bsmr.{0,10}icu\b/i,
  /\binitial\s+assessment\s+(time|kpi)\b/i,
  // "list / what are the / all KPIs" (enumerate request)
  /\b(list|show|what\s+are)\s+(all\s+)?(the\s+)?(shco\s+|nabh\s+)?kpis?\b/i,
  /\bhow\s+many\s+kpis\s+(are\s+there|does\s+shco|in\s+shco)\b/i,
];

function isKpiSpecificQuestion(q: string): boolean {
  return KPI_SPECIFIC_PATTERNS.some((p) => p.test(q));
}

// Patterns that detect medication error CATEGORIZATION questions (Annexure 2).
// Kept distinct from KPI #2 (medication error RATE/formula) which stays in KPI content.
// These fire on: harm categories, NCC-MERP, root cause, LASA, classification algorithm.
const MED_ERROR_PATTERNS: RegExp[] = [
  /\bncc.?merp\b/i,
  /\bcategory\s+[a-i]\b/i,                                        // "category A", "category D", etc.
  /\bharm\s+(level|categor)/i,
  /\b(categorize|categorise|classify|classification)\s+(a\s+)?(medication\s+|drug\s+)?error\b/i,
  /\bhow\s+(do\s+I|to)\s+(categorize|categorise|classify)\b/i,
  /\blasa\b/i,
  /\blook.?alike\s+sound.?alike\b/i,
  /\berror\s+of\s+omission\b/i,
  /\broot\s+cause.{0,40}(medication|drug|error)\b/i,
  /\b(medication|drug).{0,40}root\s+cause\b/i,
  /\bmedication\s+error.{0,30}(monitor|audit|report|analys|categor|classif|harm)\b/i,
  /\b(monitor|audit|report|analys).{0,30}medication\s+error\b/i,
  /\b(temporary|permanent)\s+harm\b/i,
  /\b(what|which)\s+(are|is)\s+(the\s+)?(harm\s+)?(levels?|categories)\s+(of\s+)?(medication\s+)?error\b/i,
  /\bdifference\s+between\s+categor(y|ies)\b/i,
  /\bno\s+harm.{0,20}error\b/i,
  /\berror.{0,20}no\s+harm\b/i,
  /\bmedication\s+error\s+categor/i,
];

function isMedicationErrorQuestion(q: string): boolean {
  return MED_ERROR_PATTERNS.some((p) => p.test(q));
}

// Patterns that detect quality-tools questions (Annexure 3) and medication chart
// review checklist questions (Annexure 2, pp.166–169).
// Runs at Step 0c — after KPI (Step 0) and med-error categorization (Step 0b).
// "RCA" and "root cause" (generic, without medication/drug/error context) fall here,
// since MED_ERROR only catches root-cause questions paired with medication context.
const QUALITY_TOOLS_PATTERNS: RegExp[] = [
  // Quality improvement tools (Annexure 3)
  /\bfmea\b/i,
  /\bfailure\s+mode(s)?\b/i,
  /\b5\s*whys?\b/i,
  /\bfishbone\b/i,
  /\bishikawa\b/i,
  /\bcause\s+and\s+effect\s+diagram\b/i,
  /\baffinity\s+diagram\b/i,
  /\bquality\s+tool(s)?\b/i,
  /\bqi\s+tool(s)?\b/i,
  /\bquality\s+improvement\s+tool(s)?\b/i,
  /\bproactive\s+(analysis|risk)\b/i,
  // RCA as a standalone concept (not paired with medication — that's MED_ERROR)
  /\broot\s+cause\s+analysis\b/i,
  /\b\brca\b(?!.{0,30}(medication|drug|error))/i,
  // Histogram as a QI/data tool
  /\bhistogram\b/i,
  // Medication chart review checklist (Annexure 2, pp.166-169)
  /\bchart\s+review\b/i,
  /\bmedication\s+(audit\s+form|chart\s+audit|chart\s+review)\b/i,
  /\b(how\s+to\s+count|counting)\s+(errors?|opportunit)/i,
  /\bcount.{0,20}opportunit.{0,20}(chart|audit|medication|drug)\b/i,
  /\bopportunities.{0,30}(chart|audit|medication|formula|kpi)\b/i,
  /\bparameter(s)?.{0,20}(nurse|doctor|pharmacist|audit|checklist)\b/i,
  /\b(nurse|doctor|pharmacist).{0,20}parameter(s)?\b/i,
  /\baudit\s+(form|parameters?|checklist)\b/i,
  /\b35\s*parameter(s)?\b/i,
];

function isQualityToolsQuestion(q: string): boolean {
  return QUALITY_TOOLS_PATTERNS.some((p) => p.test(q));
}

// Patterns that indicate a general-info question (assessment process, scoring, chapters, KPIs)
const GENERAL_INFO_PATTERNS: RegExp[] = [
  /\bfinal\s+assessment\b/i,
  /\bsurveillance\s+assessment\b/i,
  /\bre.?accreditation\b/i,
  /\brenewal\s+assessment\b/i,
  /\baccreditation\s+(cycle|process|criteria|decision|period|validity|award)\b/i,
  /\bhow\s+(long|many years)\s+is\s+(nabh\s+)?accreditation\b/i,
  /\b4.year\s+(validity|cycle|accreditation)\b/i,
  /\bkpi\b/i,
  /\bkey\s+performance\s+indicator\b/i,
  /\b(what|how)\s+(is|are|does)\s+(the\s+)?scoring\b/i,
  /\bhow\s+(is|are)\s+oe(s)?\s+scored\b/i,
  /\b5.point\s+scale\b/i,
  /\bfive.point\s+scale\b/i,
  /\bwhat\s+(is|does)\s+(a\s+)?(core|commitment|achievement|excellence)\b/i,
  /\b(core|commitment|achievement|excellence)\s+(level|oe|standard|category|objective)\b/i,
  /\blevels?\s+of\s+(oe|objective\s+elements?|standards?)\b/i,
  /\bwhat\s+is\s+(a\s+)?standard\b/i,
  /\bwhat\s+is\s+(an?\s+)?(oe|objective\s+element)\b/i,
  /\bwhat\s+is\s+nabh\b/i,
  /\babout\s+nabh\b/i,
  /\bnabh\s+accreditation\s+(programme|program|process)\b/i,
  /\bhow\s+many\s+chapters\b/i,
  /\bchapter\s+(list|structure|overview|code)\b/i,
  /\blist\s+(of\s+)?(all\s+)?chapters\b/i,
  /\bhow\s+many\s+(total\s+)?oe(s)?\b/i,
  /\btotal\s+(number\s+of\s+)?oe(s)?\b/i,
  /\b408\s+oe\b/i,
  /\baccreditation\s+decision\b/i,
  /\b80\s*(percent|%)\s+(compliance|score)\b/i,
  /\bwhat\s+score\s+do\s+i\s+need\b/i,
  /\bpass\s+(criteria|score|marks)\b/i,
];

function isGeneralInfoQuestion(q: string): boolean {
  return GENERAL_INFO_PATTERNS.some((p) => p.test(q));
}

// Chapter intent / summary questions — book-only content in shco_kb
const CHAPTER_CODES = ["AAC", "COP", "MOM", "PRE", "HIC", "PSQ", "ROM", "FMS", "HRM", "IMS"] as const;
const CHAPTER_INTENT_PATTERNS: RegExp[] = [
  /\bintent\s+of\s+(the\s+)?(aac|cop|mom|pre|hic|psq|rom|fms|hrm|ims)\b/i,
  /\b(aac|cop|mom|pre|hic|psq|rom|fms|hrm|ims)\s+chapter\s+intent\b/i,
  /\bwhat\s+is\s+(the\s+)?(aac|cop|mom|pre|hic|psq|rom|fms|hrm|ims)\s+chapter\s+about\b/i,
  /\bsummary\s+of\s+standards\s+(for\s+)?(aac|cop|mom|pre|hic|psq|rom|fms|hrm|ims)\b/i,
  /\b(aac|cop|mom|pre|hic|psq|rom|fms|hrm|ims)\s+standards\s+summary\b/i,
  /\bwhat\s+does\s+(the\s+)?(aac|cop|mom|pre|hic|psq|rom|fms|hrm|ims)\s+chapter\s+cover\b/i,
];

function getChapterIntentMatch(q: string): string | null {
  for (const p of CHAPTER_INTENT_PATTERNS) {
    const m = q.match(p);
    if (m) {
      const code = (m[2] ?? m[1]).toUpperCase();
      if (CHAPTER_CODES.includes(code as typeof CHAPTER_CODES[number])) return code;
    }
  }
  // Bare chapter code + "intent" or "about"
  const bare = q.match(
    /\b(aac|cop|mom|pre|hic|psq|rom|fms|hrm|ims)\b.*\b(intent|about|covers?|summary)\b/i,
  );
  if (bare) return bare[1].toUpperCase();
  return null;
}

// Returns the best-matching glossary entry for definitional questions, or null
function getGlossaryMatch(q: string): { term: string; definition: string } | null {
  const lower = q.toLowerCase().replace(/[?!.]+$/, "").trim();

  // Extract candidate from common definitional question patterns
  let candidate = "";
  const defPatterns = [
    /^what\s+(?:is|are)\s+(?:a\s+|an\s+|the\s+)?(.+)$/,
    /^what\s+does\s+(.+?)\s+mean$/,
    /^define\s+(?:the\s+term\s+)?(.+)$/,
    /^(?:meaning|definition)\s+of\s+(.+)$/,
    /^explain\s+(?:the\s+term\s+)?(.+)$/,
    /^(.+?)\s+(?:meaning|definition|defined)$/,
  ];
  for (const p of defPatterns) {
    const m = lower.match(p);
    if (m) { candidate = m[1].trim(); break; }
  }

  if (!candidate) return null;

  // Exact key match
  if (GLOSSARY[candidate]) return { term: candidate, definition: GLOSSARY[candidate] };

  // Candidate starts with a key (e.g. "adverse drug reaction in nabh" → "adverse drug reaction")
  for (const key of Object.keys(GLOSSARY)) {
    if (candidate.startsWith(key)) return { term: key, definition: GLOSSARY[key] };
  }

  // Key starts with candidate (e.g. "sedation levels" → "sedation")
  for (const key of Object.keys(GLOSSARY)) {
    if (key.startsWith(candidate) && Math.abs(key.length - candidate.length) < 15) {
      return { term: key, definition: GLOSSARY[key] };
    }
  }

  // Candidate contains a key as a distinct phrase (longest match first)
  const sortedKeys = Object.keys(GLOSSARY).sort((a, b) => b.length - a.length);
  for (const key of sortedKeys) {
    if (key.length >= 5 && candidate.includes(key)) {
      return { term: key, definition: GLOSSARY[key] };
    }
  }

  return null;
}

// ── Main handler ───────────────────────────────────────────────────────────────

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: CORS });
  }

  const _step = { current: "parse" };

  try {
    const { question } = await req.json();
    if (!question || typeof question !== "string") {
      return Response.json({ error: "Missing question" }, { status: 400, headers: CORS });
    }

    _step.current = "env-check";
    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
    const anthropicKey = Deno.env.get("ANTHROPIC_API_KEY");
    if (!supabaseUrl) throw new Error("SUPABASE_URL missing");
    if (!serviceKey) throw new Error("SUPABASE_SERVICE_ROLE_KEY missing");
    if (!anthropicKey) throw new Error("ANTHROPIC_API_KEY missing");

    _step.current = "supabase-init";
    const supabase = createClient(supabaseUrl, serviceKey);

    let rows: Record<string, unknown>[] | null = null;
    let isKeywordFallback = false;
    let mergedHits: { kind: "oe" | "kb"; rank: number; row: Record<string, unknown> }[] = [];
    let isGeneralRef = false;
    let isKpiRef = false;
    let isMedErrorRef = false;
    let isQualityToolsRef = false;
    let generalRefContext = "";
    let generalRefSourceLabel = "";

    // Step 0: KPI-specific detection — runs before OE extraction so that
    // "what is PSQ.2a" routes to KPI content rather than the OE lookup.
    _step.current = "kpi-check";
    if (isKpiSpecificQuestion(question)) {
      isGeneralRef = true;
      isKpiRef = true;
      generalRefContext = SHCO_KPI_CONTENT;
      generalRefSourceLabel = "SHCO Full — KPI Annexure 1 (NABH 3rd Edition Standards Book, pp.151–159)";
    }

    // Step 0b: Medication error categorization detection — runs before OE extraction.
    // Categorization/harm-level questions → Annexure 2 content.
    // Formula/rate questions are already caught by Step 0 (KPI) and never reach here.
    _step.current = "med-error-check";
    if (!isGeneralRef && isMedicationErrorQuestion(question)) {
      isGeneralRef = true;
      isMedErrorRef = true;
      generalRefContext = MEDICATION_ERROR_CONTENT;
      generalRefSourceLabel = "SHCO Full — Medication Error Monitoring (Annexure 2, NCC-MERP)";
    }

    // Step 0c: Quality tools + chart review checklist detection.
    // Fires only if KPI (Step 0) and med-error categorization (Step 0b) didn't match.
    // Generic "RCA" / "root cause analysis" lands here; RCA-with-medication-context
    // was already caught at Step 0b.
    _step.current = "quality-tools-check";
    if (!isGeneralRef && isQualityToolsQuestion(question)) {
      isGeneralRef = true;
      isQualityToolsRef = true;
      generalRefContext = QUALITY_TOOLS_CONTENT;
      // Source label used as fallback; system prompt rule 1c refines it per answer type.
      generalRefSourceLabel = "SHCO Full — Quality Tools (Annexure 3) / Medication Chart Review Checklist (Annexure 2, pp.166–169)";
    }

    // Step 1: try OE code match — scan anywhere in the question for a code pattern
    // DB format: CHAPTER.NUMBER.letter  e.g. "AAC.1.a", "PRE.2.g"
    // Handles bare codes AND natural-language wrappers:
    //   "what is MOM.3.g", "tell me about MOM 3 G", "comply with MOM-3-g" → "MOM.3.g"
    _step.current = "db-oe_code-search";
    const extractOeCode = (q: string): string | null => {
      // Scan the raw question for a code pattern anywhere in the text
      // Pattern: 2-4 letters, optional separator, 1-2 digits, optional separator, 1 letter
      const scan = q.match(/\b([A-Za-z]{2,4})[.\-\s]?(\d{1,2})[.\-\s]?([A-Za-z])\b/i);
      if (scan) {
        return `${scan[1].toUpperCase()}.${scan[2]}.${scan[3].toLowerCase()}`;
      }
      return null;
    };
    // Skip OE DB lookup entirely if a reference source already matched
    const oeCodeQuery = !isGeneralRef ? extractOeCode(question) : null;
    let codeRows = null;
    if (oeCodeQuery) {
      const { data, error: codeErr } = await supabase
        .from("shco_full_oes")
        .select("oe_code, chapter, standard_code, level, text, achieve_tips, doc_required, interpretation, assessment_stages")
        .ilike("oe_code", `%${oeCodeQuery}%`)
        .limit(12);
      if (codeErr) throw new Error(`DB oe_code search: ${codeErr.message}`);
      codeRows = data;
    }

    if (!isGeneralRef) {
      rows = codeRows && codeRows.length > 0 ? codeRows : null;
    }

    // Step 2: if no OE code match, check glossary
    if (!rows && !isGeneralRef) {
      _step.current = "glossary-check";
      const glossaryMatch = getGlossaryMatch(question);
      if (glossaryMatch) {
        isGeneralRef = true;
        generalRefContext = `TERM: ${glossaryMatch.term}\nDEFINITION: ${glossaryMatch.definition}`;
        generalRefSourceLabel = "SHCO Full — Official Glossary (NABH 3rd Edition Standards Book, pp.138–150)";
      }
    }

    // Step 3: chapter intent / summary from shco_kb (book-only)
    if (!rows && !isGeneralRef) {
      const chapterCode = getChapterIntentMatch(question);
      if (chapterCode) {
        _step.current = "chapter-intent-kb";
        const { data: kbRows, error: kbErr } = await supabase
          .from("shco_kb")
          .select("title, content, source_label, category, section")
          .eq("section", chapterCode)
          .in("category", ["chapter_intent", "chapter_summary"])
          .order("category");
        if (kbErr) throw new Error(`DB chapter KB: ${kbErr.message}`);
        if (kbRows && kbRows.length > 0) {
          isGeneralRef = true;
          generalRefContext = kbRows
            .map((r) => `${r.title}\n${r.content}`)
            .join("\n\n");
          generalRefSourceLabel = kbRows.map((r) => r.source_label).join(" / ");
        }
      }
    }

    // Step 4: if no glossary match, check general info topics
    if (!rows && !isGeneralRef && isGeneralInfoQuestion(question)) {
      _step.current = "general-info-check";
      isGeneralRef = true;
      generalRefContext = GENERAL_INFO;
      generalRefSourceLabel = "SHCO Full — General Reference (NABH 3rd Edition Standards Book)";
    }

    // Step 5: if no curated reference matched, fall back to ranked full-text search.
    // Search BOTH the OE table (search_shco_full_oes) and the curated KB (search_shco_kb)
    // in parallel, then merge the hits by ts_rank so the most relevant rows across both
    // sources feed the answer model. (Replaces the old unranked ILIKE-OR; both RPCs use
    // websearch_to_tsquery converted to OR + ts_rank and expose a numeric `rank`.)
    if (!rows && !isGeneralRef) {
      _step.current = "db-fts-search";
      const [oeRes, kbRes] = await Promise.all([
        supabase.rpc("search_shco_full_oes", { q: question, match_count: 8 }),
        supabase.rpc("search_shco_kb", { q: question, match_count: 8 }),
      ]);
      if (oeRes.error) throw new Error(`DB FTS search (oes): ${oeRes.error.message}`);
      if (kbRes.error) throw new Error(`DB FTS search (kb): ${kbRes.error.message}`);

      const tag = (kind: "oe" | "kb") => (r: Record<string, unknown>) => ({
        kind,
        rank: typeof r.rank === "number" ? r.rank : 0,
        row: r,
      });
      mergedHits = [
        ...((oeRes.data ?? []) as Record<string, unknown>[]).map(tag("oe")),
        ...((kbRes.data ?? []) as Record<string, unknown>[]).map(tag("kb")),
      ]
        .sort((a, b) => b.rank - a.rank)
        .slice(0, 10);

      if (mergedHits.length > 0) {
        rows = mergedHits.map((h) => h.row);
        isKeywordFallback = true;
      } else {
        rows = [];
      }
    }

    _step.current = "build-context";
    const renderOe = (r: Record<string, unknown>) => {
      const tips =
        Array.isArray(r.achieve_tips) && r.achieve_tips.length > 0
          ? r.achieve_tips.join(" | ")
          : "—";
      const docFlag =
        r.doc_required === true
          ? "Mandatory system documentation (*)"
          : r.doc_required === false
            ? "No mandatory doc flag in book"
            : "—";
      const interp =
        typeof r.interpretation === "string" && r.interpretation.trim()
          ? r.interpretation.trim()
          : "—";
      const stages =
        typeof r.assessment_stages === "string" && r.assessment_stages.trim()
          ? r.assessment_stages.trim()
          : "—";
      return (
        `${r.oe_code} | ${r.level} | Assessed at: ${stages}` +
        ` | OE: ${r.text} | Doc flag: ${docFlag}` +
        ` | Official interpretation: ${interp}` +
        ` | Achieve tips: ${tips}`
      );
    };
    const renderKb = (r: Record<string, unknown>) =>
      `${r.title} [${r.source_label}] | ${r.content}`;

    const contextBlock = isGeneralRef
      ? generalRefContext
      : mergedHits.length > 0
        ? mergedHits
            .map((h) => (h.kind === "oe" ? renderOe(h.row) : renderKb(h.row)))
            .join("\n")
        : rows && rows.length > 0
          ? rows.map(renderOe).join("\n") // Step-1 direct oe_code match (all OE rows)
          : "";

    // System prompt — two variants depending on context type
    const systemPrompt = isGeneralRef
      ? `You are AccredReady's NABH SHCO Full compliance assistant. You answer ONLY` +
        ` using the reference content provided below in <context>, which is sourced` +
        ` from the official NABH SHCO 3rd Edition Standards Book (August 2022).` +
        ` You have no other knowledge of NABH standards or accreditation requirements` +
        ` — anything not in the provided context is outside what you know.\n\n` +
        `Rules:\n` +
        `1. Answer clearly and completely from the <context> provided.\n` +
        (isKpiRef
          ? `1a. For KPI questions, ALWAYS include the exact formula (numerator / denominator × multiplier)` +
            ` and the unit in your answer — hospital staff need these to implement tracking. If multiple` +
            ` KPIs are relevant, list each one with its formula and unit. Also mention sampling requirements` +
            ` (YES/NO) and any SPECIAL NOTEs from <context>.\n`
          : ``) +
        (isMedErrorRef
          ? `1b. For medication error categorization questions, ALWAYS include the specific category` +
            ` letter(s) (A through I) and the harm level (No Error / Error No Harm / Error Harm /` +
            ` Error Death) in your answer. Walk through the classification algorithm when it helps` +
            ` the user understand which category applies.\n`
          : ``) +
        (isQualityToolsRef
          ? `1c. For quality tools questions: if answering about RCA, 5 Whys, Fishbone/Ishikawa,` +
            ` Affinity Diagram, Histogram, or FMEA, or the medication chart review checklist,` +
            ` include the relevant detail from <context>.\n`
          : ``) +
        `2. If the <context> does not address the question, say: 'I couldn't find` +
        ` a matching SHCO Full reference for that — try rephrasing, or check with` +
        ` your AccredReady admin.' Do NOT guess or use general NABH knowledge.\n` +
        `3. Keep answers practical and easy to understand for hospital staff.\n` +
        `4. Always end your answer with exactly: SHCO 3rd edition\n` +
        `5. Do NOT speculate about anything not explicitly in <context>.\n\n` +
        `<context>\n${contextBlock}\n</context>`
      : `You are AccredReady's NABH SHCO Full compliance assistant. You answer ONLY` +
        ` using the SHCO Full reference content provided below in <context> — a mix of` +
        ` Objective Elements (OEs) and curated reference entries. You have no other` +
        ` knowledge of NABH standards, KPIs, or accreditation requirements — anything` +
        ` not in the provided context is outside what you know.\n\n` +
        `Rules:\n` +
        `1. If the answer is fully contained in <context>, answer clearly and cite the` +
        ` exact oe_code(s) for OE lines, or the bracketed [source label] for curated` +
        ` reference lines, that you used.\n` +
        `2. If <context> is empty or doesn't address the question, say: 'I couldn't` +
        ` find a matching SHCO Full requirement for that — try rephrasing, or check` +
        ` with your AccredReady admin.' Do NOT guess or use general NABH knowledge.\n` +
        `3. Never state OE counts, chapter totals, fees, or validity periods unless` +
        ` they appear verbatim in <context>.\n` +
        `4. Keep answers practical and specific — hospital staff need to know what to` +
        ` DO, not just what the rule says.\n` +
        `5. Achieve tips in <context> are optional practical guidance — use them when` +
        ` helpful but do not add any disclaimer or separate source line about them.\n` +
        `6. "Official interpretation" comes only from the NABH book. If it shows "—",` +
        ` do NOT invent an interpretation — answer from the OE text and doc flag only.\n` +
        `6a. More broadly: if <context> discusses the general topic (e.g. a committee,` +
        ` a process, a policy) but does NOT explicitly state a specific detail you were` +
        ` asked for — meeting frequency, membership/composition, chairperson, quorum,` +
        ` timelines, or any other number or named requirement — you MUST split your` +
        ` answer: first state clearly what <context> DOES say, citing the source, then` +
        ` say exactly: "The SHCO reference content available to me does not specify` +
        ` [the missing detail]. NABH generally expects the hospital to define this in` +
        ` its own committee terms of reference / policy document." Do NOT fill the gap` +
        ` with general NABH knowledge, typical industry practice, or a plausible-sounding` +
        ` specific — a confident wrong answer about frequency or membership is worse` +
        ` than admitting the gap, since hospitals act on what you tell them.\n` +
        `7. If Doc flag is "Mandatory system documentation (*)", tell the user the` +
        ` book requires written system documentation for this OE.\n` +
        `8. Always end your answer with exactly: SHCO 3rd edition\n` +
        `9. When you cannot find a match, state ONLY that no matching SHCO Full` +
        ` requirement was found, and suggest the user rephrase or check with their` +
        ` AccredReady admin. Do NOT speculate about which chapter, standard, or OE` +
        ` might contain the answer, do NOT guess chapter names or codes, and do NOT` +
        ` describe NABH structure beyond what is explicitly in <context>. If <context>` +
        ` is empty, your entire response must be limited to the refusal sentence —` +
        ` nothing else.\n` +
        `(Rules 6–9 above supersede any earlier numbering in this prompt block.)\n\n` +
        `<context>\n${contextBlock}\n</context>`;

    _step.current = "anthropic-fetch";
    const anthropicRes = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": anthropicKey.trim(),
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({
        model: "claude-sonnet-4-6",
        max_tokens: 700,
        system: systemPrompt,
        messages: [{ role: "user", content: question }],
      }),
    });

    _step.current = "anthropic-parse";
    if (!anthropicRes.ok) {
      const body = await anthropicRes.text();
      throw new Error(`Anthropic API error: ${anthropicRes.status} — ${body}`);
    }

    const anthropicData = await anthropicRes.json();
    const answer = anthropicData.content?.[0]?.text ?? "";

    // Sources: OE codes only for direct OE matches; empty for general ref or keyword fallback
    const sources =
      !isGeneralRef && !isKeywordFallback && rows && rows.length > 0
        ? rows.map((r) => r.oe_code)
        : [];

    // Suggestions: fixed example questions when no real OE match
    const suggestions =
      !isGeneralRef && (isKeywordFallback || (rows && rows.length === 0))
        ? [
            "What must we do for hand hygiene?",
            "What must we do for biomedical waste segregation?",
            "What must we do for fire safety and emergency preparedness?",
            "What does the infection control committee do?",
          ]
        : [];

    return Response.json({ answer, sources, suggestions }, { headers: CORS });
  } catch (err) {
    console.error(`[${_step.current}]`, err);
    return Response.json(
      { error: "Something went wrong. Please try again." },
      { status: 500, headers: CORS },
    );
  }
});
