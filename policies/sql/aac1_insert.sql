-- AAC.1 master policy -- DRAFT for review. Do NOT set status = 'approved' here;
-- approval is a separate manual step after fact-checking.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 1, printed page 50
-- (PDF page index 56). Levels: a, b, c, d all Commitment.
-- ONE OE CARRIES THE ASTERISK -- AAC.1.c, the department scope of services. It is the
-- documented-evidence anchor and the only Tier 1 element under the two-tier standing rule.
--
-- version and revision_history are included from the start (migration 20260812);
-- HIC.1-6 predate that migration and were backfilled instead.
--
-- The five optional sections are deliberately not populated, matching HIC.1-6.

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
  'AAC.1',
  'AAC',
  array['AAC.1.a', 'AAC.1.b', 'AAC.1.c', 'AAC.1.d'],
  $q$Definition and Display of Healthcare Services$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} decides which healthcare services it provides, satisfies itself that each of them can actually be delivered, writes down what every department does and does not do, and tells the public.

A hospital's defined services are the promise on which everything else rests. A patient chooses this hospital, or is brought to it unconscious, on the strength of what it says it can do. Every later decision — whether to register, whether to admit, whether to treat or to stabilise and transfer — leans on a boundary that must already exist in writing before the patient arrives. Where that boundary is undefined, each of those decisions is improvised, and the patient most at risk from the improvisation is the one the hospital was never equipped to care for.

This document therefore governs four things: the written definition of the services of {{HOSPITAL_NAME}} and its grounding in the needs of the community served; the resourcing behind every defined service; the scope of services of each department, including the boundary of what it does not do; and the display through which the public is told.$q$,
  $q$This policy applies to the whole of {{HOSPITAL_NAME}}: every clinical department and specialty, every diagnostic service, and every support function whose availability the defined services depend on. It binds the head of the institution, every head of department, the staff who maintain the service display and other public-facing material, and every member of staff who answers a patient's question about what this hospital does.

It covers the hospital-level definition of services, the department-level scope of services documents, the community-needs basis on which services are chosen, and every medium through which the services are held out to the public — signage, boards, printed material and the hospital's online presence.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- This policy defines what the hospital does. The registration and admission of an individual patient against that definition — including the decision not to admit a patient whose needs fall outside it — is governed by the registration and admission policy of {{HOSPITAL_NAME}}.
- The verification of staff qualifications, registrations and credentials is governed by the human resource policies of {{HOSPITAL_NAME}}. This policy relies on that verification when it requires each defined service to be backed by suitably qualified personnel; it does not restate the method.
- The display of patient rights and responsibilities, of tariffs, and of statutory notices is governed by the patient rights policies of {{HOSPITAL_NAME}} and by the statutes that require them. This policy owns the display of the services; where the two share a wall, each is maintained under its own document.
- Isolation and infection control signage is governed by the infection control policies of {{HOSPITAL_NAME}} and has nothing to do with the display governed here.$q$,
  $q${{HOSPITAL_NAME}} defines its healthcare services in writing, approves the definition at the level of the head of the institution, keeps it consistent with the registrations and licences the hospital holds, and grounds it in an assessment of the needs of the community it serves.

{{HOSPITAL_NAME}} holds out no service it cannot deliver. A service enters the definition only when the personnel, the diagnostics and the treatment capability behind it exist, and it leaves the definition — and the display — when they cease to. The display is treated as a promise to the public, and a promise the hospital cannot keep is removed rather than explained.

{{HOSPITAL_NAME}} requires every department to carry a written scope of services stating what it does and, with equal precision, what it does not do. The boundary is treated as the safety content of the document: the patients a hospital is not equipped for are protected by the exclusions, not by the list of capabilities.

{{HOSPITAL_NAME}} displays its defined services prominently, in the languages the community it serves reads, keeps the display identical in substance to the written definition, and corrects it at once when a service is suspended or withdrawn.

{{HOSPITAL_NAME}} changes its services in a fixed order — resource first, then define, then scope, then display — so that no patient ever acts on a promise that ran ahead of the capability behind it.

{{HOSPITAL_NAME}} expects every member of staff to know the scope of their own department, and treats directing a patient to another provider, when this hospital cannot care for them, as correct practice and never as lost business.$q$,
  array[
    $s$1. Defining the healthcare services of {{HOSPITAL_NAME}}

{{HOSPITAL_NAME}} maintains a written definition of the healthcare services it provides — the service directory. The directory lists every clinical specialty and service offered, states for each whether it is available on an out-patient basis, an in-patient basis, an emergency basis, or a combination of these, and names the diagnostic and support services that stand behind them.

The directory is approved by the head of the institution, is dated and version-controlled, and is consistent with the registrations and licences {{HOSPITAL_NAME}} holds — a service that the hospital's registration or licence does not permit does not appear in it.

The services defined are chosen against the needs of the community {{HOSPITAL_NAME}} serves, and the basis of the choice is recorded rather than assumed: the population of the catchment area, its broad disease profile, the services already available from other providers nearby, and the pattern of demand and referral seen at this hospital. The community needs assessment is held at [Hospital to define — where the community needs assessment is held and when it was last performed], and is revisited when the directory is reviewed.

The directory is reviewed at [Hospital to define — review interval for the service directory], and immediately upon any service being added, suspended or withdrawn under step 7.$s$,
    $s$2. Resourcing every defined service

A service appears in the directory only when {{HOSPITAL_NAME}} can deliver it. For each defined healthcare service, the hospital maintains:

- the diagnostic and treatment services the specialty requires, either within the hospital or under a documented arrangement the directory identifies;
- suitably qualified personnel — practitioners registered with the professional council governing their practice and holding the qualifications the role requires, verified under the human resource procedures of {{HOSPITAL_NAME}};
- out-patient consultation, in-patient care and emergency cover for the service, with the emergency arrangement stated in writing: resident cover, or an on-call roster with the expected response arrangement.

Where a clinician providing a service is visiting rather than full-time, the directory says so, and the arrangement for that service outside the visiting hours is stated. Where {{HOSPITAL_NAME}} intends a narrower offering — a specialty seen on an out-patient basis only, for example — the service is not held out as a full service: the directory and the display state the limitation, and the department's scope of services records where patients needing more than the hospital provides are referred.

The resourcing behind each service is confirmed at every review of the directory, against the current staffing and equipment rather than against what was true when the service was introduced.$s$,
    $s$3. The scope of services of each department — what it states

Every department of {{HOSPITAL_NAME}}, clinical and diagnostic alike, holds a written scope of services. This is the documented-evidence anchor of this standard — the document an assessor will ask for by name — and it is written so that a member of staff can act on it at the moment a question arises, not merely file it.

Each department's scope states:

- the services and procedures the department performs;
- the patient populations it accepts — the age groups it takes, and any category of patient it does not;
- the level of acuity it can manage, and the point beyond which a patient's needs exceed it;
- the hours during which each of its services is available, and the arrangement outside those hours — resident cover, on-call cover with the expected response, or not available;
- the services the department depends on to do its work — anaesthesia, laboratory, imaging, blood — and where each dependency is met from, so that the scope fails visibly if a dependency disappears;
- the conditions the department stabilises and refers rather than treats, and where it refers them;
- the person in charge of the department.

Each element is there because a decision leans on it. The populations and acuity limits are what the duty doctor consults when deciding whether the department can accept the patient in front of them. The hours and out-of-hours arrangement are what reception consults before telling a caller to come in. The dependency list is what makes a scope honest: a surgical service is only as available as its anaesthesia cover, and a scope that claims the service without naming the dependency claims more than the department controls. The stabilise-and-refer list is what turns a refusal into a plan.

The commonest defect in this document is genericness — a scope copied between departments, or downloaded, that describes a department the hospital does not have. The test applied at {{HOSPITAL_NAME}} is specificity: a reader who knows the hospital should be able to tell from the scope alone which department it describes, and a reader who knows the department should find nothing in the scope it does not actually do. Each department's scope is held at [Hospital to define — where each department's scope of services is held and how the set is indexed].$s$,
    $s$4. The scope of services — the boundary matters more than the list

The safety content of a scope of services is its negative half. A hospital is rarely harmed by declining a patient it could in fact have treated; it is harmed — and the patient is harmed — by accepting one it could not. The exclusions are therefore written with the same precision as the capabilities, and vagueness in an exclusion is treated as a defect in the document, because an exclusion that can be read two ways will be read the convenient way under pressure.

Exclusions are specific: the procedures the department does not perform, the ages below or above which it does not accept a patient, the conditions it does not manage beyond stabilisation, and the situations in which a patient is transferred out rather than admitted. For each exclusion that a patient may nonetheless present with, the scope names the response — stabilise and refer, and to where — so that the boundary always points somewhere rather than ending in a refusal.

The boundary is what the hospital's admission and emergency decisions lean on. The person deciding at the door whether {{HOSPITAL_NAME}} can care for a patient does not weigh the question from first principles at that moment; they apply a boundary that was set in advance, in writing, when there was time to set it honestly. That is the reason this document exists at department level rather than only hospital level: the boundary of a hospital is the sum of the boundaries of its departments, and a hospital-level list cannot say which department's limit a given patient is about to cross.

When a department's real capability moves — a specialist leaves, a machine fails, a dependency named in the scope becomes unavailable — the boundary has moved with it whether or not the paper is updated, and the paper is updated so that staff are applying the real boundary and not last year's. The route for that update is step 7, and the department head's duty to trigger it is stated there.$s$,
    $s$5. The scope of services — approval, alignment, review and communication

Authorship and approval. Each scope of services is authored by the head of the department it describes, because only the department knows its real boundary, and is approved by the head of the institution, because the scope commits hospital resources beyond the department — the dependencies at step 3 belong to other departments. Each scope is dated, version-controlled, and signed by both.

Alignment — the four-way check. A scope of services is one of four statements of the same facts, and the four are checked against each other rather than trusted separately:

- the service directory against the department scopes — every service in the directory maps to at least one department's scope, and nothing claimed in a scope is missing from the directory;
- the scopes against the registrations and licences of {{HOSPITAL_NAME}} — nothing in any scope exceeds what the hospital is registered or licensed to do;
- the scopes against reality — the personnel, equipment and dependencies each scope relies on exist today, not merely at the date of writing;
- the scopes against the display at step 6 — the public is being told what the scopes say, no more and no less.

The check is performed at every review, and whenever any one of the four changes. A mismatch found is corrected in whichever document is wrong, and the correction is recorded. The reason the check is structured this way: each of the four documents is maintained by different hands at different times, and unchecked they drift apart — the display is the slowest to change and the licences the easiest to forget, and an assessor reading all four will find a divergence the hospital has stopped seeing.

Review. Each scope is reviewed at [Hospital to define — review interval for department scopes of services], and immediately on any trigger event: a new service or procedure introduced, the arrival or departure of a specialist the scope depends on, equipment commissioned or withdrawn, a change to a registration or licence, or a change to any dependency named in the scope. The department head owns the trigger — the review does not wait for the calendar when the facts have already changed.

Communication. A scope that staff have not read protects no one. Each department's staff receive its scope at induction to the department; the current scope is available within the department; and reception, the front office and the emergency area hold the full set or a consolidated summary of all department scopes, because those are the points where a patient's first question — can this hospital treat this? — actually lands, and the person answering must answer from the document rather than from impression.$s$,
    $s$6. Displaying the services

The defined healthcare services of {{HOSPITAL_NAME}} are prominently displayed, so that a patient, a family or a referring practitioner can learn what this hospital does without having to ask.

The display is provided at minimum at the main entrance, at reception, and at the emergency entrance, and at [Hospital to define — any further display locations]. It is in the languages the community served reads — [Hospital to define — the languages of the display] — and is legible, maintained and lit.

The display states the services provided, the basis on which each is available — out-patient, in-patient, emergency — and identifies the services available round the clock. Where the hospital's printed material and online presence describe the services, they carry the same content as the display and are corrected on the same trigger.

The display matches the service directory exactly in substance: no service is displayed that is not defined and resourced, and no defined service is omitted. A displayed service the hospital cannot deliver is not a signage error; it is a promise the next patient will act on, and under the Consumer Protection Act a misleading representation of services besides.

Statutory display obligations that attach to particular services — the registration certificate and signage required where ultrasonography is performed, the display of registration and of rates where the clinical establishments legislation in force requires them — are honoured where they apply. They are governed by the statutes themselves and by the patient rights policies of {{HOSPITAL_NAME}}; they are noted here because they share the display space and are checked at the same time.

Responsibility for keeping every display current sits with [Hospital to define — the role responsible for the display], who corrects it within the timescale at step 7 whenever the directory changes.$s$,
    $s$7. Changing the services — the order of operations

A service is added in this order: resourced first, then entered in the service directory, then written into the owning department's scope, then displayed. The display is last deliberately — it is the promise, and the promise is made only after everything behind it exists.

A service is suspended or withdrawn in the reverse emphasis: the display, the online presence, reception and the emergency area are corrected and informed first and at once, because from the moment the capability is gone every minute of continued display is a false statement to the public; the directory and the scope are updated with the change and the referral arrangement for patients who need the service; and the community needs record at step 1 is annotated if the withdrawal is permanent.

A temporary suspension — a specialist on leave without cover, equipment awaiting repair — follows the same route with a stated expected duration, and is reviewed if it exceeds it. Staff at the points of first contact are told what to say and where patients are being referred meanwhile.

Every change, temporary or permanent, updates all four aligned documents at step 5 or records why one is unaffected. The change and its date are recorded, and the head of the institution is informed of every suspension and withdrawal.$s$
  ],
  $q$The head of the institution approves the service directory and every department scope of services, provides the personnel, equipment and arrangements that resourcing a defined service requires, is informed of every suspension and withdrawal, and is accountable for {{HOSPITAL_NAME}} holding out no service it cannot deliver.

Heads of departments author the scope of services of their own department, keep it true — including triggering the review at step 5 the moment the department's real capability changes rather than waiting for the calendar — communicate it to their staff, and answer for the boundary being applied in their department's daily decisions.

The person responsible for administration of {{HOSPITAL_NAME}} maintains the service directory, performs the four-way alignment check at step 5 and records its result, coordinates the change sequence at step 7, and holds the community needs assessment.

The human resource function verifies the registration and qualifications of the personnel behind every defined service under its own procedures, and informs the administration when a departure or lapse affects a defined service.

The role named at step 6 maintains every display and the public-facing material, and corrects them at once on any change to the directory.

Reception, the front office and the emergency area hold the current set of department scopes or the consolidated summary, and answer the public from it.

The quality or accreditation coordinator audits the currency of the directory, the scopes and the display against each other at the review interval, and reports findings to the head of the institution.

All staff are expected to know the scope of their own department, to direct a patient whose needs fall outside it along the referral route the scope names, and to report a display or directory statement they know to be no longer true.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Access, Assessment and Continuity of Care chapter, standard AAC.1.
- Clinical Establishments (Registration and Regulation) Act, 2010 and the rules under it, where adopted by the State — registration of the establishment, minimum standards, and the display of registration and of rates; or the corresponding State clinical establishments or nursing home registration law where the 2010 Act is not in force.
- The professional registration statutes behind "suitably qualified personnel": the National Medical Commission Act, 2019 and State Medical Council registration; the Indian Nursing Council Act, 1947 and State Nursing Council registration; and the corresponding councils for the other professions {{HOSPITAL_NAME}} employs.
- Consumer Protection Act, 2019 — the prohibition of misleading advertisement, which is what a displayed service the hospital cannot deliver amounts to.
- Statutes attaching registration, licensing or display conditions to specific services, applicable where {{HOSPITAL_NAME}} provides the service concerned: the Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994 for ultrasonography; Atomic Energy Regulatory Board licensing for diagnostic radiology; the Drugs and Cosmetics Act, 1940 for a blood centre or pharmacy; the Medical Termination of Pregnancy Act, 1971; and the Transplantation of Human Organs and Tissues Act, 1994.
- Internal documents of {{HOSPITAL_NAME}}: the registration and licence portfolio; the service directory and the department scope of services set maintained under this policy; the community needs assessment; the registration and admission policy; the human resource qualification verification records; and the patient rights display materials.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every head of department, clinical and diagnostic; reception and the front office; the emergency area; nursing administration; the human resource function; the role responsible for the display and public-facing material; and whoever maintains the hospital's online presence.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The service directory and the department scope of services set — the working documents this policy requires — are held additionally at reception, the front office and the emergency area, where the public's questions arrive.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO and OE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

AERB — Atomic Energy Regulatory Board
MTP — Medical Termination of Pregnancy
NMC — National Medical Commission
PC-PNDT — Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the Bio-Medical Waste Management Rules, 2016 and the Food Safety and Standards Act, 2006. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "AAC.1.a", "requirement": "The healthcare services provided are defined and are in consonance with the needs of the community", "steps": "Steps 1, 7", "evidence": "The service directory of {{HOSPITAL_NAME}}, approved by the head of the institution, dated and version-controlled, listing every service with its out-patient, in-patient and emergency availability; the community needs assessment with its date and the catchment, disease-profile, other-provider and demand information it relied on; the record of directory reviews at the stated interval and on every change; evidence of consistency between the directory and the hospital's registrations and licences", "responsible": "Head of the institution approves the directory; the administration maintains it and holds the community needs assessment; quality or accreditation coordinator audits the review cycle"}, {"oe_code": "AAC.1.b", "requirement": "Each defined healthcare service has diagnostic and treatment services with suitably qualified personnel providing out-patient, in-patient and emergency cover", "steps": "Steps 2, 7", "evidence": "Per defined service, the personnel behind it with their professional council registrations and qualification verification under the human resource procedures; the diagnostic and treatment arrangement for each service, in-house or documented external; the written emergency cover arrangement per service — resident cover or the on-call roster with its response arrangement; visiting-consultant terms and the stated arrangement outside visiting hours; the recorded limitation and referral route for any service offered on a narrower basis; the resourcing confirmation made at each directory review", "responsible": "Head of the institution for resourcing; heads of departments for rosters and cover in their service; human resource function for registration and qualification verification"}, {"oe_code": "AAC.1.c", "requirement": "The scope of healthcare services of each department is defined", "steps": "Steps 3-5, 7", "evidence": "The written scope of services of every department, clinical and diagnostic, each authored by the head of that department and approved by the head of the institution, dated, version-controlled and signed by both; each scope stating the services and procedures performed, the patient populations accepted with the ages and categories not accepted, the acuity manageable and the point beyond it, the hours of each service and the out-of-hours arrangement, the dependencies relied on and where each is met from, the conditions stabilised and referred with the referral destination, and the person in charge; the specific exclusions written to the precision step 4 requires, each pointing to a response rather than ending in a refusal; the four-way alignment check record — directory against scopes, scopes against registrations and licences, scopes against current personnel and equipment, scopes against the display — with mismatches found, the document corrected and the correction recorded; review records at the stated interval and on every trigger event, showing the trigger honoured when a specialist left, equipment changed or a dependency moved; induction records showing each department's staff received its scope; the current scope available within the department; and the full set or consolidated summary held at reception, the front office and the emergency area", "responsible": "Heads of departments author and keep current the scope of their own department and trigger its review the moment capability changes; head of the institution approves every scope; the administration performs and records the four-way alignment check; reception, front office and emergency hold the set and answer the public from it; quality or accreditation coordinator audits currency at the review interval"}, {"oe_code": "AAC.1.d", "requirement": "The defined healthcare services are prominently displayed", "steps": "Steps 6, 7", "evidence": "The display itself at the main entrance, reception and the emergency entrance and at any further stated location, in the stated languages, legible and maintained; the displayed content matching the service directory exactly, with round-the-clock services identified; the match check between display and directory performed with the alignment check at step 5; consistency of printed material and the online presence with the display; the record of prompt correction of every display on each suspension, withdrawal or addition, with dates; and the statutory displays attaching to specific services in place where those services are provided", "responsible": "The role named at step 6 maintains every display and corrects it at once on any change; the administration controls the displayed content against the directory; heads of departments report capability changes that the display must follow"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. AAC.1 standard text and all four OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 1 Access, Assessment and Continuity of Care, printed page 50 (PDF page index 56). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page, the same document the repo's extractions were built from. Levels: AAC.1.a Commitment, AAC.1.b Commitment, AAC.1.c Commitment, AAC.1.d Commitment.
   ONE OE CARRIES THE ASTERISK -- AAC.1.c, the department scope of services. Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; its output matched the committed scripts/shco_oe_asterisks.json on all 408 entries with zero differences), the AAC.1 page read directly from the extracted page text, and the committed asterisk file's own byte-for-byte agreement with the live shco_full_oes verified 2026-08-13 (132 true / 276 false / 408 total on both sides). AAC.1 was NOT among the 14 mismatches of the 2026-08-10 ten-chapter audit. doc_required for AAC.1.a/b/d is false and for AAC.1.c is true, and the PDF agrees.

TIERING UNDER THE STANDING RULE -- THIS IS THE FIRST MASTER POLICY DRAFTED UNDER IT
1. This is the seventh master policy, so the two-tier depth standing rule of 2026-08-10 (scripts/master-policy-todos.md) applies for the first time. Tier 1, full HIC.6-grade treatment: AAC.1.c only -- procedure steps 3-5 carry the reasoning, the exclusion-precision position and the four-way alignment check, and its evidence column is the deepest in the mapping. Tier 2: AAC.1.a (step 1), AAC.1.b (step 2) and AAC.1.d (step 6) -- requirement and method stated without extended rationale, evidence columns list the records without exhaustive multi-clause detail. Reviewer to note the shallower treatment of a, b and d is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check for AAC.1.c: all six approved HIC masters searched (2026-08-17) for the subject matter of this standard -- service definition, scope of services, department scope, display of services, community needs. No overlap found. The 'signage' hits in HIC.1 and HIC.2 are isolation-precaution signage, a different subject owned by HIC.2 and stated as a boundary in this draft's Scope; HIC.6's 'services provided' hits are review triggers inside its own procedure, not service definition. Tier 2 quick checks for a, b and d: same searches, no flags. NOTHING IS ADDED TO THE RECONCILIATION LIST BY THIS DRAFT.
3. FORWARD REFERENCES CREATED BY THIS DRAFT, for the standards that will own them: the Scope and step 4 refer to 'the registration and admission policy of {{HOSPITAL_NAME}}' (AAC.2, not yet drafted -- the same forward-promise pattern HIC.3/HIC.4 used toward HIC.6, which resolved when it was drafted); the Scope and step 2 rely on 'the human resource policies' for qualification verification (HRM chapter, not yet drafted); the Scope and step 6 leave rights/tariff display to 'the patient rights policies' (PRE chapter, not yet drafted). Each is a deliberate boundary, not missing content.

STATUTORY AND EXTERNAL FACTS
4. The Clinical Establishments (Registration and Regulation) Act, 2010 applies only in States that have adopted it; the draft says 'where adopted by the State' and offers the State law alternative, asserting no position on which applies to {{HOSPITAL_NAME}}. Registration/display duties are described at the level of the Act's general scheme only.
5. Statutes attached to specific services (PC-PNDT for ultrasonography including its display requirements, AERB licensing for diagnostic radiology, Drugs and Cosmetics Act for blood centre and pharmacy, MTP Act, Transplantation of Human Organs and Tissues Act) are named ONLY as applying 'where {{HOSPITAL_NAME}} provides the service concerned', with no assertion about which services this hospital provides.
6. The Consumer Protection Act, 2019 point at step 6 -- that a displayed service the hospital cannot deliver is a misleading representation -- is stated at the level of the Act's general prohibition of misleading advertisement, without citing a section number or asserting how a court would decide.
7. EXTERNAL CLINICAL/TECHNICAL FACT-CHECKING: NOT APPLICABLE, AND RECORDED AS A DECISION. The standing rule requires Tier 1 fact-checking against CDC/WHO/ISO/AAMI/CLSI and Indian statutory sources 'where the OE is technical or clinical'. AAC.1.c is organisational -- a documentation and governance requirement -- so no clinical claim exists in this draft to check. The Indian statutory references above were verified at the general level stated. No entry in this draft states a clinical fact.
8. NO NUMBERS ARE STATED ANYWHERE IN THIS DRAFT -- no review intervals, no display sizes, no language mandates beyond 'the languages the community served reads', no response times for on-call cover. Every such value is [Hospital to define]. Consistent with the no-numbers default confirmed for HIC.6 item 11.

EDITORIAL POSITIONS TAKEN -- THE REVIEWER SHOULD SEE THEM
9. Step 4's position that the exclusions are the safety content of a scope, and that vague exclusions are a document defect, is an editorial position of this draft, not a quoted requirement. It is consistent with the boundary discipline of the approved HIC set.
10. Step 7's order of operations (resource, then define, then scope, then display -- and display corrected FIRST on suspension) is an editorial position; the standard requires definition and display but does not prescribe a sequence.
11. The Policy Statement's line that directing a patient elsewhere is correct practice and never lost business is an editorial position consistent with the disclosure and non-punitive postures of the approved HIC set.

VERSION AND REVISION HISTORY -- POPULATED FROM THE START
12. version = '1.0' and revision_history = [{version 1.0, date 17-08-2026, Initial release.}] are included in the INSERT itself -- the first master policy to carry them from the start rather than by backfill, using the infrastructure of migration 20260812_shco_policy_masters_version_revision_history.sql. Date format DD-MM-YYYY per the migration's convention. HIC.1-6 were backfilled by that migration and are not touched by this draft.

DISCLAIMER BLOCK -- VERBATIM FROM THE SHARED HIC.3/4/5/6 BLOCK, AND WHAT THAT MEANS
13. The disclaimer is the shared block reproduced word for word and asserted by md5 at build time (LF-normalised, same value as the live HIC.5 row), so it cannot drift unnoticed. AAC.1 makes five documents carrying it. The known limitation recorded against HIC.6 applies MORE strongly here: paragraph 2 cites the Bio-Medical Waste Management Rules, 2016 and the Food Safety and Standards Act, 2006, NEITHER of which this document relies on, and paragraph 4 does not name the Clinical Establishments Act or Consumer Protection Act bodies this document does cite. Per the position taken at HIC.6, fixing the boilerplate belongs to a deliberate pass across all masters, not to this file; the hash assertion exists precisely so that pass cannot happen accidentally.

DELIBERATELY NOT INCLUDED -- checked and judged to belong to other standards:
- Registration, admission and the management of patients who cannot be admitted -- AAC.2 (its OEs cover registration/admission processes, staff awareness of them, and managing patients in the event of non-availability of beds; confirmed from the same PDF page as AAC.1). This draft defines the boundary those processes apply.
- Infection control signage of every kind -- HIC.2, approved.
- Staff credentialing method, personnel files and privileging -- HRM chapter.
- Patient rights display, tariff display as a rights matter, and communication in a language the patient understands during care -- PRE chapter.
- The five optional sections (definitions, training_competency, resources_required, monitoring_audit, exceptions) are deliberately left unset, matching HIC.1-6.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 10 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 8 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 10; a search for "Hospital to define" without brackets finds all 10, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, wired in from the first build of this file, which also asserts that no nested placeholder exists.

The values the hospital must supply: where the community needs assessment is held and when last performed; the review interval for the service directory; where each department's scope of services is held and how the set is indexed; the review interval for department scopes; any further display locations; the languages of the display; the role responsible for the display; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
