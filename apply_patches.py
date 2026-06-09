#!/usr/bin/env python3
"""
Apply patches to App.js
Usage: python apply_patches.py src/App.js
"""
import sys

if len(sys.argv) < 2:
    print("Usage: python apply_patches.py path/to/App.js")
    sys.exit(1)

filepath = sys.argv[1]

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Read {len(content)} chars from {filepath}")

patches = [

# ── PATCH 1: recharts import ──────────────────────────────────────
(
'import { useState, useEffect, useCallback } from "react";\nimport { createClient } from "@supabase/supabase-js";',
'import { useState, useEffect, useCallback } from "react";\nimport { createClient } from "@supabase/supabase-js";\nimport { LineChart, Line, BarChart, Bar, XAxis, YAxis, Tooltip, ReferenceLine, ResponsiveContainer, CartesianGrid } from "recharts";'
),

# ── PATCH 2: MONTHS_SHORT constant ───────────────────────────────
(
'const sevColor = s => s==="CRITICAL"?T.red:s==="HIGH"?T.orange:s==="MEDIUM"?T.gold:T.green;',
'const sevColor = s => s==="CRITICAL"?T.red:s==="HIGH"?T.orange:s==="MEDIUM"?T.gold:T.green;\nconst MONTHS_SHORT = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];'
),

# ── PATCH 3: search state in ScoringScreen ────────────────────────
(
'  const [filter,setFilter]=useState("ALL"); const [chFilter,setChFilter]=useState("ALL");\n  const [toast,setToast]=useState(null); const [saving,setSaving]=useState({});',
'  const [filter,setFilter]=useState("ALL"); const [chFilter,setChFilter]=useState("ALL");\n  const [search,setSearch]=useState("");\n  const [toast,setToast]=useState(null); const [saving,setSaving]=useState({});'
),

# ── PATCH 4: search in filtered ───────────────────────────────────
(
'  const filtered=oes.filter(oe=>{const lm=filter==="ALL"||oe.level===filter;const cm=chFilter==="ALL"||oe.chapter===chFilter;return lm&&cm;});',
'  const filtered=oes.filter(oe=>{const lm=filter==="ALL"||oe.level===filter;const cm=chFilter==="ALL"||oe.chapter===chFilter;const sm=!search||oe.id.toLowerCase().includes(search.toLowerCase())||(oe.text||"").toLowerCase().includes(search.toLowerCase());return lm&&cm&&sm;});'
),

# ── PATCH 5: replace filter bar with search+filter bar ────────────
(
'      <div style={{display:"flex",gap:8,marginBottom:14,flexWrap:"wrap"}}>\n        <div style={{display:"flex",gap:4,flexWrap:"wrap"}}>{levels.map(l=><button key={l} onClick={()=>setFilter(l)} style={{padding:"5px 12px",borderRadius:8,fontSize:10,cursor:"pointer",background:filter===l?T.goldD:"transparent",border:`1px solid ${filter===l?T.gold:T.border}`,color:filter===l?T.goldL:T.muted}}>{l}</button>)}</div>\n        <select value={chFilter} onChange={e=>setChFilter(e.target.value)} style={{padding:"5px 10px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:10}}>{chapters.map(c=><option key={c} value={c}>{c}</option>)}</select>\n      </div>',
'      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 14px",marginBottom:14}}>\n        <input value={search} onChange={e=>setSearch(e.target.value)} placeholder="Search OEs by ID or text (e.g. \'hand hygiene\', \'COP.1.a\', \'fall risk\')..." style={{width:"100%",padding:"9px 12px",borderRadius:8,border:`1px solid ${search?T.gold:T.border}`,background:T.panel2,color:T.text,fontSize:12,marginBottom:10,boxSizing:"border-box"}}/>\n        <div style={{display:"flex",gap:8,flexWrap:"wrap",alignItems:"center"}}>\n          <div style={{display:"flex",gap:4,flexWrap:"wrap"}}>{levels.map(l=><button key={l} onClick={()=>setFilter(l)} style={{padding:"5px 12px",borderRadius:8,fontSize:10,cursor:"pointer",background:filter===l?T.goldD:"transparent",border:`1px solid ${filter===l?T.gold:T.border}`,color:filter===l?T.goldL:T.muted}}>{l}</button>)}</div>\n          <select value={chFilter} onChange={e=>setChFilter(e.target.value)} style={{padding:"5px 10px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:10}}>{chapters.map(c=><option key={c} value={c}>{c}</option>)}</select>\n          {(search||filter!=="ALL"||chFilter!=="ALL")&&(<button onClick={()=>{setSearch("");setFilter("ALL");setChFilter("ALL");}} style={{padding:"4px 10px",borderRadius:6,fontSize:9,cursor:"pointer",background:T.redD,border:`1px solid ${T.red}30`,color:T.red}}>X Clear</button>)}\n          <span style={{fontSize:9,color:T.muted,marginLeft:"auto"}}>{filtered.length} OEs shown</span>\n        </div>\n      </div>'
),

# ── PATCH 6: empty search message ────────────────────────────────
(
'        {filtered.length===0&&<div style={{textAlign:"center",color:T.muted,padding:"30px",fontSize:12}}>No OEs match this filter.</div>}',
'        {filtered.length===0&&<div style={{textAlign:"center",color:T.muted,padding:"30px",fontSize:12}}>{search?"No OEs match your search. Try different keywords or clear filters.":"No OEs match this filter."}</div>}'
),

# ── PATCH 7: KpiTrendChart + AuditComplianceChart components ──────
(
'function LoginScreen({ onLogin, initialError }) {',
r'''function KpiTrendChart({ history, target, unit }) {
  if (!history || history.length === 0) return (
    <div style={{background:T.panel2,borderRadius:8,padding:"20px",textAlign:"center",border:`1px solid ${T.border}`,marginBottom:12}}>
      <div style={{fontSize:28,marginBottom:8}}>📈</div>
      <div style={{fontSize:11,color:T.muted}}>No data yet. Enter monthly values above to see your trend chart.</div>
    </div>
  );
  const chartData=[...history].sort((a,b)=>a.year!==b.year?a.year-b.year:a.month-b.month).slice(-12).map(d=>({name:`${MONTHS_SHORT[d.month-1]} ${String(d.year).slice(2)}`,value:d.value,capa:d.capa_required}));
  const vals=chartData.map(d=>d.value);const minVal=Math.min(...vals);const maxVal=Math.max(...vals);const pad=Math.max((maxVal-minVal)*0.2,1);
  const yMin=Math.max(0,Math.floor((minVal-pad)*10)/10);const yMax=Math.ceil((Math.max(maxVal,parseFloat(target)||0)+pad)*10)/10;
  const CustomDot=(props)=>{const{cx,cy,payload}=props;if(!payload.capa)return <circle cx={cx} cy={cy} r={3} fill={T.gold}/>;return <circle cx={cx} cy={cy} r={5} fill={T.orange} stroke={T.bg} strokeWidth={1.5}/>;};
  const TT=({active,payload,label})=>{if(!active||!payload||!payload.length)return null;const d=payload[0].payload;return(<div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:8,padding:"8px 12px",fontSize:10}}><div style={{color:T.gold,fontWeight:700,marginBottom:4}}>{label}</div><div style={{color:T.white}}>Value: <strong style={{color:T.goldL}}>{d.value} {unit}</strong></div>{target&&<div style={{color:T.green,marginTop:2}}>Target: {target}</div>}{d.capa&&<div style={{color:T.orange,marginTop:2}}>CAPA raised</div>}</div>);};
  return(<div style={{background:T.panel2,border:`1px solid ${T.border}`,borderRadius:8,padding:"12px 8px 8px 0",marginBottom:12}}><div style={{fontSize:9,color:T.gold,letterSpacing:1,marginBottom:8,paddingLeft:12,display:"flex",gap:12}}><span>TREND — last {chartData.length} months</span>{target&&<span style={{color:T.green}}>Target: {target} {unit}</span>}</div><ResponsiveContainer width="100%" height={160}><LineChart data={chartData} margin={{top:4,right:16,left:0,bottom:0}}><CartesianGrid strokeDasharray="2 4" stroke={T.border} vertical={false}/><XAxis dataKey="name" tick={{fontSize:8,fill:T.muted}} axisLine={false} tickLine={false}/><YAxis domain={[yMin,yMax]} tick={{fontSize:8,fill:T.muted}} axisLine={false} tickLine={false} width={36}/><Tooltip content={<TT/>}/>{target&&<ReferenceLine y={parseFloat(target)} stroke={T.green} strokeDasharray="4 3" strokeWidth={1.5}/>}<Line type="monotone" dataKey="value" stroke={T.gold} strokeWidth={2.5} dot={<CustomDot/>} activeDot={{r:5,fill:T.goldL}}/></LineChart></ResponsiveContainer><div style={{display:"flex",gap:14,paddingLeft:12,marginTop:6,fontSize:8,color:T.muted}}><span style={{color:T.gold}}>Value</span>{target&&<span style={{color:T.green}}>-- Target</span>}<span style={{color:T.orange}}>o CAPA</span></div></div>);
}

function AuditComplianceChart({ records }) {
  if (!records || records.length === 0) return (
    <div style={{background:T.panel2,borderRadius:8,padding:"20px",textAlign:"center",border:`1px solid ${T.border}`,marginBottom:12}}>
      <div style={{fontSize:28,marginBottom:8}}>📊</div>
      <div style={{fontSize:11,color:T.muted}}>No records yet. Record an audit to see compliance trends.</div>
    </div>
  );
  const getBarColor=(pct)=>pct>=80?T.green:pct>=60?T.orange:T.red;
  const chartData=[...records].filter(r=>r.sample_size>0&&r.compliant_count!==null).sort((a,b)=>new Date(a.audit_date)-new Date(b.audit_date)).slice(-12).map(r=>({name:new Date(r.audit_date).toLocaleDateString("en-IN",{day:"2-digit",month:"short"}),pct:Math.round((r.compliant_count/r.sample_size)*100),capa:r.capa_raised}));
  if(chartData.length===0)return(<div style={{background:T.panel2,borderRadius:8,padding:"12px",textAlign:"center",border:`1px solid ${T.border}`,fontSize:10,color:T.muted,marginBottom:12}}>Enter sample size and compliant count when recording audits to see charts.</div>);
  const TT=({active,payload,label})=>{if(!active||!payload||!payload.length)return null;const d=payload[0].payload;return(<div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:8,padding:"8px 12px",fontSize:10}}><div style={{color:T.gold,fontWeight:700,marginBottom:4}}>{label}</div><div style={{color:getBarColor(d.pct),fontWeight:700,fontSize:13}}>{d.pct}%</div>{d.capa&&<div style={{color:T.orange,marginTop:3}}>CAPA raised</div>}</div>);};
  return(<div style={{background:T.panel2,border:`1px solid ${T.border}`,borderRadius:8,padding:"12px 8px 8px 0",marginBottom:12}}><div style={{fontSize:9,color:T.gold,letterSpacing:1,marginBottom:8,paddingLeft:12,display:"flex",gap:12}}><span>COMPLIANCE TREND — last {chartData.length} audits</span><span style={{color:T.green}}>Target: 80%</span></div><ResponsiveContainer width="100%" height={150}><BarChart data={chartData} margin={{top:4,right:16,left:0,bottom:0}}><CartesianGrid strokeDasharray="2 4" stroke={T.border} vertical={false}/><XAxis dataKey="name" tick={{fontSize:8,fill:T.muted}} axisLine={false} tickLine={false}/><YAxis domain={[0,100]} tick={{fontSize:8,fill:T.muted}} axisLine={false} tickLine={false} width={30} tickFormatter={v=>`${v}%`}/><Tooltip content={<TT/>}/><ReferenceLine y={80} stroke={T.green} strokeDasharray="4 3" strokeWidth={1.5}/><Bar dataKey="pct" radius={[3,3,0,0]} shape={(props)=>{const{x,y,width,height,value}=props;return <rect x={x} y={y} width={Math.max(width,4)} height={Math.max(height,1)} rx={3} fill={getBarColor(value)} fillOpacity={0.85}/>;}} /></BarChart></ResponsiveContainer><div style={{display:"flex",gap:14,paddingLeft:12,marginTop:6,fontSize:8,color:T.muted}}><span style={{color:T.green}}>Good (80%+)</span><span style={{color:T.orange}}>Fair (60-79%)</span><span style={{color:T.red}}>Critical</span></div></div>);
}

function LoginScreen({ onLogin, initialError }) {'''
),

# ── PATCH 8: Wire KpiTrendChart in KPIs history ───────────────────
(
'                  {/* History */}\n                  {history.length>0&&(\n                    <div style={{borderTop:`1px solid ${T.border}`,paddingTop:12}}>\n                      <div style={{fontSize:9,color:T.muted,marginBottom:8,letterSpacing:1}}>TRACKING HISTORY ({history.length} entries)</div>',
'                  {/* History */}\n                  {history.length>0&&(\n                    <div style={{borderTop:`1px solid ${T.border}`,paddingTop:12}}>\n                      <KpiTrendChart history={history} target={k.benchmark_value||k.target} unit={k.unit}/>\n                      <div style={{fontSize:9,color:T.muted,marginBottom:8,letterSpacing:1,marginTop:12}}>TRACKING HISTORY ({history.length} entries)</div>'
),

# ── PATCH 9: Wire AuditComplianceChart in NABH audit records ──────
(
'                      {records.length>0&&(\n                        <div>\n                          <div style={{fontSize:9,color:T.muted,marginBottom:6,letterSpacing:1}}>AUDIT RECORDS ({records.length})</div>',
'                      {records.length>0&&(\n                        <div>\n                          <AuditComplianceChart records={records}/>\n                          <div style={{fontSize:9,color:T.muted,marginBottom:6,letterSpacing:1,marginTop:12}}>AUDIT RECORDS ({records.length})</div>'
),

]

applied = 0
for i, (old, new) in enumerate(patches):
    if old in content:
        content = content.replace(old, new, 1)
        print(f"Patch {i+1}: OK")
        applied += 1
    else:
        print(f"Patch {i+1}: NOT FOUND")
        print(f"  Looking for: {repr(old[:80])}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nResult: {applied}/{len(patches)} patches applied to {filepath}")
if applied < len(patches):
    sys.exit(1)
