# -*- coding: utf-8 -*-
"""Builds the HIC.1 master policy draft: JSON for review + SQL for the Supabase SQL Editor."""
import json
import re

STANDARD_CODE = "HIC.1"
CHAPTER = "HIC"
OE_CODES = ["HIC.1.a", "HIC.1.b", "HIC.1.c", "HIC.1.d", "HIC.1.e", "HIC.1.f"]

# Column types, verified against the live schema where noted.
#   oe_codes   -> text[]  (confirmed 2026-08-03 via information_schema: ARRAY / _text)
#   oe_mapping -> jsonb   (confirmed via 20260803_shco_policy_masters_oe_mapping.sql)
#   procedure_steps -> UNVERIFIED. Flip this to False if information_schema reports
#   ARRAY / _text for it, and re-run; the emitted SQL switches to an array literal.
PROCEDURE_STEPS_IS_JSONB = False

POLICY_TITLE = "Hospital Infection Prevention and Control Programme"

PURPOSE = """This document establishes the infection prevention and control programme of {{HOSPITAL_NAME}} and sets out how that programme is owned, organised, resourced, implemented and reviewed. Its aim is to reduce the risk of healthcare associated infection to patients, staff, visitors, contract personnel and the surrounding community to the lowest level reasonably achievable, and to give everyone working at {{HOSPITAL_NAME}} one place to find who is accountable for infection control, what the programme covers, and how its performance is judged. This is the parent document of the infection control manual: it defines the programme, while the clinical practices themselves are set out in the individual policies that sit beneath it."""

SCOPE = """This policy applies across the whole of {{HOSPITAL_NAME}} without exception, including inpatient wards, critical and high-dependency areas, operating and procedure rooms, emergency and outpatient departments, laboratory and imaging services, pharmacy, and every support area — kitchen, laundry, stores, engineering and waste handling — whether run by {{HOSPITAL_NAME}} directly or by a contractor.

It binds every category of person present in {{HOSPITAL_NAME}}: employed clinical and non-clinical staff, visiting and consultant practitioners, nursing and allied trainees, outsourced and contract personnel, volunteers, patients and their attendants.

What this policy covers is the programme itself — its governance, its documentation, its resourcing, its assessment, and its community-facing obligations. What it does not cover is the detail of clinical practice: standard and transmission-based precautions, hand hygiene technique, safe injection practice and antimicrobial use are set out in the infection prevention and control practices policy; environmental cleaning, sterilisation and instrument reprocessing, linen handling and biomedical waste are set out in their own policies within the infection control manual. This policy states that those policies must exist, must be current and must be followed; it does not restate their content."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} treats infection prevention and control as a core clinical safety obligation of the organisation rather than as a set of tasks delegated to a single department. Infection risk is created by decisions taken throughout the hospital — in purchasing, staffing, construction, housekeeping and clinical practice alike — and so responsibility for controlling it is shared across all of them.

The management of {{HOSPITAL_NAME}} commits to maintaining a written, funded and continuously operating infection prevention and control programme, to appointing a multidisciplinary committee and a working team to run it, and to providing the people, equipment, consumables and physical facilities the programme needs to function. Resource decisions affecting infection control are taken as patient-safety decisions, not solely as cost decisions.

{{HOSPITAL_NAME}} accepts that a programme is only real if it is measured. The programme is assessed at defined intervals against an established infection control assessment tool, the results are recorded, the gaps are acted upon, and the trend across assessment cycles is the primary evidence that the programme works.

{{HOSPITAL_NAME}} further recognises that infection does not stop at its boundary wall. The hospital therefore educates patients, attendants and the wider community on infection prevention, notifies communicable disease to the public health authorities as required by law, and makes its staff and facilities available to the district health administration during outbreaks and pandemics.

Reporting an infection control problem, a breach or a near miss is expected of every member of staff and is treated as a contribution to safety. {{HOSPITAL_NAME}} does not take disciplinary action against a person for reporting in good faith; it reserves such action for wilful or repeated disregard of a known precaution."""

PROCEDURE_STEPS = [
"""1. How the infection prevention and control programme is structured

The infection prevention and control programme of {{HOSPITAL_NAME}} is built on three layers, each with a distinct job. Confusing them is the most common reason a programme looks complete on paper but fails in practice.

- The Infection Prevention and Control Committee (IPCC) is the governing body. It sets policy, approves the annual programme, reviews performance and escalates resource needs to management. It meets periodically; it does not run the programme day to day.
- The Infection Control Team (ICT) is the working arm. It carries out surveillance, training, audit and outbreak investigation on a daily basis and reports to the IPCC.
- Every head of department is the owner of infection control practice within their own area. The ICT advises and audits; it does not relieve a department head of responsibility for what happens in that department.

The programme covers, at minimum: standard and transmission-based precautions; hand hygiene; safe injection and sharps practice; cleaning, disinfection and sterilisation; environmental hygiene; linen and laundry; biomedical waste; surveillance of healthcare associated infection; antimicrobial stewardship; staff health and post-exposure management; isolation facilities; and education of staff, patients and the community.""",

"""2. The Infection Prevention and Control Committee (IPCC)

{{HOSPITAL_NAME}} constitutes a multidisciplinary Infection Prevention and Control Committee. Multidisciplinary is a requirement, not a preference: a committee drawn only from nursing or only from administration cannot see the whole infection risk of the hospital.

The committee draws its members from across the disciplines whose work creates or controls infection risk, which for {{HOSPITAL_NAME}} means representation from:

- medical and surgical clinical services;
- nursing;
- microbiology or laboratory services;
- pharmacy;
- housekeeping and environmental services;
- central sterile supply and operating theatre services;
- engineering and maintenance;
- hospital administration or management.

The committee is chaired by [Hospital to define] and its member list, by name and designation, is recorded in the committee's terms of reference and revised whenever a member changes. The committee meets at a frequency defined by {{HOSPITAL_NAME}} of [Hospital to define], and the quorum for a valid meeting is [Hospital to define].

Every meeting has a circulated agenda, a signed attendance record, and minutes that record decisions, the person made responsible for each action and the date by which it is due. Minutes of the previous meeting are tabled at the next one so that open actions are visibly carried forward rather than lost. Minutes are filed chronologically and retained as set out in step 28.""",

"""3. The Infection Control Team (ICT)

Alongside the committee, {{HOSPITAL_NAME}} maintains an Infection Control Team that performs the programme's daily work. The team is led by an Infection Control Officer, who is a medically qualified person — a microbiologist or a physician with infection control training — and includes at least one Infection Control Nurse with dedicated, protected time for the role.

The infection control nurse role is not an additional duty performed in the gaps of a full clinical roster. {{HOSPITAL_NAME}} defines the time committed to it as [Hospital to define] and protects that time, because surveillance and audit that are only performed when the ward is quiet are not performed at all.

The team's standing responsibilities are:

- daily rounds of clinical areas to observe practice and identify breaches at the point they occur;
- collection and collation of surveillance data;
- investigation of suspected outbreaks and of any cluster of infection;
- delivery and recording of staff training;
- audit of compliance with infection control policies, and feedback of the results to the area audited;
- advice to clinical teams on isolation decisions and patient placement;
- preparation of the data and analysis the IPCC needs for its meetings.

The names and contact details of the current team members are displayed in every clinical area of {{HOSPITAL_NAME}} so that any member of staff can reach them without going through a supervisor.""",

"""4. The infection control manual and what it must contain

{{HOSPITAL_NAME}} maintains a written infection control manual. The manual is the collected set of policies that govern infection prevention across the hospital, with this policy as its opening document.

The manual contains, at minimum:

- this programme policy, including the committee and team structure;
- standard precautions and transmission-based precautions;
- hand hygiene;
- personal protective equipment — selection, donning and removal;
- safe injection, infusion and sharps practice;
- cleaning and disinfection of the environment, with the cleaning schedule by area;
- decontamination, disinfection and sterilisation of instruments and equipment;
- linen and laundry handling;
- biomedical waste segregation, storage, transport and disposal;
- isolation and barrier nursing;
- surveillance of healthcare associated infection;
- antimicrobial stewardship;
- occupational health, immunisation of staff, and management of needlestick and other exposures;
- management of blood and body fluid spills;
- infection control requirements during construction and renovation;
- outbreak identification, investigation and response.

A single controlled master copy is held by the Infection Control Team. Each clinical area holds a copy — printed or electronic — that staff can reach at the point of care without asking permission. Where the manual is held electronically, {{HOSPITAL_NAME}} ensures it remains readable when the network or a device is unavailable.""",

"""5. Keeping the manual current

Each document in the manual carries a version number, an approval date and a scheduled review date on its face, so that anyone reading it can tell whether it is current.

The whole manual is reviewed at least once every [Hospital to define], and any individual policy is reviewed sooner when one of the following occurs:

- a national guideline, statutory rule or NABH requirement bearing on it changes;
- an outbreak, incident or adverse event exposes a gap in it;
- an audit or assessment finds it is not being followed because it is impractical as written;
- a service, procedure or piece of equipment is introduced that it does not cover.

Revisions are approved by the IPCC before they take effect. When a document is revised, the superseded version is withdrawn from every point of use and one dated copy is retained by the Infection Control Team as a record — an obsolete policy left in a ward folder is a source of error, not a record. Each policy carries an amendment history showing what changed, why, and on whose approval.""",

"""6. Annual infection risk assessment

Before the programme for a year is written, the Infection Control Team carries out a documented assessment of the infection risks specific to {{HOSPITAL_NAME}}. A programme not grounded in the hospital's own risks tends to be a copy of someone else's.

The assessment considers:

- the services {{HOSPITAL_NAME}} actually provides, and the invasive procedures and devices each involves;
- the patient population served, including any concentration of immunocompromised, paediatric, obstetric or elderly patients;
- the hospital's own surveillance data from the preceding period, including infection rates and any clusters;
- local and regional antimicrobial resistance patterns, drawn from the hospital's own culture reports where available;
- the physical plant — ventilation, water systems, layout, ongoing construction;
- findings from the previous assessment tool review, audits and any accreditation or statutory inspection;
- communicable disease activity in the surrounding community.

Risks are ranked so that the programme's effort follows the largest risks rather than the most visible ones. The completed assessment is tabled at the IPCC and retained.""",

"""7. The written annual programme

From the risk assessment, {{HOSPITAL_NAME}} produces a written infection prevention and control programme for the year. This document is what NABH means by the programme being documented, and it is approved by the IPCC and endorsed by management before the period it covers begins.

The programme states:

- the objectives for the period, each expressed so that meeting it can be demonstrated rather than argued;
- the surveillance to be conducted, and in which areas;
- the audits planned, their frequency and who performs them;
- the training planned, and for which staff groups;
- the improvement projects to be undertaken, with the person accountable for each;
- the resources required, which form the basis of the budget request in step 14;
- how and to whom progress will be reported.

Where an objective carries a numeric target — a compliance percentage, an infection rate, a training coverage figure — the target is set by {{HOSPITAL_NAME}} at [Hospital to define] against its own baseline. Progress against the programme is reviewed at each IPCC meeting, and the programme is closed out at the end of the period with a written statement of what was and was not achieved.""",

"""8. Surveillance of healthcare associated infection within the programme

Surveillance is a defined component of the programme of {{HOSPITAL_NAME}}, and the programme states which infections are under surveillance, in which areas, and who collects the data.

{{HOSPITAL_NAME}} conducts surveillance of, at minimum, surgical site infection, catheter-associated urinary tract infection, central line-associated bloodstream infection and ventilator-associated events, in whichever of these apply to the services it provides.

The case definitions, the counting of device days, the calculation of rates and the benchmarking and feedback method are set out in the hospital's surveillance policy and are not restated here. What this policy fixes is ownership: surveillance data is collected by the Infection Control Team, reviewed at every IPCC meeting, and fed back to the clinical area it came from. Data that is collected but never returned to the people whose practice it describes does not change practice.""",

"""9. Environmental surveillance within the programme

The programme of {{HOSPITAL_NAME}} also includes surveillance of the care environment, and the IPCC reviews its results alongside the infection data.

Environmental surveillance covers, according to the services {{HOSPITAL_NAME}} provides, the microbiological and physical monitoring of operating theatres and other critical areas — air sampling, ventilation and filter performance, temperature and humidity — together with any surface or water sampling the hospital undertakes.

The methods, sampling points, frequencies and acceptance limits are set out in the hospital's environment and facility policies, which own this subject. What this policy fixes is that environmental monitoring is part of the programme, that its results reach the IPCC rather than remaining in an engineering file, and that an out-of-limit result generates a recorded corrective action with a named owner and a re-test.""",

"""10. How the programme implements change

{{HOSPITAL_NAME}} does not rely on issuing a policy and expecting practice to follow. Every significant infection control intervention is implemented using a combined approach that addresses five things together, because interventions that address only one of them reliably fade once attention moves elsewhere:

- System change — putting in place what the practice physically requires: the handrub at the bedside, the sharps container within arm's reach, the isolation signage, the sink that works.
- Training and education — making sure staff know what to do and can demonstrate it, not merely that they were told.
- Monitoring and feedback — measuring what is actually happening and returning the result to the team concerned promptly enough to matter.
- Reminders and communication — visual cues at the point of care that prompt the right action at the moment it is needed.
- Culture — visible participation by senior clinicians and managers, so that the practice is understood as how {{HOSPITAL_NAME}} works rather than as an imposition from the infection control office.

Each improvement project in the annual programme identifies how it addresses all five.""",

"""11. Education and training under the programme

The Infection Control Team delivers and records a training programme covering all staff groups whose work bears on infection risk, including clinical, nursing, housekeeping, laundry, kitchen, waste-handling, security and administrative staff, at a depth appropriate to each role.

Training is delivered:

- at induction, before a new joiner begins independent work;
- at a recurring interval thereafter of [Hospital to define];
- whenever a policy, technique or piece of equipment changes materially;
- in response to an audit finding, outbreak or incident that reveals a specific gap.

Attendance is recorded by name, date, topic and trainer, and the records are retained. Where a technique is being taught — hand hygiene, PPE removal, spill management — the record notes that competence was observed and not merely that the session was attended.""",

"""12. Reviewing the programme against an infection control assessment tool

{{HOSPITAL_NAME}} formally reviews its infection prevention and control programme against an established infection control assessment tool, at an interval of [Hospital to define]. This is a structured self-assessment of the programme as a whole, and it is distinct from the routine practice audits described in step 3 — those examine whether staff followed a policy; this examines whether the programme itself is sound.

The tool adopted by {{HOSPITAL_NAME}} is [Hospital to define]. A widely used and freely available option is the World Health Organization's Infection Prevention and Control Assessment Framework, which scores a facility across eight programme components — the programme itself; written guidelines; education and training; surveillance of healthcare associated infection; multimodal implementation strategies; monitoring, audit and feedback; workload, staffing and bed occupancy; and the built environment, materials and equipment. Each component carries up to 100 points for a maximum of 800, and the total places the facility at one of four levels: inadequate at 0 to 200, basic at 201 to 400, intermediate at 401 to 600, and advanced at 601 to 800.

The review is led by the Infection Control Officer or Infection Control Nurse. It is completed honestly against evidence that can be produced on request, and not from recollection — a score that cannot be evidenced is recorded as not met.""",

"""13. Acting on the assessment findings

The completed assessment is not the output; the improvement is.

After each review the Infection Control Team prepares a short written summary setting out the score obtained overall and by component, the gaps identified, the action proposed for each gap, the person accountable for it and the date it is due. The summary is tabled at the next IPCC meeting and the discussion is minuted.

Progress against the previous cycle's actions is a standing item at IPCC meetings until each action is closed. Successive scores are retained and compared so that the direction of travel across cycles is visible — a single score describes a moment, while the trend across cycles is what demonstrates that the programme is working. Where a score has fallen, the fall is investigated and the reason recorded rather than explained away.

Findings that need money or posts that the committee cannot authorise are escalated to management under step 14.""",

"""14. Resources — the infection control budget

The management of {{HOSPITAL_NAME}} makes available the resources the infection prevention and control programme requires, and does so through a documented process rather than case by case.

Each year the Infection Control Team prepares a written statement of what the programme needs, derived from the annual programme in step 7. It covers personal protective equipment; hand hygiene consumables; disinfectants and cleaning agents; sterilisation supplies and monitoring indicators; biomedical waste consumables; isolation facility equipment; surveillance and audit tools; staff immunisation; training materials; and any staffing or infrastructure requirement identified by the assessment tool review.

The statement is submitted to management, and management records its decision in writing, including the reason where a request is not met in full and what alternative control will be applied in the interim. Both the request and the decision are retained, and the outcome is recorded in the IPCC minutes.

An unfunded infection control requirement is treated as an open risk: it is entered in the hospital's risk register and reviewed at each IPCC meeting until it is resolved.""",

"""15. Resources — consumables and continuity of supply

Infection control consumables are stocked as essential items at {{HOSPITAL_NAME}}, not as discretionary ones. Running out of gloves, handrub or colour-coded waste bags stops correct practice immediately, whatever the policy says.

{{HOSPITAL_NAME}} therefore:

- maintains a stock register for infection control consumables;
- defines a minimum stock level and a reorder level for each item, set at [Hospital to define] based on its own consumption;
- triggers replenishment at the reorder level rather than at exhaustion;
- checks expiry dates on disinfectants, handrub and sterilisation indicators, and removes expired stock from use;
- records any stock-out, the clinical areas affected, the interim measure applied and the corrective action, and reports it to the IPCC.

Substitution of a specified product with an alternative during a shortage requires the agreement of the Infection Control Officer, so that an ineffective or incompatible agent is not introduced under supply pressure.""",

"""16. Resources — staffing the programme

{{HOSPITAL_NAME}} allocates dedicated staff time to infection control rather than expecting the work to be absorbed.

The internationally recognised minimum benchmark is at least one full-time equivalent trained infection prevention professional — a nurse or a doctor — for every 250 beds, and this is a floor rather than a target; facilities with high-acuity or high-turnover caseloads commonly require a richer ratio. {{HOSPITAL_NAME}} sets its own establishment at [Hospital to define], stating the number of posts and the whole-time equivalent hours committed, and records the basis on which that number was arrived at.

Persons appointed to infection control roles receive formal training for the role, and the certificates or training records are retained. Where {{HOSPITAL_NAME}} cannot meet the benchmark, the shortfall is recorded as a risk under step 14 together with the interim arrangement being relied on, rather than left undocumented.""",

"""17. Resources — infrastructure at the point of care

Management ensures the physical means of infection control are present where care is delivered. The Infection Control Team verifies the following on its rounds and records any deficiency and its correction:

- hand hygiene facilities at every point of care — running water, soap and alcohol-based handrub, with dispensers filled and functional;
- personal protective equipment available in the appropriate sizes and quantities in each clinical area;
- puncture-resistant sharps containers within arm's reach wherever sharps are used, and not overfilled;
- colour-coded biomedical waste containers with liners at every point of waste generation;
- spill management materials accessible in every clinical area;
- isolation facilities as described in steps 18 to 22;
- functioning ventilation in critical areas.

A deficiency that cannot be corrected on the spot is logged with a target date and tracked to closure at the IPCC.""",

"""18. Isolation and barrier nursing facilities

{{HOSPITAL_NAME}} provides facilities that allow a patient with a known or suspected transmissible infection to be nursed apart from other patients. Isolation capacity is planned in advance, because a hospital that has to improvise placement during an outbreak will place patients badly.

{{HOSPITAL_NAME}} designates [Hospital to define] isolation room or rooms. Each designated room:

- is a single-occupancy room with its own door that can be kept closed;
- has, wherever the layout permits, its own toilet and washing facility;
- has hand hygiene facilities at the entrance and inside;
- has a supply of personal protective equipment held immediately outside or in an anteroom, so that staff can put it on before entering;
- holds patient-care equipment dedicated to that room — stethoscope, thermometer, blood pressure cuff — which is not shared with other patients and is decontaminated before leaving the room;
- has a clear means of displaying the precaution in force at the entrance, without naming the patient's diagnosis where that would breach confidentiality;
- has a waste and linen disposal arrangement that does not require carrying uncontained material through clean areas.

An inventory of isolation equipment is maintained and checked at an interval of [Hospital to define] so that the room is ready before it is needed rather than being equipped at the moment of admission.""",

"""19. Airborne infection isolation

Where {{HOSPITAL_NAME}} admits or is likely to encounter patients with infections transmitted by the airborne route — pulmonary tuberculosis, measles, varicella and similar — it provides or arranges access to an airborne infection isolation room.

Such a room operates at negative pressure relative to the corridor and adjoining spaces, so that air flows inward when the door is opened. The recognised engineering specification is a pressure differential of at least 2.5 pascals, equivalent to 0.01 inches of water gauge, with at least 12 air changes per hour for newly built or renovated rooms and not fewer than 6 air changes per hour where an existing room is being used. Room air is exhausted directly to the outside away from air intakes and occupied areas, or passed through a high-efficiency particulate air filter if it must be recirculated.

The pressure differential is verified at an interval of [Hospital to define] and the result recorded; a room assumed to be negative without measurement cannot be relied upon. The door is kept closed for the negative pressure to hold, and staff entering wear a fit-tested particulate respirator as specified in the transmission-based precautions policy.

Where {{HOSPITAL_NAME}} does not have such a room, it states in writing the interim measure it applies — a single room with the door closed, exhaust ventilation to the outside, masking of the patient — and the referral arrangement under which the patient is transferred to a facility that has one. This is recorded as a resource gap under step 14.""",

"""20. Patient placement when a single room is not available

A single-occupancy room is always the preferred placement for a patient requiring isolation. Where one is not available, the Infection Control Team is consulted before the patient is placed, and the decision and its reasoning are recorded.

The alternatives, in order of preference, are:

- cohorting — placing patients infected or colonised with the same organism together in one bay or area, with no other patients admitted to it, and where practicable with staff assigned to that cohort;
- placing the patient in a multi-bed room with a roommate selected for lowest risk, avoiding patients who are immunocompromised, who have an open wound or an invasive device, or whose expected stay is long.

Where a patient requiring droplet precautions must remain in a multi-bed room, a spatial separation of at least one metre — approximately three feet — is maintained between that patient and any other patient or visitor, and the curtain between beds is kept drawn.

Patients requiring airborne precautions are not cohorted with patients under other precautions and are not placed in an open bay other than as an explicitly recorded emergency measure while transfer is arranged.""",

"""21. Barrier nursing practice in an isolation area

Barrier nursing is what makes an isolation room effective; the room alone achieves nothing.

Within an isolation area of {{HOSPITAL_NAME}}:

- the precaution in force is displayed at the entrance and every person entering complies with it, including doctors, visitors, students and support staff;
- personal protective equipment appropriate to the precaution is put on before entry and removed before leaving, with hand hygiene performed after removal;
- the number of staff and visitors entering is kept to the minimum necessary, and visitors are instructed before their first entry;
- equipment dedicated to the room stays in the room and is decontaminated before it is removed;
- linen and waste are contained within the room before being removed;
- movement of the patient out of the room is limited to what is clinically necessary, the receiving area is informed in advance, and the patient is masked or the affected site covered during transfer as the precaution requires;
- cleaning of the room follows the enhanced and terminal cleaning arrangements in the environmental cleaning policy.

The precautions themselves — which apply to which route of transmission, and the sequence for putting on and removing protective equipment — are set out in the transmission-based precautions policy and are not restated here.""",

"""22. Isolation register and review of isolation use

The Infection Control Team maintains a register of every patient placed in isolation or barrier nursing at {{HOSPITAL_NAME}}, recording:

- the patient identifier, ward and room;
- the date isolation began and the date it ended;
- the indication — the organism or syndrome, and the route of transmission;
- the category of precaution applied;
- whether a single room was used and, if not, what alternative placement was used and why;
- the reason for discontinuation.

The register is reviewed at each IPCC meeting for what it reveals about the hospital rather than about individual patients: whether isolation capacity was sufficient, whether patients waited for placement, whether precautions were started promptly after suspicion arose, and whether any avoidable transmission followed a delay.

Competence in barrier nursing is maintained by practical drills at an interval of [Hospital to define], with the observations and any corrective action recorded.""",

"""23. Information, education and communication for patients, visitors and the community

{{HOSPITAL_NAME}} runs a planned information, education and communication programme extending beyond its staff to patients, attendants and the surrounding community.

The programme is set out as a calendar for the year, identifying the topic, the audience, the format, the person responsible and the date. Topics include hand hygiene, respiratory hygiene and cough etiquette, safe handling and disposal of waste at home, food and water hygiene, care of wounds and devices after discharge, appropriate use of antibiotics, and the locally relevant communicable diseases.

Delivery uses means suited to the audience rather than to the hospital's convenience:

- printed material and posters in the languages that patients of {{HOSPITAL_NAME}} actually read, using pictures where literacy cannot be assumed;
- displays in outpatient and emergency waiting areas, wards and reception;
- verbal counselling of patients and attendants at admission and before discharge, particularly where care will continue at home;
- outreach activity such as health camps, school sessions and community meetings, at a frequency of [Hospital to define].

Activities are recorded with the date, topic, audience and approximate number reached, and the record is reviewed by the IPCC so that the programme is adjusted rather than merely repeated.""",

"""24. Participation in community outbreaks and pandemics

{{HOSPITAL_NAME}} is part of the public health response in its area and does not treat an outbreak in the community as external to it.

{{HOSPITAL_NAME}} maintains a written outbreak and pandemic response plan stating:

- what triggers its activation, and who has the authority to activate it;
- the internal command structure during activation, by role;
- how surge capacity in beds, isolation space, staff, oxygen, PPE and consumables would be created, and from where;
- how screening and segregation of arriving patients would be organised at the entrance;
- how staff would be protected, monitored and relieved, including arrangements for exposed or infected staff;
- how the hospital communicates with the district health authority, with its own staff, and with patients and the public;
- how essential non-outbreak services would continue.

The named point of contact with the district or municipal health authority is [Hospital to define]. When a public health emergency is declared, {{HOSPITAL_NAME}} follows the directions issued by the competent health authority, reports the data required of it in the format and frequency specified, and makes staff, facilities or information available as requested within its capacity.

The plan is tested at an interval of [Hospital to define] by drill or tabletop exercise, and the findings are used to revise it. Participation and findings are recorded.""",

"""25. Notification of communicable disease to the public health authorities

{{HOSPITAL_NAME}} reports notifiable communicable disease to the public health authorities as required by law, and does so promptly — a notification that arrives after the contacts have dispersed serves no purpose.

In India this reporting runs through the national disease surveillance arrangements, under which hospitals in both the public and private sector report to the district surveillance unit, now largely through the electronic platform that has replaced paper reporting under the Integrated Disease Surveillance Programme. Individual States and local authorities additionally specify diseases notifiable within their jurisdiction, and the list applying to {{HOSPITAL_NAME}} is [Hospital to define].

{{HOSPITAL_NAME}} therefore:

- keeps the current notifiable disease list for its State available where clinicians can see it;
- names the person responsible for making notifications and a deputy — [Hospital to define];
- notifies within the timeframe prescribed for the disease concerned, and immediately for any suspected outbreak or unusual cluster, without waiting for laboratory confirmation where the clinical suspicion alone requires reporting;
- retains a copy of every notification made, with the date and the recipient;
- cooperates with any investigation the health authority undertakes, including providing records and access.

A cluster of infection among patients or staff of {{HOSPITAL_NAME}} is reported internally to the Infection Control Officer on the same day it is suspected, and externally where the disease or the scale requires it.""",

"""26. Recognising and responding to an outbreak within the hospital

An outbreak within {{HOSPITAL_NAME}} is any occurrence of infection above the expected level for that organism, area and period, or the appearance of an organism of particular significance even as a single case — including a multidrug-resistant organism new to the hospital.

On suspicion, the Infection Control Team:

- confirms the cases against the surveillance definitions and establishes when and where they occurred;
- institutes control measures immediately, without waiting for the investigation to conclude, since delay to achieve certainty costs more than a precaution later found unnecessary;
- informs the Infection Control Officer and the head of the affected area, and convenes the IPCC or an emergency subgroup of it;
- investigates the source and route, involving the laboratory, and reviews practice, equipment, environment and staffing in the affected area;
- notifies the public health authority where step 25 requires it;
- records the sequence of events, the measures taken and the outcome, and reports the conclusion to the IPCC with the changes required to prevent recurrence.

The outbreak record is retained and the lessons are reflected in revisions to the relevant policy and in the next annual risk assessment.""",

"""27. Reporting programme performance to management

The IPCC reports to the management of {{HOSPITAL_NAME}} at an interval of [Hospital to define]. The report is short, factual and evidenced, and covers surveillance results and trends; audit and compliance results; training coverage; the outcome of the most recent assessment tool review and progress on its gap-closure actions; outbreaks and significant incidents; resource requests outstanding; and the status of objectives in the annual programme.

Management records its consideration of the report and any decision taken. Where management declines or defers a request, the reason and the interim control are recorded under step 14.""",

"""28. Records retained under this policy

{{HOSPITAL_NAME}} retains the following as evidence that the programme operates: committee terms of reference and membership; meeting agendas, attendance records and minutes; the annual risk assessment; the written annual programme and its closing report; the infection control manual with version and amendment histories; completed assessment tool reviews and gap-closure summaries; training records; audit reports and feedback; surveillance data and reports; environmental monitoring results and corrective actions; the isolation register; drill records; budget requests and management decisions; stock and consumable registers; IEC activity records; outbreak investigation reports; and copies of notifications made to public health authorities.

Records are retained for a period of [Hospital to define], which is not less than any period prescribed by applicable law or by the accreditation standard, and are stored so that they remain legible, retrievable and confidential.""",

"""29. Review of this policy

This policy is reviewed by the IPCC at least once every [Hospital to define], and earlier where step 5 requires it. The review considers whether the structure described here still matches how {{HOSPITAL_NAME}} actually operates, and the policy is amended where it does not — a policy describing a committee that no longer meets, or a post no longer filled, is worse than no policy at all. Revisions are approved by the IPCC, endorsed by management, and issued under step 5."""
]

RESPONSIBILITY = """Management of {{HOSPITAL_NAME}} is accountable for the existence, funding and standing of the infection prevention and control programme, for approving the resources it requires, and for acting on what the IPCC reports.

The Infection Prevention and Control Committee owns this policy and the infection control manual. It approves the annual programme, reviews surveillance, audit and assessment results, tracks gap-closure actions to completion, and escalates unmet resource needs to management.

The Infection Control Officer leads the Infection Control Team, provides clinical and microbiological judgement to the programme, authorises isolation and outbreak control measures, and leads outbreak investigations.

The Infection Control Nurse conducts daily rounds, surveillance, audit and training, maintains the isolation register and programme records, prepares the assessment tool review, and is the first point of contact for staff on infection control questions.

Heads of departments and clinical area in-charges are responsible for infection control practice within their own areas, for ensuring their staff are trained and their area is equipped, and for closing the actions assigned to them.

All staff, practitioners, trainees, contract personnel and volunteers are responsible for following the infection control policies applicable to their work and for reporting breaches, deficiencies and suspected clusters promptly.

The administrative or purchase function is responsible for maintaining the supply of infection control consumables, and the engineering function for the ventilation, water and physical conditions the programme depends on."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Hospital Infection Control chapter, standard HIC.1.
- World Health Organization, Guidelines on Core Components of Infection Prevention and Control Programmes at the National and Acute Health Care Facility Level, 2016.
- World Health Organization, Minimum Requirements for Infection Prevention and Control Programmes, 2019.
- World Health Organization, Infection Prevention and Control Assessment Framework at the Facility Level (IPCAF), WHO/HIS/SDS/2018.9.
- World Health Organization, multimodal improvement strategy for implementing infection prevention and control interventions.
- National Centre for Disease Control, Ministry of Health and Family Welfare, Government of India, National Guidelines for Infection Prevention and Control in Healthcare Facilities, 2020.
- Centers for Disease Control and Prevention, Guideline for Isolation Precautions: Preventing Transmission of Infectious Agents in Healthcare Settings, and CDC guidance on airborne infection isolation room ventilation.
- Integrated Disease Surveillance Programme / Integrated Health Information Platform, Ministry of Health and Family Welfare, Government of India — outbreak and notifiable disease reporting.
- Internal documents of {{HOSPITAL_NAME}}: infection prevention and control practices policy, surveillance policy, environmental cleaning policy, sterilisation and instrument reprocessing policy, biomedical waste management policy, occupational health policy, and the outbreak and pandemic response plan."""

DISTRIBUTION = """Controlled master copy: Infection Control Team, {{HOSPITAL_NAME}}.

Copies issued to: the office of the head of the institution; the Infection Prevention and Control Committee (all members); nursing administration; every inpatient ward and critical care area; operating theatre and procedure rooms; emergency and outpatient departments; laboratory; pharmacy; central sterile supply; housekeeping and laundry; kitchen and dietary services; engineering and maintenance; stores and purchase; and the quality or accreditation coordinator.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the Infection Control Team."""

ABBREVIATIONS = """ACH — Air Changes per Hour
AIIR — Airborne Infection Isolation Room
AMR — Antimicrobial Resistance
CAUTI — Catheter-Associated Urinary Tract Infection
CLABSI — Central Line-Associated Bloodstream Infection
CSSD — Central Sterile Supply Department
HAI — Healthcare Associated Infection
HEPA — High-Efficiency Particulate Air (filter)
HIC — Hospital Infection Control (NABH chapter)
ICN — Infection Control Nurse
ICO — Infection Control Officer
ICT — Infection Control Team
IEC — Information, Education and Communication
IDSP — Integrated Disease Surveillance Programme
IHIP — Integrated Health Information Platform
IPC — Infection Prevention and Control
IPCAF — Infection Prevention and Control Assessment Framework (WHO)
IPCC — Infection Prevention and Control Committee
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NCDC — National Centre for Disease Control
OE — Objective Element
PPE — Personal Protective Equipment
SHCO — Small Healthcare Organisation
SSI — Surgical Site Infection
VAE — Ventilator-Associated Event
WHO — World Health Organization"""

DISCLAIMER = """This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. Guidance changes, and {{HOSPITAL_NAME}} remains responsible for verifying that the content is current and consistent with applicable law, statutory rules and the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, or any other body named in it. Wording is original; no text has been reproduced from the standards or guidelines referenced."""

OE_MAPPING = [
    {
        "oe_code": "HIC.1.a",
        "requirement": "The infection prevention and control programme is documented and aims at preventing and reducing healthcare associated infection risk",
        "steps": "Steps 1, 4-11 and 26",
    },
    {
        "oe_code": "HIC.1.b",
        "requirement": "The programme is reviewed using an infection control assessment tool",
        "steps": "Steps 12-13",
    },
    {
        "oe_code": "HIC.1.c",
        "requirement": "A multidisciplinary infection control committee and an infection control team coordinate all IPC activities",
        "steps": "Steps 2-3",
    },
    {
        "oe_code": "HIC.1.d",
        "requirement": "IEC programme for the community, and participation in managing community outbreaks and pandemics",
        "steps": "Steps 23-25",
    },
    {
        "oe_code": "HIC.1.e",
        "requirement": "Management makes the resources required for the programme available",
        "steps": "Steps 14-17",
    },
    {
        "oe_code": "HIC.1.f",
        "requirement": "Isolation and barrier nursing facilities are available",
        "steps": "Steps 18-22",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

1. WHO eight core components of an IPC programme — used as the structural spine of the programme and reproduced as the eight scored components in step 12. Components: IPC programmes; guidelines; education and training; HAI surveillance; multimodal strategies; monitoring/audit/feedback; workload, staffing and bed occupancy; built environment, materials and equipment. Components 1-6 apply at both national and facility level; 7-8 are facility level. Verified via WHO Guidelines on Core Components of IPC Programmes (2016), NCBI Bookshelf NBK401761 / NBK401773.

2. WHO IPCAF scoring — eight sections, maximum 100 points each, 800 total; bands Inadequate 0-200, Basic 201-400, Intermediate 401-600, Advanced 601-800. Used in step 12. Verified via WHO IPCAF (WHO/HIS/SDS/2018.9) and published facility studies applying it.

3. WHO multimodal improvement strategy, five elements — system change; training and education; monitoring and feedback; reminders and communications; culture of safety. Used verbatim as the five bullets in step 10 (in my own wording). Verified via WHO IPC core components multimodal strategy document.

4. IPC staffing benchmark — a minimum of one full-time equivalent trained infection prevention professional (nurse or doctor) per 250 beds, described in the source as a floor with a richer ratio argued for in higher-acuity settings. Used in step 16. Verified via WHO Minimum Requirements for Infection Prevention and Control Programmes (2019).

5. Airborne infection isolation room engineering specification — negative pressure differential of at least 2.5 Pa (0.01 inches water gauge); at least 12 air changes per hour for new construction and renovation, not fewer than 6 ACH for existing rooms; exhaust to outside away from intakes, or HEPA filtration if recirculated. Used in step 19. Verified via CDC guidance and ASHRAE Standard 170 as reported in current AIIR references.

6. Droplet precautions spatial separation — at least 3 feet (approximately 1 metre) between an infected patient and others where a single room is unavailable, with the bed curtain drawn; single-patient room preferred, cohorting only after consulting IPC personnel. Used in step 20. Verified via CDC Guideline for Isolation Precautions.

7. India national IPC reference — National Guidelines for Infection Prevention and Control in Healthcare Facilities, NCDC / Ministry of Health and Family Welfare, published January 2020 (first reprint March 2020), developed with the WHO Country Office. Cited in references and underpins the India-specific framing.

8. India outbreak and notifiable disease reporting route — hospitals in both public and private sector report to the district surveillance unit under the Integrated Disease Surveillance Programme, now largely through the Integrated Health Information Platform, the cloud-based system rolled out nationally in 2021 that replaced paper-based IDSP reporting; State governments additionally specify their own notifiable disease lists. Used in step 25. Verified via MoHFW/IDSP sources and the WHO India announcement of the IHIP rollout.

DELIBERATELY NOT INCLUDED — these were checked and judged to belong to other standards:
- Spaulding classification, high-level disinfection, sterilisation agents and contact times, CSSD reprocessing, laundry wash parameters, and the environmental cleaning schedule. These sit with HIC.3 / HIC.6 and remain open in scripts/master-policy-todos.md. Step 4 requires the manual to contain policies on them; it does not attempt to write those policies.
- HAI surveillance methodology (case definitions, device-day counting, rate calculation, benchmarking). Step 8 carries a pointer only and names the four infection types; the method belongs to CQI, matching the treatment already agreed for the HIC.2 draft.
- Environmental surveillance method (OT air sampling, HEPA integrity, temperature and humidity limits). Step 9 fixes ownership and the requirement that results reach the IPCC, but defers method to the environment/facility standards. Note: NABH's own HIC checklist tags this "HIC 1 c", but that checklist uses an older Entry-Level edition's numbering — under SHCO 3rd Edition, HIC.1.c is the infection control committee, so the tag was not followed as an OE map.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] — 20 occurrences: IPCC chair, meeting frequency and quorum; ICN committed hours; manual review interval; numeric programme targets; training interval; assessment tool identity and review interval; IPC staffing establishment; consumable stock/reorder levels; number of isolation rooms; isolation equipment check interval; AIIR pressure verification interval; barrier nursing drill interval; community outreach frequency; district health authority contact; outbreak plan test interval; State notifiable disease list; notification officer and deputy; management reporting interval; record retention period; intranet/folder location."""

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
    "status": "draft",
}

# newline="\n" is REQUIRED. Without it Python translates every \n to \r\n on Windows,
# including inside the policy text, and the docx renderer's step regex
# (/^(\d+)\.\s([^\n]+)\n\n([\s\S]*)$/) then fails to match "Title\r\n\r\nBody" --
# every step silently falls back to one unformatted paragraph.
with open("hic1_draft.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(draft, f, ensure_ascii=False, indent=2)


def dollar(s, tag="q"):
    assert f"${tag}$" not in s, f"delimiter collision in: {s[:60]}"
    return f"${tag}${s}${tag}$"


def pg_array(items):
    """Postgres text[] literal. Single quotes are doubled per SQL string escaping."""
    return "array[" + ", ".join("'" + i.replace("'", "''") + "'" for i in items) + "]"


def steps_literal(steps):
    if PROCEDURE_STEPS_IS_JSONB:
        return dollar(json.dumps(steps, ensure_ascii=False)) + "::jsonb"
    return "array[\n    " + ",\n    ".join(dollar(s, "s") for s in steps) + "\n  ]"


steps_type = "jsonb" if PROCEDURE_STEPS_IS_JSONB else "text[]"
steps_form = "a jsonb literal" if PROCEDURE_STEPS_IS_JSONB else "an array[...] literal"
steps_wrong = "ARRAY / _text" if PROCEDURE_STEPS_IS_JSONB else "jsonb"
steps_flag = "False" if PROCEDURE_STEPS_IS_JSONB else "True"

sql = f"""-- HIC.1 master policy draft — {STANDARD_CODE}
-- Run in the Supabase SQL Editor. Inserts/updates one row with status='draft'.
-- Review the universal_facts_checklist and oe_mapping before changing status to 'approved'.
--
-- COLUMN TYPES:
--   oe_codes        text[]  -- confirmed against live schema, written as array[...]
--   oe_mapping      jsonb   -- confirmed via the 20260803 migration
--   procedure_steps {steps_type}  -- confirmed against live schema
--
-- procedure_steps is written as {steps_form}. If that column is ever changed to
-- {steps_wrong}, this insert fails with a type error; regenerate with
-- PROCEDURE_STEPS_IS_JSONB = {steps_flag} in build_hic1.py. Re-check types with:
--   select column_name, data_type, udt_name from information_schema.columns
--   where table_name = 'shco_policy_masters' order by ordinal_position;
--
-- ON CONFLICT (standard_code) requires a unique constraint or unique index on
-- standard_code. Verify with:
--   select indexname, indexdef from pg_indexes
--   where schemaname = 'public' and tablename = 'shco_policy_masters';

insert into public.shco_policy_masters (
  standard_code, chapter, oe_codes, policy_title, purpose, scope, policy_statement,
  procedure_steps, responsibility, references_text, distribution, abbreviations,
  disclaimer, oe_mapping, universal_facts_checklist, status, updated_at
) values (
  {dollar(STANDARD_CODE)},
  {dollar(CHAPTER)},
  {pg_array(OE_CODES)},
  {dollar(POLICY_TITLE)},
  {dollar(PURPOSE)},
  {dollar(SCOPE)},
  {dollar(POLICY_STATEMENT)},
  {steps_literal(PROCEDURE_STEPS)},
  {dollar(RESPONSIBILITY)},
  {dollar(REFERENCES)},
  {dollar(DISTRIBUTION)},
  {dollar(ABBREVIATIONS)},
  {dollar(DISCLAIMER)},
  {dollar(json.dumps(OE_MAPPING, ensure_ascii=False))}::jsonb,
  {dollar(UNIVERSAL_FACTS_CHECKLIST)},
  'draft',
  now()
)
on conflict (standard_code) do update set
  chapter = excluded.chapter,
  oe_codes = excluded.oe_codes,
  policy_title = excluded.policy_title,
  purpose = excluded.purpose,
  scope = excluded.scope,
  policy_statement = excluded.policy_statement,
  procedure_steps = excluded.procedure_steps,
  responsibility = excluded.responsibility,
  references_text = excluded.references_text,
  distribution = excluded.distribution,
  abbreviations = excluded.abbreviations,
  disclaimer = excluded.disclaimer,
  oe_mapping = excluded.oe_mapping,
  universal_facts_checklist = excluded.universal_facts_checklist,
  status = 'draft',
  updated_at = now();
"""

with open("hic1_insert.sql", "w", encoding="utf-8", newline="\n") as f:
    f.write(sql)

# Guard: a CR anywhere in the emitted SQL breaks the renderer's step regex.
_raw = open("hic1_insert.sql", "rb").read()
assert b"\r" not in _raw, "CR found in hic1_insert.sql -- step formatting will silently regress"

# Guard: every step must still match the renderer's regex after round-tripping.
_step_re = re.compile(r"^(\d+)\.\s([^\n]+)\n\n([\s\S]*)$")
_unmatched = [i for i, s in enumerate(PROCEDURE_STEPS, 1) if not _step_re.match(s)]
assert not _unmatched, f"steps not matching renderer regex: {_unmatched}"

# --- sanity checks -----------------------------------------------------------
import re

problems = []
for i, s in enumerate(PROCEDURE_STEPS, 1):
    if not re.match(r"^\d+\.\s[^\n]+\n\n", s):
        problems.append(f"step {i}: does not match the renderer's 'N. Title\\n\\nBody' shape")
    if not s.startswith(f"{i}. "):
        problems.append(f"step {i}: number prefix mismatch -> {s[:20]!r}")

mapped = set()
for m in OE_MAPPING:
    for part in m["steps"].replace("Steps", "").replace("Step", "").split(","):
        part = part.strip().replace("and", ",").strip()
        for chunk in part.split(","):
            chunk = chunk.strip()
            if not chunk:
                continue
            if "-" in chunk:
                a, b = chunk.split("-")
                mapped.update(range(int(a), int(b) + 1))
            else:
                mapped.add(int(chunk))

print("steps:", len(PROCEDURE_STEPS))
print("format problems:", problems or "none")
print("mapping covers all 6 OEs:", sorted(m["oe_code"] for m in OE_MAPPING) == sorted(OE_CODES))
print("steps NOT referenced:", sorted(set(range(1, len(PROCEDURE_STEPS) + 1)) - mapped))
print("mapping references out-of-range step:", sorted(x for x in mapped if x > len(PROCEDURE_STEPS)) or "none")
# Placeholder audit — see policy_placeholder_audit.py. The count that used to sit
# here (steps + distribution, exact form only) omitted rendered fields and missed
# every "[Hospital to define — guidance]" variant entirely.
from policy_placeholder_audit import audit
audit(draft)
print("{{HOSPITAL_NAME}} occurrences:", json.dumps(draft, ensure_ascii=False).count("{{HOSPITAL_NAME}}"))
print("sql bytes:", len(sql))
print("$q$ delimiter count (must be even):", sql.count("$q$"))
