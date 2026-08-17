# -*- coding: utf-8 -*-
"""Builds the COP.11 master policy draft: JSON for review + SQL for later insert.

UNAPPROVED DRAFT. Do not insert, approve, or write this to Supabase.

THIS IS DRAFTED UNDER THE TWO-TIER DEPTH STANDING RULE (2026-08-10) AND THE
DISCLAIMER STATUTE-MATCHING STANDING RULE (2026-08-17), both in
scripts/master-policy-todos.md.

Tier is decided by doc_required / the asterisk in the official PDF:
  Tier 1 (full treatment): COP.11.a, COP.11.d (Core), COP.11.h
  Tier 2 (lighter pass):   COP.11.b, COP.11.c, COP.11.e, COP.11.f,
                           COP.11.g, COP.11.i (Core), COP.11.j (Core)

Official source: NABH Standards for Small Healthcare Organisations, 3rd Edition
(August 2022), Chapter 2, standard COP.11 and OEs COP.11.a-j, read from the
official standards PDF (downloaded 2026-08-17 from the NABH website's Explore
NABH Standards page), printed page 67, PDF page index 73.

Asterisks verified 2026-08-17: scripts/asterisk_extract.py re-run against that
download (self-validation passed, 408 OEs, 132 asterisks, output matched the
committed scripts/shco_oe_asterisks.json on all 408 entries) and the COP.11
page read directly. COP.11.a, COP.11.d and COP.11.h carry the asterisk;
COP.11.b, c, e, f, g, i and j are unasterisked.
"""
from policy_build_common import emit_and_verify, make_disclaimer

STANDARD_CODE = "COP.11"
CHAPTER = "COP"
OE_CODES = [
    "COP.11.a", "COP.11.b", "COP.11.c", "COP.11.d", "COP.11.e",
    "COP.11.f", "COP.11.g", "COP.11.h", "COP.11.i", "COP.11.j",
]
TIER1_OES = ["COP.11.a", "COP.11.d", "COP.11.h"]

POLICY_TITLE = "Clinical Procedures and Operation Theatre Practice"

VERSION = "1.0"
REVISION_HISTORY = [
    {"version": "1.0", "date": "17-08-2026", "description": "Initial release."},
]

PURPOSE = """This document sets out how {{HOSPITAL_NAME}} performs clinical procedures and operations in a consistent and safe manner: written guidance that the teams actually use; a pre-operative assessment, diagnosis and instructions before the knife; consent obtained by the doctor who will operate; a method that prevents wrong site, wrong patient and wrong surgery; standard precautions applied in the theatre as they are applied everywhere else; an operation note and a post-operative plan in the record; facilities and equipment that match the list; a quality-assurance programme that looks at whether those steps ran; and, where the hospital holds itself out as a transplant centre, a programme that meets the Transplantation of Human Organs and Tissues Act, 1994. Whether or not a transplant programme exists here, the hospital takes measures to create awareness of organ donation.

A procedure performed from memory, a laterality confirmed after the drape is down, or a checklist ticked after the patient has left the table, is not a safe procedure. This document is the process that makes the chapter intent operational in the operating theatre, the procedure room and the day-care theatre of {{HOSPITAL_NAME}}."""

SCOPE = """This policy applies to every clinical procedure and every operation performed at {{HOSPITAL_NAME}}: the main operating theatre, any day-care or minor-procedure theatre, endoscopy or other procedure rooms where a surgical or invasive procedure is done, and the recovery area that receives the patient immediately afterwards. It binds the operating surgeon, the anaesthetist (whose anaesthetic care is owned elsewhere), the scrub and circulating nurses, technicians, and any visiting or honorary surgeon who operates under this hospital's unique identification number.

It covers: written guidance that makes procedure practice consistent and safe; pre-operative assessment, documented pre-operative diagnosis and pre-operative instructions; informed consent obtained by the doctor prior to the procedure; prevention of wrong site, wrong patient and wrong surgery, including the hospital's surgical-safety checklist; adherence to standard precautions during the procedure; accurate documentation of the procedure or operation notes, post-procedure monitoring and the post-operative care plan; availability of appropriate facilities, equipment, instruments and supplies in the operating theatre; the quality-assurance programme for procedural and theatre practice; the organ-transplant programme where one exists, in consonance with legal requirements and conducted ethically; and measures to create awareness of organ donation.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Procedural sedation is governed by the procedural-sedation policy of {{HOSPITAL_NAME}} (COP.9). Anaesthesia services — pre-anaesthesia assessment and plan, pre-induction assessment, anaesthetic consent, intra-operative anaesthetic monitoring, post-anaesthesia recovery criteria, and the anaesthetic record — are governed by the anaesthesia policy of {{HOSPITAL_NAME}} (COP.10). This policy owns the surgical or clinical procedure, the site, the patient identity for the procedure, the surgical-safety checklist as the team's pause, the operation note and the post-operative surgical plan. Sedation is not general anaesthesia; anaesthesia is not the operation. This document does not write the sedation policy and does not write the anaesthesia policy.
- Standard precautions, hand hygiene, personal protective equipment, safe injection and sharps practice in every clinical area including the operating theatre are governed by the infection-prevention-and-control-practices policy of {{HOSPITAL_NAME}} (HIC.2, approved). COP.11.e requires that the procedure is done adhering to those standard precautions. This policy does not restate personal protective equipment selection, the five moments, or the injection-safety rules.
- The surgical-site-infection prevention bundle — pre-operative bathing, hair removal without razors, surgical prophylaxis timing as an infection-control process, skin preparation, normothermia, glycaemic control, and post-operative wound care as written there — is governed by the healthcare-associated-infection-prevention policy of {{HOSPITAL_NAME}} (HIC.4, approved). This policy owns the operation, site-marking, the surgical-safety checklist, and the surgical notes. Completing a checklist is not completing the SSI bundle; running the SSI bundle is not marking the site.
- Surgical-site-infection surveillance, including post-discharge detection and the case definitions used to count SSI, is governed by the infection-surveillance policy of {{HOSPITAL_NAME}} (HIC.5, approved). The quality-assurance programme in this document looks at whether the procedural process ran (checklist completion, consent, notes, postponements, near-misses of wrong site or wrong patient). It does not count SSI and does not write NHSN definitions.
- Reprocessing, sterilisation, sterile storage and the check before use of surgical instruments are governed by the sterilisation-and-disinfection policy of {{HOSPITAL_NAME}} (HIC.6, approved). This policy requires that sterile instruments and supplies are available in the theatre for the list; it does not write the decontamination cycle.
- Colour-coded biomedical waste generated in the theatre, including anatomical waste, is governed by the support-services infection-control policy of {{HOSPITAL_NAME}} (HIC.3, approved). This policy does not restate the four colour categories.
- Transfer of the patient from a ward or emergency area into the operating theatre, and from the theatre or recovery back to a unit, is governed by the continuity, handover and internal-transfer policy of {{HOSPITAL_NAME}} (AAC.7). This policy owns what happens in the theatre once the patient has been received.
- The two identifiers used to confirm identity at the point of care are governed by the uniform-care policy of {{HOSPITAL_NAME}} (COP.1). This policy uses those identifiers before a procedure; it does not invent a third identifier system.
- Generation of the unique identification number at registration is governed by the registration and admission policy of {{HOSPITAL_NAME}} (AAC.2). This policy requires that number on the consent, the checklist, the operation note and the implant record; it does not issue the number.
- The method of informed consent generally is governed by the patient-rights policies of {{HOSPITAL_NAME}} (PRE, not yet drafted). This policy owns that the doctor who will perform the procedure obtains consent before that procedure.
- The medical record itself — its structure, retention and confidentiality — is governed by the information-management policies of {{HOSPITAL_NAME}} (IMS, not yet drafted). This policy owns the procedure and operation-note content written into that record.
- End-of-life pathways and brain-death declaration, where they exist, are governed by the intensive-care policy of {{HOSPITAL_NAME}} (COP.6). This policy owns only the transplant-programme and donation-awareness duties of COP.11.i and COP.11.j."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} performs clinical procedures and operations according to written guidance, in a consistent and safe manner, in every theatre and procedure room it uses.

{{HOSPITAL_NAME}} does not start an elective or scheduled procedure without a pre-operative assessment, a documented pre-operative diagnosis, and documented pre-operative instructions.

{{HOSPITAL_NAME}} requires the doctor who will perform the procedure to obtain informed consent before it starts.

{{HOSPITAL_NAME}} takes care to prevent wrong site, wrong patient and wrong surgery. Identity is confirmed using the two identifiers of the uniform-care policy. The side and site are marked, where marking applies, before the patient is moved into the operating room. The team pauses on a surgical-safety checklist whose framework is the World Health Organization Guidelines for Safe Surgery 2009; the hospital's own checklist is this hospital's document, not a photocopy of the WHO items treated as a mandated script.

{{HOSPITAL_NAME}} performs every procedure adhering to the standard precautions already in force under the infection-prevention-and-control-practices policy. This document does not rewrite those precautions.

{{HOSPITAL_NAME}} documents the procedure or operation notes, post-procedure monitoring and the post-operative care plan accurately in the patient record.

{{HOSPITAL_NAME}} keeps appropriate facilities, equipment, instruments and supplies available in the operating theatre for the procedures it has defined.

{{HOSPITAL_NAME}} implements a quality-assurance programme for procedural and theatre practice.

Whether {{HOSPITAL_NAME}} conducts an organ transplant programme is [Hospital to define — whether this hospital conducts an organ transplant programme]. If it does, that programme is conducted in consonance with the Transplantation of Human Organs and Tissues Act, 1994, and ethically. If it does not, that fact is recorded and the transplant-programme rules of this document do not operate. In either case, {{HOSPITAL_NAME}} takes measures to create awareness of organ donation."""

PROCEDURE_STEPS = [
"""1. Written guidance that makes procedures consistent and safe

Clinical procedures, and procedures done in the operation theatres of {{HOSPITAL_NAME}}, are done in a consistent and safe manner. Consistency means that the same class of procedure is prepared, paused, performed and documented the same way whether it is on this morning's list or an emergency at night, and whether the surgeon is employed or visiting. Safety means that identity, site, consent, sterility of what is opened, and the record of what was done are not left to memory.

This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask how the hospital makes theatre practice consistent. The answer must be written guidance that staff can show they used on the last list, not a claim that experienced surgeons know what to do.

The written guidance covers at least: which procedures may be performed in which theatre or procedure room, matching the service directory and the department scopes of services maintained under the definition-and-display policy of {{HOSPITAL_NAME}}; who may perform them, using credentials verified under the human resource policies of {{HOSPITAL_NAME}} and not restated here; how a list is scheduled and how an emergency case is inserted; what must be present before the patient is moved into the operating room (identity confirmed, consent, marked site where marking applies, investigations the surgeon has stated as required, blood where the case needs it); the surgical-safety checklist at step 4; standard precautions by pointer to the infection-prevention-and-control-practices policy at step 5; the operation-note content at step 6; and what happens when a case is postponed or abandoned.

The reason the guidance has to be written, and used, is that theatre is a place where several professions work at speed on a person who cannot speak for themselves once anaesthetised. Without a shared method, each list is a private arrangement between whoever is in the room. That arrangement holds until the day the laterality is the other one, the implant is the wrong size, or the visiting surgeon's usual sequence is not this hospital's. Written guidance is what makes the next list the same process as the last one.

The common error is a theatre manual that lives in a cupboard and a list that runs on habit. Habit is not a method. A new staff member, a locum, or a night emergency cannot consult habit. The guidance in force, and the named roles that apply it, are held at [Hospital to define — where the written procedural and operation-theatre guidance is held].

This step does not write the SSI bundle, the sterilisation cycle, or the anaesthetic. Those remain in the documents named in Scope.""",

"""2. Pre-operative assessment, diagnosis and instructions

Surgical patients have a pre-operative assessment, a documented pre-operative diagnosis, and pre-operative instructions provided before surgery and documented.

The pre-operative assessment is performed by [Hospital to define — who performs the pre-operative assessment] and is recorded against the unique identification number. It is not the pre-anaesthesia assessment owned by the anaesthesia policy of {{HOSPITAL_NAME}}; that assessment produces the anaesthetic plan. This assessment produces the surgical decision: that this patient, with this diagnosis, is to have this procedure, on this side if laterality applies, with these instructions beforehand.

The documented pre-operative diagnosis is written before the patient is moved into the operating room. A diagnosis first written in the operation note after the procedure is not a pre-operative diagnosis.

Pre-operative instructions — fasting, medication to omit or to take, skin preparation the surgeon requires beyond the SSI-bundle bathing owned by the healthcare-associated-infection-prevention policy, and anything the patient or ward must do — are given and documented. The instruction set used at {{HOSPITAL_NAME}} is [Hospital to define — the pre-operative instructions given, and where they are documented].

An emergency procedure that cannot wait for a full elective work-up still has a recorded working diagnosis and the instructions that were possible. Absence of time is recorded; absence of a diagnosis is not.""",

"""3. Informed consent obtained by the doctor prior to the procedure

Informed consent is obtained by the doctor prior to the procedure. In this document the doctor is the person who will perform the procedure, or a doctor of the same surgical team who will be present and responsible for it. A consent taken by a clerk, a nurse or a doctor who will not be in the theatre does not meet this step.

The method of consent — the information given, the language, the signature, the witness, and capacity — is governed by the patient-rights policies of {{HOSPITAL_NAME}}. This step owns the timing and the person: consent is present, in the record, before the procedure starts, obtained by that doctor.

The consent names the procedure, the side where laterality applies, and the unique identification number. A consent for "surgery" without the procedure, or without the side of a paired organ, is incomplete.

How consent is recorded, and where the form is held in the record, is [Hospital to define — how procedural consent is recorded and where it is held in the record].

An emergency that makes prior consent impossible is recorded as such, with the reason and the person who decided to proceed, in line with the patient-rights policies. Emergency is not a standing exemption for convenience.""",

"""4. Preventing wrong site, wrong patient and wrong surgery

Care is taken to prevent adverse events like wrong site, wrong patient and wrong surgery. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask how the hospital stops the operation on the wrong person or the wrong side. The answer must be a method the last list used, not a statement that it has never happened here.

Wrong-site, wrong-patient and wrong-procedure events are rare and devastating, and they are almost always a failure of a pause that was skipped, a mark that was not made, or an identity that was assumed because the trolley was in the right theatre. The World Health Organization Guidelines for Safe Surgery 2009: Safe Surgery Saves Lives — chapter reference 64 of this standard — is the framework {{HOSPITAL_NAME}} uses for that pause. The 2009 guidance organises the pause into three moments: before induction of anaesthesia, before skin incision, and before the patient leaves the operating room. {{HOSPITAL_NAME}} adopts those three moments as its framework. It does not paste the WHO checklist items as a mandated verbatim script. The hospital's own surgical-safety checklist, the items it contains, and who leads each pause are [Hospital to define — the surgical-safety checklist in use, its items, and who leads each pause]. The checklist is completed as the pauses happen, by the people in the room, out loud. Completing it later from memory, or ticking it in recovery, is forbidden. A ticked box that was not a pause is a record of a pause that did not occur, and it is how the next wrong-site event will be documented as having been prevented.

Identity is confirmed at the first pause using the two identifiers required by the uniform-care policy of {{HOSPITAL_NAME}}, matched to the consent, the operating list and the unique identification number. The patient participates in that confirmation while able to do so. A wristband glanced at by one person, or a name called from the corridor, is not confirmation.

Where the procedure has a side or a level, the site is marked before the patient is moved into the operating room, with the patient participating where able, using [Hospital to define — the site-marking method, including who marks, with what, and which procedures are exempt because laterality does not apply]. Marking after the drape is down, or marking the opposite side as a reminder, is forbidden. The mark is visible after draping; a mark that the drape hides is not a mark the team can use.

The operating list, the consent, the mark and the imaging (where imaging defines the site) are agreed at the pause before incision. Disagreement stops the procedure until it is resolved. Starting because the list is running late is the common error this step exists to stop. Deutsch and colleagues (2018) — chapter reference 15 — documented that wrong-site nerve blocks, a close cousin of wrong-site surgery, persist where the pause is treated as optional around regional anaesthesia; the same pause applies to a block that laterality can get wrong.

Implants, prostheses and any laterality-specific device are confirmed at the pause against the consent and the planned procedure. The confirmation is recorded.

A near-miss — the wrong patient brought to theatre, a missing mark, a laterality mismatch caught at the pause — is recorded and reviewed under step 8. Catching it is the method working. Not recording it is the method pretending it was never needed.

The completed checklist travels with the unique identification number in the record. Where the completed checklists are filed is [Hospital to define — where completed surgical-safety checklists are filed].""",

"""5. Standard precautions during the procedure

The procedure is done adhering to standard precautions. Standard precautions at {{HOSPITAL_NAME}} are owned by the infection-prevention-and-control-practices policy (HIC.2). They apply to every patient in the operating theatre and in every procedure room, without reference to diagnosis.

This step is the instruction to follow that policy in this setting. It does not restate hand hygiene moments, personal-protective-equipment selection, surgical attire beyond what HIC.2 and the SSI bundle already require, safe injection, or sharps handling. Those rules are not different in the theatre; they are the same rules applied where the exposure is greater.

The circulating and scrub staff, the surgeon and the anaesthetist apply HIC.2 in the theatre. A breach of standard precautions during a procedure is reported and handled under that policy, not under a parallel theatre-only rule.

The SSI bundle (bathing, hair, prophylaxis timing, skin preparation, normothermia, glycaemia, wound care) remains HIC.4. Instrument sterility remains HIC.6. Theatre biomedical waste remains HIC.3. None of those is rewritten here.

How theatre staff are shown that HIC.2 applies in the operating theatre, including at induction to the theatre, is [Hospital to define — how theatre staff are briefed that standard precautions under HIC.2 apply in the operating theatre].""",

"""6. Procedure notes, post-procedure monitoring and the post-operative care plan

Procedures and operation notes, post-procedure monitoring and the post-operative care plan are documented accurately in the patient record, against the unique identification number.

The operation or procedure note is written by [Hospital to define — who writes the operation or procedure note, and by when it must be in the record]. It includes at least: the procedure actually performed, the side, findings, implants or specimens with their identification, estimated blood loss as the surgeon records it, complications intra-operatively, and the name of the operating surgeon and assistants. The anaesthetic record is owned by the anaesthesia policy and is not duplicated here.

Post-procedure monitoring in recovery, until the patient leaves for a ward or for home, is recorded. Objective discharge from recovery after anaesthesia is owned by the anaesthesia policy. This step owns the surgical observations and the surgical plan that travel with the patient.

The post-operative care plan — wound, drains, antibiotics as a clinical prescription (the SSI-bundle prophylaxis stop remains HIC.4), mobilisation, diet, and review — is written before the patient leaves recovery. A plan that exists only as a verbal instruction to the receiving nurse is not documented.

The medical record structure is owned by the information-management policies of {{HOSPITAL_NAME}}. This step owns the surgical content.""",

"""7. Facilities, equipment, instruments and supplies in the operating theatre

Appropriate facilities, equipment, instruments and supplies are available in the operating theatre for the procedures {{HOSPITAL_NAME}} has defined.

The theatre or procedure rooms in use, and the procedures each may hold, are [Hospital to define — the operating theatres and procedure rooms in use, and the procedures each may hold], aligned with the service directory. A procedure the directory does not include is not listed here.

Instruments used on sterile tissue are sterile at the point of use. The decontamination cycle, the pack, and the check before opening are owned by the sterilisation-and-disinfection policy of {{HOSPITAL_NAME}}. This step requires that the sets needed for the list are present, in date, and with intact indicators, and that a missing or unsterile set stops the case rather than being substituted from an unchecked tray.

Equipment that must be present for the defined lists — lights, table, suction, cautery, emergency airway and resuscitation equipment as the resuscitation policy requires in this area — is [Hospital to define — the equipment inventory that must be present in each operating theatre]. Equipment that is out of service is labelled and is not counted as available.

Supplies, including implants the list requires, are confirmed before the patient is anaesthetised. Discovering that the implant is not in the hospital after induction is a preventable cancellation and is reviewed under step 8.

Engineering controls of the theatre — ventilation, pressure, temperature as an engineering matter — are owned by the support-services infection-control policy and the facility policies of {{HOSPITAL_NAME}}. This step does not write those parameters.""",

"""8. Quality-assurance programme for procedural and theatre practice

The organisation shall implement a quality-assurance programme. This step is the documented-evidence anchor of that asterisked requirement. A programme that exists as a file of theatre statistics no one reads is not implemented.

{{HOSPITAL_NAME}} names a theatre quality lead. The named lead is [Hospital to define — the named theatre quality lead]. That person is accountable for the programme running, for the records it produces, and for bringing findings to the review forum.

The programme looks at whether the process in this document ran, not at the infection rates owned by the infection-surveillance policy. It includes at least: completion of the surgical-safety checklist as a pause rather than as a retrospective tick; consent present before incision; a documented pre-operative diagnosis; an operation note in the record within the time at step 6; postponements and cancellations after the patient has arrived, with the reason (missing implant, missing consent, unmarked site, equipment failure); near-misses of wrong site, wrong patient or wrong procedure; and any actual wrong-site, wrong-patient or wrong-procedure event, which is reported immediately and analysed.

Why this is a separate programme from SSI surveillance: HIC.5 counts infections with published case definitions and device or procedure denominators. That count cannot tell the hospital whether yesterday's list paused before incision. A hospital can have a low counted SSI rate and still be one skipped pause away from operating on the other kidney. The quality-assurance programme here is the process look; surveillance is the outcome look. Neither substitutes for the other. Haynes, Berry and Gawande (2015) — chapter reference 19 — summarised what is known about the safe-surgery checklist: the benefit follows use of the pause, not possession of the form. This programme therefore measures use, not possession.

The measures, the sample or census used, and the interval are [Hospital to define — the quality-assurance measures for theatre practice, the sample or census, and the review interval]. No numeric threshold is mandated in this document. Targets, if the hospital sets them, are [Hospital to define — any quality-assurance targets for theatre practice].

Findings that require change produce a corrective and preventive action with an owner and a due date. An action that is only a reminder to "be careful" is not a change to the method.

The forum at which findings are reviewed is [Hospital to define — the forum at which theatre quality-assurance findings are reviewed]. The infection-prevention-and-control committee may hear SSI-bundle compliance under HIC.4 and SSI rates under HIC.5 at a related meeting; those agenda items are not this programme.

The common error is to treat theatre quality assurance as a count of cases done, or as a photocopy of the infection-control minutes. Volume is not assurance. Infection-control minutes are not a checklist-completion audit.""",

"""9. Organ transplant programme — legal and ethical, or a recorded absence

The organ transplant programme shall be in consonance with the legal requirements and shall be conducted ethically.

Whether {{HOSPITAL_NAME}} conducts an organ transplant programme is the same hospital decision named in the Policy Statement: [Hospital to define — whether this hospital conducts an organ transplant programme]. That decision must match the service directory maintained under the definition-and-display policy. A transplant service displayed to the public that this step says does not exist, or a transplant performed that the directory does not name, is a document defect and a legal one.

If {{HOSPITAL_NAME}} does not conduct an organ transplant programme, this step records that fact. No retrieval or transplantation of human organs is performed here. Staff do not hold the hospital out as a transplant centre. The remainder of the transplant-programme rules in this step do not operate. Step 10 still applies in full: donation-awareness measures are required of the organisation whether or not it transplants.

If {{HOSPITAL_NAME}} does conduct an organ transplant programme, that programme operates only as a registered transplant centre under the Transplantation of Human Organs and Tissues Act, 1994, and the rules under it, including State authorisation and the involvement of the appropriate Authorization Committee. Organs are not transplanted from a living donor except as that Act permits. Commercial dealing in human organs is forbidden. Brain-death declaration, where donation after brainstem death is part of the pathway, uses the legal method; the intensive-care policy of {{HOSPITAL_NAME}} owns the end-of-life and brain-death clinical pathway, and this step owns that a transplant is not begun on a declaration this hospital is not authorised to make. The skill mix, the intensive-care support and the laboratory support behind the programme match what the directory claims. The World Health Organization Guiding Principles on Human Cell, Tissue and Organ Transplantation — chapter reference 18 — inform the ethical posture (non-commercial, consent, equitable allocation) and are not imported as a substitute for the 1994 Act.

The named person accountable for the transplant programme, where one exists, and the location of the registration and Authorization Committee records, are [Hospital to define — the named transplant-programme lead, where a programme exists, and where the statutory registration and Authorization Committee records are held].

This step does not write intensive-care end-of-life care. It writes the legal-and-ethical envelope of transplantation, or the recorded fact that transplantation is not done here.""",

"""10. Awareness of organ donation

The organisation shall take measures to create awareness regarding organ donation. This Core requirement applies whether or not {{HOSPITAL_NAME}} conducts a transplant programme. A hospital that does not transplant still sees deaths, still sees families, and still sits in a community that can donate through the national and State organ-transplant network.

The awareness measures in force at {{HOSPITAL_NAME}} are [Hospital to define — the measures taken to create awareness of organ donation, including who is responsible and which materials or sessions are used]. They may include displayed information, briefing of relevant clinical staff on how a family is given information and how a referral to the State or regional organ-transplant organisation is made, and information offered to the public the hospital serves. This document does not mandate a particular campaign, a quota of pledges, or a script for grieving families.

Awareness is not procurement. Staff do not pressure a family. Where a patient or family asks about donation, the person who responds is [Hospital to define — who responds to a family enquiry about organ donation, and how a referral to the organ-transplant network is made when the hospital does not itself transplant].

If a transplant programme exists under step 9, awareness measures are additional to that programme and are not satisfied merely by being registered as a centre.

Records of the measures — the materials, the dates of any session, the display — are kept by [Hospital to define — who keeps the organ-donation awareness records].""",

"""11. Records, review and the order of operations

Every pre-operative assessment, pre-operative diagnosis, pre-operative instruction, consent, site mark, completed surgical-safety checklist, operation note, post-operative plan, postponement, near-miss, quality-assurance finding, transplant-programme record where one exists, and donation-awareness record is filed against the unique identification number where a patient is involved, and is retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for procedural and operation-theatre records] for: written guidance in use rather than only on file; a pre-operative diagnosis dated before the procedure; consent obtained by the operating doctor; a completed checklist that matches the time of the procedure rather than a block of ticks at the end of the list; an operation note and a post-operative plan in the record; checklist and consent defects feeding the quality-assurance programme; the recorded transplant-programme status matching the service directory; and donation-awareness measures that exist even when there is no transplant programme.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a wrong-site or wrong-patient event or near-miss occurs, when the service directory adds or removes a procedure or a transplant programme, or when the infection-control, anaesthesia, sedation, internal-transfer or intensive-care policies that this document hands work to are revised.""",
]

RESPONSIBILITY = """The head of the institution is accountable for {{HOSPITAL_NAME}} performing procedures consistently and safely, for a method that prevents wrong site, wrong patient and wrong surgery, for a quality-assurance programme that is run, and for the hospital's transplant-programme status and donation-awareness measures matching the law and the service directory.

The person in charge of the operating theatre holds the written guidance at step 1, the equipment and supply inventory at step 7, and supports the pauses at step 4.

The operating surgeon obtains consent at step 3, marks the site at step 4, leads or participates in the pauses, writes or ensures the operation note and post-operative plan at step 6, and does not start when identity, site, consent or sterility of the opened set is in doubt.

The named theatre quality lead at step 8 operates the quality-assurance programme and reports findings at the stated forum.

Theatre nursing and technical staff apply the written guidance, complete the checklist as a pause, apply standard precautions under HIC.2, and do not open an unsterile or overdue set.

The anaesthetist participates in the pauses at step 4; anaesthetic care remains the anaesthesia policy.

The named transplant-programme lead, where a programme exists, holds the statutory registration and Authorization Committee records at step 9.

The person named at step 10 holds the donation-awareness measures and records.

The quality or accreditation coordinator audits the records at step 11 and reports findings to the head of the institution.

All staff are expected to treat a skipped pause, an unmarked laterality, a consent obtained after incision, and a hospital held out as transplanting when it is not registered to do so, as defects, and to report them."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.11.
- Transplantation of Human Organs and Tissues Act, 1994, and the rules under it, insofar as this hospital conducts an organ transplant programme or takes measures to create awareness of organ donation.
- World Health Organization, WHO Guidelines for Safe Surgery 2009: Safe Surgery Saves Lives — chapter reference 64 of this standard; used here as the three-moment checklist framework (before induction, before incision, before the patient leaves the operating room). This document does not import the WHO checklist items as a mandated verbatim script; the hospital's own checklist is [Hospital to define].
- Haynes, A. B., Berry, W. R., and Gawande, A. A. (2015). What Do We Know About the Safe Surgery Checklist Now? Annals of Surgery, 261(5), 829-830 — chapter reference 19; used here to support measuring use of the pause, not possession of the form.
- Deutsch, E. S., et al. (2018). Wrong-site nerve blocks: A systematic literature review to guide principles for prevention. Journal of Clinical Anesthesia, 46, 101-111 — chapter reference 15; used here to extend the same pause to laterality-sensitive blocks, without importing that review's tables.
- World Health Organization, Guiding principles on human cell, tissue and organ transplantation — chapter reference 18; ethical posture only, not a substitute for the 1994 Act.
- Internal documents of {{HOSPITAL_NAME}}: the service directory and department scopes of services; the written procedural and operation-theatre guidance; the surgical-safety checklist; the pre-operative instruction set; the site-marking method; completed checklists and operation notes; the theatre quality-assurance records; the recorded transplant-programme status and, where a programme exists, the statutory registration; the organ-donation awareness records; the uniform-care policy; the anaesthesia and procedural-sedation policies; the continuity and internal-transfer policy; the infection-prevention-and-control-practices policy; the healthcare-associated-infection-prevention policy; the infection-surveillance policy; the sterilisation-and-disinfection policy; the support-services infection-control policy; the intensive-care policy; the patient-rights policies; the human resource policies; and the information-management policies."""

DISTRIBUTION = """Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every operating theatre and procedure room; recovery; the surgical departments; anaesthesia; nursing administration; the person in charge of the operating theatre; the named theatre quality lead; the named transplant-programme lead where that role exists; and every visiting or honorary surgeon who operates here.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The written procedural guidance, the surgical-safety checklist and the site-marking method — the working documents this policy requires — are held in each operating theatre.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, OT, SSI, PPE, WHO, SOP, ICT and CSSD.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

NOTTO — National Organ and Tissue Transplant Organisation
THOA — Transplantation of Human Organs and Tissues Act, 1994

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

STATUTE_CLAUSE = (
    "the Transplantation of Human Organs and Tissues Act, 1994, insofar as this hospital "
    "conducts an organ transplant programme or takes measures to create awareness of organ donation"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "COP.11.a",
        "requirement": "Clinical procedures as well as procedures done in operation theatres are done in a consistent and safe manner.",
        "steps": "Steps 1, 11",
        "evidence": "The written procedural and operation-theatre guidance covering which procedures may be performed in which theatre, who may perform them, how a list is scheduled and how an emergency is inserted, what must be present before the patient is moved into the operating room, the surgical-safety checklist pointer, the standard-precautions pointer, the operation-note content and the postponement route; alignment of that guidance with the current service directory and department scopes of services; human-resource credentialing used and not restated; sample lists showing the same class of procedure prepared, paused, performed and documented the same way on a routine list and on an emergency or out-of-hours case, and by employed and visiting surgeons; the location where the guidance is held and induction or briefing records showing theatre staff have been shown it rather than a cupboard copy; records of a case stopped or postponed when a required element was missing rather than started from habit; the audit sample at step 11 of written guidance in use rather than only on file",
        "responsible": "Person in charge of the operating theatre holds the written guidance; operating surgeons and theatre staff apply it; head of the institution is accountable that procedures are consistent and safe; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "COP.11.b",
        "requirement": "Surgical patients have a preoperative assessment, a documented pre-operative diagnosis, and pre-operative instructions provided before surgery and documented.",
        "steps": "Steps 2, 11",
        "evidence": "Pre-operative assessment records against the unique identification number, distinct from the pre-anaesthesia assessment; documented pre-operative diagnosis dated before the patient is moved into the operating room; the written pre-operative instruction set and sample records that instructions were given; emergency cases with a recorded working diagnosis rather than a blank",
        "responsible": "Operating surgeon or the role named at step 2 performs and documents the assessment, diagnosis and instructions",
    },
    {
        "oe_code": "COP.11.c",
        "requirement": "Informed consent is obtained by the doctor prior to the procedure.",
        "steps": "Steps 3, 11",
        "evidence": "Consent forms naming the procedure, the side where laterality applies and the unique identification number, signed by the doctor who will perform the procedure before it starts; records of incomplete consents not accepted; documented emergency exceptions with reason, consistent with the patient-rights policies",
        "responsible": "Operating doctor obtains consent; patient-rights policies own the consent method; theatre staff do not start without it",
    },
    {
        "oe_code": "COP.11.d",
        "requirement": "Care is taken to prevent adverse events like wrong site, wrong patient and wrong surgery.",
        "steps": "Steps 4, 8, 11",
        "evidence": "The hospital's own surgical-safety checklist, stating that the World Health Organization Guidelines for Safe Surgery 2009 is the three-moment framework (before induction, before incision, before the patient leaves the operating room) and that WHO checklist items are not pasted as a mandated verbatim script; the named person who leads each pause; sample completed checklists filed against the unique identification number whose times match the procedure rather than a block of ticks at the end of the list; identity confirmation at the first pause using the two identifiers of the uniform-care policy, matched to consent, operating list and unique identification number, with patient participation while able; the written site-marking method (who marks, with what, which procedures are exempt because laterality does not apply), with marks made before the patient is moved into the operating room, visible after draping, and with marking after the drape or marking the opposite side forbidden; records of the operating list, consent, mark and imaging agreed at the pause before incision, and of procedures stopped when those disagreed rather than started because the list was running late; implant and laterality-specific device confirmation at the pause; near-miss records of wrong patient, missing mark or laterality mismatch caught at the pause, reviewed under the quality-assurance programme at step 8; the location where completed checklists are filed; induction or briefing records showing visiting surgeons use this hospital's checklist and marking method; the audit sample at step 11 of checklists that match the time of the procedure",
        "responsible": "Operating surgeon marks the site and does not start when identity, site or consent is in doubt; the named checklist lead runs each pause out loud; theatre staff refuse a retrospective tick; named theatre quality lead reviews near-misses; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "COP.11.e",
        "requirement": "The procedure is done adhering to standard precautions.",
        "steps": "Steps 5, 11",
        "evidence": "Pointer records that HIC.2 standard precautions apply in the operating theatre and procedure rooms; briefing or induction records for theatre staff; breaches handled under HIC.2 rather than a parallel theatre rule; no restated PPE or hand-hygiene protocol in this document",
        "responsible": "Theatre staff apply HIC.2; Infection Control Team owns the precautions; person in charge of the operating theatre ensures the briefing",
    },
    {
        "oe_code": "COP.11.f",
        "requirement": "Procedures / operation notes, post procedure monitoring and post-operative care plan are documented accurately in the patient record.",
        "steps": "Steps 6, 11",
        "evidence": "Operation or procedure notes against the unique identification number including procedure performed, side, findings, implants or specimens, complications and names of surgeon and assistants, timed as required; recovery surgical observations; written post-operative care plan before the patient leaves recovery",
        "responsible": "Operating surgeon ensures the note and the post-operative plan; recovery staff record surgical observations; information-management policies own the record structure",
    },
    {
        "oe_code": "COP.11.g",
        "requirement": "Appropriate facilities, equipment, instruments and supplies are available in the operating theatre.",
        "steps": "Steps 7, 11",
        "evidence": "Written list of theatres and procedure rooms and the procedures each may hold, aligned with the service directory; equipment inventory for each theatre; records of sterile sets present, in date, with intact indicators, and of cases stopped for an unsterile or missing set; implant availability confirmed before induction; out-of-service equipment labelled and not counted",
        "responsible": "Person in charge of the operating theatre keeps facilities, equipment and supplies available; HIC.6 owns instrument reprocessing; surgeons do not start without the set and implant",
    },
    {
        "oe_code": "COP.11.h",
        "requirement": "The organization shall implement a quality assurance programme.",
        "steps": "Steps 8, 11",
        "evidence": "The named theatre quality lead and the accountability of that role for the programme running; the written quality-assurance measures covering checklist completion as a pause rather than a retrospective tick, consent before incision, documented pre-operative diagnosis, operation notes within the stated time, postponements and cancellations after arrival with reason, near-misses of wrong site, wrong patient or wrong procedure, and any actual such event with immediate report and analysis; the sample or census and the review interval; records showing the programme measured use of the pause rather than possession of the form, and that SSI rates and NHSN definitions were left to the infection-surveillance policy rather than duplicated here; any hospital-set targets recorded as this hospital's decision and not as a numeric mandate of this document; corrective and preventive actions with owner and due date rather than a reminder to be careful; the forum at which findings are reviewed, distinct from infection-control minutes treated as a substitute; the audit sample at step 11 of checklist and consent defects feeding this programme",
        "responsible": "Named theatre quality lead operates the programme and reports findings; head of the institution is accountable that the programme is run; quality or accreditation coordinator audits; Infection Control Team does not own this process look",
    },
    {
        "oe_code": "COP.11.i",
        "requirement": "The organ transplant program shall be in consonance with the legal requirements and shall be conducted ethically.",
        "steps": "Steps 9, 11",
        "evidence": "The recorded hospital decision whether an organ transplant programme is conducted, matching the service directory; if none, that recorded fact and evidence that retrieval or transplantation is not performed here; if a programme exists, registration under the Transplantation of Human Organs and Tissues Act, 1994, Authorization Committee records, living-donor permissions as the Act permits, and the named programme lead",
        "responsible": "Head of the institution for transplant-programme status matching the directory and the Act; named transplant-programme lead where a programme exists; quality or accreditation coordinator audits the match",
    },
    {
        "oe_code": "COP.11.j",
        "requirement": "The organization shall take measures to create awareness regarding organ donation.",
        "steps": "Steps 10, 11",
        "evidence": "The written awareness measures, materials or sessions, and display, including when no transplant programme exists; the named person who responds to a family enquiry and how a referral to the organ-transplant network is made; records kept of the measures",
        "responsible": "Person named at step 10 holds awareness measures; clinical staff do not pressure families; head of the institution is accountable that awareness exists without a transplant programme",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. COP.11 standard text and all ten OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 2 Care of Patients, printed page 67 (PDF page index 73). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: COP.11.a Commitment, COP.11.b Commitment, COP.11.c Commitment, COP.11.d Core, COP.11.e Commitment, COP.11.f Commitment, COP.11.g Commitment, COP.11.h Achievement, COP.11.i Core, COP.11.j Core.
   THREE OEs CARRY THE ASTERISK -- COP.11.a, COP.11.d and COP.11.h. The draft builds three separate deep blocks (step 1 for a; step 4 for d; step 8 for h). COP.11.b, c, e, f, g, i and j are unasterisked and are correspondingly Tier 2. COP.11.d, i and j are Core; only d of those three is asterisked.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the COP.11 page read directly from the extracted page text, and the committed asterisk file. COP.11 was not among the 14 mismatches of the 2026-08-10 audit.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. THREE OF TEN OEs ARE TIER 1. Tier 1: COP.11.a, COP.11.d, COP.11.h -- procedure steps 1, 4 and 8 carry the reasoning (why written guidance rather than habit; why a retrospective tick is not a pause; why process QA is not SSI surveillance). Tier 2: COP.11.b, c, e, f, g, i, j -- requirement and method without extended rationale. Reviewer to note the shallower treatment of b, c, e, f, g, i and j is a DECISION UNDER THE STANDING RULE, not an omission. COP.11.i is Core and still Tier 2 because it is unasterisked; the legal content is accurate and short.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of COP.11.a/d/h against all six approved HIC masters and the AAC.1-AAC.8 drafts. Files: /tmp/aac_drafts/hic1_draft.json through hic6_draft.json, aac1_draft.json through aac8_draft.json. Search terms: operation theatre, surgical, checklist, wrong site, SSI, standard precautions, consent, transplant, organ donation, sterilisation.
   HIC.2 (approved): standard precautions, PPE, hand hygiene, injection, sharps. This draft's Scope and step 5 require adherence in the OT and do not restate PPE or the five moments. Not a contradiction.
   HIC.3 (approved): BMW four colours including anatomical waste; OT as a high-risk housekeeping zone; ventilation as engineering. This draft does not restate colours or HVAC. Not added to the reconciliation list.
   HIC.4 (approved): SSI bundle (bathing, hair, prophylaxis timing, skin prep, normothermia, glycaemia, wound care) and a mention of a completed surgical safety checklist as bundle evidence. This draft owns the operation, site-marking, the checklist as the team's pause, and the notes. Division stated in Scope: completing a checklist is not completing the SSI bundle. Not a contradiction of method; a division of owner. Flagged for the reconciliation pass as a shared artefact (the checklist appears in HIC.4 evidence and is owned here).
   HIC.5 (approved): SSI surveillance, post-discharge detection, NHSN-style definitions. This draft's step 8 process QA does not count SSI. Division stated.
   HIC.6 (approved): instrument reprocessing, sterility at point of use. This draft's step 7 requires availability of sterile sets and stops the case if they are not; it does not write the cycle.
   AAC.1: service directory including whether transplant and which procedures are provided. Steps 1, 7 and 9 align to that directory and do not rewrite it.
   AAC.2: unique identification number. This draft uses it; it does not issue it.
   AAC.7: internal transfer into and out of OT. This draft owns what happens after the patient is received.
   COP.1 (forward): two identifiers at point of care. Step 4 uses them.
   COP.9 / COP.10 (forward): sedation vs anaesthesia vs this document's surgery. Stated in both Scopes as required by the intra-COP division list.
   COP.6 (forward): brain-death / EOL pathway. Step 9 points; does not write it.
3. FORWARD REFERENCES: PRE consent method; IMS record structure; HRM credentialing; FMS theatre engineering; COP.9, COP.10, COP.6, COP.1 as sibling COP documents. Each is a deliberate boundary.
4. T2 QUICK CHECK: COP.11.e vs HIC.2 -- flagged in Scope, follow do not rewrite. COP.11.i/j vs COP.6 brain-death -- flagged in Scope. COP.11.c vs PRE consent -- flagged. COP.11.g vs HIC.6 -- flagged. None is a contradiction with an approved document.

STATUTORY AND EXTERNAL FACTS
5. Transplantation of Human Organs and Tissues Act, 1994 -- cited for the transplant programme (COP.11.i) and as the legal context of donation awareness (COP.11.j). If the hospital does not run a transplant programme, a placeholder records that fact and i's programme rules do not operate; j still applies. No assertion whether {{HOSPITAL_NAME}} is a registered transplant centre. No section number. Commercial dealing forbidden at the level of the Act's general scheme.
6. WHO Guidelines for Safe Surgery 2009 -- chapter reference 64. USED: three-moment framework (before induction, before incision, before leaving the operating room). NOT USED: WHO checklist items pasted as mandated verbatim requirements. Hospital checklist is [Hospital to define]. Haynes 2015 (chapter ref 19) used to support measuring use of the pause. Deutsch 2018 (chapter ref 15) used to extend the pause to laterality-sensitive blocks.
7. WHO Guiding Principles on Human Cell, Tissue and Organ Transplantation -- chapter reference 18; ethical posture only.
8. NO NUMBERS ARE STATED as requirements -- no pause durations, no list-size limits, no pledge quotas, no QA percentage thresholds. Every such value is [Hospital to define].

EDITORIAL POSITIONS TAKEN
9. Step 4's prohibition of completing the checklist later from memory is an editorial position consistent with the asterisk on wrong-site prevention and with Haynes 2015.
10. Step 8's separation of process QA from HIC.5 SSI surveillance is an editorial position required by the overlap rule.
11. Step 9's recorded-absence route is an editorial position required by the drafting brief: a hospital that does not transplant must say so and still do j.
12. Step 3's rule that the operating doctor obtains consent, not a clerk, is an editorial reading of "obtained by the doctor prior to the procedure"; PRE still owns the consent method.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
13. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the Transplantation of Human Organs and Tissues Act, 1994, insofar as this hospital conducts an organ transplant programme or takes measures to create awareness of organ donation -- the statute this document's References actually cite. It does NOT name the Bio-Medical Waste Management Rules, 2016, the Food Safety and Standards Act, 2006, or the Clinical Establishments Act, 2010. BMW of OT waste remains HIC.3.

DELIBERATELY NOT INCLUDED
- PPE, hand hygiene technique, safe injection -- HIC.2.
- SSI bundle measures -- HIC.4.
- SSI surveillance definitions -- HIC.5.
- Instrument reprocessing -- HIC.6.
- Anaesthetic care -- COP.10.
- Procedural sedation -- COP.9.
- WHO checklist items as a mandated script.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 27 fillable blanks in the rendered document: 3 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block, and one in References for the hospital's own surgical-safety checklist) and 24 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 3 of 27; a search for "Hospital to define" without brackets finds all 27, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: whether this hospital conducts an organ transplant programme; where the written procedural and operation-theatre guidance is held; who performs the pre-operative assessment; the pre-operative instructions and where they are documented; how procedural consent is recorded and where it is held; the surgical-safety checklist in use, its items, and who leads each pause; the site-marking method; where completed surgical-safety checklists are filed; how theatre staff are briefed that HIC.2 applies in the OT; who writes the operation note and by when; theatres and procedure rooms and the procedures each may hold; the equipment inventory for each theatre; the named theatre quality lead; the quality-assurance measures, sample or census, and review interval; any quality-assurance targets; the forum at which theatre QA findings are reviewed; the named transplant-programme lead and where statutory records are held, where a programme exists; the organ-donation awareness measures; who responds to a family enquiry about donation; who keeps awareness records; the audit interval for procedural records; the review interval for this policy; the intranet or folder location; and any additional local abbreviation."""

SQL_HEADER = """-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 2, printed page 67
-- (PDF page index 73). Levels: a Commitment, b Commitment, c Commitment, d Core,
-- e Commitment, f Commitment, g Commitment, h Achievement, i Core, j Core.
-- THREE OEs CARRY THE ASTERISK -- COP.11.a, COP.11.d, COP.11.h.
-- UNAPPROVED DRAFT. Do not run this insert until the owner confirms the write.
"""

if __name__ == "__main__":
    emit_and_verify(
        standard_code=STANDARD_CODE,
        chapter=CHAPTER,
        oe_codes=OE_CODES,
        policy_title=POLICY_TITLE,
        purpose=PURPOSE,
        scope=SCOPE,
        policy_statement=POLICY_STATEMENT,
        procedure_steps=PROCEDURE_STEPS,
        responsibility=RESPONSIBILITY,
        references_text=REFERENCES,
        distribution=DISTRIBUTION,
        abbreviations=ABBREVIATIONS,
        disclaimer=DISCLAIMER,
        oe_mapping=OE_MAPPING,
        universal_facts_checklist=UNIVERSAL_FACTS_CHECKLIST,
        version=VERSION,
        revision_history=REVISION_HISTORY,
        tier1_oes=TIER1_OES,
        statute_clause=STATUTE_CLAUSE,
        sql_header=SQL_HEADER,
        json_name="cop11_draft.json",
        sql_name="cop11_insert.sql",
    )
