# CLAUDE.md

## Session Start Rule

At the start of every session, always run:

```
git pull origin master
```

## Post-Deploy Rule

After every successful `npm run deploy`, automatically run:

```
git add . && git commit -m "deploy: auto-sync" && git push origin master
```

## NABH DATA ACCURACY RULES

- Never mention specific OE counts in any public SEO page or marketing content
- Never mention specific standard counts per chapter
- Only the app (`src/App.js`) may reference specific OE numbers as they come from Supabase
- Correct validity periods: HCO Full = 4 years, HCO ELC = 2 years, SHCO Full = 4 years (confirmed from official NABH documents), SHCO ELC = 2 years
- Correct programme names: HCO Full Accreditation, HCO Entry Level Certification (ELC), SHCO Full Accreditation, SHCO Entry Level Certification
- AccredReady covers multiple NABH programmes — never position it as HCO-only or 6th Edition only
- When in doubt about any NABH number — do not include it
