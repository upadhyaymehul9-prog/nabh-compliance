// src/components/GennieMascot.jsx
// Gennie — AccredReady's SHCO Full assistant mascot.
// Two exports: a head-only crop for the floating launcher button,
// and the full lamp-and-smoke figure for the greeting panel.

const HEAD_VB = { w: 130, h: 120 };
const FULL_VB = { w: 320, h: 400 };

export function GennieHead({ size = 56, title = "Gennie" }) {
  return (
    <svg
      width={size}
      height={size * (HEAD_VB.h / HEAD_VB.w)}
      viewBox={`0 0 ${HEAD_VB.w} ${HEAD_VB.h}`}
      role="img"
      aria-label={title}
      style={{ display: "block", flexShrink: 0 }}
    >
      {/* bald head + jaw */}
      <path
        d="M 10 45 C 10 -10 120 -10 120 45 C 120 100 100 110 65 110 C 30 110 10 100 10 45 Z"
        fill="#7e57c2"
      />
      <ellipse cx="45" cy="15" rx="16" ry="9" fill="#fff" opacity="0.12" />

      {/* ears + gold hoop earrings */}
      <ellipse cx="7" cy="62" rx="8" ry="12" fill="#7e57c2" />
      <ellipse cx="123" cy="62" rx="8" ry="12" fill="#7e57c2" />
      <circle cx="7" cy="74" r="6" fill="none" stroke="#ffc94d" strokeWidth="2.2" />
      <circle cx="123" cy="74" r="6" fill="none" stroke="#ffc94d" strokeWidth="2.2" />

      {/* eyebrows */}
      <path d="M 20 58 Q 34 53 46 60" stroke="#1a1040" strokeWidth="3.5" fill="none" strokeLinecap="round" />
      <path d="M 110 58 Q 96 53 84 60" stroke="#1a1040" strokeWidth="3.5" fill="none" strokeLinecap="round" />

      {/* eyes */}
      <ellipse cx="34" cy="72" rx="7" ry="8.5" fill="#fff" />
      <circle cx="36" cy="73" r="4" fill="#1a1040" />
      <circle cx="37.3" cy="71.3" r="1.3" fill="#fff" />
      <ellipse cx="96" cy="72" rx="7" ry="8.5" fill="#fff" />
      <circle cx="94" cy="73" r="4" fill="#1a1040" />
      <circle cx="95.3" cy="71.3" r="1.3" fill="#fff" />

      {/* nose */}
      <ellipse cx="65" cy="86" rx="5" ry="7" fill="#5e35b1" />

      {/* smile */}
      <path d="M 44 100 Q 65 111 86 100 Q 65 124 44 100 Z" fill="#1a1040" />
      <path d="M 53 108 Q 65 114 77 108 Q 65 119 53 108 Z" fill="#ef9a9a" />
    </svg>
  );
}

export function GennieFull({ size = 132, title = "Gennie" }) {
  return (
    <svg
      width={size}
      height={size * (FULL_VB.h / FULL_VB.w)}
      viewBox={`0 0 ${FULL_VB.w} ${FULL_VB.h}`}
      role="img"
      aria-label={title}
      style={{ display: "block", margin: "0 auto", flexShrink: 0 }}
    >
      <defs>
        <radialGradient id="gn-sk" cx="40%" cy="32%" r="80%">
          <stop offset="0%" stopColor="#b39ddb" />
          <stop offset="50%" stopColor="#7e57c2" />
          <stop offset="100%" stopColor="#4527a0" />
        </radialGradient>
        <linearGradient id="gn-gd" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="#fff3c4" />
          <stop offset="50%" stopColor="#ffc94d" />
          <stop offset="100%" stopColor="#e08600" />
        </linearGradient>
        <linearGradient id="gn-tail" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor="#7e57c2" />
          <stop offset="60%" stopColor="#4dd0e1" />
          <stop offset="100%" stopColor="#4dd0e1" stopOpacity="0.2" />
        </linearGradient>
      </defs>

      <path d="M 210 335 C 230 290 190 260 160 240 C 130 260 150 300 210 335 Z" fill="url(#gn-tail)" />
      <path d="M 210 335 C 170 320 120 280 140 240 L 180 240 C 190 280 180 320 210 335 Z" fill="url(#gn-tail)" opacity="0.6" />

      <path d="M 160 280 C 120 270 108 250 128 240 L 192 240 C 212 250 200 270 160 280 Z" fill="url(#gn-sk)" />

      <path d="M 110 165 Q 60 186 70 230 Q 70 256 95 256 Q 125 256 119 235 Q 110 200 120 180 Z" fill="url(#gn-sk)" />
      <path d="M 210 165 Q 260 186 250 230 Q 250 256 225 256 Q 195 256 201 235 Q 210 200 200 180 Z" fill="url(#gn-sk)" />

      <ellipse cx="90" cy="256" rx="15" ry="12" fill="url(#gn-sk)" />
      <ellipse cx="230" cy="256" rx="15" ry="12" fill="url(#gn-sk)" />
      <rect x="76" y="234" width="28" height="9" rx="4" fill="url(#gn-gd)" />
      <rect x="216" y="234" width="28" height="9" rx="4" fill="url(#gn-gd)" />

      <path d="M 100 186 Q 112 195 125 180" stroke="url(#gn-gd)" strokeWidth="7" fill="none" strokeLinecap="round" />
      <path d="M 220 186 Q 208 195 195 180" stroke="url(#gn-gd)" strokeWidth="7" fill="none" strokeLinecap="round" />

      <path d="M 110 160 Q 160 140 210 160 L 195 244 Q 160 264 125 244 Z" fill="url(#gn-sk)" />

      <path d="M 125 185 Q 160 200 195 185" stroke="#4527a0" strokeWidth="3" fill="none" strokeLinecap="round" />
      <path d="M 160 185 L 160 230" stroke="#4527a0" strokeWidth="2.5" fill="none" strokeLinecap="round" />
      <path d="M 148 205 Q 160 210 172 205" stroke="#4527a0" strokeWidth="2" fill="none" strokeLinecap="round" />
      <path d="M 148 220 Q 160 225 172 220" stroke="#4527a0" strokeWidth="2" fill="none" strokeLinecap="round" />

      <path d="M 116 165 C 130 195 190 195 204 165" stroke="url(#gn-gd)" strokeWidth="4.5" fill="none" strokeDasharray="6 3" strokeLinecap="round" />
      <circle cx="160" cy="186" r="12" fill="url(#gn-gd)" />
      <circle cx="160" cy="186" r="9" fill="#00e5ff" opacity="0.5" />
      <circle cx="160" cy="186" r="6" fill="#00e5ff" />
      <circle cx="158" cy="184" r="2.5" fill="#e0f7fa" />

      <path d="M 110 90 C 110 35 210 35 210 90 C 210 145 190 155 160 155 C 130 155 110 145 110 90 Z" fill="url(#gn-sk)" />
      <ellipse cx="145" cy="55" rx="18" ry="10" fill="#fff" opacity="0.12" />

      <ellipse cx="107" cy="112" rx="9" ry="13" fill="url(#gn-sk)" />
      <ellipse cx="213" cy="112" rx="9" ry="13" fill="url(#gn-sk)" />
      <circle cx="107" cy="125" r="7" fill="none" stroke="url(#gn-gd)" strokeWidth="2.5" />
      <circle cx="213" cy="125" r="7" fill="none" stroke="url(#gn-gd)" strokeWidth="2.5" />

      <path d="M 122 93 Q 138 88 152 95" stroke="#1a1040" strokeWidth="4" fill="none" strokeLinecap="round" />
      <path d="M 198 93 Q 182 88 168 95" stroke="#1a1040" strokeWidth="4" fill="none" strokeLinecap="round" />

      <ellipse cx="138" cy="108" rx="8" ry="10" fill="#fff" />
      <circle cx="140" cy="109" r="4.5" fill="#1a1040" />
      <circle cx="141.5" cy="107" r="1.5" fill="#fff" />
      <ellipse cx="182" cy="108" rx="8" ry="10" fill="#fff" />
      <circle cx="180" cy="109" r="4.5" fill="#1a1040" />
      <circle cx="181.5" cy="107" r="1.5" fill="#fff" />

      <path d="M 131 116 Q 138 120 145 116" stroke="#1a1040" strokeWidth="1.5" fill="none" opacity="0.5" strokeLinecap="round" />
      <path d="M 189 116 Q 182 120 175 116" stroke="#1a1040" strokeWidth="1.5" fill="none" opacity="0.5" strokeLinecap="round" />

      <ellipse cx="160" cy="122" rx="5.5" ry="8" fill="#5e35b1" />

      <path d="M 138 136 Q 160 148 182 136 Q 160 164 138 136 Z" fill="#1a1040" />
      <path d="M 148 145 Q 160 152 172 145 Q 160 158 148 145 Z" fill="#ef9a9a" />

      <path d="M 132 134 Q 130 140 135 146" stroke="#1a1040" strokeWidth="2" fill="none" strokeLinecap="round" opacity="0.6" />
      <path d="M 188 134 Q 190 140 185 146" stroke="#1a1040" strokeWidth="2" fill="none" strokeLinecap="round" opacity="0.6" />

      <g transform="translate(10, 0)">
        <path d="M 95 365 C 50 350 60 395 110 380" stroke="url(#gn-gd)" strokeWidth="7" fill="none" strokeLinecap="round" />
        <path d="M 115 385 L 145 385 L 140 375 L 120 375 Z" fill="url(#gn-gd)" />
        <ellipse cx="130" cy="365" rx="40" ry="22" fill="url(#gn-gd)" />
        <ellipse cx="130" cy="365" rx="32" ry="15" fill="none" stroke="#e08600" strokeWidth="2" opacity="0.4" />
        <path d="M 115 345 L 145 345 Q 130 330 115 345" fill="url(#gn-gd)" />
        <circle cx="130" cy="334" r="5" fill="url(#gn-gd)" />
        <path d="M 160 365 Q 200 370 200 335 Q 185 345 165 348 Z" fill="url(#gn-gd)" />
        <ellipse cx="200" cy="335" rx="7" ry="4" fill="#0b1220" />
      </g>
    </svg>
  );
}
