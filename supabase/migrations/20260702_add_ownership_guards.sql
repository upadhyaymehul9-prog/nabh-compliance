-- Migration: Add ownership guards + search_path to SECURITY DEFINER functions
-- Date: 2 July 2026
-- Rollback: supabase/migrations/20260702_snapshot_security_definer_functions.sql (commit 5f9294a)
--
-- Closes 3 authorization holes (get_pillar_readiness, get_final_decision, get_active_gaps)
-- + 1 minor leak (get_score_impact). Guards only — business logic is byte-identical.
-- Also folds SET search_path TO 'public' into all SECURITY DEFINER functions (linter hardening).

-- =====================================================================
-- 1. get_pillar_readiness  (plpgsql — RAISE guard)
-- =====================================================================
CREATE OR REPLACE FUNCTION public.get_pillar_readiness(p_hospital_id uuid, p_assessment_id uuid)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'public'
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
  -- Ownership check: caller must belong to the requested hospital
  IF NOT EXISTS (
    SELECT 1 FROM profiles
    WHERE id = auth.uid() AND hospital_id = p_hospital_id
  ) THEN
    RAISE EXCEPTION 'Access denied';
  END IF;
  select count(distinct kpi_id)
  into v_kpi_count
  from (
    select kpi_id, count(*) as months
    from kpi_data
    where hospital_id = p_hospital_id
    group by kpi_id
    having count(*) >= 3
  ) k;
  select count(*) into v_kpi_total from kpis;
  select count(distinct committee_id)
  into v_committee_count
  from committee_meetings
  where hospital_id = p_hospital_id
    and meeting_date >= now() - interval '12 months';
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

-- =====================================================================
-- 2. get_final_decision  (plpgsql — RAISE guard)
-- =====================================================================
CREATE OR REPLACE FUNCTION public.get_final_decision(param_id uuid)
 RETURNS jsonb
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
DECLARE
  v_hospital_id    uuid;
  v_total_oes      integer := 639;
  v_total_core     integer;
  v_scored         integer;
  v_sum            numeric;
  v_overall_pct    numeric;
  v_core_failures  integer;
  v_core_unscored  integer;
  v_core_total_failures integer;
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

  -- Ownership check: caller must belong to the assessment's hospital
  IF NOT EXISTS (
    SELECT 1 FROM profiles
    WHERE id = auth.uid() AND hospital_id = v_hospital_id
  ) THEN
    RAISE EXCEPTION 'Access denied';
  END IF;

  SELECT count(*) INTO v_total_core
  FROM objective_elements WHERE level = 'CORE';
  SELECT count(*) INTO v_core_failures
  FROM scores s
  JOIN objective_elements oe ON oe.id = s.oe_id
  WHERE s.assessment_id = param_id
    AND oe.level = 'CORE'
    AND s.score < 4;
  SELECT count(*) INTO v_core_unscored
  FROM objective_elements oe
  WHERE oe.level = 'CORE'
    AND NOT EXISTS (
      SELECT 1 FROM scores s
      WHERE s.assessment_id = param_id AND s.oe_id = oe.id
    );
  v_core_total_failures := v_core_failures + v_core_unscored;
  v_rule1_pass := (v_core_total_failures = 0);
  SELECT coalesce(sum(s.score), 0), count(*)
  INTO v_sum, v_scored
  FROM scores s WHERE s.assessment_id = param_id;
  v_overall_pct := round((v_sum / (v_total_oes * 5.0)) * 100, 1);
  v_rule2_pass := (v_overall_pct >= 80);
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
  SELECT count(*) INTO v_std_violations
  FROM scores s WHERE s.assessment_id = param_id AND s.score <= 2;
  v_rule4_pass := (v_std_violations = 0);
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
  SELECT count(*) INTO v_kpi_total FROM kpis;
  SELECT count(distinct kpi_id) INTO v_kpi_tracked
  FROM (
    SELECT kpi_id, count(*) AS months
    FROM kpi_data WHERE hospital_id = v_hospital_id
    GROUP BY kpi_id HAVING count(*) >= 3
  ) k;
  v_kpi_pct := CASE WHEN v_kpi_total > 0
    THEN round((v_kpi_tracked::numeric / v_kpi_total::numeric) * 100, 1) ELSE 0 END;
  v_kpi_ready := (v_kpi_pct >= 80);
  SELECT count(distinct committee_id) INTO v_comm_active
  FROM committee_meetings
  WHERE hospital_id = v_hospital_id
    AND meeting_date >= now() - interval '12 months';
  v_comm_ready := (v_comm_active >= 20);
  SELECT count(distinct audit_id) INTO v_audit_done
  FROM audit_records
  WHERE hospital_id = v_hospital_id
    AND status = 'completed'
    AND audit_date >= now() - interval '12 months';
  v_audit_ready := (v_audit_done >= 20);
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
    'core_failures',      v_core_total_failures,
    'core_scored_failures', v_core_failures,
    'core_unscored',      v_core_unscored,
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

-- =====================================================================
-- 3. get_active_gaps  (sql — WHERE-EXISTS guard, returns empty set)
-- =====================================================================
CREATE OR REPLACE FUNCTION public.get_active_gaps(param_id uuid)
 RETURNS TABLE(oe_id text, chapter_id text, standard_id text, level text, oe_text text, doc_required boolean, score integer, severity text, priority_score integer, message text, has_evidence boolean, doc_gap boolean, capa_status text, gap_closed boolean)
 LANGUAGE sql
 SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
  select
    sc.oe_id, oe.chapter_id, oe.standard_id, oe.level, oe.text,
    oe.doc_required, sc.score,
    case when oe.level='CORE' and sc.score<4 then 'CRITICAL'
         when sc.score<=2 then 'HIGH'
         when sc.score=3  then 'MEDIUM'
         else 'LOW' end as severity,
    (case oe.level when 'CORE' then 50 else 0 end
     + case when sc.score=1 then 30 when sc.score=2 then 20 when sc.score=3 then 10 else 0 end
     + case when oe.doc_required and not exists(
         select 1 from evidence ev where ev.oe_id=sc.oe_id and ev.assessment_id=sc.assessment_id
       ) then 15 else 0 end) as priority_score,
    case when oe.level='CORE' and sc.score=1 then 'CORE NON-COMPLIANT: No evidence. Failure guaranteed.'
         when oe.level='CORE' and sc.score=2 then 'CORE CRITICAL: Partial compliance. Will cause failure.'
         when oe.level='CORE' and sc.score=3 then 'CORE WARNING: Not consistently monitored.'
         when sc.score=1 then 'Non-compliant: No evidence. Immediate action required.'
         when sc.score=2 then 'High risk: Inconsistent implementation.'
         when sc.score=3 then 'Moderate: Documentation gaps exist.'
         when sc.score=4 and oe.doc_required then 'Compliant — attach evidence link for assessor.'
         else 'Minor gap: Near compliant.' end as message,
    exists(select 1 from evidence ev where ev.oe_id=sc.oe_id and ev.assessment_id=sc.assessment_id) as has_evidence,
    (oe.doc_required and not exists(select 1 from evidence ev where ev.oe_id=sc.oe_id and ev.assessment_id=sc.assessment_id)) as doc_gap,
    coalesce((select cp.status from capa cp where cp.oe_id=sc.oe_id and cp.assessment_id=sc.assessment_id order by cp.created_at desc limit 1),'none') as capa_status,
    (sc.score>=4 and exists(select 1 from capa cp where cp.oe_id=sc.oe_id and cp.assessment_id=sc.assessment_id and cp.status='completed')) as gap_closed
  from scores sc
  join objective_elements oe on oe.id=sc.oe_id
  where sc.assessment_id=param_id
    and exists (
      select 1 from assessments a
      join profiles p on p.hospital_id = a.hospital_id
      where a.id = param_id and p.id = auth.uid()
    )
    and (
      sc.score<4
      or (sc.score=4 and oe.doc_required and not exists(
        select 1 from evidence ev where ev.oe_id=sc.oe_id and ev.assessment_id=sc.assessment_id
      ))
    )
  order by priority_score desc, sc.score asc;
$function$;

-- =====================================================================
-- 4. get_score_impact  (sql — CASE-wrapped guard, returns null)
-- =====================================================================
CREATE OR REPLACE FUNCTION public.get_score_impact(param_assessment uuid, param_oe text, param_score integer)
 RETURNS jsonb
 LANGUAGE sql
 SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
  select case when exists (
    select 1 from assessments a
    join profiles p on p.hospital_id = a.hospital_id
    where a.id = param_assessment and p.id = auth.uid()
  ) then
  jsonb_build_object(
    'oe_id',      param_oe,
    'new_score',  param_score,
    'level',      (select level from objective_elements where id=param_oe),
    'chapter',    (select chapter_id from objective_elements where id=param_oe),
    'standard',   (select standard_id from objective_elements where id=param_oe),
    'alerts',     (
      select jsonb_agg(alert) from (
        select jsonb_build_object('type','CORE_FAILURE','severity','CRITICAL',
          'message', format('CORE FAILURE at %s (score %s/5).', param_oe, param_score)) as alert
        where (select level from objective_elements where id=param_oe)='CORE' and param_score < 4
        union all
        select jsonb_build_object('type','CORE_RESOLVED','severity','SUCCESS',
          'message', format('CORE element %s is now compliant (%s/5).', param_oe, param_score)) as alert
        where (select level from objective_elements where id=param_oe)='CORE' and param_score >= 4
        union all
        select jsonb_build_object('type','STANDARD_VIOLATION','severity','HIGH',
          'message', format('Standard %s has major non-conformity (score %s/5).', (select standard_id from objective_elements where id=param_oe), param_score)) as alert
        where param_score <= 2
        union all
        select jsonb_build_object('type','DOC_MISSING','severity','MEDIUM',
          'message', format('%s requires documentation but none uploaded.', param_oe)) as alert
        where (select doc_required from objective_elements where id=param_oe)=true
          and not exists(select 1 from evidence where oe_id=param_oe and assessment_id=param_assessment)
      ) alerts_sub
    )
  )
  else null end;
$function$;

-- =====================================================================
-- 5. search_path hardening on remaining SECURITY DEFINER functions
--    (safe triggers / self-only — no ownership guards needed)
-- =====================================================================
ALTER FUNCTION public.delete_user() SET search_path TO 'public';
ALTER FUNCTION public.fn_log_score() SET search_path TO 'public';
ALTER FUNCTION public.fn_capture_history() SET search_path TO 'public';
ALTER FUNCTION public.fn_log_evidence() SET search_path TO 'public';
ALTER FUNCTION public.fn_log_capa() SET search_path TO 'public';
ALTER FUNCTION public.handle_new_hospital() SET search_path TO 'public';
