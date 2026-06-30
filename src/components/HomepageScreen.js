import { useState, useEffect } from "react";

const YOUTUBE_PROMO_ID = "de3TKt7LfT8";
const YOUTUBE_PROMO_URL = `https://www.youtube.com/watch?v=${YOUTUBE_PROMO_ID}`;
const FOUNDER_LINKEDIN_URL = "https://www.linkedin.com/in/dr-mehul-upadhyay-039a07197";

export default function HomepageScreen({ onSignIn }) {
  const [openPersons, setOpenPersons] = useState([false, false, false]);
  const [menuOpen, setMenuOpen] = useState(false);

  const togPerson = (idx) =>
    setOpenPersons(prev => prev.map((v, i) => i === idx ? !v : v));

  const wl = (name) => {
    const subj = encodeURIComponent("Waitlist: " + name);
    const body = encodeURIComponent(
      "Hi, I would like to join the waitlist for " + name + ". My hospital / organisation is: "
    );
    window.location.href = "mailto:doctor@accredready.in?subject=" + subj + "&body=" + body;
  };

  useEffect(() => {
    if (!document.querySelector('link[data-figtree]')) {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.setAttribute('data-figtree', '1');
      link.href = 'https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap';
      document.head.appendChild(link);
    }
    document.documentElement.style.scrollBehavior = 'smooth';
    const header = document.getElementById('hp-header');
    if (!header) return;
    const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 8);
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => {
      window.removeEventListener('scroll', onScroll);
      document.documentElement.style.scrollBehavior = '';
    };
  }, []);

  return (
    <div id="hp-root">
      <style>{`
        /* ── TOKENS + BASE ── */
        #hp-root {
          --brand:       #065F46;
          --brand-dark:  #064E3B;
          --brand-mid:   #047857;
          --brand-bg:    #ECFDF5;
          --brand-light: #A7F3D0;
          --teal:        #0891B2;
          --amber:       #D97706;
          --amber-dark:  #B45309;
          --amber-bg:    #FFFBEB;
          --surface:     #F8FAFC;
          --border:      #E2E8F0;
          --text:        #1E293B;
          --muted:       #475569;
          --subtle:      #94A3B8;
          --white:       #FFFFFF;
          --shadow-sm:   0 1px 3px rgba(0,0,0,.07), 0 1px 2px rgba(0,0,0,.04);
          --shadow-md:   0 4px 14px rgba(0,0,0,.08), 0 2px 4px rgba(0,0,0,.04);
          --shadow-lg:   0 10px 30px rgba(0,0,0,.10), 0 4px 8px rgba(0,0,0,.05);
          font-family: 'Inter', system-ui, -apple-system, sans-serif;
          color: var(--text);
          background: var(--white);
          line-height: 1.6;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }
        #hp-root *, #hp-root *::before, #hp-root *::after { margin: 0; padding: 0; box-sizing: border-box; }
        #hp-root a { color: inherit; text-decoration: none; }
        #hp-root .ff { font-family: 'Figtree', system-ui, sans-serif; }
        #hp-root .wrap { max-width: 1100px; margin: 0 auto; padding: 0 24px; }

        /* ── TYPOGRAPHY ATOMS ── */
        #hp-root .eyebrow {
          display: inline-flex; align-items: center; gap: 7px;
          font-family: 'Figtree', sans-serif; font-size: 11.5px; font-weight: 700;
          letter-spacing: .15em; text-transform: uppercase; color: var(--teal);
        }
        #hp-root .eyebrow.on-dark { color: #5EEAD4; }
        #hp-root .eyebrow.amber   { color: var(--amber); }
        #hp-root .sec-head { max-width: 58ch; margin-bottom: 52px; }
        #hp-root .sec-head.center { margin-left: auto; margin-right: auto; text-align: center; }
        #hp-root .sec-head h2 {
          font-family: 'Figtree', sans-serif;
          font-size: clamp(26px, 3.2vw, 40px); font-weight: 800; color: var(--text);
          line-height: 1.13; margin-top: 14px; letter-spacing: -.025em;
        }
        #hp-root .sec-head h2 .hi    { color: var(--brand); }
        #hp-root .sec-head h2 .amber { color: var(--amber-dark); }
        #hp-root .si { font-family: 'Fraunces', Georgia, serif; font-style: italic; font-weight: 400; color: #c69a5c; }
        #hp-root .sec-head p { margin-top: 16px; color: var(--muted); font-size: 16px; line-height: 1.75; }
        #hp-root .sec-head.on-dark h2 { color: #fff; }
        #hp-root .sec-head.on-dark p  { color: #A7C4BA; }

        /* ── BUTTONS ── */
        #hp-root .btn {
          display: inline-flex; align-items: center; gap: 7px;
          font-family: 'Figtree', sans-serif; font-weight: 700; font-size: 14.5px;
          border-radius: 9px; padding: 10px 22px; cursor: pointer; border: none;
          min-height: 44px;
          transition: background .15s ease, box-shadow .2s cubic-bezier(0.175, 0.885, 0.32, 1.1), border-color .15s ease;
          line-height: 1; text-align: center; white-space: nowrap;
        }
        #hp-root .btn:focus-visible { outline: 2px solid var(--teal); outline-offset: 2px; }
        #hp-root .btn-primary { background: var(--brand); color: #fff; box-shadow: 0 1px 3px rgba(6,95,70,.25); }
        #hp-root .btn-primary:hover { background: var(--brand-dark); box-shadow: var(--shadow-md); }
        #hp-root .btn-amber { background: var(--amber); color: #fff; box-shadow: 0 1px 3px rgba(217,119,6,.25); }
        #hp-root .btn-amber:hover { background: var(--amber-dark); box-shadow: 0 4px 14px rgba(217,119,6,.35); }
        #hp-root .btn-ghost-white { background: rgba(255,255,255,.1); color: #fff; border: 1.5px solid rgba(255,255,255,.2); backdrop-filter: blur(4px); }
        #hp-root .btn-ghost-white:hover { background: rgba(255,255,255,.18); border-color: rgba(255,255,255,.4); }
        #hp-root .btn-lg { padding: 13px 30px; font-size: 15.5px; border-radius: 10px; }

        /* ── BADGES / TAGS ── */
        #hp-root .tag {
          display: inline-block; font-family: 'Figtree', sans-serif;
          font-size: 11px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase;
          padding: 4px 12px; border-radius: 100px; white-space: nowrap;
        }
        #hp-root .tag-founder { background: var(--amber-bg); color: var(--amber-dark); }
        #hp-root .tag-expert  { background: var(--brand-bg); color: var(--brand-mid); }
        #hp-root .badge-live {
          font-size: 9.5px; font-family: 'Figtree', sans-serif; font-weight: 700;
          letter-spacing: .08em; text-transform: uppercase;
          background: #059669; color: #fff; padding: 2px 8px; border-radius: 4px; vertical-align: middle;
        }
        #hp-root .badge-soon {
          font-size: 9.5px; font-family: 'Figtree', sans-serif; font-weight: 700;
          letter-spacing: .08em; text-transform: uppercase;
          background: transparent; color: #6EE7B7; border: 1px solid rgba(110,231,183,.4);
          padding: 2px 8px; border-radius: 4px; vertical-align: middle;
        }
        #hp-root .badge-soon-warm {
          font-size: 9.5px; font-family: 'Figtree', sans-serif; font-weight: 700;
          letter-spacing: .08em; text-transform: uppercase;
          background: var(--amber-bg); color: var(--amber); padding: 2px 9px; border-radius: 5px;
        }

        /* ── NAV ── */
        #hp-root header {
          position: sticky; top: 0; z-index: 100;
          background: rgba(255,255,255,.93);
          backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
          border-bottom: 1px solid var(--border); transition: box-shadow .2s ease;
        }
        #hp-root header.scrolled { box-shadow: 0 2px 14px rgba(0,0,0,.06); }
        #hp-root nav { display: flex; align-items: center; justify-content: space-between; height: 66px; gap: 12px; }
        #hp-root .logo { display: flex; align-items: center; gap: 10px; font-family: 'Figtree', sans-serif; font-weight: 700; font-size: 18px; color: var(--text); }
        #hp-root .logo-mark {
          width: 35px; height: 35px; border-radius: 9px; background: var(--brand);
          display: flex; align-items: center; justify-content: center;
          font-family: 'Figtree', sans-serif; font-weight: 800; font-size: 17px;
          color: #fff; letter-spacing: -.02em; flex-shrink: 0;
        }
        #hp-root .logo-name b { color: var(--brand); }
        #hp-root .navlinks { display: flex; align-items: center; gap: 4px; font-size: 14px; }
        #hp-root .navlinks a.nav-link { padding: 6px 13px; border-radius: 8px; color: var(--muted); font-weight: 500; transition: background .15s, color .15s; min-height: 44px; display: inline-flex; align-items: center; }
        #hp-root .navlinks a.nav-link:hover { color: var(--text); background: var(--surface); }
        #hp-root .navlinks a.nav-link:focus-visible { outline: 2px solid var(--teal); outline-offset: 2px; }
        #hp-root .nav-right { display: flex; align-items: center; gap: 4px; }
        #hp-root .menu-toggle {
          display: none; align-items: center; justify-content: center;
          width: 44px; height: 44px; border-radius: 10px; border: 1px solid var(--border);
          background: var(--white); color: var(--text); cursor: pointer;
        }
        #hp-root .menu-toggle:focus-visible { outline: 2px solid var(--teal); outline-offset: 2px; }
        #hp-root .mobile-menu {
          display: none; position: absolute; top: 66px; left: 0; right: 0;
          background: rgba(255,255,255,.98); border-bottom: 1px solid var(--border);
          padding: 12px 24px 16px; box-shadow: var(--shadow-md); z-index: 99;
        }
        #hp-root .mobile-menu.open { display: block; }
        #hp-root .mobile-menu a, #hp-root .mobile-menu button {
          display: flex; width: 100%; padding: 12px 0; border: none; background: none;
          font-size: 15px; font-weight: 600; color: var(--text); text-align: left; cursor: pointer;
          border-bottom: 1px solid var(--border); font-family: 'Figtree', sans-serif;
        }
        #hp-root .mobile-menu a:last-child, #hp-root .mobile-menu button:last-child { border-bottom: none; }
        @media(max-width:740px) {
          #hp-root .navlinks a.nav-link { display: none; }
          #hp-root .menu-toggle { display: inline-flex; }
        }

        /* ── HERO ── */
        #hp-root .hero { background: var(--brand-dark); color: #fff; position: relative; overflow: hidden; }
        #hp-root .hero::before {
          content: ""; position: absolute; inset: 0;
          background-image: radial-gradient(circle, rgba(255,255,255,.055) 1px, transparent 1px);
          background-size: 30px 30px; pointer-events: none;
        }
        #hp-root .hero::after {
          content: ""; position: absolute; right: -180px; bottom: -180px;
          width: 520px; height: 520px; border-radius: 50%;
          background: radial-gradient(circle, rgba(4,120,87,.45) 0%, transparent 70%);
          pointer-events: none;
        }
        #hp-root .hero-inner {
          position: relative; z-index: 2; padding: 88px 24px 76px;
          display: grid; grid-template-columns: minmax(0, 1fr) minmax(280px, 420px); gap: 48px;
          align-items: center; max-width: 1100px; margin: 0 auto;
        }
        @media(max-width:960px) {
          #hp-root .hero-inner { grid-template-columns: 1fr; gap: 40px; }
          #hp-root .hero-mockup, #hp-root .hero-video { max-width: 480px; width: 100%; margin: 0 auto; justify-self: center; }
        }
        @media(max-width:768px) { #hp-root .hero-inner { padding: 64px 20px 56px; } }
        #hp-root .hero-badge {
          display: inline-flex; align-items: center; gap: 8px;
          background: rgba(255,255,255,.09); border: 1px solid rgba(255,255,255,.16);
          color: #6EE7B7; font-family: 'Figtree', sans-serif; font-size: 11.5px;
          font-weight: 700; letter-spacing: .13em; text-transform: uppercase;
          padding: 6px 15px; border-radius: 100px; margin-bottom: 28px; backdrop-filter: blur(4px);
        }
        #hp-root .hero-badge .live-dot { width: 7px; height: 7px; border-radius: 50%; background: #34D399; box-shadow: 0 0 7px #34D399; flex-shrink: 0; }
        #hp-root .hero h1 { font-family: 'Figtree', sans-serif; font-size: clamp(36px, 5.2vw, 60px); line-height: 1.08; font-weight: 800; letter-spacing: -.03em; color: #fff; max-width: 16ch; }
        #hp-root .hero h1 .hero-hi { display: block; }
        #hp-root .hero-sub { margin: 26px 0 36px; font-size: 17px; color: #A7C4BA; max-width: 52ch; line-height: 1.75; }
        #hp-root .hero-actions { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }
        #hp-root .hero-app { display: flex; align-items: center; gap: 10px; margin-top: 18px; }
        #hp-root .hero-app-label { font-size: 12px; color: rgba(255,255,255,.6); white-space: nowrap; }
        #hp-root .hero-app img { height: 48px; display: inline-block; border: none; background: none; vertical-align: middle; }
        #hp-root .hero-social { display: flex; align-items: center; gap: 7px; margin-top: 14px; font-size: 13px; color: rgba(255,255,255,.8); }
        #hp-root .hero-social i { color: #6EE7B7; font-size: 15px; }
        #hp-root .hero-note { margin-top: 20px; font-size: 13px; color: #5A8A7C; display: flex; align-items: center; gap: 6px; }
        #hp-root .hero-stats { display: flex; flex-wrap: wrap; gap: 0; margin-top: 52px; border-top: 1px solid rgba(255,255,255,.1); }
        #hp-root .hstat { flex: 1; min-width: 140px; padding-top: 26px; padding-right: 28px; }
        #hp-root .hstat + .hstat { padding-left: 28px; border-left: 1px solid rgba(255,255,255,.08); }
        @media(max-width:640px) { #hp-root .hstat + .hstat { border-left: none; padding-left: 0; } }
        #hp-root .hstat .val { font-family: 'Figtree', sans-serif; font-size: 32px; font-weight: 800; color: #fff; letter-spacing: -.03em; line-height: 1; }
        #hp-root .hstat .val .accent { color: #6EE7B7; }
        #hp-root .hstat .label { font-size: 13px; color: #6B9B8E; margin-top: 7px; line-height: 1.45; max-width: 20ch; }

        /* ── HERO MOCKUP ── */
        #hp-root .hero-mockup {
          background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.14);
          border-radius: 18px; overflow: hidden;
          backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
          box-shadow: 0 8px 32px rgba(0,0,0,.25);
          width: 100%; max-width: 420px; justify-self: end;
        }
        #hp-root .mock-titlebar { display: flex; align-items: center; gap: 8px; padding: 14px 18px; border-bottom: 1px solid rgba(255,255,255,.1); background: rgba(0,0,0,.15); }
        #hp-root .mock-dot { width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,.18); }
        #hp-root .mock-url-bar { flex: 1; background: rgba(255,255,255,.08); border-radius: 6px; padding: 5px 12px; font-size: 11.5px; color: rgba(255,255,255,.4); font-family: 'Inter', sans-serif; margin-left: 4px; }
        #hp-root .mock-body { padding: 22px 20px 24px; }
        #hp-root .mock-prog-label { font-size: 10.5px; font-family: 'Figtree', sans-serif; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: #5EEAD4; margin-bottom: 14px; }
        #hp-root .mock-score-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 20px; }
        #hp-root .mock-stat-card { background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.1); border-radius: 10px; padding: 12px 10px; text-align: center; }
        #hp-root .mock-stat-val { font-family: 'Figtree', sans-serif; font-size: 22px; font-weight: 800; line-height: 1; color: #fff; }
        #hp-root .mock-stat-val.green  { color: #6EE7B7; }
        #hp-root .mock-stat-val.yellow { color: #FCD34D; }
        #hp-root .mock-stat-val.teal   { color: #7DD3FC; }
        #hp-root .mock-stat-lbl { font-size: 10.5px; color: rgba(255,255,255,.45); margin-top: 5px; font-family: 'Figtree', sans-serif; font-weight: 600; text-transform: uppercase; letter-spacing: .06em; }
        #hp-root .mock-progress-wrap { margin-bottom: 20px; }
        #hp-root .mock-progress-head { display: flex; justify-content: space-between; font-size: 11.5px; color: rgba(255,255,255,.5); margin-bottom: 7px; font-family: 'Figtree', sans-serif; }
        #hp-root .mock-bar-track { height: 6px; background: rgba(255,255,255,.1); border-radius: 10px; overflow: hidden; }
        #hp-root .mock-bar-fill { height: 100%; background: linear-gradient(90deg, #059669, #6EE7B7); border-radius: 10px; width: 72%; }
        #hp-root .mock-gaps-title { font-size: 10.5px; font-family: 'Figtree', sans-serif; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: rgba(255,255,255,.4); margin-bottom: 10px; }
        #hp-root .mock-gap-item { display: flex; align-items: center; gap: 9px; padding: 8px 0; border-bottom: 1px solid rgba(255,255,255,.06); font-size: 12.5px; color: rgba(255,255,255,.75); }
        #hp-root .mock-gap-item:last-child { border-bottom: none; }
        #hp-root .mock-sev { font-size: 9.5px; font-family: 'Figtree', sans-serif; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; padding: 2px 7px; border-radius: 4px; flex-shrink: 0; }
        #hp-root .mock-sev.high { background: rgba(239,68,68,.25); color: #FCA5A5; }
        #hp-root .mock-sev.med  { background: rgba(245,158,11,.2);  color: #FCD34D; }
        #hp-root .mock-sev.low  { background: rgba(6,95,70,.4);     color: #6EE7B7; }

        /* ── HERO VIDEO (YouTube) ── */
        #hp-root .hero-video {
          background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.14);
          border-radius: 18px; overflow: hidden;
          backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
          box-shadow: 0 8px 32px rgba(0,0,0,.25);
          width: 100%; max-width: 520px; justify-self: end;
        }
        #hp-root .hero-video-cap {
          padding: 12px 16px; border-bottom: 1px solid rgba(255,255,255,.1);
          background: rgba(0,0,0,.15);
          font-family: 'Figtree', sans-serif; font-size: 11.5px; font-weight: 700;
          letter-spacing: .08em; text-transform: uppercase; color: #5EEAD4;
          display: flex; align-items: center; gap: 8px;
        }
        #hp-root .hero-video-cap i { font-size: 16px; }
        #hp-root .hero-video-inner { position: relative; width: 100%; padding-bottom: 56.25%; height: 0; background: #000; }
        #hp-root .hero-video-inner iframe {
          position: absolute; inset: 0; width: 100%; height: 100%; border: 0;
        }

        /* ── TRUST BAR ── */
        #hp-root .trust-bar { background: var(--surface); border-bottom: 1px solid var(--border); padding: 16px 0; }
        #hp-root .trust-bar .wrap { display: flex; align-items: center; gap: 28px; flex-wrap: wrap; justify-content: center; }
        #hp-root .trust-item { display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 500; color: var(--muted); white-space: nowrap; }
        #hp-root .trust-item i { color: var(--brand); font-size: 16px; }
        #hp-root .trust-sep { width: 1px; height: 18px; background: var(--border); }
        @media(max-width:680px) { #hp-root .trust-sep { display: none; } }

        /* ── SECTION SHELL ── */
        #hp-root section { padding: 88px 0; }
        @media(max-width:768px) { #hp-root section { padding: 64px 0; } }

        /* ── FEATURES ── */
        #hp-root .features { background: var(--surface); }
        #hp-root .fgrid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
        @media(max-width:860px) { #hp-root .fgrid { grid-template-columns: repeat(2, 1fr); } }
        @media(max-width:540px) { #hp-root .fgrid { grid-template-columns: 1fr; } }
        #hp-root .fcard { background: var(--white); border: 1px solid var(--border); border-radius: 14px; padding: 28px; transition: border-color .2s, box-shadow .2s cubic-bezier(0.175, 0.885, 0.32, 1.1); cursor: default; }
        #hp-root .fcard:hover { border-color: var(--brand-light); box-shadow: var(--shadow-md); }
        #hp-root .fcard .ic { width: 46px; height: 46px; border-radius: 12px; background: var(--brand-bg); color: var(--brand); display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 18px; }
        #hp-root .fcard h3 { font-family: 'Figtree', sans-serif; font-size: 16.5px; font-weight: 700; color: var(--text); margin-bottom: 9px; }
        #hp-root .fcard p { font-size: 14.5px; color: var(--muted); line-height: 1.7; }

        /* ── HOW IT WORKS ── */
        #hp-root .how { background: var(--white); }
        #hp-root .steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 48px; }
        @media(max-width:700px) { #hp-root .steps { grid-template-columns: 1fr; gap: 0; } }
        #hp-root .step { display: flex; flex-direction: column; align-items: flex-start; }
        @media(max-width:700px) { #hp-root .step { padding: 24px 0; border-top: 1px solid var(--border); } }
        #hp-root .step-num { width: 48px; height: 48px; border-radius: 14px; background: var(--brand); color: #fff; font-family: 'Figtree', sans-serif; font-weight: 800; font-size: 20px; display: flex; align-items: center; justify-content: center; margin-bottom: 22px; flex-shrink: 0; }
        #hp-root .step-num.s2 { background: var(--teal); }
        #hp-root .step-num.s3 { background: var(--amber); }
        #hp-root .step h3 { font-family: 'Figtree', sans-serif; font-size: 18px; font-weight: 700; color: var(--text); margin-bottom: 10px; }
        #hp-root .step p { font-size: 14.5px; color: var(--muted); line-height: 1.75; }

        /* ── DELIVERABLES BAND ── */
        #hp-root .band { background: var(--brand-dark); color: #fff; }
        #hp-root .bgrid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
        @media(max-width:760px) { #hp-root .bgrid { grid-template-columns: 1fr; } }
        #hp-root .bcard { background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.11); border-radius: 14px; padding: 28px; transition: background .2s, border-color .2s; cursor: default; }
        #hp-root .bcard:hover { background: rgba(255,255,255,.11); border-color: rgba(255,255,255,.2); }
        #hp-root .bcard .ic { width: 46px; height: 46px; border-radius: 12px; background: rgba(110,231,183,.12); color: #6EE7B7; display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 18px; }
        #hp-root .bcard h3 { font-family: 'Figtree', sans-serif; font-size: 16.5px; font-weight: 700; color: #fff; margin-bottom: 10px; display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
        #hp-root .bcard p { font-size: 14px; color: #A7C4BA; line-height: 1.7; }

        /* ── TEAM / FOUNDER ── */
        #hp-root .team { background: var(--white); }
        #hp-root .person { border: 1px solid var(--border); border-radius: 14px; margin-bottom: 12px; overflow: hidden; background: var(--white); transition: border-color .15s, box-shadow .15s; }
        #hp-root .person:hover { border-color: var(--brand-light); }
        #hp-root .person.open { border-color: var(--brand-light); box-shadow: var(--shadow-sm); }
        #hp-root .person-head { display: flex; align-items: center; gap: 16px; padding: 20px 24px; cursor: pointer; user-select: none; transition: background .15s; background: none; border: none; width: 100%; text-align: left; font-family: inherit; font-size: inherit; color: inherit; }
        #hp-root .person-head:hover { background: var(--surface); }
        #hp-root .person-head:focus-visible { outline: 2px solid var(--teal); outline-offset: 2px; }
        #hp-root .person-av { width: 52px; height: 52px; border-radius: 12px; background: var(--brand-bg); color: var(--brand); font-family: 'Figtree', sans-serif; font-size: 17px; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
        #hp-root .person-info { flex: 1; min-width: 0; }
        #hp-root .person-info h3 { font-family: 'Figtree', sans-serif; font-size: 17px; font-weight: 700; color: var(--text); line-height: 1.3; }
        #hp-root .person-info .role { font-size: 13.5px; color: var(--muted); margin-top: 3px; }
        @media(max-width:560px) { #hp-root .person-info .role { display: none; } }
        #hp-root .p-caret { color: var(--subtle); font-size: 18px; transition: transform .25s ease; flex-shrink: 0; }
        #hp-root .person.open .p-caret { transform: rotate(180deg); }
        #hp-root .person-body { max-height: 0; overflow: hidden; transition: max-height .35s ease; }
        #hp-root .person.open .person-body { max-height: 1000px; }
        #hp-root .person-body .inner { padding: 4px 24px 28px; border-top: 1px solid var(--border); }
        #hp-root .person-body p { color: var(--muted); font-size: 14.5px; line-height: 1.75; margin-top: 16px; max-width: 74ch; }
        #hp-root .meta-line { font-size: 13px !important; margin-top: 10px !important; }
        #hp-root .meta-line b { color: var(--text); }
        #hp-root .founder-links { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 14px !important; }
        #hp-root .founder-links a {
          display: inline-flex; align-items: center; gap: 6px;
          font-size: 13px; font-weight: 600; color: var(--brand-mid);
        }
        #hp-root .founder-links a:hover { color: var(--brand-dark); text-decoration: underline; }
        #hp-root .hosp-chips { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 14px; }
        #hp-root .hosp-chips span { font-size: 12px; background: var(--surface); border: 1px solid var(--border); color: var(--text); padding: 5px 12px; border-radius: 7px; font-weight: 500; }

        /* ── PROGRAMMES ── */
        #hp-root .progs { background: var(--brand-dark); color: #fff; }
        #hp-root .pgrid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
        @media(max-width:860px) { #hp-root .pgrid { grid-template-columns: repeat(2, 1fr); } }
        @media(max-width:540px) { #hp-root .pgrid { grid-template-columns: 1fr; } }
        #hp-root .pcard { background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.11); border-radius: 12px; padding: 22px; transition: background .2s, border-color .2s; cursor: default; }
        #hp-root .pcard:hover { background: rgba(255,255,255,.11); border-color: rgba(110,231,183,.25); }
        #hp-root .pcard .prog-type { display: flex; align-items: center; gap: 6px; font-size: 11.5px; font-family: 'Figtree', sans-serif; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: #5EEAD4; margin-bottom: 10px; }
        #hp-root .pcard h4 { font-family: 'Figtree', sans-serif; font-size: 15.5px; font-weight: 700; color: #E2F5EE; margin-bottom: 8px; }
        #hp-root .pcard p { font-size: 13.5px; color: #7FA898; line-height: 1.65; }
        #hp-root .pcard .validity { margin-top: 13px; display: flex; align-items: center; gap: 5px; font-size: 11.5px; font-family: 'Figtree', sans-serif; font-weight: 600; color: #6EE7B7; }
        #hp-root .prog-note { margin-top: 26px; font-size: 13.5px; color: #6B9B8E; border-left: 3px solid rgba(110,231,183,.35); padding-left: 16px; line-height: 1.65; }

        /* ── PRICING ── */
        #hp-root .pricing { background: var(--white); }
        #hp-root .pricing-card { max-width: 900px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; border: 2px solid var(--brand); border-radius: 20px; overflow: hidden; box-shadow: var(--shadow-lg); }
        @media(max-width:620px) { #hp-root .pricing-card { grid-template-columns: 1fr; } }
        #hp-root .pricing-left { background: var(--brand); color: #fff; padding: 46px 42px; display: flex; flex-direction: column; }
        #hp-root .pricing-amt { font-family: 'Figtree', sans-serif; font-size: 60px; font-weight: 800; color: #fff; line-height: 1; letter-spacing: -.04em; }
        #hp-root .pricing-amt small { font-size: 20px; font-weight: 500; color: #A7F3D0; letter-spacing: 0; }
        #hp-root .pricing-vs { margin-top: 16px; font-size: 13.5px; color: #A7F3D0; line-height: 1.65; }
        #hp-root .pricing-vs b { color: #FCD34D; }
        #hp-root .pricing-vs .caveat { font-size: 11.5px; color: rgba(255,255,255,.35); display: block; margin-top: 4px; }
        #hp-root .pricing-cta { margin-top: auto; padding-top: 36px; }
        #hp-root .pricing-cta .btn { width: 100%; justify-content: center; }
        #hp-root .pricing-disclaimer { font-size: 12px; color: rgba(255,255,255,.4); margin-top: 12px; line-height: 1.5; }
        #hp-root .pricing-right { background: var(--white); padding: 46px 42px; }
        #hp-root .pricing-right h3 { font-family: 'Figtree', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--muted); margin-bottom: 22px; }
        #hp-root .pricing-right ul { list-style: none; }
        #hp-root .pricing-right li { display: flex; align-items: flex-start; gap: 11px; font-size: 14.5px; color: var(--text); padding: 11px 0; border-bottom: 1px solid var(--border); }
        #hp-root .pricing-right li:last-child { border-bottom: none; }
        #hp-root .pricing-right li i { color: var(--brand); font-size: 17px; flex-shrink: 0; margin-top: 1px; }

        /* ── MK TECH ── */
        #hp-root .mktech { background: var(--surface); }
        #hp-root .tier-label { font-family: 'Figtree', sans-serif; font-size: 11.5px; font-weight: 700; letter-spacing: .15em; text-transform: uppercase; color: var(--subtle); margin-bottom: 16px; margin-top: 34px; }
        #hp-root .mgrid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
        @media(max-width:860px) { #hp-root .mgrid { grid-template-columns: repeat(2, 1fr); } }
        @media(max-width:480px) { #hp-root .mgrid { grid-template-columns: 1fr; } }
        #hp-root .mcard { background: var(--white); border: 1px solid var(--border); border-radius: 12px; padding: 22px; position: relative; transition: border-color .2s, box-shadow .2s; }
        #hp-root .mcard:hover { border-color: var(--brand-light); box-shadow: var(--shadow-sm); }
        #hp-root .mcard.soon { background: var(--surface); border-style: dashed; }
        #hp-root .mcard .ic { width: 40px; height: 40px; border-radius: 10px; background: var(--brand-bg); color: var(--brand); display: flex; align-items: center; justify-content: center; font-size: 20px; margin-bottom: 14px; }
        #hp-root .mcard h4 { font-family: 'Figtree', sans-serif; font-size: 15px; font-weight: 700; color: var(--text); margin-bottom: 7px; }
        #hp-root .mcard p { font-size: 13px; color: var(--muted); line-height: 1.65; }
        #hp-root .mcard .soon-badge { position: absolute; top: 14px; right: 14px; }
        #hp-root .waitlist-btn { display: inline-flex; align-items: center; gap: 6px; font-size: 12.5px; font-family: 'Figtree', sans-serif; font-weight: 700; color: var(--brand); margin-top: 12px; cursor: pointer; padding: 0; background: none; border: none; transition: color .15s; }
        #hp-root .waitlist-btn:hover { color: var(--brand-dark); }
        #hp-root .waitlist-btn:focus-visible { outline: 2px solid var(--teal); outline-offset: 2px; border-radius: 4px; }

        /* ── FINAL CTA ── */
        #hp-root .final { background: var(--brand-dark); color: #fff; padding: 104px 0; text-align: center; }
        #hp-root .final h2 { font-family: 'Figtree', sans-serif; font-size: clamp(30px, 4vw, 46px); font-weight: 800; line-height: 1.1; letter-spacing: -.03em; color: #fff; margin-top: 18px; }
        #hp-root .final h2 .hi { color: #6EE7B7; }
        #hp-root .final p { color: #A7C4BA; max-width: 54ch; margin: 20px auto 36px; font-size: 17px; line-height: 1.75; }
        #hp-root .contact-row { display: flex; gap: 52px; justify-content: center; flex-wrap: wrap; margin-top: 56px; border-top: 1px solid rgba(255,255,255,.1); padding-top: 38px; }
        #hp-root .contact-row .item .k { font-family: 'Figtree', sans-serif; font-size: 11px; font-weight: 700; letter-spacing: .15em; text-transform: uppercase; color: #5EEAD4; }
        #hp-root .contact-row .item .v { font-size: 15px; color: #fff; margin-top: 7px; }

        /* ── FOOTER ── */
        #hp-root footer { background: var(--brand-dark); color: #4D7A70; border-top: 1px solid rgba(255,255,255,.07); padding: 28px 0; font-size: 13px; }
        #hp-root footer .wrap { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 14px; align-items: center; }
        #hp-root footer .footer-links { display: flex; gap: 22px; }
        #hp-root footer a { transition: color .15s; }
        #hp-root footer a:hover { color: #fff; }
        #hp-root footer a:focus-visible { outline: 2px solid var(--teal); outline-offset: 2px; border-radius: 3px; }

        /* ── RESPONSIVE ── */
        @media(max-width:640px) {
          #hp-root .pricing-left, #hp-root .pricing-right { padding: 32px 28px; }
          #hp-root .hero-badge { font-size: 10.5px; }
        }

        /* ── REDUCED MOTION ── */
        @media(prefers-reduced-motion: reduce) {
          #hp-root *, #hp-root *::before, #hp-root *::after {
            transition-duration: .01ms !important;
            animation-duration: .01ms !important;
          }
        }

        /* ── ICON RESET ── */
        #hp-root .ti { font-style: normal; }
      `}</style>

      {/* NAV */}
      <header id="hp-header">
        <div className="wrap" style={{position:"relative"}}>
          <nav>
            <a className="logo ff" href="#top">
              <div className="logo-mark">A</div>
              <span className="logo-name">Accred<b>Ready</b></span>
            </a>
            <div className="nav-right">
              <div className="navlinks">
                <a className="nav-link" href="#features">Features</a>
                <a className="nav-link" href="#how-it-works">How it works</a>
                <a className="nav-link" href="#about">About</a>
                <a className="nav-link" href="#pricing">Pricing</a>
                <button className="btn btn-primary" onClick={onSignIn}>Sign In</button>
              </div>
              <button type="button" className="menu-toggle" aria-label="Open menu" aria-expanded={menuOpen} onClick={()=>setMenuOpen(v=>!v)}>
                <i className={`ti ${menuOpen?"ti-x":"ti-menu-2"}`} aria-hidden="true"></i>
              </button>
            </div>
          </nav>
          <div className={`mobile-menu${menuOpen?" open":""}`}>
            <a href="#features" onClick={()=>setMenuOpen(false)}>Features</a>
            <a href="#how-it-works" onClick={()=>setMenuOpen(false)}>How it works</a>
            <a href="#about" onClick={()=>setMenuOpen(false)}>About</a>
            <a href="#pricing" onClick={()=>setMenuOpen(false)}>Pricing</a>
            <button type="button" onClick={()=>{setMenuOpen(false);onSignIn();}}>Sign In</button>
          </div>
        </div>
      </header>

      <span id="top"></span>

      {/* HERO */}
      <section className="hero" aria-label="AccredReady platform introduction">
        <div className="hero-inner">
          <div>
            <div className="hero-badge">
              <span className="live-dot" aria-hidden="true"></span>
              NABH Compliance Platform — India
            </div>
            <h1>
              Get accreditation-ready,{" "}
              <em className="hero-hi si">without the consultant price tag.</em>
            </h1>
            <p className="hero-sub">India's most affordable NABH compliance platform — built by a healthcare operations leader. Score your standards, find your gaps, fix them, and reach survey-readiness. For hospitals and small healthcare organisations.</p>
            <div className="hero-actions">
              <button className="btn btn-amber btn-lg" onClick={onSignIn}>
                <i className="ti ti-rocket" aria-hidden="true"></i> Start Free
              </button>
              <a className="btn btn-ghost-white btn-lg" href="#features">
                See How It Works <i className="ti ti-arrow-down" aria-hidden="true"></i>
              </a>
              <a className="btn btn-ghost-white btn-lg" href={YOUTUBE_PROMO_URL} target="_blank" rel="noopener noreferrer">
                <i className="ti ti-brand-youtube" aria-hidden="true"></i> Watch Video
              </a>
            </div>
            <div className="hero-app">
              <span className="hero-app-label">Also available on Android</span>
              <a href="https://play.google.com/store/apps/details?id=com.mktech.nabhcompliance" target="_blank" rel="noopener noreferrer">
                <img src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" alt="Get it on Google Play" />
              </a>
            </div>
            <p className="hero-social">
              <i className="ti ti-circle-check" aria-hidden="true"></i> 40+ hospitals already signed up
            </p>
            <p className="hero-note">
              <i className="ti ti-lock" aria-hidden="true"></i>
              No card required &nbsp;·&nbsp; Secured by Supabase &nbsp;·&nbsp; Email-only signup
            </p>
            <div className="hero-stats">
              <div className="hstat">
                <div className="val">15<span className="accent">+</span></div>
                <div className="label">Years healthcare operations &amp; quality management</div>
              </div>
              <div className="hstat">
                <div className="val">All</div>
                <div className="label">Types of NABH accreditation &amp; certification covered</div>
              </div>
              <div className="hstat">
                <div className="val">60<span className="accent">+</span></div>
                <div className="label">Hospitals served by our accreditation partner network</div>
              </div>
            </div>
          </div>

          <div className="hero-video" id="promo-video">
            <div className="hero-video-cap">
              <i className="ti ti-player-play" aria-hidden="true"></i>
              2-min product overview
            </div>
            <div className="hero-video-inner">
              <iframe
                src={`https://www.youtube-nocookie.com/embed/${YOUTUBE_PROMO_ID}?rel=0&modestbranding=1`}
                title="AccredReady — NABH Compliance Software for Hospitals"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                allowFullScreen
                loading="lazy"
              />
            </div>
          </div>
        </div>
      </section>

      {/* TRUST BAR */}
      <div className="trust-bar" role="region" aria-label="Trust indicators">
        <div className="wrap">
          <div className="trust-item"><i className="ti ti-rosette-discount-check" aria-hidden="true"></i> Built by a healthcare operations leader</div>
          <div className="trust-sep" aria-hidden="true"></div>
          <div className="trust-item"><i className="ti ti-building-hospital" aria-hidden="true"></i> All NABH programmes covered</div>
          <div className="trust-sep" aria-hidden="true"></div>
          <div className="trust-item"><i className="ti ti-shield-check" aria-hidden="true"></i> 50+ accreditations by our expert partner network</div>
          <div className="trust-sep" aria-hidden="true"></div>
          <div className="trust-item"><i className="ti ti-currency-rupee" aria-hidden="true"></i> From ₹499/month</div>
        </div>
      </div>

      {/* FEATURES */}
      <section className="features" id="features">
        <div className="wrap">
          <div className="sec-head">
            <span className="eyebrow"><i className="ti ti-layout-grid" aria-hidden="true"></i> The platform</span>
            <h2>Everything you need to reach <em className="si">survey-readiness</em>, <em className="si">in one place.</em></h2>
            <p>From gap analysis through to the day the assessor walks in — scoring, documentation, and corrective-action workflow, together.</p>
          </div>
          <div className="fgrid">
            <div className="fcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-checklist"></i></div>
              <h3>Score your standards</h3>
              <p>Self-assess every objective element 1–5, with built-in achievement tips on how to meet each one.</p>
            </div>
            <div className="fcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-target-arrow"></i></div>
              <h3>Instant gap analysis</h3>
              <p>See your top gaps ranked by severity and a clear readiness verdict, updated live as you score.</p>
            </div>
            <div className="fcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-tools"></i></div>
              <h3>Fix gaps with CAPA</h3>
              <p>Log corrective and preventive actions against each gap, assign owners, and attach evidence links.</p>
            </div>
            <div className="fcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-users-group"></i></div>
              <h3>Committees, KPIs &amp; audits</h3>
              <p>Ready-made committees, KPI calculators, audit toolkits, checklists, and mock-drill plans.</p>
            </div>
            <div className="fcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-layers-subtract"></i></div>
              <h3>Multiple programmes</h3>
              <p>Covers all types of NABH accreditation and certification, with more added continuously.</p>
            </div>
            <div className="fcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-robot"></i></div>
              <h3>AI assistant</h3>
              <p>Ask questions and get answers grounded strictly in the actual standards — no guesswork.</p>
            </div>
          </div>
        </div>
      </section>

      {/* HOW IT WORKS */}
      <section className="how" id="how-it-works">
        <div className="wrap">
          <div className="sec-head center">
            <span className="eyebrow"><i className="ti ti-route" aria-hidden="true"></i> Workflow</span>
            <h2>Three steps from gap to <em className="si">survey-ready.</em></h2>
            <p>AccredReady maps the entire accreditation journey into a clear, repeatable workflow — so no standard gets missed.</p>
          </div>
          <div className="steps">
            <div className="step">
              <div className="step-num" aria-hidden="true">1</div>
              <h3>Score every standard</h3>
              <p>Work chapter by chapter. Rate each objective element 1–5 with guidance built in. Your live readiness score updates in real time.</p>
            </div>
            <div className="step">
              <div className="step-num s2" aria-hidden="true">2</div>
              <h3>Identify &amp; prioritise gaps</h3>
              <p>The platform ranks your gaps by severity, generates a chapter-wise compliance report, and tells you exactly what to fix first.</p>
            </div>
            <div className="step">
              <div className="step-num s3" aria-hidden="true">3</div>
              <h3>Fix, document &amp; close</h3>
              <p>Create CAPA actions per gap, assign owners, attach evidence, and schedule committees and drills. Generate a PDF report when ready.</p>
            </div>
          </div>
        </div>
      </section>

      {/* DELIVERABLES BAND */}
      <section className="band">
        <div className="wrap">
          <div className="sec-head on-dark">
            <span className="eyebrow on-dark"><i className="ti ti-sparkles" aria-hidden="true"></i> AI-supported workflow</span>
            <h2>Not just scoring — <em className="si">real deliverables.</em></h2>
            <p>AccredReady turns your self-assessment into documents you can hand to your MD and your assessor.</p>
          </div>
          <div className="bgrid">
            <div className="bcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-file-download"></i></div>
              <h3>PDF gap &amp; CAPA reports <span className="badge-live">Live</span></h3>
              <p>Generate a clean, survey-ready PDF after gap analysis and CAPA — overall compliance, chapter-wise scores, ranked gaps, the lot.</p>
            </div>
            <div className="bcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-calendar-check"></i></div>
              <h3>Full-year scheduling <span className="badge-live">Live</span></h3>
              <p>Set your entire year of committee meetings and mock drills on a date calendar — planned, tracked, and ready to show the assessor.</p>
            </div>
            <div className="bcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-wand"></i></div>
              <h3>AI document generation <span className="badge-soon">Coming soon</span></h3>
              <p>Generate the required NABH documents right from your dashboard — drafted for you, ready to adapt.</p>
            </div>
          </div>
        </div>
      </section>

      {/* TEAM / FOUNDER */}
      <section className="team" id="about">
        <div className="wrap">
          <div className="sec-head">
            <span className="eyebrow"><i className="ti ti-users" aria-hidden="true"></i> Who's behind it</span>
            <h2>Built from the inside <em className="si">of the standard.</em></h2>
            <p>A practising NABH Quality Manager, an independent expert consulting panel, and a healthcare financing partner. Tap any name to see the full background.</p>
          </div>

          <div className={`person${openPersons[0] ? " open" : ""}`}>
            <button className="person-head" aria-expanded={openPersons[0]} aria-controls="person-body-0" onClick={() => togPerson(0)}>
              <div className="person-av" aria-hidden="true">MU</div>
              <div className="person-info">
                <h3>Dr. Mehul Upadhyay</h3>
                <div className="role">Founder · Healthcare leader &amp; certified NABH Quality Manager</div>
              </div>
              <span className="tag tag-founder">Founder</span>
              <i className="ti ti-chevron-down p-caret" aria-hidden="true"></i>
            </button>
            <div className="person-body" id="person-body-0">
              <div className="inner">
                <p>15+ years of healthcare operations experience, including international exposure in New Zealand. Currently Head of Medical Services &amp; Operations at HMP Foundation, Ankleshwar.</p>
                <p>AccredReady was built out of that direct, on-ground experience: the documentation burden, the audit cycles, and the gap between a standard's written requirement and a hospital's day-to-day reality. The platform reflects what accreditation actually looks like from inside a hospital, not from outside it.</p>
                <p className="meta-line"><b>Current role:</b> Head of Medical Services &amp; Operations, HMP Foundation (Reliance) · <b>Based in:</b> Ankleshwar, Gujarat · <b>Also:</b> IIM Kozhikode — Healthcare Management &amp; AI</p>
                <p className="meta-line founder-links">
                  <a href={FOUNDER_LINKEDIN_URL} target="_blank" rel="noopener noreferrer">
                    <i className="ti ti-brand-linkedin" aria-hidden="true"></i> LinkedIn profile
                  </a>
                  <a href={YOUTUBE_PROMO_URL} target="_blank" rel="noopener noreferrer">
                    <i className="ti ti-brand-youtube" aria-hidden="true"></i> Product video
                  </a>
                </p>
              </div>
            </div>
          </div>

          <div className={`person${openPersons[1] ? " open" : ""}`}>
            <button className="person-head" aria-expanded={openPersons[1]} aria-controls="person-body-1" onClick={() => togPerson(1)}>
              <div className="person-av" aria-hidden="true">PE</div>
              <div className="person-info">
                <h3>PMS EduCon</h3>
                <div className="role">Accreditation Partner · NABH consulting &amp; training, Ahmedabad</div>
              </div>
              <span className="tag tag-expert">Expert Panel</span>
              <i className="ti ti-chevron-down p-caret" aria-hidden="true"></i>
            </button>
            <div className="person-body" id="person-body-1">
              <div className="inner">
                <p>End-to-end NABH accreditation consulting for hospitals, SHCOs, eye hospitals, Ayush centres, dental and imaging centres — including documentation support, gap analysis, mock audits, and onsite/online training covering NABH standards, internal auditing, infection control, and fire safety.</p>
                <p className="meta-line"><b>Coverage:</b> Remote &amp; in-person, Greater Ahmedabad Area</p>
                <p className="meta-line"><b>Track record:</b> 50+ successful NABH accreditations · 50+ hospitals &amp; healthcare organisations served</p>
                <div className="hosp-chips">
                  <span>Vision Eye Care Hospital</span>
                  <span>Shiv Jyoti Eye Hospital</span>
                  <span>Atulya Super Speciality &amp; ICU</span>
                  <span>Stavya Spine Hospital</span>
                  <span>Krishna Hospital</span>
                  <span>+20 more</span>
                </div>
              </div>
            </div>
          </div>

          <div className={`person${openPersons[2] ? " open" : ""}`}>
            <button className="person-head" aria-expanded={openPersons[2]} aria-controls="person-body-2" onClick={() => togPerson(2)}>
              <div className="person-av" aria-hidden="true">RK</div>
              <div className="person-info">
                <h3>Dr. D. Rakesh Khanna, MD(AM)</h3>
                <div className="role">Accreditation Partner · Quality, Operations &amp; Accreditation Strategist</div>
              </div>
              <span className="tag tag-expert">Expert Panel</span>
              <i className="ti ti-chevron-down p-caret" aria-hidden="true"></i>
            </button>
            <div className="person-body" id="person-body-2">
              <div className="inner">
                <p>JCI, AACI, NABH, DHA &amp; MOH standards define Dr. D. Rakesh Khanna's expertise as a trusted Accreditation Partner for hospitals across India and the UAE. An AACI Certified Internal Surveyor and Senior Healthcare Quality Strategist, he has led accreditation readiness at Medcare Hospitals &amp; Medical Centres (Aster DM Healthcare, UAE) and major Indian institutions including East Coast Hospitals, Medway Hospitals, GVN Hospitals, Dr. Rela Institute &amp; Medical Centre, and Saveetha Hospital. With proven success in commissioning hospitals to full NABH/JCI compliance, optimising manpower, reducing costs, and strengthening patient safety, he delivers end-to-end accreditation readiness and operational excellence — across more than 20 accreditations.</p>
                <p className="meta-line"><b>Based:</b> Chennai, with extensive India &amp; UAE hospital experience · <b>Accreditations led:</b> 20+</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* PROGRAMMES */}
      <section className="progs">
        <div className="wrap">
          <div className="sec-head on-dark">
            <span className="eyebrow on-dark"><i className="ti ti-certificate" aria-hidden="true"></i> Programmes covered</span>
            <h2>All types of NABH accreditation &amp; certification.</h2>
            <p>AccredReady covers multiple NABH programmes — not just one. More are added continuously as the platform expands.</p>
          </div>
          <div className="pgrid">
            <div className="pcard">
              <div className="prog-type"><i className="ti ti-building-hospital" aria-hidden="true"></i> Hospital</div>
              <h4>HCO Full Accreditation</h4>
              <p>Full hospital accreditation standard, end-to-end objective element coverage.</p>
              <div className="validity"><i className="ti ti-clock" aria-hidden="true"></i> Valid for 4 years</div>
            </div>
            <div className="pcard">
              <div className="prog-type"><i className="ti ti-building-community" aria-hidden="true"></i> Small HCO</div>
              <h4>SHCO Full Accreditation</h4>
              <p>Small Healthcare Organisation accreditation, complete chapter coverage.</p>
              <div className="validity"><i className="ti ti-clock" aria-hidden="true"></i> Valid for 4 years</div>
            </div>
            <div className="pcard">
              <div className="prog-type"><i className="ti ti-building-hospital" aria-hidden="true"></i> Hospital</div>
              <h4>HCO Entry-Level Certification</h4>
              <p>Hospital entry-level certification standards — the first step towards full accreditation.</p>
              <div className="validity"><i className="ti ti-clock" aria-hidden="true"></i> Valid for 2 years</div>
            </div>
            <div className="pcard">
              <div className="prog-type"><i className="ti ti-building-community" aria-hidden="true"></i> Small HCO</div>
              <h4>SHCO Entry-Level Certification</h4>
              <p>Small Healthcare Organisation entry-level certification standards.</p>
              <div className="validity"><i className="ti ti-clock" aria-hidden="true"></i> Valid for 2 years</div>
            </div>
            <div className="pcard">
              <div className="prog-type"><i className="ti ti-eye" aria-hidden="true"></i> Eye Care</div>
              <h4>Eye Care Organisation (ECO)</h4>
              <p>Full / Entry-Level accreditation for ophthalmic and eye care hospitals.</p>
            </div>
          </div>
          <p className="prog-note">Additional NABH programmes are in active development as part of AccredReady's ongoing platform expansion.</p>
        </div>
      </section>

      {/* PRICING */}
      <section className="pricing" id="pricing">
        <div className="wrap">
          <div className="sec-head center">
            <span className="eyebrow"><i className="ti ti-tag" aria-hidden="true"></i> Pricing</span>
            <h2>A consultant costs lakhs. <span className="amber">AccredReady costs ₹499.</span></h2>
            <p>Same readiness work — gap analysis, documentation, corrective actions — at a fraction of the price.</p>
          </div>
          <div className="pricing-card">
            <div className="pricing-left">
              <div>
                <div className="pricing-amt">₹499<small> / month</small></div>
                <div className="pricing-vs">
                  vs. consultant engagements that typically run <b>₹50,000–₹2,00,000+</b>
                  <span className="caveat">Approximate market estimates — please do your own research.</span>
                </div>
              </div>
              <div className="pricing-cta">
                <button className="btn btn-amber btn-lg" onClick={onSignIn}>
                  <i className="ti ti-rocket" aria-hidden="true"></i> Start Free
                </button>
                <p className="pricing-disclaimer">No credit card required. Email-only signup. Cancel anytime.</p>
              </div>
            </div>
            <div className="pricing-right">
              <h3>Everything included</h3>
              <ul>
                <li><i className="ti ti-check" aria-hidden="true"></i> All covered NABH programmes</li>
                <li><i className="ti ti-check" aria-hidden="true"></i> Full scoring, gap analysis &amp; readiness verdict</li>
                <li><i className="ti ti-check" aria-hidden="true"></i> Committees, KPIs, audits, checklists &amp; drills</li>
                <li><i className="ti ti-check" aria-hidden="true"></i> CAPA workflow with evidence links</li>
                <li><i className="ti ti-check" aria-hidden="true"></i> PDF gap &amp; CAPA reports</li>
                <li><i className="ti ti-check" aria-hidden="true"></i> Full-year scheduling calendar</li>
                <li><i className="ti ti-check" aria-hidden="true"></i> AI assistant grounded in the standards</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* MK TECH */}
      <section className="mktech">
        <div className="wrap">
          <div className="sec-head">
            <span className="eyebrow"><i className="ti ti-brand-stackshare" aria-hidden="true"></i> More from MK Tech</span>
            <h2>From compliant to <span className="hi">digital.</span></h2>
            <p>AccredReady is one part of a wider toolkit for running a modern hospital — built by the same team, with the same patient-first, accuracy-first approach.</p>
          </div>
          <div className="tier-label">Available now</div>
          <div className="mgrid">
            <div className="mcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-users"></i></div>
              <h4>OPD Queue Manager</h4>
              <p>Digital patient flow from entry to exit — no more blank-form re-entry at reception.</p>
            </div>
            <div className="mcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-calendar-event"></i></div>
              <h4>Appointment Scheduler</h4>
              <p>QR-based clinic booking with WhatsApp confirmations. Privacy-first, no patient data stored.</p>
            </div>
            <div className="mcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-chart-bar"></i></div>
              <h4>Hospital Dashboard</h4>
              <p>Real-time KPI monitoring across departments — see performance and revenue at a glance.</p>
            </div>
            <div className="mcard">
              <div className="ic" aria-hidden="true"><i className="ti ti-device-laptop"></i></div>
              <h4>Website &amp; App Development</h4>
              <p>Custom hospital websites and mobile apps, built and shipped end-to-end.</p>
            </div>
          </div>
          <div className="tier-label">Coming soon</div>
          <div className="mgrid">
            <div className="mcard soon">
              <span className="soon-badge badge-soon-warm">Coming soon</span>
              <div className="ic" aria-hidden="true"><i className="ti ti-bed"></i></div>
              <h4>IPD Manager</h4>
              <p>Inpatient admission-to-discharge workflow, built to order for hospitals that need it.</p>
              <button className="waitlist-btn" onClick={() => wl("IPD Manager")} aria-label="Join waitlist for IPD Manager">
                <i className="ti ti-bell" aria-hidden="true"></i> Join Waitlist
              </button>
            </div>
            <div className="mcard soon">
              <span className="soon-badge badge-soon-warm">Coming soon</span>
              <div className="ic" aria-hidden="true"><i className="ti ti-report-money"></i></div>
              <h4>Revenue Leakage Self-Audit</h4>
              <p>Find where your hospital is losing revenue — and exactly how to plug each leak.</p>
              <button className="waitlist-btn" onClick={() => wl("Revenue Leakage Self-Audit")} aria-label="Join waitlist for Revenue Leakage Self-Audit">
                <i className="ti ti-bell" aria-hidden="true"></i> Join Waitlist
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* FINAL CTA */}
      <section className="final">
        <div className="wrap">
          <span className="eyebrow on-dark" style={{justifyContent: "center"}}>
            <i className="ti ti-rosette-discount-check" aria-hidden="true"></i> AccredReady
          </span>
          <h2>Accreditation readiness, <em className="si">built and backed</em> end to end.</h2>
          <p>Software from a practising NABH Quality Manager. Consulting from an independent expert network. Financing from a dedicated healthcare partner.</p>
          <button className="btn btn-amber btn-lg" onClick={onSignIn}>
            <i className="ti ti-rocket" aria-hidden="true"></i> Start Free
          </button>
          <div className="contact-row">
            <div className="item"><div className="k">Website</div><div className="v">accredready.in</div></div>
            <div className="item"><div className="k">Email</div><div className="v">doctor@accredready.in</div></div>
            <div className="item"><div className="k">Location</div><div className="v">Gujarat — India</div></div>
          </div>
        </div>
      </section>

      <footer>
        <div className="wrap">
          <span>© 2026 AccredReady — NABH Compliance Platform · MK Tech</span>
          <div className="footer-links">
            <a href="mailto:doctor@accredready.in">Contact</a>
            <a href="/terms.html">Terms</a>
            <a href="/privacy.html">Privacy</a>
          </div>
        </div>
      </footer>
    </div>
  );
}
