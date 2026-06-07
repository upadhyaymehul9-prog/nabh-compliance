-- Migration: add programme column to elc_scores to distinguish HCO ELC vs SHCO ELC scores
-- Run once in Supabase SQL Editor

ALTER TABLE elc_scores ADD COLUMN IF NOT EXISTS programme TEXT DEFAULT 'HCO_ELC';
UPDATE elc_scores SET programme = 'HCO_ELC' WHERE programme IS NULL;
