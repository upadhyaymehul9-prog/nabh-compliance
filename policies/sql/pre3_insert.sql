-- PRE.3 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 4, printed page 88
-- (PDF page index 94). Levels: a Core, b Core, c Commitment, d Core.
-- TWO OEs CARRY THE ASTERISK -- PRE.3.a and PRE.3.c.
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
  'PRE.3',
  'PRE',
  array['PRE.3.a', 'PRE.3.b', 'PRE.3.c', 'PRE.3.d'],
  $q$Informed Consent$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} obtains informed consent from the patient or family for situations where informed consent is required, in a process that adheres to statutory norms; what information that consent includes; who can give consent when the patient is incapable of independent decision-making; and that consent is taken by the person performing the procedure.

The chapter intent is that informed consent is obtained from the patient or family for specified procedures and care, and that the key components of information include risks, benefits and alternatives. A signature on a blank form, a clerk collecting consent for a surgeon who is not in the building, or a copied oncology consent in a hospital that does not operate, is not that intent.

This document is the general consent method. That a transfusion, sedation, anaesthesia or surgical consent actually happened, before the act, remains the clinical policies that own those acts.$q$,
  $q$This policy applies to every situation at {{HOSPITAL_NAME}} in which informed consent is required: transfusion of blood and blood components, anaesthesia, surgery, initiation of any research protocol, and any other invasive or high-risk procedure or treatment the hospital has named. It binds the person who performs the procedure, the person who explains consent, the person who records it, and whoever decides who may consent when the patient cannot.

It covers: obtaining informed consent where it is required, with a process that adheres to statutory norms; the information consent includes (procedure, risks, benefits, alternatives, who will perform it, in a language they can understand); who can give consent when the patient is incapable of independent decision-making; and that consent is taken by the person performing the procedure.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- The right that consent is obtained before transfusion, anaesthesia, surgery, research and other invasive or high-risk treatment is listed under the beliefs-values-and-decision-making policy of {{HOSPITAL_NAME}} (PRE.2.g, sibling). This document owns the method. PRE.2 does not write the form.
- Transfusion consent before the unit is hung, including donation consent, is owned as a clinical act by the transfusion policy of {{HOSPITAL_NAME}} (COP.5). This document owns how consent is explained, recorded and who may give it. COP.5 owns that it was present before the act.
- Procedural-sedation consent before the sedative is given is owned as a clinical act by the procedural-sedation policy of {{HOSPITAL_NAME}} (COP.9). Same split.
- Anaesthesia consent before induction is owned as a clinical act by the anaesthesia policy of {{HOSPITAL_NAME}} (COP.10). A surgical consent silent on anaesthesia is not anaesthesia consent; COP.10 states that. This document owns the method both use.
- Procedural consent obtained by the doctor prior to the procedure is owned as timing and person by the procedures-and-operation-theatre policy of {{HOSPITAL_NAME}} (COP.11). COP.11 step 3 already requires the person performing (or a doctor of the same surgical team who will be present and responsible) to take it, and hands method to PRE. This document accepts that handoff.
- Implant counselling for usage and precautions is governed by the implant policy of {{HOSPITAL_NAME}} (MOM.9). That counselling is not surgical consent. This document owns surgical consent for the implanting procedure.
- Education about healthcare needs in a language and format they can understand is governed by the information-education-and-communication policy of {{HOSPITAL_NAME}} (PRE.4, sibling). PRE.3.b is the consent conversation. PRE.4 is ongoing education. They may use the same language; they are not the same act.
- Documentation, display and promotion of rights, including the right to refuse, are governed by PRE.1 and PRE.2.e. Refusal after information is a PRE.2 right; this document records that consent was not given.
- Research protocols, if this hospital initiates any, remain subject to this consent method and to whatever ethics arrangement the hospital has defined. This document does not invent a research-ethics committee for a hospital that does not do research; unused research is a recorded absence against the service directory (AAC.1).
- Organ-transplant consent, where a transplant programme exists, remains under COP.11's legal requirements for that programme. This document does not rewrite transplant statute.
- The medical record is governed by the information-management policies of {{HOSPITAL_NAME}} (IMS, not yet drafted). This policy owns the consent content written into that record.$q$,
  $q${{HOSPITAL_NAME}} obtains informed consent from the patient or family for situations where informed consent is required. The process adheres to statutory norms. A signature without the information in PRE.3.b is not informed consent.

{{HOSPITAL_NAME}} includes in that consent the procedure, its risks, benefits, alternatives, and who will perform it, in a language the patient or family can understand.

{{HOSPITAL_NAME}} describes who can give consent when a patient is incapable of independent decision-making, and implements that description.

{{HOSPITAL_NAME}} requires that informed consent is taken by the person performing the procedure.

{{HOSPITAL_NAME}} records a documented emergency that made prior consent impossible; emergency is not a standing exemption for convenience.$q$,
  array[
    $s$1. Informed consent obtained where required, process adhering to statutory norms

The organisation obtains informed consent from the patient or family for situations where informed consent is required. The informed consent process adheres to statutory norms. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask when consent is required here and how the process meets the law. The answer must be this hospital's written list of situations and a process that can satisfy the statutes this document actually cites — not a blank signed form, and not a copied Supreme Court quotation that the chapter bibliography does not name.

The reason this is the safety step is that the act without information is not care the patient agreed to. The chapter intent names specified procedures and care, and names risks, benefits and alternatives as key components. Kumar, Mullick, Prakash and Bharadwaj (2015) — chapter reference 10 — and Nandimath (2009) — chapter reference 13 — are the book's own legal sources on consent and the Indian medical practitioner. They are used as frameworks for what "informed" and "statutory norms" mean in Indian clinical practice. They are not pasted as a protocol, and they are not a mandate to print case names. Samira Kohli v. Dr. Prabha Manchanda is not a numbered reference of this chapter and is not imported as a NABH case-law mandate.

Situations where informed consent is required at {{HOSPITAL_NAME}} include at least: transfusion of blood and blood components; anaesthesia; surgery; initiation of any research protocol this hospital actually runs; and any other invasive or high-risk procedure or treatment this hospital has named. That list, including any addition this hospital makes, is [Hospital to define — the situations in which informed consent is required, including any addition beyond transfusion, anaesthesia, surgery, research and other invasive or high-risk treatment]. A class the service directory does not provide (for example research, or a procedure this hospital does not do) is a recorded absence, not a copied consent SOP.

How the consent process is run so that it adheres to statutory norms — when it is obtained, how it is recorded, how refusal is recorded, and how a documented emergency that made prior consent impossible is recorded — is [Hospital to define — how the informed-consent process is run so that it adheres to statutory norms, including recording of refusal and of a documented emergency]. Emergency is not a standing exemption because the list is long. COP.5, COP.9, COP.10 and COP.11 own that the relevant consent was present before those acts; this step owns the method they use.

The National Medical Commission Act, 2019 governs that a registered medical practitioner obtains consent consistent with professional practice. The Mental Healthcare Act, 2017 is applied at step 3 when that Act's definition of a person with mental illness is met; it is not applied as a blanket capacity statute for every unconscious surgical patient. The Indian Contract Act, 1872 is not named as a NABH mandate; it is not a numbered chapter reference.$s$,
    $s$2. Information included in informed consent

Informed consent includes information regarding the procedure, its risks, benefits, alternatives, and as to who will perform the procedure, in a language that they can understand.

How that information is given and recorded — form, language, and where it sits in the record — is [Hospital to define — how consent information (procedure, risks, benefits, alternatives, who will perform) is given and recorded, and in which language or format]. A form that lists "surgery" without the procedure, or that is silent on who will perform it, is incomplete. Language is the language the patient or family can understand; PRE.4 owns ongoing education in that language, not this conversation.

This document does not print a risks table or a named alternative as a NABH mandate.$s$,
    $s$3. Who can give consent when the patient is incapable of independent decision-making

The organisation describes who can give consent when a patient is incapable of independent decision-making and implements the same. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask who signed when the patient could not. The answer must be a written description this hospital uses, not an assumed husband, and not a Mental Healthcare Act process applied to a patient that Act does not cover.

The reason this is written separately from step 1 is that "patient or family" in the standard header is not a substitute for a rule. An unconscious adult, a child, and a person with mental illness as defined in the Mental Healthcare Act, 2017 are not the same incapacity. The common error is one next-of-kin stamp used for all three, or a copied MHCA nominated-representative SOP in a hospital that has not met that Act's definitions.

Who can give consent when the patient is incapable of independent decision-making — including a child, an unconscious or otherwise non-communicating adult, a documented emergency, and a person with mental illness as defined in the Mental Healthcare Act, 2017 where that Act applies — is [Hospital to define — who can give consent when the patient is incapable of independent decision-making, including child, unconscious adult, documented emergency, and a person with mental illness where the Mental Healthcare Act, 2017 applies]. For a person with mental illness as defined in that Act, nominated representative and advance directive under that Act are used; this document does not reprint those sections. For other incapacity, this hospital's description is used. This document does not print a family-hierarchy table as a NABH mandate.

The description is implemented: sample consents show the person who signed was a person the description allows, or a documented emergency with the reason and the person who decided to proceed.$s$,
    $s$4. Consent taken by the person performing the procedure

Informed consent is taken by the person performing the procedure.

Who that person is, for each class of procedure, is [Hospital to define — who is the person performing the procedure for the purpose of taking consent, for each class of procedure in use]. For surgery, the procedures-and-operation-theatre policy of {{HOSPITAL_NAME}} already requires the doctor who will perform the procedure, or a doctor of the same surgical team who will be present and responsible. This step applies that rule to every class in the step-1 list. A clerk, a nurse, or a doctor who will not be present, taking consent "for" the performer, does not meet this OE.

How that taking is recorded is the method at steps 1 and 2.$s$,
    $s$5. Records, review and the order of operations

The written list of situations, the process, the information method, the incapacity description, and consents in the record against the unique identification number, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for informed-consent records] for: consent present for situations in the list; information covering procedure, risks, benefits, alternatives and who will perform, in a language they can understand; the signer matching the incapacity description, or a documented emergency; consent taken by the person performing; no blank signed form; and no Samira Kohli quotation offered as the process.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a procedure in the list was done without consent, a clerk collected surgical consent, or an MHCA process was applied to a patient that Act does not cover, or when COP.5, COP.9, COP.10, COP.11 or PRE.2/PRE.4 that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} obtaining informed consent where it is required, by the person performing the procedure, under a process that adheres to statutory norms.

The named lead for informed consent authors and keeps current the list of situations, the process, the information method and the incapacity description. The named lead is [Hospital to define — the named lead for informed consent].

The person performing the procedure takes the consent. Staff who explain or witness do not replace that person. Staff who receive a refusal record it as refusal, not as a missing signature to be fetched later.

The quality or accreditation coordinator audits the records at step 5 and reports findings to the head of the institution.

All staff are expected to treat a blank signed form, consent taken by a person who will not perform the procedure, and an assumed next-of-kin for every incapacity, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Patient Rights and Education chapter, standard PRE.3.
- Kumar, A., Mullick, P., Prakash, S., & Bharadwaj, A. (2015). Consent and the Indian medical practitioner. Indian Journal of Anaesthesia, 59(11), 695-700 — chapter reference 10; used as a framework for informed consent in Indian clinical practice; not pasted as a protocol.
- Nandimath, O. (2009). Consent and medical treatment: The legal paradigm in India. Indian Journal of Urology, 25(3), 343 — chapter reference 13; used as a framework for statutory norms; not pasted as a protocol.
- National Medical Commission Act, 2019 — insofar as registered medical practitioners obtain informed consent consistent with professional practice.
- Mental Healthcare Act, 2017 — insofar as a person with mental illness as defined in that Act is incapable of independent decision-making; nominated representative and advance directive under that Act are not reprinted here.
- Internal documents of {{HOSPITAL_NAME}}: the list of situations requiring consent; the consent process; the incapacity description; consent records; the beliefs-values policy; the education policy; the transfusion, sedation, anaesthesia and procedures policies; the implant policy; the service directory; and the information-management policies.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every location that performs a procedure on the step-1 list; the operation theatre and anaesthesia; the emergency area; transfusion; nursing administration; and the named lead.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The list of situations, the process and the incapacity description — the working documents this policy requires — are held where those procedures are done.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

MHCA — Mental Healthcare Act, 2017
NMC — National Medical Commission

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the National Medical Commission Act, 2019, insofar as registered medical practitioners obtain informed consent consistent with professional practice, and the Mental Healthcare Act, 2017, insofar as a person with mental illness as defined in that Act is incapable of independent decision-making. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "PRE.3.a", "requirement": "The organisation obtains informed consent from the patient or family for situations where informed consent is required. Informed consent process adhered to statutory norms.", "steps": "Steps 1, 5", "evidence": "The written list of situations where informed consent is required, including at least transfusion, anaesthesia, surgery, research this hospital actually runs, and other invasive or high-risk treatment this hospital has named, with a recorded absence against the service directory for a class it does not provide rather than a copied consent SOP; the written process (when obtained, how recorded, how refusal is recorded, how a documented emergency that made prior consent impossible is recorded), showing a method that can satisfy the National Medical Commission Act, 2019 professional duty and that does not treat emergency as a standing exemption; the recorded use of Kumar et al. 2015 and Nandimath 2009 (chapter references 10 and 13) as frameworks not pasted protocols; the recorded refusal to import Samira Kohli v. Dr. Prabha Manchanda or the Indian Contract Act, 1872 as a NABH mandate, those not being numbered references of this chapter; sample consents against the unique identification number for situations in the list; sample COP.5/COP.9/COP.10/COP.11 records showing those policies own that consent was present before the act and this process was the method used; the location of the list and process; induction or briefing records of staff who take or witness consent; the audit sample at step 5 of consent present for listed situations rather than a blank signed form", "responsible": "Named lead holds the list and process; persons performing procedures take consent; COP.5/9/10/11 own that the relevant consent was present before those acts; head of the institution is accountable that listed situations are not done without consent; quality or accreditation coordinator audits"}, {"oe_code": "PRE.3.b", "requirement": "Informed consent includes information regarding the procedure; it's risks, benefits, alternatives and as to who will perform the procedure in a language that they can understand.", "steps": "Steps 2, 1, 5", "evidence": "The written information method covering procedure, risks, benefits, alternatives and who will perform, in a language they can understand; sample consents showing those elements rather than a form that says only 'surgery'; the recorded split that PRE.4 owns ongoing education in that language; the audit sample at step 5", "responsible": "Person taking consent gives the information; named lead holds the method; quality or accreditation coordinator audits"}, {"oe_code": "PRE.3.c", "requirement": "The organisation describes who can give consent when a patient is incapable of independent decision making and implements the same.", "steps": "Steps 3, 1, 5", "evidence": "The written description of who can give consent when the patient is incapable of independent decision-making, distinguishing a child, an unconscious or otherwise non-communicating adult, a documented emergency, and a person with mental illness as defined in the Mental Healthcare Act, 2017 where that Act applies, showing nominated representative and advance directive used under that Act without reprinting its sections, and showing that a single next-of-kin stamp is not used for all three incapacities; sample consents where the signer matches the description, or a documented emergency with reason and the person who decided to proceed; the recorded refusal to print a family-hierarchy table as a NABH mandate; the audit sample at step 5 of signers matching the description", "responsible": "Named lead holds the incapacity description; persons taking consent apply it; quality or accreditation coordinator audits"}, {"oe_code": "PRE.3.d", "requirement": "Informed consent is taken by the person performing the procedure.", "steps": "Steps 4, 1, 5", "evidence": "The named person-performing for each class of procedure in use; sample consents showing that person (or, for surgery, a doctor of the same surgical team who will be present and responsible, as COP.11 already requires) took the consent rather than a clerk, a nurse or a doctor who will not be present; the audit sample at step 5", "responsible": "Person performing the procedure takes consent; COP.11 owns surgical timing and person; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. PRE.3 standard text and all four OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 4, printed page 88 (PDF page index 94). Header quoted from the book: "Informed consent is obtained from the patient or family about their care." Official OE PRE.3.b uses "it's risks" (apostrophe); mapping quotes that official wording. Chapter intent printed page 85 (PDF page index 91): informed consent for specified procedures/care; key components include risks, benefits and alternatives. PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: PRE.3.a Core, PRE.3.b Core, PRE.3.c Commitment, PRE.3.d Core.
   TWO OEs CARRY THE ASTERISK -- PRE.3.a and PRE.3.c. PRE.3.b and PRE.3.d are unasterisked (Tier 2).
   Verified three ways on 2026-08-17: asterisk_extract.py against the download (matched committed scripts/shco_oe_asterisks.json on all 408), the PRE.3 page read directly, and the committed asterisk file.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. TWO OF FOUR OEs ARE TIER 1. Tier 1: PRE.3.a, PRE.3.c -- steps 1 and 3 carry the reasoning. Tier 2: PRE.3.b, PRE.3.d. Shallower treatment of b and d is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of PRE.3.a/c against HIC masters and AAC/COP/MOM drafts. Search terms: informed consent, capacity, family, transfusion, anaesthesia, surgery, research.
   PRE.2.g -- right that consent is obtained before listed acts vs this method. Stated in Scope.
   COP.5 / COP.9 / COP.10 / COP.11 -- CRITICAL HANDOFF ACCEPTED. Those drafts own that consent happened before the act and forwarded method to PRE. This document accepts method. COP.11 already requires the performing doctor (or same-team doctor present and responsible). Stated in Scope and steps 1 and 4.
   MOM.9 -- implant counselling is not surgical consent. Stated in Scope.
   PRE.4 -- language of ongoing education vs language of the consent conversation. Stated in Scope and step 2.
   PRE.2.e -- refusal as a right; this document records consent not given.
   AAC.1 -- unused research is a recorded absence, not a copied ethics SOP.
   IMS -- the record. Forward reference.
3. FORWARD REFERENCES: IMS; ethics arrangement if research exists. Each is a deliberate boundary.
4. T2 QUICK CHECK: PRE.3.b vs PRE.4.a language -- flagged. PRE.3.d vs COP.11 performing doctor -- accepted handoff; flagged so COP.11's forward-ref is landed.

STATUTORY AND EXTERNAL FACTS
5. NMC Act 2019 -- named in P2 insofar as RMPs obtain consent consistent with professional practice. No section number.
6. Mental Healthcare Act, 2017 -- named in P2 only for PRE.3.c when that Act's definition of a person with mental illness is met. Not a blanket capacity statute for every unconscious adult.
7. Kumar 2015 (ch ref 10) and Nandimath 2009 (ch ref 13) -- the chapter bibliography's legal sources. Used as frameworks. Not pasted.
8. Samira Kohli v. Dr. Prabha Manchanda -- NOT a numbered PRE chapter reference. NOT imported as a NABH case-law mandate. Owner asked to verify from the PDF bibliography; it is absent there.
9. Indian Contract Act, 1872 -- NOT a numbered chapter reference. NOT named in P2. Not imported as a NABH mandate.
10. Consumer Protection Act, 2019 and Clinical Establishments Act, 2010 are NOT named in P2 of this standard (PRE.1/PRE.5/PRE.6 may name CPA where they actually use it).
11. NO NUMBERS ARE STATED as requirements. No family-hierarchy table as a mandate.
12. Bio-Medical Waste Management Rules, 2016 and Food Safety and Standards Act, 2006 are NOT named in P2.

EDITORIAL POSITIONS TAKEN
13. Step 1's refusal to import Samira Kohli or the Contract Act as NABH mandates is an editorial position required by the owner's instruction to follow the PDF bibliography.
14. Step 3's split of child / unconscious adult / MHCA mental illness, and the refusal of a single next-of-kin stamp, are editorial positions; the standard requires a description, not this taxonomy.
15. Acceptance of the COP.5/9/10/11 handoff (they own that consent happened; this owns method) is an editorial position required by those drafts.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
16. Paragraphs 1, 3 and 4 are the shared block, hash-checked at build time. Paragraph 2 names NMC Act 2019 and MHCA 2017 only as used above. It does NOT name Contract Act 1872, CPA 2019, CEA 2010, BMW or FSS. The AAC.1 defaulted-statute bug is refused.

DELIBERATELY NOT INCLUDED
- Rights list -- PRE.2. Education method -- PRE.4.
- That transfusion/sedation/anaesthesia/surgical consent happened -- COP.5/9/10/11.
- Implant usage counselling -- MOM.9.
- Samira Kohli as a NABH mandate; Contract Act 1872; a printed family-hierarchy table; a research-ethics SOP for a hospital that does not do research.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 11 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 9 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 11; a search for "Hospital to define" without brackets finds all 11, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: situations requiring consent; how the process is run including refusal and emergency; how information is given and recorded; who can give consent when the patient is incapable; who is the person performing for each class; the named lead; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
