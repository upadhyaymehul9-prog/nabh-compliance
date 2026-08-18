-- AAC.6 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 1, printed page 53
-- (PDF page index 59). Levels: a Commitment, b Commitment, c Commitment,
-- d Commitment, e Commitment.
-- ONE OE CARRIES THE ASTERISK -- AAC.6.a. Whole of b-e is Tier 2.
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
  'AAC.6',
  'AAC',
  array['AAC.6.a', 'AAC.6.b', 'AAC.6.c', 'AAC.6.d', 'AAC.6.e'],
  $q$Laboratory and Imaging Safety$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} keeps the laboratory and the imaging service safe for the people who work in them and for the patients who pass through them: a laboratory-safety programme that is actually implemented; laboratory personnel trained and equipped to work safely; patients screened for safety and risk before imaging; radiation-safety devices and monitoring where they apply; and imaging signage that is up, in the right places, and saying the right thing.

The chapter intent is that laboratory and imaging services are provided by competent staff in a safe environment for both patients and staff. The laboratory-services policy and the imaging-services policy of {{HOSPITAL_NAME}} own the work those services do. This document owns that the environment in which that work is done is safe.

A safety programme that exists as a folder, or signage that exists as a purchase order, is not a safe environment. This document is the programme that has to be running on the day a reagent spills, a sharp breaks, a patient of childbearing age is about to be irradiated, or a visitor walks toward a restricted door.$q$,
  $q$This policy applies to the laboratory of {{HOSPITAL_NAME}} and to every imaging modality the hospital actually provides, including any outsourced arrangement only insofar as this hospital's own staff or patients are exposed on these premises. It binds laboratory personnel, imaging personnel, the person who leads the laboratory-safety programme, the person who issues and collects personnel-monitoring devices, and whoever maintains imaging signage. It does not assume that {{HOSPITAL_NAME}} provides magnetic resonance imaging, computed tomography, interventional radiology or nuclear medicine: those modalities appear only where the defined scope includes them.

It covers the laboratory-safety programme and its implementation, including incidents and review; training of laboratory personnel and the safety measures provided to them; screening of patients for safety and risk before imaging; use of radiation-safety and monitoring devices by imaging personnel and patients, and training in imaging and radiation safety; and prominent display of imaging signage in all appropriate locations.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Infection-prevention practices — hand hygiene, standard precautions, transmission-based-precaution personal protective equipment, and bloodborne-pathogen sharps safety, including in laboratory specimen-handling areas — are governed by the infection-prevention-and-control-practices policy of {{HOSPITAL_NAME}}. This policy owns the laboratory-safety programme as a whole: biosafety cabinets where the work requires them, chemical hygiene, fire as it arises from laboratory work, reagent and specimen spills other than the blood-and-body-fluid spill already governed there, and laboratory-specific protective equipment beyond standard precautions.
- Biomedical-waste colour code, on-site transport, storage, handover to the common treatment facility, and State Pollution Control Board authorisation are governed by the environment-and-waste policy of {{HOSPITAL_NAME}}. Pre-treatment of microbiological waste before it enters that stream is named here as a laboratory-safety duty; the stream itself is not restated.
- Specimen requisition, collection, identification, handling, transportation, processing and disposal, as a pathway that produces a valid result, are governed by the laboratory-services policy of {{HOSPITAL_NAME}}. This policy owns that those practices are safe for the staff who perform them.
- Imaging licences and authorisations — AERB authorisation for diagnostic radiology, PC-PNDT registration where ultrasonography capable of sex determination is performed — are governed by the imaging-services policy of {{HOSPITAL_NAME}}. That policy owns the licences. This policy owns the safety signage, including the radiation trefoil, restricted-area notices, pregnancy caution, and the PC-PNDT notice where ultrasonography is performed.
- The public display of defined healthcare services is governed by the definition-and-display policy of {{HOSPITAL_NAME}}. Isolation and infection-control signage is governed by the infection-control policies. Neither is imaging signage.
- The hospital fire-and-non-fire emergency plans are governed by the facility-management policies of {{HOSPITAL_NAME}}. This policy owns laboratory-specific fire risk (flammable reagents, electrical equipment at wet benches) and points those events at the hospital plan; it does not rewrite that plan.
- The hospital-wide hazardous-materials programme, where one exists under facility management, owns building-level chemical stores. This policy owns chemical hygiene at the laboratory bench.$q$,
  $q${{HOSPITAL_NAME}} implements a laboratory-safety programme. The programme is written, led, used on working days, and reviewed when something goes wrong and when the calendar says so.

Laboratory personnel are trained in safe practices and are provided with the safety measures the work requires. Training that is attendance without a practice, or equipment that is locked away from the bench, is not this requirement met.

Patients are screened for safety and risk before imaging, against a written checklist appropriate to the modality actually being used. A modality this hospital does not provide is not screened for.

Where radiation is used, imaging personnel and patients use the monitoring and protective devices that apply, and are trained in imaging-safety practices and radiation-safety measures. Doses to personnel are kept as low as reasonably achievable, within the limits the AERB authorisation requires. Those limits are not restated here as numbers.

Imaging signage is displayed prominently in every location it belongs. A sign in a drawer is not displayed.$q$,
  array[
    $s$1. The laboratory-safety programme — what it covers and why

{{HOSPITAL_NAME}} maintains a written laboratory-safety programme covering the laboratory as a place of work, not as a testing pathway. The testing pathway — how a specimen is requested, identified, processed and reported — is owned by the laboratory-services policy of {{HOSPITAL_NAME}}. This programme exists because a laboratory that produces correct results can still injure the people who produce them, and because an assessor asking whether a laboratory-safety programme is implemented will ask what it covers, not whether the laboratory quality-assurance file can be produced.

The programme covers, as laboratory safety:

- biosafety — the handling of potentially infectious material at the bench, the use of a biosafety cabinet where the work generates infectious aerosols or where microbiological culture is performed, and the rule that mouth pipetting is not used;
- chemical hygiene — labelling of reagents, storage that separates incompatibles, access to the safety information for each reagent in use, and the prohibition on storing food in a reagent refrigerator;
- fire as it arises from laboratory work — flammable reagents, open flames where they are still used, and electrical equipment at wet benches — pointing every fire event at the hospital fire plan rather than inventing a second one;
- spills of specimens and of reagents at the bench, other than the blood-and-body-fluid spill already governed by the infection-prevention-and-control-practices policy of {{HOSPITAL_NAME}};
- sharps generated at the laboratory bench (broken glass, coverslips, blades used in the laboratory). Sharps arising from bloodborne-pathogen exposure during specimen collection are governed by the infection-prevention policy; they are not rewritten here;
- pre-treatment of microbiological waste, where the laboratory generates it, before that waste enters the biomedical-waste stream owned by the environment-and-waste policy of {{HOSPITAL_NAME}}. Colour code, transport and the State Pollution Control Board authorisation stay with that policy.

The programme is the whole of those elements operating together. A laboratory that has a spill kit and no chemical hygiene, or a biosafety cabinet that is never certified, has a collection of objects and does not have a programme. That is why this step is the documented-evidence anchor, and why the common error is to point at the infection-control manual or the waste authorisation and call it laboratory safety.

The written programme is held at [Hospital to define — where the laboratory-safety programme is held], and the named lead is [Hospital to define — the named lead of the laboratory-safety programme].$s$,
    $s$2. Implementing the laboratory-safety programme

Implementation is the programme in use on a working day, not the existence of the file at step 1.

On every working day the laboratory of {{HOSPITAL_NAME}}:

- works only with the protective equipment the task requires, kept at the bench and in the sizes people actually wear — laboratory-specific equipment beyond standard precautions (for example a chemical-resistant glove or an eye shield for a reagent that standard-precaution gloves will not handle) is provided under this programme; standard-precaution gloves, gowns and masks remain the infection-prevention policy's;
- uses a biosafety cabinet, where the work at step 1 requires one, that has been certified as performing and has not been treated as a storage shelf;
- stores and labels reagents so that a person who did not put the bottle down can still read what it is;
- keeps a spill kit for reagent and specimen spills at the bench, used under the written method in the programme, with blood-and-body-fluid spills continuing to follow the infection-prevention spill procedure;
- pre-treats microbiological waste, where generated, before it is placed in the yellow stream the environment-and-waste policy already defines;
- stops work that cannot be done safely — a cabinet out of certification, a reagent without a label, a spill kit that has been used and not replenished — and records the stop.

The named lead at step 1 walks the laboratory at [Hospital to define — the interval at which the laboratory-safety lead walks the laboratory] and records what was found. A walk that never finds a defect is possible; a walk that is never done is not implementation.

Outsourced laboratory work performed on another organisation's premises is not this hospital's laboratory. Outsourced work performed by visiting staff in this hospital's laboratory is.$s$,
    $s$3. Laboratory-safety incidents and review

A laboratory-safety incident is any event the programme was built to prevent and failed to: a reagent or specimen spill, a bench-sharp injury, a chemical exposure, a fire or near-fire at the bench, work done in a biosafety cabinet that was out of certification, or microbiological waste that left the laboratory without the pre-treatment the programme requires.

Every such incident is recorded in [Hospital to define — the laboratory-safety incident register], with the date and time, what happened, who was involved, the immediate action, and the change made so that it does not recur. A bloodborne-pathogen sharps injury during specimen collection continues to be recorded and managed under the infection-prevention and occupational-health policies; it is not duplicated here. A bench-sharp injury that is not a bloodborne-pathogen exposure is recorded here and is still offered the occupational-health route if exposure cannot be excluded.

Incidents are reviewed with the named lead and at [Hospital to define — the review forum and interval for laboratory-safety incidents], and the programme at step 1 is revised when a gap is the cause. A register that is never read is not review.

The programme itself is reviewed at the same interval as this policy at step 8, and sooner after an incident that exposes a gap, after a change to the tests the laboratory performs, or after a revision of the infection-prevention or environment-and-waste policies this document hands work to.

The reason incidents sit inside the documented-evidence anchor rather than as an appendix: a programme that has never had an incident may be excellent or may be unreporting. The register, the review and the walk at step 2 are how {{HOSPITAL_NAME}} can tell which.$s$,
    $s$4. Laboratory personnel — training and safety measures

Laboratory personnel are trained in the safe practices the programme at steps 1 to 3 requires, before unsupervised bench work, and again at [Hospital to define — the interval for laboratory-safety training]. Training covers biosafety at the bench, chemical hygiene, spill response, bench-sharps, fire as it arises in the laboratory, and the pre-treatment duty for microbiological waste. It is assessed by return demonstration of the spill method and of the protective equipment the person's work uses, not by attendance alone.

The safety measures provided — protective equipment at the bench, the spill kit, access to reagent safety information, and a biosafety cabinet where the work requires one — are provided by {{HOSPITAL_NAME}} and are not a personal purchase. A measure that is not at the point of work is not provided.

Staff who only collect specimens and do not work at the laboratory bench are trained under the infection-prevention policy for that collection work; they are trained under this step only for the laboratory tasks they actually perform.$s$,
    $s$5. Screening patients for safety and risk before imaging

Every patient is screened for safety and risk before an imaging study is performed, against a written checklist appropriate to the modality being used. A checklist copied from a centre that has a different modality is the common defect: it asks questions this hospital cannot act on, and misses the ones it must.

The checklist is [Hospital to define — the pre-imaging safety/risk screening checklist, by modality provided]. It includes, as applicable to the modalities {{HOSPITAL_NAME}} actually provides:

- pregnancy status, or the possibility of pregnancy, before any study using ionising radiation to the abdomen or pelvis of a person who can be pregnant, and before any study the local protocol treats as requiring that question;
- previous reaction to contrast, and risk factors for contrast-associated kidney injury, where a contrast-enhanced study is intended;
- implanted or attached metal, electronic implants and other contraindications, where magnetic resonance imaging is provided.

Where a modality is not provided, it is not screened for. Magnetic resonance imaging is not assumed.

A study is not begun until the checklist for that modality is complete. A positive screen is acted on — delayed, modified, or not performed — and the action is recorded against the unique identification number. Screening is performed by [Hospital to define — who performs pre-imaging safety/risk screening].$s$,
    $s$6. Radiation-safety devices, monitoring and training

Where ionising radiation is used, imaging personnel and patients use the radiation-safety and monitoring devices that apply, and are trained in imaging-safety practices and radiation-safety measures.

Personnel who work with radiation-generating equipment wear a personnel-monitoring device — thermoluminescent dosimeter or optically stimulated luminescence dosimeter — issued, worn at the position the AERB authorisation requires, returned at [Hospital to define — the interval at which personnel-monitoring devices are issued and returned], and not left in a drawer or shared between two people. Dose records are held as the AERB authorisation requires. Doses are kept as low as reasonably achievable and within the limits that authorisation requires. Those limits are not restated in this document as numbers.

Protective devices — lead aprons, thyroid shields, and any other device the protocol for that study requires — are available, intact, and used by personnel and, where the protocol provides, by the patient. A device with a cracked or thinned protective layer is withdrawn. Patient shielding is used where it is applicable to the study and does not obscure the region being examined.

Training in these practices is given before unsupervised work with radiation-generating equipment, and again at [Hospital to define — the interval for imaging and radiation-safety training]. Staff who do not work with radiation are not trained as if they did.

ALARA is the principle — as low as reasonably achievable — not a figure. Technique, collimation, and not repeating a study without a reason are how the principle is applied. A numeric dose constraint copied from an old circular is not this step.$s$,
    $s$7. Imaging signage

Imaging signage is displayed prominently in every location it belongs: at the entrance to any area where radiation-generating equipment is used, on the door of a restricted area, in the waiting area from which a patient of childbearing age may be called, and, where ultrasonography capable of sex determination is performed, the statutory PC-PNDT notice.

The signs include, as applicable: the radiation trefoil; a restricted-area notice; a pregnancy-caution notice instructing a patient who is or may be pregnant to tell staff before a study using ionising radiation; and the PC-PNDT notice where ultrasonography is performed.

This signage is not the service display owned by the definition-and-display policy of {{HOSPITAL_NAME}}, and it is not isolation or infection-control signage owned by the infection-control policies. A board that lists the hospital's specialties does not satisfy this step. A precaution card on an isolation room does not satisfy this step.

The person who maintains the signs is [Hospital to define — the role that maintains imaging signage]. A missing, faded or obstructed sign is replaced. A sign stored for an inspection is not displayed.

Licences behind the activity the signs warn about remain on the imaging-licence calendar under the imaging-services policy of {{HOSPITAL_NAME}}.$s$,
    $s$8. Records, review and the order of operations

Every laboratory-safety walk, incident, training session and pre-treatment record; every pre-imaging screening checklist; every personnel-monitoring issue and dose record; and the current imaging signage locations are recorded and retrievable. Where a patient is involved, the unique identification number issued at registration is used.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for laboratory-and-imaging-safety records] for a laboratory-safety programme that was walked and whose incidents were reviewed, for training that included a demonstration, for screening checklists completed before the study, for personnel-monitoring devices issued and returned, and for signage present at the locations step 7 names.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when the laboratory's test list or the imaging scope changes, when a laboratory-safety or radiation incident exposes a gap, or when the laboratory-services, imaging-services, infection-prevention or environment-and-waste policies this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} running a laboratory-safety programme rather than holding a file, and for radiation work being performed only with the monitoring, devices and signage the AERB authorisation and this policy require.

The named lead of the laboratory-safety programme writes and walks the programme, records incidents, sees that microbiological waste is pre-treated before it enters the biomedical-waste stream, and revises the programme when a gap is found.

Laboratory personnel follow the programme, use the safety measures provided, complete training before unsupervised bench work, and report incidents.

Imaging personnel complete the pre-imaging checklist before a study, wear and return personnel-monitoring devices, use protective devices that are intact, and do not begin a study the screen has not cleared.

The person who issues personnel-monitoring devices keeps the issue, return and dose records the AERB authorisation requires.

The role that maintains imaging signage keeps every required sign visible in its location.

The infection-prevention team continues to own hand hygiene, standard and transmission-based precautions, and bloodborne-pathogen sharps, including in specimen-handling areas. The environment-and-waste function continues to own the biomedical-waste stream and the State Pollution Control Board authorisation. This policy does not take those duties over.

The quality or accreditation coordinator audits the records at step 8 and reports findings to the head of the institution.

All staff are expected to treat an unscreened imaging study, a monitoring device left in a drawer, a missing radiation sign, or laboratory work done without the protective equipment the task requires, as a defect, and to report it.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Access, Assessment and Continuity of Care chapter, standard AAC.6.
- Bio-Medical Waste Management Rules, 2016 — pre-treatment of microbiological waste before it enters the colour-coded stream; the stream, transport and State Pollution Control Board authorisation remain with the environment-and-waste policy of {{HOSPITAL_NAME}}.
- Atomic Energy Act, 1962, and the Atomic Energy (Radiation Protection) Rules, together with the authorisations issued by the Atomic Energy Regulatory Board — personnel monitoring, protective devices, restricted areas and the dose records the authorisation requires.
- Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994 — the statutory notice, where ultrasonography is performed. Registration under that Act is owned by the imaging-services policy of {{HOSPITAL_NAME}}.
- World Health Organization, Laboratory Biosafety Manual, 4th edition (2020) — the principle that laboratory safety is a programme covering biosafety, chemicals, fire, spills and sharps, applied here without importing that manual's facility grades as requirements.
- Internal documents of {{HOSPITAL_NAME}}: the laboratory-safety programme and incident register; laboratory-safety training records; the pre-imaging screening checklist; personnel-monitoring and dose records; the imaging-signage locations; the laboratory-services policy; the imaging-services policy (licence calendar); the infection-prevention-and-control-practices policy; the environment-and-waste policy; and the hospital fire plan.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: the laboratory; the imaging department; the named laboratory-safety lead; the person who issues personnel-monitoring devices; the role that maintains imaging signage; the infection-prevention team; the environment-and-waste function; biomedical engineering; and occupational health.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The laboratory-safety programme, the spill method, the pre-imaging checklist and the current signage list — the working documents this policy requires — are held in the laboratory and in imaging.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, BMW and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

AERB — Atomic Energy Regulatory Board
ALARA — As Low As Reasonably Achievable
OSL — Optically Stimulated Luminescence (dosimeter)
PC-PNDT — Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act
TLD — Thermoluminescent Dosimeter
UID — Unique Identification Number

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the Bio-Medical Waste Management Rules, 2016, the Atomic Energy Act, 1962 and the Atomic Energy (Radiation Protection) Rules together with the authorisations issued by the Atomic Energy Regulatory Board, and, where ultrasonography is performed, the Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "AAC.6.a", "requirement": "The laboratory-safety programme is implemented", "steps": "Steps 1, 2, 3, 8", "evidence": "The written laboratory-safety programme covering biosafety at the bench (including a biosafety cabinet where work generates infectious aerosols or microbiological culture is performed, and the prohibition on mouth pipetting), chemical hygiene (labelling, separation of incompatibles, reagent safety information at the point of use, no food in a reagent refrigerator), fire as it arises from laboratory work pointing at the hospital fire plan, specimen and reagent spills at the bench other than the blood-and-body-fluid spill owned by the infection-prevention policy, bench-sharps other than bloodborne-pathogen collection sharps, and pre-treatment of microbiological waste before it enters the biomedical-waste stream owned by the environment-and-waste policy; the named lead and the place the programme is held; records showing the programme in use on working days — protective equipment at the bench including laboratory-specific equipment beyond standard precautions, biosafety-cabinet certification current where a cabinet is required and the cabinet not used as a shelf, labelled reagents, a replenished spill kit, pre-treatment of microbiological waste where generated, and recorded stops of work that could not be done safely; the named lead's walk records at the stated interval; the laboratory-safety incident register with date and time, what happened, who was involved, immediate action and the change made, covering reagent or specimen spills, bench-sharp injuries, chemical exposures, fire or near-fire at the bench, work in an uncertified cabinet, and microbiological waste that left without pre-treatment; the review record at the stated forum and interval, and revisions of the programme after a gap; the recorded division that bloodborne-pathogen sharps injuries during collection continue under the infection-prevention and occupational-health policies and are not duplicated here; the audit sample at step 8 of walks that occurred and of incidents that were reviewed rather than of a folder titled laboratory safety", "responsible": "The named laboratory-safety lead writes, walks and revises the programme and records incidents; laboratory personnel work inside it and report incidents; infection-prevention owns standard precautions and bloodborne-pathogen sharps including in specimen-handling areas; environment-and-waste owns the biomedical-waste stream and the State Pollution Control Board authorisation; facility-management fire plans receive laboratory fire events; quality or accreditation coordinator audits implementation"}, {"oe_code": "AAC.6.b", "requirement": "Laboratory personnel are appropriately trained in safe practices and are provided with appropriate safety measures", "steps": "Steps 4, 8", "evidence": "Training records before unsupervised bench work and at the stated interval, covering biosafety, chemical hygiene, spill response, bench-sharps, laboratory fire and microbiological-waste pre-treatment, with return demonstration of the spill method and of the protective equipment the person's work uses; records that protective equipment, the spill kit, reagent safety information and a biosafety cabinet where required were provided at the point of work and not as a personal purchase", "responsible": "The named laboratory-safety lead trains and records competence; administration provides the measures at the bench; quality or accreditation coordinator audits"}, {"oe_code": "AAC.6.c", "requirement": "Patients are appropriately screened for safety / risk before imaging", "steps": "Steps 5, 8", "evidence": "The written pre-imaging checklist by modality actually provided (pregnancy where ionising radiation to abdomen or pelvis applies; contrast history and renal risk where contrast is used; metal and implant contraindications where MRI is provided — MRI not assumed); sample checklists completed before the study, against the unique identification number, with the action taken on a positive screen; the named role that screens", "responsible": "The named screening role completes the checklist before the study; imaging personnel do not begin an unscreened study; quality or accreditation coordinator audits"}, {"oe_code": "AAC.6.d", "requirement": "Imaging personnel and patients use appropriate radiation safety and monitoring devices where applicable, and are trained in imaging safety practices and radiation-safety measures", "steps": "Steps 6, 8", "evidence": "Personnel-monitoring issue, return and dose records as the AERB authorisation requires, at the stated interval, devices not shared; lead aprons, thyroid shields and other protocol devices available, intact and used, with cracked devices withdrawn; training records before unsupervised radiation work and at the stated interval; a recorded statement that numeric dose limits are those the AERB authorisation requires and are not restated in this policy", "responsible": "The person who issues monitoring devices keeps the records; imaging personnel wear them and use intact protective devices; quality or accreditation coordinator audits"}, {"oe_code": "AAC.6.e", "requirement": "Imaging signage is prominently displayed in all appropriate locations", "steps": "Steps 7, 8", "evidence": "The current list of imaging-signage locations and the signs in place — radiation trefoil, restricted-area notice, pregnancy caution, and the PC-PNDT notice where ultrasonography is performed; the named role that maintains them; a check that this list is not the service display and not isolation signage", "responsible": "The named signage role keeps signs visible; imaging-services policy owns the licences the signs warn about; definition-and-display policy owns service boards; infection-control policies own isolation cards; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. AAC.6 standard text and all five OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 1 Access, Assessment and Continuity of Care, printed page 53 (PDF page index 59). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: AAC.6.a Commitment, AAC.6.b Commitment, AAC.6.c Commitment, AAC.6.d Commitment, AAC.6.e Commitment.
   ONE OE CARRIES THE ASTERISK -- AAC.6.a. The draft builds the deep block in steps 1, 2 and 3 (what the laboratory-safety programme covers and why; implementation; incidents and review). AAC.6.b, AAC.6.c, AAC.6.d and AAC.6.e are unasterisked and are correspondingly Tier 2 -- the whole of b-e is lean.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the AAC.6 page read directly, and the committed asterisk file. AAC.6.a was not among the 14 mismatches of the 2026-08-10 audit.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. THE WHOLE STANDARD IS MOSTLY TIER 2 EXCEPT AAC.6.a. Tier 1: AAC.6.a -- procedure steps 1, 2 and 3 carry the reasoning (why laboratory safety is not the infection-control manual and not the waste authorisation, why a cabinet used as a shelf is not implementation, why an empty incident register is ambiguous). Tier 2: AAC.6.b (step 4), AAC.6.c (step 5), AAC.6.d (step 6) and AAC.6.e (step 7) -- requirement and method without extended rationale. Reviewer to note the shallower treatment of b, c, d and e is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of AAC.6.a against all six approved HIC masters and the approved AAC.1 master, plus the unapproved AAC.2, AAC.3, AAC.5, AAC.7 and AAC.8 drafts. Search terms: laboratory safety, biosafety, chemical, spill, sharps, microbiological waste, pre-treat.
   HIC.2: deliberate division stated in Scope and step 1 -- HIC.2 owns hand hygiene, standard/TBP PPE and bloodborne-pathogen sharps including in laboratory specimen-handling areas, and blood/body-fluid spills. This document owns the laboratory-safety programme as a whole (cabinets, chemical hygiene, fire, reagent spills, lab-specific PPE beyond standard precautions). Not an overlap; the two documents agree. Flagged for the reconciliation pass only as a T2-adjacent reminder that HIC.2's BMW segregation step also exists; colour code remains HIC.3's.
   HIC.3: deliberate division -- HIC.3 owns BMW colour code, transport, SPCB. This document names pre-treatment of microbiological waste as a lab-safety duty pointing at HIC.3's stream, without restating the four-colour code. Not an overlap.
   HIC.4: occupational exposure / PEP remains HIC.4's; a bench-sharp injury that cannot exclude exposure is offered that route. Not an overlap.
   AAC.1: isolation signage is HIC; service display is AAC.1. This document's step 7 restates that split for imaging signage. Not an overlap.
   AAC.5 (same pass, unapproved): AAC.5.a owns licences; AAC.6.e owns safety signage. Stated in both Scopes.
3. FORWARD REFERENCES CREATED BY THIS DRAFT: laboratory specimen pathway -- AAC.4, expected in the same pass, Scope states AAC.4 owns the pathway that produces a valid result and this owns that those practices are safe for staff; hospital fire plans -- FMS.5, not yet drafted, laboratory fire points at that plan; hospital hazardous materials -- FMS, not yet drafted, this owns bench chemical hygiene; hospital-wide equipment -- FMS.3, cabinet certification sits with whoever maintains the cabinet, named here as a lab-safety condition. Each is a deliberate boundary.
4. T2 QUICK CHECK: AAC.6.b training vs HIC.2 induction training -- this step is laboratory-task training, not a second copy of standard precautions. AAC.6.c screening vs AAC.5 reporting -- screening is safety, reporting is AAC.5. AAC.6.d TLD/OSL vs AAC.5 licences -- monitoring is this document; the AERB authorisation is AAC.5. AAC.6.e vs FMS.1.c internal/external signposting -- FMS owns wayfinding; this owns radiation/PC-PNDT/pregnancy signs. One-line flag for the FMS.1 reconciliation pass; not a contradiction with an approved document.

STATUTORY AND EXTERNAL FACTS
5. Bio-Medical Waste Management Rules, 2016 -- cited only for pre-treatment of microbiological waste before it enters the colour-coded stream. The four-colour code is not restated. No storage-hour figure is stated.
6. Atomic Energy Act, 1962 and the Atomic Energy (Radiation Protection) Rules with AERB authorisations -- cited for personnel monitoring, protective devices, restricted areas and dose records. NO numeric occupational dose limit is stated. The draft says "within the limits the AERB authorisation requires". Consistent with the standing rule's no-numbers default and with not restating a limit that the authorisation itself carries.
7. PC-PNDT Act, 1994 -- cited only for the statutory notice where ultrasonography is performed. Registration is AAC.5's.
8. WHO Laboratory Biosafety Manual, 4th edition (2020) -- cited as informing that laboratory safety is a programme covering biosafety, chemicals, fire, spills and sharps. Facility grades / biosafety levels from that manual are not imported as requirements, because an SHCO laboratory is not assumed to be a culture facility.
9. EXTERNAL CLINICAL/TECHNICAL FACT-CHECKING (Tier 1 OE AAC.6.a): the programme contents (biosafety, chemical hygiene, fire, spills, sharps, microbiological-waste pre-treatment) match the division the owner specified and the WHO LBM 4th ed. principle that safety is a programme rather than a single control. No BSL number, no cabinet class, no contact time, no ppm is stated. Mouth pipetting is prohibited as ordinary laboratory-safety practice, not as a numbered standard. Skip deep fact-checking on T2 OEs; nothing on its face was wrong. ALARA is named as a principle, not a number.
10. NO NUMBERS ARE STATED as requirements -- no mSv limits, no training hours, no walk frequency in days, no apron lead-equivalence in mm. Every such value is [Hospital to define] or "as the AERB authorisation requires".

EDITORIAL POSITIONS TAKEN
11. Step 1's refusal to let the infection-control manual or the waste authorisation stand in for a laboratory-safety programme is an editorial position consistent with the OE naming a laboratory-safety programme.
12. Step 2's rule that a biosafety cabinet used as a shelf is not implementation, and that work stops when it cannot be done safely, are editorial positions.
13. Step 3's observation that an empty incident register may mean excellence or unreporting is an editorial position; the walks and the review are the method chosen to tell them apart.
14. Step 6's refusal to restate numeric dose limits is required by the no-numbers default.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
15. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the Bio-Medical Waste Management Rules, 2016, the Atomic Energy Act 1962 and the Radiation Protection Rules with AERB authorisations, and the PC-PNDT Act 1994 where ultrasonography is performed -- the statutes this document's References actually cite. BMW IS relevant and is named. It does NOT name the Food Safety and Standards Act, 2006. The HIC wholesale inherit of FSS is refused by the build.

DELIBERATELY NOT INCLUDED
- Imaging licences and the imaging-report / critical-result / outsourcing / QA pathway -- AAC.5.
- Laboratory specimen pathway, TAT, lab critical values, lab outsourcing, lab QA -- AAC.4.
- Hand hygiene, standard/TBP PPE, bloodborne-pathogen sharps, blood/body-fluid spills -- HIC.2.
- BMW colour code, transport, SPCB -- HIC.3.
- Occupational PEP -- HIC.4.
- Hospital fire plans -- FMS.5.
- Service display -- AAC.1. Isolation signage -- HIC.
- Numeric dose limits in mSv.
- An assumption that the hospital has MRI, CT, interventional radiology or nuclear medicine.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 16 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 14 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 16; a search for "Hospital to define" without brackets finds all 16, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: where the laboratory-safety programme is held; the named lead of the laboratory-safety programme; the interval at which the laboratory-safety lead walks the laboratory; the laboratory-safety incident register; the review forum and interval for laboratory-safety incidents; the interval for laboratory-safety training; the pre-imaging safety/risk screening checklist by modality provided; who performs pre-imaging safety/risk screening; the interval at which personnel-monitoring devices are issued and returned; the interval for imaging and radiation-safety training; the role that maintains imaging signage; the audit interval for laboratory-and-imaging-safety records; the review interval for this policy; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
