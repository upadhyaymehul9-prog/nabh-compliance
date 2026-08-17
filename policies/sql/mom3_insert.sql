-- MOM.3 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 3, printed page 77
-- (PDF page index 83). Levels: a Commitment, b Core, c Commitment, d Excellence,
-- e Core, f Achievement, g Achievement, h Core.
-- THREE OEs CARRY THE ASTERISK -- MOM.3.a, MOM.3.b, MOM.3.e.
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
  'MOM.3',
  'MOM',
  array['MOM.3.a', 'MOM.3.b', 'MOM.3.c', 'MOM.3.d', 'MOM.3.e', 'MOM.3.f', 'MOM.3.g', 'MOM.3.h'],
  $q$Safe and Rational Prescription of Medications$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} prescribes medications safely and rationally: prescription in consonance with good practices for rational use; adherence to the hospital's determined minimum requirements of a prescription; ascertaining drug allergies and previous adverse drug reactions before prescribing; a mechanism that assists the clinician in choosing an appropriate medicine; verbal orders implemented so that medication management remains safe; audit of medication orders and prescriptions; corrective and preventive action from that audit; and reconciliation of medications at transition points of care.

The chapter intent is a safe and organised medication process. Prescription is governed by written guidance. This document is the clinical decision to prescribe. It is not the storage policy, and it is not the uniform order-writing policy: MOM.4 owns how an order appears in the record (location, legibility, authorised writers, name/route/strength/frequency). This document owns whether the prescription is rational, complete as a prescription, informed by allergy and previous reaction, assisted, safely verbal when verbal, audited, and reconciled at transitions.

Blood and blood components are not prescribed here as ward-stock medicines; the clinical transfusion method is the transfusion policy. Pain titration as a clinical loop is the pain policy; prescribing the analgesic is this document.$q$,
  $q$This policy applies to every clinician at {{HOSPITAL_NAME}} who prescribes a medicine, every location in which a prescription or medication order is written or given verbally, and the staff who record allergies, who receive verbal orders, who audit prescriptions, and who reconcile medicines at a transition. It binds employed practitioners and any visiting practitioner who prescribes under this hospital's unique identification number.

It covers: medication prescription in consonance with good practices and guidelines for rational prescription; adherence to the determined minimum requirements of a prescription; ascertaining drug allergies and previous adverse drug reactions before prescribing; a mechanism to assist the clinician in prescribing an appropriate medication; implementation of verbal orders so that medication management remains safe; audit of medication orders and prescriptions for safe and rational prescription; corrective and/or preventive action based on that audit where appropriate; and reconciliation of medications at transition points of patient care.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Uniform order writing — who may write orders, the uniform location in the record, legibility, dating, timing and signing, and the order-content fields of name, route, strength and frequency — is governed by MOM.4 (not yet drafted). MOM.4 owns how the order appears in the record. This document owns the clinical decision to prescribe rationally and the determined minimum of a prescription as a clinical document, which the hospital may define to include indication, allergies and other elements as well as those fields. This document does not duplicate MOM.4's four fields in a way that makes MOM.4 redundant.
- The formulary and non-formulary procedure are governed by MOM.1. This document requires prescription from the current formulary or through that procedure. It does not rewrite the formulary.
- Storage, high-risk and look-alike/sound-alike controls, and the emergency-medication list are governed by MOM.2. This document does not write cupboard method.
- Narcotic, psychotropic, chemotherapeutic and radioactive prescription by appropriate caregivers, and their storage, are governed by MOM.8 (not yet drafted). This document does not inherit the Narcotic Drugs and Psychotropic Substances Act, 1985 as a wholesale statute.
- Transfusion of blood and blood components is governed by COP.5. This document does not rewrite hanging a unit. Blood is not prescribed here as a ward-stock medicine.
- Two identifiers at the point of care are governed by COP.1. The unique identification number is generated under AAC.2. A prescription carries that number; this policy does not issue it.
- Initial assessment, including facts that may be collected there, is governed by AAC.3. Allergies may be collected at assessment. Completing an assessment checkbox is not the act of ascertaining allergy and previous adverse reaction before this prescription. MOM.3.c owns that ascertaining.
- Internal transfer and the handover method used on that move are governed by AAC.7. AAC.7 owns the move. Reconciliation of medications at that transition is MOM.3.h.
- The discharge summary, including medication instructions the patient takes away, is governed by AAC.8. AAC.8 owns the summary. Reconciliation at discharge as a transition is MOM.3.h. The two must not disagree; they are not the same act.
- Pain assessment and titration according to need and response are governed by COP.13. COP.13 owns the clinical loop. Prescribing the analgesic is this document.
- Procedural sedation and anaesthesia are governed by COP.9 and COP.10. Those policies own the clinical act. Prescribing the sedative or anaesthetic agent, as a prescription, is this document; storage of any NDPS agent among them is MOM.8.
- The service directory is governed by AAC.1. Rational prescription is within defined services; this document does not invent a specialty the directory declined.
- Safe injection is governed by HIC.2. Pharmaceutical waste is governed by HIC.3. Device bundles are governed by HIC.4. Pointed, not restated; Bio-Medical Waste Management Rules are not named in the statutory paragraph of the disclaimer.
- Counselling and education about medicines are governed by PRE (not yet drafted). The medical record itself is governed by IMS (not yet drafted).$q$,
  $q${{HOSPITAL_NAME}} prescribes medications in consonance with good practices for rational prescription. A medicine added because it is familiar, or a combination that has no recorded indication, is not that practice.

{{HOSPITAL_NAME}} adheres to the determined minimum requirements of a prescription. An incomplete prescription is not dispensed by hoping the next person will guess.

{{HOSPITAL_NAME}} ascertains drug allergies and previous adverse drug reactions before prescribing. A checkbox ticked at assessment and never looked at at the moment of prescribing is not that ascertaining.

{{HOSPITAL_NAME}} has a mechanism that assists the clinician in prescribing an appropriate medication.

{{HOSPITAL_NAME}} implements verbal orders so that medication management remains safe. An unwritten shout from a corridor is not a verbal order under this document.

{{HOSPITAL_NAME}} audits medication orders and prescriptions for safe and rational prescription, and takes corrective and preventive action where the audit shows it is needed.

{{HOSPITAL_NAME}} reconciles medications at transition points of patient care.$q$,
  array[
    $s$1. Rational prescription in consonance with good practices

Medication prescription at {{HOSPITAL_NAME}} is in consonance with good practices and guidelines for the rational prescription of medications. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask what "rational" means here and how a prescription is judged against it. The answer must be this hospital's written good-practice method, used at the point of prescribing, not a WHO poster in the seminar room.

The reason rational prescription is the safety step is that harm from medicines is often a medicine that did not need to be given, or a combination that no one can explain. Polypharmacy without indication, an antibiotic for a viral presentation because it is expected, a branded product when the formulary equivalent would do and was not considered, a child's dose guessed from an adult habit, are how an organised pharmacy still injures. The common error is to equate "rational" with "from the formulary". Formulary adherence is MOM.1.f. A listed medicine can still be the wrong medicine for this patient. This step is the clinical decision.

The good practices and guidelines this hospital uses for rational prescription are [Hospital to define — the good practices and guidelines this hospital uses for rational prescription]. World Health Organization work on promoting rational use of medicines (chapter reference 23), the National List of Essential Medicines 2018 (chapter reference 21), the WHO Model Lists of Essential Medicines (chapter reference 19), and WHO drug-use indicators (chapter reference 9) may inform that method. They are not pasted as protocols and they are not this hospital's standard treatment guidelines unless the hospital has adopted them. Standard treatment guidelines this hospital actually uses, if any, are part of the placeholder above. This document does not print an antibiotic protocol, a dose table, or a duration in days.

Who may prescribe is a registered medical practitioner whose registration under the National Medical Commission Act, 2019 and the State Medical Council is current, and any other practitioner the hospital's written method and their professional registration both allow. Human-resource procedures verify registration; this step uses that verification. Schedule H and Schedule H1 medicines under the Drugs and Cosmetics Act, 1940 and Rules are prescribed, not sold as if they were general items. This step does not reprint those schedules.

Prescription is from the current formulary or through the non-formulary procedure. Pain medicines are prescribed here; titration after they are given remains the pain policy. Sedative and anaesthetic agents, as prescriptions, are written here; the clinical act of sedation or anaesthesia remains those policies. Narcotic and psychotropic prescription by appropriate caregivers remains MOM.8 for that class; this step still requires that the prescription is rational.

The written rational-prescription guidance is held at [Hospital to define — where the written rational-prescription guidance is held].$s$,
    $s$2. Determined minimum requirements of a prescription

{{HOSPITAL_NAME}} adheres to the determined minimum requirements of a prescription. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask what this hospital has determined a prescription must contain, and whether yesterday's prescriptions contain it. The answer must be a written minimum that clinicians use, not a claim that everyone knows how to write an order.

The reason a determined minimum is the safety step is that an incomplete prescription shifts the clinical decision onto the person who dispenses or administers. A missing strength, a missing route, a name that could be two products, an indication that cannot be reconstructed, are how a later person invents what the prescriber did not decide. The common error is to treat MOM.4's four order-content fields (name, route, strength, frequency) as this OE, so that the two standards become one paragraph and MOM.4 has nothing left to own. MOM.4 owns how the order appears in the record: authorised writers, uniform location, name and unique identification number on that location, legibility, date, time, signature, and those four fields as order content. This step owns the determined minimum of a prescription as a clinical document. The hospital's minimum may include those elements and also indication, known allergies, the patient's identity, and any other element this hospital determines. This document does not itself list MOM.4's four fields as if they were this OE's entire content.

The determined minimum requirements of a prescription are [Hospital to define — the determined minimum requirements of a prescription]. National Coordinating Council for Medication Error Reporting and Prevention recommendations on accuracy of prescription and medication-order writing (chapter references 25 and 26) may inform that minimum. They are not imported as a numeric rule and they are not the only acceptable set. Error-prone abbreviations (chapter reference 13) may inform what this hospital forbids; this document does not print a banned-abbreviation table as a NABH mandate.

A prescription that does not meet the minimum is not a prescription under this document. It is returned to the prescriber to complete, not guessed into a dose. How an incomplete prescription is returned, and who may not complete it by inference, are [Hospital to define — how an incomplete prescription is returned to the prescriber, and who may not complete it by inference].

The written minimum is held at [Hospital to define — where the determined minimum requirements of a prescription are held], including at the place of prescribing. Out-patient prescriptions and in-patient medication orders both meet this hospital's minimum as it applies to each form; the hospital may determine one minimum with form-specific notes, not two contradictory minima.$s$,
    $s$3. Drug allergies and previous adverse drug reactions ascertained before prescribing

Drug allergies and previous adverse drug reactions are ascertained before prescribing.

How they are ascertained, and where the finding is recorded so that the prescriber sees it at the moment of prescribing, are [Hospital to define — how drug allergies and previous adverse drug reactions are ascertained before prescribing, and where the finding is recorded so that the prescriber sees it]. Ascertained means the prescriber has looked, including a recorded unknown or a recorded none, before the medicine is chosen. An assessment form under AAC.3 may already have collected allergy facts. Completing that checkbox is not this act. This step owns the look before this prescription.

A known allergy or previous reaction to a proposed medicine stops that prescription unless a documented clinical reason is recorded by the prescriber. This document does not write a desensitisation protocol.

Counselling the patient about an allergy remains PRE when drafted. This step owns the ascertain-before-prescribe act.$s$,
    $s$4. Mechanism to assist the clinician in prescribing an appropriate medication

{{HOSPITAL_NAME}} has a mechanism to assist the clinician in prescribing an appropriate medication.

The mechanism is [Hospital to define — the mechanism that assists the clinician in prescribing an appropriate medication]. Examples a hospital may choose — formulary available at the point of prescribing, standard treatment guidelines, a defined enquiry route to the pharmacy, an electronic prompt if one exists — are examples, not a mandated product. This document does not require a named software. It requires that a mechanism exists and that clinicians can actually use it at the time they prescribe.

Assistance is not a substitute for the prescriber's decision at step 1, and it is not the MOM.4 order-writing layout.$s$,
    $s$5. Verbal orders implemented so that medication management remains safe

Implementation of verbal orders at {{HOSPITAL_NAME}} ensures safe medication management practices. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask when a verbal order is allowed, how it is received, and how it becomes a written order. The answer must be a written method staff have used at night, not a ban that everyone ignores or an open permission that never becomes writing.

The reason a verbal-order method is the safety step is that speech is how the wrong medicine, the wrong patient and the wrong dose enter care without a record that can be checked. A shout from a corridor, a telephone instruction that one nurse heard and another thought she heard, an order that is given and never written, are how verbal convenience becomes an undocumentable event. The common error is either to forbid verbal orders in a policy while they continue in practice, or to allow them without a read-back and without a later written order, so that the administration record is the only trace. NCCMERP recommendations to reduce medication errors associated with verbal medication orders and prescriptions (chapter reference 27) are a recognised framework for read-back and for limiting verbal orders to situations that need them. They are not imported as a numeric sign-off time and they are not the only acceptable method.

When a verbal order is permitted, who may give it, who may receive it, and how it is recorded, are [Hospital to define — when a verbal order is permitted, who may give it, who may receive it, and how it is recorded]. Permitted means defined situations (a typical example is an emergency in which the prescriber cannot at that moment write), not "whenever it is quicker". Who may give a verbal order is a person who may prescribe at step 1. Who may receive it is named. Recording includes the medicine, the dose the hospital's minimum at step 2 requires, the patient unique identification number, the giver, the receiver, and the time. This document does not state a number of minutes within which the order must be signed. How the verbal order becomes a written or signed order, and who is responsible for that, are [Hospital to define — how a verbal order becomes a written or signed order, and who is responsible for that].

Read-back — the receiver repeating the order and the giver confirming — is the method this document expects unless the hospital's written method records a defined alternative that still catches a mis-heard name or dose. Look-alike names are a known verbal risk; the high-risk list under the storage policy informs which names need particular care; this step does not rewrite storage.

A verbal order still ascertains allergy at step 3 insofar as the emergency allows; if it could not, the record states why and the ascertaining is completed as soon as it can be. A verbal order for an NDPS agent, if ever permitted, still uses MOM.8's register; this step does not create a spoken exception to that cupboard.

The written verbal-order method is held at [Hospital to define — where the written verbal-order method is held], including in the areas that would use it. A method that lives only in the quality office is not implementation.$s$,
    $s$6. Audit of medication orders and prescriptions

Audit of medication orders and prescriptions is carried out to check for safe and rational prescription of medications.

What is audited, the sample, the interval, and who performs the audit are [Hospital to define — what is audited in medication orders and prescriptions, the sample, the interval, and who performs the audit]. The audit looks at rational prescription against step 1, completeness against step 2, allergy ascertained against step 3, verbal orders against step 5, and formulary adherence as MOM.1 requires. WHO drug-use indicators (chapter reference 9) may inform measures; they are not mandated as a numeric set.

The audit record is dated and retrievable. An audit that is planned and not done is not an audit.$s$,
    $s$7. Corrective and preventive action based on the audit

Corrective and/or preventive action is taken based on the audit, where appropriate.

How actions are assigned, dated and closed, and the forum that reviews them, are [Hospital to define — how corrective and preventive actions from the prescription audit are assigned, dated and closed, and the forum that reviews them]. Where appropriate means an audit that finds no defect records that finding; an audit that finds a defect produces an action. An action that is recorded and not done is not an action.

The multidisciplinary medication committee under the pharmacy-committee policy is an available forum; this hospital may name another. This step owns that the prescription audit leads to action, not only to a percentage.$s$,
    $s$8. Reconciliation of medications at transition points of patient care

Reconciliation of medications occurs at transition points of patient care.

The transition points at which reconciliation is performed, and the method used, are [Hospital to define — the transition points at which medication reconciliation is performed, and the method used]. Transitions include at least admission, internal transfer, and discharge, and any other point this hospital names. AAC.7 owns the internal-transfer move and handover method; this step owns that medicines are reconciled as part of that transition, not that the move is rewritten. AAC.8 owns the discharge summary including medication instructions; this step owns that the medicines in force are reconciled at discharge so that the summary can be right. Completing a handover checkbox is not reconciliation. Completing a discharge-medication list without comparing it to what the patient was actually taking is not reconciliation.

WHO High 5s medication reconciliation (chapter reference 29), WHO medication safety in transition of care (chapter reference 17), and AHRQ medication reconciliation (chapter reference 16) are recognised frameworks. This document does not mandate a named tool or a proprietary form as a NABH requirement.

Who performs reconciliation at each named transition is [Hospital to define — who performs medication reconciliation at each named transition]. The result is recorded against the unique identification number: medicines continued, stopped, changed, and the reason where a change is made. A discrepancy that is noticed and not resolved is a defect of this step.$s$,
    $s$9. Records, review and the order of operations

Every prescription and medication order, allergy ascertaining, verbal order, prescription audit, corrective action, and reconciliation at a named transition is recorded against the unique identification number and is retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for prescription, verbal-order and reconciliation records] for: prescriptions that meet the determined minimum rather than guessed completions; rational prescription against this hospital's good-practice method rather than familiarity; allergy looked at before the medicine rather than only an assessment checkbox; verbal orders that were permitted, read back and then written, rather than unwritten shouts; audits of prescriptions that produced action where needed; and reconciliation at named transitions that compared lists rather than copied the last one. MOM.4 order-writing defects are handed to MOM.4 rather than absorbed as this document's minimum.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a wrong-medicine prescription, an unwritten verbal order, a missed allergy, a transition without reconciliation, or a revision of the formulary, order-writing, assessment, transfer, discharge or pain policies that this document hands work to, exposes a gap.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} prescribing rationally, for a determined minimum that is actually used, for verbal orders that become written orders, and for reconciliation at named transitions.

The named person who holds the rational-prescription guidance, the determined minimum, and the verbal-order method is [Hospital to define — the named person who holds the rational-prescription guidance, the determined minimum, and the verbal-order method].

Prescribing clinicians apply steps 1 to 5, ascertain allergy before the medicine, do not complete an incomplete prescription by inference when they are the receiver, and reconcile at the transitions they own.

Staff who receive a verbal order record it, read it back, and do not administer an unwritten shout as if it were an order.

The person or forum at step 6 audits prescriptions. The person assigned an action at step 7 closes it.

The quality or accreditation coordinator audits the records at step 9 and reports findings to the head of the institution.

All staff are expected to treat an incomplete prescription that was guessed, a verbal order that was never written, a known allergy that was not looked at, and a transition that copied the last list without comparing it, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.3.
- Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules — insofar as Schedule H and Schedule H1 medicines are prescribed rather than sold as general items.
- National Medical Commission Act, 2019 and State Medical Council registration — insofar as they govern who may prescribe.
- Promoting rational use of medicines: core components, World Health Organization (2012) — chapter reference 23; informs rational-use method; not pasted as a protocol.
- National List of Essential Medicines (2018) — chapter reference 21; may inform formulary-aligned rational choice; not pasted as a protocol.
- Model Lists of Essential Medicines, World Health Organization — chapter reference 19; a recognised framework; not mandated.
- How to Investigate Drug Use in Health Facilities, World Health Organization (1993) — chapter reference 9; drug-use indicators may inform audit; not a mandated numeric set.
- Recommendations to Enhance Accuracy of Prescription/Medication Order Writing, National Coordinating Council for Medication Error Reporting and Prevention (2015) — chapter references 25 and 26; a recognised framework for the determined minimum; not imported as a numeric rule.
- Recommendations to Reduce Medication Errors Associated with Verbal Medication Orders and Prescriptions, National Coordinating Council for Medication Error Reporting and Prevention (2015) — chapter reference 27; a recognised verbal-order framework; not a mandated sign-off time.
- List of Error-Prone Abbreviations, Institute for Safe Medication Practices (2017) — chapter reference 13; may inform what this hospital forbids; not a mandated table.
- Medication Reconciliation, Agency for Healthcare Research and Quality Patient Safety Network (2019) — chapter reference 16; a recognised framework; not a mandated tool.
- Medication Safety in transition of care, World Health Organization (2019) — chapter reference 17; a recognised framework.
- The High 5s Project – Standard Operating Protocol Assuring Medication Accuracy at Transitions in Care: Medication Reconciliation, World Health Organization (2014) — chapter reference 29; a recognised framework; not a mandated proprietary form.
- Internal documents of {{HOSPITAL_NAME}}: the rational-prescription guidance; the determined minimum requirements of a prescription; the allergy-ascertaining method; the prescribing-assistance mechanism; the verbal-order method; the prescription-audit method and CAPA forum; the reconciliation method at named transitions; the formulary and pharmacy-committee policy; the storage policy; the order-writing policy; the assessment, internal-transfer and discharge policies; the pain, sedation, anaesthesia and transfusion policies; and the information-management policies.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every in-patient ward; the out-patient department; day-care; the emergency area; the operation theatre and recovery; intensive or high-dependency areas where they exist; the pharmacy; nursing administration; every head of department whose staff prescribe; and the members of the multidisciplinary medication committee.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The rational-prescription guidance, the determined minimum, the verbal-order method and the reconciliation method — the working documents this policy requires — are held at the place of prescribing and in the areas that receive verbal orders or perform transitions.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

ADR — Adverse Drug Reaction
CAPA — Corrective and Preventive Action
NCCMERP — National Coordinating Council for Medication Error Reporting and Prevention
NLEM — National List of Essential Medicines
NMC — National Medical Commission
NDPS — Narcotic Drugs and Psychotropic Substances (Act, 1985), named only as the statute MOM.8 will own; not inherited here

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, insofar as Schedule H and Schedule H1 medicines are prescribed, and the National Medical Commission Act, 2019, insofar as it governs who may prescribe. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "MOM.3.a", "requirement": "Medication prescription is in consonance with good practices and guidelines for rational prescription of medications.", "steps": "Steps 1, 6, 9", "evidence": "The written good-practice method this hospital uses for rational prescription, held at the place of prescribing rather than as a WHO poster in a seminar room, and showing that rational is not equated with formulary adherence alone (MOM.1.f owns formulary adherence; a listed medicine can still be the wrong medicine); the named guidelines actually used, with WHO promoting rational use, NLEM 2018, WHO EML and WHO drug-use indicators (chapter references 9, 19, 21, 23) recorded as frameworks that may inform and not as pasted protocols, antibiotic tables or mandated durations; sample prescriptions against the unique identification number showing a recorded indication or a recorded clinical reason rather than a combination no one can explain; the named roles who may prescribe, with current registration under the National Medical Commission Act, 2019 and State Medical Council used from human-resource verification, and Schedule H / H1 medicines prescribed under the Drugs and Cosmetics Act, 1940 rather than sold as general items; records of prescription from the current formulary or through the MOM.1 non-formulary procedure; records distinguishing this prescription of an analgesic from COP.13 titration, this prescription of a sedative or anaesthetic from COP.9 / COP.10 clinical acts, and this rational-use look from MOM.8's 'appropriate caregiver' rule for narcotic and psychotropic agents; the location of the written guidance; induction or briefing records of prescribing clinicians; the audit sample at steps 6 and 9 of rational prescription against this hospital's method rather than familiarity", "responsible": "Prescribing clinicians apply the good-practice method; named person holds the guidance; human resource function verifies registration; quality or accreditation coordinator audits"}, {"oe_code": "MOM.3.b", "requirement": "The organisation adheres to the determined minimum requirements of a prescription.", "steps": "Steps 2, 6, 9", "evidence": "The written determined minimum requirements of a prescription as a clinical document, held at the place of prescribing, including the hospital's chosen elements (which may include indication, known allergies, patient identity and other determined items as well as name, route, strength and frequency) and showing the recorded split that MOM.4 owns how the order appears in the record (authorised writers, uniform location, unique identification number on that location, legibility, date, time, signature, and those four fields as order content) so that this OE is not written as a duplicate that makes MOM.4 redundant; the recorded statement that NCCMERP prescription-writing recommendations (chapter references 25 and 26) and ISMP error-prone abbreviations (chapter reference 13) are frameworks the hospital may use, not a numeric rule and not a mandated banned-abbreviation table; the written method for returning an incomplete prescription to the prescriber rather than guessing it into a dose, and who may not complete it by inference; sample out-patient prescriptions and in-patient medication orders showing the minimum met for each form, or returned rather than inferred; induction or briefing records of prescribers and of staff who would otherwise complete by inference; the audit sample at steps 6 and 9 of prescriptions that meet the determined minimum rather than guessed completions, with MOM.4 layout defects handed to MOM.4", "responsible": "Prescribing clinicians meet the minimum; staff who receive a prescription return an incomplete one rather than infer; named person holds the written minimum; MOM.4 owns order appearance in the record when drafted; quality or accreditation coordinator audits"}, {"oe_code": "MOM.3.c", "requirement": "Drug allergies and previous adverse drug reactions are ascertained before prescribing.", "steps": "Steps 3, 9", "evidence": "The written method for ascertaining allergy and previous adverse reaction, and where the finding is recorded so the prescriber sees it at the moment of prescribing; sample records showing a look before the medicine (including recorded none or unknown) rather than only an AAC.3 assessment checkbox; records of a known allergy stopping the prescription unless a documented clinical reason was recorded; the audit sample at step 9", "responsible": "Prescribing clinicians ascertain before choosing the medicine; AAC.3 may collect the fact; PRE owns counselling when drafted; quality or accreditation coordinator audits"}, {"oe_code": "MOM.3.d", "requirement": "The organisation has a mechanism to assist the clinician in prescribing an appropriate medication.", "steps": "Steps 4, 1, 9", "evidence": "The written mechanism (formulary at the point of prescribing, standard treatment guidelines, pharmacy enquiry route, electronic prompt if used, or other local method) and records that clinicians can use it at the time they prescribe; the recorded statement that no named software is mandated; the audit sample at step 9", "responsible": "Named person holds the mechanism; prescribing clinicians use it; quality or accreditation coordinator audits"}, {"oe_code": "MOM.3.e", "requirement": "Implementation of verbal orders ensures safe medication management practices.", "steps": "Steps 5, 2, 3, 9", "evidence": "The written verbal-order method stating when a verbal order is permitted (defined situations such as an emergency in which the prescriber cannot at that moment write, not whenever it is quicker), who may give it (a person who may prescribe at step 1), who may receive it, and how it is recorded (medicine, the dose elements the determined minimum requires, unique identification number, giver, receiver, time) without a mandated number of minutes for later signature presented as a NABH requirement; the written method for how the verbal order becomes a written or signed order and who is responsible for that, showing that an unwritten shout is not an order under this document; the recorded expectation of read-back unless a defined alternative that still catches a mis-heard name or dose is written, with NCCMERP verbal-order recommendations (chapter reference 27) used as a framework not as a numeric sign-off rule; sample verbal-order records against the unique identification number showing permission, read-back, recording and later writing rather than a corridor instruction that never became a record; records of allergy ascertaining at step 3 insofar as the emergency allowed, or a recorded reason why it could not and completion afterwards; the recorded division that a verbal NDPS order, if ever permitted, still uses MOM.8's register rather than a spoken exception to that cupboard, and that look-alike names take care informed by the MOM.2 high-risk list without rewriting storage; the location of the method in the areas that would use it rather than only in the quality office; induction or briefing records of staff who give or receive verbal orders; the audit sample at step 9 of verbal orders that were permitted, read back and then written", "responsible": "Prescribers give verbal orders only when permitted; receivers record, read back and do not administer an unwritten shout; named person holds the method; MOM.8 owns any NDPS register; quality or accreditation coordinator audits"}, {"oe_code": "MOM.3.f", "requirement": "Audit of medication orders and prescriptions is carried out to check for safe and rational prescription.", "steps": "Steps 6, 9", "evidence": "The written audit method including what is looked at, the sample, the interval and who performs it; sample audit records covering rational prescription, completeness, allergy, verbal orders and formulary adherence; the audit sample at step 9 of audits that were done rather than only planned", "responsible": "Named auditor performs the audit; quality or accreditation coordinator reviews that it ran"}, {"oe_code": "MOM.3.g", "requirement": "Corrective and/or preventive action is taken based on the audit, where appropriate.", "steps": "Steps 7, 6, 9", "evidence": "The written method for assigning, dating and closing actions and the named forum; sample actions closed; records of an audit with no defect stating that finding rather than inventing an action; the audit sample at step 9", "responsible": "Named forum assigns actions; the person assigned an action closes it; quality or accreditation coordinator audits"}, {"oe_code": "MOM.3.h", "requirement": "Reconciliation of medications occurs at transition points of patient care.", "steps": "Steps 8, 9", "evidence": "The named transition points and the written method; who performs reconciliation at each; sample records at admission, internal transfer and discharge showing medicines continued, stopped or changed rather than a copied list; the recorded split that AAC.7 owns the move and AAC.8 owns the discharge summary; the recorded statement that WHO High 5s, WHO transition-of-care and AHRQ reconciliation (chapter references 16, 17, 29) are frameworks not a mandated tool; the audit sample at step 9", "responsible": "Named persons reconcile at each transition; AAC.7 owns the move; AAC.8 owns the summary; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. MOM.3 standard text and all eight OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 3 Management of Medication, printed page 77 (PDF page index 83). Header quoted from that page: "Medications are prescribed safely and rationally." THIS is the real MOM.3 header; MOM.5's OE-page header wrongly copies this wording and is not this standard. The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page (https://nabh-portal-live.s3.ap-south-1.amazonaws.com/wp-content/uploads/2025/07/13110738/SHCO-Standards-3rd-Edition.pdf, md5 39e3bc86d73d651b9cfef283bbf018a9, 188 pages). Levels: MOM.3.a Commitment, MOM.3.b Core, MOM.3.c Commitment, MOM.3.d Excellence, MOM.3.e Core, MOM.3.f Achievement, MOM.3.g Achievement, MOM.3.h Core.
   THREE OEs CARRY THE ASTERISK -- MOM.3.a, MOM.3.b and MOM.3.e. The draft builds three separate deep blocks (step 1 for a; step 2 for b; step 5 for e). MOM.3.c, MOM.3.d, MOM.3.f, MOM.3.g and MOM.3.h are unasterisked and are correspondingly Tier 2.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed, 408 OEs, 132 asterisks; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the MOM.3 page read directly from the extracted page text, and the committed asterisk file.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. THREE OF EIGHT OEs ARE TIER 1. Tier 1: MOM.3.a, MOM.3.b, MOM.3.e -- procedure steps 1, 2 and 5 carry the reasoning (why formulary adherence is not rationality, why MOM.4's four fields must not be copied as this minimum, why an unwritten shout is not a verbal order). Tier 2: MOM.3.c (step 3), MOM.3.d (step 4), MOM.3.f (step 6), MOM.3.g (step 7), MOM.3.h (step 8) -- requirement and method without extended rationale. Reviewer to note the shallower treatment of c, d, f, g and h is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of MOM.3.a/b/e against the approved HIC.1-HIC.6 masters, the AAC.1-AAC.8 drafts and the COP.1-COP.13 drafts. Search terms: prescription, prescribe, verbal order, allergy, reconciliation, order writing, analgesic, sedation, transfusion, formulary.
   MOM.4 -- CRITICAL SPLIT, stated in Scope and step 2. MOM.4 owns uniform order writing in the record. MOM.3.b owns the determined minimum of a prescription as a clinical document. Do not duplicate MOM.4's four fields so as to make MOM.4 redundant. Flagged for parent log and for the MOM.4 drafter to mirror.
   MOM.1 -- formulary / non-formulary. Rational is not the same as listed. Stated in step 1.
   COP.5 -- transfusion not rewritten; blood not ward-stock prescription.
   COP.13 -- pain titration vs prescribing the analgesic. Stated in Purpose, Scope and step 1.
   COP.9 / COP.10 -- clinical act vs this prescription of the agent.
   AAC.3 -- allergies may be collected at assessment; MOM.3.c owns ascertaining before prescribing. Flagged as T2 one-line in item 4; stated in Scope because T1 steps also touch it at verbal-order emergency.
   AAC.7 / AAC.8 -- move/summary vs MOM.3.h reconciliation. T2; stated in Scope because the split is structural.
   COP.1 / AAC.2 -- identifiers and UID. Applied.
   HIC.2 / HIC.3 / HIC.4 -- injection, waste, device bundles. Pointed.
   AAC.1 -- rational prescription within defined services.
   PRE / IMS -- undrafted.
   MOM.8 -- NDPS not inherited; verbal NDPS still uses MOM.8 register.
3. FORWARD REFERENCES: MOM.4 order writing (sibling, not yet drafted); MOM.8 NDPS; PRE education; IMS record. Each is a deliberate boundary.
4. T2 QUICK CHECK: MOM.3.c vs AAC.3 -- assessment checkbox is not ascertaining before this prescription; flagged for parent log. MOM.3.d -- no named software mandated. MOM.3.f/g -- audit and CAPA; committee is an available forum. MOM.3.h vs AAC.7/AAC.8 -- reconciliation vs move vs discharge summary; flagged for parent log. WHO High 5s / AHRQ are frameworks not mandated tools. Nothing added to the HIC reconciliation list.

STATUTORY AND EXTERNAL FACTS
5. Drugs and Cosmetics Act, 1940 and Rules -- cited insofar as Schedule H / H1 medicines are prescribed. No schedule reprinted. No dose as a mandate.
6. National Medical Commission Act, 2019 -- cited insofar as it governs who may prescribe. No section number.
7. WHO rational use / NLEM 2018 / WHO EML / drug-use indicators (ch refs 9, 19, 21, 23) -- frameworks, not pasted protocols.
8. NCCMERP prescription writing (25/26) and verbal orders (27) -- frameworks, not numeric sign-off rules.
9. WHO High 5s (29), WHO transition-of-care (17), AHRQ med rec (16) -- frameworks, no mandated tool name as a NABH requirement.
10. NDPS Act 1985 is NOT named in P2.
11. NO NUMBERS ARE STATED as requirements -- no doses, no sign-off hours, no audit percentages. Every such value is [Hospital to define].
12. Bio-Medical Waste Management Rules, 2016, Food Safety and Standards Act, 2006, and Clinical Establishments Act, 2010 are NOT named in P2.

EDITORIAL POSITIONS TAKEN
13. Step 1's rule that formulary adherence is not rationality is an editorial position required to keep MOM.1.f and MOM.3.a distinct.
14. Step 2's refusal to print MOM.4's four fields as this OE's entire minimum is an editorial position required by the owner's instruction.
15. Step 5's default of read-back, with a written alternative permitted, and the refusal to state a sign-off time in hours, are editorial positions; NCCMERP informs, it does not mandate a number here.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
16. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the Drugs and Cosmetics Act, 1940 (Schedule H/H1 prescription) and the National Medical Commission Act, 2019 (who may prescribe) -- the statutes this document's References actually rely on. It does NOT name NDPS, BMW Rules 2016, FSS Act 2006, or CEA 2010. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- Formulary and committee -- MOM.1.
- Storage, LASA, emergency list -- MOM.2.
- Uniform order writing (authorised writers, location, legibility, four content fields as order appearance) -- MOM.4.
- Dispensing -- MOM.5.
- Administration -- MOM.6.
- Post-administration monitoring -- MOM.7.
- NDPS / chemo / radioactive -- MOM.8.
- Transfusion method -- COP.5.
- Pain titration loop -- COP.13.
- Internal-transfer method -- AAC.7.
- Discharge-summary method -- AAC.8.
- Assessment dataset -- AAC.3.
- A named e-prescribing product, a mandated High 5s form, or a numeric verbal-order sign-off time.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 20 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 18 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 20; a search for "Hospital to define" without brackets finds all 20, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: the good practices and guidelines used for rational prescription; where that guidance is held; the determined minimum requirements of a prescription; how an incomplete prescription is returned; where the minimum is held; how allergies and previous ADRs are ascertained and where recorded; the prescribing-assistance mechanism; when a verbal order is permitted, who may give and receive it, and how it is recorded; how a verbal order becomes written; where the verbal-order method is held; what the prescription audit covers, sample, interval and who performs it; how CAPA from that audit is assigned and the forum; transition points and reconciliation method; who reconciles at each transition; the named person who holds the guidance, minimum and verbal-order method; the audit interval for these records; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
