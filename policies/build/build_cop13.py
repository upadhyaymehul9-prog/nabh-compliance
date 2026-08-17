# -*- coding: utf-8 -*-
"""Builds the COP.13 master policy draft: JSON for review + SQL for later insert.

UNAPPROVED DRAFT. Do not insert, approve, or write this to Supabase.

THIS IS DRAFTED UNDER THE TWO-TIER DEPTH STANDING RULE (2026-08-10) AND THE
DISCLAIMER STATUTE-MATCHING STANDING RULE (2026-08-17), both in
scripts/master-policy-todos.md.

Tier is decided by doc_required / the asterisk in the official PDF:
  Tier 1 (full treatment): COP.13.a, COP.13.c, COP.13.e
  Tier 2 (lighter pass):   COP.13.b, COP.13.d, COP.13.f

Official source: NABH Standards for Small Healthcare Organisations, 3rd Edition
(August 2022), Chapter 2, standard COP.13 and OEs COP.13.a-f, read from the
official standards PDF (downloaded 2026-08-17 from the NABH website's Explore
NABH Standards page), printed pages 68-69, PDF page index 74-75.

Asterisks verified 2026-08-17: scripts/asterisk_extract.py re-run against that
download (self-validation passed, 408 OEs, 132 asterisks, output matched the
committed scripts/shco_oe_asterisks.json on all 408 entries) and the COP.13
pages read directly. COP.13.a, COP.13.c and COP.13.e carry the asterisk;
COP.13.b, d and f are unasterisked. COP.13.c was among the 14 flags flipped
by the 2026-08-10 audit (now asterisked); the 2026-08-17 re-run confirms the
asterisk on c.
"""
from policy_build_common import emit_and_verify, make_disclaimer

STANDARD_CODE = "COP.13"
CHAPTER = "COP"
OE_CODES = [
    "COP.13.a", "COP.13.b", "COP.13.c",
    "COP.13.d", "COP.13.e", "COP.13.f",
]
TIER1_OES = ["COP.13.a", "COP.13.c", "COP.13.e"]

POLICY_TITLE = "Pain Management, Rehabilitation Services and Nutritional Therapy"

VERSION = "1.0"
REVISION_HISTORY = [
    {"version": "1.0", "date": "17-08-2026", "description": "Initial release."},
]

PURPOSE = """This document sets out how {{HOSPITAL_NAME}} provides pain management, rehabilitation services and nutritional therapy in a safe, collaborative and consistent manner: patients in pain are identified and managed; alleviation is started and adjusted according to need and response; the scope of rehabilitation matches the healthcare services the hospital has defined; rehabilitation is planned with the people who will deliver it; every admitted patient is screened for nutritional risk and those at risk are assessed; and a therapeutic diet is planned and provided with dietetics.

Pain that is not asked about, rehabilitation that is advertised but not staffed, and a kitchen that is clean while nobody has screened the patient for whether they can eat, are three different ways of failing the same patient. This document is the clinical process. It is not the kitchen's food-safety licence, and it is not the service directory; it uses both."""

SCOPE = """This policy applies to every clinical setting of {{HOSPITAL_NAME}} in which a patient may be in pain, may need rehabilitation, or is admitted and therefore must be screened for nutritional risk: in-patient wards, day-care, the emergency area insofar as pain is managed there, out-patient encounters where pain or rehabilitation is part of the defined service, intensive or high-dependency areas where they exist, and the dietetics function. It binds the clinicians who assess pain and prescribe alleviation, the nurses who reassess and titrate within the prescribed plan, the rehabilitation professionals where those services exist, the staff who screen for nutritional risk, and the dietetics staff who plan a therapeutic diet.

It covers: effective management of patients in pain; initiation and titration of pain-alleviation measures or medications according to need and response; a rehabilitation scope that is at a minimum commensurate with the services the organisation provides; collaborative planning of rehabilitation; screening of admitted patients for nutritional risk and assessment of those found at risk; and collaborative planning and provision of the therapeutic diet.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- The written definition of healthcare services, including whether rehabilitation is a defined service, which disciplines it includes, and the department scope of any physiotherapy, occupational therapy, speech therapy or similar service, is governed by the definition-and-display policy of {{HOSPITAL_NAME}} (AAC.1). COP.13.c requires that the rehabilitation scope in this document match that definition. This policy does not rewrite the service directory. If rehabilitation is not a defined service, this document records that fact and does not hold out a rehabilitation programme.
- Kitchen hygiene, the food-safety licence, food-handler health, temperature control of cooked and held food, and pest control of the kitchen are governed by the support-services infection-control policy of {{HOSPITAL_NAME}} (HIC.3, approved). This policy owns nutritional-risk screening, nutritional assessment of those at risk, and the therapeutic-diet prescription planned with dietetics. It does not name the Food Safety and Standards Act, 2006, and it does not restate kitchen practice.
- Maternal nutrition as part of antenatal assessment is governed by the obstetric policy of {{HOSPITAL_NAME}} (COP.7). Nutritional, growth, developmental and immunisation assessment of children is governed by the paediatric policy of {{HOSPITAL_NAME}} (COP.8). This policy owns hospital-wide nutritional-risk screening of admitted patients and the therapeutic diet. An antenatal nutrition note is not this screening; a paediatric growth chart is not this screening. Both may run on the same patient when a pregnant woman or a child is admitted; they are not substitutes.
- Analgesics, as medications, are governed by the medication policies of {{HOSPITAL_NAME}} (MOM, not yet drafted). This policy owns pain assessment, the decision to alleviate, and titration according to need and response. MOM owns prescribing, dispensing, administration records and storage of the drug. A pain score is not a prescription; a prescription is not a pain assessment.
- Initial assessment and the care plan are governed by the assessment policy of {{HOSPITAL_NAME}} (AAC.3). Pain, rehabilitation need and nutritional risk may be collected there. This policy owns the programmes that manage them.
- Falls, pressure-ulcer and thrombosis programmes, including mobilisation as a thrombosis or pressure-ulcer measure, are governed by the higher-risk-patient policy of {{HOSPITAL_NAME}} (COP.12). Mobilisation that is a rehabilitation plan is planned under this document and coordinated with that one; neither rewrites the other.
- Standard precautions during rehabilitation therapy (contact with non-intact skin, shared equipment) are governed by the infection-prevention-and-control-practices policy of {{HOSPITAL_NAME}} (HIC.2). This policy does not rewrite PPE.
- The medical record itself is governed by the information-management policies of {{HOSPITAL_NAME}} (IMS, not yet drafted). This policy owns the pain, rehabilitation and nutrition content written into that record."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} manages patients in pain. Pain is asked about, recorded, and treated; it is not inferred from whether the patient complains loudly.

{{HOSPITAL_NAME}} initiates and titrates pain-alleviation measures or medications according to the patient's need and response.

The scope of rehabilitation services at {{HOSPITAL_NAME}} is commensurate with the healthcare services the hospital has defined. Whether rehabilitation is a defined service is the service-directory decision. This document matches it.

Where rehabilitation is provided, care-providers plan it collaboratively.

{{HOSPITAL_NAME}} screens every admitted patient for nutritional risk and assesses those found at risk.

The therapeutic diet is planned and provided collaboratively with dietetics. Kitchen food-safety practice remains the support-services infection-control policy."""

PROCEDURE_STEPS = [
"""1. Patients in pain are effectively managed

Patients in pain are effectively managed. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask how the hospital knows a patient is in pain and what is done. The answer must be a method used on yesterday's admissions — a recorded assessment and a recorded response — not a statement that pain is treated when patients ask.

Effective management begins with finding the pain. Every in-patient, and every other patient in a setting this hospital has included, is asked about pain using [Hospital to define — the pain-assessment method used, including the scale or description method, and in which settings it is applied]. This document does not mandate a named scale, a numeric cut-off at which treatment must start, or a frequency in minutes. Tripathi and Kumar (2014) — chapter reference 56 — record that intensity scales are tools with limits; the hospital chooses a method staff can actually use, including for patients who cannot self-report (behavioural observation, or a method for children if children are in the service directory). Chou and colleagues (2016) — chapter reference 9 — inform post-operative pain as a clinical practice area; they are not imported as a mandated protocol or a required drug list. A Japanese chronic-pain guideline (chapter reference 11) is a chapter reference of this standard and is not adopted here as the hospital's chronic-pain protocol unless the hospital so chooses.

The assessment is recorded against the unique identification number, with the time. A blank pain field is an incomplete assessment, not evidence of no pain. Reassessment after a measure is given is part of management and is owned with titration at step 2; this step owns that pain is found and that a plan to alleviate it exists.

The plan is written: pharmacological, non-pharmacological, or both. Non-pharmacological measures this hospital uses are [Hospital to define — the non-pharmacological pain measures used]. Pharmacological measures are prescribed under the medication policies. This step owns that a patient in pain has a plan; MOM owns the drug.

Why this is a programme rather than "give an injection if they ask": patients who are stoic, who do not speak the language of the ward, who are children, who have been told to expect pain, or who cannot speak, will not ask in the way a policy that waits for a complaint requires. Unasked-about pain is untreated pain. The common error is a printed scale in the file and a ward that records "0" for every patient because the field is mandatory, without asking. A recorded zero that was not asked is a false record, and it is how unmanaged pain looks like managed pain.

The named person who keeps the pain-assessment method current is [Hospital to define — who keeps the pain-assessment method current]. Settings in which pain is assessed (wards, day-care, emergency, out-patient) are part of the method at the first placeholder in this step.

This step does not write an analgesic formulary and does not set a score at which an opioid is required.""",

"""2. Titration according to need and response

Pain-alleviation measures or medications are initiated and titrated according to the patient's need and response.

Initiation follows the plan at step 1. Titration means the measure is increased, reduced, changed or stopped according to the recorded response, not according to a standing dose that is never looked at again.

Need and response are recorded using the same assessment method as step 1, at [Hospital to define — when pain is reassessed after a measure is given, and when the plan is reviewed]. This document does not mandate a number of minutes. A measure given with no recorded response is not titration.

Who may titrate within a prescribed range, and when the treating clinician must be called, is [Hospital to define — who may titrate within a prescribed range, and when the treating clinician is called]. Administration of a medicine remains the medication policies. This step owns the clinical loop: assess, give, reassess, adjust.

A patient whose pain is not responding is not left on the same plan by default. The reason for a change, or for holding the plan, is recorded.""",

"""3. Rehabilitation scope commensurate with the services of {{HOSPITAL_NAME}}

Scope of rehabilitation services at a minimum is commensurate to the services provided by the organisation. This step is the documented-evidence anchor of a requirement the standard asterisks — COP.13.c was confirmed asterisked on the 2026-08-17 re-run, including the 2026-08-10 audit flip. An assessor will ask what rehabilitation this hospital provides and whether that matches what it holds out. The answer must be the same answer as the service directory.

The test is alignment with the current service directory and the department scopes of services, maintained under the definition-and-display policy of {{HOSPITAL_NAME}}. Rehabilitation here means the therapies the hospital has defined as a healthcare service — typically physiotherapy, and any occupational therapy, speech and language therapy, or other rehabilitation discipline the directory names. It does not mean "the nurse helped the patient sit up", which may be good nursing and is not a rehabilitation service for this OE.

Whether {{HOSPITAL_NAME}} provides rehabilitation as a defined healthcare service is [Hospital to define — whether rehabilitation is a defined healthcare service of this hospital, and which disciplines it includes]. That decision must match the directory. Two honest states exist:

- Rehabilitation is a defined service. Then this step's scope lists those disciplines, the patient groups they accept, the hours they are available, and the point at which a patient is referred elsewhere. The department scope of each rehabilitation discipline is authored under AAC.1; this step uses it and does not rewrite it. Staffing and equipment behind that scope are the AAC.1.b resourcing of a defined service; this step requires that the COP.13 scope does not claim a discipline the directory does not resource. Where rehabilitation is provided, the Rights of Persons with Disabilities Act, 2016 informs that persons with disability are not excluded from a service the hospital holds out, and that accessibility of the rehabilitation area is a legal concern of that Act; this document does not invent a building-standard catalogue (facility policies own the fabric) and does not quote section numbers.
- Rehabilitation is not a defined service. Then this step records that fact. {{HOSPITAL_NAME}} does not display, advertise or verbally hold out physiotherapy or other rehabilitation it does not provide. A patient who needs rehabilitation is referred using the referral route the relevant department scope already names under AAC.1. Steps 4's collaborative-plan rules do not operate as a rehabilitation-service process; they do not create a service the directory declined.

The reason commensurate is the safety word: a hospital that lists "physiotherapy" on the board and has a visiting therapist on Tuesdays only, without saying so, is holding out a service it cannot deliver on Wednesday. AAC.1 already forbids that as a directory-and-display problem. This step forbids it as a care problem — the post-operative patient whose plan assumes daily therapy that does not exist. The common error is a copied rehabilitation SOP describing a department the SHCO does not have, sitting next to a directory that never named it. Specificity is the test: a reader should be able to tell from this scope whether this hospital has a rehabilitation service, and which.

The written rehabilitation scope (or the recorded statement that there is none), and where it is held, are [Hospital to define — the written rehabilitation scope or the recorded statement that rehabilitation is not a defined service, and where that document is held].

This step does not write AAC.1's four-way alignment check. It requires that the COP.13 scope and the directory do not disagree.""",

"""4. Collaborative rehabilitation planning

Care providers collaboratively plan rehabilitation services.

This step operates where rehabilitation is a defined service under step 3. If it is not, this step is recorded as not operating, and no collaborative rehabilitation plan is invented to imply a service.

Where it operates, the plan is made with the treating clinician, the rehabilitation professional, nursing, and the patient or family as far as the patient can take part. The plan states the goal, the therapy, the frequency this hospital can actually deliver, and the review. How the plan is recorded is [Hospital to define — how a collaborative rehabilitation plan is recorded].

A plan written by a therapist alone, or a doctor's order "physio" with no goal and no therapist named, is not collaborative planning.

Internal referral into rehabilitation uses the information-sharing method of the continuity policy of {{HOSPITAL_NAME}} (AAC.7) for the referral; this step owns the rehabilitation plan that follows.""",

"""5. Nutritional-risk screening of admitted patients, and assessment of those at risk

Patients admitted to the organisation are screened for nutritional risk, and assessment is done for patients found at risk during nutritional screening. This step is the documented-evidence anchor of that asterisked requirement. An assessor will ask how the hospital finds the admitted patient who is not eating, who has lost weight, or who cannot swallow. The answer must be a screen completed on yesterday's admissions and an assessment on those the screen flagged, not a kitchen that is well run.

Screening is a short, defined method applied to every admission. The method is [Hospital to define — the nutritional-risk screening method used for admitted patients, who performs it, and by when after admission it is completed]. This document does not mandate a named tool or a numeric cut-off. Chapter references 35 (National Council on Aging malnutrition screening tools) and 59 (Queensland comparison of validated tools) and McClave and colleagues (2016) — chapter reference 29 — inform that screening and, for those at risk, assessment are different acts, and that a tool is chosen rather than invented in the moment. They are not imported as a required instrument.

A screen is not an assessment. The screen flags risk. Assessment of those flagged is performed by [Hospital to define — who performs nutritional assessment of patients screened at risk], and is recorded: intake, weight or the hospital's chosen nutritional findings, swallowing concern if present, and the problem the therapeutic diet at step 6 must address. A flagged patient with no assessment is an incomplete process. A patient screened as not at risk is not given a full assessment by this OE; they remain on the ordinary diet unless the treating clinician decides otherwise.

Why screening has to be every admission, not "when we notice": the patient who looks well, who is elderly and polite, who is post-operative and drowsy, is the one nobody notices until the wound fails or the fall happens. McClave and colleagues treat nutrition therapy in the hospitalised adult as a clinical process, not a catering preference. The common error is to treat a filled meal-order slip as a screen, or to treat HIC.3's kitchen licence as proof that patients are nourished. A safe kitchen can still serve a full diet to a person who cannot swallow it. This step finds that person. HIC.3 keeps the kitchen from poisoning them.

Obstetric antenatal nutrition (COP.7) and paediatric growth and nutrition assessment (COP.8) are not this screen. When a pregnant woman or a child is admitted, this admission screen still runs; those other assessments run under their own documents and are not ticked off by this screen.

The screen and the at-risk assessment are recorded against the unique identification number. The forms or fields used are [Hospital to define — where nutritional-risk screening and at-risk assessment are recorded].""",

"""6. Therapeutic diet planned and provided collaboratively

The therapeutic diet is planned and provided collaboratively.

Collaboration means the treating clinician, dietetics (or the role this hospital uses for diet planning), and nursing agree the diet for a patient who needs one — including patients assessed at risk at step 5, and any other patient the clinician places on a therapeutic diet. The diet is recorded as a prescription of a diet type, not only as a kitchen tick. How the diet is planned and how the kitchen is told is [Hospital to define — how the therapeutic diet is planned collaboratively and how it is communicated to the kitchen].

Dietetics plans; the kitchen prepares under the support-services infection-control policy. This step does not restate food-handler health, holding temperatures, or the food-safety licence. Those remain HIC.3. This step owns that the patient who needs a texture-modified, diabetic, renal, or other therapeutic diet is identified and that the diet reaching the bedside is the one planned.

A diet changed at the bedside by a relative, or a "soft diet" shouted down a corridor, is not a collaborative plan. If the patient refuses the planned diet, that refusal is recorded and the plan is reviewed rather than silently replaced.

Provision is confirmed: the planned diet was served. How that confirmation is made is [Hospital to define — how provision of the planned therapeutic diet is confirmed].""",

"""7. Records, review and the order of operations

Every pain assessment and plan, every titration record, the rehabilitation scope or recorded absence, every collaborative rehabilitation plan where the service exists, every admission nutritional-risk screen, every at-risk nutritional assessment, and every therapeutic-diet plan is recorded against the unique identification number where a patient is involved, and is retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for pain, rehabilitation and nutrition records] for: pain asked about rather than assumed; titration that shows a recorded response; a rehabilitation scope that matches the service directory, or a recorded absence that matches a directory without rehabilitation; nutritional-risk screens on admissions rather than meal slips treated as screens; at-risk patients assessed; and therapeutic diets planned with dietetics rather than only with the kitchen.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when the service directory adds or removes rehabilitation, when unmanaged pain, an unscreened admission, or a therapeutic diet that did not reach the patient exposes a gap, or when the definition-and-display, kitchen, obstetric, paediatric, medication or assessment policies that this document hands work to are revised.""",
]

RESPONSIBILITY = """The head of the institution is accountable for {{HOSPITAL_NAME}} managing pain, for a rehabilitation scope that matches the defined services, and for nutritional-risk screening of admitted patients.

Treating clinicians assess pain, prescribe alleviation, indicate rehabilitation where the service exists, and indicate a therapeutic diet.

Nurses apply the pain-assessment method, reassess after measures, screen admitted patients for nutritional risk, and confirm that the planned diet was served.

Rehabilitation professionals, where the service exists, participate in collaborative plans and deliver the therapy the directory resources.

Dietetics (or the role named for diet planning) assesses patients screened at risk and plans the therapeutic diet with the treating clinician. Kitchen staff prepare under HIC.3.

The person who keeps the pain-assessment method current at step 1, and the person who holds the rehabilitation scope at step 3, keep those documents aligned with practice and with the service directory.

The quality or accreditation coordinator audits the records at step 7 and reports findings to the head of the institution.

All staff are expected to treat unasked-about pain, a rehabilitation service held out that the directory does not resource, and an admission without a nutritional-risk screen, as defects, and to report them."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.13.
- Rights of Persons with Disabilities Act, 2016, insofar as rehabilitation services are a defined healthcare service of this hospital.
- National Medical Commission Act, 2019, insofar as registered medical practitioners must provide pain management and nutritional care consistent with professional practice.
- Chou, R., et al. (2016). Management of Postoperative Pain: A Clinical Practice Guideline From the American Pain Society, the American Society of Regional Anesthesia and Pain Medicine, and the American Society of Anesthesiologists. J Pain, 17(2), 131-157 — chapter reference 9; informs post-operative pain as a clinical area; not a mandated protocol.
- Clinical practice Guideline for Chronic Pain (2018), Japanese Society for the Study of Pain — chapter reference 11; chapter reference only, not adopted as this hospital's protocol unless the hospital so chooses.
- Tripathi, L., and Kumar, P. (2014). Challenges in pain assessment: Pain intensity scales. Indian Journal of Pain, 28(2), 61 — chapter reference 56.
- McClave, S. A., et al. (2016). ACG Clinical Guideline: Nutrition Therapy in the Adult Hospitalized Patient. American Journal of Gastroenterology, 111(3), 315-334 — chapter reference 29; informs screening versus assessment; not a mandated tool.
- National Council on Aging (2017). Malnutrition Screening and Assessment Tools — chapter reference 35.
- Validated Malnutrition Screening and Assessment Tools: Comparison Guide (2017), Queensland Health — chapter reference 59.
- Internal documents of {{HOSPITAL_NAME}}: the service directory and department scopes of services; the pain-assessment method; the rehabilitation scope or recorded absence; collaborative rehabilitation plans; the nutritional-risk screening method and at-risk assessments; therapeutic-diet plans; the assessment policy; the support-services infection-control policy; the obstetric and paediatric policies; the higher-risk-patient policy; the medication policies; the continuity and internal-transfer policy; and the information-management policies."""

DISTRIBUTION = """Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every in-patient ward; day-care; the emergency area; dietetics; the kitchen (for the therapeutic-diet communication method only, not as a food-safety manual); rehabilitation areas where they exist; nursing administration; and every head of department whose staff assess pain or screen nutrition.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The pain-assessment method, the rehabilitation scope or recorded absence, and the nutritional-risk screening method — the working documents this policy requires — are held on the wards that use them.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

NMC — National Medical Commission
RPWD — Rights of Persons with Disabilities Act, 2016

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

STATUTE_CLAUSE = (
    "the Rights of Persons with Disabilities Act, 2016, insofar as rehabilitation "
    "services are a defined healthcare service of this hospital, and the National "
    "Medical Commission Act, 2019 insofar as registered medical practitioners must "
    "provide pain management and nutritional care consistent with professional practice"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "COP.13.a",
        "requirement": "Patients in pain are effectively managed",
        "steps": "Steps 1, 2, 7",
        "evidence": "The written pain-assessment method, including the scale or description method and the settings in which it is applied, with no mandated numeric cut-off; sample records against the unique identification number showing pain asked about and recorded, including for patients who cannot self-report where such a method is defined, rather than a blank field or a default zero that was not asked; a written plan for the patient in pain (pharmacological, non-pharmacological, or both) with non-pharmacological measures as this hospital defined them and pharmacological measures prescribed under the medication policies; the named person who keeps the method current; induction or briefing records showing ward staff use the method rather than waiting for a loud complaint; the audit sample at step 7 of pain asked about rather than assumed",
        "responsible": "Treating clinicians plan alleviation; nurses apply the assessment method; named person at step 1 keeps the method current; MOM owns the analgesic as a medication; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "COP.13.b",
        "requirement": "Pain alleviation measures or medications are initiated and titrated according to the patient's need and response.",
        "steps": "Steps 2, 7",
        "evidence": "Records of initiation and of reassessment after a measure using the same method as step 1; who may titrate within a prescribed range and when the clinician is called; recorded changes when pain does not respond; administration remaining under the medication policies",
        "responsible": "Nurses reassess and titrate within the prescribed range; treating clinicians review non-response; MOM owns administration records",
    },
    {
        "oe_code": "COP.13.c",
        "requirement": "Scope of rehabilitation services at a minimum is commensurate to the services provided by the organization.",
        "steps": "Steps 3, 7",
        "evidence": "The written hospital decision whether rehabilitation is a defined healthcare service and which disciplines it includes, matching the service directory and department scopes maintained under the definition-and-display policy rather than a copied SOP for a department the hospital does not have; if rehabilitation is provided, the COP.13 scope listing disciplines, patient groups, hours and referral point, using the AAC.1 department scope and not rewriting it, and not claiming a discipline the directory does not resource; if rehabilitation is not provided, the recorded fact, evidence that physiotherapy or other rehabilitation is not displayed or held out, and the referral route used; the location of that scope or recorded absence; the Rights of Persons with Disabilities Act, 2016 cited insofar as the service exists, without a building-catalogue or section-number claim; the audit sample at step 7 of scope matching the directory or absence matching a directory without rehabilitation",
        "responsible": "Head of the institution for directory alignment; person who holds the rehabilitation scope at step 3; heads of rehabilitation departments where they exist author the AAC.1 scope this step uses; quality or accreditation coordinator audits the match",
    },
    {
        "oe_code": "COP.13.d",
        "requirement": "Care providers collaboratively plan rehabilitation services.",
        "steps": "Steps 4, 7",
        "evidence": "Where rehabilitation is a defined service, sample collaborative plans stating goal, therapy, deliverable frequency and review, made with clinician, therapist, nursing and patient or family; where it is not a defined service, the recorded statement that this step does not operate; internal referral using AAC.7 for the referral method",
        "responsible": "Rehabilitation professionals and treating clinicians plan together where the service exists; nursing participates; AAC.7 owns referral method",
    },
    {
        "oe_code": "COP.13.e",
        "requirement": "Patients admitted to the organization are screened for nutritional risk, and assessment is done for patients found at risk during nutritional screening.",
        "steps": "Steps 5, 7",
        "evidence": "The written nutritional-risk screening method for every admitted patient, who performs it, and by when after admission it is completed, with no mandated named tool or numeric cut-off; sample admission records against the unique identification number showing a completed screen rather than a meal-order slip treated as a screen; the named role that performs nutritional assessment of patients screened at risk, and sample assessments recording intake, the hospital's chosen nutritional findings, swallowing concern if present, and the problem the therapeutic diet must address; records showing a flagged patient was assessed rather than left flagged; the distinction recorded that obstetric antenatal nutrition and paediatric growth assessment are not this screen and are not ticked off by it; the distinction recorded that HIC.3 kitchen practice is not this screen; the location of the screen and at-risk assessment records; the audit sample at step 7 of screens on admissions and of at-risk patients assessed",
        "responsible": "Nurses or the named role screen every admission; dietetics or the named role assess those at risk; treating clinicians act on the assessment; kitchen does not own the screen; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "COP.13.f",
        "requirement": "The therapeutic diet is planned and provided collaboratively.",
        "steps": "Steps 6, 7",
        "evidence": "Therapeutic-diet plans agreed by clinician, dietetics and nursing; communication to the kitchen; confirmation that the planned diet was served; kitchen hygiene left to HIC.3; refusals recorded and reviewed rather than silently replaced",
        "responsible": "Dietetics plans with the treating clinician; nursing confirms provision; kitchen prepares under HIC.3",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. COP.13 standard text and all six OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 2 Care of Patients, printed pages 68-69 (PDF page index 74-75). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: COP.13.a Commitment, COP.13.b Commitment, COP.13.c Commitment, COP.13.d Commitment, COP.13.e Commitment, COP.13.f Commitment.
   THREE OEs CARRY THE ASTERISK -- COP.13.a, COP.13.c and COP.13.e. COP.13.c was among the 14 mismatches of the 2026-08-10 audit and was flipped to asterisked; the 2026-08-17 asterisk_extract.py re-run confirms the asterisk on c (raw text ends "*."). Mapping requirement for c is the PDF OE text without the asterisk character: "Scope of rehabilitation services at a minimum is commensurate to the services provided by the organization."
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the COP.13 pages read directly, and the committed asterisk file.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. THREE OF SIX OEs ARE TIER 1. Tier 1: COP.13.a, COP.13.c, COP.13.e -- steps 1, 3 and 5 carry the reasoning (why pain must be asked about; why commensurate with AAC.1 is the safety word; why a kitchen licence is not a nutrition screen). Tier 2: COP.13.b, d, f -- requirement and method without extended rationale. Reviewer to note the shallower treatment of b, d and f is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of COP.13.a/c/e against all six approved HIC masters and the AAC.1-AAC.8 drafts. Search terms: pain, rehabilitation, physiotherapy, nutrition, diet, kitchen, FSSAI, screening.
   AAC.1: service directory and department scopes, including whether rehabilitation exists. This draft's Scope and step 3 require the COP.13 rehab scope to match that definition and do not rewrite the directory. Not a contradiction.
   HIC.3 (approved): kitchen, FSSAI licence, food-handler health, temperatures. This draft's Scope and steps 5-6 own screening, assessment and therapeutic-diet prescription and deliberately do not name the Food Safety and Standards Act. Not added to the reconciliation list.
   HIC.2: standard precautions during therapy. Pointer only.
   AAC.3: assessment may collect pain, rehab need, nutritional facts. This document owns the programmes.
   AAC.7: internal referral method into rehabilitation. Pointer at step 4.
   COP.7.c (forward): maternal nutrition in antenatal assessment. Division stated: not this admission screen.
   COP.8.e (forward): paediatric nutritional/growth/dev/immunisation assessment. Division stated.
   COP.12 (sibling): mobilisation as falls/PU/VTE measure vs rehab plan. Coordinated, not rewritten.
   MOM (forward): analgesic as medication. Division stated.
3. FORWARD REFERENCES: MOM analgesics; PRE if consent to therapy is needed; IMS record; COP.7, COP.8, COP.12; FMS accessibility fabric under RPWD. Each is a deliberate boundary.
4. T2 QUICK CHECK: COP.13.b titration vs MOM administration -- flagged, this owns the clinical loop, MOM owns the drug. COP.13.d collaborative plan vs AAC.7 referral -- flagged. COP.13.f therapeutic diet vs HIC.3 kitchen -- flagged, HIC.3 owns hygiene, this owns the prescription. None is a contradiction with an approved document.

STATUTORY AND EXTERNAL FACTS
5. Rights of Persons with Disabilities Act, 2016 -- cited insofar as rehabilitation is a defined service (preferred statute because rehab is in this standard's scope as an OE). No section number. No building-catalogue. If the hospital does not provide rehabilitation, the insofar-as clause does not attach a duty this hospital does not have, and NMC remains for pain and nutrition.
6. National Medical Commission Act, 2019 -- professional-practice obligations for pain management and nutritional care by registered medical practitioners. No section number.
7. Food Safety and Standards Act, 2006 -- NOT named in P2, References, or body. HIC.3 owns kitchen/FSSAI. Deliberate.
8. Bio-Medical Waste Management Rules, 2016 -- NOT named. Clinical Establishments Act, 2010 -- NOT named, not defaulted.
9. Chou 2016, Tripathi 2014, JSSP 2018 -- chapter refs 9, 56, 11; no mandated scale, cut-off, or chronic-pain protocol.
10. McClave 2016, NCOA 2017, Queensland 2017 -- chapter refs 29, 35, 59; screening and assessment are different acts; no mandated tool.
11. NO NUMBERS ARE STATED as requirements -- no pain-score cut-offs, no reassessment minutes, no screening-hour TAT, no staffing ratios. Every such value is [Hospital to define].

EDITORIAL POSITIONS TAKEN
12. Step 1's rule that a recorded zero that was not asked is a false record is an editorial position consistent with the asterisk on effective management.
13. Step 3's two honest states (rehab is a defined service / it is not) and the refusal to let a copied SOP create a service are editorial positions required by alignment with AAC.1.
14. Step 5's rule that a meal slip or a kitchen licence is not a nutritional-risk screen is an editorial position required by the overlap with HIC.3.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
15. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the Rights of Persons with Disabilities Act, 2016 (insofar as rehabilitation is a defined service) and the National Medical Commission Act, 2019 (pain and nutrition professional obligations) -- the statutes this document's References actually cite. It does NOT name FSS Act 2006, BMW Rules 2016, or CEA 2010.

DELIBERATELY NOT INCLUDED
- Kitchen hygiene, FSSAI licence, food-handler health -- HIC.3.
- Service directory authorship -- AAC.1.
- Analgesic storage and administration method -- MOM.
- Antenatal maternal nutrition -- COP.7.
- Paediatric growth/nutrition/immunisation assessment -- COP.8.
- A mandated pain-score cut-off or malnutrition-tool name.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 18 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 16 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 18; a search for "Hospital to define" without brackets finds all 18, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: the pain-assessment method and settings; non-pharmacological pain measures; who keeps the pain-assessment method current; when pain is reassessed after a measure; who may titrate and when the clinician is called; whether rehabilitation is a defined service and which disciplines; the written rehabilitation scope or recorded absence and where it is held; how a collaborative rehabilitation plan is recorded; the nutritional-risk screening method, who performs it and by when; who performs at-risk nutritional assessment; where screening and assessment are recorded; how the therapeutic diet is planned and communicated to the kitchen; how provision is confirmed; the audit interval; the review interval for this policy; the intranet or folder location; and any additional local abbreviation."""

SQL_HEADER = """-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 2, printed pages 68-69
-- (PDF page index 74-75). Levels: a Commitment, b Commitment, c Commitment,
-- d Commitment, e Commitment, f Commitment.
-- THREE OEs CARRY THE ASTERISK -- COP.13.a, COP.13.c, COP.13.e.
-- COP.13.c asterisk confirmed 2026-08-17 (flipped in the 2026-08-10 audit).
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
        json_name="cop13_draft.json",
        sql_name="cop13_insert.sql",
    )
