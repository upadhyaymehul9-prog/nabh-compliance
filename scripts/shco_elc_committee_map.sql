-- Run in Supabase SQL Editor to give SHCO ELC the same 9 committees as HCO ELC.
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

-- Verify: should return 9 rows for each programme
SELECT programme, count(*) AS committee_count
FROM public.committee_programme_map
WHERE programme IN ('HCO_ELC', 'SHCO_ELC')
GROUP BY programme
ORDER BY programme;
