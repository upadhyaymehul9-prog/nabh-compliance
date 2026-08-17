# -*- coding: utf-8 -*-
"""Builds the MOM.8 master policy draft: JSON for review + SQL for later insert.

UNAPPROVED DRAFT. Do not insert, approve, or write this to Supabase.

THIS IS DRAFTED UNDER THE TWO-TIER DEPTH STANDING RULE (2026-08-10) AND THE
DISCLAIMER STATUTE-MATCHING STANDING RULE (2026-08-17), both in
scripts/master-policy-todos.md.

Tier is decided by doc_required / the asterisk in the official PDF:
  Tier 1 (full treatment): MOM.8.a only
  Tier 2 (lighter pass):   MOM.8.b, MOM.8.c, MOM.8.d, MOM.8.e

ONE of five OEs is asterisked. The draft builds a deep block for a.
b-e are lean.

Official source: NABH Standards for Small Healthcare Organisations, 3rd Edition
(August 2022), Chapter 3 Management of Medication, standard MOM.8 and OEs
MOM.8.a-e, read from the official standards PDF (downloaded 2026-08-17 from the
NABH website's Explore NABH Standards page), printed page 80, PDF page index 86.

Asterisks verified 2026-08-17: scripts/asterisk_extract.py re-run against that
download (self-validation passed, 408 OEs, 132 asterisks, output matched the
committed scripts/shco_oe_asterisks.json on all 408 entries) and the MOM.8 page
read directly. MOM.8.a carries the asterisk; MOM.8.b-e are unasterisked.

THIS IS THE NDPS STANDARD. COP.9 and COP.10 explicitly refused to inherit the
Narcotic Drugs and Psychotropic Substances Act, 1985 as a storage statute and
forwarded cupboard, register and destruction to MOM. This document accepts
that handoff.
"""
from policy_build_common import emit_and_verify, make_disclaimer

STANDARD_CODE = "MOM.8"
CHAPTER = "MOM"
OE_CODES = [
    "MOM.8.a", "MOM.8.b", "MOM.8.c", "MOM.8.d", "MOM.8.e",
]
TIER1_OES = ["MOM.8.a"]

POLICY_TITLE = "Safe Use of Narcotics, Chemotherapeutic Agents and Radioactive Agents"

VERSION = "1.0"
REVISION_HISTORY = [
    {"version": "1.0", "date": "17-08-2026", "description": "Initial release, with a distinct chemotherapeutic-agent handling block (PPE, spill, closed-system transfer or equivalent, extravasation, hazardous waste) separate from the narcotics custody chain."},
]

PURPOSE = """This document sets out how {{HOSPITAL_NAME}} uses narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents in a safe manner: which of those three classes this hospital actually uses; who may prescribe them; how those in use are stored securely; how chemotherapeutic agents, if used, are handled as a cytotoxic process (PPE, spill, closed-system transfer or equivalent, extravasation, hazardous waste) separate from the narcotics custody chain; how radioactive agents used as therapy, if used, are prepared and by whom they are administered; and the record of usage, administration and disposal.

The chapter intent is that safety is paramount when using narcotics, chemotherapeutic agents and radioactive agents. A morphine ampoule in an unlocked drawer, a cytotoxic prepared on a ward bench because the list has started, or a copied oncology SOP in a hospital that does not give chemotherapy, is not that safety. This document is the process that makes the intent operational for the classes this hospital uses, and that records absence against the service directory for the classes it does not.

This document accepts the handoff from the procedural-sedation and anaesthesia policies of {{HOSPITAL_NAME}}: the clinical act of sedating or anaesthetising remains those policies; the Narcotic Drugs and Psychotropic Substances Act, 1985 cupboard, register and destruction live here. Chemotherapeutic-agent handling is not implied by that custody chain; it is written as its own step."""

SCOPE = """This policy applies to every location at {{HOSPITAL_NAME}} in which a narcotic drug, a psychotropic substance, a chemotherapeutic agent or a radioactive agent used as therapy is prescribed, stored, prepared, administered or disposed of. It binds the clinicians who prescribe those agents, the staff who hold keys or access to secure storage, the persons who prepare chemotherapy or radioactive agents where those services exist, the persons who administer them, and whoever keeps the usage, administration and disposal record.

It covers: safe use of those three classes; prescription by appropriate caregivers; secure storage; proper and safe preparation of chemotherapeutic agents, including cytotoxic PPE, spill management, closed-system transfer or equivalent, extravasation response and hazardous-waste disposal, as a block distinct from narcotics custody; proper and safe preparation of radioactive agents used as therapy and administration of those two classes by qualified personnel; and a proper record of usage, administration and disposal of all three classes.

A class this hospital does not provide is recorded as absent against the service directory of {{HOSPITAL_NAME}}. Absence is a record. It is not a bunker, a hot laboratory, a cytotoxic reconstitution room, or a preparation SOP invented for assessment.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Ordinary storage of medicines — clean, safe, secure, manufacturer's recommendations, look-alike and sound-alike, emergency stock — is governed by the medication-storage policy of {{HOSPITAL_NAME}} (MOM.2, sibling). This document owns secure storage of the three classes named in MOM.8.c. MOM.2 does not write the NDPS cupboard. This document does not rewrite general pharmacy storage.
- Who may prescribe medicines generally, and how orders are written, are governed by the prescribing and order-writing policies of {{HOSPITAL_NAME}} (MOM.3 and MOM.4, siblings). This document owns that these three classes are prescribed by appropriate caregivers. MOM.3 does not name the NDPS authorised prescriber list.
- Dispensing of ordinary medicines is governed by the dispensing policy of {{HOSPITAL_NAME}} (MOM.5, sibling). The usage, administration and disposal record of these three classes is this document (MOM.8.e). MOM.5 does not write the NDPS register.
- Administration of ordinary medicines is governed by the administration policy of {{HOSPITAL_NAME}} (MOM.6, sibling). Preparation of chemotherapeutic agents, including the cytotoxic PPE, spill, closed-system or equivalent, extravasation and hazardous-waste method, preparation of radioactive agents used as therapy, and administration of those two by qualified personnel, are this document (MOM.8.d). MOM.6 does not write a cytotoxic reconstitution method.
- Monitoring after a dose, and capture of near miss, medication error and adverse drug reaction, including events involving these classes, are governed by the post-medication monitoring and medication-event policy of {{HOSPITAL_NAME}} (MOM.7, sibling). This document does not write the near-miss book.
- Procedural sedation is governed by the procedural-sedation policy of {{HOSPITAL_NAME}} (COP.9). Anaesthesia is governed by the anaesthesia policy of {{HOSPITAL_NAME}} (COP.10). Those documents own the clinical act. They explicitly refused to inherit the Narcotic Drugs and Psychotropic Substances Act, 1985 as a storage statute. This document accepts that handoff: cupboard, register and destruction of narcotic drugs and psychotropic substances used as sedatives or anaesthetics are written here. COP.9 and COP.10 do not write them. This document does not write sedation method or anaesthesia method.
- Clinical procedures and operations, including chemotherapy given in the operation theatre, are governed for the surgical act by the procedures-and-operation-theatre policy of {{HOSPITAL_NAME}} (COP.11). Preparation of the chemotherapeutic agent and administration by a qualified person remain this document even when the dose is given in theatre.
- Imaging services, including legal requirements for diagnostic radiology, and the imaging radiation-safety programme, are governed by the imaging and laboratory-and-imaging-safety policies of {{HOSPITAL_NAME}} (AAC.5 and AAC.6). Diagnostic radiology licences stay there. This document owns radioactive AGENTS used as therapy (for example iodine-131). A hospital that takes X-rays and does not give therapeutic unsealed sources has AAC.5/AAC.6 work and an MOM.8 recorded absence for radioactive agents. Mixing the two invents a nuclear-medicine service the directory does not define.
- The written definition of healthcare services is governed by the definition-and-display policy of {{HOSPITAL_NAME}} (AAC.1). Whether this hospital provides chemotherapy, and whether it uses radioactive agents as therapy, must match that directory. This document records absence against that directory; it does not invent a service.
- Colour-coded waste from cytotoxic or chemotherapy material is governed by the support-services infection-control policy of {{HOSPITAL_NAME}} (HIC.3, approved). This policy requires that unused dose, empty vials, contaminated sharps, contaminated PPE and spill debris from chemotherapeutic agents enter that stream and are not general waste; it does not restate colour categories, storage times or common-treatment-facility handover. Chemo waste is not named in this document's statutory paragraph.
- Donning and doffing of personal protective equipment are governed by the infection-prevention-and-control-practices policy of {{HOSPITAL_NAME}} (HIC.2, approved). This document names the extra hazardous-drug PPE items worn when preparing or administering chemotherapeutic agents. HIC.2 standard-precaution PPE is not, by itself, cytotoxic PPE. Blood-or-body-fluid spill method remains HIC.2. Building chemical or mercury spills remain under the facility policies of {{HOSPITAL_NAME}} (FMS, not yet drafted). The written cytotoxic-spill method, closed-system transfer or equivalent, and extravasation response are this document (MOM.8.d).
- Who may practise as a registered medical practitioner is governed by the National Medical Commission Act, 2019 and State Medical Council registration, verified under the human resource policies of {{HOSPITAL_NAME}} (HRM, not yet drafted). This policy requires appropriate caregivers and qualified personnel for these classes; it does not restate the credentialing file.
- The medical record itself is governed by the information-management policies of {{HOSPITAL_NAME}} (IMS, not yet drafted). This policy owns the usage, administration and disposal content written for these classes."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} uses narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents safely, and only the classes it actually uses. A class that is not a defined service is recorded as absent against the service directory. Absence is not a copied bunker.

{{HOSPITAL_NAME}} requires that those classes in use are prescribed by appropriate caregivers.

{{HOSPITAL_NAME}} stores those classes in use securely. The Narcotic Drugs and Psychotropic Substances Act, 1985 governs narcotic drugs and psychotropic substances used here. This document is where that Act's cupboard, register and destruction live.

{{HOSPITAL_NAME}} requires that chemotherapeutic agents, where used, are prepared properly and safely and administered by qualified personnel, under a written cytotoxic-handling method that names extra hazardous-drug PPE, a cytotoxic-spill method, a closed-system transfer device or equivalent, an extravasation response, and hazardous-waste disposal. That method is not the narcotics cupboard or register. Radioactive agents used as therapy, where used, are prepared and administered under their own step, not under the cytotoxic-spill method. A hospital that does not use those agents does not invent a preparation room.

{{HOSPITAL_NAME}} keeps a proper record of usage, administration and disposal of each class in use.

{{HOSPITAL_NAME}} does not treat diagnostic radiology as a radioactive agent used as therapy, and does not treat ordinary medication storage as the secure storage of these three classes."""

PROCEDURE_STEPS = [
"""1. Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are used safely

Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are used safely at {{HOSPITAL_NAME}}. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask how this hospital uses those three classes, and the answer must be a written method for the classes it actually uses, plus a recorded absence for any class it does not — not a copied oncology or nuclear-medicine file in a hospital that provides neither.

The reason safe use is written as one step covering three classes is that the book names them together, and that each class fails in a different way if it is treated as ordinary ward stock. A narcotic that can be taken from an unlocked drawer is diverted or given without an account. A chemotherapeutic agent reconstituted on a bench without the protection and the person this hospital has named is a harm to the patient and to the staff. A radioactive agent used as therapy without the licence and the person this hospital has named is a radiation event, not a medication round. The common error is the opposite of those three failures: a small hospital that uses morphine, does not give chemotherapy, and does not give iodine-131, keeping a full cytotoxic-bunker SOP and a hot-lab SOP "because the standard lists three classes". That SOP is fiction. Fiction is not safe use. Safe use of an unused class is the recorded absence.

Which of the three classes this hospital uses, and the recorded absence against the service directory of {{HOSPITAL_NAME}} for any class it does not use, are [Hospital to define — which of narcotic drugs and psychotropic substances, chemotherapeutic agents, and radioactive agents used as therapy this hospital uses, and the recorded absence against the service directory for any class it does not]. Narcotic drugs and psychotropic substances will almost always be in use: an opioid, a benzodiazepine, or another scheduled medicine used for pain, seizure, sedation or anaesthesia. The Narcotic Drugs and Psychotropic Substances Act, 1985 therefore applies if any such medicine is used. Chemotherapeutic agents are in use only if a defined service of this hospital gives them. Radioactive agents are in use only if this hospital uses them as therapy. Diagnostic imaging under the imaging policies of {{HOSPITAL_NAME}} is not that use.

This document accepts the handoff from the procedural-sedation and anaesthesia policies of {{HOSPITAL_NAME}}. Those policies own the clinical act of sedating or anaesthetising. They refused to inherit the Narcotic Drugs and Psychotropic Substances Act as a wholesale storage statute. Cupboard, register and destruction of the narcotic drugs and psychotropic substances used in sedation or anaesthesia are written in the steps that follow, not in COP.9 or COP.10. This step does not write sedation method and does not write anaesthesia method.

This step does not print the NDPS schedules, does not print a destruction method as a numbered mandate, and does not print chemotherapeutic doses. Those values, where a class is in use, are hospital-defined at the later steps: the cupboard and who holds access at step 3, the cytotoxic-handling method at step 4, the radioactive-agent method at step 5, the register at step 6. What this step requires is that the hospital names the classes it uses, records absence for the rest, and applies the later steps only to the classes in use.

The written safe-use guidance — the named classes, the recorded absences, and the pointer to steps 2 to 6 for the classes in use — is held at [Hospital to define — where the written safe-use guidance for these three classes is held]. A location that holds a class this hospital has not named does not use it.""",

"""2. Prescribed by appropriate caregivers

Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents that this hospital uses are prescribed by appropriate caregivers. A class recorded as absent at step 1 is not prescribed here.

Who may prescribe each class in use is [Hospital to define — who may prescribe narcotic drugs and psychotropic substances, chemotherapeutic agents, and radioactive agents, for each class this hospital uses]. Appropriateness is current professional registration, verified under the human resource policies of {{HOSPITAL_NAME}}, plus any further authorisation this hospital requires for that class (for example a named NDPS authorised prescriber, a named oncology prescriber). This step does not restate the credentialing file. A person who may prescribe ordinary medicines is not, by that fact alone, an appropriate caregiver for every class in this standard.

Prescription of these classes still follows the prescribing and order-writing policies of {{HOSPITAL_NAME}} for how the order is written. This step owns who is allowed to write it.""",

"""3. Stored securely

Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents that this hospital uses are stored securely. The official OE text reads "agents drugs are stored"; the requirement this hospital meets is secure storage of those agents. A class recorded as absent at step 1 is not stored here, and this step does not invent a cupboard for it.

How and where each class in use is stored securely — the cupboard or other secure location, who holds access, and how access is recorded — are [Hospital to define — how and where each class in use is stored securely, including the cupboard or location and who holds access]. This document does not print an NDPS schedule table and does not mandate a numbered lock type. It requires that storage of these classes is secure in a way ordinary medication storage under the medication-storage policy of {{HOSPITAL_NAME}} is not asked to be, and that narcotic drugs and psychotropic substances used here are stored in a manner that can satisfy the Narcotic Drugs and Psychotropic Substances Act, 1985. Chemotherapeutic agents in use are stored so that they are not handled as ordinary ward stock. Handling after they leave that storage — PPE, spill, closed-system transfer or equivalent, extravasation and hazardous waste — is step 4, not this cupboard step. Radioactive agents used as therapy, if any, are stored under the conditions the Atomic Energy (Radiation Protection) Rules, 2004 and the authorisation from the Atomic Energy Regulatory Board require; diagnostic-radiology rooms remain under the imaging policies.

Keys or access left in a drawer, a narcotic kept in the general drug trolley overnight, or a cytotoxic stored next to look-alike ordinary ampoules, is not secure storage of these classes.""",

"""4. Chemotherapeutic and cytotoxic agents: PPE, spill, closed-system transfer or equivalent, extravasation, and hazardous waste

Chemotherapeutic agents, where this hospital uses them, are prepared properly and safely and administered by qualified personnel. This step is the cytotoxic-handling method. It is not the narcotic-drugs custody chain of steps 3 and 6. If chemotherapeutic agents are recorded as absent at step 1, this entire step is that recorded absence: no extra PPE list, no spill kit, no closed-system method, no extravasation drill, and no cytotoxic-waste stream invented for assessment.

Who may prepare chemotherapeutic agents, and where preparation is done, are [Hospital to define — who may prepare chemotherapeutic agents and where preparation is done, or the recorded absence if chemotherapeutic agents are not used]. Who may administer them is [Hospital to define — who may administer chemotherapeutic agents, or the recorded absence if chemotherapeutic agents are not used]. This document does not print chemotherapeutic doses and does not print a reconstitution recipe.

PPE. Staff who prepare or administer chemotherapeutic agents wear the extra hazardous-drug PPE this hospital has named, not only the standard-precaution PPE of the infection-prevention policy of {{HOSPITAL_NAME}}. The extra items — for example chemo-rated gloves, a protective gown, and eye or face protection as this hospital defines them — are [Hospital to define — the extra hazardous-drug PPE items worn when preparing or administering chemotherapeutic agents, or the recorded absence if chemotherapeutic agents are not used]. Donning and doffing method remains the infection-prevention policy; this step names the extra items. Standard-precaution PPE is not, by itself, cytotoxic PPE.

Spill. A written cytotoxic-spill method is used for a leak or splash of a chemotherapeutic agent: stop, contain, who attends, and where the kit is. That method is [Hospital to define — the written cytotoxic-spill method, including who attends and the location and contents of the spill kit, or the recorded absence if chemotherapeutic agents are not used]. This is not the blood-or-body-fluid spill method of the infection-prevention policy. Building chemical or mercury spills remain under the facility policies of {{HOSPITAL_NAME}} (FMS, not yet drafted). Contaminated linen and PPE from a cytotoxic spill enter the waste stream in the hazardous-waste paragraph of this step.

Closed-system transfer or equivalent. Preparation uses a closed-system transfer device or an equivalent this hospital has named that limits aerosol and splash — for example a designated cabinet plus a defined technique. Which of those this hospital uses is [Hospital to define — whether a closed-system transfer device or a named equivalent that limits aerosol and splash is used for chemotherapeutic preparation, or the recorded absence if chemotherapeutic agents are not used]. This document does not name a brand and does not treat any numbered pharmacy chapter as an NABH mandate.

Extravasation. If a chemotherapeutic infusion leaks into tissue, the infusion is stopped, the named person is called, the site is managed as this hospital has written, and the event is recorded. Who is called, and the written site-management method, are [Hospital to define — who is called and the written site-management method when a chemotherapeutic infusion extravasates, or the recorded absence if chemotherapeutic agents are not used]. This document does not print a vesicant list and does not name antidotes as a mandate. Capture of the event as a near miss, medication error or adverse drug reaction remains the post-medication monitoring policy of {{HOSPITAL_NAME}}.

Hazardous waste. Unused dose, empty vials, contaminated sharps, contaminated PPE and spill debris from chemotherapeutic agents enter the biomedical-waste stream of {{HOSPITAL_NAME}}. They are not general waste. Colour categories, storage times and common-treatment-facility handover are not restated here.

Narcotic drugs and psychotropic substances are not reconstituted as chemotherapy. Their safe use and secure storage are steps 1 and 3; their administration as a clinical act of sedation or anaesthesia remains under those clinical policies; administration as analgesia remains under the administration policy of {{HOSPITAL_NAME}} with the account at step 6.

A chemotherapeutic dose prepared in the operation theatre is still prepared and administered under this step, including the PPE, spill, closed-system or equivalent, extravasation and waste paragraphs. The surgical act is the procedures-and-operation-theatre policy of {{HOSPITAL_NAME}}.""",

"""5. Radioactive agents used as therapy: prepared properly and safely, and administered by qualified personnel

Radioactive agents used as therapy, where this hospital uses them, are prepared properly and safely and administered by qualified personnel. If radioactive agents used as therapy are recorded as absent at step 1, this step is that recorded absence. It is not a hot laboratory, a nuclear-medicine SOP, or a qualified-person list invented for assessment. Diagnostic radiology remains under the imaging policies of {{HOSPITAL_NAME}}.

Who may prepare or handle radioactive agents used as therapy, and where that is done, are [Hospital to define — who may prepare or handle radioactive agents used as therapy and where that is done, or the recorded absence if radioactive agents are not used as therapy]. Who may administer them is [Hospital to define — who may administer radioactive agents used as therapy, or the recorded absence if radioactive agents are not used as therapy].

Radiation-protection PPE and contamination response follow the method aligned with the Atomic Energy (Radiation Protection) Rules, 2004 and the authorisation from the Atomic Energy Regulatory Board. They are not the cytotoxic PPE, spill kit, or closed-system method of step 4. Unused dose and contaminated material from therapeutic radioactive agents enter the waste stream this hospital has defined under those authorisations and the biomedical-waste policy of {{HOSPITAL_NAME}}; they are not general waste. Colour categories are not restated here.""",

"""6. Record of usage, administration and disposal

A proper record is kept of the usage, administration and disposal of narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents that this hospital uses. A class recorded as absent at step 1 has no usage to record, and this step does not invent a register for it.

How usage, administration and disposal of each class in use are recorded — the register or other record, what each entry contains, and who writes it — are [Hospital to define — how usage, administration and disposal of each class in use are recorded]. This document does not print a destruction method as a numbered mandate. Destruction or disposal of narcotic drugs and psychotropic substances, where it occurs, is recorded here in the manner this hospital has defined so that it can satisfy the Narcotic Drugs and Psychotropic Substances Act, 1985. Disposal of chemotherapeutic waste as waste is the biomedical-waste policy of {{HOSPITAL_NAME}}; the account that a given dose was used, returned or discarded is this record.

A register that does not match the cupboard, or a disposal that is not written, is not a proper record.""",

"""7. Records, review and the order of operations

The named classes, the recorded absences against the service directory, the authorised prescribers, the secure-storage arrangement, the cytotoxic-handling method at step 4 where chemotherapeutic agents are used, the radioactive-agent method at step 5 where that class is used, and the usage-administration-disposal record of each class in use, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for narcotic, chemotherapeutic and radioactive-agent records] for: classes in use matching the service directory, and unused classes recorded as absent rather than documented as a bunker that does not exist; prescription only by the appropriate caregivers; secure storage of classes in use; chemotherapeutic handling only where that class is in use, including extra hazardous-drug PPE, a written cytotoxic-spill method, a closed-system transfer device or equivalent, an extravasation response, and hazardous waste entering the biomedical-waste stream; preparation and administration of radioactive agents used as therapy only where that class is in use and only by the named persons; a usage, administration and disposal record that matches the cupboard; and no diagnostic-radiology licence offered as MOM.8 radioactive-agent evidence.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a class was used that the directory does not define, a narcotic was found outside secure storage, a destruction was unrecorded, a chemotherapeutic agent was prepared without the extra PPE or spill method of step 4, or a copied chemo SOP was found in a hospital that does not give chemotherapy, or when the storage, administration, sedation, anaesthesia, imaging or infection-control policies that this document hands work to are revised.""",
]

RESPONSIBILITY = """The head of the institution is accountable for {{HOSPITAL_NAME}} using only the named classes, storing them securely, and keeping the usage, administration and disposal record, and for recorded absence where a class is not a defined service.

The named lead for these three classes authors and keeps current the written safe-use guidance at step 1, the authorised-prescriber list at step 2, the secure-storage arrangement at step 3, the cytotoxic-handling method at step 4 where chemotherapeutic agents are used, the radioactive-agent method at step 5 where that class is used, and the register method at step 6. The named lead is [Hospital to define — the named lead for narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents].

Prescribers of these classes prescribe only if they are on the appropriate-caregiver list. Staff who hold access to secure storage do not leave that access unattended. Persons who prepare or administer chemotherapeutic agents do so only if named at step 4, and apply the extra PPE, spill, closed-system or equivalent, extravasation and waste paragraphs of that step. Persons who prepare or administer radioactive agents used as therapy do so only if named at step 5.

The quality or accreditation coordinator audits the records at step 7 and reports findings to the head of the institution.

All staff are expected to treat an unlocked narcotic, a chemotherapeutic preparation by an unnamed person or without the extra PPE of step 4, and a copied bunker for a class this hospital does not use, as defects, and to report them."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.8.
- Narcotic Drugs and Psychotropic Substances Act, 1985 — insofar as it governs possession, storage, account and disposal of narcotic drugs and psychotropic substances used at this hospital. This document does not print the schedules and does not print a destruction method as a numbered mandate.
- Drugs and Cosmetics Act, 1940, and the Drugs and Cosmetics Rules, insofar as chemotherapeutic agents used here are medicines.
- Atomic Energy Act, 1962, and the Atomic Energy (Radiation Protection) Rules, 2004, and authorisations issued by the Atomic Energy Regulatory Board — insofar as this hospital uses radioactive agents as therapy. Diagnostic radiology remains under the imaging policies of {{HOSPITAL_NAME}}. A hospital that does not use radioactive agents as therapy records that absence against the service directory and does not hold these authorisations for a service it does not provide.
- Internal documents of {{HOSPITAL_NAME}}: the written safe-use guidance and recorded absences; the appropriate-caregiver lists; the secure-storage arrangement; the cytotoxic-handling method (extra hazardous-drug PPE, spill, closed-system transfer or equivalent, extravasation, hazardous waste) where chemotherapeutic agents are used; the qualified-preparer and administrator lists where radioactive agents are used as therapy; the usage, administration and disposal record; the service directory; the medication-storage, prescribing, dispensing and administration policies; the procedural-sedation and anaesthesia policies; the imaging and radiation-safety policies; and the infection-prevention and biomedical-waste policies."""

DISTRIBUTION = """Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: pharmacy; every location that holds a narcotic drug or psychotropic substance; the operation theatre and anaesthesia; the emergency area; any location that prepares or administers chemotherapy, if that service exists; any location that uses radioactive agents as therapy, if that service exists; nursing administration; and the named lead.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The safe-use guidance, the cupboard access list and the register — the working documents this policy requires — are held where those classes are used.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

AERB — Atomic Energy Regulatory Board
CSTD — closed-system transfer device
NDPS — Narcotic Drugs and Psychotropic Substances (Act, 1985)

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

STATUTE_CLAUSE = (
    "the Narcotic Drugs and Psychotropic Substances Act, 1985, the Drugs and Cosmetics "
    "Act, 1940 insofar as chemotherapeutic agents are medicines, and the Atomic Energy "
    "Act, 1962 and the Atomic Energy (Radiation Protection) Rules, 2004 insofar as this "
    "hospital uses radioactive agents as therapy"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.8.a",
        "requirement": "Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are used safely.",
        "steps": "Steps 1, 7",
        "evidence": "The written safe-use guidance naming which of the three classes this hospital actually uses, with a recorded absence against the service directory for any class it does not use, showing that absence is a record and not a copied cytotoxic bunker, hot laboratory or nuclear-medicine SOP invented for assessment, and showing that narcotic drugs and psychotropic substances remain in scope if any such medicine is used (as they almost always are) because the Narcotic Drugs and Psychotropic Substances Act, 1985 applies to that use; the recorded acceptance of the handoff from the procedural-sedation and anaesthesia policies, that those policies own the clinical act and that cupboard, register and destruction of narcotic drugs and psychotropic substances live in this document, not in COP.9 or COP.10; the recorded distinction that chemotherapeutic handling (extra hazardous-drug PPE, spill, closed-system transfer or equivalent, extravasation, hazardous waste) is the step-4 block and is not implied by the narcotics register; the recorded distinction that diagnostic radiology licences and imaging radiation-safety devices remain under the imaging and laboratory-and-imaging-safety policies and are not evidence of radioactive agents used as therapy; the recorded refusal to print NDPS schedule tables, destruction methods as numbered mandates, or chemotherapeutic doses in this document, those values being hospital-defined at the cupboard, cytotoxic-handling, radioactive-agent and register steps; the location where the written guidance is held; induction or briefing records showing staff in locations that hold these classes have been shown the named classes and the absences; the audit sample at step 7 of classes in use matching the service directory and unused classes recorded as absent rather than documented as a bunker that does not exist",
        "responsible": "Named lead holds the written safe-use guidance, named classes and recorded absences; head of the institution is accountable that unused classes are not invented as facilities; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.8.b",
        "requirement": "Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are prescribed by appropriate caregivers.",
        "steps": "Steps 2, 1, 7",
        "evidence": "The named appropriate caregivers who may prescribe each class in use, with current professional registration used from human-resource verification and any further hospital authorisation for that class; sample prescriptions showing a person not on that list did not prescribe; the recorded absence for a class not in use; the recorded division that MOM.3/MOM.4 own how the order is written and this step owns who may write it for these classes",
        "responsible": "Named lead holds the appropriate-caregiver lists; prescribers apply them; human resource function verifies registration; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.8.c",
        "requirement": "Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents drugs are stored securely.",
        "steps": "Steps 3, 1, 7",
        "evidence": "The written secure-storage arrangement for each class in use (cupboard or location, who holds access, how access is recorded), showing storage stricter than ordinary medication storage and able to satisfy the Narcotic Drugs and Psychotropic Substances Act, 1985 for narcotics and psychotropics in use; the recorded absence of a cupboard for a class not in use; the recorded distinction that diagnostic-radiology rooms are not this storage; the recorded distinction that chemotherapeutic handling after storage is step 4, not this cupboard step; the audit sample at step 7 of secure storage of classes in use",
        "responsible": "Named lead holds the secure-storage arrangement; staff who hold access apply it; MOM.2 owns ordinary medication storage; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.8.d",
        "requirement": "Chemotherapy and radioactive agents are prepared properly and safely, and administered by qualified personnel.",
        "steps": "Steps 4, 5, 1, 7",
        "evidence": "The named persons who may prepare and who may administer chemotherapeutic agents, where preparation is done, the extra hazardous-drug PPE items, the written cytotoxic-spill method including who attends and the spill-kit location and contents, the closed-system transfer device or named equivalent that limits aerosol and splash, the extravasation response (who is called and the written site-management method), and unused dose, empty vials, contaminated sharps, contaminated PPE and spill debris entering the biomedical-waste stream and not general waste — or the recorded absence of this entire block if chemotherapeutic agents are not used; the named persons who may prepare or handle and who may administer radioactive agents used as therapy, and where that is done, or the recorded absence if that class is not used, showing radiation-protection PPE and contamination response follow the AERB-aligned method and are not the cytotoxic method of step 4; sample preparation and administration records against the unique identification number where a class is in use; records showing a chemotherapeutic dose in the operation theatre was still prepared and administered under step 4; the audit sample at step 7 of preparation and administration only where the class is in use and only by the named persons",
        "responsible": "Named lead holds the cytotoxic-handling method and the radioactive-agent lists where those classes are used; named preparers and administrators apply them; HIC.2 owns donning and doffing; HIC.3 owns the waste stream and colours; COP.11 owns the surgical act; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.8.e",
        "requirement": "A proper record is kept of the usage, administration and disposal of narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents.",
        "steps": "Steps 6, 1, 7",
        "evidence": "The written method for recording usage, administration and disposal of each class in use (register or other record, contents of an entry, who writes it), showing a record that can satisfy the Narcotic Drugs and Psychotropic Substances Act, 1985 for narcotics and psychotropics without a destruction method printed as a numbered mandate; sample entries matching the cupboard; the recorded absence of a register for a class not in use; the recorded distinction that cytotoxic waste colours remain under the biomedical-waste policy while the account of a given dose is this record; the audit sample at step 7 of a usage, administration and disposal record that matches the cupboard",
        "responsible": "Named lead holds the register method; staff who use, administer or dispose of a class in use write the entry; quality or accreditation coordinator audits",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. MOM.8 standard text and all five OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 3 Management of Medication, printed page 80 (PDF page index 86). Page header quoted from the book: "Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are used in a safe manner." The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: MOM.8.a Commitment, MOM.8.b Commitment, MOM.8.c Commitment, MOM.8.d Commitment, MOM.8.e Commitment.
   ONE OE CARRIES THE ASTERISK -- MOM.8.a. The draft builds one deep block (step 1 for a). MOM.8.b, MOM.8.c, MOM.8.d and MOM.8.e are unasterisked and are correspondingly Tier 2.
   Official OE MOM.8.c text includes the awkward wording "agents drugs are stored"; mapping requirement quotes that official text; procedure prose states the requirement as secure storage of those agents.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the MOM.8 page read directly from the extracted page text, and the committed asterisk file. MOM.8 was not among the 14 mismatches of the 2026-08-10 audit.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. ONE OF FIVE OEs IS TIER 1. Tier 1: MOM.8.a only -- procedure step 1 carries the reasoning (why a copied bunker for an unused class is not safe use, why NDPS still applies if any narcotic or psychotropic is used, why this document accepts the COP.9/COP.10 storage handoff). Tier 2: MOM.8.b (step 2), MOM.8.c (step 3), MOM.8.d (steps 4 and 5), MOM.8.e (step 6) -- requirement and method without extended rationale. Step 4 is a dedicated cytotoxic-handling block added 2026-08-17 at the owner's request before approval, still written as T2 method not T1 rationale, because MOM.8.d is unasterisked. Reviewer to note the shallower treatment of b-e is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of MOM.8.a against the approved HIC masters and the AAC/COP drafts. Search terms: NDPS, narcotic, psychotropic, chemotherapy, cytotoxic, radioactive, AERB, cupboard, controlled drug.
   COP.9 and COP.10 -- CRITICAL HANDOFF ACCEPTED. Those drafts refused to inherit NDPS as a storage statute and forwarded cupboard/register/destruction to MOM. This document states in Purpose, Scope and step 1 that it accepts that handoff. Clinical sedation/anaesthesia method stays COP. Flagged so those drafts' forward-ref is now landed.
   MOM.2 -- general storage vs MOM.8.c secure storage of these three classes. Stated in Scope. Flagged for the MOM.2 drafter to mirror.
   MOM.3/4 -- prescribing generally vs MOM.8.b appropriate caregivers for these classes. Stated in Scope.
   MOM.5 -- dispensing vs MOM.8.e usage/disposal record. Stated in Scope.
   MOM.6 -- administration vs MOM.8.d chemo/radioactive preparation and qualified admin. Stated in Scope.
   MOM.7 -- NM/ME/ADR capture remains MOM.7 even when the drug is one of these classes, including extravasation recorded as an event.
   COP.11 -- chemo in OT is still MOM.8 step-4 handling; surgical act is COP.11. Stated in Scope and step 4.
   AAC.5/AAC.6 -- diagnostic radiology licences and imaging radiation safety stay there; MOM.8 radioactive AGENTS are therapy (I-131 etc.). If none, record absence. Stated in Scope, Policy statement and steps 1 and 5.
   AAC.1 -- unused chemo or radioactive services recorded against the service directory, not invented. Stated in Scope and step 1.
   HIC.3 -- unused dose, empty vials, contaminated sharps, contaminated PPE and spill debris enter the HIC.3 stream; colours not restated; BMW not in P2. Stated in Scope and steps 4-6.
   HIC.2 -- donning and doffing remain HIC.2; extra hazardous-drug PPE is named at step 4; standard-precaution PPE is not by itself cytotoxic PPE. Blood/body-fluid spill remains HIC.2. Stated in Scope and step 4.
   FMS -- building chemical or mercury spills remain FMS (undrafted); cytotoxic spill at preparation/administration is step 4.
3. FORWARD REFERENCES: MOM.2 storage; MOM.3/4/5/6 siblings; AAC.5/6 imaging; PRE/HRM/IMS; FMS chemical spill. Each is a deliberate boundary.
4. T2 QUICK CHECK: MOM.8.b vs MOM.3 -- flagged. MOM.8.c vs MOM.2 -- flagged. MOM.8.d vs MOM.6, HIC.2, HIC.3 and FMS -- flagged. MOM.8.e vs MOM.5 and HIC.3 -- flagged. Nothing added to the HIC reconciliation list.

STATUTORY AND EXTERNAL FACTS
5. Narcotic Drugs and Psychotropic Substances Act, 1985 -- named in P2 and References. Cupboard, register and destruction are hospital-defined; this draft does NOT print schedule tables or a numbered destruction method. No section number. NDPS is not applied to chemotherapeutic or radioactive agents.
6. Drugs and Cosmetics Act, 1940 -- named in P2 insofar as chemotherapeutic agents are medicines. Chemo waste is HIC.3, not this P2.
7. Atomic Energy Act, 1962 and Atomic Energy (Radiation Protection) Rules, 2004 / AERB -- named in P2 and References insofar as this hospital uses radioactive agents as therapy. A hospital that does not use them records absence and does not invent a licence. Diagnostic radiology stays AAC.5.
8. NO NUMBERS ARE STATED as requirements -- no lock counts, no chemo doses, no destruction recipes, no schedule lists, no USP chapter numbers, no CSTD brand. Every such value is [Hospital to define].
9. Bio-Medical Waste Management Rules, 2016, Food Safety and Standards Act, 2006, and Clinical Establishments Act, 2010 are NOT named in P2. Chemo waste is pointed at HIC.3.

EDITORIAL POSITIONS TAKEN
10. Step 1's rule that safe use of an unused class is recorded absence, not a copied bunker, is an editorial position required by the owner's instruction.
11. Step 1's acceptance of the COP.9/COP.10 NDPS storage handoff is an editorial position required by those drafts and by the owner's instruction.
12. Step 3's reading of the awkward official "agents drugs are stored" as secure storage of those agents is an editorial clarification; mapping requirement keeps the official wording.
13. Step 4 as a distinct cytotoxic-handling block (PPE, spill, CSTD or equivalent, extravasation, hazardous waste), split from narcotics custody and from radioactive-agent handling at step 5, is an editorial position required by the owner's 2026-08-17 review before approval. MOM.8.d remains Tier 2.
14. Step 4's statements that narcotics are not reconstituted as chemotherapy, that HIC.2 standard-precaution PPE is not by itself cytotoxic PPE, that a CSTD brand and a numbered pharmacy chapter are not NABH mandates, and that chemo in the OT is still this step, are editorial positions.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
15. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the NDPS Act 1985, the Drugs and Cosmetics Act 1940 insofar as chemotherapeutic agents are medicines, and the Atomic Energy Act 1962 and Atomic Energy (Radiation Protection) Rules 2004 insofar as this hospital uses radioactive agents as therapy -- the statutes this document's References actually rely on. It does NOT name BMW Rules 2016, FSS Act 2006, or CEA 2010. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- General medication storage -- MOM.2.
- Ordinary prescribing, order-writing, dispensing, administration -- MOM.3-6.
- Sedation method -- COP.9. Anaesthesia method -- COP.10.
- Diagnostic radiology licences and imaging radiation safety -- AAC.5 / AAC.6.
- Cytotoxic waste colour categories -- HIC.3.
- PPE donning and doffing -- HIC.2. Extra hazardous-drug PPE items are named here.
- Blood/body-fluid spill -- HIC.2. Building chemical or mercury spill -- FMS.
- NM/ME/ADR capture -- MOM.7.
- NDPS schedule tables, numbered destruction methods, chemotherapeutic doses.
- USP <800> or any numbered pharmacy chapter as an NABH mandate; a named CSTD brand; a vesicant list or named antidotes as mandate.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 19 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 17 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 19; a search for "Hospital to define" without brackets finds all 19, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: which of the three classes it uses and the recorded absence for any class it does not; where the written safe-use guidance is held; who may prescribe each class in use; how and where each class in use is stored securely; who may prepare chemotherapeutic agents and where, or recorded absence; who may administer chemotherapeutic agents, or recorded absence; the extra hazardous-drug PPE items; the written cytotoxic-spill method including who attends and the spill-kit location and contents; whether a closed-system transfer device or a named equivalent is used; who is called and the written site-management method on extravasation; who may prepare or handle radioactive agents used as therapy and where, or recorded absence; who may administer radioactive agents used as therapy, or recorded absence; how usage, administration and disposal of each class in use are recorded; the named lead; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation."""

SQL_HEADER = """-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 3, printed page 80
-- (PDF page index 86). Levels: a Commitment, b Commitment, c Commitment, d Commitment,
-- e Commitment.
-- ONE OE CARRIES THE ASTERISK -- MOM.8.a.
-- THIS IS THE NDPS STANDARD. COP.9/COP.10 storage handoff is accepted here.
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
        json_name="mom8_draft.json",
        sql_name="mom8_insert.sql",
    )
