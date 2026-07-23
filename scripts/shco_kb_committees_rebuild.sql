-- Rebuild the SHCO Full committee rows in public.shco_kb.
--
-- SCOPE: touches ONLY public.shco_kb, rows with category = 'committees'.
--        No other table is read or written.
--
-- Live schema confirmed 2026-07-23 by probing PostgREST + search_shco_kb RPC:
--   shco_kb columns in use: category, section, title, content, source_label
--   (NOTE: scripts/shco_kb_schema.sql is STALE — it declares kb_type/chapter/oe_code,
--    which do NOT exist on the live table. Do not use that file as the reference.)
--
-- OE text below is verbatim from scripts/shco_oes_data.json (official SHCO 3rd Ed
-- extract). Frequency and chair are AccredReady recommendations and are labelled
-- as such in every row — the SHCO book does not specify either.
--
-- HOW TO RUN: paste into the Supabase SQL Editor for project tbptllgcjtiiqspxqcde.
-- Review the output of the final SELECT before committing.

begin;

------------------------------------------------------------------------
-- 0. Guard: confirm we are deleting exactly the 6 rows we surveyed.
--    Aborts the whole transaction if the live table has drifted.
------------------------------------------------------------------------
do $$
declare n int;
begin
  select count(*) into n from public.shco_kb where category = 'committees';
  if n <> 6 then
    raise exception 'Expected 6 existing committee rows, found %. Aborting — re-survey before running.', n;
  end if;
end $$;

------------------------------------------------------------------------
-- 1. Delete the 6 existing committee rows.
------------------------------------------------------------------------
delete from public.shco_kb where category = 'committees';

------------------------------------------------------------------------
-- 2. Insert the 10 verified SHCO_FULL committees.
--
--    Each row states the NABH basis first (verbatim OE text + level), then
--    AccredReady's recommended frequency/chair, explicitly separated so the
--    assistant cannot present the recommendation as book text.
------------------------------------------------------------------------
insert into public.shco_kb (category, section, title, content, source_label) values

-- id 1 — Quality Improvement & Patient Safety Committee (PSQ.1.a, PSQ.1.e)
('committees', 'Committees — Quality Improvement & Patient Safety',
 'Quality Improvement & Patient Safety Committee',
 $ct$NABH basis (SHCO 3rd Edition): PSQ.1.a (Core) — "The patient safety programme is developed, implemented and maintained by a multi-disciplinary committee." PSQ.1.e (Core) — "Acomprehensive quality improvement programme is developed, implemented and maintained by a multi-disciplinary committee." The book therefore requires a multi-disciplinary committee for both patient safety and quality improvement.

AccredReady's recommended practice (NOT NABH book text): meets Monthly; chaired by the CEO / Medical Director.

The SHCO 3rd Edition book does not specify meeting frequency, membership, quorum or chairperson for this committee. Each hospital must define these in its own committee terms of reference / policy document.$ct$,
 'SHCO Full — Committees — Quality Improvement & Patient Safety (PSQ.1.a, PSQ.1.e, NABH 3rd Edition, p.109)'),

-- id 2 — Infection Prevention & Control Committee (HIC.1.c)
('committees', 'Committees — Infection Prevention & Control',
 'Infection Prevention & Control Committee (IPCC)',
 $ct$NABH basis (SHCO 3rd Edition): HIC.1.c (Commitment) — "The organisation has a multidisciplinary infection control committee and an infection control team, which coordinate the implementation of all infection prevention and control activities." The book explicitly requires both a committee and a team.

AccredReady's recommended practice (NOT NABH book text): meets Monthly; chaired by the Medical Superintendent / CEO.

The SHCO 3rd Edition book does not specify meeting frequency, membership, quorum or chairperson for this committee. Each hospital must define these in its own committee terms of reference / policy document.$ct$,
 'SHCO Full — Committees — Infection Prevention & Control (HIC.1.c, NABH 3rd Edition, p.100)'),

-- id 3 — Pharmacy & Therapeutics Committee (MOM.1.b)
('committees', 'Committees — Pharmacy & Therapeutics',
 'Pharmacy & Therapeutics Committee (PTC)',
 $ct$NABH basis (SHCO 3rd Edition): MOM.1.b (Core) — "Pharmacy services and medication usage are implemented following written guidance through a multidisciplinary committee." The book explicitly requires a multidisciplinary committee.

AccredReady's recommended practice (NOT NABH book text): meets Monthly; chaired by the HOD Medicine / a Senior Clinician.

The SHCO 3rd Edition book does not specify meeting frequency, membership, quorum or chairperson for this committee. Each hospital must define these in its own committee terms of reference / policy document.$ct$,
 'SHCO Full — Committees — Pharmacy & Therapeutics (MOM.1.b, NABH 3rd Edition, p.83)'),

-- id 4 — Blood Transfusion Committee (COP.5.f)
('committees', 'Committees — Blood Transfusion',
 'Blood Transfusion Committee',
 $ct$NABH basis (SHCO 3rd Edition): COP.5.f (Achievement) — "Post-transfusion form is collected, reactions if any identified and are analysed for corrective and preventive actions."

IMPORTANT: this OE requires the analysis of transfusion reactions; it does NOT itself mandate a standing Blood Transfusion Committee. AccredReady recommends a committee as a practical way to own and evidence that analysis.

AccredReady's recommended practice (NOT NABH book text): meets Monthly; chaired by the Medical Director / Haematologist.

The SHCO 3rd Edition book does not specify meeting frequency, membership, quorum or chairperson. Each hospital must define these in its own committee terms of reference / policy document.$ct$,
 'SHCO Full — Committees — Blood Transfusion (COP.5.f)'),

-- id 5 — Medical Records Committee (IMS.6.a)
('committees', 'Committees — Medical Records',
 'Medical Records Committee',
 $ct$NABH basis (SHCO 3rd Edition): IMS.6.a (Core) — "The medical records are reviewed periodically."

IMPORTANT: this OE requires periodic review of medical records; it does NOT itself mandate a standing Medical Records Committee. AccredReady recommends a committee as a practical way to own and evidence that review. Note the book says "periodically" without defining an interval.

AccredReady's recommended practice (NOT NABH book text): meets Monthly; chaired by the Medical Director.

The SHCO 3rd Edition book does not specify meeting frequency, membership, quorum or chairperson. Each hospital must define these in its own committee terms of reference / policy document.$ct$,
 'SHCO Full — Committees — Medical Records (IMS.6.a)'),

-- id 8 — Credentials & Privileging Committee (HRM.7.c)
('committees', 'Committees — Credentials & Privileging',
 'Credentials & Privileging Committee',
 $ct$NABH basis (SHCO 3rd Edition): HRM.7.c (Core) — "Medical professionals are granted privileges to admit and care for the patients in consonance with their qualification, training, experience and registration."

IMPORTANT: this OE requires a privileging process; it does NOT itself mandate a standing Credentials & Privileging Committee. AccredReady recommends a committee as a practical way to own and evidence credentialing decisions.

AccredReady's recommended practice (NOT NABH book text): meets Quarterly / as needed; chaired by the Medical Director.

The SHCO 3rd Edition book does not specify meeting frequency, membership, quorum or chairperson. Each hospital must define these in its own committee terms of reference / policy document.$ct$,
 'SHCO Full — Committees — Credentials & Privileging (HRM.7.c)'),

-- id 9 — Safety Committee (HRM.3.a)
('committees', 'Committees — Safety',
 'Safety Committee',
 $ct$NABH basis (SHCO 3rd Edition): HRM.3.a (Commitment) — "Staff are trained in the organisation's safety programme".

IMPORTANT: this OE requires staff training on the safety programme; it does NOT itself mandate a standing Safety Committee. AccredReady recommends a committee as a practical way to own the safety programme and evidence it.

AccredReady's recommended practice (NOT NABH book text): meets Monthly; chaired by the General Manager / Administrator.

The SHCO 3rd Edition book does not specify meeting frequency, membership, quorum or chairperson. Each hospital must define these in its own committee terms of reference / policy document.$ct$,
 'SHCO Full — Committees — Safety (HRM.3.a)'),

-- id 11 — Antimicrobial Stewardship Team (HIC.2.g)
('committees', 'Committees — Antimicrobial Stewardship',
 'Antimicrobial Stewardship Team (AST)',
 $ct$NABH basis (SHCO 3rd Edition): HIC.2.g (Excellence) — "The organisation implements an antibiotic stewardship programme."

IMPORTANT: two qualifications. (1) This OE is at EXCELLENCE level, not Core or Commitment. (2) It requires a stewardship programme; it does NOT itself mandate a standing team or committee. AccredReady recommends an AST as the practical way to run and evidence the programme.

AccredReady's recommended practice (NOT NABH book text): meets Weekly/Monthly; led by an Infectious Disease Specialist / Microbiologist.

The SHCO 3rd Edition book does not specify meeting frequency, membership, quorum or chairperson. Each hospital must define these in its own committee terms of reference / policy document.$ct$,
 'SHCO Full — Committees — Antimicrobial Stewardship (HIC.2.g)'),

-- id 17 — Grievance Redressal Committee (PRE.6.c)
('committees', 'Committees — Grievance Redressal',
 'Grievance Redressal Committee (Patient)',
 $ct$NABH basis (SHCO 3rd Edition): PRE.6.c (Core) — "The organisation redresses patient complaints as per the defined mechanism. Patient and/or family members are made aware of the procedure for giving feedback and/or lodging complaints".

IMPORTANT: this OE requires a defined complaint-redressal mechanism; it does NOT itself mandate a standing Grievance Redressal Committee. AccredReady recommends a committee as a practical way to own and evidence that mechanism.

AccredReady's recommended practice (NOT NABH book text): convenes as needed, with a monthly review of complaints; chaired by the Executive Director.

The SHCO 3rd Edition book does not specify meeting frequency, membership, quorum or chairperson. Each hospital must define these in its own committee terms of reference / policy document.$ct$,
 'SHCO Full — Committees — Grievance Redressal (PRE.6.c)'),

-- id 20 — Code Blue (Resuscitation) Committee (COP.3.d)
('committees', 'Committees — Code Blue / Resuscitation',
 'Code Blue (Resuscitation) Committee',
 $ct$NABH basis (SHCO 3rd Edition): COP.3.d (Commitment) — "Amultidisciplinary committee does a post-event analysis of all cardiopulmonary resuscitations, and corrective and preventive measures are taken based on this." The book explicitly requires a multidisciplinary committee, and requires post-event analysis of ALL resuscitations.

AccredReady's recommended practice (NOT NABH book text): meets Monthly, and additionally after each event for post-event analysis; chaired by the Medical Director.

The SHCO 3rd Edition book does not specify meeting frequency, membership, quorum or chairperson for this committee. Each hospital must define these in its own committee terms of reference / policy document.$ct$,
 'SHCO Full — Committees — Code Blue / Resuscitation (COP.3.d, NABH 3rd Edition, p.70)');

------------------------------------------------------------------------
-- 3. Roster row — answers "how many committees" / "list all committees".
------------------------------------------------------------------------
insert into public.shco_kb (category, section, title, content, source_label) values
('committees', 'Committees — Full List',
 'Complete list of SHCO Full committees (10 total)',
 $ct$AccredReady tracks 10 committees for the NABH SHCO Full Accreditation programme. The complete list, with the NABH objective element each one supports:

1. Quality Improvement & Patient Safety Committee — PSQ.1.a, PSQ.1.e
2. Infection Prevention & Control Committee (IPCC) — HIC.1.c
3. Pharmacy & Therapeutics Committee (PTC) — MOM.1.b
4. Blood Transfusion Committee — COP.5.f
5. Medical Records Committee — IMS.6.a
6. Credentials & Privileging Committee — HRM.7.c
7. Safety Committee — HRM.3.a
8. Antimicrobial Stewardship Team (AST) — HIC.2.g
9. Grievance Redressal Committee (Patient) — PRE.6.c
10. Code Blue (Resuscitation) Committee — COP.3.d

Of these, the SHCO 3rd Edition book explicitly requires a multidisciplinary committee in only four places: PSQ.1.a and PSQ.1.e (patient safety / quality improvement), HIC.1.c (infection control committee and team), MOM.1.b (pharmacy and therapeutics), and COP.3.d (resuscitation post-event analysis). The remaining committees are AccredReady's recommended structure for owning and evidencing the underlying requirement — they are not named as committees in the book.

This count of 10 is AccredReady's SHCO Full committee set. The book does not state a total number of committees.$ct$,
 'SHCO Full — Committees — Full List (AccredReady committee set)');

------------------------------------------------------------------------
-- 4. RECOMMENDED ADDITION — not in your original spec. See notes.
--    The deleted set included a ROM.3.c row that has NO counterpart in the
--    10-committee list; without this insert that book requirement is lost
--    from shco_kb entirely. Delete this statement if you don't want it.
------------------------------------------------------------------------
insert into public.shco_kb (category, section, title, content, source_label) values
('committees', 'Committees — Effectiveness Review',
 'Committee Effectiveness Review',
 $ct$NABH basis (SHCO 3rd Edition): ROM.3.c (Commitment) — "The functioning of committees is reviewed for their effectiveness."

This applies to ALL committees, not to any single one: the hospital must periodically review whether its committees are actually functioning effectively, and retain evidence of that review.

The SHCO 3rd Edition book does not specify how often this review must happen, who conducts it, or what form the evidence takes. Each hospital must define this in its own committee terms of reference / governance policy.$ct$,
 'SHCO Full — Committees — Committee Effectiveness Review (ROM.3.c, NABH 3rd Edition, p.117)');

------------------------------------------------------------------------
-- 5. Verify before you commit.
------------------------------------------------------------------------
select title, section, source_label
from public.shco_kb
where category = 'committees'
order by title;

-- Expected: 12 rows (10 committees + 1 roster + 1 effectiveness review),
-- or 11 if you removed section 4 above.

commit;
