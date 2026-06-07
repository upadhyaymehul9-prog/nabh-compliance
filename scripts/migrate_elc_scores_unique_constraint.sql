-- Migration: update elc_scores unique constraint to include programme
-- Run in Supabase SQL Editor after migrate_elc_scores_programme.sql

-- Drop the old unique constraint (adjust name if different — check via: \d elc_scores)
ALTER TABLE elc_scores DROP CONSTRAINT IF EXISTS elc_scores_hospital_id_oe_code_key;

-- Add new unique constraint covering hospital_id + oe_code + programme
ALTER TABLE elc_scores ADD CONSTRAINT elc_scores_hospital_id_oe_code_programme_key
  UNIQUE (hospital_id, oe_code, programme);
