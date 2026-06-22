# CLAUDE.md

## Session Start Rule

At the start of every session, always run:

```
git pull origin master
```

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

## NABH DATA ACCURACY RULES

- Never mention specific OE counts in any public SEO page or marketing content
- Never mention specific standard counts per chapter
- Only the app (`src/App.js`) may reference specific OE numbers as they come from Supabase
- Correct validity periods: HCO Full = 4 years, HCO ELC = 2 years, SHCO Full = 4 years (confirmed from official NABH documents), SHCO ELC = 2 years
- Correct programme names: HCO Full Accreditation, HCO Entry Level Certification (ELC), SHCO Full Accreditation, SHCO Entry Level Certification
- AccredReady covers multiple NABH programmes — never position it as HCO-only or 6th Edition only
- When in doubt about any NABH number — do not include it
