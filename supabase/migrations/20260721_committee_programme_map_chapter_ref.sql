-- Add per-programme OE reference to committee_programme_map.
-- Nullable; NULL falls back to committees.chapter_ref in the component (HCO 6th Ed codes unaffected).
-- Idempotent: safe to re-run.

ALTER TABLE public.committee_programme_map
  ADD COLUMN IF NOT EXISTS chapter_ref text;

-- Populate SHCO_FULL rows with verified SHCO 3rd Edition OE codes.
UPDATE public.committee_programme_map SET chapter_ref = 'PSQ.1.a, PSQ.1.e' WHERE programme = 'SHCO_FULL' AND committee_id = 1;
UPDATE public.committee_programme_map SET chapter_ref = 'HIC.1.c'          WHERE programme = 'SHCO_FULL' AND committee_id = 2;
UPDATE public.committee_programme_map SET chapter_ref = 'MOM.1.b'          WHERE programme = 'SHCO_FULL' AND committee_id = 3;
UPDATE public.committee_programme_map SET chapter_ref = 'COP.3.d'          WHERE programme = 'SHCO_FULL' AND committee_id = 20;
UPDATE public.committee_programme_map SET chapter_ref = 'COP.5.f'          WHERE programme = 'SHCO_FULL' AND committee_id = 4;
UPDATE public.committee_programme_map SET chapter_ref = 'HRM.7.c'          WHERE programme = 'SHCO_FULL' AND committee_id = 8;
UPDATE public.committee_programme_map SET chapter_ref = 'PRE.6.c'          WHERE programme = 'SHCO_FULL' AND committee_id = 17;
UPDATE public.committee_programme_map SET chapter_ref = 'IMS.6.a'          WHERE programme = 'SHCO_FULL' AND committee_id = 5;
UPDATE public.committee_programme_map SET chapter_ref = 'HRM.3.a'          WHERE programme = 'SHCO_FULL' AND committee_id = 9;
UPDATE public.committee_programme_map SET chapter_ref = 'HIC.2.g'          WHERE programme = 'SHCO_FULL' AND committee_id = 11;
