# CLAUDE.md

## Post-Deploy Rule

After every successful `npm run deploy`, automatically run:

```
git add . && git commit -m "deploy: auto-sync" && git push origin master
```
