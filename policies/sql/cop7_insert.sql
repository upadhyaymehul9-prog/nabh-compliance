-- COP.7 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 2, printed pages 64-65
-- (PDF page index 70-71). Levels: a Commitment, b Commitment, c Commitment, d Commitment,
-- e Commitment.
-- TWO OEs CARRY THE ASTERISK -- COP.7.a, COP.7.c.
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
  'COP.7',
  'COP',
  array['COP.7.a', 'COP.7.b', 'COP.7.c', 'COP.7.d', 'COP.7.e'],
  $q$Safe Obstetric Care$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} organises and provides obstetric care safely: how antenatal, labour, birth and postnatal care are run as a service; how high-risk obstetric cases are identified, cared for by competent doctors and nurses, and referred when this hospital cannot meet the need; how antenatal assessment includes maternal nutrition; how peri-natal and post-natal monitoring is performed; and how, when this hospital cares for high-risk obstetric cases, it has the human resources and facilities to take care of the neonates of those cases.

The chapter intent is that written guidance, applicable laws and regulations guide the care of high-risk obstetric patients. A labour room that is a room rather than a service, an antenatal clinic that never asks what the woman eats, or a high-risk birth without anyone who can receive the neonate, is not that care. This document is the process that makes the intent operational in the clinic, in the labour room, and at the moment of birth.

Obstetric care is where three legal duties sit on the same patient: the prohibition of sex determination, the law on termination of pregnancy where termination is provided, and the registration of live birth and stillbirth. This document exists so that those duties are part of the obstetric process, not notices on someone else's wall.$q$,
  $q$This policy applies to every location at {{HOSPITAL_NAME}} in which obstetric care is provided: the antenatal clinic, the labour room, the postnatal ward, the operation theatre insofar as a caesarean birth or an obstetric procedure is performed there, the emergency area insofar as an obstetric emergency is received, and any high-dependency or intensive-care area that receives an obstetric patient. It binds the doctors and nurses who provide obstetric care, the staff who identify high-risk pregnancy, the staff who monitor mother and neonate around birth, and whoever arranges referral of a high-risk case this hospital cannot manage.

It covers: organisation and safe provision of obstetric services; identification of high-risk obstetric cases, care of those cases by competent doctors and nurses, and referral to another appropriate centre where needed; inclusion of maternal nutrition in antenatal assessment; peri-natal and post-natal monitoring; and the human resources and facilities required to take care of neonates of high-risk obstetric cases.

If {{HOSPITAL_NAME}} does not provide obstetric services, this document is adapted to state that fact in the hospital's own words and is not used to invent a labour room the service directory does not define.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Imaging licences, including registration under the Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994 for ultrasonography capable of sex determination, and Atomic Energy Regulatory Board authorisations for radiation-generating equipment, are governed by the imaging-services policy of {{HOSPITAL_NAME}} (AAC.5). This policy owns the obstetric process, including that antenatal care does not include determination or communication of the sex of a foetus. AAC.5 owns the imaging registration, the statutory records that registration requires, and the licence calendar. A PC-PNDT registration is not obstetric care; an obstetric consultation that tells the family the sex is not an imaging-licence problem alone. Both documents are required. The statutory PC-PNDT notice displayed in imaging is owned by the laboratory-and-imaging-safety policy of {{HOSPITAL_NAME}} (AAC.6).
- Neonatal care of the baby — how neonates and children are cared for, including neonatal care in consonance with national or international guidelines — is governed by the paediatric-services policy of {{HOSPITAL_NAME}} (COP.8, a sibling being drafted separately). This policy (COP.7.e) owns that an obstetric service which cares for high-risk obstetric cases has the human resources and facilities to take care of the neonates of those cases: the backup at birth. COP.8 owns the care of the neonate after that backup has received the baby. COP.7 does not write neonatal clinical protocols. COP.8 does not write the obstetric service's duty to have that backup present.
- Transfer of a high-risk obstetric patient to another organisation is governed by the registration, admission and transfer policy of {{HOSPITAL_NAME}} (AAC.2). This policy owns the clinical identification of the high-risk case and the decision that referral is needed; AAC.2 owns the between-organisation transfer once that decision is made.
- Discharge of the mother and of the neonate from the organisation, and the discharge summary, are governed by the discharge policy of {{HOSPITAL_NAME}} (AAC.8). Registration of live birth and stillbirth under the Registration of Births and Deaths Act, 1969 is this obstetric process's statutory duty; the clinical discharge summary is AAC.8's. The two are not the same document. AAC.8 already distinguishes the clinical case summary of a death from the statutory death certificate; this document makes the parallel distinction for birth.
- Infection-control practices in the labour room and postnatal ward — hand hygiene, transmission-based precautions, PPE, device bundles, surveillance, biomedical waste, and reprocessing — remain with HIC.2, HIC.4, HIC.5, HIC.3 and HIC.6. This policy requires those practices in obstetric areas; it does not rewrite them.
- Uniform identifiers at the point of care are governed by the uniform-care policy of {{HOSPITAL_NAME}} (COP.1). Mother and neonate are each identified; this policy does not choose the identifier pair.
- Internal transfer of an obstetric patient into intensive or high-dependency care is governed by AAC.7 for the move and by COP.6 for admission criteria.
- Nutritional screening of in-patients in general is governed, when drafted, by COP.13. Paediatric nutritional, growth, developmental and immunisation assessment is COP.8.e. Kitchen hygiene is HIC.3. This policy owns maternal nutrition as part of antenatal assessment, not those other nutrition processes.
- The written definition of whether obstetric services are defined services is governed by AAC.1.
- Informed-consent method in general will be governed by PRE (not yet drafted). This policy owns that obstetric procedures, including termination where provided, are not performed without the consent the applicable law requires.
- The medical record itself is governed by the information-management policies of {{HOSPITAL_NAME}}.$q$,
  $q${{HOSPITAL_NAME}} organises and provides obstetric services safely. Antenatal care, labour, birth and postnatal care are a defined service with written guidance, not a room that is used when a woman arrives.

{{HOSPITAL_NAME}} identifies high-risk obstetric cases, cares for them with competent doctors and nurses, and refers them to another appropriate centre where this hospital cannot meet the need.

{{HOSPITAL_NAME}} includes maternal nutrition in antenatal assessment. An antenatal visit that never addresses what the woman eats is an incomplete assessment.

{{HOSPITAL_NAME}} performs appropriate peri-natal and post-natal monitoring of the mother and, where the neonate is this hospital's patient, of the neonate until paediatric care takes over.

{{HOSPITAL_NAME}}, when it cares for high-risk obstetric cases, maintains the human resources and facilities to take care of the neonates of those cases. How those neonates are then cared for is the paediatric-services policy.

{{HOSPITAL_NAME}} does not determine or communicate the sex of a foetus. Termination of pregnancy, where provided, is provided in consonance with the Medical Termination of Pregnancy Act, 1971 as amended in 2021. Live births and stillbirths are registered under the Registration of Births and Deaths Act, 1969.$q$,
  array[
    $s$1. Obstetric services organised and provided safely

Obstetric services are organised and provided safely. This step is the documented-evidence anchor of that asterisked requirement. Organisation means the service is defined, staffed, equipped and guided in writing. Safety means those arrangements are the ones used at a birth at night, not only the ones described for an assessment visit.

The obstetric scope of services of {{HOSPITAL_NAME}} is [Hospital to define — the obstetric scope of services, and where it is held]. It states whether antenatal care, labour and birth (including instrumental birth and caesarean birth), postnatal care, and termination of pregnancy are provided here, and the hours during which each is available. Alignment is with the current service directory under the definition-and-display policy of {{HOSPITAL_NAME}}. A service the directory does not define is not held out as obstetric care.

Written guidance for antenatal care, labour, birth and postnatal care is [Hospital to define — the written obstetric guidance, and where it is held]. The World Health Organization Safe Childbirth Checklist programme, and the Indian coaching-based evaluation of that programme (chapter reference 51 of this chapter), are a recognised framework this hospital may use. This document does not paste WHO checklist items as if they were mandated verbatim. The checklist {{HOSPITAL_NAME}} actually uses at birth, if it uses one, is [Hospital to define — the childbirth checklist used at birth, if a checklist is used]. ACOG Committee Opinion No. 390 on ethical decision-making in obstetrics and gynaecology (chapter reference 2 of this chapter) is recognised background for ethical decisions in this service; it is not imported as a protocol.

Staffing of the obstetric service — the doctors and nurses on duty for antenatal clinics, for labour and birth, and out of hours — is [Hospital to define — the obstetric staffing, including out of hours]. Qualifications and professional-council registration are verified under the human resource policies of {{HOSPITAL_NAME}}; this step uses that verification. The equipment and facilities of the labour room and antenatal clinic are [Hospital to define — the labour-room and antenatal-clinic equipment and facilities]. Equipment that is out of service is not counted as backing a birth the scope still claims.

Safety includes the legal duties that attach to obstetric care on this site.

Sex determination is prohibited. Antenatal care at {{HOSPITAL_NAME}} does not include determining the sex of a foetus or communicating a presumed sex to the patient, the family, or anyone else. Ultrasonography, where performed, is an imaging act whose registration, statutory records and licence calendar are owned by the imaging-services policy of {{HOSPITAL_NAME}}. This step owns the obstetric process that must not ask for, receive as a clinical goal, or pass on that information. The reason the prohibition sits in this document as well as in AAC.5 is that the conversation happens in the antenatal clinic and the labour ward, not only in the imaging room. A registration certificate in imaging does not stop an obstetrician who tells the family "it is a boy" from a scan performed elsewhere. The common error is the informal aside: a scan done for growth, a wink, a whispered sex, treated as courtesy rather than as the act the 1994 Act forbids. That aside is forbidden here. A request from a family to be told the sex is refused, and the refusal is the clinical act, not a bureaucratic one.

Termination of pregnancy, where it is within the obstetric scope, is provided in consonance with the Medical Termination of Pregnancy Act, 1971 as amended in 2021. The local arrangement — who may terminate, in which circumstances this hospital provides the service, and where the statutory opinion and consent records are held — is [Hospital to define — whether termination of pregnancy is provided here, and the MTP arrangement if it is]. If termination is not provided, that fact is stated in the obstetric scope and a patient who needs it is referred under step 2. This document does not write a gestational-limit table; the current Act, as amended, is the source, and the hospital verifies the current text.

Infection-control practices in the labour room, including hand hygiene, precautions, device bundles where devices are used, waste and reprocessing, follow the infection-control policies of {{HOSPITAL_NAME}}. They are not rewritten here. Two identifiers at the point of care follow the uniform-care policy; mother and neonate are each identified before any procedure and before any handover of the neonate.

The reason organisation and safety are one asterisked requirement, not two posters, is that an unstaffed labour room with a beautiful protocol is not a safe obstetric service, and a staffed room that determines sex, skips a checklist the hospital said it used, or runs without out-of-hours cover is not organised. The common error is to treat "safe obstetric care" as a laminated WHO poster and a labour table. The scope, the guidance actually used, the roster that backs a night birth, the refusal to determine sex, the MTP arrangement if any, and the identifiers, are the method that replaces that error.$s$,
    $s$2. High-risk obstetric cases: identify, care, refer

The organisation identifies and provides care to high-risk obstetric cases with competent doctors and nurses, and where needed, refers them to another appropriate centre.

The written criteria by which a pregnancy or a labour is identified as high-risk, and who may make that identification, are [Hospital to define — the high-risk obstetric criteria and who identifies them]. Identification is recorded in the antenatal record and, if it occurs first in labour, in the labour record. A high-risk label that is never written is not identification.

Care of a high-risk case that remains at {{HOSPITAL_NAME}} is provided by doctors and nurses whose competence for that care has been verified under the human resource policies of {{HOSPITAL_NAME}}. The named competent roster for high-risk obstetric care is [Hospital to define — the competent doctors and nurses who care for high-risk obstetric cases]. A high-risk labour is not left to a person who is not on that roster.

Where this hospital cannot provide the care the high-risk case needs — including when the neonatal backup at step 5 is not available for the neonate of that case — the patient is referred to another appropriate centre. The clinical decision to refer is this step's. The between-organisation transfer is performed under the registration, admission and transfer policy of {{HOSPITAL_NAME}}. Referral is not delayed until an emergency that this hospital has already said it cannot manage.$s$,
    $s$3. Antenatal assessment includes maternal nutrition

Antenatal assessment also includes maternal nutrition. This step is the documented-evidence anchor of that asterisked requirement. "Also" is the word that matters: nutrition is not a parallel dietetics service that may be offered, and it is not a weight written in a column. It is part of the antenatal assessment itself.

Every antenatal assessment at {{HOSPITAL_NAME}} includes a maternal-nutrition component. What that component covers — at least dietary history, nutritional risk (including anaemia risk as this hospital defines it), and the advice or supplementation offered — is [Hospital to define — the maternal-nutrition component of antenatal assessment]. Weight may be recorded as part of that component; weight alone is not the component. Who performs it, and where it is recorded on the antenatal record, are [Hospital to define — who records maternal nutrition in the antenatal assessment, and where it is recorded]. A tick without content is not inclusion.

The reason nutrition sits inside antenatal assessment, and why the standard asterisks it, is that maternal nutrition is a clinical determinant of the pregnancy, not a lifestyle extra. Anaemia, inadequate intake, and unaddressed nutritional risk are found in the clinic or they are found as a haemorrhage, a low-birth-weight neonate, or a postnatal woman who cannot recover. The antenatal visit that checks blood pressure and fundal height and never asks what the woman eats has not assessed the pregnancy it claims to have assessed. The common error is the column: a weight, sometimes a haemoglobin copied from a laboratory report, and a printed diet sheet handed over without a history. That column is not this step. The history, the recorded risk, and the advice or supplementation actually offered, on the antenatal record, are the method.

This step is not the in-patient nutritional-risk screen owned, when drafted, by the pain-rehabilitation-and-nutrition policy of {{HOSPITAL_NAME}}. It is not the paediatric nutritional, growth, developmental and immunisation assessment owned by the paediatric-services policy. It is not kitchen hygiene, which remains with the support-services infection-control policy. Those documents may share a dietitian; they do not share this assessment. An in-patient screen performed after admission does not complete antenatal maternal nutrition, and an antenatal nutrition note does not complete an in-patient screen.

Advice given under this step is recorded against the unique identification number. If the hospital refers the woman to dietetics, that referral is recorded; the referral does not replace the inclusion of nutrition in the antenatal assessment itself.$s$,
    $s$4. Peri-natal and post-natal monitoring

Appropriate peri-natal and post-natal monitoring is performed.

Peri-natal monitoring of the mother in labour and at birth, and post-natal monitoring of the mother after birth, follow written guidance. The observations, their interval, and where they are recorded are [Hospital to define — peri-natal and post-natal monitoring of the mother: observations, interval, and where recorded]. Monitoring is recorded against the unique identification number. A partograph or other labour record, if used, is [Hospital to define — the labour record used, if a partograph or other labour record is used]. This document does not mandate a named partograph.

Where the neonate is this hospital's patient, peri-natal and immediate post-natal monitoring of the neonate is performed by the neonatal backup at step 5 until the paediatric-services policy of {{HOSPITAL_NAME}} takes over the care. This step does not write neonatal clinical protocols.

Deterioration of the mother is escalated using the early-warning process of the assessment policy of {{HOSPITAL_NAME}} where that process applies, and using obstetric emergency response as the obstetric guidance at step 1 provides. Cardio-pulmonary resuscitation, when needed, uses the resuscitation policy.$s$,
    $s$5. Human resources and facilities for neonates of high-risk cases

The organisation caring for high-risk obstetric cases has the human resources and facilities to take care of neonates of such cases.

If {{HOSPITAL_NAME}} cares for high-risk obstetric cases, it maintains named human resources and named facilities that can receive and take care of the neonate of such a case at birth. Those resources and facilities are [Hospital to define — the human resources and facilities that take care of neonates of high-risk obstetric cases]. If those resources are not available for a given case, that case is referred under step 2 before birth whenever time allows, and is not booked as a high-risk birth this hospital cannot back.

This step is the obstetric service's backup duty. It is not the paediatric-services policy of {{HOSPITAL_NAME}}. COP.8 owns how neonates and children are cared for, including neonatal care in consonance with national or international guidelines, age-specific competency, and prevention of abduction and abuse. This document requires that the backup exists and is present for the high-risk birth. It does not write the neonatal care guideline. COP.8 does not write this backup duty.

Live births and stillbirths occurring at {{HOSPITAL_NAME}} are registered under the Registration of Births and Deaths Act, 1969. Who completes that registration, and where the record is held, are [Hospital to define — who registers live births and stillbirths, and where that record is held]. The statutory registration is not the discharge summary. The discharge of mother and neonate from the organisation remains with the discharge policy of {{HOSPITAL_NAME}}.$s$,
    $s$6. Records, review and the order of operations

Every antenatal assessment including its nutrition component, every high-risk identification, every labour, birth and postnatal record, every referral, every neonatal-backup attendance at a high-risk birth, and every birth registration is recorded against the unique identification number where a patient is involved, and is retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for obstetric records] for: an obstetric scope aligned with the service directory; written guidance used at birth rather than a poster unused; no record of sex determination or communication of foetal sex; MTP records where termination is provided; high-risk cases identified and either cared for on the competent roster or referred under AAC.2; antenatal records that include maternal nutrition beyond a weight column; peri-natal and post-natal monitoring recorded; neonatal backup present for high-risk births that occurred here; and live-birth and stillbirth registration under the 1969 Act.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a sex-determination incident, a high-risk birth without backup, a missing nutrition component, or a stillbirth that was not registered exposes a gap, or when the imaging, paediatric, transfer, discharge or infection-control policies that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} organising obstetric services as a defined safe service, for antenatal assessment that includes maternal nutrition, for high-risk cases being identified and either cared for or referred, and for neonatal backup existing when high-risk obstetric care is provided.

The person in charge of obstetric services authors and keeps current the obstetric scope and written guidance at step 1, holds the high-risk criteria and competent roster at step 2, holds the maternal-nutrition component of antenatal assessment at step 3, holds peri-natal and post-natal monitoring at step 4, and holds the neonatal-backup arrangement at step 5 without writing COP.8's neonatal care.

Doctors and nurses who provide obstetric care apply the written guidance, refuse to determine or communicate foetal sex, include maternal nutrition in antenatal assessment, identify high-risk cases, and do not conduct a high-risk birth this hospital cannot back.

The imaging service continues to own PC-PNDT registration under AAC.5. Obstetric staff still own the clinical prohibition.

The paediatric service, under COP.8 when drafted, owns how the neonate is cared for after the backup at step 5 has received the baby.

The quality or accreditation coordinator audits the records at step 6 and reports findings to the head of the institution.

All staff are expected to treat communication of foetal sex, a high-risk birth without backup, an antenatal record without maternal nutrition, and a birth that was not registered, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.7.
- Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994, insofar as it prohibits sex determination and communication of the sex of a foetus in obstetric care. Imaging registration and statutory imaging records remain with the imaging-services policy of {{HOSPITAL_NAME}}.
- Medical Termination of Pregnancy Act, 1971, as amended in 2021, where termination of pregnancy is provided.
- Registration of Births and Deaths Act, 1969, for registration of live births and stillbirths occurring at {{HOSPITAL_NAME}}.
- ACOG Committee Opinion No. 390: Ethical Decision Making in Obstetrics and Gynecology (2007) — chapter reference 2 of this chapter; recognised background; not imported as a protocol.
- Semrau, K. E., et al. (2017), Outcomes of a Coaching-Based WHO Safe Childbirth Checklist Program in India, New England Journal of Medicine, 377(24), 2313-2324 — chapter reference 51 of this chapter; a recognised framework for a childbirth checklist. The hospital's checklist is chosen locally and is not a verbatim paste of WHO items.
- Internal documents of {{HOSPITAL_NAME}}: the service directory; the obstetric scope of services; the written obstetric guidance and childbirth checklist; the high-risk criteria and competent roster; the antenatal record including the maternal-nutrition component; peri-natal and post-natal monitoring records; the neonatal-backup arrangement; the birth-registration record; the imaging-services policy; the paediatric-services policy; the registration, admission and transfer policy; the discharge policy; the infection-control policies; the uniform-care policy; and the information-management policies.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: the antenatal clinic; the labour room; the postnatal ward; the operation theatre; the emergency area; nursing administration; the person in charge of obstetric services; the person in charge of paediatric / neonatal backup; and the imaging service insofar as obstetric ultrasonography is performed.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The obstetric scope, the written obstetric guidance, the high-risk criteria, the antenatal record and the neonatal-backup arrangement — the working documents this policy requires — are held in the obstetric areas that use them.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO and OE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

MTP — Medical Termination of Pregnancy
PC-PNDT — Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act
RBD — Registration of Births and Deaths Act, 1969

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994, insofar as it prohibits sex determination in obstetric care, the Medical Termination of Pregnancy Act, 1971 as amended in 2021 where termination of pregnancy is provided, and the Registration of Births and Deaths Act, 1969 for registration of live births and stillbirths. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "COP.7.a", "requirement": "Obstetric services are organised and provided safely", "steps": "Steps 1, 6", "evidence": "The written obstetric scope of services, listing whether antenatal care, labour and birth including instrumental and caesarean birth, postnatal care and termination of pregnancy are provided, and the hours of each, aligned with the current service directory rather than holding out a service the directory does not define; the written obstetric guidance for antenatal care, labour, birth and postnatal care and where it is held; the childbirth checklist actually used at birth if one is used, showing WHO Safe Childbirth Checklist items were not pasted as if mandated verbatim; the obstetric staffing including out of hours, using human-resource verification of qualifications rather than restating it; the labour-room and antenatal-clinic equipment and facilities, with out-of-service equipment not counted as backing a claimed birth; records showing antenatal care did not include determination or communication of foetal sex, including records of a family request for sex being refused as a clinical act, and showing imaging PC-PNDT registration remained with the imaging-services policy rather than being treated as completing the obstetric prohibition; the written statement of whether termination of pregnancy is provided and, if it is, the MTP arrangement including who may terminate and where statutory opinion and consent records are held, or if it is not, the obstetric scope stating that fact and sample referrals; records of infection-control practices in the labour room following HIC.2, HIC.4, HIC.5, HIC.3 and HIC.6 rather than a local rewrite; records of two identifiers applied to mother and to neonate under the uniform-care policy before procedures and before handover of the neonate; briefing records of obstetric staff; the audit sample at step 6 of scope aligned with the directory, guidance used at birth, and no record of sex determination or communication of foetal sex", "responsible": "Person in charge of obstetric services holds the scope and guidance and requires the sex-determination prohibition in the obstetric process; imaging service owns PC-PNDT registration under AAC.5; HIC policies own infection-control method; quality or accreditation coordinator audits"}, {"oe_code": "COP.7.b", "requirement": "The organization identifies and provides care to high risk obstetric cases with competent doctors and nurses, and where needed, refers them to another appropriate centre", "steps": "Steps 2, 5, 6", "evidence": "The written high-risk obstetric criteria and who identifies them; sample antenatal and labour records showing the identification written; the named competent roster; sample high-risk cases cared for on that roster; sample referrals of cases this hospital could not manage, including when neonatal backup was not available, with the between-organisation transfer performed under AAC.2; the audit sample at step 6 of high-risk cases identified and either cared for or referred", "responsible": "Obstetric doctors and nurses identify high-risk cases and care for them on the competent roster; AAC.2 owns the between-organisation transfer; quality or accreditation coordinator audits"}, {"oe_code": "COP.7.c", "requirement": "Antenatal assessment also includes maternal nutrition", "steps": "Steps 3, 6", "evidence": "The written maternal-nutrition component of antenatal assessment, covering at least dietary history, nutritional risk including anaemia risk as this hospital defines it, and the advice or supplementation offered, and stating that weight alone is not the component; the named person who records it and the location on the antenatal record; sample antenatal records showing that component completed with content rather than a tick or a weight column only; records distinguishing this antenatal component from the in-patient nutritional-risk screen owned when drafted by COP.13, from paediatric nutritional assessment owned by COP.8.e, and from kitchen hygiene owned by HIC.3, including records showing an in-patient screen after admission was not treated as completing antenatal maternal nutrition; records of dietetics referral where used, showing the referral did not replace inclusion in the antenatal assessment itself; briefing records of staff who perform antenatal assessment; the audit sample at step 6 of antenatal records that include maternal nutrition beyond a weight column", "responsible": "Staff who perform antenatal assessment include and record maternal nutrition; person in charge of obstetric services holds the component; COP.13, COP.8 and HIC.3 remain owners of their nutrition processes; quality or accreditation coordinator audits"}, {"oe_code": "COP.7.d", "requirement": "Appropriate peri-natal and post-natal monitoring is performed", "steps": "Steps 4, 5, 6", "evidence": "The written peri-natal and post-natal monitoring of the mother (observations, interval, where recorded); the labour record used if a partograph or other labour record is used; sample monitoring records against the unique identification number; records of neonatal monitoring by the backup at step 5 until COP.8 takes over, without this document writing neonatal protocols; the audit sample at step 6 of peri-natal and post-natal monitoring recorded", "responsible": "Obstetric doctors and nurses monitor the mother; neonatal backup monitors the neonate until paediatric services take over; quality or accreditation coordinator audits"}, {"oe_code": "COP.7.e", "requirement": "The organization caring for high risk obstetric cases has the human resources and facilities to take care of neonates of such cases", "steps": "Steps 5, 2, 6", "evidence": "The named human resources and facilities that take care of neonates of high-risk obstetric cases; sample high-risk births showing that backup present; sample cases referred under step 2 when backup was not available rather than booked as a high-risk birth this hospital could not back; records distinguishing this backup duty from COP.8's ownership of how neonates are cared for; live-birth and stillbirth registration records under the Registration of Births and Deaths Act, 1969, distinguished from the AAC.8 discharge summary; the audit sample at step 6 of neonatal backup present for high-risk births that occurred here and of birth registration", "responsible": "Person in charge of obstetric services holds the backup arrangement; paediatric services under COP.8 own subsequent neonatal care; AAC.8 owns discharge of mother and neonate; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. COP.7 standard text and all five OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 2 Care of Patients, printed pages 64-65 (PDF page index 70-71). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: COP.7.a Commitment, COP.7.b Commitment, COP.7.c Commitment, COP.7.d Commitment, COP.7.e Commitment.
   TWO OEs CARRY THE ASTERISK -- COP.7.a and COP.7.c. The draft builds two separate deep blocks (step 1 for a; step 3 for c). COP.7.b, COP.7.d and COP.7.e are unasterisked and are correspondingly Tier 2.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the COP.7 pages read directly from the extracted page text, and the committed asterisk file. COP.7.a was among the 14 mismatches of the 2026-08-10 audit and is treated as asterisked, matching the committed file and the PDF.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. TWO OF FIVE OEs ARE TIER 1. Tier 1: COP.7.a and COP.7.c -- procedure steps 1 and 3 carry the reasoning (why organisation and safety are one requirement, why PC-PNDT sits in the obstetric process as well as in AAC.5, why maternal nutrition is inside antenatal assessment and not a weight column). Tier 2: COP.7.b (step 2), COP.7.d (step 4), COP.7.e (step 5) -- requirement and method without extended rationale. Reviewer to note the shallower treatment of b, d and e is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of COP.7.a/c against the approved HIC masters and the AAC drafts in /tmp/aac_drafts/. Search terms: obstetric, PC-PNDT, sex determination, antenatal, nutrition, labour, MTP, birth registration, neonate.
   AAC.5 (draft): USG PC-PNDT registration, statutory imaging records, licence calendar. This draft's Scope and step 1 own the obstetric prohibition on determining or communicating foetal sex and do not take the licence. Division stated explicitly.
   AAC.6: statutory PC-PNDT notice in imaging -- not restated.
   AAC.1: obstetric services as a defined service. Scope aligned; directory not rewritten.
   AAC.2: between-organisation transfer of high-risk cases. COP.7.b decides referral is needed; AAC.2 performs the transfer. Flagged in Scope and step 2.
   AAC.8: discharge of mother/neonate; statutory death certificate distinguished from case summary. This draft distinguishes RBD birth registration from the discharge summary.
   HIC.2/3/4/5/6 (approved): labour-room infection control, waste, bundles, surveillance, reprocessing. This draft requires them and does not rewrite them.
   COP.8 (sibling, not yet drafted): neonatal care guidelines vs COP.7.e backup. Scope states the division: COP.7 owns that obstetric service has neonatal backup; COP.8 owns how neonates/children are cared for.
   COP.13 (sibling): in-patient nutritional screen. COP.7.c is maternal nutrition in antenatal assessment. Division stated in Scope and step 3.
   COP.6 / AAC.7: obstetric patient into ICU. Pointed, not rewritten.
3. T2 QUICK CHECK: COP.7.b vs AAC.2 transfer -- flagged. COP.7.d monitoring vs AAC.3 early warning -- flagged in step 4 (escalation uses AAC.3 where it applies). COP.7.e vs COP.8 -- flagged in Scope as a standing intra-COP division.

STATUTORY AND EXTERNAL FACTS
4. PC-PNDT Act, 1994 -- cited insofar as the obstetric process must not determine or communicate foetal sex. Imaging licences remain AAC.5. No section number. No assertion which registration {{HOSPITAL_NAME}} currently holds.
5. Medical Termination of Pregnancy Act, 1971 as amended 2021 -- cited where termination is provided. No gestational-limit table is printed; the hospital verifies the current text. Whether this hospital provides MTP is [Hospital to define].
6. Registration of Births and Deaths Act, 1969 -- cited for live birth and stillbirth registration. Distinguished from AAC.8 discharge summary / death case summary.
7. Chapter refs 2 and 51 -- ACOG ethics opinion and WHO Safe Childbirth Checklist programme in India. Checklist items are NOT pasted as mandates.
8. Bio-Medical Waste Management Rules, 2016, Food Safety and Standards Act, 2006, and Clinical Establishments Act 2010 are NOT named in disclaimer paragraph 2. CEA is not used as a default.
9. NO NUMBERS ARE STATED as requirements -- no ANC visit count, no haemoglobin cutoff, no gestational-age table, no staffing ratio. Every such value is [Hospital to define].

EDITORIAL POSITIONS TAKEN
10. Step 1's rule that PC-PNDT sits in the obstetric conversation as well as in imaging registration, and that a whispered sex is the prohibited act, is an editorial position required by the overlap brief.
11. Step 1's refusal to paste WHO Safe Childbirth Checklist items, and refusal to print an MTP gestational table, are editorial positions.
12. Step 3's rule that weight alone is not maternal nutrition, and that an in-patient screen does not complete ANC nutrition, are editorial positions; the standard requires that antenatal assessment includes maternal nutrition.
13. Step 5's split -- backup exists here, neonatal care guidelines in COP.8 -- is an editorial position required by the intra-COP division brief.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
14. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names PC-PNDT 1994 (obstetric prohibition), MTP Act 1971 as amended 2021 (where provided), and RBD Act 1969 -- the statutes this document's References actually cite. It does NOT name BMW Rules 2016 or FSS Act 2006. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- USG PC-PNDT registration and imaging licence calendar -- AAC.5.
- PC-PNDT notice display -- AAC.6.
- Neonatal care guidelines, abduction/abuse -- COP.8.
- Between-organisation transfer method -- AAC.2.
- Discharge summary -- AAC.8.
- HIC labour-room practices -- HIC.2/3/4/5/6, not rewritten.
- In-patient nutrition screen -- COP.13.
- A numeric ANC schedule or haemoglobin cutoff.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 19 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 17 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 19; a search for "Hospital to define" without brackets finds all 19, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: the obstetric scope of services and where it is held; the written obstetric guidance and where it is held; the childbirth checklist used at birth if one is used; obstetric staffing including out of hours; labour-room and antenatal-clinic equipment and facilities; whether termination of pregnancy is provided and the MTP arrangement if it is; the high-risk obstetric criteria and who identifies them; the competent doctors and nurses who care for high-risk cases; the maternal-nutrition component of antenatal assessment; who records maternal nutrition and where; peri-natal and post-natal monitoring of the mother; the labour record used if any; the human resources and facilities for neonates of high-risk cases; who registers live births and stillbirths and where that record is held; the audit interval; the review interval for this policy; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
