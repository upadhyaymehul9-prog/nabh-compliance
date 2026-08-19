-- Set master_docx_path for FMS.1–FMS.5 after uploading v2 masters to Storage.
-- Prerequisite: provision_v2_fms_masters.py --upload (or manual upload to same paths).
-- Does not change status, version, or any v1 content field.

update public.shco_policy_masters set master_docx_path = 'FMS/FMS.1_v2.docx' where standard_code = 'FMS.1';
update public.shco_policy_masters set master_docx_path = 'FMS/FMS.2_v2.docx' where standard_code = 'FMS.2';
update public.shco_policy_masters set master_docx_path = 'FMS/FMS.3_v2.docx' where standard_code = 'FMS.3';
update public.shco_policy_masters set master_docx_path = 'FMS/FMS.4_v2.docx' where standard_code = 'FMS.4';
update public.shco_policy_masters set master_docx_path = 'FMS/FMS.5_v2.docx' where standard_code = 'FMS.5';

select standard_code, master_docx_path, status, version
from public.shco_policy_masters
where standard_code like 'FMS.%'
order by standard_code;
