# -*- coding: utf-8 -*-
"""Builds the MOM.6 master policy draft: JSON for review + SQL for later insert.

UNAPPROVED DRAFT. Do not insert, approve, or write this to Supabase.

THIS IS DRAFTED UNDER THE TWO-TIER DEPTH STANDING RULE (2026-08-10) AND THE
DISCLAIMER STATUTE-MATCHING STANDING RULE (2026-08-17), both in
scripts/master-policy-todos.md.

Tier is decided by doc_required / the asterisk in the official PDF:
  Tier 1 (full treatment): MOM.6.a, MOM.6.f, MOM.6.h, MOM.6.i
  Tier 2 (lighter pass):   MOM.6.b, MOM.6.c, MOM.6.d, MOM.6.e, MOM.6.g

FOUR of nine OEs are asterisked. The draft builds deep blocks for a, f, h and i.
b, c, d, e and g are lean.

Official source: NABH Standards for Small Healthcare Organisations, 3rd Edition
(August 2022), Chapter 3, standard MOM.6 and OEs MOM.6.a-i, read from the
official standards PDF (downloaded 2026-08-17 from the NABH website's Explore
NABH Standards page), printed page 79, PDF page index 85.

Header: "Medications are administered safely."
MOM.6.a raw text attaches the asterisk to "manner": "Administration of
medication is done in a safe manner*."

Asterisks verified 2026-08-17: scripts/asterisk_extract.py re-run against that
download (self-validation passed, 408 OEs, 132 asterisks, output matched the
committed scripts/shco_oe_asterisks.json on all 408 entries) and the MOM.6
page read directly. MOM.6.a, MOM.6.f, MOM.6.h and MOM.6.i carry the asterisk;
MOM.6.b, c, d, e and g are unasterisked.
"""
from policy_build_common import emit_and_verify, make_disclaimer

STANDARD_CODE = "MOM.6"
CHAPTER = "MOM"
OE_CODES = [
    "MOM.6.a", "MOM.6.b", "MOM.6.c", "MOM.6.d", "MOM.6.e",
    "MOM.6.f", "MOM.6.g", "MOM.6.h", "MOM.6.i",
]
TIER1_OES = ["MOM.6.a", "MOM.6.f", "MOM.6.h", "MOM.6.i"]

POLICY_TITLE = "Safe Administration of Medications"

VERSION = "1.0"
REVISION_HISTORY = [
    {"version": "1.0", "date": "17-08-2026", "description": "Initial release."},
]

PURPOSE = """This document sets out how {{HOSPITAL_NAME}} administers medications safely: administration is done in a safe manner by persons entitled to administer; a prepared medication is labelled before a second drug is prepared; the patient is identified before administration; the medicine is verified from the medication order and physically inspected before it is given; strength, route and timing are verified from the order; measures to avoid catheter and tubing mis-connections are implemented; administration is documented; patient's self-administration, if the hospital allows it at all, is governed in writing; and medications brought from outside the organisation, if they are used at all, are governed in writing.

The chapter intent is that the organisation has a safe and organised medication process, and that administration is governed by written guidance. A medicine given to the patient in the next bed, a line connected because the fittings matched, a second syringe prepared before the first was labelled, or a family's bottle from home poured into the drug trolley, is not that process. This document is the administration process that makes the intent operational at the bedside, in the theatre, in the emergency area, and in every other location where a medicine is given.

This document is not the prescribing policy, is not the dispensing policy, and is not the post-administration monitoring policy. Those are owned by MOM.3, MOM.5 and MOM.7. It does not hang blood (COP.5) and it does not implant devices (MOM.9), even though the chapter intent says medications include blood, implants and devices. It does not rewrite injection technique (HIC.2) or device-infection bundles (HIC.4)."""

SCOPE = """This policy applies to every location at {{HOSPITAL_NAME}} in which a medication is administered: in-patient wards, the emergency area, day-care, out-patient treatment rooms, the operation theatre and recovery, intensive or high-dependency areas where they exist, labour and procedure rooms, and any other clinical location in which a medicine is given. It binds every person who prepares or administers a medication, every person who traces a line before connecting it, and the staff who govern self-administration and medications brought from outside, including by forbidding those practices if that is the hospital's decision.

It covers: administration of medication in a safe manner; labelling of a prepared medication before preparation of a second drug; identification of the patient before administration; verification from the medication order and physical inspection before administration; verification of strength, route and timing from the order before administration; measures to avoid catheter and tubing mis-connections during medication administration; documentation of administration; measures to govern patient's self-administration of medications; and measures to govern patient's medications brought from outside the organisation.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- The two identifiers used at the point of care are governed by the uniform-care policy of {{HOSPITAL_NAME}} (COP.1). This policy (MOM.6.c) owns identifying the patient before administration USING those two identifiers. COP.1 owns the pair; this document owns the administration-time check. A bed number is not an identifier under COP.1 and is not used here.
- Safe injection and intravenous-access technique — one needle, one syringe, one patient, one time; aseptic preparation; sharps safety — is governed by the infection-prevention-and-control-practices policy of {{HOSPITAL_NAME}} (HIC.2). This policy requires those practices at administration; it does not rewrite them.
- Ventilator, central-line, urinary-catheter and surgical-site bundles are governed by the healthcare-associated-infection policy of {{HOSPITAL_NAME}} (HIC.4). Tubing misconnection under MOM.6.f is a medication-administration connection error (WHO Patient Safety Solution 7, chapter reference 2), not an infection-prevention bundle. This document does not rewrite HIC.4.
- Giving a sedative for a procedure, giving an anaesthetic, or giving a medicine during surgery is owned as a clinical method by the procedural-sedation, anaesthesia and procedures-and-operation-theatre policies of {{HOSPITAL_NAME}} (COP.9, COP.10, COP.11). The medication-administration checks in this document (identity, verify the order, inspect, document) still apply. This document does not rewrite sedation depth, the anaesthetic plan, or surgical method.
- Pain assessment and the titration loop (need and response) are governed by the pain, rehabilitation and nutrition policy of {{HOSPITAL_NAME}} (COP.13). Administration of the prescribed analgesic, and documentation of that administration, remain this document. A pain score is not a prescription; a prescription is not a pain assessment.
- Discharge-summary medication instructions, including medicines to take after leaving, are governed by the discharge policy of {{HOSPITAL_NAME}} (AAC.8). Self-administration while the patient is in this hospital is MOM.6.h. Medications brought from outside the organisation are MOM.6.i. The three are different acts.
- Labelling of a dispensed pack at the pharmacy is governed by the safe-dispensing policy of {{HOSPITAL_NAME}} (MOM.5.d). Labelling of a medication prepared for administration, before a second drug is prepared, is this document (MOM.6.b). They are different acts.
- The written medication order is governed by the uniform-medication-orders policy of {{HOSPITAL_NAME}} (MOM.4). This policy reads that order; it does not write it. An incomplete or illegible order is not administered.
- Who may prescribe, including verbal orders, is MOM.3. Who may dispense is MOM.5. Who may administer is this document, under the National Medical Commission Act, 2019 and the Indian Nursing Council Act, 1947 as they apply to the role.
- Monitoring after administration, and capture of near-miss, error and adverse drug reaction, are governed by the post-administration monitoring policy of {{HOSPITAL_NAME}} (MOM.7). This document owns that the dose was given and documented; MOM.7 owns what is watched afterwards.
- Narcotic, chemotherapy and radioactive administration by qualified personnel, and the register, remain under the high-risk-classes policy of {{HOSPITAL_NAME}} (MOM.8). The identity, order-verification and documentation checks of this document still apply.
- Blood and blood components are administered under the transfusion policy of {{HOSPITAL_NAME}} (COP.5). This document does not hang a unit. Implantable prosthesis and medical devices are used under the implant policy (MOM.9). This document does not implant a device.
- Self-administration and patient's-own medicines: the hospital may forbid either or both. If allowed, written measures govern them. This document does not invent a right to self-medicate.
- Used sharps and administration waste enter the hospital-wide waste programme governed by the support-services infection-control policy of {{HOSPITAL_NAME}} (HIC.3). Colour categories are not restated. Waste rules are not named in this document's statutory paragraph."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} administers medication in a safe manner. A person who is not entitled to administer does not give a medicine. An order that is not valid is not given. Injection technique follows the infection-prevention policy; this document does not rewrite it.

{{HOSPITAL_NAME}} labels a prepared medication before preparing a second drug.

{{HOSPITAL_NAME}} identifies the patient, using the two identifiers of the uniform-care policy, before administration.

{{HOSPITAL_NAME}} verifies the medication from the medication order and physically inspects it before administration, and verifies strength, route and timing from the order before administration.

{{HOSPITAL_NAME}} implements measures to avoid catheter and tubing mis-connections during medication administration. A fitting that matches is not, by itself, the right line.

{{HOSPITAL_NAME}} documents medication administration.

{{HOSPITAL_NAME}} implements written measures that either govern patient's self-administration of medications or forbid it. There is no implied right to self-medicate.

{{HOSPITAL_NAME}} implements written measures that either govern patient's medications brought from outside the organisation or forbid their use. There is no implied right to use a home bottle on the ward.

{{HOSPITAL_NAME}} does not hang blood under this document and does not implant a device under this document."""

PROCEDURE_STEPS = [
"""1. Administration of medication is done in a safe manner

Administration of medication at {{HOSPITAL_NAME}} is done in a safe manner. This step is the documented-evidence anchor of a requirement the standard asterisks (the asterisk in the official PDF is attached to "manner"). An assessor will ask how yesterday's doses were given, not whether a poster of "rights" exists. Safe manner means a competent person, a valid order, the patient in front of the giver, the medicine in the giver's hand matched to that order, the line — if a line is used — traced before it is connected, and a record that the dose was given. It is the whole act. The later steps of this document are parts of that act; they are not a substitute for it.

The reason a "safe manner" is written as more than a slogan is that administration is the last act before the medicine is inside the patient. Prescribing can be excellent and dispensing labelled, and the patient in the next bed still receives the injection if the giver does not identify, does not read the order, or connects the syringe to the tubing that was nearest. The National Coordinating Council for Medication Error Reporting and Prevention recommendations to enhance accuracy of administration (chapter reference 20) describe that last act in process terms: clarify an incomplete or illegible order before preparing; read the label when reaching for, preparing, giving and putting away; design the process so that the correct medicine, dose, person, route, form, time and reason can be achieved without a workaround; train the people who give; give them the patient information and the product information at the point of use; consider the work environment. This document uses those recommendations as a recognised framework. It does not import a named eMAR or bar-code product, a smart-pump brand, a free-flow-protection model number, or a list of "rights" as a NABH checklist that can be ticked instead of performing the later steps. The later steps remain mandatory whether or not the hospital uses technology.

Who may administer a medication is [Hospital to define — who may administer medications, by role, route and setting]. The statutory gate for a medical practitioner is current registration under the National Medical Commission Act, 2019 and the State Medical Council. The statutory gate for a nurse is current registration under the Indian Nursing Council Act, 1947 and the State Nursing Council. Human-resource procedures verify registration; this step uses that verification. A person whose registration has lapsed, or who is not in a role this hospital has authorised for that route, does not administer. Students administer only under the supervision this hospital has written. Drugs and Cosmetics law, insofar as it governs administration of scheduled medicines, is the backdrop: an unlabelled or unauthorised administration is not a lawful supply into the patient. This step does not print a section number.

Safe injection and infusion technique is applied from the infection-prevention-and-control-practices policy of {{HOSPITAL_NAME}}. This step requires that a person who injects follows that policy. It does not reprint one needle, one syringe, one patient, one time.

A medicine is administered only against a valid medication order under the uniform-medication-orders policy. An incomplete, illegible, unsigned or unauthorised order is clarified before preparation and is not guessed. Verbal orders are taken under the prescribing policy; once written they are MOM.4 orders and are read here as orders.

This step does not hang blood. Transfusion is the transfusion policy of {{HOSPITAL_NAME}}. This step does not implant a device. Implants are the implant policy. The chapter intent's inclusion of blood, implants and devices in "medications" does not move those acts into this procedure.

Where a sedative, an anaesthetic, or a medicine given during a procedure is administered, the clinical method remains under the procedural-sedation, anaesthesia or procedures policies. The identity check, the order verification, the inspection, the line-trace where a line is used, and the documentation in this document still apply. Stretching those clinical policies to skip these checks, or stretching this document to write an anaesthetic technique, is the boundary this paragraph exists to keep.

The written administration method, including who may administer by route and setting, is held at [Hospital to define — where the written medication-administration method is held].""",

"""2. Prepared medication is labelled before preparation of a second drug

Prepared medication is labelled before preparation of a second drug.

When a medicine is drawn, mixed or otherwise prepared for administration, the container that will be taken to the patient is labelled before a second medicine is started. Two unlabelled syringes on the same tray are a defect even if the person "knows" which is which.

What the prepared-medication label carries is [Hospital to define — the content of the prepared-medication label]. This labelling is not a substitute for the dispensed-pack label owned by the safe-dispensing policy. A pharmacy pack already labelled under MOM.5.d does not remove the duty, when that pack is further prepared (drawn, diluted, transferred), to label the prepared container before a second drug is prepared.""",

"""3. The patient is identified before administration

The patient is identified before administration.

Identification uses the two identifiers of the uniform-care policy of {{HOSPITAL_NAME}}. COP.1 owns the pair. This step owns the administration-time check: both identifiers are confirmed against the patient (or the patient's identifier band or equivalent) and against the order, immediately before the medicine is given. A bed number, a room number or a trolley position is not an identifier and is not used.

How the confirmation is recorded, if it is recorded separately from the administration entry at step 7, follows the uniform-care policy's recording method. This step requires that the check happened before the dose.""",

"""4. Verified from the medication order and physically inspected before administration

Medication is verified from the medication order and physically inspected before administration.

The person who will administer reads the order in the uniform location and matches the medicine in hand to that order: name and form. The pack, vial, ampoule or prepared container is physically inspected: the label is read; the integrity of the container is looked at; an expired, damaged, discoloured, recalled or unlabelled product is not given.

A mismatch is not resolved by assuming the trolley is right. The order is re-read or clarified under the uniform-medication-orders policy.""",

"""5. Strength, route and timing verified from the order before administration

Strength, route and timing is verified from the order before administration.

The person who will administer reads the strength, the route and the time or frequency from the order, and confirms that the product in hand and the intended act match those three elements. A medicine that is the right name at the wrong strength, given by the wrong route, or given at the wrong time, has not been verified.

What this hospital treats as the acceptable timing window for a scheduled dose, including any distinction it chooses to make between time-critical and other scheduled medicines, is [Hospital to define — the acceptable timing window for a scheduled dose]. The Institute for Safe Medication Practices Acute Care Guidelines for Timely Administration of Scheduled Medications (chapter reference 10) may inform that window. This document does not import that guideline's minutes as a NABH mandate.""",

"""6. Measures to avoid catheter and tubing mis-connections during medication administration

Measures to avoid catheter and tubing mis-connections during medication administration are implemented. This step is the documented-evidence anchor of a Core requirement the standard asterisks. A mis-connection is a medication-administration connection error: a tube or catheter joined to the wrong port because the fittings matched. It is not a ventilator bundle, not a central-line bundle, and not a urinary-catheter bundle. Those bundles remain under the healthcare-associated-infection policy of {{HOSPITAL_NAME}}. This step does not rewrite them.

The reason this is a documented measure, not a reminder to "be careful", is that many unrelated clinical systems have historically used compatible connectors. Enteral feed connected to an intravenous line, a blood-pressure cuff insufflator connected to an intravenous cannula, oxygen tubing connected to a needleless port, or an epidural line connected to an intravenous giving set, are the events this objective element exists to stop. The World Health Organization Patient Safety Solution 7, Avoiding Catheter and Tubing Mis-Connections (chapter reference 2), is the chapter's cited framework: trace all lines from the patient back to the point of origin before connecting or reconnecting; do not force a fit; label high-risk catheters and tubes; route tubes so that an enteral or other non-intravenous line cannot be mistaken for an intravenous line; and report a mis-connection as an incident, not as a near-miss that is reset and forgotten. This document uses that Solution as a recognised framework. It does not import a named ISO connector series, a colour-code table, or a device-purchase mandate as a NABH requirement. The hospital writes the measures it actually uses.

The measures {{HOSPITAL_NAME}} implements are [Hospital to define — the measures used to avoid catheter and tubing mis-connections during medication administration, including how lines are traced before connecting, how high-risk lines are labelled, and how a suspected mis-connection is stopped and reported]. At a minimum this document requires that, before a medication is connected to a tube or catheter, the person connecting traces that line from the patient to the origin and confirms it is the intended line for that medicine and that route. A fitting that matches is not confirmation. The common error is a reconnection after a transfer, a wash, or a procedure, done by joining the two ends that are the same shape. That reconnection without a trace is how a correct medicine enters the wrong lumen. It is forbidden here.

This step applies during medication administration. It does not own insertion technique for a urinary catheter, a central line, or an endotracheal tube, and it does not own the daily necessity review of those devices. HIC.4 owns those. A medicine given through a line that HIC.4 also addresses is still traced here before the connection.

The written mis-connection measures are held with the administration method at step 1.""",

"""7. Medication administration is documented

Medication administration is documented.

The administration entry is made against the unique identification number and records at least that the named medicine was given, the dose or strength given, the route, the date and time, and the person who administered. How that entry is made — medication chart, electronic record, or other form — is [Hospital to define — how medication administration is documented]. A dose that was not given is recorded as not given, with the reason, so that a blank is not read as given.

Documentation of administration is not the post-administration monitoring record, which is owned by the post-administration monitoring policy of {{HOSPITAL_NAME}}. It is not the pain-titration note, which is owned by the pain policy; that policy still requires this administration entry when an analgesic is given.""",

"""8. Measures to govern patient's self-administration of medications

Measures to govern patient's self-administration of medications are implemented. This step is the documented-evidence anchor of that asterisked requirement. Govern means the hospital has a written position and applies it. The position may be that self-administration is not allowed. The standard does not create a right to self-medicate.

The reason this must be written is that a patient who takes a tablet from a locker, a family member who gives an injection brought from home, or a ward that "lets them take their own thyroid tablet because they always do", is administration that has left the process at steps 1 to 7: no identity check by staff, no verification from the order, no inspection, no documentation by the person accountable for the dose. The common error is an informal permission that exists for "stable" patients and is invisible in the record. That informal permission is how a double dose happens — the ward stock dose and the patient's own — or how a medicine the order stopped is still taken. Either the hospital forbids self-administration, or it writes who may self-administer, which medicines, under whose observation, how the dose is still documented, and how the medicine is still reconciled with the current order.

Whether {{HOSPITAL_NAME}} allows patient's self-administration of medications while the patient is in this organisation, and if so the written measures (which patients, which medicines, whose observation, how the dose is documented, how the current order is still the order that is taken), or the written statement that self-administration is not allowed, is [Hospital to define — whether patient's self-administration of medications is allowed and, if it is, the governing measures; or the written statement that it is not allowed]. If the hospital forbids it, staff do not make local exceptions. If the hospital allows it, a patient who is not inside the written measures does not self-administer.

Self-administration in hospital is not the discharge-summary instruction on medicines to take after leaving, which is owned by the discharge policy of {{HOSPITAL_NAME}}. A patient who is being discharged is not, by that fact, self-administering under this step.

Narcotic drugs and psychotropic substances are not self-administered. Their use remains under the high-risk-classes policy.

The written self-administration position is held with the administration method at step 1.""",

"""9. Measures to govern patient's medications brought from outside the organisation

Measures to govern patient's medications brought from outside the organisation are implemented. This step is the documented-evidence anchor of an Achievement requirement the standard asterisks. Achievement does not reduce the depth: the asterisk allocates Tier 1. Govern means the hospital has a written position and applies it. The position may be that medicines brought from outside are not used. The standard does not create a right to use a home bottle on the ward.

The reason a home medicine is not automatically hospital stock is that the identity, integrity, storage history and current indication of a pack that arrived in a bag are not known to this organisation in the way a dispensed pack under the safe-dispensing policy is known. A strip from home may be the wrong strength, another family member's medicine, expired, recalled, or a medicine the current order has stopped. Putting it in the drug trolley, or letting the patient continue it alongside ward stock, is how an unknown product enters administration. The common error is courtesy: "they have been taking it for years" followed by a locker full of bottles that no one has listed against the current order. That courtesy is an ungoverned medication process. It is forbidden unless the written measures, on defined conditions, allow a defined use, and those conditions are met and recorded.

Whether {{HOSPITAL_NAME}} allows use of patient's medications brought from outside the organisation, and if so the written measures (how they are declared, identified, checked against the current order, stored so they cannot be mixed with hospital stock, administered or self-administered only under this document's other steps, and returned or removed at discharge), or the written statement that such medicines are not used, is [Hospital to define — whether patient's medications brought from outside the organisation may be used and, if they may, the governing measures; or the written statement that they are not used]. If they are not used, they are not placed in the drug trolley and are not left in a locker as an informal supply. They are returned to the family or held for return, labelled as the patient's property, and are not converted into pharmacy stock. Return to pharmacy stock is forbidden under the safe-dispensing policy's return rule.

This step is not the discharge-summary list of medicines to continue after leaving (AAC.8). It is not self-administration of hospital-dispensed medicines (step 8). It is not MOM.3's reconciliation of medications at transition points, which owns the clinical list at transfer; this step owns the physical packs that arrived with the patient.

The written position on medicines brought from outside is held with the administration method at step 1.""",

"""10. Records, review and the order of operations

Every administration this document requires to be retrievable is recorded against the unique identification number: the person who administered, the identity check, the verification from the order, the inspection, the strength, route and time, the line-trace where a line was used, the administration entry, and any self-administration or outside-medicine episode under the written measures — or the recorded position that those practices are forbidden.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for medication-administration records] for: administration only by a person entitled to administer, against a valid order; prepared medications labelled before a second drug; two identifiers used before the dose rather than a bed number; verification and physical inspection before administration; strength, route and timing read from the order; line-trace before a medication connection; administration documented rather than left blank; and self-administration and outside medicines either forbidden in writing or governed by the written measures rather than by a locker habit.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a wrong-patient administration, a mis-connected line, an unlabelled prepared syringe, an undocumented dose, or an ungoverned home bottle exposes a gap, or when the uniform-care, infection-prevention, device-bundle, dispensing, order, discharge, transfusion, sedation, anaesthesia, theatre, pain or high-risk-classes policies that this document hands work to are revised.""",
]

RESPONSIBILITY = """The head of the institution is accountable for {{HOSPITAL_NAME}} administering medications only in a safe manner, for mis-connection measures that are used rather than posted, and for a written position on self-administration and on medicines brought from outside.

The named medication-administration lead authors and keeps current the administration method, the prepared-medication label, the timing window, the mis-connection measures, and the written positions on self-administration and on medicines brought from outside. The named lead is [Hospital to define — the named medication-administration lead].

Persons who administer identify the patient with two identifiers, verify and inspect against the order, verify strength, route and timing, label a prepared medicine before preparing a second, trace a line before connecting a medicine, document the dose, and do not make local exceptions to the self-administration or outside-medicine position.

The quality or accreditation coordinator audits the records at step 10 and reports findings to the head of the institution.

All staff are expected to treat a dose given without identity check, a mis-connected line, two unlabelled syringes, an undocumented administration, and an ungoverned home bottle, as defects, and to report them."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 3 Management of Medication, standard MOM.6.
- National Medical Commission Act, 2019 and State Medical Council registration — insofar as they govern who may administer a medication as a medical practitioner.
- Indian Nursing Council Act, 1947 and State Nursing Council registration — insofar as they govern who may administer a medication as a nurse.
- Drugs and Cosmetics Act, 1940 and the rules under it — insofar as they govern administration of scheduled medicines. No section number is imported as a mandate.
- World Health Organization, Avoiding Catheter and Tubing Mis-Connections, Patient Safety Solution 7 (2007) — chapter reference 2; the framework for tracing lines from the patient to the origin before connecting, labelling high-risk tubes, and treating a matching fitting as insufficient. This document does not import a named connector standard as a NABH mandate.
- National Coordinating Council for Medication Error Reporting and Prevention, Recommendations to Enhance Accuracy of Administration of Medications (chapter reference 20) — a recognised framework for clarifying incomplete orders, reading labels, designing the process so the correct medicine reaches the correct person without a workaround, and training the people who give; this document does not import a named eMAR, bar-code or pump product as a NABH mandate.
- Institute for Safe Medication Practices, Acute Care Guidelines for Timely Administration of Scheduled Medications (chapter reference 10) — may inform the hospital's timing window; this document does not import that guideline's minutes as a NABH mandate.
- Internal documents of {{HOSPITAL_NAME}}: the medication-administration method; the prepared-medication label; the timing window; the mis-connection measures; the self-administration position; the position on medicines brought from outside; the uniform-care policy; the infection-prevention policy; the device-bundle policy; the dispensing policy; the uniform-order and prescribing policies; the discharge policy; the transfusion policy; the implant policy; the sedation, anaesthesia and theatre policies; the pain policy; the high-risk-classes medication policy; the post-administration monitoring policy; and the human resource policies."""

DISTRIBUTION = """Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every in-patient ward; the emergency area; day-care; out-patient treatment rooms; the operation theatre and recovery; intensive or high-dependency areas where they exist; labour and procedure rooms; pharmacy (for the boundary with dispensed-pack labelling); nursing administration; and the named medication-administration lead.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The administration method, the prepared-medication label, the mis-connection measures, and the written positions on self-administration and on medicines brought from outside — the working documents this policy requires — are held in every location that administers medicines.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP, PPE, VAP, CLABSI and CAUTI.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

NMC — National Medical Commission
INC — Indian Nursing Council
NCCMERP — National Coordinating Council for Medication Error Reporting and Prevention
ISMP — Institute for Safe Medication Practices
UID — Unique Identification Number

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

STATUTE_CLAUSE = (
    "the National Medical Commission Act, 2019 and the Indian Nursing Council "
    "Act, 1947, insofar as they govern who may administer a medication, and "
    "the Drugs and Cosmetics Act, 1940 and the rules under it insofar as they "
    "govern administration of scheduled medicines"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.6.a",
        "requirement": "Administration of medication is done in a safe manner.",
        "steps": "Steps 1, 10",
        "evidence": "The written medication-administration method used in every location that gives a medicine, covering who may administer by role, route and setting, that a valid order is required, that the later identity, verification, inspection, line-trace and documentation steps are parts of the same act rather than a poster of rights that can be ticked instead, and the rule that blood is not hung here and a device is not implanted here even though the chapter intent includes blood, implants and devices among medications; the named roles who may administer, with current registration under the National Medical Commission Act, 2019 and State Medical Council for a medical practitioner and under the Indian Nursing Council Act, 1947 and State Nursing Council for a nurse, used from human-resource verification rather than restated as a credentialing method, and showing that a person whose registration has lapsed or who is not authorised for that route does not administer; the recorded application of the infection-prevention policy's injection technique rather than a reprint of one needle, one syringe, one patient, one time; the recorded rule that an incomplete, illegible, unsigned or unauthorised order is clarified under the uniform-medication-orders policy before preparation and is not guessed; the recorded use of NCCMERP administration recommendations (chapter reference 20) as a framework without a named eMAR, bar-code or pump product presented as a NABH mandate; the recorded boundary that sedation, anaesthesia and intra-operative medicines keep their clinical method under those policies while the identity, order-verification, inspection, line-trace and documentation checks of this document still apply; sample administration episodes against the unique identification number showing a person entitled to administer, a valid order, and the later steps performed as one act; the location where the written method is held; induction or briefing records showing staff who administer have been shown that method; the audit sample at step 10 of administration only by a person entitled to administer, against a valid order",
        "responsible": "Named medication-administration lead holds the written method and authorised-administrator rules; persons who administer apply that method; human resource function verifies registration; infection-prevention policy owns injection technique; head of the institution is accountable that unnamed persons do not administer; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.6.b",
        "requirement": "Prepared medication is labelled before preparation of a second drug.",
        "steps": "Steps 2, 10",
        "evidence": "The written content of the prepared-medication label; sample preparation showing the first container labelled before a second drug was started, rather than two unlabelled syringes on one tray; the recorded distinction from dispensed-pack labelling under the safe-dispensing policy, including that further preparation of a pharmacy pack still requires this label",
        "responsible": "Persons who prepare medications label before starting a second drug; dispensing policy owns pack labels; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.6.c",
        "requirement": "The patient is identified before administration.",
        "steps": "Steps 3, 10",
        "evidence": "Sample administration records showing the two identifiers of the uniform-care policy confirmed against the patient and the order immediately before the dose, rather than a bed number; the recorded division that the uniform-care policy owns the pair and this step owns the administration-time check",
        "responsible": "Persons who administer confirm two identifiers before the dose; uniform-care policy owns the identifier pair; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.6.d",
        "requirement": "Medication is verified from the medication order and physically inspected before administration.",
        "steps": "Steps 4, 10",
        "evidence": "Sample records showing the medicine in hand matched to the order for name and form, and physically inspected (label, integrity, not expired, damaged, discoloured, recalled or unlabelled) before administration; records of a mismatch not resolved by assuming the trolley was right",
        "responsible": "Persons who administer verify from the order and inspect before giving; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.6.e",
        "requirement": "Strength, route and timing is verified from the order before administration.",
        "steps": "Steps 5, 10",
        "evidence": "The written acceptable timing window for a scheduled dose, with ISMP timely-administration guidance used as a framework if at all and not as imported minutes; sample records showing strength, route and timing read from the order before the dose",
        "responsible": "Persons who administer verify strength, route and timing from the order; named lead holds the timing window; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.6.f",
        "requirement": "Measures to avoid catheter and tubing mis-connections during medication administration are implemented.",
        "steps": "Steps 6, 10",
        "evidence": "The written measures used to avoid catheter and tubing mis-connections during medication administration, including how lines are traced from the patient to the origin before connecting or reconnecting, how high-risk lines are labelled, and how a suspected mis-connection is stopped and reported, showing a process rather than a poster to be careful, and rather than a reconnection after a transfer or a wash done by joining the two ends that are the same shape; the recorded minimum that a fitting that matches is not confirmation of the intended line; the recorded use of WHO Patient Safety Solution 7 (chapter reference 2) as a framework without a named ISO connector series, colour-code table or device-purchase mandate presented as a NABH requirement; the recorded division that this step is a medication-administration connection error and is not a rewrite of the healthcare-associated-infection policy's ventilator, central-line, urinary-catheter or surgical-site bundles, while a medicine given through a line those bundles also address is still traced here before the connection; sample administration episodes involving a tube or catheter showing the trace before the medicine was connected; incident records of a suspected mis-connection treated as an incident rather than reset and forgotten; induction or briefing records showing staff who connect medications to lines have been shown the measures; the audit sample at step 10 of line-trace before a medication connection",
        "responsible": "Named medication-administration lead holds the mis-connection measures; persons who connect a medicine to a tube or catheter trace the line first; healthcare-associated-infection policy owns device bundles and is not rewritten here; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.6.g",
        "requirement": "Medication administration is documented.",
        "steps": "Steps 7, 10",
        "evidence": "The written method of the administration entry (chart, electronic record, or other form) recording the named medicine, dose or strength, route, date and time, and the person who administered, against the unique identification number; sample entries showing a dose not given recorded as not given rather than left blank; the recorded distinction from post-administration monitoring and from the pain-titration note",
        "responsible": "Persons who administer document the dose; post-administration monitoring policy owns what is watched afterwards; pain policy owns titration; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.6.h",
        "requirement": "Measures to govern patient's self-administration of medications are implemented.",
        "steps": "Steps 8, 10",
        "evidence": "The written position on patient's self-administration of medications while the patient is in this organisation: either the written statement that self-administration is not allowed, with records showing staff did not make local exceptions, or the written measures naming which patients, which medicines, whose observation, how the dose is documented, and how the current order remains the order that is taken, with sample episodes showing a patient outside those measures did not self-administer; the recorded statement that the standard does not create a right to self-medicate and that an informal permission for 'stable' patients is not governance; the recorded distinction that discharge-summary instructions on medicines to take after leaving are owned by the discharge policy and are not this step; the recorded rule that narcotic drugs and psychotropic substances are not self-administered and remain under the high-risk-classes policy; the written position held with the administration method; induction or briefing records showing ward staff apply the position rather than a locker habit; the audit sample at step 10 of self-administration either forbidden in writing or governed by the written measures",
        "responsible": "Named medication-administration lead holds the self-administration position; persons who administer apply it and do not invent local exceptions; discharge policy owns post-discharge medicine instructions; high-risk-classes policy owns narcotics; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.6.i",
        "requirement": "Measures to govern patient's medications brought from outside the organisation are implemented.",
        "steps": "Steps 9, 10",
        "evidence": "The written position on patient's medications brought from outside the organisation: either the written statement that such medicines are not used, with records showing they were not placed in the drug trolley and were returned or held as the patient's property rather than converted into pharmacy stock, or the written measures for declaration, identification, checking against the current order, storage so they cannot be mixed with hospital stock, administration only under this document's other steps, and return or removal at discharge, with sample episodes showing those conditions were met and recorded; the recorded statement that the standard does not create a right to use a home bottle on the ward and that courtesy ('they have been taking it for years') is not governance; the recorded distinction from the discharge-summary list (AAC.8), from self-administration of hospital-dispensed medicines (step 8), and from reconciliation of medications at transition points under the prescribing policy, which owns the clinical list at transfer while this step owns the physical packs that arrived with the patient; the recorded rule that a home pack is not restocked under the safe-dispensing return rule; the written position held with the administration method; induction or briefing records showing ward staff apply the position rather than a locker of undeclared bottles; the audit sample at step 10 of outside medicines either forbidden in writing or governed by the written measures",
        "responsible": "Named medication-administration lead holds the outside-medicine position; persons who administer apply it; dispensing policy forbids converting a home pack into pharmacy stock; discharge policy owns post-discharge lists; prescribing policy owns reconciliation at transitions; quality or accreditation coordinator audits",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. MOM.6 standard text and all nine OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 3 Management of Medication, printed page 79 (PDF page index 85). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page and opened for this draft (md5 39e3bc86d73d651b9cfef283bbf018a9). OE-page header quote: "Medications are administered safely." Levels: MOM.6.a Commitment, MOM.6.b Commitment, MOM.6.c Commitment, MOM.6.d Core, MOM.6.e Commitment, MOM.6.f Core, MOM.6.g Commitment, MOM.6.h Commitment, MOM.6.i Achievement.
   FOUR OEs CARRY THE ASTERISK -- MOM.6.a (asterisk attached to "manner" in the raw line "Administration of medication is done in a safe manner*"), MOM.6.f, MOM.6.h and MOM.6.i. The draft builds four deep blocks (step 1 for a; step 6 for f; step 8 for h; step 9 for i). MOM.6.b, c, d, e and g are unasterisked and are correspondingly Tier 2. MOM.6.i is Achievement AND asterisked, so it is Tier 1. Achievement is not what allocates depth; the asterisk is.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; 408 OEs, 132 asterisks; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the MOM.6 page read directly from the extracted page text, and the committed asterisk file. MOM.6 was not among the 14 mismatches of the 2026-08-10 audit.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. FOUR OF NINE OEs ARE TIER 1. Tier 1: MOM.6.a, f, h, i -- steps 1, 6, 8 and 9 carry the reasoning (why a safe manner is the whole act; why a matching fitting is not the right line; why the standard does not create a right to self-medicate; why a home bottle is not hospital stock). Tier 2: MOM.6.b, c, d, e, g -- requirement and method without extended rationale. Reviewer to note the shallower treatment of b, c, d, e and g is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of MOM.6.a/f/h/i against the approved HIC.1-HIC.6 masters and the AAC.1-AAC.8 and COP.1-COP.13 drafts. Search terms: administer, self-admin, brought from outside, tubing, mis-connection, misconnection, catheter connection, medication administration.
   COP.1 -- two identifiers. MOM.6.c (T2) uses them at administration time. COP.1 owns the pair. Stated in Scope.
   HIC.2 -- safe injection / IV access technique. Applied, not rewritten. Stated in Scope and step 1.
   HIC.4 -- VAP/CLABSI/CAUTI bundles. MOM.6.f is a medication-admin connection error (WHO Patient Safety Solution 7), NOT the IPC bundle. Do not rewrite HIC.4. Stated in Scope and step 6.
   COP.9/10/11 -- giving a sedative/anaesthetic/during surgery is those clinical policies; identity, verify order, document still apply; do not rewrite anaesthesia method. Stated in Scope and step 1.
   COP.13 -- pain titration loop vs administration documentation. Stated in Scope and step 7.
   AAC.8 -- discharge-summary medication instructions vs MOM.6.h self-admin in hospital vs MOM.6.i meds brought from outside. Stated in Scope and steps 8-9.
   MOM.5.d -- dispensed-pack labelling vs MOM.6.b prepared-med labelling. Different acts. Stated in Scope and step 2.
   COP.5 -- this document does not hang blood. MOM.9 -- this document does not implant devices. Chapter intent includes blood, implants and devices among medications; those acts stay with their owners. Stated in Purpose, Scope and step 1.
   Self-admin and patient's-own-meds: hospital may forbid; if allowed, written measures. No invented right to self-medicate. Stated in Scope and steps 8-9.
3. FORWARD REFERENCES: MOM.3/4 order; MOM.5 dispensed-pack label and returns; MOM.7 post-admin monitoring; MOM.8 high-risk classes; MOM.9 implants; COP.1 identifiers; COP.5 transfusion; COP.9/10/11 sedation/anaesthesia/theatre; COP.13 pain; AAC.8 discharge summary; HIC.2 injection; HIC.3 waste; HIC.4 device bundles; HRM registration. Each is a deliberate boundary.
4. T2 QUICK CHECK: MOM.6.b vs MOM.5.d labelling -- flagged. MOM.6.c vs COP.1 identifiers -- flagged. MOM.6.d/e vs MOM.4 order content -- flagged. MOM.6.g vs MOM.7 monitoring and COP.13 titration -- flagged. Nothing added to the HIC reconciliation list.

STATUTORY AND EXTERNAL FACTS
5. National Medical Commission Act, 2019 and Indian Nursing Council Act, 1947 -- cited insofar as they govern who may administer. No section numbers. Human-resource procedures verify registration.
6. Drugs and Cosmetics Act, 1940 and the rules under it -- cited insofar as administration of scheduled medicines. No section number. No wholesale storage method. BMW Rules are NOT named in P2.
7. WHO Patient Safety Solution 7, Avoiding Catheter and Tubing Mis-Connections (chapter ref 2, 2007) -- verified as the chapter's cited framework: trace lines from patient to origin before connecting; matching fittings are a known hazard (enteral to IV, BP cuff to IV, oxygen to needleless port, epidural to IV). Used as a framework. NOT used as an ISO 80369 mandate or a colour-code table.
8. NCCMERP Recommendations to Enhance Accuracy of Administration of Medications (chapter ref 20) -- used as a framework. NOT used as a named technology mandate. (Council page revised 2023; chapter cites the 2015 retrieval. The principles used here — clarify incomplete orders, read labels, design out workarounds — are stable across those dates.)
9. ISMP Acute Care Guidelines for Timely Administration of Scheduled Medications (chapter ref 10) -- may inform the hospital's timing window. Minutes are NOT imported as a mandate.
10. NO NUMBERS ARE STATED as requirements -- no administration-window minutes, no connector standard years, no double-check staffing. Every such value is [Hospital to define]. Consistent with the no-numbers default.
11. Bio-Medical Waste Management Rules, 2016, Food Safety and Standards Act, 2006, and Clinical Establishments Act, 2010 are NOT named in P2.

EDITORIAL POSITIONS TAKEN
12. Step 1's reading that "safe manner" is the whole act of which the later OEs are parts, not a poster of rights, is an editorial position.
13. Step 1's refusal to hang blood or implant devices under this document, despite the chapter intent's inclusive definition of medications, is an editorial position required by the owner's instruction.
14. Step 6's rule that a matching fitting is not confirmation, and that reconnection without a trace is forbidden, are editorial positions; the standard requires measures, not this sentence.
15. Steps 8 and 9's default that the hospital may forbid self-administration and home medicines, and that the standard creates no right to either, are editorial positions required by the owner's instruction.
16. Step 9 remaining Tier 1 despite Achievement level is the standing rule (asterisk allocates depth), recorded so a later reader does not "downgrade" it.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
17. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the National Medical Commission Act, 2019, the Indian Nursing Council Act, 1947, and the Drugs and Cosmetics Act, 1940 -- the statutes this document's References actually rely on. It does NOT name NDPS, BMW Rules 2016, FSS Act 2006, or CEA 2010. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- Rational prescribing and verbal orders -- MOM.3.
- Written-order artefact -- MOM.4.
- Dispensed-pack labelling, recalls, near-expiry at the hatch -- MOM.5.
- Post-administration monitoring, error/ADR capture -- MOM.7.
- NDPS register -- MOM.8.
- Implants -- MOM.9.
- Transfusion method -- COP.5.
- Injection technique reprint -- HIC.2.
- Device-infection bundles -- HIC.4.
- Waste colour categories -- HIC.3.
- Identifier pair definition -- COP.1.
- Discharge-summary medicine list -- AAC.8.
- ISMP minutes as a mandate.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 14 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 12 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 14; a search for "Hospital to define" without brackets finds all 14, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: who may administer by role, route and setting; where the administration method is held; prepared-medication label content; the acceptable timing window; mis-connection measures; how administration is documented; whether self-administration is allowed and the measures or the prohibition; whether outside medicines may be used and the measures or the prohibition; the named medication-administration lead; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation."""

SQL_HEADER = """-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 3, printed page 79
-- (PDF page index 85). Header: "Medications are administered safely."
-- Levels: a Commitment, b Commitment, c Commitment, d Core, e Commitment,
-- f Core, g Commitment, h Commitment, i Achievement.
-- FOUR OEs CARRY THE ASTERISK -- MOM.6.a, f, h, i.
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
        json_name="mom6_draft.json",
        sql_name="mom6_insert.sql",
    )
