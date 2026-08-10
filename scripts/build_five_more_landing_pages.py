#!/usr/bin/env python3
"""Generate 5 additional NABH landing pages from verified nabh.co facts only."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def faq_json(pairs: list[tuple[str, str]]) -> str:
    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in pairs
            ],
        },
        indent=2,
    )


def related_html(items: list[tuple[str, str]]) -> str:
    return "\n".join(
        f'          <li>→ <a href="https://accredready.in/{u}" class="rounded text-verify '
        f'underline-offset-2 hover:underline focus-visible:ring-2 focus-visible:ring-verify">{t}</a></li>'
        for u, t in items
    )


def render(page: dict) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page['title']}</title>
  <meta name="description" content="{page['meta']}" />
  <meta name="keywords" content="{page['keywords']}" />
  <link rel="canonical" href="https://accredready.in/{page['canonical']}" />
  <meta property="og:title" content="{page['og_title']}" />
  <meta property="og:description" content="{page['meta']}" />
  <meta property="og:url" content="https://accredready.in/{page['canonical']}" />
  <meta property="og:image" content="https://accredready.in/logo512.png" />
  <meta property="og:type" content="article" />
  <script type="application/ld+json">
{page['faq_json']}
  </script>
  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{page['h1_plain']}",
  "description": "{page['meta']}",
  "author": {{"@type": "Person", "name": "Dr. Mehul Upadhyay", "jobTitle": "Healthcare Operations Leader"}},
  "publisher": {{"@type": "Organization", "name": "AccredReady", "url": "https://accredready.in"}},
  "datePublished": "2026-08-10",
  "dateModified": "2026-08-10",
  "mainEntityOfPage": "https://accredready.in/{page['canonical']}"
}}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{ extend: {{
        colors: {{ ink:'#0B1B2B', paper:'#FBFDFD', verify:'#0E8A5F', verifydark:'#0A6B4A', signal:'#D97706', alert:'#DC2626', slate:'#4B5D6E', hairline:'#DCE6E4', mint:'#EBF4F0' }},
        fontFamily: {{ display:['"Bricolage Grotesque"','sans-serif'], body:['"IBM Plex Sans"','sans-serif'], mono:['"IBM Plex Mono"','monospace'] }}
      }}}}
    }};
  </script>
  <style type="text/tailwindcss">
    @layer components {{
      .tbl {{ @apply w-full border-collapse text-[0.9rem]; }}
      .tbl th {{ @apply bg-mint px-4 py-3 text-left font-mono text-[0.78rem] font-medium uppercase tracking-wide text-ink; }}
      .tbl td {{ @apply border-b border-hairline px-4 py-2.5 align-top text-slate; }}
      .tbl strong {{ @apply text-ink; }}
    }}
  </style>
  <style>
    body {{ background:#FBFDFD; }}
    html {{ scroll-behavior: smooth; }}
    @media (prefers-reduced-motion: reduce) {{
      html {{ scroll-behavior: auto; }}
      *, *::before, *::after {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }}
    }}
  </style>
</head>
<body class="font-body text-ink leading-[1.7] antialiased">
  <a href="#main" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-[200] focus:rounded-lg focus:bg-verify focus:px-4 focus:py-2 focus:text-white focus:outline-none">Skip to content</a>
  <nav class="sticky top-0 z-[100] border-b border-hairline bg-paper/90 backdrop-blur">
    <div class="mx-auto flex max-w-7xl items-center justify-between px-6 py-4 lg:px-8">
      <a href="https://accredready.in" class="rounded font-display text-[22px] font-bold tracking-[-0.01em] text-ink focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2">AccredReady</a>
      <a href="https://accredready.in" class="rounded-xl bg-verify px-5 py-2.5 text-[15px] font-semibold text-white transition-all duration-150 hover:-translate-y-px hover:bg-verifydark hover:shadow-[0_6px_16px_rgba(14,138,95,0.25)] focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 motion-reduce:transform-none motion-reduce:transition-none">Start free trial</a>
    </div>
  </nav>
  <main id="main">
    <header class="mx-auto max-w-3xl px-5 pb-10 pt-16 text-center sm:px-8">
      <span class="mb-6 inline-flex items-center gap-2 rounded-lg border border-verify/20 bg-mint px-3 py-1.5 font-mono text-[13px] uppercase tracking-wide text-verify"><span class="h-1.5 w-1.5 rounded-full bg-verify"></span>{page['eyebrow']}</span>
      <h1 class="mb-5 font-display text-[clamp(1.8rem,4vw,3rem)] font-bold leading-[1.1] tracking-[-0.02em]">{page['h1']}</h1>
      <p class="mx-auto max-w-2xl text-lg text-slate">{page['sub']}</p>
    </header>
    <article class="mx-auto max-w-3xl px-5 pb-16 sm:px-8 [&_h2]:mb-4 [&_h2]:mt-10 [&_h2]:font-display [&_h2]:text-2xl [&_h2]:font-bold [&_h3]:mb-2 [&_h3]:mt-7 [&_h3]:font-display [&_h3]:text-lg [&_h3]:font-bold [&_h3]:text-ink [&_p]:mb-4 [&_p]:text-[0.97rem] [&_p]:text-slate [&_strong]:text-ink">
      <div class="mb-8 flex flex-wrap items-center gap-x-4 gap-y-1 border-b border-hairline pb-5 text-[0.83rem] text-slate">
        <span class="flex items-center gap-1.5">
          <span class="h-6 w-6 rounded-full bg-mint flex items-center justify-center font-display text-[11px] font-bold text-verify" aria-hidden="true">MU</span>
          <strong class="text-ink">Dr. Mehul Upadhyay</strong>
        </span>
        <span class="text-slate/50">·</span>
        <span>Healthcare Operations Leader</span>
        <span class="text-slate/50">·</span>
        <time datetime="2026-08-10">Published: August 2026</time>
        <span class="text-slate/50">·</span>
        <time datetime="2026-08-10">Updated: August 2026</time>
      </div>
{page['body']}
      <div class="my-8 rounded-xl border border-hairline bg-white px-5 py-4 text-[0.83rem] text-slate">
        <p class="!mb-0"><strong class="text-ink">Sources:</strong> {page['sources']} Always verify live rules and fees at <a href="https://nabh.co" target="_blank" rel="noopener noreferrer" class="rounded text-verify underline-offset-2 hover:underline focus-visible:ring-2 focus-visible:ring-verify">nabh.co</a>.</p>
      </div>
      <div class="my-6 rounded-xl border border-hairline bg-white px-5 py-4 text-[0.9rem]">
        <p class="!mb-2 font-mono text-[12px] uppercase tracking-wide text-slate">Related pages</p>
        <ul class="space-y-1.5 !mb-0">
{page['related']}
        </ul>
      </div>
      <div class="my-10 rounded-2xl bg-ink px-6 py-12 text-center">
        <p class="font-mono text-[12px] uppercase tracking-widest text-white/50 mb-3">AccredReady</p>
        <h2 class="!mt-0 font-display text-2xl font-bold !text-white">{page['cta_h']}</h2>
        <p class="mx-auto mt-3 max-w-lg !text-white/70">{page['cta_p']}</p>
        <a href="https://accredready.in" class="mt-5 inline-block rounded-xl bg-verify px-8 py-3.5 font-semibold text-white transition-all duration-150 hover:-translate-y-px hover:bg-verifydark hover:shadow-[0_6px_16px_rgba(14,138,95,0.25)] focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 focus-visible:ring-offset-ink motion-reduce:transform-none motion-reduce:transition-none">Start free on AccredReady →</a>
      </div>
    </article>
  </main>
  <footer class="bg-ink text-white/70">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8">
      <nav aria-label="Footer" class="flex flex-wrap justify-center gap-x-7 gap-y-3 text-[14px]">
        <a href="https://accredready.in" class="rounded hover:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 focus-visible:ring-offset-ink">Home</a>
        <a href="https://accredready.in/learn" class="rounded hover:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 focus-visible:ring-offset-ink">Learn</a>
        <a href="https://accredready.in/nabh-accreditation-software" class="rounded hover:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 focus-visible:ring-offset-ink">NABH Software</a>
        <a href="https://accredready.in/privacy" class="rounded hover:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 focus-visible:ring-offset-ink">Privacy Policy</a>
      </nav>
      <p class="mt-8 text-center font-mono text-[12px] text-white/45">© 2026 AccredReady by MK Tech.</p>
    </div>
  </footer>
</body>
</html>
"""


def page(**kwargs) -> dict:
    kwargs["faq_json"] = faq_json(kwargs.pop("faqs"))
    kwargs["related"] = related_html(kwargs.pop("related"))
    return kwargs


PAGES = [
    page(
        path="public/learn/nabh-surprise-assessment.html",
        title="NABH surprise assessment — unannounced visit policy | AccredReady",
        meta="NABH publishes a Surprise Assessment policy separate from surveillance and focus visits. What quality teams should keep ready every day.",
        keywords="NABH surprise assessment, NABH unannounced visit, NABH surprise assessment policy, NABH surprise visit hospital",
        canonical="learn/nabh-surprise-assessment",
        og_title="NABH surprise assessment — unannounced visit policy",
        h1_plain="NABH surprise assessment — stay ready without a calendar invite",
        eyebrow="NABH Guide · Surprise assessment",
        h1="NABH surprise assessment — stay ready without a calendar invite",
        sub="NABH lists a separate Surprise Assessment policy on programme document pages. It is not surveillance and not focus assessment.",
        faqs=[
            (
                "Does NABH conduct surprise assessments?",
                "Yes. NABH publishes a Policy for Surprise Assessment on programme document lists (for example under Entry Level and SHCO programme pages on nabh.co). Read the latest issue PDF for triggers and process.",
            ),
            (
                "Is a surprise assessment the same as surveillance?",
                "No. Surveillance is the scheduled mid-cycle check (for HCO Full under 6th Edition: 21–24 months). Surprise assessment is governed by a separate surprise-assessment policy.",
            ),
            (
                "Is a surprise assessment the same as focus assessment?",
                "No. Focus assessment has its own Policy & Procedure for Focus Assessment. Keep the three mechanisms distinct when briefing leadership.",
            ),
            (
                "What should hospitals keep ready every day?",
                "The same evidence habit as final assessment: current statutory/FMS documents, living committee minutes, KPI action, closed CAPAs, and staff who can demonstrate practice without rehearsal week.",
            ),
            (
                "Where is the official surprise assessment policy?",
                "On nabh.co programme pages under Documents — look for “NABH Policy for Surprise Assessment”. Always use the latest issue number published there.",
            ),
        ],
        body="""
      <p class="!text-[1.05rem] !text-ink"><strong>NABH publishes a Surprise Assessment policy as a distinct mechanism from scheduled surveillance and focus assessment.</strong> If your hospital only prepares when a date is announced, you are preparing for the wrong risk. Source: programme Documents lists on nabh.co.</p>
      <div class="my-5 rounded-xl border border-signal/30 bg-signal/5 px-6 py-4"><p class="!mb-0 !text-ink"><strong>Three different policies:</strong> surveillance (mid-cycle schedule), focus assessment (targeted), surprise assessment (unannounced / policy-triggered). Do not use the words interchangeably in board updates.</p></div>
      <h2>Where to find the official rule</h2>
      <p>Open your programme page on <a href="https://nabh.co" target="_blank" rel="noopener noreferrer" class="rounded text-verify underline-offset-2 hover:underline focus-visible:ring-2 focus-visible:ring-verify">nabh.co</a> → Documents → <strong>NABH Policy for Surprise Assessment</strong>. The issue number and wording on that PDF override secondary guides.</p>
      <h2>What “always ready” actually means</h2>
      <ul class="my-5 space-y-2.5 text-[0.95rem] text-slate">
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Statutory and facility documents current (not “renewal next month” piles).</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Committee minutes and action tracking continuous after award day.</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>CAPAs closed with evidence — open findings are visible on any visit type.</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Frontline staff can explain their own protocols without reading the SOP aloud.</span></li>
      </ul>
      <h2>Frequently asked questions</h2>
      <h3>Does NABH conduct surprise assessments?</h3>
      <p>Yes — under a published Surprise Assessment policy listed on nabh.co programme document sections.</p>
      <h3>Is it the same as surveillance?</h3>
      <p>No. Surveillance is scheduled mid-cycle (HCO Full: 21–24 months under 6th Edition).</p>
      <h3>Is it the same as focus assessment?</h3>
      <p>No — separate Focus Assessment policy.</p>
      <h3>What should hospitals keep ready every day?</h3>
      <p>Current statutory docs, living quality evidence, closed CAPAs, and staff demonstration of practice.</p>
      <h3>Where is the official policy?</h3>
      <p>nabh.co programme Documents → “NABH Policy for Surprise Assessment” (latest issue).</p>
""",
        sources='nabh.co Entry Level / SHCO programme Documents lists (Surprise Assessment policy); HCO 6th Edition surveillance timing for contrast.',
        related=[
            ("learn/nabh-surveillance-assessment", "Surveillance assessment"),
            ("learn/nabh-focus-assessment", "Focus assessment"),
            ("learn/nabh-assessment-preparation", "Assessment preparation"),
            ("nabh-accreditation-software", "NABH accreditation software"),
        ],
        cta_h="Build readiness that does not need a date",
        cta_p="Track OEs, CAPAs, and statutory dates on AccredReady so any NABH visit type finds a living system.",
    ),
    page(
        path="public/learn/nabh-self-assessment.html",
        title="NABH self-assessment before you apply | AccredReady",
        meta="NABH FAQs require self-assessment before submitting documents and fees. How to run an honest self-assessment against your programme standards.",
        keywords="NABH self assessment, NABH self-assessment toolkit, how to self assess NABH, NABH gap self assessment",
        canonical="learn/nabh-self-assessment",
        og_title="NABH self-assessment before you apply",
        h1_plain="NABH self-assessment — do this before you submit fees",
        eyebrow="NABH Guide · Self-assessment",
        h1="NABH self-assessment — do this before you submit fees",
        sub="NABH’s published process includes self-assessment after implementing standards and before submitting documents and fees.",
        faqs=[
            (
                "Is self-assessment part of the official NABH process?",
                "Yes. nabh.co FAQs – Hospitals list the process as: select programme; study and implement standards; conduct a self-assessment; submit documents and fees; undergo onsite assessment; close non-conformities.",
            ),
            (
                "When should self-assessment happen?",
                "After you have implemented the relevant standards for the minimum period your programme requires (for example ELC and SHCO pages require standards implementation for at least 3 months before application). Self-assessment before implementation is theatre.",
            ),
            (
                "Is self-assessment the same as gap analysis?",
                "In practice they overlap: you score current compliance against applicable objective elements and flag gaps. Use programme-specific standards — HCO, SHCO, or Entry Level matrices differ.",
            ),
            (
                "Can E-Mitra help with self-assessment?",
                "Yes. NABH FAQs state E-Mitra checklists and guidance can support gap analysis and preparation for assessment stages. Customise every template to your operations.",
            ),
            (
                "What happens if self-assessment shows major gaps?",
                "Delay the application. Paying fees with open CORE/patient-safety gaps usually converts into non-conformities and rework after onsite assessment.",
            ),
        ],
        body="""
      <p class="!text-[1.05rem] !text-ink"><strong>NABH’s published hospital FAQ process includes a self-assessment after you implement standards and before you submit documents and fees.</strong> Skipping it is how hospitals discover their real gaps during onsite assessment — at the highest cost.</p>
      <h2>Official process position</h2>
      <ol class="my-6 space-y-3 text-[0.95rem] text-slate list-decimal pl-5">
        <li>Select the appropriate programme</li>
        <li>Study and implement the relevant standards</li>
        <li><strong class="text-ink">Conduct a self-assessment</strong></li>
        <li>Submit documents and fees</li>
        <li>Onsite assessment</li>
        <li>Close non-conformities</li>
      </ol>
      <h2>How to run it honestly</h2>
      <ul class="my-5 space-y-2.5 text-[0.95rem] text-slate">
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Score against the edition and matrix you will be assessed on (ELC Core/Commitment/Excellence differs by bed strength and cycle).</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Mark “document exists but staff cannot demonstrate” as non-compliant.</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Convert every red item into an owned CAPA with a date.</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Re-score after closure — then decide on portal submission.</span></li>
      </ul>
      <h2>Frequently asked questions</h2>
      <h3>Is self-assessment part of the official NABH process?</h3>
      <p>Yes — listed in nabh.co FAQs – Hospitals between implementation and document/fee submission.</p>
      <h3>When should it happen?</h3>
      <p>After the programme’s minimum implementation window (commonly ≥3 months for ELC/SHCO standards on those programme pages).</p>
      <h3>Is it the same as gap analysis?</h3>
      <p>They overlap; both require scoring against applicable objective elements for your pathway.</p>
      <h3>Can E-Mitra help?</h3>
      <p>Yes as draft checklists — customise and verify practice.</p>
      <h3>What if self-assessment shows major gaps?</h3>
      <p>Fix them before applying.</p>
""",
        sources='nabh.co FAQs – Hospitals (accreditation process); ELC/SHCO programme minimum implementation periods; E-Mitra FAQ guidance on nabh.co.',
        related=[
            ("learn/nabh-how-to-apply", "How to apply for NABH"),
            ("learn/nabh-gap-analysis", "NABH gap analysis"),
            ("learn/nabh-e-mitra", "NABH E-Mitra"),
            ("nabh-accreditation-software", "NABH accreditation software"),
        ],
        cta_h="Self-assess with a living score, not a spreadsheet snapshot",
        cta_p="Run gap scoring and CAPA closure on AccredReady before you pay nabh.co application fees.",
    ),
    page(
        path="public/learn/nabh-non-conformity-closure.html",
        title="NABH non-conformity closure after assessment | AccredReady",
        meta="If a hospital falls short at NABH assessment, NABH provides a non-conformity report and timeframe to close gaps. How quality teams should close NCs without losing the thread.",
        keywords="NABH non conformity, NABH NC closure, NABH corrective action, NABH assessment non compliance",
        canonical="learn/nabh-non-conformity-closure",
        og_title="NABH non-conformity closure after assessment",
        h1_plain="NABH non-conformity closure — what to do after findings",
        eyebrow="NABH Guide · Non-conformities",
        h1="NABH non-conformity closure — what to do after findings",
        sub="NABH FAQs: if you fall short, you get a report and a reasonable timeframe to address non-conformities. Closure quality decides the outcome.",
        faqs=[
            (
                "What if a facility does not fully meet standards during assessment?",
                "NABH FAQs – Hospitals state that if a facility falls short, it is provided with a report outlining the non-conformities, along with a reasonable timeframe to address them. Accreditation follows successful closure as per NABH process.",
            ),
            (
                "Is receiving non-conformities an automatic fail forever?",
                "No. NABH frames quality improvement as a journey and provides time to address findings. Ignoring deadlines or closing on paper only is what converts findings into prolonged adverse outcomes.",
            ),
            (
                "What evidence should CAPA / NC closure include?",
                "Root cause (not only correction), corrective action, preventive action where applicable, responsible owner, due date, and proof that practice changed — not only an updated SOP file.",
            ),
            (
                "How does this relate to focus assessment?",
                "NABH also publishes a Focus Assessment policy for targeted verification. Some closure pathways may involve further verification — read the assessment report instructions and current NABH policies on nabh.co.",
            ),
            (
                "Should open internal CAPAs be closed before assessment?",
                "Yes as practice. Open internal findings at assessment time are a common path to onsite non-conformities. Run internal audits early enough to close CAPAs before the visit.",
            ),
        ],
        body="""
      <p class="!text-[1.05rem] !text-ink"><strong>If your hospital falls short during NABH assessment, NABH provides a non-conformity report and a reasonable timeframe to address the findings.</strong> The certificate decision depends on satisfactory closure — not on how quickly you email a revised Word file. Source: nabh.co FAQs – Hospitals.</p>
      <h2>Closure loop that assessors recognise</h2>
      <div class="my-6 overflow-x-auto rounded-xl border border-hairline shadow-sm"><table class="tbl"><thead><tr><th>Step</th><th>What “done” looks like</th></tr></thead><tbody>
      <tr><td><strong>1. Understand the NC</strong></td><td>Quote the finding; identify the standard/OE referenced in the report</td></tr>
      <tr><td><strong>2. Root cause</strong></td><td>Why it happened (process, training, resources) — not “staff mistake” alone</td></tr>
      <tr><td><strong>3. Corrective action</strong></td><td>Fix the instance and the system that allowed it</td></tr>
      <tr><td><strong>4. Evidence</strong></td><td>Records, observations, retraining proof, updated practice</td></tr>
      <tr><td><strong>5. Verify effectiveness</strong></td><td>Re-check after a defined period; keep the trail</td></tr>
      </tbody></table></div>
      <h2>Do not confuse document update with closure</h2>
      <p>Changing an SOP version number without changing bedside practice leaves you exposed on verification visits — including focus or surprise assessments under separate NABH policies.</p>
      <h2>Frequently asked questions</h2>
      <h3>What if we do not fully meet standards at assessment?</h3>
      <p>NABH issues an NC report with a timeframe to address findings (nabh.co FAQs).</p>
      <h3>Is that an automatic permanent fail?</h3>
      <p>No — closure within NABH’s process can still lead to grant.</p>
      <h3>What should closure evidence include?</h3>
      <p>Root cause, actions, owner, dates, and proof of changed practice.</p>
      <h3>How does focus assessment relate?</h3>
      <p>Separate policy may apply for targeted verification — follow your report and nabh.co policies.</p>
      <h3>Should internal CAPAs be closed before assessment?</h3>
      <p>Yes — open internal findings often become onsite NCs.</p>
""",
        sources='nabh.co FAQs – Hospitals (facilities that do not fully meet standards); Focus/Surprise assessment policy lists on nabh.co programme pages.',
        related=[
            ("learn/nabh-assessment-preparation", "Assessment preparation"),
            ("learn/nabh-focus-assessment", "Focus assessment"),
            ("learn/nabh-self-assessment", "Self-assessment before apply"),
            ("nabh-accreditation-software", "NABH accreditation software"),
        ],
        cta_h="Close CAPAs with evidence, not optimism",
        cta_p="Track non-conformities, owners, and proof on AccredReady so closure packages are audit-ready.",
    ),
    page(
        path="public/learn/nabh-gst-accreditation-fees.html",
        title="GST on NABH accreditation fees — 18% explained | AccredReady",
        meta="NABH programme fee tables on nabh.co state 18% GST is applicable extra on accreditation and certification fees. How to budget Year-1 cost correctly.",
        keywords="GST on NABH fees, NABH accreditation GST 18%, NABH fee GST inclusive, NABH application fee GST",
        canonical="learn/nabh-gst-accreditation-fees",
        og_title="GST on NABH accreditation fees — 18% explained",
        h1_plain="GST on NABH accreditation fees — budget the 18%",
        eyebrow="NABH Guide · Fees &amp; GST",
        h1="GST on NABH accreditation fees — budget the 18%",
        sub="nabh.co fee tables for SHCO and Entry Level state 18% GST applicable extra. Do not treat published fee lines as final payable.",
        faqs=[
            (
                "Is GST applicable on NABH fees?",
                "Yes. Current nabh.co SHCO and Entry Level Certification fee sections state 18% GST applicable extra. Confirm the live wording on the programme page you are paying against.",
            ),
            (
                "Are published NABH fee amounts inclusive of GST?",
                "On the SHCO and ELC tables reviewed on nabh.co, base fee lines are listed and GST is called out separately as extra. Always re-read the live table before remittance.",
            ),
            (
                "Which fee heads typically attract GST?",
                "Programme tables commonly list application/certification fees, annual fees (where applicable), virtual assessment, focus assessment, and certificate re-issue — with GST stated as applicable extra. Verify each head on your programme’s live table.",
            ),
            (
                "How should a quality manager present Year-1 cost to leadership?",
                "Show programme fee (ex-GST) + 18% GST + any assessor travel/boarding if your programme notes say those are borne by the HCO on actuals. Do not present only the ex-GST line.",
            ),
            (
                "Where should I verify fees before paying?",
                "Only on the live programme fee table at nabh.co (and any official NABH fee notification linked there). Secondary websites can lag.",
            ),
        ],
        body="""
      <p class="!text-[1.05rem] !text-ink"><strong>On current nabh.co fee sections for SHCO Accreditation and Entry Level Certification, NABH states 18% GST is applicable extra.</strong> If your board memo uses only the ex-GST number, your payable amount is understated by nearly one-fifth.</p>
      <h2>How to read a nabh.co fee table</h2>
      <ul class="my-5 space-y-2.5 text-[0.95rem] text-slate">
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Take the published fee line for your bed slab / programme.</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Add <strong class="text-ink">18% GST</strong> when the page says GST is extra.</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Add any separate heads listed (virtual assessment, focus assessment, re-issue) the same way.</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Check notes about assessor travel/boarding — some programmes state these are borne by the organisation on actuals.</span></li>
      </ul>
      <h2>Example framing (illustrative arithmetic only)</h2>
      <p>If a published ex-GST head is ₹1,00,000 and GST is 18% extra, GST = ₹18,000 and payable for that head = ₹1,18,000. Replace the base figure with your live nabh.co line — do not copy examples as your invoice.</p>
      <h2>Frequently asked questions</h2>
      <h3>Is GST applicable on NABH fees?</h3>
      <p>Yes — 18% GST applicable extra on current SHCO/ELC nabh.co fee sections.</p>
      <h3>Are table amounts GST-inclusive?</h3>
      <p>Those tables list fees and call GST out as extra — confirm live text.</p>
      <h3>Which heads attract GST?</h3>
      <p>Follow each head on your programme’s live table (application/certification, annual, virtual, focus, re-issue as listed).</p>
      <h3>How should Year-1 cost be presented?</h3>
      <p>Ex-GST fees + GST + any actuals noted by NABH for assessor travel/boarding.</p>
      <h3>Where to verify before paying?</h3>
      <p>Live nabh.co programme fee table only.</p>
""",
        sources='<a href="https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/" class="rounded text-verify underline-offset-2 hover:underline" target="_blank" rel="noopener noreferrer">SHCO fee section</a> and <a href="https://nabh.co/programmes/entry-level-hospitals-certification-programme/" class="rounded text-verify underline-offset-2 hover:underline" target="_blank" rel="noopener noreferrer">ELC fee section</a> stating 18% GST applicable extra.',
        related=[
            ("nabh-accreditation-cost", "Full NABH fee structure"),
            ("learn/nabh-how-to-apply", "How to apply"),
            ("learn/nabh-entry-level-vs-full", "ELC vs Full"),
            ("nabh-accreditation-software", "NABH software"),
        ],
        cta_h="Budget fees correctly — then track compliance",
        cta_p="After you allocate the GST-inclusive NABH budget, use AccredReady to keep preparation on timeline.",
    ),
    page(
        path="public/learn/nabh-day-care-elc.html",
        title="NABH Entry Level for day-care centres — occupancy rules | AccredReady",
        meta="NABH Entry Level Certification (2nd Edition) counts day-care beds as census beds for occupancy in listed standalone day-care centres, with specialty case rules over six months.",
        keywords="NABH day care Entry Level, NABH ELC day care beds, NABH dialysis day care accreditation, NABH ophthalmology day care ELC",
        canonical="learn/nabh-day-care-elc",
        og_title="NABH Entry Level for day-care centres — occupancy rules",
        h1_plain="NABH Entry Level for day-care centres — how occupancy is counted",
        eyebrow="NABH Guide · Day-care ELC",
        h1="NABH Entry Level for day-care centres — how occupancy is counted",
        sub="Official ELC 2nd Edition notes for standalone day-care centres such as ophthalmology, chemotherapy, IVF, and dialysis.",
        faqs=[
            (
                "How are day-care beds counted for ELC occupancy?",
                "For centres such as Ophthalmology, Chemotherapy, IVF, Dialysis, etc., the Entry-Level Certification Programme (2nd Edition) page states day-care beds shall be considered as census beds for calculating occupancy.",
            ),
            (
                "Is there a case-volume rule for specialty scope?",
                "The same ELC page states assessment for inclusion in the scope of certification for the concerned superspecialty shall continue to be based on the availability of a minimum of three cases over a six-month period. Confirm live wording on nabh.co.",
            ),
            (
                "Do general ELC occupancy thresholds still apply?",
                "Yes. ELC publishes minimum occupancy by cycle: final assessment 20% (last 3 months); 1st renewal 25% (preceding 1 year); 2nd renewal 30% (preceding 1 year), plus functional ≥6 months and standards ≥3 months.",
            ),
            (
                "Are standalone dental or diagnostic centres eligible for this ELC pathway?",
                "ELC exclusions list standalone Dental, Physiotherapy, Diagnostics & Pathology, Psychology, Diabetology and De-addiction Centres. Do not assume day-care specialty language overrides those exclusions.",
            ),
            (
                "What else must day-care centres ensure?",
                "ELC notes that in day-care beds, the hospital should ensure availability of emergency services whenever necessary, and certification follows an all-or-none principle for services offered.",
            ),
        ],
        body="""
      <p class="!text-[1.05rem] !text-ink"><strong>Under NABH Entry-Level Certification Programme (2nd Edition), for standalone day-care centres such as Ophthalmology, Chemotherapy, IVF, Dialysis, etc., day-care beds are counted as census beds for occupancy.</strong> Specialty scope inclusion also references a minimum of three cases over a six-month period. Source: nabh.co ELC programme page.</p>
      <h2>Occupancy thresholds that still apply</h2>
      <div class="my-6 overflow-x-auto rounded-xl border border-hairline shadow-sm"><table class="tbl"><thead><tr><th>Point</th><th>Minimum occupancy</th></tr></thead><tbody>
      <tr><td><strong>Final assessment</strong></td><td>20% during the last 3 months</td></tr>
      <tr><td><strong>1st renewal</strong></td><td>25% during the preceding 1 year</td></tr>
      <tr><td><strong>2nd renewal</strong></td><td>30% during the preceding 1 year</td></tr>
      </tbody></table></div>
      <h2>Do not ignore exclusions</h2>
      <p>Standalone dental, physiotherapy, diagnostics &amp; pathology, psychology, diabetology, and de-addiction centres are listed under ELC exclusions. Day-care specialty examples on the ELC page do not rewrite that exclusion list.</p>
      <h2>Operational notes from the same page</h2>
      <ul class="my-5 space-y-2.5 text-[0.95rem] text-slate">
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Ensure emergency services availability whenever necessary for day-care beds.</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>All-or-none principle: every service offered should be applied for certification.</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Functional ≥6 months and standards ≥3 months before application.</span></li>
      </ul>
      <h2>Frequently asked questions</h2>
      <h3>How are day-care beds counted?</h3>
      <p>As census beds for occupancy for listed standalone day-care centre types on the ELC page.</p>
      <h3>Is there a specialty case-volume rule?</h3>
      <p>Minimum of three cases over six months for concerned superspecialty scope inclusion — confirm live text.</p>
      <h3>Do 20%/25%/30% thresholds still apply?</h3>
      <p>Yes.</p>
      <h3>Are standalone dental/diagnostics eligible here?</h3>
      <p>They appear on the ELC exclusion list — check nabh.co before applying.</p>
      <h3>What else must day-care centres ensure?</h3>
      <p>Emergency service availability when needed; all-or-none service application.</p>
""",
        sources='<a href="https://nabh.co/programmes/entry-level-hospitals-certification-programme/" class="rounded text-verify underline-offset-2 hover:underline" target="_blank" rel="noopener noreferrer">Entry-Level Certification Programme (2nd Edition)</a> — Standalone Day-Care Centres, occupancy, exclusions.',
        related=[
            ("learn/nabh-elc-eligibility", "ELC eligibility & occupancy"),
            ("learn/nabh-entry-level-vs-full", "ELC vs Full"),
            ("nabh-entry-level-certification", "ELC complete guide"),
            ("nabh-elc-software", "ELC software"),
        ],
        cta_h="Track ELC evidence for day-care pathways too",
        cta_p="AccredReady supports Entry Level tracking so occupancy windows and standards implementation stay visible before you apply.",
    ),
]


def main() -> None:
    for p in PAGES:
        out = ROOT / p["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        html = render(p)
        out.write_text(html, encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
