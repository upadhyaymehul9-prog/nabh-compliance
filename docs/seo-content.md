# SEO Content

AccredReady publishes static HTML pages for search engine visibility, lead generation, and educational content about NABH accreditation. These pages deploy alongside the React app via GitHub Pages.

**Sitemap:** [public/sitemap.xml](../public/sitemap.xml)

---

## Content rules

From [CLAUDE.md](../CLAUDE.md) — **NABH data accuracy rules**:

| Rule | Detail |
|------|--------|
| No OE counts on public pages | Never mention specific objective element counts in SEO or marketing content |
| No standard counts per chapter | Do not publish chapter-level standard counts |
| OE numbers in app only | Only `src/App.js` may reference specific OE numbers (from Supabase) |
| Validity periods | HCO Full = 4 years, HCO ELC = 2 years, SHCO Full = 4 years, SHCO ELC = 2 years |
| Programme names | Use official names: HCO Full Accreditation, HCO Entry Level Certification (ELC), SHCO Full Accreditation, SHCO Entry Level Certification |
| Multi-programme positioning | AccredReady covers multiple NABH programmes — never position as HCO-only or 6th Edition only |
| When in doubt | Do not include the number |

These rules apply to all files in `public/`, `marketing/`, and any external content.

---

## Page inventory

### App entry

| File | Purpose |
|------|---------|
| `public/index.html` | CRA shell + rich SEO meta, JSON-LD `SoftwareApplication`, embedded resources |
| `public/404.html` | GitHub Pages SPA redirect |
| `public/CNAME` | Custom domain (`accredready.in`) |
| `public/robots.txt` | Crawler directives |
| `public/sitemap.xml` | URL index (~65 URLs) |

### Product landing pages (~30)

Programme-specific and feature landing pages:

| Examples | Topic |
|----------|-------|
| `nabh-accreditation-software.html` | Main product landing |
| `shco-accreditation-software.html` | SHCO Full programme |
| `nabh-elc-software.html` | Entry Level Certification |
| `eco-accreditation-software.html` | Eye Care Organisation |
| `nabh-6th-edition-checklist.html` | HCO 6th Edition |
| `nabh-shco-checklist.html` | SHCO checklist |
| `nabh-affordable-software.html` | Pricing positioning |
| `nabh-software-vs-excel.html` | Comparison content |
| `nabh-consultant-vs-software.html` | Comparison content |

Topic-specific pages cover infection control, KPIs, mock drills, internal audit, linen management, clinical audit, committee lists, and more.

### Learn hub (`public/learn/` — 19 articles)

Educational content hub with index at `public/learn/index.html`:

| Examples | Topic |
|----------|-------|
| `nabh-programmes-comparison.html` | Programme comparison guide |
| `nabh-gap-analysis.html` | Gap analysis methodology |
| `nabh-kpi-tracking.html` | KPI tracking guide |
| `nabh-shco-standards.html` | SHCO standards overview |
| `nabh-accreditation-timeline.html` | Accreditation timeline |
| `hospital-revenue-leakage-guide.html` | Revenue leakage for hospitals |
| `hospital-marketing-guide-india.html` | Hospital marketing in India |
| `local-seo-for-hospitals-clinics.html` | Local SEO guide |

### Blog (`public/blog/` — 6 posts)

| File | Topic |
|------|-------|
| `nabh-accreditation-preparation-guide.html` | Preparation guide |
| `nabh-hospital-infection-control.html` | Infection control |
| `nabh-internal-audit-checklist.html` | Internal audit |
| `nabh-kpi-indicators.html` | KPI indicators |
| `nabh-pre-patient-rights.html` | Patient rights |
| `importance-of-nabh-accreditation.html` | Accreditation importance |

### Legal and utility

| File | Purpose |
|------|---------|
| `terms.html` | Terms of service |
| `privacy.html` | Privacy policy |
| `delete-account.html` | Account deletion instructions |

### Standalone micro-apps

| Path | Purpose |
|------|---------|
| `public/revenue-leakage-review/` | Revenue Leakage Self-Audit (pre-built Vite app) |
| `public/marketing-leakage-check-for-healthcare/` | Marketing leakage check tool |
| `public/clinic-revenue-retention.html` | Clinic revenue retention landing |
| `public/healthcare-ecosystem.html` | Healthcare ecosystem page |

---

## Marketing folder

`marketing/` holds internal strategy documents — not served by the web app:

| Path | Purpose |
|------|---------|
| `marketing/STRATEGY.md` | Overall marketing strategy |
| `marketing/FIRST-10-CUSTOMERS.md` | Early customer acquisition plan |
| `marketing/WEEK1-OUTREACH.md` | Outreach plan |
| `marketing/linkedin/` | LinkedIn automation and profile updates |
| `marketing/video/` | Promo video scripts and CapCut guide |
| `marketing/reports/` | Weekly marketing reports |

---

## Adding new SEO pages

1. Create the HTML file in `public/` (or `public/learn/` / `public/blog/` as appropriate)
2. Follow NABH accuracy rules above — no specific OE or standard counts
3. Add the URL to `public/sitemap.xml`
4. Link from related existing pages where natural
5. Test locally: `npm start` serves `public/` assets
6. Deploy via standard workflow (see [deployment.md](deployment.md))

### Page structure conventions

Existing landing pages follow a consistent pattern:

- Semantic HTML with proper heading hierarchy (single H1)
- Meta description and Open Graph tags
- Internal links to related learn/blog articles and the main app
- Clear CTA to sign up or try AccredReady
- Mobile-responsive layout (inline CSS or shared patterns from existing pages)

Copy an existing page in the same category as a template rather than starting from scratch.

---

## Content reference files (root)

These markdown files hold curated NABH reference content used during development — not published directly:

| File | Content |
|------|---------|
| `shco_general_info_content.md` | SHCO general information |
| `shco_kpi_content.md` | SHCO KPI content |
| `shco_quality_tools_content.md` | Quality tools content |
| `shco_medication_error_content.md` | Medication error content |

Do not copy specific counts from these into public SEO pages.
