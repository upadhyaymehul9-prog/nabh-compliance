# Deployment

AccredReady deploys the React frontend to **GitHub Pages** at [https://accredready.in](https://accredready.in). Supabase (database and edge functions) is deployed separately.

---

## Local-first workflow

Every change follows this order (enforced in [CLAUDE.md](../CLAUDE.md)):

```
1. Build locally
2. Test locally (npm start → localhost:3000)
3. Confirm everything works
4. Deploy (npm run deploy)
5. Post-deploy git sync
```

**Never deploy untested code.**

---

## Development

```bash
git pull origin master
npm install
npm start
```

Open [http://localhost:3000](http://localhost:3000). The dev server hot-reloads on file changes.

---

## Production build

```bash
npm run build
```

Output goes to `build/`. This is a standard CRA production build — minified, hashed filenames, optimised bundles.

Test the production build locally before deploying:

```bash
npx serve -s build
```

---

## Deploy to GitHub Pages

```bash
npm run deploy
```

This runs `predeploy` (which calls `npm run build`) then publishes the `build/` folder via `gh-pages`.

Configuration in `package.json`:

- `"homepage": "https://accredready.in"` — asset paths and canonical URL
- `"deploy": "gh-pages -d build"` — publish target

The `public/CNAME` file sets the custom domain.

### What deploys

| Included | Not included |
|----------|--------------|
| CRA build output (`build/`) | Supabase migrations |
| Static HTML from `public/` (copied into build) | Edge function deployments |
| `sitemap.xml`, `robots.txt`, favicons | Database changes |

Static SEO pages in `public/` (landing pages, learn hub, blog) are copied into the build by CRA and served alongside the React app.

---

## Post-deploy auto-sync

After every successful `npm run deploy`, run:

```bash
git add src/ public/ supabase/functions/ scripts/
git commit -m "deploy: auto-sync"
git push origin master
```

**Never use `git add .`** — it can stage secrets from `.claude/settings.local.json` or other untracked sensitive files.

---

## Supabase deployment

Database and edge functions are **not** part of `npm run deploy`.

### Migrations

Apply new migrations via the Supabase SQL Editor or CLI:

```bash
supabase db push
```

### Edge functions

Deploy individual functions after changes:

```bash
supabase functions deploy ai-assistant
supabase functions deploy generate-hospital-policy
supabase functions deploy generate-policy-document
supabase functions deploy backfill-embeddings
```

Secrets (Anthropic API key, service role key) are configured in the Supabase dashboard under Project Settings → Edge Functions.

---

## Domain and hosting

| Item | Value |
|------|-------|
| Domain | `accredready.in` |
| Hosting | GitHub Pages |
| DNS | CNAME → GitHub Pages (see `public/CNAME`) |
| Backend | Supabase (`tbptllgcjtiiqspxqcde.supabase.co`) |

---

## Standalone micro-apps

Some tools in `public/` are pre-built standalone apps with their own bundled assets:

- `public/revenue-leakage-review/` — Revenue Leakage Self-Audit
- `public/marketing-leakage-check-for-healthcare/` — Marketing leakage check

These are committed as built assets. Rebuild them in their source projects if changes are needed, then copy the output into `public/`.

---

## Troubleshooting

| Problem | Check |
|---------|-------|
| Blank page after deploy | `homepage` in package.json matches domain; check browser console for 404 on JS/CSS |
| Routes 404 on refresh | GitHub Pages serves `404.html` redirect (CRA default) — verify `public/404.html` exists |
| App works locally but not deployed | Run `npm run build` locally and test with `npx serve -s build` |
| Supabase errors in production | RLS policies applied? See [security.md](security.md) |
| Edge function CORS errors | `ai-assistant` CORS is locked to `accredready.in` — test from production domain |
