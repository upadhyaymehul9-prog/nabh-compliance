-- COP.12 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 2, printed page 68
-- (PDF page index 74). Levels: a Commitment, b Commitment, c Core, d Core,
-- e Core, f Commitment.
-- TWO OEs CARRY THE ASTERISK -- COP.12.a, COP.12.f.
-- UNAPPROVED DRAFT. Do not run this insert until the owner confirms the write.


insert into public.shco_policy_masters (
  standard_code,
  chapter,
  oe_codes,
  policy_title,
  purpose,
  scope,
  policy_statement,
  procedure_steps,
  responsibility,
  references_text,
  distribution,
  abbreviations,
  disclaimer,
  oe_mapping,
  universal_facts_checklist,
  version,
  revision_history,
  status
) values (
  'COP.12',
  'COP',
  array['COP.12.a', 'COP.12.b', 'COP.12.c', 'COP.12.d', 'COP.12.e', 'COP.12.f'],
  $q$Identification and Management of Patients at Higher Risk of Morbidity and Mortality$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} identifies and manages patients who are at higher risk of morbidity and mortality: people the hospital treats as vulnerable; a care-environment that is safe and secure for them; patients at risk of falling; patients at risk of developing or worsening pressure ulcers; patients at risk of developing or worsening deep vein thrombosis; and patients who need restraint.

Ordinary hospital processes — a high bed, an unanswered call, a tight sheet, an unreviewed catheter, a belt applied because the shift is short — harm these patients first. The chapter intent is that the organisation identifies and manages them. This document is that identification and that management. It is not the building's security system, and it is not the initial-assessment form; it is the programmes that start when a risk is found.$q$,
  $q$This policy applies to every clinical setting of {{HOSPITAL_NAME}} in which a patient may be vulnerable or at higher risk: in-patient wards, day-care, the emergency area, intensive or high-dependency areas where they exist, the operating theatre and recovery insofar as falls, pressure injury, thrombosis or restraint arise there, and any other location where a patient of this hospital is under care. It binds the clinicians and nurses who identify risk, the staff who apply the management measures, the doctor who orders restraint if restraint is used, and the named leads of the risk programmes.

It covers: identification and management of vulnerable patients; a safe and secure care-environment for the vulnerable patient; identification and management of patients at risk of fall; identification and management of patients at risk of developing or worsening pressure ulcers; identification and management of patients at risk of developing or worsening deep vein thrombosis; and identification and management of patients who need restraints, including the statutory rules that apply when the person has mental illness.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Initial assessment, the care plan, reassessment and early-warning of deterioration are governed by the assessment policy of {{HOSPITAL_NAME}} (AAC.3). That assessment may collect risk factors for falls, pressure injury, thrombosis or vulnerability. This policy owns the risk programmes that use those findings — the tool, the measures, the review. Completing an assessment checkbox is not running this programme; running this programme is not rewriting the initial-assessment dataset.
- The two identifiers at the point of care are governed by the uniform-care policy of {{HOSPITAL_NAME}} (COP.1). This policy uses those identifiers; it does not invent another identity system for vulnerable patients.
- Building security, access control, CCTV, fire and the physical fabric of the premises are governed by the facility-management policies of {{HOSPITAL_NAME}} (FMS, not yet drafted). COP.12.b is the care-environment for the vulnerable patient — who is at the bedside, how the patient is observed, how a missing vulnerable patient is noticed — not the building's locks and cameras.
- Prevention of child or neonate abduction and abuse is governed by the paediatric policy of {{HOSPITAL_NAME}} (COP.8). If children are included in this hospital's vulnerable categories, this policy still owns the vulnerability programme; it does not rewrite the abduction-and-abuse measures.
- Intensive-care admission criteria and end-of-life care are governed by the intensive-care policy of {{HOSPITAL_NAME}} (COP.6). A patient in intensive care may be vulnerable; the vulnerability programme remains this document.
- Standard precautions, transmission-based precautions and hand hygiene are governed by the infection-prevention-and-control-practices policy of {{HOSPITAL_NAME}} (HIC.2). HIC does not own falls, pressure ulcers, venous thromboembolism or restraints. This policy does not rewrite PPE.
- Medication used for analgesia, anticoagulation or sedation is governed by the medication policies of {{HOSPITAL_NAME}} (MOM, not yet drafted). This policy owns the decision that a patient is at thrombotic risk and that a mechanical or pharmacological measure is indicated; MOM owns the anticoagulant as a medication. This policy owns physical restraint; it does not write chemical restraint as a medication process.
- The method of informed consent generally, and patient rights including dignity, are governed by the patient-rights policies of {{HOSPITAL_NAME}} (PRE, not yet drafted). Restraint under this document remains a last-resort clinical measure and is not a substitute for consent to treatment.
- The medical record itself is governed by the information-management policies of {{HOSPITAL_NAME}} (IMS, not yet drafted). This policy owns the risk-assessment and restraint-record content written into that record.
- Rehabilitation, pain and nutrition are governed by the pain, rehabilitation and nutrition policy of {{HOSPITAL_NAME}} (COP.13). Mobilisation as a thrombosis or pressure-ulcer measure is coordinated with that document; it is not rewritten here.$q$,
  $q${{HOSPITAL_NAME}} identifies patients it treats as vulnerable and manages their care as a defined programme, not as an informal extra kindness.

{{HOSPITAL_NAME}} provides a safe and secure care-environment for the vulnerable patient. Building security remains the facility policies.

{{HOSPITAL_NAME}} identifies patients at risk of falling and manages that risk.

{{HOSPITAL_NAME}} identifies patients at risk of developing or worsening pressure ulcers and manages that risk.

{{HOSPITAL_NAME}} identifies patients at risk of developing or worsening deep vein thrombosis and manages that risk.

{{HOSPITAL_NAME}} identifies patients who need restraint and manages restraint as a last-resort, time-limited, documented measure. Where the person has mental illness, restraint and seclusion follow the Mental Healthcare Act, 2017. Restraint is not used for the convenience of staff, as punishment, or as a substitute for observation.$q$,
  array[
    $s$1. Identifying and managing vulnerable patients

The organisation identifies and manages vulnerable patients. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask who this hospital treats as vulnerable and what is done differently for them. The answer must be a written category list that staff applied to yesterday's admissions, and a management method that can be shown in the record, not a poster that says the hospital cares.

A vulnerable patient, in this document, is a person whose age, condition, disability, dependence or circumstance makes ordinary hospital processes more likely to cause harm, and who may be less able to recognise or report that harm. The categories {{HOSPITAL_NAME}} treats as vulnerable are [Hospital to define — the categories of patient this hospital treats as vulnerable]. This document does not mandate a national list. Typical categories a hospital may include — the elderly, children, persons with disability, persons with mental illness, the unconscious, the terminally ill, women in late pregnancy, patients who cannot communicate in a language staff speak — are examples for the hospital to accept, reject or add; they are not a required set. A category the hospital does not serve (for example neonates, if the service directory has no neonatal service) is not listed as if it did.

Identification happens at the first clinical contact that can do it, and is repeated when the patient's condition changes. The method of identification — a field on the initial-assessment form owned in structure by the assessment policy, a separate vulnerable-patient flag, a wristband of a defined kind, or another method — is [Hospital to define — how a vulnerable patient is identified and how that identification is recorded]. The assessment policy may collect the facts; this step owns that those facts produce a flag and a plan. A checkbox ticked and never read is not identification.

Management means that the flag changes what happens next: the observations, the accompaniment, the environment at step 2, and the specific risk programmes at steps 3 to 6 when those risks are also present. The management measures for each category, beyond those later steps, are [Hospital to define — the management measures applied once a patient is identified as vulnerable]. A flag without a measure is a label.

Why this has to be a programme rather than kindness: kindness is uneven. The patient who is quietly confused at night, who does not look "geriatric", who is a child on an adult ward because the paediatric bed is full, is the one a kindness-based system misses. Written categories, applied at admission and on change of condition, are how that patient is seen. The harm this step exists to prevent is not a rare event; it is the ordinary hospital day landing on someone who cannot get out of its way.

The common error is a policy that lists categories and a ward that identifies nobody, because no one is assigned to apply the list, or because every patient is declared vulnerable and the flag means nothing. Both failures are the same failure: identification that does not discriminate. The named person who keeps the category list current and who reviews that flags are applied is [Hospital to define — who keeps the vulnerable-patient category list and reviews that flags are applied].

This step does not rewrite paediatric abduction measures, intensive-care admission, or facility locks.$s$,
    $s$2. Safe and secure care-environment for the vulnerable patient

The organisation provides for a safe and secure environment for the vulnerable patient.

The care-environment in this step is what surrounds the patient at the point of care: a bed or trolley from which the patient cannot silently fall or wander unnoticed, a call method the patient can use, lighting and toileting access that match the patient's ability, accompaniment when the patient must leave the unit, and a method of noticing that a vulnerable patient is not where they should be.

Building security — locks, cameras, perimeter, visitor control as a facility system — is governed by the facility-management policies of {{HOSPITAL_NAME}}. This step uses those systems where they exist; it does not specify cameras or staffing ratios.

The care-environment measures in force, including how a missing vulnerable patient is noticed and who is called, are [Hospital to define — the care-environment measures for vulnerable patients, including how a missing vulnerable patient is noticed]. Paediatric abduction remains the paediatric policy.

A vulnerable patient is not left in a public corridor, an unlocked bathroom, or an unattended trolley as a holding pattern.$s$,
    $s$3. Patients at risk of fall

The organisation identifies and manages patients who are at risk of fall.

Identification uses a written method. The method — a named tool, a locally written set of factors, or another method — is [Hospital to define — the method used to identify patients at risk of fall]. This document does not mandate a proprietary score or a numeric cut-off. The Agency for Healthcare Research and Quality toolkit Preventing Falls in Hospitals (2013) and Dykes and colleagues (2010) — chapter references 43 and 16 — inform that identification plus a bundle of measures is the work; they are not imported as a required tool.

Identification is recorded against the unique identification number, at admission or at first contact that can do it, and is repeated when condition, medication or mobility changes. The assessment policy may collect mobility and medication facts; this step owns that those facts produce a falls-risk identification and a plan.

Management measures once a patient is identified at risk are [Hospital to define — the measures applied to a patient identified at risk of fall]. Typical measures a hospital may choose — footwear, bed height, assistance to toilet, keeping a call device in reach, reviewing medicines that increase fall risk with the treating doctor — are examples, not a mandated bundle. Medication review as a prescription change is owned by the medication policies.

A fall that occurs is recorded, the patient is assessed, and the identification and measures are reviewed. How a fall is reported is [Hospital to define — how a fall is recorded and reported]. This step does not set a numeric fall-rate target.$s$,
    $s$4. Patients at risk of pressure ulcers

The organisation identifies and manages patients who are at risk of developing or worsening of pressure ulcers.

Identification uses a written method. The method is [Hospital to define — the method used to identify patients at risk of developing or worsening pressure ulcers]. This document does not mandate a named scale or a numeric cut-off. Burch and Tort (2019) and Moore and Patton (2019) — chapter references 7 and 33 — record that risk-assessment tools alone have not been shown to prevent pressure ulcers; identification is still required, and management does the work.

A patient who already has a pressure ulcer is identified as at risk of worsening and is managed, not only patients with intact skin.

Management measures once a patient is identified at risk, or as having an ulcer, are [Hospital to define — the measures applied to prevent developing or worsening pressure ulcers, including skin inspection and repositioning]. Repositioning interval, support surfaces and dressing choice are this hospital's clinical decision. Infection-control of a wound dressing remains HIC.2 / HIC.4 wound-care practice where those documents already apply; this step owns the pressure-injury programme.

The ulcer, if present, is described in the record (location, stage or the hospital's chosen description method) and reassessed. The description method is [Hospital to define — how a pressure ulcer is described and reassessed in the record]. No staging system is mandated here.$s$,
    $s$5. Patients at risk of deep vein thrombosis

The organisation identifies and manages patients who are at risk of developing or worsening deep vein thrombosis. (The official OE text repeats "developing"; this step uses the official sense: risk of a new thrombosis, and risk of a thrombosis that is already present getting worse.)

Identification uses a written method. The method is [Hospital to define — the method used to identify patients at risk of developing or worsening deep vein thrombosis]. This document does not mandate a named score. Henke and Pannucci (2010) — chapter reference 20 — inform that risk-factor assessment and prophylaxis are a paired process; they are not imported as a required calculator.

Management once a patient is identified at risk is [Hospital to define — the measures applied to a patient at risk of developing or worsening deep vein thrombosis, including mechanical and, where indicated, pharmacological options]. Pharmacological prophylaxis, when used, is prescribed and administered under the medication policies of {{HOSPITAL_NAME}}. This step owns the indication and that a measure is in place; MOM owns the drug. A patient who already has a thrombosis is managed for worsening under the treating clinician, including mobilisation or restriction as that clinician decides, coordinated with the rehabilitation policy where mobilisation is a rehabilitation plan.

Contraindications to a chosen measure are recorded rather than silently skipped. This step does not print a dosing table.$s$,
    $s$6. Patients who need restraints

The organisation identifies and manages patients who need restraints. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask when this hospital restrains a person, under whose order, for how long, and how it is recorded. The answer must be a method that yesterday's restraint, if any, followed, not a cupboard of belts.

Restraint, in this document, is the use of physical or mechanical means to limit a patient's movement when that limitation is not part of ordinary treatment (a surgical table strap during an operation is not this step; a belt applied on the ward to stop a person rising is). Seclusion — placing a person alone in a room they cannot leave — is included where {{HOSPITAL_NAME}} uses it. Chemical restraint as a medication process is owned by the medication policies; this step forbids using a sedative as an undeclared substitute for a documented restraint decision, and it does not write the drug protocol.

The legal frame has two layers.

Where the person has mental illness, restraint and seclusion follow the Mental Healthcare Act, 2017: they are used only when they are the only means available to prevent imminent and immediate harm to the person or to others; they are not used as punishment or for the convenience of staff; and they are documented. {{HOSPITAL_NAME}} does not invent a parallel rule for this group. The American Psychiatric Nurses Association position on seclusion and restraint (2018) — chapter reference 58 — is consistent with a last-resort, documented, time-limited posture and is not imported as a substitute for the 2017 Act.

Where the person does not have mental illness — pulling at a tube, unsafe mobility after a procedure, delirium on a medical ward — restraint is still last-resort, time-limited and documented. It is used only when less restrictive measures have been tried or are not possible, only to prevent imminent harm to the patient or to others, never as punishment, never because the ward is short of staff, and only on a recorded order of a doctor. The order states the reason, the type of restraint, the time it starts, and the latest time it must be reviewed. The review interval, the observations required while restraint is in place, and who may apply the device are [Hospital to define — the restraint order, review interval, observations while restrained, and who may apply the device]. An order without a review time is incomplete. Restraint that continues because nobody came back is a new, unordered restraint.

Why last-resort is the rule, not a slogan: restraint prevents one harm by inflicting another — loss of liberty, pressure injury, delayed detection of deterioration, humiliation. A hospital that restrains because it is easier than sitting with the patient has chosen the harm it finds convenient. The common error is a device applied by a nurse "for safety", with no order, no clock, and no record, which then remains until the next shift discovers it or the patient is injured by it. That practice is forbidden here. If the situation is so urgent that a device is applied before the doctor arrives, the doctor attends at once, the order is written, and the reason for the seconds without an order is recorded. Urgency is not a standing exemption.

Identification of need is the clinical judgement that imminent harm cannot otherwise be prevented. Family are informed that restraint is in use, unless the emergency makes that impossible in the moment, in which case they are informed as soon as possible. Consent to treatment is still owned by the patient-rights policies; restraint is not a way around refusal of care.

Every episode is recorded against the unique identification number: indication, less-restrictive measures tried, type, start and stop times, observations, the ordering doctor, and any injury. Episodes are reviewed at [Hospital to define — the forum and interval at which restraint episodes are reviewed]. A hospital that records zero episodes because it does not document them is not a hospital that does not restrain.

Devices used, and where they are kept, are [Hospital to define — the restraint devices used and where they are kept]. Devices are not stored in a way that makes informal use the path of least resistance.$s$,
    $s$7. Records, review and the order of operations

Every vulnerable-patient identification, care-environment measure, falls-risk identification and fall report, pressure-ulcer identification and description, thrombosis-risk identification and prophylaxis indication, and restraint episode is recorded against the unique identification number and is retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for higher-risk-patient records] for: vulnerable-patient flags that match the written categories and that have a management measure; falls, pressure-ulcer and thrombosis identifications with a plan rather than a score alone; restraint episodes with a doctor's order, a review time, observations, and a stop time; and no restraint of a person with mental illness that falls outside the Mental Healthcare Act, 2017.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a serious fall, a stage-worsened pressure ulcer, a hospital-acquired thrombosis, a restraint injury, or an unauthorised restraint occurs, or when the assessment, facility, paediatric, medication or patient-rights policies that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} identifying and managing patients at higher risk of morbidity and mortality, and for restraint that is last-resort, documented and lawful.

The named person at step 1 keeps the vulnerable-patient category list and reviews that flags are applied.

Treating clinicians identify risk, order prophylaxis or restraint when indicated, and review restraint at the stated interval.

Nursing staff apply identification tools, apply the management measures at steps 2 to 5, apply restraint only under a doctor's order as step 6 requires, observe the restrained patient, and record falls, ulcers and restraint episodes.

The facility function provides building security under its own policies; this document remains responsible for the care-environment at the bedside.

The quality or accreditation coordinator audits the records at step 7 and reports findings to the head of the institution.

All staff are expected to treat an unidentified vulnerable patient who came to harm, a fall that was not recorded, and a restraint without an order or a clock, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.12.
- Mental Healthcare Act, 2017, insofar as restraint or seclusion of a person with mental illness is used: last resort to prevent imminent and immediate harm, not as punishment or for the convenience of staff, and documented.
- Agency for Healthcare Research and Quality, Preventing Falls in Hospitals (2013) — chapter reference 43; informs identification plus measures; not a mandated tool.
- Dykes, P. C., et al. (2010). Fall Prevention in Acute Care Hospitals. JAMA, 304(17), 1912 — chapter reference 16.
- Burch, J., and Tort, S. (2019). Does the use of risk assessment tools help prevent the development of pressure ulcers? Cochrane Clinical Answers — chapter reference 7.
- Moore, Z. E., and Patton, D. (2019). Risk assessment tools for the prevention of pressure ulcers. Cochrane Database of Systematic Reviews — chapter reference 33.
- Henke, P., and Pannucci, C. (2010). VTE Risk Factor Assessment and Prophylaxis. Phlebology, 25(5), 219-223 — chapter reference 20.
- American Psychiatric Nurses Association, Position Statement on the Use of Seclusion and Restraint (2018) — chapter reference 58; last-resort posture only, not a substitute for the 2017 Act.
- Internal documents of {{HOSPITAL_NAME}}: the vulnerable-patient category list and identification method; the care-environment measures; the falls, pressure-ulcer and thrombosis identification methods and measures; the restraint order and episode records; the assessment policy; the uniform-care policy; the paediatric policy; the intensive-care policy; the facility-management policies; the medication policies; the patient-rights policies; the infection-control practices policy; and the pain, rehabilitation and nutrition policy.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every in-patient ward; day-care; the emergency area; intensive or high-dependency areas where they exist; nursing administration; the named person who keeps the vulnerable-patient list; and every head of department whose staff identify risk or apply restraint.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The identification methods and the restraint-order method — the working documents this policy requires — are held on the wards that use them.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, ICU, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

DVT — Deep Vein Thrombosis
MHC — Mental Healthcare Act, 2017
VTE — Venous Thromboembolism

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the Mental Healthcare Act, 2017, insofar as restraint or seclusion of a person with mental illness is used. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "COP.12.a", "requirement": "The organization identifies and manages vulnerable patients.", "steps": "Steps 1, 7", "evidence": "The written categories of patient this hospital treats as vulnerable, dated, matching the services the hospital actually provides rather than a generic downloaded list, and naming the person who keeps the list current; the identification method (flag, field, band or other) and sample records showing identification at first clinical contact and on change of condition, against the unique identification number, producing a flag that is read rather than a checkbox that is never used; management measures for each category beyond the later risk programmes, with sample records showing the flag changed observations, accompaniment or environment rather than remaining a label; review records that flags are actually applied, including enquiry when a period of admissions shows nobody flagged or when everybody is flagged; induction or briefing records showing ward staff have been shown the categories and the method; the distinction recorded that the assessment policy may collect the facts while this programme owns the flag and the plan; the audit sample at step 7 of flags that match the written categories and that have a management measure", "responsible": "Named person at step 1 keeps the category list and reviews application; treating clinicians and nurses identify and manage; quality or accreditation coordinator audits; head of the institution is accountable for the programme"}, {"oe_code": "COP.12.b", "requirement": "The organization provides for a safe and secure environment for the vulnerable patient.", "steps": "Steps 2, 7", "evidence": "The written care-environment measures for vulnerable patients, including call method, accompaniment when leaving the unit, and how a missing vulnerable patient is noticed and who is called; sample records of those measures applied; building security left to facility policies rather than specified here", "responsible": "Nursing staff apply the care-environment measures; facility function owns building security; named person at step 1 reviews that the measures exist"}, {"oe_code": "COP.12.c", "requirement": "The organization identifies and manages patients who are at risk of fall.", "steps": "Steps 3, 7", "evidence": "The written falls-risk identification method and sample identifications against the unique identification number, repeated on change of condition; the measures applied once at risk; fall reports with assessment after a fall and review of measures; no mandated numeric score or rate target", "responsible": "Nurses identify and apply measures; treating clinicians review medicines that increase fall risk; quality or accreditation coordinator audits"}, {"oe_code": "COP.12.d", "requirement": "The organization identifies and manages patients who are at risk of developing / worsening of pressure ulcers.", "steps": "Steps 4, 7", "evidence": "The written pressure-ulcer risk identification method, including patients who already have an ulcer; measures for prevention of developing or worsening, including skin inspection and repositioning as this hospital defined them; ulcer description and reassessment in the record", "responsible": "Nurses identify, inspect, reposition and record; treating clinicians manage existing ulcers; quality or accreditation coordinator audits"}, {"oe_code": "COP.12.e", "requirement": "The organization identifies and manages patients who are at risk of developing or worsening of deep vein thrombosis.", "steps": "Steps 5, 7", "evidence": "The written thrombosis-risk identification method; measures applied including mechanical and, where indicated, pharmacological options; contraindications recorded; pharmacological prophylaxis prescribed under the medication policies rather than dosed in this document", "responsible": "Treating clinicians identify risk and indicate prophylaxis; nurses apply mechanical measures and administer medicines under MOM; quality or accreditation coordinator audits"}, {"oe_code": "COP.12.f", "requirement": "The organization identifies and manages patients who need restraints.", "steps": "Steps 6, 7", "evidence": "The written restraint method distinguishing persons with mental illness (Mental Healthcare Act, 2017: only means available to prevent imminent and immediate harm, not punishment, not convenience of staff, documented) from other patients (still last-resort, time-limited, documented, doctor's order); the definition in use (physical or mechanical limitation of movement that is not ordinary treatment; seclusion where used); sample episode records against the unique identification number showing indication, less-restrictive measures tried, type of restraint, start time, latest review time, observations while restrained, ordering doctor, stop time, family informed, and any injury; records of any urgent application before a doctor arrived, with the doctor attending at once and the order written; the written review interval, observations and named roles who may apply a device; the forum and interval at which episodes are reviewed; the devices used and where they are kept; the rule recorded that chemical restraint as a medication process is owned by the medication policies and is not an undeclared substitute; audit sample at step 7 of orders with a clock and of no MHC-inconsistent restraint", "responsible": "Treating doctor orders and reviews restraint; nurses apply only under that order, observe and record; head of the institution is accountable that restraint is last-resort and lawful; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. COP.12 standard text and all six OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 2 Care of Patients, printed page 68 (PDF page index 74). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: COP.12.a Commitment, COP.12.b Commitment, COP.12.c Core, COP.12.d Core, COP.12.e Core, COP.12.f Commitment.
   TWO OEs CARRY THE ASTERISK -- COP.12.a and COP.12.f. The draft builds two separate deep blocks (step 1 for a; step 6 for f). COP.12.b, c, d and e are unasterisked and are correspondingly Tier 2 even though c, d and e are Core.
   COP.12.e official wording contains a doubled "developing" ("worsening of developing deep vein thrombosis"). Mapping requirement uses the official sense without copying the doubled word into the polished requirement, as the drafting brief instructed.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the COP.12 page read directly, and the committed asterisk file. COP.12 was not among the 14 mismatches of the 2026-08-10 audit.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. TWO OF SIX OEs ARE TIER 1. Tier 1: COP.12.a, COP.12.f -- steps 1 and 6 carry the reasoning (why a programme rather than kindness; why last-resort restraint is the rule). Tier 2: COP.12.b, c, d, e -- requirement and method without extended rationale. Reviewer to note the shallower treatment of the three Core OEs c, d and e is a DECISION UNDER THE STANDING RULE, not an omission: they are Core and unasterisked.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of COP.12.a/f against all six approved HIC masters and the AAC.1-AAC.8 drafts. Search terms: vulnerable, restraint, seclusion, fall, pressure ulcer, thrombosis, DVT, VTE, secure environment.
   HIC.1-HIC.6: no ownership of falls, pressure ulcers, VTE or restraints. HIC.2 PPE/HH is pointed at and not rewritten. Not added to the reconciliation list.
   AAC.3: initial assessment may collect risk factors. Scope states AAC.3 owns the assessment dataset; this document owns the risk programmes. Not a contradiction.
   AAC.1: service directory may include mental-health or paediatric services that affect who is vulnerable. This draft does not rewrite the directory.
   COP.8 (forward): child abduction/abuse. Flagged in Scope.
   COP.6 (forward): ICU. Flagged in Scope.
   FMS (forward): building security vs care-environment. Flagged in Scope as required.
   MOM (forward): anticoagulants, chemical restraint as medication. Flagged.
   PRE (forward): consent and dignity. Flagged.
3. FORWARD REFERENCES: FMS building security; MOM medication; PRE consent; IMS record; COP.8, COP.6, COP.13, COP.1. Each is a deliberate boundary.
4. T2 QUICK CHECK: COP.12.c falls vs AAC.3 assessment -- flagged, AAC.3 may collect factors, this owns the programme. COP.12.d PU vs HIC wound care -- flagged, HIC owns dressing asepsis where already written, this owns the PU programme. COP.12.e DVT vs MOM anticoagulant -- flagged. COP.12.b vs FMS -- flagged. None is a contradiction with an approved document.

STATUTORY AND EXTERNAL FACTS
5. Mental Healthcare Act, 2017 -- cited for restraint/seclusion of persons with mental illness, at the level of the Act's general scheme (last resort to prevent imminent harm; not punishment; not convenience; documented). No section number. For patients without mental illness this document still requires last-resort, time-limited, documented restraint with a doctor's order. NOT the Clinical Establishments Act, NOT BMW Rules, NOT the Food Safety and Standards Act.
6. AHRQ Preventing Falls in Hospitals (2013) and Dykes 2010 -- chapter refs 43 and 16; identification plus measures; no mandated tool or cut-off.
7. Cochrane pressure-ulcer risk-tool reviews (chapter refs 7, 33) -- tools alone have not been shown to prevent ulcers; identification still required; management does the work. No mandated Braden cut-off.
8. Henke and Pannucci 2010 -- chapter ref 20; risk assessment paired with prophylaxis; no mandated score or dose.
9. APNA 2018 seclusion and restraint -- chapter ref 58; last-resort posture only.
10. NO NUMBERS ARE STATED as requirements -- no fall-rate targets, no repositioning-hour mandates, no restraint-duration maxima as a number, no VTE-score cut-offs. Every such value is [Hospital to define].

EDITORIAL POSITIONS TAKEN
11. Step 1's refusal to mandate a national vulnerable-category list, and the warning that flagging everybody empties the flag, are editorial positions.
12. Step 6's two-layer legal frame (MHC 2017 for mental illness; last-resort documented medical restraint for others), the prohibition of convenience restraint, and the rule that an order without a review time is incomplete, are editorial positions consistent with the asterisk and the Act's scheme.
13. Step 6's exclusion of a surgical table strap as ordinary treatment, and the forwarding of chemical restraint to MOM, are editorial positions.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
14. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the Mental Healthcare Act, 2017, insofar as restraint or seclusion of a person with mental illness is used -- the statute this document's References actually cite. It does NOT name BMW Rules 2016, FSS Act 2006, or CEA 2010.

DELIBERATELY NOT INCLUDED
- Building locks, CCTV, fire -- FMS.
- Initial-assessment dataset -- AAC.3.
- Paediatric abduction -- COP.8.
- Anticoagulant dosing -- MOM.
- Chemical-restraint drug protocol -- MOM.
- PPE -- HIC.2.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 21 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 19 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 21; a search for "Hospital to define" without brackets finds all 21, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: the categories of patient treated as vulnerable; how a vulnerable patient is identified and recorded; the management measures once identified; who keeps the category list; the care-environment measures including how a missing vulnerable patient is noticed; the falls identification method and measures; how a fall is recorded; the pressure-ulcer identification method, measures, and description method; the thrombosis identification method and measures; the restraint order, review interval, observations and who may apply the device; the forum that reviews restraint episodes; the restraint devices and where they are kept; the audit interval; the review interval for this policy; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
