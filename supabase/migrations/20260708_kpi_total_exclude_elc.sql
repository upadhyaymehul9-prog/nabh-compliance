-- Fix: HCO Full KPI total was leaking ELC-scoped KPI rows.
--
-- The `kpis` table now carries the ELC KPI definitions (kpi_no 51-64), each
-- twinned across HCO_ELC + SHCO_ELC via the programme_scope array = 28 rows.
-- Both get_pillar_readiness and get_final_decision did `count(*) from kpis`
-- with NO programme_scope guard, so HCO Full's "KPIs tracked" denominator
-- became 50 + 28 = 78. This redefines both functions verbatim, changing ONLY
-- the total-KPI count to exclude any row whose programme_scope overlaps the
-- ELC tags. Everything else is unchanged.
--
-- Guard: `not (coalesce(programme_scope,'{}') && array['HCO_ELC','SHCO_ELC'])`
--   - NULL scope  -> coalesced to '{}' -> no overlap -> kept  (the 50 Full KPIs)
--   - ['HCO_ELC'] -> overlaps          -> excluded            (ELC twins)
--
-- Idempotent — safe to re-run. Run in the Supabase SQL Editor.

------------------------------------------------------------------------
-- 1) get_pillar_readiness
------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION public.get_pillar_readiness(p_hospital_id uuid, p_assessment_id uuid)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
declare
  v_kpi_count integer;
  v_kpi_total integer;
  v_kpi_pct numeric;
  v_committee_count integer;
  v_committee_total integer := 26;
  v_audit_count integer;
  v_audit_total integer := 12;
  v_months_with_data integer;
begin
  -- KPI: count distinct KPIs with at least 3 months of data
  select count(distinct kpi_id)
  into v_kpi_count
  from (
    select kpi_id, count(*) as months
    from kpi_data
    where hospital_id = p_hospital_id
    group by kpi_id
    having count(*) >= 3
  ) k;

  -- Get total KPIs (HCO Full only — exclude ELC-scoped rows, kpi_no 51-64)
  select count(*) into v_kpi_total from kpis
  where not (coalesce(programme_scope, '{}'::text[]) && array['HCO_ELC','SHCO_ELC']);

  -- Committees: count distinct committees with at least 1 meeting in last 12 months
  select count(distinct committee_id)
  into v_committee_count
  from committee_meetings
  where hospital_id = p_hospital_id
    and meeting_date >= now() - interval '12 months';

  -- Audits: count distinct audits completed in last 12 months
  select count(distinct audit_id)
  into v_audit_count
  from audit_records
  where hospital_id = p_hospital_id
    and status = 'completed'
    and audit_date >= now() - interval '12 months';

  return jsonb_build_object(
    'kpi', jsonb_build_object(
      'tracked', v_kpi_count,
      'total', v_kpi_total,
      'pct', case when v_kpi_total > 0
             then round((v_kpi_count::numeric / v_kpi_total::numeric) * 100, 1)
             else 0 end,
      'status', case
        when v_kpi_count = 0 then 'NOT_STARTED'
        when v_kpi_count < v_kpi_total * 0.5 then 'IN_PROGRESS'
        when v_kpi_count >= v_kpi_total * 0.8 then 'READY'
        else 'IN_PROGRESS'
      end
    ),
    'committees', jsonb_build_object(
      'active', v_committee_count,
      'total', v_committee_total,
      'pct', round((v_committee_count::numeric / v_committee_total::numeric) * 100, 1),
      'status', case
        when v_committee_count = 0 then 'NOT_STARTED'
        when v_committee_count < 20 then 'IN_PROGRESS'
        when v_committee_count >= 20 then 'READY'
        else 'IN_PROGRESS'
      end
    ),
    'audits', jsonb_build_object(
      'completed', v_audit_count,
      'total', v_audit_total,
      'pct', round((v_audit_count::numeric / v_audit_total::numeric) * 100, 1),
      'status', case
        when v_audit_count = 0 then 'NOT_STARTED'
        when v_audit_count < 10 then 'IN_PROGRESS'
        when v_audit_count >= 10 then 'READY'
        else 'IN_PROGRESS'
      end
    )
  );
end;
$function$;

------------------------------------------------------------------------
-- 2) get_final_decision
------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION public.get_final_decision(param_id uuid)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
AS $function$
DECLARE
  v_hospital_id    uuid;
  v_total_oes      integer := 639;
  v_total_core     integer;
  v_scored         integer;
  v_sum            numeric;
  v_overall_pct    numeric;
  v_core_failures  integer;  -- CORE OEs scored < 4
  v_core_unscored  integer;  -- CORE OEs not scored at all
  v_core_total_failures integer; -- scored <4 + unscored
  v_chapter_min    numeric;
  v_std_violations integer;
  v_chapter_breakdown jsonb;

  v_rule1_pass    boolean;
  v_rule2_pass    boolean;
  v_rule3_pass    boolean;
  v_rule4_pass    boolean;

  v_kpi_tracked   integer;
  v_kpi_total     integer;
  v_kpi_pct       numeric;
  v_kpi_ready     boolean;

  v_comm_active   integer;
  v_comm_ready    boolean;

  v_audit_done    integer;
  v_audit_total   integer := 35;
  v_audit_ready   boolean;

  v_oe_pass       boolean;
  v_all_pass      boolean;
  v_verdict       text;
  v_readiness     text;
BEGIN
  SELECT hospital_id INTO v_hospital_id
  FROM assessments WHERE id = param_id;

  -- Total CORE OEs
  SELECT count(*) INTO v_total_core
  FROM objective_elements WHERE level = 'CORE';

  -- Rule 1: CORE OEs scored < 4
  SELECT count(*) INTO v_core_failures
  FROM scores s
  JOIN objective_elements oe ON oe.id = s.oe_id
  WHERE s.assessment_id = param_id
    AND oe.level = 'CORE'
    AND s.score < 4;

  -- CORE OEs not scored at all (missing = failure)
  SELECT count(*) INTO v_core_unscored
  FROM objective_elements oe
  WHERE oe.level = 'CORE'
    AND NOT EXISTS (
      SELECT 1 FROM scores s
      WHERE s.assessment_id = param_id AND s.oe_id = oe.id
    );

  v_core_total_failures := v_core_failures + v_core_unscored;
  v_rule1_pass := (v_core_total_failures = 0);

  -- Rule 2: Overall >= 80%
  SELECT coalesce(sum(s.score), 0), count(*)
  INTO v_sum, v_scored
  FROM scores s WHERE s.assessment_id = param_id;
  v_overall_pct := round((v_sum / (v_total_oes * 5.0)) * 100, 1);
  v_rule2_pass := (v_overall_pct >= 80);

  -- Rule 3: Every chapter average >= 80%
  SELECT min(chapter_pct) INTO v_chapter_min
  FROM (
    SELECT oe.chapter_id,
           round((sum(s.score)::numeric / (
             SELECT count(*) FROM objective_elements oe2 WHERE oe2.chapter_id = oe.chapter_id
           ) / 5.0) * 100, 1) AS chapter_pct
    FROM scores s
    JOIN objective_elements oe ON oe.id = s.oe_id
    WHERE s.assessment_id = param_id
    GROUP BY oe.chapter_id
  ) t;
  v_rule3_pass := coalesce(v_chapter_min >= 80, false);

  -- Rule 4: No OE scored <= 2
  SELECT count(*) INTO v_std_violations
  FROM scores s WHERE s.assessment_id = param_id AND s.score <= 2;
  v_rule4_pass := (v_std_violations = 0);

  -- Chapter breakdown
  SELECT jsonb_object_agg(chapter_id, chapter_pct)
  INTO v_chapter_breakdown
  FROM (
    SELECT oe.chapter_id,
           round((sum(s.score)::numeric / (
             SELECT count(*) FROM objective_elements oe2 WHERE oe2.chapter_id = oe.chapter_id
           ) / 5.0) * 100, 1) AS chapter_pct
    FROM scores s
    JOIN objective_elements oe ON oe.id = s.oe_id
    WHERE s.assessment_id = param_id
    GROUP BY oe.chapter_id
  ) t;

  v_oe_pass := v_rule1_pass AND v_rule2_pass AND v_rule3_pass AND v_rule4_pass;

  -- KPI Tracking (HCO Full only — exclude ELC-scoped rows, kpi_no 51-64)
  SELECT count(*) INTO v_kpi_total FROM kpis
  WHERE NOT (coalesce(programme_scope, '{}'::text[]) && array['HCO_ELC','SHCO_ELC']);
  SELECT count(distinct kpi_id) INTO v_kpi_tracked
  FROM (
    SELECT kpi_id, count(*) AS months
    FROM kpi_data WHERE hospital_id = v_hospital_id
    GROUP BY kpi_id HAVING count(*) >= 3
  ) k;
  v_kpi_pct := CASE WHEN v_kpi_total > 0
    THEN round((v_kpi_tracked::numeric / v_kpi_total::numeric) * 100, 1) ELSE 0 END;
  v_kpi_ready := (v_kpi_pct >= 80);

  -- Committees
  SELECT count(distinct committee_id) INTO v_comm_active
  FROM committee_meetings
  WHERE hospital_id = v_hospital_id
    AND meeting_date >= now() - interval '12 months';
  v_comm_ready := (v_comm_active >= 20);

  -- Audits
  SELECT count(distinct audit_id) INTO v_audit_done
  FROM audit_records
  WHERE hospital_id = v_hospital_id
    AND status = 'completed'
    AND audit_date >= now() - interval '12 months';
  v_audit_ready := (v_audit_done >= 20);

  -- Final verdict
  v_all_pass := v_oe_pass AND v_kpi_ready AND v_comm_ready AND v_audit_ready;

  IF v_all_pass THEN
    v_verdict := 'PASS'; v_readiness := 'READY';
  ELSIF v_oe_pass THEN
    v_verdict := 'PARTIAL'; v_readiness := 'RISKY';
  ELSIF NOT v_rule1_pass THEN
    v_verdict := 'FAIL'; v_readiness := 'NOT READY';
  ELSE
    v_verdict := 'FAIL'; v_readiness := 'NOT READY';
  END IF;

  RETURN jsonb_build_object(
    'verdict',            v_verdict,
    'readiness',          v_readiness,
    'core_pass',          v_rule1_pass,
    'core_failures',      v_core_total_failures, -- total: scored<4 + unscored
    'core_scored_failures', v_core_failures,     -- only scored ones below 4
    'core_unscored',      v_core_unscored,       -- not scored at all
    'total_core',         v_total_core,
    'overall_pct',        v_overall_pct,
    'overall_pass',       v_rule2_pass,
    'chapter_pass',       v_rule3_pass,
    'standards_pass',     v_rule4_pass,
    'scored_count',       v_scored,
    'total_oes',          v_total_oes,
    'chapter_breakdown',  coalesce(v_chapter_breakdown, '{}'::jsonb),
    'kpi_tracked',        v_kpi_tracked,
    'kpi_total',          v_kpi_total,
    'kpi_pct',            v_kpi_pct,
    'kpi_ready',          v_kpi_ready,
    'comm_active',        v_comm_active,
    'comm_ready',         v_comm_ready,
    'audit_done',         v_audit_done,
    'audit_total',        v_audit_total,
    'audit_ready',        v_audit_ready,
    'rule1_core',         v_rule1_pass,
    'rule2_overall',      v_rule2_pass,
    'rule3_chapters',     v_rule3_pass,
    'rule4_standards',    v_rule4_pass
  );
END;
$function$;
