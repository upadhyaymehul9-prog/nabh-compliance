# -*- coding: utf-8 -*-
"""Hospital-facing What-we-do methods for HCO PRE.1–PRE.8.

Written from official Standards PDF OE wording plus Guidebook Interpretation
depth (method notes are attached separately by the generator). Do not restate
the OE line as the whole method.
"""
from __future__ import annotations


def method_bodies(*, D, HOSPITAL, BLANK) -> dict[str, str]:
    """Return method body text keyed by oe_code (without the 5.N title)."""
    qc = D("Quality Coordinator")
    ms = D("Medical Superintendent")
    ns = D("Nursing Superintendent")
    pa = D("Patient Accounts In-Charge")
    gr = D("Guest Relations / Patient Rights Officer")
    yearly = D("annually")
    quarterly = D("quarterly")

    return {
        "PRE.1.a": f"""{HOSPITAL} documents patient and family rights and responsibilities in consonance with the Charter of Patients' Rights named by the statutory body. The current text is displayed where patients, families and visitors can see it (registration, OPD waiting, ward notice boards, emergency). Pamphlets or equivalent IEC material are available; the material is at least bilingual.

The {qc} owns the current version. Staff who register or admit patients point to the display and offer the pamphlet at first contact. A rights-and-responsibilities file that exists only in a quality folder is not implemented.""",

        "PRE.1.b": f"""Rights and responsibilities are actively promoted, not only posted. For in-patients, {D('the admitting nurse or Guest Relations')} counsels the patient and/or family on rights and responsibilities in a format and language they can understand, and records that counselling in the admission note.

For out-patients, educational material is easily accessible and prominently displayed in OPD. The {qc} spot-checks display and counselling records {quarterly}.""",

        "PRE.1.c": f"""Staff are trained at induction and {yearly} on their duty to protect and respect patient and family rights. Conduct during examination, communication and record-handling must convey that duty.

The {ms} names the {gr} as the day-to-day owner of rights protection. A rights poster without staff training is not protection under this element.""",

        "PRE.1.d": f"""The organisation keeps a written list of examples of rights infringements (privacy compromise, confidentiality breach, disrespect of religious or cultural needs, records not provided in the stipulated time, and other items the {ms} adds for this hospital). Staff report a violation on the incident form, including how the right was violated and, where applicable, by whom.

Patients and families can report a violation themselves — through the feedback form (rights worded so a lay person can tick them) or by speaking to the {gr}. Anonymous reports are logged. The {qc} holds the incident file.""",

        "PRE.1.e": f"""Every logged rights violation is investigated. Top leadership ({ms} with the {qc}) documents the incident, the investigation and the outcome, and assigns corrective and/or preventive action in a time frame the organisation defines ({D('within 15 days of the report, sooner if the patient is still in hospital')}).

Open actions are tracked until closed. A log without investigation or CAPA is not compliance with this CORE element.""",

        "PRE.2.a": f"""Staff ask how the patient wishes to be addressed, and record dietary preferences, worship requirements and any specific requirement following death. The {D('treating doctor and the assigned nurse')} act on those preferences unless a documented clinical or statutory reason prevents it.

Spiritual-need requests go to {D('the hospital arranged faith / counselling contact')} without delaying care. Preferences are visible on the nursing kardex / admission sheet.""",

        "PRE.2.b": f"""During examination, procedures and treatment the patient is exposed only immediately before the actual procedure; screens, drapes and a closed door (or equivalent) are used. The organisation's privacy-and-dignity guidelines sit with the {ns}.

Photographs or recordings of a procedure require explicit informed consent and must not reveal the patient's identity in teaching or publicity material. A privacy breach in progress is a stop-work trigger (section 6).""",

        "PRE.2.c": f"""Staff protect patients from neglect or abuse: unattended fall from bed/trolley, assault, unwarranted repeated internal examination, manhandling. Extra precautions apply to elderly, neonate, physically or mentally challenged, comatose and anaesthetised patients.

Any suspected neglect or abuse is stopped, the patient is protected, and the incident is reported the same shift under PRE.1.d. This is a stop-work trigger (section 6).""",

        "PRE.2.d": f"""Patient information is confidential. Staff do not discuss patients in public places (lifts, corridors, cafeterias). HIV status and other confidential information are not written or pasted on the cover of the medical record, and are not displayed in a way the public can read.

Statutory requirements on privileged communication are followed. Disclosure without the patient's permission is an incident under PRE.1.d. The {qc} includes confidentiality in the {yearly} rights training.""",

        "PRE.2.e": f"""When a patient refuses treatment, the treating doctor discusses the available options, explains the consequences of refusal, and documents the discussion. If the patient still refuses after that explanation, the refusal is respected.

The note records what was offered, what was refused, and who witnessed the explanation. Coercing a competent adult to accept treatment is a rights violation.""",

        "PRE.2.f": f"""Patients and families may seek an additional opinion from inside or outside {HOSPITAL}. Staff respect that decision and facilitate access to relevant information and clinical evaluation (copies of records, imaging, reports).

A request for information on a particular physician's qualifications and experience is answered from the credential file. The {ms} names how an internal second opinion is arranged ({D('another consultant of the same specialty, documented in the record')}).""",

        "PRE.2.g": f"""Informed consent is obtained by the treating doctor or a doctor member of the treating team before transfusion of blood or blood components, anaesthesia, surgery, initiation of any research protocol, and any other invasive / high-risk procedure / treatment.

The consent list and the process live in PRE.4. Starting any listed item without that consent is a stop-work trigger (section 6). Emergency life-saving exceptions follow PRE.4.""",

        "PRE.2.h": f"""The displayed rights include the right to complain and the method to voice a complaint. The mechanism is accessible (written, verbal, telephone) and redressal is fair and transparent.

Complaint process detail is owned by PRE.7. This element is met when the rights display and the admission counselling actually tell people how to complain, not only when a complaints SOP exists in a file.""",

        "PRE.2.i": f"""Patients and families are told the expected cost of treatment in a transparent way — consultations, procedures and investigations — by written estimate or by making the relevant tariff available.

Detailed pricing, tariff and change-in-plan rules are owned by PRE.6. This element is met when the rights counselling includes cost information, not only when a tariff exists in accounts.""",

        "PRE.2.j": f"""Every patient has access to their clinical record, in line with the Code of Medical Ethics and statutory requirements. The request path is {D('written application to Medical Records, copies within the organisation-defined time')}.

Cross-reference IMS.4.h for the records procedure. Refusal to show a competent adult their record is a rights violation under PRE.1.d.""",

        "PRE.2.k": f"""The patient and family are told the name of the treating doctor, the care plan, progress, and information on healthcare needs. The {D('treating doctor')} does this at admission and at significant plan changes; nursing reinforces the name of the consultant on the board / wristband process.

A patient who cannot name their treating doctor on a sample walk-round is a gap for this element.""",

        "PRE.2.l": f"""The patient decides what information about their care is given to self and to family. Sensitive or confidential information goes to the patient and to the next of kin only if the patient wants that. For minors, information is given to at least one parent or guardian.

The {D('treating doctor')} records the patient's choice in the medical record (including 'share with named family member X' or 'do not share diagnosis with family').""",

        "PRE.3.a": f"""The attending doctor discusses proposed care — including referral to internal or external services — with the patient and/or family in a language they understand: risks, benefits, alternatives, expected results and possible complications.

The explanation is documented and signed by the doctor concerned. Expected outcomes are discussed again at periodic intervals. This CORE discussion is not replaced by a signed consent form alone (consent is PRE.4).""",

        "PRE.3.b": f"""The care plan is prepared and modified in consultation with the patient and/or family. Treatment options, risks and benefits are explained while the plan is being written. Where possible the plan incorporates their concerns and requests, limited by statutory requirements, and takes religious, cultural and spiritual views into account.

The {D('treating doctor')} records that consultation. A plan written only in the doctor's notes with no evidence of discussion is not Achievement for this element.""",

        "PRE.3.c": f"""Results of diagnostic tests are explained at least in broad terms, including what they mean for progress and treatment. The {D('treating doctor')} does this; abnormal results that change the plan are explained the same day they are available (or as soon as the patient/family can be reached).

Dumping a printout in the file without explanation is not informing.""",

        "PRE.3.d": f"""Changes in condition — improvement, deterioration or complications — are explained in a timely manner. Withholding-of-resuscitation requests from relatives are discussed only within ethical and legal parameters (the competent patient's own decision governs).

Night and emergency deterioration is communicated by the {D('on-call doctor')} without waiting for the next routine round.""",

        "PRE.3.e": f"""{HOSPITAL} identifies situations that need multi-disciplinary counselling: family of a critically ill patient, potential organ donor and/or family, long-stay patients, and other situations the {ms} adds. The treating clinician leads; doctors from involved specialties, nurses and physiotherapists join as required.

Counselling is recorded (who was present, what was discussed). Cross-reference COP.1.e for uniform-care counselling. This Achievement element is evidenced by actual multi-disciplinary sessions, not by a committee name.""",

        "PRE.4.a": f"""The {ms} keeps a written list of procedures for which informed consent is required. The list is built from this standard and from statutory requirements — including, where they apply to {HOSPITAL}'s scope, the MTP Act, the PC-PNDT Act, the Transplantation of Human Organs Act, and HIV testing under the HIV and AIDS (Prevention and Control) Act 2017 and NACO policy.

Written guidance names the steps of the consent process and the person responsible. Staff who obtain consent are trained on that guidance. Starting a listed procedure without consent is a stop-work trigger (section 6).""",

        "PRE.4.b": f"""The consent process follows statutory norms, including at least: consent taken before the procedure; at least one witness who was present for the entire doctor–patient communication signing the form.

For a procedure repeated over a long time (for example dialysis), consent is taken at the first instance with a defined validity not more than six months; the patient endorses at each repeat; a change or addition of modality needs fresh consent. The {qc} audits a sample of consent forms {quarterly}.""",

        "PRE.4.c": f"""The consent names the doctor performing the procedure. If more than one specialty operates, the consent names the principal surgeon from each specialty; each explains their own role, benefits, risks and alternatives. A doctor under training is specified, and the supervising qualified doctor is named.

The form is at least bilingual. If counselling is in a language other than the form, the record names that language and any interpreter. Risks, benefits and alternatives are part of the documentation. Consent is a communication process, not only a signature.""",

        "PRE.4.d": f"""Consent is taken from the patient whenever the patient is capable and above the legal age. No one consents on behalf of a competent adult. When the patient is incapable, next of kin / legal guardian is used, in the order spouse, son/daughter, parents, brothers/sister, unless a statute applicable to that case says otherwise.

In a life-threatening situation when the patient is incapable and next of kin is not available, the treating doctor and another clinician may decide to safeguard the patient's life; both names and the reason are recorded the same shift.""",

        "PRE.4.e": f"""The person performing the procedure is responsible for the entire consent process — explanation and signature. It is not acceptable for that person only to explain and for a nurse to take the written consent.

A doctor member of the performing team may take consent on that person's behalf. Cross-reference COP.7.e, COP.12.b, COP.13.d and COP.14.c for procedure-, sedation-, anaesthesia- and surgery-specific consent. The {ms} samples this on {quarterly} record audit.""",

        "PRE.5.a": f"""Staff screen (informally) the patient and/or family's understanding and language needs, then educate in that language and format — counselling, printed material, audio-visual aids. Material uses the language identified at PRE.1.a, not only English.

The {ns} owns ward and OPD education practice. Education that the patient cannot understand is not education under this CORE element.""",

        "PRE.5.b": f"""The organisation keeps a list of medications that need extra education on safe and effective use and potential side effects (for example digoxin, and drugs that must be taken at a specific time). Nursing or pharmacy educates against that list when those drugs are prescribed, and records it.

This is not a substitute for MOM administration checks. The {D('Pharmacy In-Charge')} keeps the education list current with the formulary.""",

        "PRE.5.c": f"""A list of food–drug interactions that matter here (for example no alcohol with metronidazole) is used to educate the patient and family about diet during that medication. Dietetics or nursing delivers the message when the listed drug is prescribed.

The list sits with pharmacy and dietetics. Education is recorded on the medication-counselling / diet note.""",

        "PRE.5.d": f"""Diet and nutrition education covers the relationship between foods or supplements and the patient's condition, plus general healthy-diet advice. The {D('Dietetics In-Charge')} provides this for in-patients on a therapeutic diet and for out-patients when the treating doctor requests it.

A generic poster in the dining area is not patient-specific education.""",

        "PRE.5.e": f"""Immunisation education for adults covers vaccines relevant to the patient (influenza, pneumococcus, typhoid, hepatitis B, meningococcus, and others the treating doctor names). Paediatric immunisation education follows the universal immunisation programme.

The {D('treating doctor or immunisation clinic nurse')} records the advice and vaccines due.""",

        "PRE.5.f": f"""Pain-management education is given when the patient is likely to have long-term pain because the underlying condition is not treatable, and it stays within their personal, cultural and religious beliefs. Acute post-operative pain teaching is additional, not a substitute for this element.

Cross-reference COP pain-management policy. The {ns} names who delivers long-term pain education.""",

        "PRE.5.g": f"""Disease-specific education covers the process, complications and prevention: lifestyle (stress, exercise, smoking and substance cessation), diet and immunisation where appropriate. Booklets, videos or leaflets matching the hospital's common conditions support the counselling.

The {D('treating doctor')} assigns the education; nursing or a health educator delivers and records it.""",

        "PRE.5.h": f"""Patients and families are educated on preventing healthcare-associated infections — at least hand washing and avoiding overcrowding at the bedside. IPC posters support, they do not replace, person-to-person education at admission.

Cross-reference the IPC chapter for the hospital's infection-prevention programme. Nursing records HAI-prevention advice on the admission checklist.""",

        "PRE.5.i": f"""Special educational needs are identified during treatment (for example ADHD, autism support, physical disability, speech-language-communication needs, social and emotional health needs) and addressed with counselling, print or audio-visual aids that fit that need.

The {D('treating doctor with nursing')} flags the need in the record and names how it was addressed. This Achievement element is evidenced by identified needs that were actually met.""",

        "PRE.5.j": f"""{HOSPITAL} promotes patient engagement: disease-based support groups where the scope allows, involvement in patient safety and quality improvement, encouragement to report safety incidents, near misses and concerns, and — where the {ms} implements it — a patient advisory council and named patient-safety champions.

The {qc} records engagement activities {quarterly}. A suggestion box alone is not Excellence for this element.""",

        "PRE.6.a": f"""Pricing-policy components — consultation charges, bed charges, nursing charges, security deposit — are available near registration and/or the admission desk for out-patient, emergency, ICU and in-patient settings, based on the billing policy.

The {pa} keeps the displayed components current. A policy that exists only in accounts and is not visible at the desk is not CORE compliance.""",

        "PRE.6.b": f"""An updated tariff list is available for patients to review. {HOSPITAL} charges as per that list; any additional charge is enumerated in the tariff and communicated. Rates are uniform in a given setting and transparent.

The {pa} dates the current list. Informal 'extra' charges that are not on the tariff are not permitted.""",

        "PRE.6.c": f"""Patients receive an estimate of treatment expenses, preferably written, based on the treatment plan. OPD / registration / admission staff prepare it in consultation with the treating doctor. Limitations (for example emergency admission) are discussed.

The estimate is filed in the patient account / medical record. 'We'll see at discharge' is not an explanation of expected costs.""",

        "PRE.6.d": f"""When the care plan changes in a way that affects cost — shift to or from ICU, medical to surgical management, further expensive investigations — the patient and/or family are informed of the financial implication before the change is treated as agreed (emergencies: as soon as practicable).

The {pa} or the {D('treating doctor')} records the revised estimate. Surprise charges at discharge for a known plan change are a gap.""",

        "PRE.7.a": f"""Feedback is captured physically or electronically and includes patient satisfaction. Out-patient and in-patient data are kept separate. The {qc} owns the tool and the response rate target ({D('a defined sample of discharges and a defined OPD sample each month')}).

A visitor book that is never tabulated is not a feedback mechanism.""",

        "PRE.7.b": f"""Patient experience is captured beyond satisfaction: communication with doctors and nurses, pain management, hospital environment (cleanliness and quietness), staff responsiveness, discharge information, communication about medications, overall rating, and patient-reported experience measures (PREMs).

The {qc} reports PREM / experience results {quarterly} to the {ms}. Satisfaction scores alone are not Achievement for this element.""",

        "PRE.7.c": f"""Written guidance names how to lodge a complaint (including verbal or telephonic), how complaints are compiled and analysed, the time frame, the person responsible, and how action is documented. Anonymous complaints may be given credence as the organisation decides. Complaints against healthcare workers are included.

The {gr} logs every complaint. Redressal without a defined mechanism is not this CORE asterisked element.""",

        "PRE.7.d": f"""Patients and families are made aware of how to give feedback and lodge complaints — by display and/or written information — in an environment of trust. The path is on the rights display (PRE.2.h) and in the admission pamphlet.

The {qc} checks that the displayed path matches the actual complaints desk / phone / form.""",

        "PRE.7.e": f"""Feedback and complaints are reviewed and/or analysed within a defined time frame ({D('complaints within 7 days; feedback tabulated monthly')}). The process is documented. Where appropriate the patient and/or family are involved and told the outcome.

Overdue open complaints are listed for the {ms} each month.""",

        "PRE.7.f": f"""Where analysis shows a gap, corrective and/or preventive action is taken and recorded (owner, due date, closure). The {qc} tracks CAPA from feedback and complaints together with PRE.1.e rights-violation CAPA when the subject overlaps.

Analysis without action is not this element.""",

        "PRE.8.a": f"""Communication with patients and/or families is done so that it serves its purpose — clear, correct, complete, concrete, concise, considerate and courteous (or another model the organisation adopts). Barriers (language, hearing, literacy) are identified and overcome; interpreters are arranged when needed.

Staff are trained on this at induction and {yearly}. Cross-reference the glossary for 'effective communication'. This asterisked element is evidenced by training plus observed practice, not by a poster of the seven Cs.""",

        "PRE.8.b": f"""The {ms} keeps a written list of special situations that need enhanced communication: breaking bad news, handling adverse events, an aggressive patient or family, talking with the family after a death, counselling for a complicated intervention, and others this hospital adds.

The list is in this policy's training pack. Staff who work in emergency, ICU, OT and wards are taught which situations are on it.""",

        "PRE.8.c": f"""For each listed special situation, the organisation details the enhanced communication required. Breaking bad news uses SPIKES (Setting, Perception, Invitation or information, Knowledge, Empathy, Summarize or strategize) or another named model the {ms} adopts.

The {D('treating doctor')} leads enhanced communication; nursing supports. A note records that the conversation happened (without reducing it to a tick-box that replaces the conversation).""",

        "PRE.8.d": f"""Unacceptable communication is not allowed: abusing patients, hurting religious or cultural sentiments, communicating with disrespect. A breach is a conduct incident and a rights incident (PRE.1.d).

The {ms} acts on a confirmed breach the same as any other serious conduct issue. Training names examples so staff can recognise the line.""",

        "PRE.8.e": f"""Implementation of effective communication is monitored and reviewed through patient and stakeholder feedback and complaints (PRE.7) and through {quarterly} observation or record sample by the {qc}.

Findings go to the {ms}. This Achievement element is evidenced by the review happening and by actions when communication fails, not by the existence of PRE.8.a training alone.""",
    }
