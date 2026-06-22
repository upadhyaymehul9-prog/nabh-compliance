import { useState } from "react";
import "./HomepageScreen.css";

export default function HomepageScreen({ onSignIn }) {
  const [openPersons, setOpenPersons] = useState([false, false, false]);

  const togPerson = (idx) => {
    setOpenPersons(prev => prev.map((v, i) => i === idx ? !v : v));
  };

  const wl = (name) => {
    const subj = encodeURIComponent("Waitlist: " + name);
    const body = encodeURIComponent(
      "Hi, I would like to join the waitlist for " + name + ". My hospital / organisation is: "
    );
    window.location.href = "mailto:doctor@accredready.in?subject=" + subj + "&body=" + body;
  };

  return (
    <div id="hp-root">

      <header>
        <div className="wrap">
          <nav>
            <a className="logo" href="#top">
              <span className="mark serif">A</span>
              <span className="nm">Accred<b>Ready</b></span>
            </a>
            <div className="navlinks">
              <a href="#features">Features</a>
              <a href="#founder">About</a>
              <a href="#pricing">Pricing</a>
              <button className="signin btn btn-ghost" onClick={onSignIn}>Sign in</button>
            </div>
          </nav>
        </div>
      </header>

      <span id="top"></span>

      {/* ── HERO ── */}
      <section className="hero">
        <div className="wrap">
          <p className="eyebrow">AI-Powered NABH Compliance Platform</p>
          <h1 className="serif">Get accreditation-ready, <em>without the consultant price tag.</em></h1>
          <p className="sub">India's most affordable NABH compliance platform — built by a healthcare professional. Score your standards, find your gaps, fix them, and reach survey-readiness. For hospitals and small healthcare organisations.</p>
          <div className="hero-cta">
            <button className="btn btn-gold" onClick={onSignIn}>Start free →</button>
            <a className="btn btn-ghost" style={{borderColor:"var(--gold)",color:"#fff"}} href="#features">See how it works</a>
          </div>
          <p className="hero-note"><i className="ti ti-lock"></i>&nbsp; No card required · Secured by Supabase · Email-only signup</p>
          <div className="stats">
            <div className="stat"><div className="n serif">15+ <span>yrs</span></div><div className="l">Healthcare operations & quality management</div></div>
            <div className="stat"><div className="n serif">All <span>types</span></div><div className="l">Of NABH accreditation & certification covered</div></div>
            <div className="stat"><div className="n serif">60+ <span>hospitals</span></div><div className="l">Served by our accreditation partner network</div></div>
          </div>
        </div>
      </section>

      {/* ── FEATURES ── */}
      <section className="features" id="features">
        <div className="wrap">
          <div className="sec-head">
            <p className="eyebrow">The platform</p>
            <h2 className="serif">Everything you need to reach <em>survey-readiness</em>, in one place.</h2>
            <p>From gap analysis through to the day the assessor walks in — documentation, scoring, and corrective-action workflow together.</p>
          </div>
          <div className="fgrid">
            <div className="fcard"><div className="ic"><i className="ti ti-checklist"></i></div><h3>Score your standards</h3><p>Self-assess every objective element 1–5, with built-in achievement tips on how to meet each one.</p></div>
            <div className="fcard"><div className="ic"><i className="ti ti-target-arrow"></i></div><h3>Instant gap analysis</h3><p>See your top gaps ranked by severity and a clear readiness verdict, updated live as you score.</p></div>
            <div className="fcard"><div className="ic"><i className="ti ti-tools"></i></div><h3>Fix gaps with CAPA</h3><p>Log corrective and preventive actions against each gap, assign owners, and attach evidence links.</p></div>
            <div className="fcard"><div className="ic"><i className="ti ti-users-group"></i></div><h3>Committees, KPIs & audits</h3><p>Ready-made committees, KPI calculators, audit toolkits, checklists and mock-drill plans.</p></div>
            <div className="fcard"><div className="ic"><i className="ti ti-layers-subtract"></i></div><h3>Multiple programmes</h3><p>Covers all types of NABH accreditation and certification, with more added continuously.</p></div>
            <div className="fcard"><div className="ic"><i className="ti ti-robot"></i></div><h3>AI assistant</h3><p>Ask questions and get answers grounded strictly in the actual standards — no guesswork.</p></div>
          </div>
        </div>
      </section>

      {/* ── WHO'S BEHIND IT ── */}
      <section id="founder">
        <div className="wrap">
          <div className="sec-head">
            <p className="eyebrow">Who's behind it</p>
            <h2 className="serif">Built from the inside <em>of the standard.</em></h2>
            <p>A practising NABH Quality Manager, an independent expert consulting panel, and a healthcare financing partner. Tap any name to see the full background.</p>
          </div>

          {/* Person 0 — Dr. Mehul Upadhyay */}
          <div className={`person${openPersons[0] ? " open" : ""}`} onClick={() => togPerson(0)}>
            <div className="person-head">
              <div className="mn serif">MU</div>
              <div className="who">
                <h3>Dr. Mehul Upadhyay</h3>
                <div className="one">Founder · Healthcare leader & certified NABH Quality Manager</div>
              </div>
              <span className="tag tag-gold">Founder</span>
              <i className="ti ti-chevron-down caret"></i>
            </div>
            <div className="person-body">
              <div className="inner">
                <p>15+ years of healthcare operations experience, including international exposure in New Zealand. Currently Head of Medical Services & Operations at HMP Foundation, Ankleshwar.</p>
                <p>AccredReady was built out of that direct, on-ground experience: the documentation burden, the audit cycles, and the gap between a standard's written requirement and a hospital's day-to-day reality. The platform reflects what accreditation actually looks like from inside a hospital, not from outside it.</p>
                <p className="small"><b>Current role:</b> Head of Medical Services & Operations, HMP Foundation · <b>Based in:</b> Ankleshwar, Gujarat · <b>Also:</b> IIM Kozhikode — Healthcare Management & AI</p>
              </div>
            </div>
          </div>

          {/* Person 1 — PMS EduCon */}
          <div className={`person${openPersons[1] ? " open" : ""}`} onClick={() => togPerson(1)}>
            <div className="person-head">
              <div className="mn serif">PE</div>
              <div className="who">
                <h3>PMS EduCon</h3>
                <div className="one">Accreditation Partner · NABH consulting & training, Ahmedabad</div>
              </div>
              <span className="tag tag-green">Expert Panel</span>
              <i className="ti ti-chevron-down caret"></i>
            </div>
            <div className="person-body">
              <div className="inner">
                <p>End-to-end NABH accreditation consulting for hospitals, SHCOs, eye hospitals, Ayush centres, dental and imaging centres — including documentation support, gap analysis, mock audits, and onsite/online training covering NABH standards, internal auditing, infection control, and fire safety.</p>
                <p className="small"><b>Coverage:</b> Remote & in-person, Greater Ahmedabad Area</p>
                <p className="small"><b>Track record:</b> 50+ successful NABH accreditations · 50+ hospitals & healthcare organisations served</p>
                <div className="hosp">
                  <span>Vision Eye Care Hospital</span><span>Shiv Jyoti Eye Hospital</span><span>Atulya Super Speciality & ICU</span><span>Stavya Spine Hospital</span><span>Krishna Hospital</span><span>+20 more</span>
                </div>
              </div>
            </div>
          </div>

          {/* Person 2 — Dr. D. Rakesh Khanna */}
          <div className={`person${openPersons[2] ? " open" : ""}`} onClick={() => togPerson(2)}>
            <div className="person-head">
              <div className="mn serif">RK</div>
              <div className="who">
                <h3>Dr. D. Rakesh Khanna, MD(AM)</h3>
                <div className="one">Accreditation Partner · Quality, Operations & Accreditation Strategist</div>
              </div>
              <span className="tag tag-green">Expert Panel</span>
              <i className="ti ti-chevron-down caret"></i>
            </div>
            <div className="person-body">
              <div className="inner">
                <p>JCI, AACI, NABH, DHA & MOH standards define Dr. D. Rakesh Khanna's expertise as a trusted Accreditation Partner for hospitals across India and the UAE. An AACI Certified Internal Surveyor and Senior Healthcare Quality Strategist, he has led accreditation readiness at Medcare Hospitals & Medical Centres (Aster DM Healthcare, UAE) and major Indian institutions including East Coast Hospitals, Medway Hospitals, GVN Hospitals, Dr. Rela Institute & Medical Centre, and Saveetha Hospital. With proven success in commissioning hospitals to full NABH/JCI compliance, optimising manpower, reducing costs, and strengthening patient safety, he delivers end-to-end accreditation readiness and operational excellence — across more than 20 accreditations.</p>
                <p className="small"><b>Based:</b> Chennai, with extensive India & UAE hospital experience</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ── FEATURE HIGHLIGHT BAND ── */}
      <section className="band">
        <div className="wrap">
          <div className="sec-head">
            <p className="eyebrow">AI-supported workflow</p>
            <h2 className="serif">Not just scoring — <em>real deliverables.</em></h2>
            <p>AccredReady turns your self-assessment into things you can actually hand to your MD and your assessor.</p>
          </div>
          <div className="bgrid">
            <div className="bcard"><div className="ic"><i className="ti ti-file-download"></i></div><h3>PDF gap & CAPA reports <span className="live">Live</span></h3><p>Generate a clean, survey-ready PDF after gap analysis and CAPA — overall compliance, chapter-wise scores, ranked gaps, the lot.</p></div>
            <div className="bcard"><div className="ic"><i className="ti ti-calendar-check"></i></div><h3>Full-year scheduling <span className="live">Live</span></h3><p>Set your entire year of committee meetings and mock drills on a date calendar — planned, tracked, and ready to show the assessor.</p></div>
            <div className="bcard"><div className="ic"><i className="ti ti-sparkles"></i></div><h3>AI document generation <span className="soon-label">Coming soon</span></h3><p>Soon, generate the required NABH documents right from your dashboard — drafted for you, ready to adapt.</p></div>
          </div>
        </div>
      </section>

      {/* ── PROGRAMMES ── */}
      <section className="progs">
        <div className="wrap">
          <div className="sec-head">
            <p className="eyebrow">Programmes covered</p>
            <h2 className="serif">All types of NABH accreditation <em>& certification.</em></h2>
          </div>
          <div className="pgrid">
            <div className="pcard"><h4>HCO Full Accreditation</h4><p>Full hospital accreditation standard, end-to-end objective element coverage.</p></div>
            <div className="pcard"><h4>SHCO Full Accreditation</h4><p>Small Healthcare Organisation accreditation, complete chapter coverage.</p></div>
            <div className="pcard"><h4>HCO Entry-Level Certification</h4><p>Hospital entry-level certification, 2nd Edition standards.</p></div>
            <div className="pcard"><h4>SHCO Entry-Level Certification</h4><p>Small Healthcare Organisation entry-level certification, 2nd Edition standards.</p></div>
            <div className="pcard"><h4>Eye Care Organisation (ECO)</h4><p>Full / Entry-Level accreditation for ophthalmic and eye care hospitals.</p></div>
          </div>
          <p className="prog-note">Additional NABH programmes are in active development as part of AccredReady's ongoing platform expansion.</p>
        </div>
      </section>

      {/* ── PRICING ── */}
      <section className="pricing" id="pricing">
        <div className="wrap">
          <div className="sec-head" style={{margin:"0 auto 40px",textAlign:"center"}}>
            <p className="eyebrow">Pricing</p>
            <h2 className="serif">A consultant costs lakhs. <em>AccredReady costs ₹499.</em></h2>
            <p style={{marginLeft:"auto",marginRight:"auto"}}>Same readiness work — gap analysis, documentation, corrective actions — at a fraction of the price.</p>
          </div>
          <div className="price-box">
            <div className="amt serif">₹499<small> / month</small></div>
            <div className="vs">vs. consultant engagements that typically run <b>₹50,000–₹2,00,000+</b><br/><span style={{fontSize:"12.5px"}}>(approximate market estimates — please do your own research)</span></div>
            <ul>
              <li><i className="ti ti-check"></i> All covered NABH programmes</li>
              <li><i className="ti ti-check"></i> Full scoring, gap analysis & readiness verdict</li>
              <li><i className="ti ti-check"></i> Committees, KPIs, audits, checklists & drills</li>
              <li><i className="ti ti-check"></i> CAPA workflow with evidence links</li>
              <li><i className="ti ti-check"></i> AI assistant grounded in the standards</li>
            </ul>
            <button className="btn btn-primary" style={{padding:"12px 32px",fontSize:"15px"}} onClick={onSignIn}>Start free →</button>
          </div>
        </div>
      </section>

      {/* ── MK TECH ── */}
      <section className="mktech">
        <div className="wrap">
          <div className="sec-head">
            <p className="eyebrow">More from MK Tech</p>
            <h2 className="serif">From compliant to <em>digital.</em></h2>
            <p>AccredReady is one part of a wider toolkit for running a modern hospital — built by the same team, with the same patient-first, accuracy-first approach.</p>
          </div>
          <div className="tier-label">Available now</div>
          <div className="mgrid">
            <div className="mcard"><div className="ic"><i className="ti ti-users"></i></div><h4>OPD Queue Manager</h4><p>Digital patient flow from entry to exit — no more blank-form re-entry at reception.</p></div>
            <div className="mcard"><div className="ic"><i className="ti ti-calendar-event"></i></div><h4>Appointment Scheduler</h4><p>QR-based clinic booking with WhatsApp confirmations. Privacy-first, no patient data stored.</p></div>
            <div className="mcard"><div className="ic"><i className="ti ti-chart-bar"></i></div><h4>Hospital Dashboard</h4><p>Real-time KPI monitoring across departments — see performance and revenue at a glance.</p></div>
            <div className="mcard"><div className="ic"><i className="ti ti-device-laptop"></i></div><h4>Website & App Development</h4><p>Custom hospital websites and mobile apps, built and shipped end-to-end.</p></div>
          </div>
          <div className="tier-label">Coming soon</div>
          <div className="mgrid">
            <div className="mcard soon">
              <span className="soon-badge">Coming soon</span>
              <div className="ic"><i className="ti ti-bed"></i></div>
              <h4>IPD Manager</h4>
              <p>Inpatient admission-to-discharge workflow, built to order for hospitals that need it.</p>
              <div className="waitlist" onClick={() => wl("IPD Manager")}><i className="ti ti-bell"></i> Join waitlist</div>
            </div>
            <div className="mcard soon">
              <span className="soon-badge">Coming soon</span>
              <div className="ic"><i className="ti ti-report-money"></i></div>
              <h4>Revenue Leakage Self-Audit</h4>
              <p>Find where your hospital is losing revenue — and exactly how to plug each leak.</p>
              <div className="waitlist" onClick={() => wl("Revenue Leakage Self-Audit")}><i className="ti ti-bell"></i> Join waitlist</div>
            </div>
          </div>
        </div>
      </section>

      {/* ── FINAL CTA ── */}
      <section className="final">
        <div className="wrap">
          <p className="eyebrow" style={{color:"var(--gold-light)"}}>Accred<b style={{color:"var(--gold)"}}>Ready</b></p>
          <h2 className="serif" style={{marginTop:14}}>Accreditation readiness, <em>built and backed</em> end to end.</h2>
          <p>Software from a practising NABH Quality Manager. Consulting from an independent expert network. Financing from a dedicated healthcare partner.</p>
          <button className="btn btn-gold" style={{padding:"13px 34px",fontSize:"15px"}} onClick={onSignIn}>Start free →</button>
          <div className="contact-row">
            <div><div className="k">Website</div><div className="v">accredready.in</div></div>
            <div><div className="k">Email</div><div className="v">doctor@accredready.in</div></div>
            <div><div className="k">Location</div><div className="v">Gujarat — India</div></div>
          </div>
        </div>
      </section>

      <footer>
        <div className="wrap">
          <span>© 2026 AccredReady — NABH Compliance Platform · MK Tech</span>
          <span><a href="/contact">Contact</a> · <a href="/terms">Terms</a> · <a href="/privacy.html">Privacy</a></span>
        </div>
      </footer>

    </div>
  );
}
