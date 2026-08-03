-- Adds a structured OE-to-content cross-reference to each master policy, so a
-- hospital admin or NABH assessor can see at a glance which OE each part of
-- the document addresses, instead of having to read the whole document to
-- figure out where (say) HIC.2.c is covered.
--
-- Shape: array of { oe_code, requirement, steps } — "steps" is a short
-- human-readable pointer like "Steps 15-19", not a foreign key, since the
-- procedure_steps array doesn't have stable IDs.

alter table public.shco_policy_masters
  add column if not exists oe_mapping jsonb;

comment on column public.shco_policy_masters.oe_mapping is
  'Array of {oe_code, requirement, steps} — maps each OE this standard covers to where it is addressed in procedure_steps, e.g. [{"oe_code":"HIC.2.a","requirement":"Standard precautions","steps":"Step 2"}, ...]';
