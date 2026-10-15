# AccredReady — World-Class Design System
### "Audit-Grade" Design Language · v1.0 · June 2026

**Design thesis:** Every pixel should feel like it would survive an NABH assessor's scrutiny. The aesthetic of a flawless compliance scorecard — clinical white, verified green, monospaced OE codes — elevated to premium product design. Trust through precision, not decoration.

**Deliberate rejections:** No dark mode (every generic SaaS does it; hospitals work in bright wards). No glassmorphism (reads consumer-app, not clinical). No abstract 3D shapes (this audience distrusts vagueness). The risk we take instead: real product data as the hero visual, and a scorecard motif running through the entire site.

---

## 1. Color System

| Token | Hex | Usage |
|---|---|---|
| `--ink` | `#0B1B2B` | Headlines, nav, footer background. Deep clinical navy — evolved from your existing #040d1a |
| `--paper` | `#FBFDFD` | Page background. Cool clinical white, never pure grey |
| `--verify` | `#0E8A5F` | Primary actions, "Met" status, score ring. The green of a passed audit |
| `--verify-dark` | `#0A6B4A` | Button hover, link hover |
| `--signal` | `#D97706` | "Partial" status, warnings, trial countdown. Use sparingly |
| `--alert` | `#DC2626` | "Not Met" status only. Never decorative |
| `--slate` | `#4B5D6E` | Body text, secondary labels |
| `--hairline` | `#DCE6E4` | Borders, dividers, table rules |
| `--mint-tint` | `#EBF4F0` | Section backgrounds, chip fills, ring track |

**Rules:** Green is earned — it marks verified things (Met OEs, CTAs, checkmarks), never decoration. Red appears only as "Not Met" data. Max 2 accent colors visible per viewport.

## 2. Typography

| Role | Font | Weights | Usage |
|---|---|---|---|
| Display | **Bricolage Grotesque** | 600, 700 | Headlines only. Characterful without being playful |
| Body | **IBM Plex Sans** | 400, 500, 600 | All UI and paragraph text. Engineered, clinical credibility |
| Data | **IBM Plex Mono** | 400, 500 | OE codes (AAC.1.a), scores, counts, table data |

The mono font for OE codes is the signature typographic move — OE codes ARE identifiers, and rendering them as code signals "this system is precise." Google Fonts, all free.

**Type scale (desktop / mobile):**
- H1: 56px/40px, Bricolage 700, line-height 1.05, letter-spacing -0.02em
- H2: 36px/28px, Bricolage 600, lh 1.15
- H3: 24px/20px, Bricolage 600
- Body-L: 19px/17px, Plex Sans 400, lh 1.6
- Body: 16px/15px, Plex Sans 400, lh 1.6
- Caption/Data: 13px, Plex Mono 400, letter-spacing 0.02em, often uppercase

## 3. Components

**Buttons**
- Primary: `--verify` bg, white text, 12px radius, 16px/28px padding, Plex Sans 600 16px. Hover: `--verify-dark` + translateY(-1px) + shadow `0 6px 16px rgba(14,138,95,.25)`
- Secondary: transparent, 1.5px `--ink` border, `--ink` text. Hover: `--mint-tint` fill
- Ghost: `--verify` text only, underline on hover

**Status chips (the system's recurring motif)**
- Met: `--mint-tint` bg, `--verify` text · Partial: `#FCF0DF` bg, `--signal` text · Not Met: `#FDEAEA` bg, `--alert` text
- 8px radius, Plex Mono 12px 500, 4px/10px padding, leading dot (●)

**Cards:** white bg, 1px `--hairline` border, 16px radius, shadow `0 1px 3px rgba(11,27,43,.06)`. Hover (interactive only): border becomes `--verify` at 40%, shadow deepens.

**Score ring:** conic-gradient `--verify` on `--mint-tint` track, center number in Bricolage 700.

## 4. Homepage Layout Blueprint

1. **Nav** — white, hairline bottom border. Logo left · Features / Pricing / Resources / Blog · "Sign in" ghost + "Start free trial" primary. Sticky, gains shadow on scroll.
2. **HERO** — two-column 55/45. Left: eyebrow chip `NABH 6TH EDITION · 639 OEs`, H1 "Walk into your NABH assessment already knowing the verdict.", subhead, dual CTA, founder trust-line. Right: **the live scorecard** (readiness ring + chapter bars + status chips + verdict line). Faint 24px grid pattern in background — evokes a checklist, at 3% opacity.
3. **Logo/Trust strip** — "Used by quality teams across India" + hospital names/count + Play Store badge. Mono font, quiet.
4. **The Verdict Engine** (signature section) — 3 steps shown as one continuous audit trail line connecting: Score your OEs → See gaps with 4 fix-tips each → Generate the report. Each step is a product screenshot crop in a card.
5. **Feature grid** — 3×2. Each card: mono eyebrow (the real count: `639 OE`, `35 AUDITS`, `50 KPI`...), H3, two lines, thin-stroke icon. No emojis.
6. **Old way vs AccredReady** — two columns; left column literally styled as a messy spreadsheet texture, right as the clean product. Show, don't tell.
7. **Testimonial** — single large quote, Bricolage italic, photo, name + designation + city. One real one beats three fake-looking ones.
8. **Pricing** — single ₹499 card, centered, `--verify` border. "Everything included." + Gap Assessment Report ₹20,000 as a quiet secondary card beside it.
9. **FAQ** — accordion, hairline dividers.
10. **Final CTA** — ink background, white H2 "Be assessment-ready before assessors arrive.", primary button.
11. **Footer** — ink, resource links (your SEO pages — they earn their keep), MSME/legal line.

## 5. Motion (restrained)

- One orchestrated moment: on hero load, the score ring animates 0→87% over 900ms ease-out, chapter bars stagger-fill 80ms apart. That's the demo AND the delight.
- Everything else: 150ms ease hover transitions only.
- `prefers-reduced-motion`: ring renders at final value, no animation.

## 6. Imagery Strategy + Prompt Suite

**Honest guidance first:** for this audience, real product screenshots beat generated imagery every time. Use AI images only for blog headers and section accents — never for the product itself, and never AI-generated "Indian doctors" (uncanny faces destroy clinical trust). Where you need people, use your own hospital-visit photos.

Ready-to-use prompts (Midjourney / DALL·E 3):

1. **Blog/OG header, abstract:** "Minimalist abstract composition of a clinical checklist transforming into a rising line graph, deep navy #0B1B2B and clinical white, single emerald green #0E8A5F accent line, thin precise strokes, generous whitespace, Swiss design poster style, no text, no people — flat vector illustration"
2. **Section accent, audit motif:** "Extreme close-up of a precise emerald green checkmark being drawn by a fine architectural pen on crisp white paper with faint grid lines, soft studio light, macro photography, shallow depth of field, clinical and premium, navy ink details"
3. **Trust/security section:** "Isometric vector illustration of a hospital building protected inside a translucent shield outline, deep navy and white palette with one emerald accent, thin-line technical drawing style, blueprint precision, clean white background, no text"
4. **About/story header:** "Wide minimalist illustration of a single confident path through a maze made of document stacks, navy monochrome with emerald path line, flat geometric vector style, editorial quality, white background"

## 7. Build Notes

- Implement on the static SEO pages first (they're plain HTML — fast wins), then port tokens into the React app gradually.
- Tailwind config: map the 9 tokens above; load the 3 Google Font families with `font-display: swap`.
- Quality floor: WCAG AA contrast (all combos above pass), visible focus rings (2px `--verify` offset), responsive to 360px.
- Do NOT redesign before June 20. Sequence: hero + nav + pricing section week 1 (June 22–28), remaining sections week 2.
