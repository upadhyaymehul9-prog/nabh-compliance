#!/usr/bin/env python3
"""Render LinkedIn-style NABH OE posters (AAC chapter) to PNG via Chrome headless."""

from __future__ import annotations

import json
import html
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OES_PATH = ROOT / "aac_oes.json"
OUT_DIR = ROOT
CHROME = "google-chrome"
WIDTH = 1080
HEIGHT = 1350

LEVEL_BADGE = {
    "Core": ("#c62828", "#ffebee"),
    "Commitment": ("#1565c0", "#e3f2fd"),
    "Achievement": ("#2e7d32", "#e8f5e9"),
    "Excellence": ("#6a1b9a", "#f3e5f5"),
}

MISTAKE_COLORS = ["#1565c0", "#2e7d32", "#6a1b9a", "#e65100"]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def poster_html(oe: dict) -> str:
    lvl = oe["level"]
    accent, tint = LEVEL_BADGE[lvl]
    mistakes = oe["mistakes"]
    bullets = oe["bullets"]
    steps = oe["steps"]

    mistake_html = []
    for i, m in enumerate(mistakes):
        color = MISTAKE_COLORS[i % len(MISTAKE_COLORS)]
        mistake_html.append(
            f"""
            <div class="mistake">
              <div class="num" style="background:{color}">{i+1}</div>
              <div class="body">
                <div class="mtitle" style="color:{color}">{esc(m['title'])}</div>
                <div class="mdetail">{esc(m['detail'])}</div>
              </div>
            </div>"""
        )

    bullet_html = "".join(
        f'<div class="bullet"><span class="dot"></span><span>{esc(b)}</span></div>'
        for b in bullets
    )
    step_html = "".join(
        f"""
        <div class="step">
          <div class="stepnum">{i+1}</div>
          <div class="steptext">{esc(s)}</div>
        </div>"""
        for i, s in enumerate(steps)
    )

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&family=Source+Serif+4:opsz,wght@8..60,600&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    width: {WIDTH}px; height: {HEIGHT}px; overflow: hidden;
    font-family: 'Manrope', system-ui, sans-serif;
    background: #f7fafc;
    color: #0d1f33;
  }}
  .poster {{
    width: {WIDTH}px; height: {HEIGHT}px;
    padding: 42px 44px 28px;
    display: flex; flex-direction: column;
    background:
      radial-gradient(1200px 500px at 100% -10%, #d7ebf8 0%, transparent 55%),
      radial-gradient(900px 400px at -10% 30%, #e8f5e9 0%, transparent 50%),
      linear-gradient(180deg, #ffffff 0%, #f3f7fb 100%);
    position: relative;
  }}
  .poster::before {{
    content: '';
    position: absolute; inset: 18px;
    border: 1.5px solid rgba(21,101,192,0.12);
    border-radius: 18px; pointer-events: none;
  }}
  .topline {{
    display: flex; align-items: flex-start; justify-content: space-between;
    gap: 24px; margin-bottom: 18px;
  }}
  .brand-line {{
    font-size: 18px; font-weight: 800; letter-spacing: 0.08em;
    color: #0d1f33; text-transform: uppercase;
  }}
  .code {{
    font-size: 54px; font-weight: 800; line-height: 1;
    color: {accent}; margin-top: 4px;
  }}
  .level-pill {{
    align-self: flex-start;
    background: {tint}; color: {accent};
    border: 1.5px solid {accent}33;
    font-size: 14px; font-weight: 800; letter-spacing: 0.06em;
    padding: 8px 14px; border-radius: 999px; text-transform: uppercase;
  }}
  .headline {{
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 30px; font-weight: 600; line-height: 1.25;
    color: #0a1828; margin: 8px 0 16px; max-width: 920px;
  }}
  .std {{
    font-size: 14px; color: #3a5870; margin-bottom: 14px; line-height: 1.45;
  }}
  .std strong {{ color: #1565c0; }}
  .oe-box {{
    background: #0d1f33; color: #eef4f9;
    border-radius: 14px; padding: 16px 18px; margin-bottom: 18px;
    box-shadow: 0 10px 30px rgba(13,31,51,0.12);
  }}
  .oe-label {{
    font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase;
    color: #4fc3f7; font-weight: 800; margin-bottom: 6px;
  }}
  .oe-text {{ font-size: 16px; line-height: 1.45; font-weight: 500; }}
  .bullets {{ margin-bottom: 16px; }}
  .bullet {{
    display: flex; gap: 10px; align-items: flex-start;
    font-size: 14px; line-height: 1.4; color: #1e3a52; margin-bottom: 7px;
  }}
  .dot {{
    width: 8px; height: 8px; border-radius: 50%; background: #c62828;
    margin-top: 6px; flex: 0 0 auto;
  }}
  .section-title {{
    font-size: 13px; font-weight: 800; letter-spacing: 0.1em;
    text-transform: uppercase; color: #1565c0; margin: 4px 0 10px;
  }}
  .mistakes {{
    display: flex; flex-direction: column; gap: 10px;
    flex: 1; min-height: 0;
  }}
  .mistake {{
    display: flex; gap: 12px; align-items: flex-start;
    background: rgba(255,255,255,0.85);
    border: 1px solid #d7e6f2; border-radius: 12px;
    padding: 12px 14px;
  }}
  .num {{
    width: 34px; height: 34px; border-radius: 10px;
    color: white; font-weight: 800; font-size: 16px;
    display: flex; align-items: center; justify-content: center;
    flex: 0 0 auto;
  }}
  .mtitle {{ font-size: 15px; font-weight: 800; letter-spacing: 0.02em; }}
  .mdetail {{ font-size: 13.5px; color: #334e68; margin-top: 2px; line-height: 1.35; }}
  .first {{
    margin-top: 16px;
    background: #e8f5e9; border: 1.5px solid #a5d6a7;
    border-radius: 14px; padding: 14px 16px;
  }}
  .first h3 {{
    font-size: 13px; font-weight: 800; letter-spacing: 0.08em;
    color: #2e7d32; text-transform: uppercase; margin-bottom: 10px;
  }}
  .steps {{ display: flex; gap: 10px; }}
  .step {{
    flex: 1; background: white; border-radius: 10px;
    padding: 10px; border: 1px solid #c8e6c9;
  }}
  .stepnum {{
    width: 22px; height: 22px; border-radius: 50%;
    background: #2e7d32; color: white; font-size: 12px; font-weight: 800;
    display: flex; align-items: center; justify-content: center; margin-bottom: 6px;
  }}
  .steptext {{ font-size: 12.5px; line-height: 1.35; color: #1b5e20; font-weight: 600; }}
  .footer {{
    margin-top: 16px;
    background: #0d1f33; color: white; border-radius: 14px;
    padding: 14px 18px; display: flex; align-items: center; justify-content: space-between;
    gap: 12px;
  }}
  .footer-left {{ font-size: 12px; color: #9fb6c9; line-height: 1.35; }}
  .footer-mid {{ text-align: center; }}
  .logo {{
    font-size: 18px; font-weight: 800; color: #f0d070; letter-spacing: 0.02em;
  }}
  .tag {{ font-size: 11px; color: #c8dcea; margin-top: 2px; }}
  .footer-right {{ text-align: right; font-size: 12px; color: #9fb6c9; }}
  .url {{ color: #4fc3f7; font-weight: 700; }}
  .tags {{
    margin-top: 8px; font-size: 11px; color: #5b7a94; text-align: center;
    letter-spacing: 0.02em;
  }}
</style>
</head>
<body>
  <div class="poster">
    <div class="topline">
      <div>
        <div class="brand-line">NABH Standard</div>
        <div class="code">{esc(oe['display'])}</div>
      </div>
      <div class="level-pill">{esc(lvl)}</div>
    </div>

    <div class="headline">{esc(oe['headline'])}</div>
    <div class="std"><strong>AAC.{oe['std']}</strong> — {esc(oe['standard'])}</div>

    <div class="oe-box">
      <div class="oe-label">Objective Element {esc(oe['code'])}</div>
      <div class="oe-text">{esc(oe['text'])}</div>
    </div>

    <div class="bullets">{bullet_html}</div>

    <div class="section-title">Common gaps hospitals miss</div>
    <div class="mistakes">
      {''.join(mistake_html)}
    </div>

    <div class="first">
      <h3>Simple first step</h3>
      <div class="steps">{step_html}</div>
    </div>

    <div class="footer">
      <div class="footer-left">One NABH standard<br/>explained every day</div>
      <div class="footer-mid">
        <div class="logo">AccredReady</div>
        <div class="tag">Quality Today, Accreditation Tomorrow.</div>
      </div>
      <div class="footer-right">www.accredready.in<br/><span class="url">HCO 6th Edition</span></div>
    </div>
    <div class="tags">#NABH #HealthcareQuality #HospitalAccreditation #NABH6thEdition #QualityImprovement</div>
  </div>
</body>
</html>
"""


def render_one(oe: dict, out_png: Path) -> None:
    with tempfile.TemporaryDirectory() as td:
        html_path = Path(td) / "poster.html"
        html_path.write_text(poster_html(oe), encoding="utf-8")
        # Chrome headless screenshot
        subprocess.run(
            [
                CHROME,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--force-device-scale-factor=1",
                f"--screenshot={out_png}",
                f"--window-size={WIDTH},{HEIGHT}",
                f"file://{html_path}",
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


def main() -> None:
    oes = json.loads(OES_PATH.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i, oe in enumerate(oes, 1):
        code = oe["code"].lower().replace(".", "-")
        out = OUT_DIR / f"nabh-{code}-linkedin-poster.png"
        render_one(oe, out)
        print(f"[{i}/{len(oes)}] wrote {out.name}", flush=True)
    print("DONE", len(oes))


if __name__ == "__main__":
    main()
