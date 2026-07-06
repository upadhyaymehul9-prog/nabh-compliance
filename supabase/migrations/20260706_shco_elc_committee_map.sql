-- Map the same 9 ELC committees from HCO_ELC to SHCO_ELC.
-- Idempotent: safe to re-run.

INSERT INTO public.committee_programme_map (committee_id, programme)
SELECT m.committee_id, 'SHCO_ELC'
FROM public.committee_programme_map m
WHERE m.programme = 'HCO_ELC'
  AND NOT EXISTS (
    SELECT 1
    FROM public.committee_programme_map x
    WHERE x.committee_id = m.committee_id
      AND x.programme = 'SHCO_ELC'
  );
