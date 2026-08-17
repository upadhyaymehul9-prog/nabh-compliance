-- COP.9 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 2, printed page 66
-- (PDF page index 72). Levels: a Commitment, b Commitment, c Commitment, d Commitment,
-- e Commitment.
-- ONE OE CARRIES THE ASTERISK -- COP.9.a.
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
  'COP.9',
  'COP',
  array['COP.9.a', 'COP.9.b', 'COP.9.c', 'COP.9.d', 'COP.9.e'],
  $q$Procedural Sedation$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} administers procedural sedation in a consistent manner: written guidance that is the same wherever sedation is given, informed consent before the sedative is given, competent persons who perform and who monitor, intra-procedure monitoring of the stated minimum parameters, and documented post-procedure monitoring with discharge from recovery against objective criteria.

The chapter intent is that written guidance and applicable laws guide the care of patients undergoing procedural sedation. Sedation given as a habit of the operator, in a room that cannot monitor, by a person who is also the only pair of hands, is not that service. This document is the process that makes the intent operational in every procedure room where a sedative is given to permit a procedure.

This document is not the anaesthesia policy and it is not the surgical-procedure policy. Procedural sedation is a distinct service. When sedation becomes general anaesthesia, care moves to the anaesthesia policy of {{HOSPITAL_NAME}}.$q$,
  $q$This policy applies to every location in which {{HOSPITAL_NAME}} administers procedural sedation: the operation theatre, endoscopy or other procedure rooms, the emergency area, day-care, the imaging suite where a patient is sedated for a procedure, and any other area the hospital names as a sedation location. It binds the person who administers the sedative, the person who monitors the patient, the clinician who obtains consent for sedation, and the staff of the recovery area from which the patient is discharged.

It covers: written guidance that makes administration of procedural sedation consistent across those locations; informed consent for administration of procedural sedation; competence of the persons who perform and who monitor sedation; intra-procedure monitoring of heart rate, cardiac rhythm, respiratory rate, blood pressure, oxygen saturation and level of sedation; and documented post-procedure monitoring with discharge from the recovery area based on objective criteria.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Anaesthesia services — pre-anaesthesia assessment, the anaesthesia plan, pre-induction assessment, anaesthesia consent, monitoring under anaesthesia, post-anaesthesia recovery, and the anaesthetic record — are governed by the anaesthesia policy of {{HOSPITAL_NAME}} (COP.10). Sedation is not general anaesthesia. This document does not write the anaesthesia policy. COP.10 does not write this sedation policy. A patient whose intended sedation is expected to reach a depth that is general anaesthesia is cared for under COP.10, not under a stretched reading of this document.
- Clinical procedures and procedures in the operation theatre, including the surgical safety checklist, site-marking and the operation note, are governed by the procedures-and-operation-theatre policy of {{HOSPITAL_NAME}} (COP.11, sibling, not yet drafted). This document owns the sedation that may be given so that a procedure can be performed; it does not own the procedure. COP.11 does not write sedation method.
- The method of informed consent generally — how consent is explained, recorded and witnessed — is governed by the patient-rights policies of {{HOSPITAL_NAME}} (PRE, not yet drafted). This policy owns that informed consent for administration of procedural sedation is obtained before the sedative is given. PRE does not decide whether sedation consent happened; this document does not write the hospital's general consent form.
- Who may prescribe, store, dispense and account for medicines, including controlled drugs used as sedatives, is governed by the medication policies of {{HOSPITAL_NAME}} (MOM, not yet drafted). This policy owns the clinical act of administering procedural sedation and of monitoring the patient. It does not write drug-storage, cupboard, register or destruction method. The Narcotic Drugs and Psychotropic Substances Act, 1985 is not inherited here as a wholesale storage statute; storage of controlled drugs waits for MOM.
- Who may practise as a registered medical practitioner is governed by the National Medical Commission Act, 2019 and State Medical Council registration, verified under the human resource policies of {{HOSPITAL_NAME}} (HRM, not yet drafted). This policy requires that a competent and trained person performs and a competent and trained person monitors sedation; it does not restate the credentialing file.
- Age-specific competency of those who care for children is governed by the paediatric and neonatal policy of {{HOSPITAL_NAME}} (COP.8.c). When a child is sedated, this document still owns the sedation method; COP.8 owns that the people who care for that child have age-specific competency. NICE guidance on sedation in children (chapter reference 50) may inform the hospital's paediatric sedation method; it is not pasted as a mandated protocol.
- Standard precautions, hand hygiene and injection safety in the procedure room are governed by the infection-prevention policy of {{HOSPITAL_NAME}} (HIC.2). Safe injection practice for the sedative follows HIC.2; this document does not rewrite it.
- HIC.4 mentions sedation only as part of ventilator care (minimising sedation, a sedation scale, daily interruption). Those hits are incidental ICU practices owned by HIC.4. They are not this document's procedural-sedation method.
- Reprocessing of reusable airway and monitoring equipment used during sedation is governed by the sterilisation policy of {{HOSPITAL_NAME}} (HIC.6).
- The medical record itself is governed by the information-management policies of {{HOSPITAL_NAME}} (IMS, not yet drafted). This policy owns the sedation-consent, intra-procedure monitoring and recovery content written into that record.
- Uniform identification at the point of care is governed by the uniform-care policy of {{HOSPITAL_NAME}} (COP.1). The patient is identified before sedation using those two identifiers.
- Cardio-pulmonary resuscitation, if it is required during sedation, is governed by the resuscitation policy of {{HOSPITAL_NAME}} (COP.3). This policy requires that resuscitation equipment and competent help are available where sedation is given; it does not write the resuscitation algorithm.$q$,
  $q${{HOSPITAL_NAME}} administers procedural sedation in a consistent manner, against written guidance that is the same in every location where sedation is given. A location that cannot meet that guidance does not sedate.

{{HOSPITAL_NAME}} obtains informed consent for administration of procedural sedation before the sedative is given.

{{HOSPITAL_NAME}} requires that a competent and trained person performs sedation and that a competent and trained person monitors the patient. The person monitoring is not the person performing the procedure, unless the hospital's written guidance records a defined exception and the monitoring is still continuous.

{{HOSPITAL_NAME}} monitors, during the procedure, at a minimum the heart rate, cardiac rhythm, respiratory rate, blood pressure, oxygen saturation and level of sedation, and records those observations.

{{HOSPITAL_NAME}} documents post-procedure monitoring and discharges the patient from the recovery area against objective criteria. A patient who is still sedated is not discharged because the list has moved on.

{{HOSPITAL_NAME}} treats sedation that has become general anaesthesia as anaesthesia, and hands that patient to the anaesthesia policy.$q$,
  array[
    $s$1. Procedural sedation administered in a consistent manner

Procedural sedation at {{HOSPITAL_NAME}} is administered in a consistent manner. Consistent means that the same written guidance governs every location in which a sedative is given to permit a procedure: who may sedate, where sedation may be given, which depths of sedation this hospital provides, what must be present in the room, how the patient is identified, how consent is confirmed before the drug, how monitoring is performed, how recovery is judged, and what happens when sedation deepens beyond the intended level. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask how sedation in endoscopy relates to sedation in the emergency area or in a procedure room, and the answer must be one written method, not a different habit in each room.

The locations in which procedural sedation may be administered, and the depths of sedation this hospital provides in each, are [Hospital to define — the locations in which procedural sedation may be administered, and the depths of sedation provided in each]. Depths are described in the language this hospital uses — commonly the American Society of Anesthesiologists continuum of minimal sedation, moderate sedation, deep sedation and general anaesthesia, which is the framework of the 2018 Practice Guidelines for Moderate Procedural Sedation and Analgesia (chapter reference 41) and of the European Society of Anaesthesiology and European Board of Anaesthesiology guidelines (chapter reference 22). This document does not mandate those societies' tables, does not print a drug-dose chart, and does not convert any named score into a required threshold. It requires that the hospital name the depths it actually provides. A location that provides only moderate sedation says so. Deep sedation that is expected to reach general anaesthesia is not performed under this policy; it is anaesthesia, and it is performed under the anaesthesia policy of {{HOSPITAL_NAME}}.

The reason consistency is the safety step is that sedation fails in the gap between rooms. A pulse oximeter that is required in theatre and forgotten in the endoscopy room, a second person who monitors in one suite and is "not needed" in another, a recovery rule that applies to day-care and is skipped in the emergency area because the trolley is wanted, are the same service delivered as three different services. The patient cannot tell which room's habit they have walked into. Written guidance that is hospital-wide is how the habit is replaced. The common error is a sedation SOP that lives in anaesthesia and is not used where most sedation actually happens — endoscopy, imaging, the emergency area, a minor-procedure room. That SOP is a file, not a consistent manner. The guidance this step requires is the guidance those rooms use.

Who may administer procedural sedation is a registered medical practitioner whose registration under the National Medical Commission Act, 2019 and the State Medical Council is current, and who has the competence the hospital has defined for the depth being given. The named roles, and the competence required for each depth and location, are [Hospital to define — who may administer procedural sedation, by role, depth and location]. This step states the statutory gate (a person who may not practise medicine here may not sedate here) and the hospital's further gate (registration is not, by itself, competence for deep sedation in a child). Human-resource procedures verify registration; this step uses that verification. Nursing and other registered practitioners who monitor do so within the competence at step 3; they do not become the person who administers unless the hospital's written guidance and their professional registration both allow it.

What must be present in a room before sedation starts — airway equipment, oxygen, suction, monitoring that can produce the parameters at step 4, resuscitation medicines, and a means of calling help — is [Hospital to define — what must be present in a room before procedural sedation starts]. A room missing any item on that list does not start sedation. Resuscitation, if it is required, follows the resuscitation policy of {{HOSPITAL_NAME}}; this step owns having the kit and the call for help in the room, not the algorithm.

The patient is identified, before the sedative is given, using the two identifiers of the uniform-care policy of {{HOSPITAL_NAME}}. Consent is confirmed under step 2. The intended depth, the procedure, and the person who will monitor are named before the drug is given. If at any point the patient's depth exceeds what this location is written to provide, sedation is stopped from deepening so far as is safe, help is called, and the patient is managed as an anaesthesia or resuscitation event under those policies. Stretching this policy to cover unplanned general anaesthesia is the failure this paragraph exists to stop.

Medicines used for sedation are selected and given as a clinical act under this guidance. Storage, cupboard, register, destruction and the controlled-drug account are owned by the medication policies of {{HOSPITAL_NAME}}. This step does not write them and does not cite the Narcotic Drugs and Psychotropic Substances Act as if this document were the storage policy.

The written procedural-sedation guidance, including locations, depths, roles, room list and the rule for unplanned deepening, is held at [Hospital to define — where the written procedural-sedation guidance is held].$s$,
    $s$2. Informed consent for administration of procedural sedation

Informed consent for administration of procedural sedation is obtained before the sedative is given. The method of explaining, recording and witnessing consent is governed by the patient-rights policies of {{HOSPITAL_NAME}}. This step owns that the sedation-specific consent is present, is for sedation as well as for the procedure where the two are separate, and is obtained before the drug.

How sedation consent is recorded — on the procedure consent, on a dedicated sedation consent, or another form — is [Hospital to define — how informed consent for procedural sedation is recorded]. A signature obtained after the drug, or a procedure consent that is silent on sedation when sedation is then given, is not consent for administration of procedural sedation.

When the patient is a child, consent is obtained from the person entitled to consent under the patient-rights policies; age-specific care remains under the paediatric policy of {{HOSPITAL_NAME}}. When the patient cannot consent, the patient-rights policies govern the substitute. This step still requires that the record shows sedation consent before the drug.$s$,
    $s$3. Competent and trained persons perform and monitor sedation

A competent and trained person performs sedation, and a competent and trained person monitors the patient. Competence is the combination of current professional registration and the hospital-defined training for the depth and location at step 1. Registration is verified under the human resource policies of {{HOSPITAL_NAME}}; this step uses that verification.

The person who monitors is [Hospital to define — who monitors the patient during procedural sedation, and whether that person may also perform the procedure]. The default in this document is that the person monitoring is not the person performing the procedure, because monitoring is continuous and a procedure that occupies both hands occupies the person who should be watching the patient. If the hospital records a defined exception, the exception is written, the depths and locations to which it applies are named, and monitoring remains continuous.

Training required beyond professional registration, and how it is recorded, is [Hospital to define — the training required to perform and to monitor procedural sedation, and how it is recorded]. A person without that training is not assigned.$s$,
    $s$4. Intra-procedure monitoring

Intra-procedure monitoring includes at a minimum the heart rate, cardiac rhythm, respiratory rate, blood pressure, oxygen saturation and level of sedation. All six are recorded. A pulse-oximetry trace without a recorded level of sedation is incomplete. A blood pressure taken once at the start and not again is incomplete unless the hospital's written guidance defines the interval and that interval is followed.

The interval at which each parameter is recorded, the scale used for level of sedation, and where the observations are written, are [Hospital to define — the recording interval for each intra-procedure parameter, the scale used for level of sedation, and where the observations are written]. This document does not print a numeric interval or mandate a named sedation scale. It requires that the six parameters are monitored and recorded.

Cardiac rhythm means a continuously displayed rhythm that can be observed; it does not require a full twelve-lead electrocardiogram unless the hospital's guidance says so for a defined patient group.

If a parameter cannot be obtained, the reason is recorded and the sedation does not continue as if the parameter were present, unless a documented clinical reason is recorded by the person administering sedation.$s$,
    $s$5. Post-procedure monitoring and objective discharge from recovery

Post-procedure monitoring is documented. The patient remains in a recovery area until discharge from that area is based on objective criteria. The recovery area may be a designated recovery room or a defined space in the procedure area; it is not a corridor and it is not an unmonitored waiting chair.

The observations continued in recovery, and the objective criteria against which the patient is discharged from the recovery area, are [Hospital to define — the post-procedure observations and the objective criteria for discharge from the recovery area]. This document does not mandate a named recovery score. It requires that the criteria are objective — a stated set of observations and conditions — and that a patient who does not meet them is not discharged from recovery because the next case is waiting.

The person who judges discharge against those criteria is [Hospital to define — who judges discharge from the recovery area against the objective criteria]. The judgement and the observations are recorded against the unique identification number.

A patient discharged from recovery who is not being admitted is still a patient of {{HOSPITAL_NAME}} until they leave the organisation under the discharge policy where that policy applies to the setting. This step owns only discharge from the recovery area.$s$,
    $s$6. Records, review and the order of operations

Every episode of procedural sedation is recorded against the unique identification number: the location and intended depth, the person who administered, the person who monitored, the consent before the drug, the six intra-procedure parameters, the recovery observations, and the objective-criteria discharge.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for procedural-sedation records] for: sedation given only in a named location against the written guidance; consent before the drug; a competent person administering and a competent person monitoring; all six intra-procedure parameters recorded; and recovery discharge against objective criteria rather than against the theatre list.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when an unplanned deepening, a sedation in an unnamed location, a missing monitoring parameter, or a recovery discharge that did not meet the criteria exposes a gap, or when the anaesthesia, medication, paediatric, resuscitation or patient-rights policies that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} administering procedural sedation only against written guidance, only in named locations, and only by persons who are registered and competent.

The person in charge of anaesthesia or the named sedation lead authors and keeps current the written procedural-sedation guidance at step 1, names the locations and depths, holds the room list, and holds the recovery criteria at step 5. The named lead is [Hospital to define — the named procedural-sedation lead].

The registered medical practitioner who administers sedation confirms identity, confirms consent before the drug, stays within the depth the location is written to provide, and hands an unplanned general anaesthesia to the anaesthesia or resuscitation policies.

The person who monitors records the six intra-procedure parameters and does not leave the patient unmonitored.

The person who judges discharge from recovery applies the objective criteria and records the judgement.

Clinicians who obtain consent do so before the sedative is given, using the patient-rights method.

The quality or accreditation coordinator audits the records at step 6 and reports findings to the head of the institution.

All staff are expected to treat sedation in an unnamed location, a missing monitor, consent after the drug, and discharge from recovery of a patient who does not meet the criteria, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.9.
- National Medical Commission Act, 2019 and State Medical Council registration — insofar as they govern who may administer procedural sedation.
- Practice Guidelines for Moderate Procedural Sedation and Analgesia 2018, Anesthesiology, 128(3), 437-479 — chapter reference 41; used as a recognised framework for the continuum of sedation and for the principle of consistent practice; this document does not import that guideline's drug tables or numeric thresholds.
- Hinkelbein, J., et al. (2017). European Society of Anaesthesiology and European Board of Anaesthesiology guidelines for procedural sedation and analgesia in adults. European Journal of Anaesthesiology — chapter reference 22; a recognised framework the hospital may use; not mandated as the only method.
- Roback, M., et al. (2018). Tracking and Reporting Outcomes Of Procedural Sedation (TROOPS). British Journal of Anaesthesia, 120(1), 164-172 — chapter reference 46; a recognised quality-improvement tool the hospital may use; not mandated.
- Sedation in children and young people, National Institute for Health and Care Excellence (NICE CG112) — chapter reference 50; may inform paediatric sedation where children are sedated; not pasted as a mandated protocol. Age-specific competency of those who care for children remains under the paediatric policy of {{HOSPITAL_NAME}}.
- Internal documents of {{HOSPITAL_NAME}}: the written procedural-sedation guidance (locations, depths, roles, room list); the sedation-consent record; the intra-procedure monitoring record; the recovery observations and objective discharge criteria; the anaesthesia policy; the procedures-and-operation-theatre policy; the patient-rights policies; the medication policies; the paediatric policy; the resuscitation policy; the infection-prevention and sterilisation policies; and the human resource policies.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every location in which procedural sedation is administered; the operation theatre and recovery; the emergency area; day-care; endoscopy and other procedure rooms; imaging where sedation is given; nursing administration; the named procedural-sedation lead; and anaesthesia.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The written sedation guidance, the room list, the monitoring record and the recovery criteria — the working documents this policy requires — are held in every location that sedates.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

ASA — American Society of Anesthesiologists
ESA — European Society of Anaesthesiology
NICE — National Institute for Health and Care Excellence
NMC — National Medical Commission
TROOPS — Tracking and Reporting Outcomes Of Procedural Sedation

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the National Medical Commission Act, 2019, insofar as it governs who may administer procedural sedation. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "COP.9.a", "requirement": "Procedural sedation is administered in a consistent manner.", "steps": "Steps 1, 6", "evidence": "The written procedural-sedation guidance used in every location that sedates, covering who may sedate, where sedation may be given, which depths this hospital provides, what must be present in the room, identification before the drug, consent confirmation, monitoring, recovery, and the rule when sedation deepens beyond the intended level, showing one hospital-wide method rather than a different habit in endoscopy, the emergency area, imaging and a minor-procedure room, and rather than an anaesthesia-department SOP that is not used where most sedation happens; the named locations and the depths provided in each, using this hospital's language for depth (and, where the hospital uses it, the ASA continuum as a framework) without a pasted drug-dose table, and showing that deep sedation expected to reach general anaesthesia is performed under the anaesthesia policy, not under a stretched reading of this document; the named roles who may administer, by depth and location, showing current registration under the National Medical Commission Act, 2019 and State Medical Council as the statutory gate and the hospital-defined competence as the further gate; the room list of what must be present before sedation starts (airway equipment, oxygen, suction, monitoring that can produce the six parameters, resuscitation medicines, a means of calling help) and records of a room that was missing an item not starting sedation; sample episodes against the unique identification number showing identity checked with two identifiers, intended depth and monitoring person named before the drug, and unplanned deepening handed to anaesthesia or resuscitation rather than absorbed into this policy; the recorded forward reference that storage and the controlled-drug account are owned by the medication policies and that the Narcotic Drugs and Psychotropic Substances Act is not treated as this document's storage statute; the location where the written guidance is held; induction or briefing records showing staff in every named sedation location have been shown the same guidance; the audit sample at step 6 of sedation given only in a named location against that guidance", "responsible": "Named procedural-sedation lead holds the written guidance, locations, depths and room list; registered medical practitioners administer only against that guidance; head of the institution is accountable that unnamed locations do not sedate; quality or accreditation coordinator audits"}, {"oe_code": "COP.9.b", "requirement": "Informed consent for administration of procedural sedation is obtained.", "steps": "Steps 2, 1, 6", "evidence": "The written method of recording sedation consent (procedure consent, dedicated sedation consent, or other form); sample records showing consent present before the sedative was given, including where the patient was a child or could not consent; records showing a signature after the drug, or a procedure consent silent on sedation, was not treated as sedation consent; the recorded division that patient-rights policies own the consent method and this policy owns that sedation consent happened before the drug", "responsible": "Clinician obtaining consent records it before the drug; person administering sedation confirms it is present; patient-rights policies own the method; quality or accreditation coordinator audits"}, {"oe_code": "COP.9.c", "requirement": "Competent and trained persons perform and monitor sedation.", "steps": "Steps 3, 1, 6", "evidence": "The named roles that perform and that monitor, with current professional registration used from human-resource verification; the training required beyond registration and how it is recorded; the written rule on whether the monitor may also perform the procedure, including any defined exception; assignment records showing a person without the required training was not assigned", "responsible": "Named sedation lead holds the competence rules; human resource function verifies registration; the administering and monitoring persons apply them; quality or accreditation coordinator audits"}, {"oe_code": "COP.9.d", "requirement": "Intra-procedure monitoring includes at a minimum the heart rate, cardiac rhythm, respiratory rate, blood pressure, oxygen saturation, and level of sedation.", "steps": "Steps 4, 6", "evidence": "The written recording interval, the scale used for level of sedation, and where observations are written; sample intra-procedure records showing all six parameters present (heart rate, cardiac rhythm, respiratory rate, blood pressure, oxygen saturation, level of sedation); records of a parameter that could not be obtained, with the reason and the decision; the audit sample at step 6 of all six parameters recorded", "responsible": "Person monitoring records the six parameters; person administering sedation does not continue as if a missing parameter were present without a documented reason; quality or accreditation coordinator audits"}, {"oe_code": "COP.9.e", "requirement": "Post procedure monitoring is documented, and patients are discharged from the recovery area based on objective criteria.", "steps": "Steps 5, 6", "evidence": "The written post-procedure observations and objective criteria for discharge from the recovery area; the named person who judges discharge; sample recovery records showing observations documented and discharge against those criteria rather than against the theatre list; the recorded distinction that this step owns discharge from recovery, not discharge from the organisation", "responsible": "Person judging recovery discharge applies the objective criteria and records the judgement; named sedation lead holds the criteria; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. COP.9 standard text and all five OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 2 Care of Patients, printed page 66 (PDF page index 72). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: COP.9.a Commitment, COP.9.b Commitment, COP.9.c Commitment, COP.9.d Commitment, COP.9.e Commitment.
   ONE OE CARRIES THE ASTERISK -- COP.9.a. The draft builds one deep block (step 1 for a). COP.9.b, COP.9.c, COP.9.d and COP.9.e are unasterisked and are correspondingly Tier 2.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the COP.9 page read directly from the extracted page text, and the committed asterisk file. COP.9 was not among the 14 mismatches of the 2026-08-10 audit.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. ONE OF FIVE OEs IS TIER 1. Tier 1: COP.9.a only -- procedure step 1 carries the reasoning (why consistency is the safety step, why an anaesthesia SOP unused in endoscopy is not a consistent manner, why unplanned general anaesthesia is not absorbed here, why NDPS is not this document's storage statute). Tier 2: COP.9.b (step 2), COP.9.c (step 3), COP.9.d (step 4), COP.9.e (step 5) -- requirement and method without extended rationale. Reviewer to note the shallower treatment of b-e is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of COP.9.a against the approved HIC.1-HIC.6 masters and the AAC.1-AAC.8 drafts. Search terms: sedation, sedate, procedural sedation, recovery, anaesthesia, anesthesia.
   COP.10 -- CRITICAL DIVISION, stated in both this Scope and step 1. Sedation is not general anaesthesia. This document does not write the anaesthesia policy. COP.10 does not write this sedation policy. Unplanned deepening that is general anaesthesia is handed to COP.10 / COP.3. Flagged for the COP.10 drafter to mirror.
   COP.11 -- sibling, not yet drafted. COP.11 owns the procedure, site-marking, checklist and operation note. This owns the sedation given so the procedure can be performed. Stated in Scope.
   PRE (undrafted) -- owns consent METHOD generally. COP.9.b owns that sedation consent is obtained before the drug. Stated in Scope and step 2.
   MOM (undrafted) -- owns medication process including controlled-drug STORAGE. This document forward-references MOM and does NOT write storage, cupboard, register or destruction, and does NOT inherit NDPS as a wholesale storage statute. Stated in Scope and step 1.
   HIC.4 -- "sedation" hits are ICU ventilator-care practices (minimise sedation, scale, daily interruption). Incidental. Not this document. Stated in Scope. Not added to the reconciliation list.
   HIC.2 -- safe injection of the sedative. Applied, not rewritten.
   HIC.6 -- reprocessing of airway and monitoring equipment used in sedation. Not restated.
   COP.8 -- age-specific competency when a child is sedated; NICE CG112 may inform, not mandate. This still owns the sedation method.
   COP.1 -- two identifiers before the drug.
   COP.3 -- resuscitation algorithm if required; this owns kit-in-the-room.
3. FORWARD REFERENCES: MOM drug storage; PRE consent method; HRM credentialing; IMS record; COP.10 anaesthesia (drafted in this same pass); COP.11 surgery (sibling, not yet in this agent's files). Each is a deliberate boundary.
4. T2 QUICK CHECK: COP.9.b vs PRE -- flagged in Scope. COP.9.c vs NMC/HRM -- flagged. COP.9.d lists the six PDF parameters and does not add invented ones. COP.9.e recovery vs COP.10.f post-anaesthesia recovery -- sibling recovery processes; this is sedation recovery, COP.10 is anaesthesia recovery. Flagged in COP.10's Scope as well. Nothing added to the HIC reconciliation list.

STATUTORY AND EXTERNAL FACTS
5. National Medical Commission Act, 2019 -- cited insofar as it governs who may administer procedural sedation (a person who may not practise medicine here may not sedate here). No section number. Hospital-defined competence is additional, not a substitute for registration. Indian Nursing Council Act is not named in P2; nurses who monitor do so within step 3 competence, and P2 stays NMC as instructed.
6. NDPS Act 1985 and Drugs and Cosmetics Act drug-storage rules are NOT named in P2 and are not written as storage method. Forward-ref MOM. The build must not inherit NDPS as a wholesale statute.
7. ASA 2018 moderate-sedation guidelines (chapter ref 41) and ESA/EBA 2017 (chapter ref 22) -- used as recognised frameworks for the continuum and for consistent practice. NOT used as a drug table, a mandatory score, or a numeric monitoring interval.
8. TROOPS (chapter ref 46) -- named as a QI tool the hospital may use; not mandated.
9. NICE CG112 (chapter ref 50) -- may inform paediatric sedation; not pasted. COP.8 owns age-specific competency.
10. NO NUMBERS ARE STATED as requirements -- no drug doses, no SpO2 cut-offs, no recording-interval minutes, no recovery-score thresholds, no fasting hours. Every such value is [Hospital to define]. Consistent with the no-numbers default.
11. Bio-Medical Waste Management Rules, 2016, Food Safety and Standards Act, 2006, and Clinical Establishments Act, 2010 are NOT named in P2. CEA is not defaulted from AAC.

EDITORIAL POSITIONS TAKEN
12. Step 1's rule that an anaesthesia SOP unused where most sedation happens is not a consistent manner, and that unplanned general anaesthesia is not absorbed into this policy, are editorial positions.
13. Step 1's refusal to write controlled-drug storage, and the refusal to cite NDPS as this document's storage statute, are editorial positions required by the owner's instruction.
14. Step 3's default that the monitor is not the person performing the procedure, with a written exception permitted, is an editorial position; the standard requires competent persons to perform and monitor, not this separation.
15. Step 4's reading that cardiac rhythm means a continuously displayed rhythm, not a mandated twelve-lead, is an editorial position.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
16. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the National Medical Commission Act, 2019 insofar as it governs who may administer procedural sedation -- the statute this document's References actually rely on. It does NOT name NDPS, BMW Rules 2016, FSS Act 2006, or CEA 2010. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- Anaesthesia assessment, plan, intra-operative anaesthesia monitoring, post-anaesthesia recovery -- COP.10.
- Surgical procedure, WHO checklist, site-marking, operation notes -- COP.11.
- General consent method -- PRE.
- Controlled-drug storage, cupboard, register, destruction -- MOM.
- ICU sedation for ventilation -- HIC.4.
- Resuscitation algorithm -- COP.3.
- Age-specific paediatric competency method -- COP.8.c.
- Injection-safety technique -- HIC.2.
- Reprocessing of airway equipment -- HIC.6.
- A numbered drug protocol, fasting protocol, or mandatory Aldrete/other recovery score.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 16 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 14 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 16; a search for "Hospital to define" without brackets finds all 16, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: locations and depths of procedural sedation; who may administer by role, depth and location; what must be present in a room before sedation starts; where the written guidance is held; how sedation consent is recorded; who monitors and whether that person may also perform the procedure; training required to perform and monitor; recording interval, sedation scale and where observations are written; post-procedure observations and objective recovery-discharge criteria; who judges discharge from recovery; the named procedural-sedation lead; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
