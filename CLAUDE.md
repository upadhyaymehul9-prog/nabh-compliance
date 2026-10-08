# CLAUDE.md

## Session Start Rule

At the start of every session, first check the current branch:

```
git branch --show-current
```

- If it says `master`: run `git pull origin master` as before.
- If it says anything else (a feature branch): do NOT run `git pull origin master` — that merges master straight into the feature branch and causes conflicts. Instead run `git fetch origin master` only, and tell Mk if master has moved ahead, without merging it in.

## Workflow Rule — Local-First, Always

1. Every new change is built and kept LOCAL first.
2. Test locally (`npm start`, verify on localhost:3000) — confirm everything works.
3. Only after local testing passes do we move to the next level (deploy via `npm run deploy`).
4. NEVER deploy untested code. NEVER `npm run deploy` before local verification.
5. Build complete → test local → confirm OK → then and only then deploy.

This rule applies to every task in this repo from now on.

## Post-Deploy Rule

After every successful `npm run deploy`, automatically run:

```
git add src/ public/ supabase/functions/ scripts/ && git commit -m "deploy: auto-sync" && git push origin master
```

Never use `git add .` in auto-sync — it can stage secrets from `.claude/settings.local.json` or other untracked sensitive files.

## Master Policy Drafting Rule

Before drafting ANY SHCO master policy, read the standing rules at the top of `scripts/master-policy-todos.md` — in particular **"STANDING RULE: Two-tier depth (added 2026-08-10)"**, which sets how much depth each objective element gets (Tier 1 full treatment only for asterisked OEs, Tier 2 for the rest). That file is also where deferred content and open reconciliation items are logged. Read it first; do not start drafting from memory of how a previous standard was built.

## Records/SOPs/Policy Delivery Rule — Git ≠ Live

Editing a Records, SOP, or Policy .docx under `policies/build/` and pushing to git does **NOT** update what accredready.in actually serves for download. The live app delivers these files from **Supabase Storage** (`policy-masters-v2` and `policy-masters-hco-v2` buckets), read by the `download-v2-policy` / `download-v2-hco-document` edge functions — never by reading the git repo directly.

After fixing any file under `policies/build/`, find its storage path first:

```sql
SELECT name, bucket_id, updated_at FROM storage.objects WHERE name ILIKE '%<filename or code>%';
```

Then re-upload it to that exact path with `policies/build/upload_storage_file.py` (needs `SUPABASE_SERVICE_ROLE_KEY` set):

```
python policies\build\upload_storage_file.py --bucket <bucket> --path "<storage path>" --file "<local corrected file>"
```

Git push + Storage upload are two separate steps — always do both, or the fix never reaches a live download. This was missed once (Oct 2026, SOP_Emergency_Triage.docx) before being caught by Mk downloading the live file and finding it still old.

## NABH DATA ACCURACY RULES

- Never mention specific OE counts in any public SEO page or marketing content
- Never mention specific standard counts per chapter
- Only the app (`src/App.js`) may reference specific OE numbers as they come from Supabase
- Correct validity periods: HCO Full = 4 years, HCO ELC = 2 years, SHCO Full = 4 years (confirmed from official NABH documents), SHCO ELC = 2 years
- Correct programme names: HCO Full Accreditation, HCO Entry Level Certification (ELC), SHCO Full Accreditation, SHCO Entry Level Certification
- AccredReady covers multiple NABH programmes — never position it as HCO-only or 6th Edition only
- When in doubt about any NABH number — do not include it
