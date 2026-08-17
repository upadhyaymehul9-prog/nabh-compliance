-- COP.1 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 2, printed page 61
-- (PDF page index 67). Levels: a Core, b Commitment, c Achievement, d Commitment, e Excellence.
-- TWO OEs CARRY THE ASTERISK -- COP.1.d, COP.1.e. COP.1.a is Core but unasterisked (Tier 2).
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
  'COP.1',
  'COP',
  array['COP.1.a', 'COP.1.b', 'COP.1.c', 'COP.1.d', 'COP.1.e'],
  $q$Uniform Care Across Settings and Telemedicine$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} gives the same standard of care for a given clinical condition wherever that care is provided, and how a telemedicine facility, if one is provided, is run from written guidance rather than from informal remote advice.

The chapter intent is that the organisation provides uniform care to all patients in various settings — out-patient units, day-care, in-patient units including critical care, procedure rooms and the operation theatre — and that when similar care is provided in those settings, care delivery is uniform. A protocol that lives in one unit's folder and is unknown in the next is not uniform care. A WhatsApp message that is treated as a consultation without identity, consent or a record is not a telemedicine facility.

This document is the process that makes the intent operational at the point of care: two identifiers before an act of care, care that stays inside the laws that actually apply to the services this hospital has defined, evidence-based protocols that staff can find, those protocols applied the same way in every setting where that care is given, and telemedicine that is either provided under written guidance or is stated in writing not to be provided.$q$,
  $q$This policy applies to every setting in which {{HOSPITAL_NAME}} provides care: the out-patient department, day-care, every in-patient ward, intensive or high-dependency areas where they exist, the emergency area, procedure rooms, the operation theatre and recovery, and any location from which a telemedicine consultation is given or received. It binds the staff who identify patients at the point of care, the clinicians who adopt and apply clinical protocols, the heads of the settings in which similar care is given, and any registered medical practitioner who provides a telemedicine consultation under this hospital's name.

It covers: the uniform process for identifying patients using at least two identifiers; care provided in consonance with applicable laws and regulations; adoption of evidence-based clinical practice guidelines and/or clinical protocols; uniform care delivery for a given clinical condition when similar care is provided in more than one setting; and a telemedicine facility provided safely and securely based on written guidance, including a written statement that no such facility is provided if that is the hospital's decision.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Generation of the unique identification number at registration is governed by the registration, admission and transfer policy of {{HOSPITAL_NAME}} (AAC.2.b). This policy owns the use of two identifiers at the point of care. The unique identification number is one identifier once it has been issued; this document does not generate it.
- The written definition of the healthcare services, the department scopes of services, and the public display of those services are governed by the definition-and-display policy of {{HOSPITAL_NAME}} (AAC.1). This policy makes care for a given condition the same in every setting in which that care is actually provided; it does not rewrite the service directory.
- Initial assessment, the care plan, reassessment and early-warning recognition are governed by the assessment policy of {{HOSPITAL_NAME}} (AAC.3). Assessment is not a uniform-care protocol. This policy owns the clinical protocols that guide care after the patient has been assessed, and that those protocols do not contradict each other by setting.
- Specimen identity before collection is applied under the laboratory-services policy of {{HOSPITAL_NAME}} (AAC.4) using the two-identifier process this document owns. This policy does not rewrite the specimen pathway.
- Standardised handover method and internal transfer are governed by the continuity-of-care policy of {{HOSPITAL_NAME}} (AAC.7). This policy owns that the care being handed over was delivered to the same standard in the sending setting as it would have been in the receiving setting.
- Nursing documentation of care in the patient record, assignment of nursing care, nursing equipment and nursing clinical practice guidelines are governed by the nursing-care policy of {{HOSPITAL_NAME}} (COP.4). This policy's evidence-based clinical protocols (COP.1.c) are hospital-wide clinical standards; they are not the nursing clinical practice guidelines.
- Emergency clinical protocols, ambulance operation and the emergency area itself are governed by the emergency-care policy of {{HOSPITAL_NAME}} (COP.2). Cardio-pulmonary resuscitation is governed by the resuscitation policy (COP.3). Care in intensive and high-dependency units is governed by the critical-care policy (COP.6). Uniform care under this document requires that those settings apply the same condition-specific standard; it does not write their operational protocols.
- Hand hygiene, personal protective equipment, transmission-based precautions and injection safety are governed by the infection-control policies of {{HOSPITAL_NAME}} (HIC.2). Uniform care does not rewrite them.
- The medical record itself — its structure, retention and confidentiality — is governed by the information-management policies of {{HOSPITAL_NAME}}. This policy owns the identification process used at the point of care, the clinical-protocol content applied, and the telemedicine record filed against the unique identification number.$q$,
  $q${{HOSPITAL_NAME}} identifies every patient, before an act of care, by a uniform process that uses at least two identifiers. A bed number, a room number or a tray position is not an identifier.

{{HOSPITAL_NAME}} provides care in consonance with the laws and regulations that apply to the services it has defined. Those laws are named by this hospital; they are not inherited from another standard's list.

{{HOSPITAL_NAME}} adopts evidence-based clinical practice guidelines and/or clinical protocols to guide uniform patient care. The protocols in use are this hospital's list.

{{HOSPITAL_NAME}} delivers care for a given clinical condition to the same standard when similar care is provided in more than one setting. A setting is not a reason to vary the protocol.

{{HOSPITAL_NAME}} provides a telemedicine facility, if it provides one, safely and securely based on written guidance consistent with the Telemedicine Practice Guidelines, 2020. If it does not provide a telemedicine facility, that decision is written, and informal remote advice is not treated as one.$q$,
  array[
    $s$1. Two identifiers at the point of care

{{HOSPITAL_NAME}} has a uniform process for identification of patients and, at a minimum, uses two identifiers. The process is the same in every setting listed in the Scope.

The two identifiers used at {{HOSPITAL_NAME}} are [Hospital to define — the two identifiers used at the point of care]. A typical pair is the patient's name and the unique identification number issued at registration under the registration, admission and transfer policy of {{HOSPITAL_NAME}}. Another pair may be chosen. Bed number, room number, cubicle, trolley or tray position is not an identifier: those name a location, not a person, and a location can be occupied by someone else.

The unique identification number is generated at registration (AAC.2.b). This step uses that number as an identifier once it exists. It does not issue the number. An unidentified emergency patient is identified under the registration mechanism, including the emergency route that does not delay care for administrative completeness; two identifiers are then used as soon as they exist.

Staff confirm both identifiers against the patient or the patient's identifier band or equivalent, and against the record, requisition or order, before medication, a procedure, a specimen collection, a transfusion, a transfer, or any other act of care. How the confirmation is recorded is [Hospital to define — how confirmation of the two identifiers is recorded].

This is Core: it will be assessed at every visit. It is not asterisked. The depth of this step is the requirement and the method.$s$,
    $s$2. Care in consonance with applicable laws and regulations

Care is provided in consonance with applicable laws and regulations. Applicable means the laws that actually govern the services {{HOSPITAL_NAME}} has defined under the definition-and-display policy, not a borrowed list from another chapter.

The written list of laws and regulations this hospital treats as applicable to the care it provides, and where that list is held, is [Hospital to define — the applicable laws and regulations for the care this hospital provides, and where that list is held]. This document does not print a statutory catalogue. It does not name the Bio-Medical Waste Management Rules, 2016 or the Food Safety and Standards Act, 2006; those are owned by the infection-control support-services policy where they apply. It does not default to the Clinical Establishments (Registration and Regulation) Act, 2010.

When a service is added, suspended or withdrawn under the definition-and-display policy, the applicable-law list is reviewed for that service.$s$,
    $s$3. Evidence-based clinical practice guidelines and clinical protocols

{{HOSPITAL_NAME}} adopts evidence-based clinical practice guidelines and/or clinical protocols to guide uniform patient care.

The protocols and guidelines in current use, the conditions they cover, and where they are held, are [Hospital to define — the evidence-based clinical protocols in use, the conditions they cover, and where they are held]. Ministry of Health and Family Welfare Standard Treatment Guidelines, as published on the clinical establishments portal (chapter reference 30 of this chapter), and other recognised evidence-based sources, are acceptable origins. They are not the only origins, and they are not imported as a numbered local protocol until this hospital has adopted them.

A protocol is dated, version-controlled, and named as in use or withdrawn. A withdrawn protocol is removed from the points of use. Nursing clinical practice guidelines are owned by the nursing-care policy of {{HOSPITAL_NAME}} (COP.4.d) and are not this list.

This step adopts the protocols. Step 4 requires that, once adopted, they are applied the same way in every setting where that care is given.$s$,
    $s$4. Uniform care for a given condition across settings

Care delivery is uniform for a given clinical condition when similar care is provided in more than one setting. This step is the documented-evidence anchor of a requirement the standard asterisks: an assessor will ask how a patient with the same condition is cared for in the out-patient department, on the ward, in the operation theatre, in intensive care and in the emergency area, and the answer must be the same protocol applied in each setting that actually provides that care, not a claim that "we all know how to treat it."

Uniform does not mean identical intensity. A patient with the same condition may need a higher level of monitoring in intensive care than in the out-patient department. Uniform means the condition-specific standard does not contradict itself by location: the same indications, the same contraindications, the same safety checks, and the same record of what was done. Intensity may vary with clinical need. The protocol may not.

The reason this step exists as written guidance, rather than as professional habit, is that setting is a powerful source of unjustified variation. A protocol that is known on one ward and unknown in day-care, a consultant's personal practice that differs between the out-patient clinic and the theatre, or an emergency-area shortcut that would not be accepted on the ward, produces two standards for one condition. The patient who moves between those settings — or who happens to present in the setting with the weaker habit — receives a different care for no clinical reason. That is the failure this step is written to stop.

The common error is a protocol folder in one unit and a different, undated, personal or photocopied version in another, or a protocol that was adopted at step 3 and then applied only where the author works. The control is a single current version, held where the care is given, and used in every setting listed against that condition. A second version in a drawer is a second standard.

The settings in which similar care is provided for each adopted protocol, and the current version in use in each of those settings, are [Hospital to define — for each adopted clinical protocol, the settings in which that care is provided and the current version in use in each]. The definition-and-display policy of {{HOSPITAL_NAME}} states which services exist; this step states that, for a given condition, the care those services give does not vary by the room it is given in.

Emergency clinical protocols, resuscitation, and intensive-care operational rules remain in the emergency-care, resuscitation and critical-care policies of {{HOSPITAL_NAME}}. This step requires that those settings do not run a contradictory condition-specific standard. It does not write their operational documents. Infection-control methods remain in HIC.2. Assessment remains in AAC.3. Nursing clinical practice guidelines remain in COP.4.

When a protocol is revised, every setting listed against it receives the new version and withdraws the old one on the same date. A revision that reaches the ward and not the emergency area is a break in uniform care.

How staff in each setting are shown the current version, and how a contradiction between settings is reported, are [Hospital to define — how staff in each setting are shown the current protocol version, and how a contradiction between settings is reported].$s$,
    $s$5. Telemedicine facility based on written guidance

A telemedicine facility, if {{HOSPITAL_NAME}} provides one, is provided safely and securely based on written guidance. This step is the documented-evidence anchor of a requirement the standard places at Excellence and asterisks. An assessor will ask for the written guidance, not for an assurance that doctors sometimes speak to patients on the telephone.

Whether {{HOSPITAL_NAME}} provides a telemedicine facility is [Hospital to define — whether a telemedicine facility is provided]. If it is not provided, that decision is written here and at the points of contact, and informal remote advice — a WhatsApp message, an unsigned prescription sent by image, a telephone instruction with no record — is not a telemedicine facility and is not permitted as a substitute for one. The reason for writing the negative is the same as the reason for writing the positive: without a document, remote advice happens anyway, without identity, without consent and without a record, and the hospital discovers it only when something has gone wrong.

If a facility is provided, the written guidance is consistent with the Telemedicine Practice Guidelines, 2020 issued by the Ministry of Health and Family Welfare and adopted by the National Medical Commission (chapter reference 4 of this chapter informs the Indian practice context; the Guidelines are the professional rule this step follows). This document does not reprint the Guidelines. It requires that the hospital's guidance covers, in this hospital's words, the points the Guidelines make operational:

- who may provide a telemedicine consultation under this hospital's name — a registered medical practitioner, with the professional registration that the National Medical Commission Act, 2019 already requires; other staff do not issue a telemedicine prescription;
- how the practitioner and the patient are identified, using the two-identifier process at step 1 for the patient, and how the practitioner's name and registration are made known to the patient;
- how informed consent for the telemedicine consultation is obtained and recorded;
- which modes of communication are used — [Hospital to define — the telemedicine modes and the platform used];
- which services and conditions may be provided by telemedicine, and which may not, matching the service directory;
- how a prescription, if one is issued, is produced, transmitted and filed, within the limits the Guidelines set; this document does not print a drug list;
- how an emergency presenting on a remote consultation is handled: first-aid or immediate advice, and prompt direction to in-person care, not an attempt to finish the emergency on the call;
- how the consultation is recorded against the unique identification number and filed in the patient record;
- how privacy and security of the consultation and its record are kept — [Hospital to define — how privacy and security of a telemedicine consultation and its record are kept].

The reason written guidance is the control, rather than the practitioner's judgement on the day, is that telemedicine removes the ordinary safeguards of a room: the patient may not be who they say they are, the practitioner may not be the hospital's, the conversation may not be filed, and an emergency may be under-treated because it arrived as a message. The Guidelines exist because those failures had already happened in Indian practice. A hospital that provides the facility without the guidance is running the failures back in.

The common error is to treat every telephone call or messaging-app exchange as if it were a documented telemedicine consultation, or to treat a documented consultation as if the ordinary rules of identity, consent, prescription and record did not apply because the patient was not in the building. Both are forbidden here. Either there is a facility, under this guidance, or there is not, and there is no third category of unofficial remote care.

The written telemedicine guidance, the named practitioners who may provide it, and where the guidance is held, are [Hospital to define — the written telemedicine guidance, the named practitioners who may provide it, and where the guidance is held].

Registration of a telemedicine patient, and generation of the unique identification number, remain AAC.2. This step requires that a telemedicine episode is a registered episode. It does not invent a second identity system.$s$,
    $s$6. Records, review and the order of operations

Every confirmation of two identifiers, every current clinical protocol and the settings in which it is used, every contradiction reported between settings, and every telemedicine consultation (or the written decision that none is provided) is recorded against the unique identification number where a patient is involved, and is retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for uniform-care and telemedicine records] for: two identifiers used at the point of care rather than a bed number; the applicable-law list matching the current service directory; adopted protocols that are the version in use; the same current version present in every setting listed against a condition; and telemedicine consultations that show identity, consent, a record and a registered unique identification number, or a written decision that no facility is provided and no unofficial remote care in the sample.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a misidentification, a contradiction between settings, or an unofficial remote consultation exposes a gap, or when the registration, definition-and-display, assessment, nursing-care or information-management policies that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} identifying patients with two identifiers, for care that stays inside the laws that apply to its defined services, for adopted protocols that are actually used, for those protocols not contradicting each other by setting, and for telemedicine that is either guided in writing or not provided.

Heads of the out-patient department, day-care, in-patient wards, the emergency area, the operation theatre and intensive or high-dependency areas keep the current protocol version in their setting, withdraw the previous version on the same date as every other setting, and report a contradiction.

Clinicians apply the two-identifier process before an act of care, apply the adopted protocol for the condition, and do not run a personal version that differs by setting. Registered medical practitioners who provide telemedicine do so only under the written guidance at step 5.

Nursing staff apply the two-identifier process and the clinical protocols; nursing clinical practice guidelines remain in the nursing-care policy.

The person responsible for administration maintains the applicable-law list against the service directory and, if telemedicine is provided, the platform and privacy arrangement at step 5.

The quality or accreditation coordinator audits the records at step 6 and reports findings to the head of the institution.

All staff are expected to treat a misidentification, a second protocol for the same condition in another setting, and unofficial remote advice as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.1.
- Telemedicine Practice Guidelines, 2020, issued by the Ministry of Health and Family Welfare and adopted by the National Medical Commission — the professional rule for a telemedicine facility under COP.1.e. This document does not reprint the Guidelines and does not print a drug list.
- National Medical Commission Act, 2019 — insofar as only a registered medical practitioner may provide a telemedicine consultation under this hospital's name.
- Ateriya, N., Saraf, A., Meshram, V. and Setia, P. (2018), Telemedicine and virtual consultation: The Indian perspective, The National Medical Journal of India, 31(4), 215 — chapter reference 4; used as the Indian practice context, not as a protocol.
- Ministry of Health and Family Welfare, Government of India, Standard Treatment Guidelines (speciality-wise), as published on the clinical establishments portal — chapter reference 30; an acceptable origin for evidence-based protocols the hospital may adopt at step 3, not a mandated set.
- Montori, V. M., Brito, J. P. and Murad, M. H. (2013), The Optimal Practice of Evidence-Based Medicine, JAMA, 310(23), 2503 — chapter reference 32; informs that adopted protocols are evidence-based, not that a named tool is required.
- Rotter, T. et al. (2010), Clinical pathways: effects on professional practice, patient outcomes, length of stay and hospital costs, Cochrane Database of Systematic Reviews — chapter reference 47; informs that a written pathway can support uniform care; this document does not mandate a named pathway tool.
- Internal documents of {{HOSPITAL_NAME}}: the two-identifier process; the applicable-law list; the adopted clinical protocols and the settings in which each is used; the telemedicine written guidance or the written decision that no facility is provided; the registration, admission and transfer policy; the definition-and-display policy; the assessment policy; the laboratory-services policy; the continuity-of-care policy; the nursing-care policy; the emergency-care, resuscitation and critical-care policies; the infection-control policies; and the information-management policies.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: the out-patient department; day-care; every in-patient ward; the emergency area; the operation theatre and recovery; intensive or high-dependency areas where they exist; nursing administration; every head of department; and, if a telemedicine facility is provided, the practitioners named at step 5.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The two-identifier process, the current clinical protocols and the telemedicine guidance — the working documents this policy requires — are held in every setting that uses them.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

UID — Unique Identification Number
CPG — Clinical Practice Guideline
EBM — Evidence-Based Medicine
RMP — Registered Medical Practitioner
STG — Standard Treatment Guideline

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the Telemedicine Practice Guidelines, 2020 issued by the Ministry of Health and Family Welfare and adopted by the National Medical Commission, insofar as a telemedicine facility is provided. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "COP.1.a", "requirement": "The organization has a uniform process for identification of patients and at a minimum, uses two identifiers", "steps": "Steps 1, 6", "evidence": "The written two-identifier process naming the pair in use; sample point-of-care records showing both identifiers confirmed before medication, a procedure or specimen collection rather than a bed or room number; records distinguishable from AAC.2 generation of the unique identification number; the audit sample at step 6 of identifiers used at the point of care", "responsible": "Clinical and nursing staff confirm two identifiers before an act of care; registration and admission policy owns generation of the unique identification number; quality or accreditation coordinator audits"}, {"oe_code": "COP.1.b", "requirement": "Care shall be provided in consonance with applicable laws and regulations", "steps": "Steps 2, 6", "evidence": "The written list of laws and regulations this hospital treats as applicable to the care it provides, aligned to the current service directory rather than inherited from another chapter; the record of review when a service is added, suspended or withdrawn; the location where the list is held; the audit sample at step 6 of the list against the directory", "responsible": "Administration maintains the applicable-law list against the service directory; head of the institution is accountable that care stays inside those laws; quality or accreditation coordinator audits"}, {"oe_code": "COP.1.c", "requirement": "The organization adopts evidence-based clinical practice guidelines and/or clinical protocols to guide uniform patient care", "steps": "Steps 3, 4, 6", "evidence": "The written list of evidence-based clinical protocols in current use, the conditions they cover, dated and version-controlled; records showing a withdrawn protocol removed from points of use; distinction from nursing clinical practice guidelines owned by COP.4; the location where the protocols are held; the audit sample at step 6 of adopted protocols being the version in use", "responsible": "Clinicians and heads of department adopt and keep current the protocol list; nursing-care policy owns nursing CPGs; quality or accreditation coordinator audits"}, {"oe_code": "COP.1.d", "requirement": "Care delivery is uniform for a given clinical condition when similar care is provided in more than one setting", "steps": "Steps 4, 3, 6", "evidence": "The written map, for each adopted clinical protocol, of the settings in which that care is provided and the current version in use in each setting, showing a single current version rather than a unit-level copy that differs; records of protocol revision in which every listed setting received the new version and withdrew the old version on the same date; sample case records from at least two settings for the same condition showing the same condition-specific standard applied (indications, contraindications, safety checks, record of what was done) with intensity varying only by clinical need and not by location; the written method by which staff in each setting are shown the current version; records of any contradiction between settings reported and the action taken, rather than a second protocol left in a drawer; briefing or induction records showing staff in the out-patient department, day-care, in-patient wards, emergency area, operation theatre and intensive or high-dependency areas, where those settings provide the care, have been shown the current version; the stated division that AAC.1 owns which services exist, AAC.3 owns assessment, COP.4 owns nursing CPGs, COP.2/COP.3/COP.6 own emergency, resuscitation and intensive-care operational protocols, and HIC.2 owns infection-control methods, none of which is rewritten here; the audit sample at step 6 of the same current version present in every setting listed against a condition, and of no second undated or personal version found in a unit folder", "responsible": "Heads of each setting keep the current version and withdraw the previous one on the same date; clinicians apply the adopted protocol and do not run a personal version that differs by setting; quality or accreditation coordinator audits the match between settings"}, {"oe_code": "COP.1.e", "requirement": "Telemedicine facility is provided safely and securely based on written guidance", "steps": "Steps 5, 1, 6", "evidence": "The written decision whether a telemedicine facility is provided; if it is not, the written statement at the points of contact and sample records showing unofficial remote advice (messaging-app prescription, unsigned image, undocumented telephone instruction) was not treated as a consultation; if it is, the written telemedicine guidance consistent with the Telemedicine Practice Guidelines, 2020 covering who may provide a consultation (registered medical practitioner under the National Medical Commission Act, 2019), how practitioner and patient are identified using the two-identifier process, how informed consent is obtained and recorded, the modes and platform, which services may and may not be provided remotely against the service directory, how a prescription is produced, transmitted and filed without this document printing a drug list, how an emergency on a remote consultation is given first-aid or immediate advice and directed to in-person care, how the consultation is recorded against the unique identification number, and how privacy and security of the consultation and its record are kept; the named practitioners who may provide telemedicine and the location of the guidance; sample telemedicine records showing identity of both parties, consent, a registered unique identification number issued under AAC.2 rather than a second identity system, a filed note, and, where a prescription was issued, the transmission and filing; records of any emergency presenting remotely that was directed to in-person care rather than completed on the call; briefing records of the named practitioners; the audit sample at step 6 of telemedicine consultations that show identity, consent, a record and a unique identification number, or of the written decision that no facility is provided with no unofficial remote care in the sample", "responsible": "Head of the institution decides whether a facility is provided; named registered medical practitioners provide consultations only under the written guidance; administration holds the platform and privacy arrangement; registration and admission policy owns the unique identification number; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. COP.1 standard text and all five OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 2 Care of Patients, printed page 61 (PDF page index 67). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: COP.1.a Core, COP.1.b Commitment, COP.1.c Achievement, COP.1.d Commitment, COP.1.e Excellence.
   TWO OEs CARRY THE ASTERISK -- COP.1.d and COP.1.e. The draft builds two separate deep blocks (step 4 for d; step 5 for e). COP.1.a (Core, two identifiers), COP.1.b (Commitment, applicable laws) and COP.1.c (Achievement, evidence-based protocols) are unasterisked and are correspondingly Tier 2.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the COP.1 page read directly from the extracted page text, and the committed asterisk file. COP.1 was not among the 14 mismatches of the 2026-08-10 audit.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. Tier 1: COP.1.d, COP.1.e -- procedure steps 4 and 5 carry the reasoning (why setting is a source of unjustified variation; why informal remote advice is not a telemedicine facility). Tier 2: COP.1.a (step 1), COP.1.b (step 2) and COP.1.c (step 3) -- requirement and method without extended rationale. COP.1.a is Core (assessed at every visit) but not asterisked; Core is not a substitute for the asterisk when allocating depth. Reviewer to note the shallower treatment of a, b and c is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of COP.1.d/e against the approved HIC masters, the approved AAC.1 master, and the unapproved AAC.2, AAC.3, AAC.4, AAC.7 and AAC.8 drafts. Files: /tmp/aac_drafts/hic1_draft.json through hic6_draft.json and aac1_draft.json through aac8_draft.json. Search terms: uniform care, identifier, telemedicine, protocol, clinical practice guideline.
   AAC.2.b generates the unique identification number at registration. This draft's Scope and step 1 use that number as one identifier at the point of care and do not generate it. Division stated. Flag for master-policy-todos.md so the division is not lost if one is approved without the other.
   AAC.1 defines services and department scopes. This draft makes care for a given condition the same in every setting in which that care is provided. Not the same requirement. Stated in Scope.
   AAC.3 owns assessment, care plan, reassessment and early warning. Assessment is not a uniform-care protocol. Stated in Scope.
   AAC.4 applies identity before specimen collection. This document owns the hospital-wide two-identifier process; AAC.4 applies it at the chair. T2 flag only.
   AAC.7 owns handover method and internal transfer. This document owns that the care handed over was delivered to the same standard. T2 flag only.
   HIC.2 owns hand hygiene, PPE, transmission-based precautions. Uniform care does not rewrite them. Stated in Scope. Nothing added to the reconciliation list against the approved HIC set.
3. FORWARD REFERENCES: nursing CPGs -- COP.4 (drafted in the same pass); emergency operational protocols -- COP.2; resuscitation -- COP.3; intensive care -- COP.6; medical-record structure -- IMS, not yet drafted. Intra-COP: COP.1.c hospital-wide clinical protocols vs COP.4.d nursing CPGs -- both Scopes must keep the division.
4. T2 QUICK CHECK: COP.1.a vs AAC.2.b as above. COP.1.b applicable laws -- this draft refuses BMW/FSS inherit and refuses CEA-by-default; the hospital names the laws that apply to its defined services.

STATUTORY AND EXTERNAL FACTS
5. Telemedicine Practice Guidelines, 2020 (MoHFW / NMC) -- USED: RMP only; identity of both parties; informed consent; modes; prescription within the Guidelines without printing a drug list; emergency directed to in-person care; records; privacy. NOT USED as a reprinted protocol. Chapter reference 4 (Ateriya 2018) is context, not a protocol.
6. National Medical Commission Act, 2019 -- cited only insofar as who may provide a telemedicine consultation. No section number.
7. Clinical Establishments Act, 2010 -- NOT cited. COP.1.b does not default to it.
8. Bio-Medical Waste Management Rules, 2016 and Food Safety and Standards Act, 2006 -- NOT named. HIC.3 owns those where they apply.
9. Standard Treatment Guidelines on the clinical establishments portal -- chapter reference 30; acceptable origin for protocols, not a mandated set. Montori 2013 (ref 32) and Rotter 2010 (ref 47) inform evidence-based / pathway practice; no named tool is mandated.
10. NO NUMBERS ARE STATED as requirements -- no identifier-digit lengths, no telemedicine response times, no protocol-review months. Every such value is [Hospital to define]. Consistent with the no-numbers default.
11. EXTERNAL CLINICAL/TECHNICAL FACT-CHECKING (Tier 1): TPG 2020 identity, consent, RMP, emergency-to-in-person, records and privacy verified against the Guidelines' published scheme as cited in the chapter references and Ateriya 2018's Indian context. No drug schedule table is printed. Bed/room number refused as an identifier is an editorial patient-safety position, not a cited numeric rule.

EDITORIAL POSITIONS TAKEN
12. Step 1's rule that bed number, room number, cubicle, trolley or tray position is not an identifier is an editorial position; the standard requires two identifiers, not this exclusion.
13. Step 4's rule that intensity may vary with clinical need but the protocol may not contradict itself by location, and that a revision must reach every listed setting on the same date, are editorial positions; the standard requires uniform care delivery, not these specifics.
14. Step 5's rule that a written decision not to provide telemedicine is required, and that unofficial remote advice is not a third category, is an editorial position; the OE is Excellence and assumes a facility, but leaving the negative unwritten is how unofficial remote care happens.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
15. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the Telemedicine Practice Guidelines, 2020 (MoHFW / NMC) insofar as a telemedicine facility is provided -- the instrument this document's References actually rely on for COP.1.e. It does NOT name the Bio-Medical Waste Management Rules, 2016, the Food Safety and Standards Act, 2006, or the Clinical Establishments Act 2010. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- Generation of the unique identification number -- AAC.2.b.
- Service directory -- AAC.1.
- Initial assessment and care plan -- AAC.3.
- Nursing CPGs, nursing documentation, assignment, nursing equipment -- COP.4.
- Emergency area, ambulance, triage -- COP.2.
- CPR -- COP.3.
- ICU operational protocols -- COP.6.
- Hand hygiene, PPE, transmission-based precautions -- HIC.2.
- A reprinted Telemedicine Practice Guidelines protocol or a drug list.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 15 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 13 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 15; a search for "Hospital to define" without brackets finds all 15, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: the two identifiers used at the point of care; how confirmation of the two identifiers is recorded; the applicable laws and regulations and where that list is held; the evidence-based clinical protocols in use, the conditions they cover, and where they are held; for each adopted protocol, the settings in which that care is provided and the current version in each; how staff in each setting are shown the current protocol version and how a contradiction is reported; whether a telemedicine facility is provided; the telemedicine modes and platform; how privacy and security of a telemedicine consultation and its record are kept; the written telemedicine guidance, the named practitioners, and where the guidance is held; the audit interval for these records; the review interval for this policy; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
