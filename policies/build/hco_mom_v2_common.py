# -*- coding: utf-8 -*-
"""Shared helpers for HCO Full MOM.1–MOM.11 v2 builders.

Always pass draft_label via hco_document_control — never
pre_v2_common.document_control() (that still injects
\"not an approved master\").
"""
from __future__ import annotations

from hco_cop_v2_common import DRAFT_LABEL, CHAPTER, VERSION, PROGRAMME, hco_document_control
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL

# Standards where Stop-work is proposed (judgment calls — see chapter notes / handoff).
STOP_WORK_PROPOSALS: dict[int, str] = {
    3: "LASA / different concentrations stored together; emergency medications missing or unreplenished; storage outside manufacturer recommendations",
    4: "Prescribe without allergy/ADR check; verbal order outside the documented safe process; prescription that fails minimum requirements",
    6: "Dispense unlabelled medication; high-risk order not verified before dispensing; recalled or expired item",
    7: "Administer without patient identification or without verifying medication–strength–route–time against the order; tubing mis-connection; person not permitted by law",
    9: "Chemo/radiopharmaceutical preparation without qualified personnel; unsecured narcotics/psychotropics",
}


def stop_work_text(n: int) -> str:
    """Hospital-facing Stop-work section for flagged MOM standards."""
    texts = {
        3: f"""Do not store look-alike, sound-alike medications, or different concentrations of the same medication, physically together.

Do not leave an emergency-medication location without the defined list, or leave a used emergency medication unreplenished.

Do not issue or use a medication that has been stored outside the manufacturer's temperature, light or security recommendations until pharmacy has assessed it.

Stop-work applies to the storage location and to issue from that location. Immediate life-saving use of the only available dose continues while escalation happens, and is documented.

The person who stops tells the {D('Pharmacy In-Charge')} and the {D('Medication Safety Officer')} the same shift. Refusing unsafe storage or issue is not a disciplinary matter.""",
        4: f"""Do not prescribe (or transcribe a prescription for action) when drug allergies and previous adverse drug reactions have not been ascertained.

Do not act on a verbal medication order except through the organisation's documented verbal-order process (read-back, documentation, countersignature within the defined time).

Do not accept a prescription that fails the organisation's determined minimum requirements.

Stop-work applies to writing or acting on the unsafe order. Immediate life-saving medication in an emergency follows the documented emergency-prescription rules and is written up as soon as the patient is stable.

The person who stops tells the {D('treating doctor')} and the {D('Medication Safety Officer')} the same shift. Refusing an unsafe prescription is not a disciplinary matter.""",
        6: f"""Do not dispense a medication that is unlabelled, recalled, expired, or a high-risk order that has not been verified for dose, frequency and route.

Stop-work applies to the dispense. Immediate life-saving issue from floor stock in an emergency follows the documented after-hours / emergency-dispense rules and is recorded.

The person who stops tells the {D('Pharmacy In-Charge')} the same shift. Refusing an unsafe dispense is not a disciplinary matter.""",
        7: f"""Do not administer a medication when the patient has not been identified with the organisation's identifiers, when the medication / strength / route / timing has not been verified against the order, when the product fails physical inspection, or when you are not on the list of persons permitted by law and by {HOSPITAL} to administer that medication.

Do not connect a catheter or tubing for medication administration until the line has been traced from the patient to the source.

Stop-work applies to the administration start. Immediate life-saving administration in a crash continues with the best available permitted staff and is documented afterward.

The person who stops tells the {D('Nurse In-Charge')} and the {D('treating doctor')} the same shift. Refusing an unsafe administration is not a disciplinary matter.""",
        9: f"""Do not prepare or administer chemotherapeutic agents or radio-pharmaceuticals without qualified personnel and the required preparation conditions.

Do not leave narcotic drugs or psychotropic substances unsecured, or issue them without the required register entry and authorised prescriber.

Stop-work applies to preparation, issue and administration of these classes. Immediate life-saving analgesia / anaesthesia using a controlled drug follows the documented emergency-controlled-drug rules and is entered in the register the same shift.

The person who stops tells the {D('Pharmacy In-Charge')} and the {D('Medical Superintendent')} the same shift. Refusing unsafe handling of these agents is not a disciplinary matter.""",
    }
    return texts.get(n, "")


__all__ = [
    "BLANK",
    "D",
    "HOSPITAL",
    "HCO_EDITION_LABEL",
    "DRAFT_LABEL",
    "CHAPTER",
    "VERSION",
    "PROGRAMME",
    "hco_document_control",
    "STOP_WORK_PROPOSALS",
    "stop_work_text",
]
