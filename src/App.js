import { useState, useEffect, useCallback } from "react";
import { createClient } from "@supabase/supabase-js";
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, Tooltip, ReferenceLine, ResponsiveContainer, CartesianGrid } from "recharts";

const supabase = createClient(
  "https://tbptllgcjtiiqspxqcde.supabase.co",
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRicHRsbGdjanRpaXFzcHhxY2RlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY2NjkzNjAsImV4cCI6MjA5MjI0NTM2MH0.4CPgNp6ytVNRmTU0FJbu2io94QJmsAow5im-vGtoRAU",
  { auth: { flowType: "implicit" } }
);

// ── NABH 6th Edition official chapter order ─────────────────────────────
const CHAPTER_ORDER = {
  "AAC": 1,  // Access, Assessment and Continuity of Care
  "COP": 2,  // Care of Patients
  "MOM": 3,  // Management of Medication
  "PRE": 4,  // Patient Rights and Education
  "IPC": 5,  // Infection Prevention and Control
  "PSQ": 6,  // Patient Safety and Quality Improvement
  "ROM": 7,  // Responsibility of Management
  "FMS": 8,  // Facility Management and Safety
  "HRM": 9,  // Human Resource Management
  "IMS": 10, // Information Management System
};

const T = {
  bg:"#050e1a", panel:"#081525", panel2:"#0c1e35", border:"#0f2640",
  gold:"#c9a84c", goldL:"#f0d070", goldD:"rgba(201,168,76,0.10)",
  red:"#e05a5a", redD:"rgba(224,90,90,0.10)",
  orange:"#f4a441", orangeD:"rgba(244,164,65,0.10)",
  green:"#4caf7d", greenD:"rgba(76,175,125,0.10)",
  blue:"#4fc3f7", blueD:"rgba(79,195,247,0.08)",
  muted:"#3a5870", text:"#c8dcea", white:"#eef4f9",
};

const lvColor = l => l==="CORE"?"#e05a5a":l==="Commitment"?"#4fc3f7":l==="Achievement"?"#4caf7d":"#c9a84c";
const chColor = {AAC:"#4fc3f7",COP:"#f4a441",MOM:"#e05a5a",PRE:"#4caf7d",IPC:"#c084e8",PSQ:"#ff8a65",ROM:"#80cbc4",FMS:"#a5d6a7",HRM:"#f0d070",IMS:"#90caf9"};
const sevColor = s => s==="CRITICAL"?T.red:s==="HIGH"?T.orange:s==="MEDIUM"?T.gold:T.green;
const MONTHS_SHORT = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];

function Ring({ pct=0, size=110, stroke=9, color=T.green, label }) {
  const r=(size-stroke)/2,circ=2*Math.PI*r,dash=(pct/100)*circ;
  return (
    <div style={{position:"relative",width:size,height:size,flexShrink:0}}>
      <svg width={size} height={size} style={{transform:"rotate(-90deg)"}}>
        <circle cx={size/2} cy={size/2} r={r} fill="none" stroke={`${color}20`} strokeWidth={stroke}/>
        <circle cx={size/2} cy={size/2} r={r} fill="none" stroke={color} strokeWidth={stroke}
          strokeDasharray={`${dash} ${circ}`} strokeLinecap="round"
          style={{transition:"stroke-dasharray 0.8s cubic-bezier(0.4,0,0.2,1)"}}/>
      </svg>
      <div style={{position:"absolute",inset:0,display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center"}}>
        <div style={{fontSize:size>90?20:14,fontWeight:800,color,fontFamily:"Georgia,serif",lineHeight:1}}>{pct}%</div>
        {label&&<div style={{fontSize:8,color:T.muted,letterSpacing:1,marginTop:2}}>{label}</div>}
      </div>
    </div>
  );
}

function KpiTrendChart({ history, target, unit }) {
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

function LoginScreen({ onLogin, initialError }) {
  const [email,setEmail]=useState(""); const [pass,setPass]=useState("");
  const [mode,setMode]=useState("login"); const [error,setError]=useState(initialError||"");
  const [loading,setLoading]=useState(false); const [msg,setMsg]=useState("");
  useEffect(()=>{
    if(initialError)setError(initialError);
  },[initialError]);
  const handle=async()=>{
    setError("");setMsg("");setLoading(true);
    try{
      if(mode==="login"){const{data,error:err}=await supabase.auth.signInWithPassword({email,password:pass});if(err)throw err;onLogin(data.user);}
      else if(mode==="signup"){const{data,error:err}=await supabase.auth.signUp({email,password:pass});if(err)throw err;if(data.session)onLogin(data.user);else{setMsg("Account created. You can now sign in.");setMode("login");}}
      else if(mode==="reset"){if(!email.trim())throw new Error("Enter your email address first.");const{error:err}=await supabase.auth.resetPasswordForEmail(email,{redirectTo:"https://upadhyaymehul9-prog.github.io/nabh-compliance/"});if(err)throw err;setMsg("Password reset email sent! Check your inbox.");setMode("login");}
    }catch(e){setError(e.message);}
    setLoading(false);
  };
  const signInWithGoogle=async()=>{
    setError("");setLoading(true);
    const{error:err}=await supabase.auth.signInWithOAuth({
      provider:"google",
      options:{redirectTo:"https://upadhyaymehul9-prog.github.io/nabh-compliance/"}
    });
    if(err){setError(err.message);setLoading(false);}
  };
  return (
    <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",fontFamily:"Segoe UI,system-ui,sans-serif"}}>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:16,padding:"40px 36px",width:360}}>
        <div style={{textAlign:"center",marginBottom:28}}>
          <div style={{width:48,height:48,borderRadius:12,background:`linear-gradient(135deg,${T.gold},#f0d070)`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:24,margin:"0 auto 12px"}}>⚕</div>
          <div style={{fontSize:8,letterSpacing:3,color:T.gold,marginBottom:4}}>NABH 6TH EDITION</div>
          <div style={{fontSize:18,fontWeight:700,color:T.white}}>Compliance Engine</div>
          <div style={{fontSize:11,color:T.muted,marginTop:4}}>Hospital Accreditation Platform</div>
        </div>
        {error&&<div style={{background:T.redD,border:`1px solid ${T.red}40`,borderRadius:8,padding:"10px 14px",marginBottom:16,fontSize:11,color:T.red}}>{error}</div>}
        {msg&&<div style={{background:T.greenD,border:`1px solid ${T.green}40`,borderRadius:8,padding:"10px 14px",marginBottom:16,fontSize:11,color:T.green}}>{msg}</div>}
        <div style={{marginBottom:14}}>
          <div style={{fontSize:10,color:T.muted,marginBottom:6}}>EMAIL</div>
          <input value={email} onChange={e=>setEmail(e.target.value)} placeholder="admin@hospital.com" type="email"
            style={{width:"100%",padding:"10px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,boxSizing:"border-box"}}/>
        </div>
        {mode!=="reset"&&<div style={{marginBottom:20}}>
          <div style={{fontSize:10,color:T.muted,marginBottom:6}}>PASSWORD</div>
          <input value={pass} onChange={e=>setPass(e.target.value)} placeholder="••••••••" type="password" onKeyDown={e=>e.key==="Enter"&&handle()}
            style={{width:"100%",padding:"10px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,boxSizing:"border-box"}}/>
        </div>}
        {mode==="reset"&&<div style={{marginBottom:20,fontSize:11,color:T.muted,lineHeight:1.6}}>Enter your email above and we'll send you a password reset link.</div>}
        <button onClick={handle} disabled={loading} style={{width:"100%",padding:"12px",borderRadius:10,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:13,fontWeight:700,cursor:"pointer",opacity:loading?0.7:1}}>
          {loading?"Please wait…":mode==="login"?"Sign In →":mode==="signup"?"Create Account →":"Send Reset Email →"}
        </button>
        {mode==="login"&&(
          <>
            <div style={{display:"flex",alignItems:"center",gap:10,margin:"16px 0"}}>
              <div style={{flex:1,height:1,background:T.border}}/>
              <div style={{fontSize:10,color:T.muted,letterSpacing:1}}>OR</div>
              <div style={{flex:1,height:1,background:T.border}}/>
            </div>
            <button onClick={signInWithGoogle} disabled={loading}
              style={{width:"100%",padding:"11px",borderRadius:10,background:T.panel2,border:`1px solid ${T.border}`,color:T.text,fontSize:13,fontWeight:600,cursor:"pointer",display:"flex",alignItems:"center",justifyContent:"center",gap:10,opacity:loading?0.7:1}}>
              <svg width="16" height="16" viewBox="0 0 48 48"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.08 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.18 1.48-4.97 2.31-8.16 2.31-6.26 0-11.57-3.58-13.46-8.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg>
              Continue with Google
            </button>
            <div style={{textAlign:"center",marginTop:12,fontSize:11,color:T.muted}}>
              <span onClick={()=>{setMode("reset");setError("");setMsg("");}} style={{color:T.blue,cursor:"pointer"}}>Forgot password?</span>
            </div>
          </>
        )}
        <div style={{textAlign:"center",marginTop:10,fontSize:11,color:T.muted}}>
          {mode==="login"?"Don't have an account? ":mode==="signup"?"Already have an account? ":"Remember your password? "}
          <span onClick={()=>{setMode(mode==="login"?"signup":"login");setError("");setMsg("");}} style={{color:T.gold,cursor:"pointer",fontWeight:600}}>
            {mode==="login"?"Sign up":mode==="reset"?"Sign in":"Sign in"}
          </span>
        </div>
        <div style={{textAlign:"center",marginTop:10,fontSize:9,color:T.muted}}>Independent educational tool — Not affiliated with NABH/QCI</div>
      </div>
    </div>
  );
}

function SetupScreen({ user, onReady }) {
  const [hospital,setHospital]=useState(null);
  const [assessments,setAssessments]=useState([]);
  const [selAss,setSelAss]=useState("");
  const [newHosp,setNewHosp]=useState("");
  const [newAss,setNewAss]=useState("");
  const [loading,setLoading]=useState(true);
  const [error,setError]=useState("");

  useEffect(()=>{init();},[]);

  const init=async()=>{
    setLoading(true);
    // Load user's hospital (one per account)
    const{data:hosp}=await supabase.from("hospitals").select("*").limit(1).single();
    if(hosp){
      setHospital(hosp);
      const{data:ass}=await supabase.from("assessments").select("*").eq("hospital_id",hosp.id).order("created_at",{ascending:false});
      const assData=ass||[];
      setAssessments(assData);
      // If only one assessment exists, auto-proceed
      if(assData.length===1){
        onReady({hospitalId:hosp.id,assessmentId:assData[0].id,hospitalName:hosp.name,assessmentName:assData[0].name});
        return;
      }
      if(assData.length>0)setSelAss(assData[0].id);
    }
    setLoading(false);
  };

  const createHospital=async()=>{
    if(!newHosp.trim())return;
    setLoading(true);setError("");
    const{data,error:err}=await supabase.from("hospitals").insert({name:newHosp.trim(),nabh_status:"preparing"}).select().single();
    if(err){setError(err.message);setLoading(false);return;}
    await supabase.from("profiles").upsert({id:user.id,hospital_id:data.id,role:"admin",name:user.email});
    setHospital(data);setAssessments([]);setNewHosp("");setLoading(false);
  };

  const createAssessment=async()=>{
    if(!newAss.trim()||!hospital)return;
    setLoading(true);setError("");
    const{data,error:err}=await supabase.from("assessments").insert({hospital_id:hospital.id,name:newAss.trim(),created_by:user.id,status:"in_progress"}).select().single();
    if(err){setError(err.message);setLoading(false);return;}
    setAssessments(p=>[data,...p]);setSelAss(data.id);setNewAss("");setLoading(false);
  };

  const proceed=()=>{
    if(!hospital||!selAss)return;
    const ass=assessments.find(a=>a.id===selAss);
    onReady({hospitalId:hospital.id,assessmentId:selAss,hospitalName:hospital.name,assessmentName:ass?.name});
  };

  if(loading) return (
    <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",color:T.gold,fontFamily:"Segoe UI,sans-serif",fontSize:14}}>
      Setting up your workspace…
    </div>
  );

  return (
    <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",fontFamily:"Segoe UI,system-ui,sans-serif"}}>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:16,padding:"36px",width:420}}>
        <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:4}}>
          <div style={{fontSize:8,letterSpacing:3,color:T.gold}}>NABH COMPLIANCE ENGINE</div>
          <button onClick={()=>supabase.auth.signOut()} style={{fontSize:10,color:T.muted,background:"transparent",border:`1px solid ${T.border}`,borderRadius:6,padding:"3px 10px",cursor:"pointer"}}>Sign out</button>
        </div>

        {error&&<div style={{background:T.redD,border:`1px solid ${T.red}40`,borderRadius:8,padding:"10px 14px",marginBottom:16,fontSize:11,color:T.red,marginTop:12}}>{error}</div>}

        {/* No hospital yet — create one */}
        {!hospital&&(
          <>
            <div style={{fontSize:18,fontWeight:700,color:T.white,margin:"16px 0 8px"}}>Welcome! Set up your hospital</div>
            <div style={{fontSize:11,color:T.muted,marginBottom:20,lineHeight:1.6}}>Each account is linked to one hospital. Enter your hospital name to get started.</div>
            <div style={{fontSize:10,color:T.muted,marginBottom:8,letterSpacing:1}}>HOSPITAL NAME</div>
            <div style={{display:"flex",gap:8}}>
              <input value={newHosp} onChange={e=>setNewHosp(e.target.value)} placeholder="e.g. HMP Foundation Hospital" onKeyDown={e=>e.key==="Enter"&&createHospital()}
                style={{flex:1,padding:"10px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,boxSizing:"border-box"}}/>
              <button onClick={createHospital} disabled={!newHosp.trim()} style={{padding:"10px 16px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:12,fontWeight:700,cursor:newHosp.trim()?"pointer":"default",opacity:newHosp.trim()?1:0.5}}>Create</button>
            </div>
          </>
        )}

        {/* Hospital exists — select or create assessment */}
        {hospital&&(
          <>
            <div style={{fontSize:18,fontWeight:700,color:T.white,margin:"16px 0 4px"}}>{hospital.name}</div>
            <div style={{fontSize:10,color:T.green,marginBottom:20}}>✓ Hospital registered</div>

            <div style={{fontSize:10,color:T.muted,marginBottom:8,letterSpacing:1}}>ASSESSMENT</div>
            {assessments.length>0&&(
              <select value={selAss} onChange={e=>setSelAss(e.target.value)}
                style={{width:"100%",padding:"10px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,marginBottom:10,boxSizing:"border-box"}}>
                {assessments.map(a=><option key={a.id} value={a.id}>{a.name}</option>)}
              </select>
            )}
            <div style={{display:"flex",gap:8,marginBottom:16}}>
              <input value={newAss} onChange={e=>setNewAss(e.target.value)} placeholder="Or create new assessment…" onKeyDown={e=>e.key==="Enter"&&createAssessment()}
                style={{flex:1,padding:"9px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12,boxSizing:"border-box"}}/>
              <button onClick={createAssessment} disabled={!newAss.trim()} style={{padding:"9px 16px",borderRadius:8,background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,fontSize:12,cursor:"pointer"}}>Add</button>
            </div>
            <button onClick={proceed} disabled={!selAss} style={{width:"100%",padding:"12px",borderRadius:10,background:selAss?`linear-gradient(135deg,${T.gold},#f0d070)`:T.border,border:"none",color:selAss?T.bg:T.muted,fontSize:13,fontWeight:700,cursor:selAss?"pointer":"default"}}>
              Open Assessment →
            </button>
          </>
        )}
      </div>
    </div>
  );
}

function VerdictBanner({ decision }) {
  const rd=decision.readiness||"NOT READY";
  const rdColor=rd==="NOT READY"?T.red:rd==="RISKY"?T.orange:T.green;
  const rdBg=rd==="NOT READY"?T.redD:rd==="RISKY"?T.orangeD:T.greenD;
  const vColor=decision.verdict==="FAIL"?T.red:decision.verdict==="PASS"?T.green:decision.verdict==="PARTIAL"?T.orange:T.blue;
  const failReasons=decision.fail_reasons||[];
  return (
    <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:14,overflow:"hidden",marginBottom:14}}>
      <div style={{height:4,background:`linear-gradient(90deg,${vColor},${rdColor})`}}/>
      <div style={{padding:"18px 22px"}}>
        <div style={{display:"flex",gap:20,alignItems:"center",flexWrap:"wrap"}}>
          <div style={{textAlign:"center",minWidth:100}}>
            <div style={{fontSize:9,letterSpacing:3,color:T.muted,marginBottom:4}}>VERDICT</div>
            <div style={{fontSize:34,fontWeight:900,color:vColor,fontFamily:"Georgia,serif",letterSpacing:2,lineHeight:1}}>{decision.verdict||"—"}</div>
          </div>
          <div style={{width:1,height:60,background:T.border}}/>
          <div style={{background:rdBg,border:`1px solid ${rdColor}30`,borderRadius:10,padding:"10px 18px",textAlign:"center"}}>
            <div style={{fontSize:8,letterSpacing:2,color:T.muted,marginBottom:4}}>READINESS</div>
            <div style={{fontSize:15,fontWeight:800,color:rdColor,letterSpacing:1}}>{rd}</div>
          </div>
          <div style={{width:1,height:60,background:T.border}}/>
          <Ring pct={decision.overall_pct||0} color={(decision.overall_pct||0)>=80?T.green:T.red} label="OVERALL"/>
          <Ring pct={decision.total_core>0?Math.round(((decision.total_core-(decision.core_failures||0))/decision.total_core)*100):0} color={decision.core_pass?T.green:T.red} label="CORE" size={90} stroke={7}/>
          <Ring pct={Math.round(((decision.scored_count||0)/639)*100)} color={T.blue} label="SCORED" size={90} stroke={7}/>
          <div style={{flex:1,minWidth:160}}>
            <div style={{fontSize:11,color:T.text,lineHeight:1.7}}>{decision.scored_count>0?`Scored ${decision.scored_count} of ${decision.total_oes||639} OEs. Overall ${decision.overall_pct||0}% compliance.`:decision.summary||"No data yet. Start scoring OEs."}</div>
            <div style={{display:"flex",gap:6,marginTop:8,flexWrap:"wrap"}}>
              {[["Rule 1: CORE",decision.rule1_core],["Rule 2: Overall ≥80%",decision.rule2_overall],["Rule 3: Chapters",decision.rule3_chapters],["Rule 4: Standards",decision.rule4_standards]].map(([label,pass])=>(
                <span key={label} style={{fontSize:9,padding:"2px 8px",borderRadius:8,background:pass?T.greenD:T.redD,color:pass?T.green:T.red,border:`1px solid ${pass?T.green:T.red}30`}}>{pass?"✓":"✗"} {label}</span>
              ))}
            </div>
          </div>
        </div>
        {failReasons.length>0&&(
          <div style={{marginTop:14,display:"grid",gap:6}}>
            {failReasons.map((r,i)=>(
              <div key={i} style={{display:"flex",gap:10,alignItems:"flex-start",background:r.severity==="CRITICAL"?T.redD:r.severity==="HIGH"?T.orangeD:T.goldD,border:`1px solid ${sevColor(r.severity)}25`,borderRadius:8,padding:"9px 14px"}}>
                <span style={{fontSize:16,flexShrink:0}}>{r.severity==="CRITICAL"?"🚨":r.severity==="HIGH"?"⚠️":"📌"}</span>
                <div>
                  <span style={{fontSize:9,padding:"1px 7px",borderRadius:5,background:`${sevColor(r.severity)}20`,color:sevColor(r.severity),marginRight:8,fontWeight:700}}>{r.severity}</span>
                  <span style={{fontSize:11,color:T.text,lineHeight:1.6}}>{r.message}</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

function ChapterHeatmap({ breakdown }) {
  if(!breakdown||Object.keys(breakdown).length===0) return (
    <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"16px 18px"}}>
      <div style={{fontSize:9,letterSpacing:2,color:T.muted,marginBottom:12}}>CHAPTER HEATMAP</div>
      <div style={{fontSize:11,color:T.muted,textAlign:"center",padding:"20px 0"}}>No scores yet. Start scoring OEs to see chapter breakdown.</div>
    </div>
  );
  return (
    <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"16px 18px"}}>
      <div style={{fontSize:9,letterSpacing:2,color:T.muted,marginBottom:12}}>CHAPTER HEATMAP</div>
      <div style={{display:"grid",gridTemplateColumns:"repeat(5,1fr)",gap:8}}>
        {Object.entries(breakdown).sort(([a],[b])=>(CHAPTER_ORDER[a]||99)-(CHAPTER_ORDER[b]||99)).map(([ch,data])=>{
          const pct=typeof data==="number"?data:(data?.pct||0);
          const pass=pct>=80;
          const col=chColor[ch]||T.gold;
          const bg=pct>=80?`${T.green}18`:pct>=70?`${T.orange}15`:`${T.red}15`;
          const brd=pct>=80?T.green:pct>=70?T.orange:T.red;
          return (
            <div key={ch} style={{background:bg,border:`1px solid ${brd}25`,borderRadius:8,padding:"10px 8px",textAlign:"center"}}>
              <div style={{fontSize:13,fontWeight:800,color:col,marginBottom:3}}>{ch}</div>
              <div style={{height:3,background:`${brd}20`,borderRadius:2,marginBottom:5}}><div style={{width:`${pct}%`,height:"100%",background:brd,borderRadius:2}}/></div>
              <div style={{fontSize:13,fontWeight:700,color:brd}}>{pct}%</div>
              <div style={{fontSize:8,color:T.muted,marginTop:1}}>{pass?"✓ Pass":"✗ Fail"}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

function Dashboard({ decision, gaps, onNav }) {
  const top5=[...(gaps||[])].sort((a,b)=>b.priority_score-a.priority_score).slice(0,5);

  // Build pillar status from decision object
  const oePct = decision.overall_pct||0;
  const oeStatus = decision.rule1_core&&decision.rule2_overall&&decision.rule3_chapters&&decision.rule4_standards ? "READY" : oePct>0 ? "IN_PROGRESS" : "NOT_STARTED";
  const kpiPct = decision.kpi_pct||0;
  const kpiStatus = decision.kpi_ready ? "READY" : kpiPct>0 ? "IN_PROGRESS" : "NOT_STARTED";
  const commPct = Math.round(((decision.comm_active||0)/26)*100);
  const commStatus = decision.comm_ready ? "READY" : (decision.comm_active||0)>0 ? "IN_PROGRESS" : "NOT_STARTED";
  const auditTotal = decision.audit_total||35;
  const auditPct = Math.round(((decision.audit_done||0)/auditTotal)*100);
  const auditStatus = decision.audit_ready ? "READY" : (decision.audit_done||0)>0 ? "IN_PROGRESS" : "NOT_STARTED";

  const pillars=[
    {key:"oe",   label:"OE Scoring",     icon:"📋", pct:oePct,    status:oeStatus,    nav:"scoring",    detail:`${decision.scored_count||0}/639 OEs`},
    {key:"kpi",  label:"KPI Tracking",   icon:"📈", pct:kpiPct,   status:kpiStatus,   nav:"kpis",       detail:`${decision.kpi_tracked||0}/${decision.kpi_total||50} KPIs ≥3mo`},
    {key:"comm", label:"Committees",     icon:"🏛️", pct:commPct,  status:commStatus,  nav:"committees", detail:`${decision.comm_active||0}/26 active`},
    {key:"audit",label:"Clinical Audits",icon:"🔍", pct:auditPct, status:auditStatus, nav:"audits",     detail:`${decision.audit_done||0}/${auditTotal} completed`},
  ];
  const statusColor=s=>s==="READY"?T.green:s==="IN_PROGRESS"?T.orange:T.red;
  const statusLabel=s=>s==="READY"?"✅ Ready":s==="IN_PROGRESS"?"⚠️ In Progress":"❌ Not Started";
  const allReady=pillars.every(p=>p.status==="READY");

  return (
    <div>
      <VerdictBanner decision={decision}/>
      {/* 4-Pillar Readiness */}
      <div style={{background:T.panel,border:`1px solid ${allReady?T.green:T.border}`,borderRadius:12,padding:"14px 16px",marginTop:14,marginBottom:14}}>
        <div style={{fontSize:9,letterSpacing:2,color:T.muted,marginBottom:10}}>ASSESSMENT READINESS — 4 PILLARS</div>
        <div style={{display:"grid",gridTemplateColumns:"repeat(4,1fr)",gap:10}}>
          {pillars.map(p=>(
            <div key={p.key} onClick={()=>onNav(p.nav)} style={{background:T.panel2,border:`1px solid ${statusColor(p.status)}30`,borderRadius:10,padding:"12px 10px",cursor:"pointer",textAlign:"center"}}>
              <div style={{fontSize:20,marginBottom:4}}>{p.icon}</div>
              <div style={{fontSize:10,fontWeight:700,color:T.white,marginBottom:4}}>{p.label}</div>
              <div style={{fontSize:18,fontWeight:800,color:statusColor(p.status),marginBottom:2}}>{Math.round(p.pct)}%</div>
              <div style={{fontSize:8,color:T.muted,marginBottom:4}}>{p.detail}</div>
              <div style={{fontSize:8,color:statusColor(p.status)}}>{statusLabel(p.status)}</div>
              <div style={{height:3,background:T.border,borderRadius:2,marginTop:8}}>
                <div style={{height:"100%",borderRadius:2,background:statusColor(p.status),width:`${Math.min(100,p.pct)}%`}}/>
              </div>
            </div>
          ))}
        </div>
        {!allReady&&<div style={{marginTop:10,padding:"8px 12px",background:T.redD,borderRadius:8,fontSize:10,color:T.red}}>⚠️ NABH assessors verify all 4 pillars — OE scores, KPI data (≥3 months), committee meeting minutes, and clinical audit records. App shows PASS only when all 4 pillars are ready.</div>}
      </div>
      <ChapterHeatmap breakdown={decision.chapter_breakdown}/>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"16px 18px",marginTop:14}}>
        <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:12}}>
          <div style={{fontSize:9,letterSpacing:2,color:T.muted}}>TOP 5 GAPS BY PRIORITY</div>
          <button onClick={()=>onNav("gaps")} style={{fontSize:10,color:T.gold,background:"transparent",border:`1px solid ${T.gold}30`,borderRadius:10,padding:"3px 10px",cursor:"pointer"}}>View all →</button>
        </div>
        {top5.length===0&&<div style={{fontSize:11,color:T.muted,textAlign:"center",padding:"16px 0"}}>No gaps yet. Score some OEs first.</div>}
        {top5.map((g,i)=>(
          <div key={g.oe_id} style={{display:"flex",gap:10,alignItems:"center",padding:"8px 0",borderBottom:i<4?`1px solid ${T.border}`:"none"}}>
            <div style={{width:22,height:22,borderRadius:6,background:g.level==="CORE"?T.redD:T.orangeD,border:`1px solid ${g.level==="CORE"?T.red:T.orange}40`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:9,fontWeight:800,color:g.level==="CORE"?T.red:T.orange,flexShrink:0}}>{i+1}</div>
            <div style={{flex:1}}>
              <div style={{display:"flex",gap:6,alignItems:"center",marginBottom:2}}>
                <span style={{fontSize:10,fontWeight:700,color:lvColor(g.level),fontFamily:"monospace"}}>{g.oe_id}</span>
                {g.level==="CORE"&&<span style={{fontSize:8,padding:"1px 5px",borderRadius:4,background:T.redD,color:T.red}}>CORE</span>}
              </div>
              <div style={{fontSize:10,color:T.muted,lineHeight:1.3}}>{(g.oe_text||"").slice(0,70)}…</div>
            </div>
            <div style={{textAlign:"center",flexShrink:0}}>
              <div style={{fontSize:16,fontWeight:800,color:g.score<=2?T.red:g.score===3?T.orange:T.green}}>{g.score}</div>
              <div style={{fontSize:7,color:T.muted}}>/ 5</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function ScoringScreen({ assessmentId, oes, standards, onRefresh }) {
  const [filter,setFilter]=useState("ALL"); const [chFilter,setChFilter]=useState("ALL");
  const [search,setSearch]=useState("");
  const [toast,setToast]=useState(null); const [saving,setSaving]=useState({});
  const [localScores,setLocalScores]=useState({}); const [showTip,setShowTip]=useState({});
  const [localLinks,setLocalLinks]=useState({}); const [linkInputOpen,setLinkInputOpen]=useState({});
  const [linkUrl,setLinkUrl]=useState({}); const [linkLabel,setLinkLabel]=useState({}); const [linkBusy,setLinkBusy]=useState({});
  useEffect(()=>{const s={};const l={};oes.forEach(oe=>{s[oe.id]=oe.score||null;l[oe.id]=oe.evidenceLinks||[];});setLocalScores(s);setLocalLinks(l);},[oes]);
  const chapters=["ALL","AAC","COP","MOM","PRE","IPC","PSQ","ROM","FMS","HRM","IMS"];
  const levels=["ALL","CORE","Commitment","Achievement","Excellence"];
  const filtered=oes.filter(oe=>{const lm=filter==="ALL"||oe.level===filter;const cm=chFilter==="ALL"||oe.chapter===chFilter;const sm=!search||oe.id.toLowerCase().includes(search.toLowerCase())||(oe.text||"").toLowerCase().includes(search.toLowerCase());return lm&&cm&&sm;});
  const scored=Object.values(localScores).filter(s=>s!==null).length;
  const handleScore=async(oeId,oeLevel,oeDoc,newScore)=>{
    const isUnset=localScores[oeId]===newScore;
    if(isUnset){
      setLocalScores(p=>({...p,[oeId]:null}));setSaving(p=>({...p,[oeId]:true}));
      const{error}=await supabase.from("scores").delete().match({assessment_id:assessmentId,oe_id:oeId});
      setSaving(p=>({...p,[oeId]:false}));
      if(error){setToast({type:"ERROR",sev:"CRITICAL",msg:error.message});return;}
      setToast({type:"SCORE CLEARED",sev:"SUCCESS",msg:"Score removed. Click again to re-score."});
      setTimeout(()=>setToast(null),3000);
      onRefresh();
      return;
    }
    setLocalScores(p=>({...p,[oeId]:newScore}));setSaving(p=>({...p,[oeId]:true}));
    const{error}=await supabase.from("scores").upsert({assessment_id:assessmentId,oe_id:oeId,score:newScore,updated_at:new Date().toISOString()},{onConflict:"assessment_id,oe_id"});
    setSaving(p=>({...p,[oeId]:false}));
    if(error){setToast({type:"ERROR",sev:"CRITICAL",msg:error.message});return;}
    const{data}=await supabase.rpc("get_score_impact",{param_assessment:assessmentId,param_oe:oeId,param_score:newScore});
    if(data?.alerts?.length>0){
      const a=data.alerts[0];
      const isDocAlert=(a.type||"").toUpperCase().includes("DOC")||(a.message||"").toLowerCase().includes("documentation");
      const hasLinks=(localLinks[oeId]||[]).length>0;
      if(!(isDocAlert&&hasLinks)){
        setToast({type:a.type,sev:a.severity,msg:a.message});setTimeout(()=>setToast(null),4000);
      }
    }
    onRefresh();
  };
  const scoreBtn=(oeId,oeLevel,oeDoc,score,label,color)=>(
    <button key={score} onClick={()=>handleScore(oeId,oeLevel,oeDoc,score)} style={{padding:"5px 10px",borderRadius:7,fontSize:11,fontWeight:700,cursor:"pointer",background:localScores[oeId]===score?`${color}30`:"transparent",border:`1px solid ${localScores[oeId]===score?color:`${color}30`}`,color:localScores[oeId]===score?color:T.muted,transition:"all 0.15s"}}>{label}</button>
  );

  const validUrl=(s)=>{try{const u=new URL(s);return u.protocol==="http:"||u.protocol==="https:";}catch{return false;}};
  const domainOf=(s)=>{try{return new URL(s).hostname.replace(/^www\./,"");}catch{return s;}};

  const saveLink=async(oeId)=>{
    const url=(linkUrl[oeId]||"").trim();
    const label=(linkLabel[oeId]||"").trim();
    if(!url){setToast({type:"ERROR",sev:"CRITICAL",msg:"Paste a URL first."});setTimeout(()=>setToast(null),3000);return;}
    if(!validUrl(url)){setToast({type:"ERROR",sev:"CRITICAL",msg:"Invalid URL. Must start with http:// or https://"});setTimeout(()=>setToast(null),3000);return;}
    const existing=localLinks[oeId]||[];
    if(existing.length>=10){setToast({type:"LIMIT",sev:"HIGH",msg:"Max 10 links per OE."});setTimeout(()=>setToast(null),3000);return;}
    const newEntry={url,label:label||domainOf(url),added_at:new Date().toISOString()};
    const updated=[...existing,newEntry];
    setLinkBusy(p=>({...p,[oeId]:true}));
    const{error}=await supabase.from("scores").upsert({assessment_id:assessmentId,oe_id:oeId,score:localScores[oeId]||null,evidence_links:updated,updated_at:new Date().toISOString()},{onConflict:"assessment_id,oe_id"});
    setLinkBusy(p=>({...p,[oeId]:false}));
    if(error){setToast({type:"ERROR",sev:"CRITICAL",msg:error.message});setTimeout(()=>setToast(null),4000);return;}
    setLocalLinks(p=>({...p,[oeId]:updated}));
    setLinkUrl(p=>({...p,[oeId]:""}));setLinkLabel(p=>({...p,[oeId]:""}));
    setToast({type:"EVIDENCE ADDED",sev:"SUCCESS",msg:"Evidence link saved."});setTimeout(()=>setToast(null),2500);
    onRefresh();
  };

  const removeLink=async(oeId,index)=>{
    const existing=localLinks[oeId]||[];
    const updated=existing.filter((_,i)=>i!==index);
    setLinkBusy(p=>({...p,[oeId]:true}));
    const{error}=await supabase.from("scores").upsert({assessment_id:assessmentId,oe_id:oeId,score:localScores[oeId]||null,evidence_links:updated,updated_at:new Date().toISOString()},{onConflict:"assessment_id,oe_id"});
    setLinkBusy(p=>({...p,[oeId]:false}));
    if(error){setToast({type:"ERROR",sev:"CRITICAL",msg:error.message});setTimeout(()=>setToast(null),4000);return;}
    setLocalLinks(p=>({...p,[oeId]:updated}));
    onRefresh();
  };
  return (
    <div>
      {toast&&<div style={{position:"fixed",top:80,right:16,zIndex:999,maxWidth:360,background:toast.sev==="CRITICAL"?T.redD:toast.sev==="SUCCESS"?T.greenD:toast.sev==="HIGH"?T.orangeD:T.goldD,border:`1px solid ${toast.sev==="CRITICAL"?T.red:toast.sev==="SUCCESS"?T.green:toast.sev==="HIGH"?T.orange:T.gold}50`,borderRadius:10,padding:"12px 16px",boxShadow:"0 8px 32px rgba(0,0,0,0.5)"}}>
        <div style={{fontSize:10,fontWeight:700,marginBottom:4,color:toast.sev==="CRITICAL"?T.red:toast.sev==="SUCCESS"?T.green:toast.sev==="HIGH"?T.orange:T.gold}}>{toast.sev==="CRITICAL"?"🚨":toast.sev==="SUCCESS"?"✅":toast.sev==="HIGH"?"⚠️":"📄"} {toast.type?.replace(/_/g," ")}</div>
        <div style={{fontSize:11,color:T.text,lineHeight:1.5}}>{toast.msg}</div>
      </div>}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:12}}>
        <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:8}}>
          <div style={{fontSize:11,color:T.text}}>Scored: <strong style={{color:T.gold}}>{scored}</strong> / {oes.length} OEs</div>
          <div style={{fontSize:10,color:T.muted}}>{Math.round(scored/Math.max(oes.length,1)*100)}% complete</div>
        </div>
        <div style={{height:4,background:T.border,borderRadius:2}}>
          <div style={{width:`${Math.round(scored/Math.max(oes.length,1)*100)}%`,height:"100%",background:`linear-gradient(90deg,${T.gold},${T.green})`,borderRadius:2,transition:"width 0.5s"}}/>
        </div>
      </div>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 14px",marginBottom:14}}>
        <input value={search} onChange={e=>setSearch(e.target.value)} placeholder="Search OEs by ID or text (e.g. 'hand hygiene', 'COP.1.a', 'fall risk')..." style={{width:"100%",padding:"9px 12px",borderRadius:8,border:`1px solid ${search?T.gold:T.border}`,background:T.panel2,color:T.text,fontSize:12,marginBottom:10,boxSizing:"border-box"}}/>
        <div style={{display:"flex",gap:8,flexWrap:"wrap",alignItems:"center"}}>
          <div style={{display:"flex",gap:4,flexWrap:"wrap"}}>{levels.map(l=><button key={l} onClick={()=>setFilter(l)} style={{padding:"5px 12px",borderRadius:8,fontSize:10,cursor:"pointer",background:filter===l?T.goldD:"transparent",border:`1px solid ${filter===l?T.gold:T.border}`,color:filter===l?T.goldL:T.muted}}>{l}</button>)}</div>
          <select value={chFilter} onChange={e=>setChFilter(e.target.value)} style={{padding:"5px 10px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:10}}>{chapters.map(c=><option key={c} value={c}>{c}</option>)}</select>
          {(search||filter!=="ALL"||chFilter!=="ALL")&&(<button onClick={()=>{setSearch("");setFilter("ALL");setChFilter("ALL");}} style={{padding:"4px 10px",borderRadius:6,fontSize:9,cursor:"pointer",background:T.redD,border:`1px solid ${T.red}30`,color:T.red}}>X Clear</button>)}
          <span style={{fontSize:9,color:T.muted,marginLeft:"auto"}}>{filtered.length} OEs shown</span>
        </div>
      </div>
      <div style={{display:"grid",gap:8}}>
        {(() => {
          // Build standard lookup: id → title
          const stdMap = {};
          (standards||[]).forEach(s => { stdMap[s.id] = s.title; });
          // Group filtered OEs by standard_id, preserving order
          const groups = [];
          const seen = {};
          filtered.forEach(oe => {
            const sid = oe.standard || "_unknown";
            if (!seen[sid]) { seen[sid] = []; groups.push({ id: sid, items: seen[sid] }); }
            seen[sid].push(oe);
          });
          return groups.map(g => (
            <div key={g.id}>
              {g.id !== "_unknown" && (
                <div style={{
                  background: T.panel2,
                  border: `1px solid ${T.gold}40`,
                  borderLeft: `3px solid ${T.gold}`,
                  borderRadius: 8,
                  padding: "10px 14px",
                  marginTop: 14,
                  marginBottom: 6
                }}>
                  <div style={{ fontSize: 9, letterSpacing: 2, color: T.gold, marginBottom: 4 }}>
                    STANDARD {g.id.replace(/\.$/,"")}
                  </div>
                  <div style={{ fontSize: 11, color: T.white, lineHeight: 1.5, fontWeight: 600 }}>
                    {stdMap[g.id] || "Standard title not available"}
                  </div>
                </div>
              )}
              <div style={{display:"grid",gap:8}}>
              {g.items.map(oe=>{
                const currentScore=localScores[oe.id]; const isSaving=saving[oe.id];
                const scoreColor=!currentScore?T.muted:currentScore<=2?T.red:currentScore===3?T.orange:T.green;
                return (
                  <div key={oe.id} style={{background:T.panel,border:`1px solid ${oe.level==="CORE"?`${T.red}30`:T.border}`,borderRadius:10,padding:"14px 16px",opacity:isSaving?0.7:1}}>
                    <div style={{display:"flex",gap:10,alignItems:"flex-start",marginBottom:10}}>
                      <div style={{flexShrink:0}}>
                        <span style={{fontFamily:"monospace",fontSize:11,fontWeight:700,color:lvColor(oe.level)}}>{oe.id}</span>{" "}
                        <span style={{fontSize:9,padding:"2px 7px",borderRadius:5,background:oe.level==="CORE"?T.redD:T.blueD,color:oe.level==="CORE"?T.red:T.blue}}>{oe.level}</span>
                        {oe.doc&&<span style={{fontSize:9,padding:"2px 6px",borderRadius:5,background:T.goldD,color:T.gold,marginLeft:4}}>DOC*</span>}
                      </div>
                      <div style={{fontSize:10,color:T.text,lineHeight:1.5,flex:1}}>{oe.text}</div>
                      <div style={{fontSize:22,fontWeight:800,color:scoreColor,flexShrink:0,minWidth:30,textAlign:"center"}}>{isSaving?"…":currentScore||"—"}</div>
                    </div>
                    <div style={{display:"flex",gap:6,flexWrap:"wrap",alignItems:"center"}}>
                      {scoreBtn(oe.id,oe.level,oe.doc,1,"1 – None",T.red)}
                      {scoreBtn(oe.id,oe.level,oe.doc,2,"2 – Partial",T.orange)}
                      {scoreBtn(oe.id,oe.level,oe.doc,3,"3 – Mostly",T.gold)}
                      {scoreBtn(oe.id,oe.level,oe.doc,4,"4 – Full",T.green)}
                      {scoreBtn(oe.id,oe.level,oe.doc,5,"5 – Excellent",T.blue)}
                      <button onClick={()=>setShowTip(p=>({...p,[oe.id]:!p[oe.id]}))}
                        style={{marginLeft:"auto",padding:"4px 10px",borderRadius:7,fontSize:10,cursor:"pointer",
                          background:showTip[oe.id]?T.blueD:"transparent",
                          border:`1px solid ${showTip[oe.id]?T.blue:T.muted}`,
                          color:showTip[oe.id]?T.blue:T.muted}}>
                        {showTip[oe.id]?"▲ Hide":"? How to achieve"}
                      </button>
                    </div>
                    {oe.doc&&(()=>{
                      const links=localLinks[oe.id]||[];
                      const isOpen=linkInputOpen[oe.id];
                      const busy=linkBusy[oe.id];
                      return (
                        <div style={{marginTop:10,background:links.length>0?T.greenD:T.orangeD,border:`1px solid ${links.length>0?T.green:T.orange}30`,borderRadius:8,padding:"10px 12px"}}>
                          <div style={{display:"flex",gap:8,alignItems:"center",flexWrap:"wrap",marginBottom:links.length>0||isOpen?8:0}}>
                            <span style={{fontSize:10,fontWeight:700,color:links.length>0?T.green:T.orange,letterSpacing:1}}>
                              {links.length>0?`📎 EVIDENCE (${links.length})`:"⚠️ DOCUMENTATION REQUIRED"}
                            </span>
                            {links.length===0&&<span style={{fontSize:10,color:T.muted}}>This OE requires evidence — paste a Drive/OneDrive/Dropbox link.</span>}
                            <button onClick={()=>setLinkInputOpen(p=>({...p,[oe.id]:!p[oe.id]}))} style={{marginLeft:"auto",padding:"3px 10px",borderRadius:6,fontSize:10,cursor:"pointer",background:isOpen?T.panel2:`${T.gold}20`,border:`1px solid ${T.gold}40`,color:T.gold,fontWeight:700}}>
                              {isOpen?"✕ Cancel":"+ Add link"}
                            </button>
                          </div>
                          {links.length>0&&(
                            <div style={{display:"flex",gap:5,flexWrap:"wrap",marginBottom:isOpen?8:0}}>
                              {links.map((l,i)=>(
                                <div key={i} style={{display:"flex",alignItems:"center",gap:5,padding:"4px 4px 4px 10px",borderRadius:6,background:T.panel2,border:`1px solid ${T.green}30`,fontSize:10}}>
                                  <a href={l.url} target="_blank" rel="noopener noreferrer" style={{color:T.text,textDecoration:"none",maxWidth:200,overflow:"hidden",textOverflow:"ellipsis",whiteSpace:"nowrap"}}>📄 {l.label||domainOf(l.url)}</a>
                                  <span style={{fontSize:9,color:T.muted}}>· {domainOf(l.url)}</span>
                                  <button onClick={()=>removeLink(oe.id,i)} disabled={busy} style={{padding:"2px 7px",borderRadius:5,background:"transparent",border:`1px solid ${T.red}40`,color:T.red,fontSize:9,cursor:"pointer"}}>✕</button>
                                </div>
                              ))}
                            </div>
                          )}
                          {isOpen&&(
                            <div style={{display:"grid",gap:6,paddingTop:6,borderTop:`1px dashed ${T.border}`}}>
                              <input value={linkUrl[oe.id]||""} onChange={e=>setLinkUrl(p=>({...p,[oe.id]:e.target.value}))} placeholder="https://drive.google.com/..." style={{padding:"7px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:11}}/>
                              <div style={{display:"flex",gap:6}}>
                                <input value={linkLabel[oe.id]||""} onChange={e=>setLinkLabel(p=>({...p,[oe.id]:e.target.value}))} placeholder="Optional label (e.g., 'IPC Policy v3')" style={{flex:1,padding:"7px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:11}}/>
                                <button onClick={()=>saveLink(oe.id)} disabled={busy} style={{padding:"6px 14px",borderRadius:6,background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,fontSize:11,fontWeight:700,cursor:busy?"not-allowed":"pointer",opacity:busy?0.5:1}}>{busy?"Saving…":"Save link"}</button>
                              </div>
                              <div style={{fontSize:9,color:T.muted}}>Paste any URL — Google Drive, OneDrive, Dropbox, internal HIS, etc. Files stay in your storage; only the link is saved here.</div>
                            </div>
                          )}
                        </div>
                      );
                    })()}
                    {showTip[oe.id]&&(()=>{
                      const tips=oe.achieveTips;
                      const lvlTips = oe.level==="CORE"
                        ? ["CORE element — assessed at EVERY NABH visit, not just final","Score <4 on any CORE = automatic FAIL regardless of overall score","Prioritise this OE above all others in your improvement plan","Assessors will examine records, observe practice, and interview staff"]
                        : oe.level==="Achievement"
                        ? ["Achievement level — assessed at Final Assessment only","Must show measurable outcomes, not just process compliance","Collect before/after data to demonstrate improvement","Quality committee validates achievement data"]
                        : oe.level==="Excellence"
                        ? ["Excellence level — assessed at Re-accreditation only","Demonstrate innovation and leadership beyond basic compliance","Benchmark against national/international best practices","Document formal recognition or external validation"]
                        : ["Commitment level — assessed at Final Assessment","Document the policy/SOP and evidence of implementation","Staff must be able to demonstrate knowledge when interviewed","Audit trail: records should show consistent compliance"];
                      const displayTips = tips || lvlTips;
                      return (
                        <div style={{marginTop:10,background:T.blueD,border:`1px solid ${T.blue}20`,borderRadius:8,padding:"12px 14px"}}>
                          <div style={{fontSize:9,letterSpacing:2,color:T.blue,marginBottom:8}}>
                            {tips?"HOW TO ACHIEVE THIS OE":"GENERAL GUIDANCE — "+oe.level.toUpperCase()}
                          </div>
                          {displayTips.map((tip,i)=>(
                            <div key={i} style={{display:"flex",gap:8,marginBottom:6,alignItems:"flex-start"}}>
                              <div style={{width:18,height:18,borderRadius:"50%",background:`${T.blue}20`,border:`1px solid ${T.blue}40`,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0,fontSize:9,color:T.blue,fontWeight:700}}>{i+1}</div>
                              <div style={{fontSize:11,color:T.text,lineHeight:1.6,paddingTop:1}}>{tip}</div>
                            </div>
                          ))}
                          {!tips&&<div style={{fontSize:9,color:T.muted,marginTop:6,fontStyle:"italic"}}>Specific achieve tips not available for this OE — general {oe.level} guidance shown.</div>}
                        </div>
                      );
                    })()}
                  </div>
                );
              })}
              </div>
            </div>
          ));
        })()}
        {filtered.length===0&&<div style={{textAlign:"center",color:T.muted,padding:"30px",fontSize:12}}>{search?"No OEs match your search. Try different keywords or clear filters.":"No OEs match this filter."}</div>}
      </div>
    </div>
  );
}

function GapFixScreen({ assessmentId, gaps, onRefresh }) {
  const [sevFilter,setSevFilter]=useState("ALL"); const [capas,setCapas]=useState({}); const [saving,setSaving]=useState({});
  const filtered=(gaps||[]).filter(g=>sevFilter==="ALL"||g.severity===sevFilter);
  const submitCapa=async(oeId)=>{
    const c=capas[oeId];if(!c?.finding||!c?.action)return;setSaving(p=>({...p,[oeId]:true}));
    await supabase.from("capa").upsert({assessment_id:assessmentId,oe_id:oeId,finding:c.finding,root_cause:c.root_cause||"",action_planned:c.action,action_type:c.action_type||"Process",responsible_person:c.person||"",target_date:c.date||null,status:"open"},{onConflict:"assessment_id,oe_id"});
    setSaving(p=>({...p,[oeId]:false}));setCapas(p=>({...p,[oeId]:{...p[oeId],saved:true}}));onRefresh();
  };
  return (
    <div>
      <div style={{display:"flex",gap:8,marginBottom:14}}>
        {["ALL","CRITICAL","HIGH","MEDIUM","LOW"].map(s=><button key={s} onClick={()=>setSevFilter(s)} style={{padding:"5px 14px",borderRadius:8,fontSize:10,cursor:"pointer",background:sevFilter===s?`${sevColor(s)}20`:"transparent",border:`1px solid ${sevFilter===s?sevColor(s):T.border}`,color:sevFilter===s?sevColor(s):T.muted}}>{s}</button>)}
        <div style={{marginLeft:"auto",fontSize:11,color:T.muted,alignSelf:"center"}}>{filtered.length} gaps</div>
      </div>
      {filtered.length===0&&<div style={{textAlign:"center",color:T.muted,padding:"40px",fontSize:12}}>{(gaps||[]).length===0?"No gaps found. Score OEs first.":"No gaps at this severity level."}</div>}
      <div style={{display:"grid",gap:10}}>
        {filtered.map(g=>{
          const c=capas[g.oe_id]||{}; const expanded=c.expanded;
          return (
            <div key={g.oe_id} style={{background:T.panel,border:`1px solid ${sevColor(g.severity)}25`,borderRadius:12,overflow:"hidden"}}>
              <div style={{height:3,background:sevColor(g.severity)}}/>
              <div style={{padding:"14px 16px"}}>
                <div style={{display:"flex",gap:10,alignItems:"flex-start",marginBottom:8}}>
                  <div style={{flex:1}}>
                    <div style={{display:"flex",gap:8,alignItems:"center",marginBottom:4,flexWrap:"wrap"}}>
                      <span style={{fontFamily:"monospace",fontSize:11,fontWeight:700,color:lvColor(g.level)}}>{g.oe_id}</span>
                      <span style={{fontSize:9,padding:"2px 7px",borderRadius:5,background:`${sevColor(g.severity)}15`,color:sevColor(g.severity)}}>{g.severity}</span>
                      {g.level==="CORE"&&<span style={{fontSize:9,padding:"2px 6px",borderRadius:5,background:T.redD,color:T.red}}>CORE</span>}
                      {g.gap_closed&&<span style={{fontSize:9,padding:"2px 6px",borderRadius:5,background:T.greenD,color:T.green}}>✓ CLOSED</span>}
                    </div>
                    <div style={{fontSize:10,color:T.text,lineHeight:1.5,marginBottom:6}}>{g.oe_text}</div>
                    <div style={{fontSize:10,color:T.muted,fontStyle:"italic"}}>{g.message}</div>
                  </div>
                  <div style={{textAlign:"center",flexShrink:0}}>
                    <div style={{fontSize:22,fontWeight:800,color:g.score<=2?T.red:g.score===3?T.orange:T.green}}>{g.score}</div>
                    <div style={{fontSize:7,color:T.muted}}>/ 5</div>
                  </div>
                </div>
                <button onClick={()=>setCapas(p=>({...p,[g.oe_id]:{...c,expanded:!expanded}}))} style={{fontSize:10,color:T.gold,background:"transparent",border:`1px solid ${T.gold}30`,borderRadius:8,padding:"4px 14px",cursor:"pointer"}}>{expanded?"▲ Hide CAPA":"▼ Add CAPA"}</button>
                {expanded&&(
                  <div style={{marginTop:12,display:"grid",gap:8}}>
                    {c.saved&&<div style={{fontSize:10,color:T.green,padding:"6px 10px",background:T.greenD,borderRadius:6}}>✓ CAPA saved</div>}
                    <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>FINDING *</div><textarea value={c.finding||""} onChange={e=>setCapas(p=>({...p,[g.oe_id]:{...c,finding:e.target.value}}))} rows={2} placeholder="Describe the non-compliance finding…" style={{width:"100%",padding:"8px 10px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:11,resize:"vertical",boxSizing:"border-box"}}/></div>
                    <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>ACTION PLANNED *</div><textarea value={c.action||""} onChange={e=>setCapas(p=>({...p,[g.oe_id]:{...c,action:e.target.value}}))} rows={2} placeholder="Corrective action to be taken…" style={{width:"100%",padding:"8px 10px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:11,resize:"vertical",boxSizing:"border-box"}}/></div>
                    <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
                      <div style={{flex:1,minWidth:140}}><div style={{fontSize:9,color:T.muted,marginBottom:4}}>RESPONSIBLE PERSON</div><input value={c.person||""} onChange={e=>setCapas(p=>({...p,[g.oe_id]:{...c,person:e.target.value}}))} placeholder="Name / Designation" style={{width:"100%",padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:11,boxSizing:"border-box"}}/></div>
                      <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>TARGET DATE</div><input type="date" value={c.date||""} onChange={e=>setCapas(p=>({...p,[g.oe_id]:{...c,date:e.target.value}}))} style={{padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:11}}/></div>
                      <button onClick={()=>submitCapa(g.oe_id)} disabled={saving[g.oe_id]||!c.finding||!c.action} style={{marginTop:14,padding:"7px 20px",borderRadius:10,background:`linear-gradient(135deg,${T.green},#3d9e6e)`,border:"none",color:T.bg,fontSize:12,fontWeight:700,cursor:c.finding&&c.action?"pointer":"default",opacity:c.finding&&c.action?1:0.5}}>{saving[g.oe_id]?"Saving…":"Save CAPA →"}</button>
                    </div>
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}


// ── COMMITTEES — with full MOM ─────────────────────────────
function CommitteesScreen({ hospitalId }) {
  const [committees,setCommittees]=useState([]);
  const [meetings,setMeetings]=useState([]);
  const [loading,setLoading]=useState(true);
  const [search,setSearch]=useState("");
  const [filter,setFilter]=useState("ALL");
  const [expanded,setExpanded]=useState(null);
  const [guideOpen,setGuideOpen]=useState(null);
  const [view,setView]=useState("reference"); // reference | mom
  const [showMOMForm,setShowMOMForm]=useState(null); // committee_id
  const [saving,setSaving]=useState(false);
  const [momSuccess,setMomSuccess]=useState(false);

  // MOM form state
  const emptyMOM = () => ({
    meeting_date:"", meeting_no:"", venue:"", chairperson:"",
    members_present:"", members_total:"", quorum_met:true,
    agenda_items:[{item:"",discussion:"",decision:"",action_owner:"",target_date:""}],
    minutes_text:"", previous_capa_reviewed:false,
    next_meeting_date:"", next_meeting_agenda:"",
    minutes_approved_by:"", minutes_approved_date:""
  });
  const [momForm,setMOMForm]=useState(emptyMOM());

  useEffect(()=>{
    supabase.from("committees").select("*").order("id").then(({data})=>setCommittees(data||[]));
    if(hospitalId){
      supabase.from("committee_meetings").select("*").eq("hospital_id",hospitalId)
        .order("meeting_date",{ascending:false})
        .then(({data})=>{setMeetings(data||[]);setLoading(false);});
    } else { setLoading(false); }
  },[hospitalId]);

  const filtered=committees.filter(c=>{
    const ms=!search||c.name.toLowerCase().includes(search.toLowerCase())||c.chapter_ref?.toLowerCase().includes(search.toLowerCase());
    const mf=filter==="ALL"||(filter==="NEW"&&c.is_new_in_6th)||(filter==="JCI"&&c.is_jci);
    return ms&&mf;
  });

  // committee meeting counts
  const meetingCount=(cid)=>meetings.filter(m=>m.committee_id===cid).length;
  const lastMeeting=(cid)=>{
    const m=meetings.filter(m=>m.committee_id===cid).sort((a,b)=>new Date(b.meeting_date)-new Date(a.meeting_date))[0];
    return m?m.meeting_date:null;
  };

  const addAgendaItem=()=>setMOMForm(f=>({...f,agenda_items:[...f.agenda_items,{item:"",discussion:"",decision:"",action_owner:"",target_date:""}]}));
  const updateAgenda=(i,k,v)=>setMOMForm(f=>{const a=[...f.agenda_items];a[i]={...a[i],[k]:v};return{...f,agenda_items:a};});
  const removeAgenda=(i)=>setMOMForm(f=>({...f,agenda_items:f.agenda_items.filter((_,idx)=>idx!==i)}));

  const saveMOM=async(committeeId)=>{
    if(!momForm.meeting_date||!momForm.chairperson){alert("Meeting date and chairperson are required.");return;}
    setSaving(true);
    const {error}=await supabase.from("committee_meetings").insert({
      hospital_id:hospitalId,
      committee_id:committeeId,
      meeting_date:momForm.meeting_date,
      meeting_no:momForm.meeting_no||null,
      venue:momForm.venue||null,
      chairperson:momForm.chairperson,
      quorum_met:momForm.quorum_met,
      members_present:momForm.members_present?parseInt(momForm.members_present):null,
      members_total:momForm.members_total?parseInt(momForm.members_total):null,
      agenda_items:momForm.agenda_items.filter(a=>a.item.trim()),
      minutes_text:momForm.minutes_text||null,
      previous_capa_reviewed:momForm.previous_capa_reviewed,
      next_meeting_date:momForm.next_meeting_date||null,
      next_meeting_agenda:momForm.next_meeting_agenda||null,
      minutes_approved_by:momForm.minutes_approved_by||null,
      minutes_approved_date:momForm.minutes_approved_date||null,
    });
    if(!error){
      const{data}=await supabase.from("committee_meetings").select("*").eq("hospital_id",hospitalId).order("meeting_date",{ascending:false});
      setMeetings(data||[]);
      setShowMOMForm(null);
      setMOMForm(emptyMOM());
      setMomSuccess(true);
      setTimeout(()=>setMomSuccess(false),3000);
    } else { alert("Error saving MOM: "+error.message); }
    setSaving(false);
  };

  const deleteMeeting=async(id)=>{
    if(!window.confirm("Delete this meeting record?"))return;
    await supabase.from("committee_meetings").delete().eq("id",id);
    setMeetings(m=>m.filter(x=>x.id!==id));
  };

  const inp={width:"100%",padding:"7px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:11,boxSizing:"border-box"};
  const lbl={fontSize:9,color:T.muted,marginBottom:3,letterSpacing:1};

  const totalActive=new Set(meetings.filter(m=>{
    const d=new Date(m.meeting_date); const now=new Date();
    return (now-d)/(1000*60*60*24*365)<=1;
  }).map(m=>m.committee_id)).size;

  if(loading) return <div style={{textAlign:"center",color:T.muted,padding:40}}>Loading…</div>;

  return (
    <div>
      {/* 4-pillar summary bar */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:14,display:"flex",gap:16,alignItems:"center",flexWrap:"wrap"}}>
        <div style={{flex:1}}>
          <div style={{fontSize:9,color:T.muted,marginBottom:3,letterSpacing:1}}>COMMITTEE FUNCTIONING</div>
          <div style={{fontSize:12,color:totalActive>=20?T.green:totalActive>0?T.orange:T.red,fontWeight:700}}>
            {totalActive}/26 committees active <span style={{fontSize:9,color:T.muted}}>(met in last 12 months)</span>
          </div>
          <div style={{height:4,background:T.border,borderRadius:2,marginTop:6}}>
            <div style={{height:"100%",borderRadius:2,background:totalActive>=20?T.green:totalActive>0?T.orange:T.red,width:`${Math.min(100,(totalActive/26)*100)}%`,transition:"width 0.5s"}}/>
          </div>
        </div>
        <div style={{display:"flex",gap:8}}>
          <button onClick={()=>setView("reference")} style={{padding:"5px 14px",borderRadius:8,fontSize:10,cursor:"pointer",background:view==="reference"?T.goldD:"transparent",border:`1px solid ${view==="reference"?T.gold:T.border}`,color:view==="reference"?T.goldL:T.muted}}>📋 Reference</button>
          <button onClick={()=>setView("mom")} style={{padding:"5px 14px",borderRadius:8,fontSize:10,cursor:"pointer",background:view==="mom"?T.goldD:"transparent",border:`1px solid ${view==="mom"?T.gold:T.border}`,color:view==="mom"?T.goldL:T.muted}}>📝 Meeting Records {meetings.length>0&&<span style={{marginLeft:4,background:T.gold,color:T.bg,borderRadius:4,padding:"0 5px",fontSize:8}}>{meetings.length}</span>}</button>
        </div>
      </div>

      {momSuccess&&<div style={{background:T.greenD,border:`1px solid ${T.green}30`,borderRadius:8,padding:"10px 14px",marginBottom:12,fontSize:11,color:T.green}}>✅ Meeting minutes saved successfully.</div>}

      {/* REFERENCE VIEW */}
      {view==="reference"&&(
        <div>
          <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:14}}>
            <div style={{display:"flex",gap:10,alignItems:"center",flexWrap:"wrap"}}>
              <input value={search} onChange={e=>setSearch(e.target.value)} placeholder="Search committees…" style={{flex:1,minWidth:180,padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12}}/>
              {["ALL","NEW","JCI"].map(f=><button key={f} onClick={()=>setFilter(f)} style={{padding:"5px 12px",borderRadius:8,fontSize:10,cursor:"pointer",background:filter===f?T.goldD:"transparent",border:`1px solid ${filter===f?T.gold:T.border}`,color:filter===f?T.goldL:T.muted}}>{f==="NEW"?"🆕 New 6th":f==="JCI"?"🌐 JCI":"All"}</button>)}
              <div style={{fontSize:11,color:T.muted}}>{filtered.length}/{committees.length}</div>
            </div>
          </div>
          <div style={{display:"grid",gap:8}}>
            {filtered.map(c=>{
              const isOpen=expanded===c.id;
              const docs=Array.isArray(c.required_docs)?c.required_docs:(c.required_docs?JSON.parse(c.required_docs):[]);
              const mCount=meetingCount(c.id); const last=lastMeeting(c.id);
              return (
                <div key={c.id} style={{background:T.panel,border:`1px solid ${c.is_new_in_6th?`${T.gold}30`:T.border}`,borderRadius:10,overflow:"hidden"}}>
                  <div style={{padding:"14px 16px",cursor:"pointer"}} onClick={()=>setExpanded(isOpen?null:c.id)}>
                    <div style={{display:"flex",gap:10,alignItems:"flex-start"}}>
                      <div style={{flex:1}}>
                        <div style={{display:"flex",gap:8,alignItems:"center",marginBottom:5,flexWrap:"wrap"}}>
                          <span style={{fontSize:13,fontWeight:700,color:T.white}}>{c.name}</span>
                          {c.is_new_in_6th&&<span style={{fontSize:8,padding:"2px 7px",borderRadius:5,background:`${T.gold}20`,color:T.gold,fontWeight:700}}>NEW 6TH</span>}
                          {c.is_jci&&<span style={{fontSize:8,padding:"2px 7px",borderRadius:5,background:T.blueD,color:T.blue}}>JCI</span>}
                          {mCount>0?<span style={{fontSize:8,padding:"2px 7px",borderRadius:5,background:T.greenD,color:T.green}}>✓ {mCount} meeting{mCount>1?"s":""} recorded</span>
                            :<span style={{fontSize:8,padding:"2px 7px",borderRadius:5,background:T.redD,color:T.red}}>No meetings recorded</span>}
                        </div>
                        <div style={{display:"flex",gap:12,flexWrap:"wrap"}}>
                          <span style={{fontSize:10,color:T.muted}}>📋 {c.chapter_ref}</span>
                          <span style={{fontSize:10,color:T.muted}}>🔄 {c.frequency}</span>
                          <span style={{fontSize:10,color:T.muted}}>👤 {c.chair}</span>
                          {last&&<span style={{fontSize:10,color:T.green}}>Last: {last}</span>}
                        </div>
                      </div>
                      <button onClick={e=>{e.stopPropagation();setShowMOMForm(c.id);setMOMForm(emptyMOM());setView("reference");}} style={{padding:"4px 10px",borderRadius:6,fontSize:9,cursor:"pointer",background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,flexShrink:0}}>+ Add MOM</button>
                      <span style={{fontSize:14,color:T.muted}}>{isOpen?"▲":"▼"}</span>
                    </div>
                  </div>
                  {/* MOM Form inline */}
                  {showMOMForm===c.id&&(
                    <div style={{borderTop:`1px solid ${T.gold}40`,padding:"16px",background:T.panel2}}>
                      <div style={{fontSize:11,fontWeight:700,color:T.gold,marginBottom:12,letterSpacing:1}}>📝 ADD MEETING MINUTES — {c.name}</div>
                      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                        {[["Meeting Date *","date","meeting_date"],["Meeting No.","text","meeting_no"],["Venue","text","venue"],["Chairperson *","text","chairperson"]].map(([l,t,k])=>(
                          <div key={k}><div style={lbl}>{l}</div><input type={t} value={momForm[k]} onChange={e=>setMOMForm(f=>({...f,[k]:e.target.value}))} style={inp}/></div>
                        ))}
                        <div><div style={lbl}>Members Present</div><input type="number" value={momForm.members_present} onChange={e=>setMOMForm(f=>({...f,members_present:e.target.value}))} style={inp}/></div>
                        <div><div style={lbl}>Total Members</div><input type="number" value={momForm.members_total} onChange={e=>setMOMForm(f=>({...f,members_total:e.target.value}))} style={inp}/></div>
                      </div>
                      <div style={{display:"flex",gap:16,marginBottom:12}}>
                        <label style={{display:"flex",alignItems:"center",gap:6,fontSize:11,color:T.text,cursor:"pointer"}}>
                          <input type="checkbox" checked={momForm.quorum_met} onChange={e=>setMOMForm(f=>({...f,quorum_met:e.target.checked}))}/> Quorum Met
                        </label>
                        <label style={{display:"flex",alignItems:"center",gap:6,fontSize:11,color:T.text,cursor:"pointer"}}>
                          <input type="checkbox" checked={momForm.previous_capa_reviewed} onChange={e=>setMOMForm(f=>({...f,previous_capa_reviewed:e.target.checked}))}/> Previous CAPA Reviewed
                        </label>
                      </div>
                      {/* Agenda items */}
                      <div style={{marginBottom:12}}>
                        <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:8}}>
                          <div style={{fontSize:10,fontWeight:700,color:T.gold,letterSpacing:1}}>AGENDA ITEMS</div>
                          <button onClick={addAgendaItem} style={{padding:"3px 10px",borderRadius:6,fontSize:9,cursor:"pointer",background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold}}>+ Add Item</button>
                        </div>
                        {momForm.agenda_items.map((ag,i)=>(
                          <div key={i} style={{background:T.panel,borderRadius:8,padding:"10px",marginBottom:8,border:`1px solid ${T.border}`}}>
                            <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:6}}>
                              <div style={{fontSize:9,color:T.gold,fontWeight:700}}>ITEM {i+1}</div>
                              {momForm.agenda_items.length>1&&<button onClick={()=>removeAgenda(i)} style={{fontSize:9,color:T.red,background:"transparent",border:"none",cursor:"pointer"}}>✕ Remove</button>}
                            </div>
                            <div style={{display:"grid",gap:6}}>
                              {[["Agenda Item","item"],["Discussion","discussion"],["Decision","decision"]].map(([l,k])=>(
                                <div key={k}><div style={lbl}>{l}</div><input value={ag[k]} onChange={e=>updateAgenda(i,k,e.target.value)} style={inp}/></div>
                              ))}
                              <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:8}}>
                                <div><div style={lbl}>Action Owner</div><input value={ag.action_owner} onChange={e=>updateAgenda(i,"action_owner",e.target.value)} style={inp}/></div>
                                <div><div style={lbl}>Target Date</div><input type="date" value={ag.target_date} onChange={e=>updateAgenda(i,"target_date",e.target.value)} style={inp}/></div>
                              </div>
                            </div>
                          </div>
                        ))}
                      </div>
                      {/* Minutes & next meeting */}
                      <div style={{marginBottom:10}}><div style={lbl}>MINUTES / SUMMARY</div><textarea value={momForm.minutes_text} onChange={e=>setMOMForm(f=>({...f,minutes_text:e.target.value}))} rows={3} style={{...inp,resize:"vertical"}}/></div>
                      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:12}}>
                        <div><div style={lbl}>Next Meeting Date</div><input type="date" value={momForm.next_meeting_date} onChange={e=>setMOMForm(f=>({...f,next_meeting_date:e.target.value}))} style={inp}/></div>
                        <div><div style={lbl}>Next Meeting Agenda</div><input value={momForm.next_meeting_agenda} onChange={e=>setMOMForm(f=>({...f,next_meeting_agenda:e.target.value}))} style={inp}/></div>
                        <div><div style={lbl}>Minutes Approved By</div><input value={momForm.minutes_approved_by} onChange={e=>setMOMForm(f=>({...f,minutes_approved_by:e.target.value}))} style={inp}/></div>
                        <div><div style={lbl}>Approval Date</div><input type="date" value={momForm.minutes_approved_date} onChange={e=>setMOMForm(f=>({...f,minutes_approved_date:e.target.value}))} style={inp}/></div>
                      </div>
                      <div style={{display:"flex",gap:8}}>
                        <button onClick={()=>saveMOM(c.id)} disabled={saving} style={{padding:"8px 20px",borderRadius:8,background:T.green,border:"none",color:T.bg,fontSize:11,fontWeight:700,cursor:"pointer"}}>{saving?"Saving…":"💾 Save Meeting Minutes"}</button>
                        <button onClick={()=>{setShowMOMForm(null);setMOMForm(emptyMOM());}} style={{padding:"8px 16px",borderRadius:8,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:11,cursor:"pointer"}}>Cancel</button>
                      </div>
                    </div>
                  )}
                  {isOpen&&(
                    <div style={{borderTop:`1px solid ${T.border}`,padding:"14px 16px",display:"grid",gap:12}}>
                      <div><div style={{fontSize:9,color:T.muted,marginBottom:5,letterSpacing:1}}>SCOPE</div><div style={{fontSize:11,color:T.text,lineHeight:1.6}}>{c.scope}</div></div>
                      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:12}}>
                        <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>COORDINATOR</div><div style={{fontSize:11,color:T.text}}>{c.coordinator}</div></div>
                        <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>MEMBERS</div><div style={{fontSize:11,color:T.text,lineHeight:1.5}}>{c.members}</div></div>
                      </div>
                      {docs.length>0&&<div><div style={{fontSize:9,color:T.muted,marginBottom:7,letterSpacing:1}}>REQUIRED DOCUMENTS</div><div style={{display:"flex",gap:5,flexWrap:"wrap"}}>{docs.map((d,i)=><span key={i} style={{fontSize:10,padding:"3px 10px",borderRadius:6,background:T.goldD,border:`1px solid ${T.gold}30`,color:T.gold}}>📄 {d}</span>)}</div></div>}
                      {c.linked_oes?.length>0&&<div><div style={{fontSize:9,color:T.muted,marginBottom:5}}>LINKED OEs</div><div style={{display:"flex",gap:4,flexWrap:"wrap"}}>{c.linked_oes.map(oe=><span key={oe} style={{fontSize:9,padding:"2px 7px",borderRadius:5,background:T.blueD,color:T.blue,fontFamily:"monospace"}}>{oe}</span>)}</div></div>}
                      {c.formation_guide&&(()=>{
                        const fg=typeof c.formation_guide==="string"?JSON.parse(c.formation_guide):c.formation_guide;
                        const isGuideOpen=guideOpen===c.id;
                        return (
                          <div style={{borderTop:`1px dashed ${T.border}`,paddingTop:10,marginTop:2}}>
                            <div onClick={()=>setGuideOpen(isGuideOpen?null:c.id)} style={{cursor:"pointer",display:"flex",alignItems:"center",gap:6,fontSize:10,color:T.gold,letterSpacing:1,fontWeight:700}}>
                              <span>{isGuideOpen?"▲":"▼"}</span><span>📖 FORMATION GUIDE — HOW TO CONSTITUTE & RUN</span>
                            </div>
                            {isGuideOpen&&(
                              <div style={{display:"grid",gap:12,marginTop:11,padding:"12px 14px",background:T.panel2,borderRadius:8,border:`1px solid ${T.gold}20`}}>
                                <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:12}}>
                                  <div><div style={{fontSize:9,color:T.gold,marginBottom:4,letterSpacing:1,fontWeight:700}}>QUORUM</div><div style={{fontSize:11,color:T.text,lineHeight:1.5}}>{fg.quorum}</div></div>
                                  <div><div style={{fontSize:9,color:T.gold,marginBottom:4,letterSpacing:1,fontWeight:700}}>TERM</div><div style={{fontSize:11,color:T.text,lineHeight:1.5}}>{fg.term}</div></div>
                                </div>
                                {Array.isArray(fg.agenda_template)&&fg.agenda_template.length>0&&(
                                  <div>
                                    <div style={{fontSize:9,color:T.gold,marginBottom:6,letterSpacing:1,fontWeight:700}}>AGENDA TEMPLATE ({fg.agenda_template.length} ITEMS)</div>
                                    <div style={{display:"grid",gap:4}}>
                                      {fg.agenda_template.map((item,i)=>(
                                        <div key={i} style={{display:"flex",gap:8,alignItems:"flex-start",padding:"6px 9px",background:T.panel,borderRadius:5,border:`1px solid ${T.border}`}}>
                                          <span style={{fontSize:9,color:T.gold,fontWeight:700,minWidth:14}}>{i+1}.</span>
                                          <span style={{fontSize:10,color:T.text,lineHeight:1.5}}>{item}</span>
                                        </div>
                                      ))}
                                    </div>
                                  </div>
                                )}
                                {Array.isArray(fg.induction_first_90_days)&&fg.induction_first_90_days.length>0&&(
                                  <div>
                                    <div style={{fontSize:9,color:T.gold,marginBottom:6,letterSpacing:1,fontWeight:700}}>FIRST 90 DAYS — INDUCTION ROADMAP</div>
                                    <div style={{display:"grid",gap:5}}>
                                      {fg.induction_first_90_days.map((step,i)=>(
                                        <div key={i} style={{padding:"7px 10px",background:T.panel,borderRadius:5,borderLeft:`3px solid ${T.gold}`,fontSize:10,color:T.text,lineHeight:1.55}}>{step}</div>
                                      ))}
                                    </div>
                                  </div>
                                )}
                                {fg.escalation_path&&(
                                  <div style={{padding:"10px 12px",background:T.redD,borderRadius:6,border:`1px solid ${T.red}30`}}>
                                    <div style={{fontSize:9,color:T.red,marginBottom:5,letterSpacing:1,fontWeight:700}}>⚠️ ESCALATION PATH</div>
                                    <div style={{fontSize:10,color:T.text,lineHeight:1.55}}>{fg.escalation_path}</div>
                                  </div>
                                )}
                              </div>
                            )}
                          </div>
                        );
                      })()}
                      {/* Past meetings for this committee */}
                      {meetings.filter(m=>m.committee_id===c.id).length>0&&(
                        <div style={{borderTop:`1px dashed ${T.border}`,paddingTop:10}}>
                          <div style={{fontSize:9,color:T.muted,marginBottom:8,letterSpacing:1}}>MEETING HISTORY ({meetings.filter(m=>m.committee_id===c.id).length})</div>
                          {meetings.filter(m=>m.committee_id===c.id).map(m=>(
                            <div key={m.id} style={{background:T.panel2,borderRadius:8,padding:"10px 12px",marginBottom:6,border:`1px solid ${T.green}20`}}>
                              <div style={{display:"flex",justifyContent:"space-between",alignItems:"flex-start"}}>
                                <div>
                                  <div style={{fontSize:11,fontWeight:700,color:T.white}}>{m.meeting_date} {m.meeting_no&&<span style={{color:T.muted,fontSize:9}}>— {m.meeting_no}</span>}</div>
                                  <div style={{fontSize:10,color:T.muted,marginTop:2}}>Chair: {m.chairperson} | {m.members_present}/{m.members_total} members | Quorum: {m.quorum_met?"✅":"❌"}</div>
                                  {m.agenda_items?.length>0&&<div style={{fontSize:9,color:T.muted,marginTop:3}}>{m.agenda_items.length} agenda items · {m.previous_capa_reviewed?"CAPA reviewed":"CAPA not reviewed"}</div>}
                                </div>
                                <button onClick={()=>deleteMeeting(m.id)} style={{fontSize:9,color:T.red,background:"transparent",border:`1px solid ${T.red}30`,borderRadius:4,padding:"2px 7px",cursor:"pointer"}}>Delete</button>
                              </div>
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* MOM RECORDS VIEW */}
      {view==="mom"&&(
        <div>
          {meetings.length===0?(
            <div style={{textAlign:"center",padding:40,color:T.muted}}>
              <div style={{fontSize:32,marginBottom:12}}>📝</div>
              <div style={{fontSize:13,marginBottom:6}}>No meeting minutes recorded yet.</div>
              <div style={{fontSize:11}}>Switch to Reference view and click "+ Add MOM" on any committee.</div>
            </div>
          ):(
            <div style={{display:"grid",gap:8}}>
              {meetings.map(m=>{
                const comm=committees.find(c=>c.id===m.committee_id);
                return (
                  <div key={m.id} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"14px 16px"}}>
                    <div style={{display:"flex",justifyContent:"space-between",alignItems:"flex-start",marginBottom:8}}>
                      <div>
                        <div style={{fontSize:12,fontWeight:700,color:T.white}}>{comm?.name||m.committee_id}</div>
                        <div style={{fontSize:10,color:T.muted,marginTop:2}}>{m.meeting_date} {m.meeting_no&&`— ${m.meeting_no}`} | {m.venue||"Venue not specified"}</div>
                      </div>
                      <div style={{display:"flex",gap:6,alignItems:"center"}}>
                        <span style={{fontSize:9,padding:"2px 8px",borderRadius:4,background:m.quorum_met?T.greenD:T.redD,color:m.quorum_met?T.green:T.red}}>Quorum {m.quorum_met?"Met":"Not Met"}</span>
                        <button onClick={()=>deleteMeeting(m.id)} style={{fontSize:9,color:T.red,background:"transparent",border:`1px solid ${T.red}30`,borderRadius:4,padding:"2px 7px",cursor:"pointer"}}>Delete</button>
                      </div>
                    </div>
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr 1fr",gap:8,marginBottom:8}}>
                      <div style={{background:T.panel2,borderRadius:6,padding:"7px 10px"}}><div style={{fontSize:8,color:T.muted}}>CHAIRPERSON</div><div style={{fontSize:10,color:T.text}}>{m.chairperson}</div></div>
                      <div style={{background:T.panel2,borderRadius:6,padding:"7px 10px"}}><div style={{fontSize:8,color:T.muted}}>ATTENDANCE</div><div style={{fontSize:10,color:T.text}}>{m.members_present||"—"}/{m.members_total||"—"} members</div></div>
                      <div style={{background:T.panel2,borderRadius:6,padding:"7px 10px"}}><div style={{fontSize:8,color:T.muted}}>NEXT MEETING</div><div style={{fontSize:10,color:T.text}}>{m.next_meeting_date||"Not set"}</div></div>
                    </div>
                    {m.agenda_items?.length>0&&(
                      <div>
                        <div style={{fontSize:9,color:T.muted,marginBottom:5,letterSpacing:1}}>AGENDA & DECISIONS ({m.agenda_items.length} items)</div>
                        {m.agenda_items.map((ag,i)=>(
                          <div key={i} style={{background:T.panel2,borderRadius:6,padding:"7px 10px",marginBottom:4,borderLeft:`2px solid ${T.gold}`}}>
                            <div style={{fontSize:10,fontWeight:700,color:T.text}}>{i+1}. {ag.item}</div>
                            {ag.decision&&<div style={{fontSize:9,color:T.green,marginTop:2}}>Decision: {ag.decision}</div>}
                            {ag.action_owner&&<div style={{fontSize:9,color:T.blue,marginTop:1}}>Action: {ag.action_owner} by {ag.target_date||"—"}</div>}
                          </div>
                        ))}
                      </div>
                    )}
                    {m.minutes_approved_by&&<div style={{fontSize:9,color:T.muted,marginTop:6}}>Minutes approved by: {m.minutes_approved_by} on {m.minutes_approved_date||"—"}</div>}
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

// ── KPIs — with monthly data entry ───────────────────────────
function KPIsScreen({ hospitalId }) {
  const [kpis,setKpis]=useState([]);
  const [kpiData,setKpiData]=useState([]); // existing monthly data
  const [loading,setLoading]=useState(true);
  const [tab,setTab]=useState("hospital");
  const [search,setSearch]=useState("");
  const [expanded,setExpanded]=useState(null);
  const [dataForm,setDataForm]=useState({}); // {kpiId: {month,year,value,trend,capa_required,capa_notes}}
  const [saving,setSaving]=useState(null);
  const [saveSuccess,setSaveSuccess]=useState(null);

  const now=new Date(); const curMonth=now.getMonth()+1; const curYear=now.getFullYear();
  const MONTHS=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];

  useEffect(()=>{
    supabase.from("kpis").select("*").order("kpi_no").then(({data})=>setKpis(data||[]));
    if(hospitalId){
      supabase.from("kpi_data").select("*").eq("hospital_id",hospitalId)
        .order("year",{ascending:false}).order("month",{ascending:false})
        .then(({data})=>{setKpiData(data||[]);setLoading(false);});
    } else { setLoading(false); }
  },[hospitalId]);

  const filtered=kpis.filter(k=>k.category===tab&&(!search||k.name.toLowerCase().includes(search.toLowerCase())||(k.dept||"").toLowerCase().includes(search.toLowerCase())));
  const depts=[...new Set(kpis.filter(k=>k.category==="dept_specific").map(k=>k.dept))].sort();

  const getKpiHistory=(kpiId)=>kpiData.filter(d=>String(d.kpi_id)===String(kpiId)).sort((a,b)=>b.year-a.year||b.month-a.month);
  const getLatest=(kpiId)=>getKpiHistory(kpiId)[0];
  const monthsTracked=(kpiId)=>new Set(kpiData.filter(d=>String(d.kpi_id)===String(kpiId)).map(d=>`${d.year}-${d.month}`)).size;

  const trackingStatus=(kpiId)=>{
    const n=monthsTracked(kpiId);
    if(n===0) return {label:"Not started",color:T.red};
    if(n<3) return {label:`${n} month${n>1?"s":""}`,color:T.orange};
    return {label:`${n} months`,color:T.green};
  };

  const initForm=(kpi)=>{
    if(!dataForm[kpi.id]){
      setDataForm(f=>({...f,[kpi.id]:{month:curMonth,year:curYear,value:"",trend:"stable",capa_required:false,capa_notes:""}}));
    }
  };

  const saveKpiData=async(kpi)=>{
    const f=dataForm[kpi.id];
    if(!f||f.value===""){alert("Enter a value to save.");return;}
    setSaving(kpi.id);
    // check if entry for this month/year exists
    const existing=kpiData.find(d=>String(d.kpi_id)===String(kpi.id)&&d.month===parseInt(f.month)&&d.year===parseInt(f.year));
    let error;
    if(existing){
      ({error}=await supabase.from("kpi_data").update({
        value:parseFloat(f.value),trend:f.trend,capa_required:f.capa_required,capa_notes:f.capa_notes||null
      }).eq("id",existing.id));
    } else {
      ({error}=await supabase.from("kpi_data").insert({
        hospital_id:hospitalId,kpi_id:kpi.id,
        month:parseInt(f.month),year:parseInt(f.year),
        value:parseFloat(f.value),benchmark:kpi.benchmark_value||null,
        trend:f.trend,capa_required:f.capa_required,capa_notes:f.capa_notes||null
      }));
    }
    if(!error){
      const{data}=await supabase.from("kpi_data").select("*").eq("hospital_id",hospitalId).order("year",{ascending:false}).order("month",{ascending:false});
      setKpiData(data||[]);
      setSaveSuccess(kpi.id);
      setTimeout(()=>setSaveSuccess(null),2000);
    } else { alert("Error: "+error.message); }
    setSaving(null);
  };

  // Overall KPI tracking summary
  const tracked=kpis.filter(k=>monthsTracked(k.id)>=3).length;
  const total=kpis.length;

  const inp={padding:"6px 9px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:11};

  if(loading) return <div style={{textAlign:"center",color:T.muted,padding:40}}>Loading KPIs…</div>;

  return (
    <div>
      {/* Summary bar */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:14}}>
        <div style={{display:"flex",gap:16,alignItems:"center",flexWrap:"wrap"}}>
          <div style={{flex:1}}>
            <div style={{fontSize:9,color:T.muted,marginBottom:3,letterSpacing:1}}>KPI TRACKING STATUS</div>
            <div style={{fontSize:12,color:tracked>=total*0.8?T.green:tracked>0?T.orange:T.red,fontWeight:700}}>
              {tracked}/{total} KPIs with ≥3 months data
              <span style={{fontSize:9,color:T.muted,marginLeft:6}}>(minimum required for NABH assessment)</span>
            </div>
            <div style={{height:4,background:T.border,borderRadius:2,marginTop:6}}>
              <div style={{height:"100%",borderRadius:2,background:tracked>=total*0.8?T.green:tracked>0?T.orange:T.red,width:`${Math.min(100,(tracked/total)*100)}%`,transition:"width 0.5s"}}/>
            </div>
          </div>
          <div style={{textAlign:"right"}}>
            <div style={{fontSize:20,fontWeight:700,color:T.gold}}>{Math.round((tracked/total)*100)}%</div>
            <div style={{fontSize:9,color:T.muted}}>KPI readiness</div>
          </div>
        </div>
      </div>

      {/* Tabs & Search */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:14}}>
        <div style={{display:"flex",gap:8,marginBottom:10}}>
          {[["hospital","🏥 Hospital-wide (32)"],["dept_specific","🏬 Dept-specific (18)"]].map(([k,l])=>(
            <button key={k} onClick={()=>{setTab(k);setSearch("");}} style={{padding:"6px 14px",borderRadius:8,fontSize:10,cursor:"pointer",background:tab===k?T.goldD:"transparent",border:`1px solid ${tab===k?T.gold:T.border}`,color:tab===k?T.goldL:T.muted}}>{l}</button>
          ))}
        </div>
        <input value={search} onChange={e=>setSearch(e.target.value)} placeholder="Search KPIs…" style={{width:"100%",padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12,boxSizing:"border-box"}}/>
      </div>
      {tab==="dept_specific"&&!search&&<div style={{display:"flex",gap:5,flexWrap:"wrap",marginBottom:10}}>{depts.map(d=><button key={d} onClick={()=>setSearch(d)} style={{padding:"3px 10px",borderRadius:6,fontSize:9,cursor:"pointer",background:T.blueD,border:`1px solid ${T.blue}30`,color:T.blue}}>{d}</button>)}</div>}

      <div style={{display:"grid",gap:8}}>
        {filtered.map(k=>{
          const isOpen=expanded===k.id;
          const history=getKpiHistory(k.id);
          const latest=getLatest(k.id);
          const status=trackingStatus(k.id);
          const f=dataForm[k.id]||{month:curMonth,year:curYear,value:"",trend:"stable",capa_required:false,capa_notes:""};

          return (
            <div key={k.id} style={{background:T.panel,border:`1px solid ${k.is_mandatory?`${T.gold}25`:T.border}`,borderRadius:10,overflow:"hidden"}}>
              <div style={{padding:"12px 16px",cursor:"pointer"}} onClick={()=>{setExpanded(isOpen?null:k.id);if(!isOpen)initForm(k);}}>
                <div style={{display:"flex",gap:10,alignItems:"flex-start"}}>
                  <div style={{width:28,height:28,borderRadius:6,background:T.goldD,border:`1px solid ${T.gold}30`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:10,fontWeight:800,color:T.gold,flexShrink:0}}>{k.kpi_no}</div>
                  <div style={{flex:1}}>
                    <div style={{display:"flex",gap:7,alignItems:"center",marginBottom:3,flexWrap:"wrap"}}>
                      <span style={{fontSize:12,fontWeight:700,color:T.white}}>{k.name}</span>
                      {k.is_mandatory&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:`${T.red}20`,color:T.red}}>MANDATORY</span>}
                      {k.dept&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.blueD,color:T.blue}}>{k.dept}</span>}
                      <span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:`${status.color}20`,color:status.color}}>📊 {status.label}</span>
                    </div>
                    <div style={{display:"flex",gap:10,flexWrap:"wrap"}}>
                      <span style={{fontSize:10,color:T.muted}}>📋 {k.standard_ref}</span>
                      <span style={{fontSize:10,color:T.green,fontWeight:600}}>🎯 {k.target}</span>
                      <span style={{fontSize:10,color:T.muted}}>📅 {k.frequency}</span>
                      {latest&&<span style={{fontSize:10,color:T.blue}}>Latest: {latest.value} ({MONTHS[latest.month-1]} {latest.year})</span>}
                    </div>
                  </div>
                  <span style={{fontSize:14,color:T.muted}}>{isOpen?"▲":"▼"}</span>
                </div>
              </div>

              {isOpen&&(
                <div style={{borderTop:`1px solid ${T.border}`,padding:"14px 16px",display:"grid",gap:12}}>
                  {/* KPI definition */}
                  <div style={{fontSize:11,color:T.text,lineHeight:1.6}}>{k.definition}</div>
                  <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
                    <div style={{background:T.panel2,borderRadius:8,padding:"10px 12px"}}><div style={{fontSize:9,color:T.muted,marginBottom:4}}>NUMERATOR</div><div style={{fontSize:11,color:T.text}}>{k.numerator}</div></div>
                    <div style={{background:T.panel2,borderRadius:8,padding:"10px 12px"}}><div style={{fontSize:9,color:T.muted,marginBottom:4}}>DENOMINATOR</div><div style={{fontSize:11,color:T.text}}>{k.denominator}</div></div>
                  </div>
                  <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
                    <div style={{background:T.goldD,border:`1px solid ${T.gold}30`,borderRadius:8,padding:"8px 12px",flex:1}}><div style={{fontSize:9,color:T.muted,marginBottom:3}}>FORMULA</div><div style={{fontSize:11,color:T.gold,fontWeight:700}}>{k.formula} → {k.unit}</div></div>
                    <div style={{background:T.greenD,border:`1px solid ${T.green}30`,borderRadius:8,padding:"8px 12px",flex:1}}><div style={{fontSize:9,color:T.muted,marginBottom:3}}>TARGET</div><div style={{fontSize:11,color:T.green,fontWeight:700}}>{k.target}</div></div>
                  </div>
                  {k.remarks&&<div style={{fontSize:10,color:T.muted,fontStyle:"italic",lineHeight:1.5}}>💡 {k.remarks}</div>}

                  {/* DATA ENTRY */}
                  <div style={{borderTop:`1px solid ${T.border}`,paddingTop:12}}>
                    <div style={{fontSize:10,fontWeight:700,color:T.gold,marginBottom:10,letterSpacing:1}}>📥 ENTER MONTHLY DATA</div>
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr 1fr",gap:8,marginBottom:8}}>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>MONTH</div>
                        <select value={f.month} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,month:parseInt(e.target.value)}}))} style={{...inp,width:"100%"}}>
                          {MONTHS.map((m,i)=><option key={i} value={i+1}>{m}</option>)}
                        </select>
                      </div>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>YEAR</div>
                        <select value={f.year} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,year:parseInt(e.target.value)}}))} style={{...inp,width:"100%"}}>
                          {[curYear-1,curYear,curYear+1].map(y=><option key={y} value={y}>{y}</option>)}
                        </select>
                      </div>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>VALUE ({k.unit})</div>
                        <input type="number" step="0.01" value={f.value} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,value:e.target.value}}))} placeholder="Enter value" style={{...inp,width:"100%",boxSizing:"border-box"}}/>
                      </div>
                    </div>
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:8,marginBottom:8}}>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>TREND</div>
                        <select value={f.trend} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,trend:e.target.value}}))} style={{...inp,width:"100%"}}>
                          <option value="improving">📈 Improving</option>
                          <option value="stable">➡️ Stable</option>
                          <option value="worsening">📉 Worsening</option>
                        </select>
                      </div>
                      <div style={{display:"flex",alignItems:"flex-end"}}>
                        <label style={{display:"flex",alignItems:"center",gap:6,fontSize:11,color:T.text,cursor:"pointer",paddingBottom:2}}>
                          <input type="checkbox" checked={f.capa_required} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,capa_required:e.target.checked}}))}/> CAPA Required
                        </label>
                      </div>
                    </div>
                    {f.capa_required&&(
                      <div style={{marginBottom:8}}>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>CAPA NOTES</div>
                        <textarea value={f.capa_notes} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,capa_notes:e.target.value}}))} rows={2} placeholder="Describe corrective action planned…" style={{...inp,width:"100%",resize:"vertical",boxSizing:"border-box"}}/>
                      </div>
                    )}
                    <button onClick={()=>saveKpiData(k)} disabled={saving===k.id} style={{padding:"7px 18px",borderRadius:7,background:saveSuccess===k.id?T.green:T.goldD,border:`1px solid ${saveSuccess===k.id?T.green:T.gold}`,color:saveSuccess===k.id?T.bg:T.gold,fontSize:11,fontWeight:700,cursor:"pointer"}}>
                      {saving===k.id?"Saving…":saveSuccess===k.id?"✅ Saved!":"💾 Save Entry"}
                    </button>
                  </div>

                  {/* History */}
                  {history.length>0&&(
                    <div style={{borderTop:`1px solid ${T.border}`,paddingTop:12}}>
                      <KpiTrendChart history={history} target={k.benchmark_value||k.target} unit={k.unit}/>
                      <div style={{fontSize:9,color:T.muted,marginBottom:8,letterSpacing:1,marginTop:12}}>TRACKING HISTORY ({history.length} entries)</div>
                      <div style={{display:"grid",gap:4}}>
                        {history.slice(0,6).map(d=>(
                          <div key={d.id} style={{display:"flex",gap:10,alignItems:"center",padding:"6px 10px",background:T.panel2,borderRadius:6,border:`1px solid ${d.capa_required?`${T.orange}30`:T.border}`}}>
                            <span style={{fontSize:10,color:T.muted,minWidth:60}}>{MONTHS[d.month-1]} {d.year}</span>
                            <span style={{fontSize:12,fontWeight:700,color:T.white}}>{d.value} {k.unit}</span>
                            <span style={{fontSize:9,color:d.trend==="improving"?T.green:d.trend==="worsening"?T.red:T.muted}}>{d.trend==="improving"?"📈":d.trend==="worsening"?"📉":"➡️"} {d.trend}</span>
                            {d.capa_required&&<span style={{fontSize:9,color:T.orange}}>⚠️ CAPA</span>}
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        })}
        {filtered.length===0&&<div style={{textAlign:"center",color:T.muted,padding:30,fontSize:12}}>No KPIs match.</div>}
      </div>
    </div>
  );
}

// ── AUDITS — 3 tabs: NABH Audits | My Audits | What is Audit ─────────────────────────────────────
function AuditsScreen({ hospitalId }) {
  const [mainTab,setMainTab]=useState("nabh"); // nabh | mine | learn

  // ── NABH AUDITS state ──
  const [audits,setAudits]=useState([]);
  const [auditRecords,setAuditRecords]=useState([]);
  const [loading,setLoading]=useState(true);
  const [filter,setFilter]=useState("ALL");
  const [catFilter,setCatFilter]=useState("ALL");
  const [expanded,setExpanded]=useState(null);
  const [checked,setChecked]=useState({});
  const [guideOpen,setGuideOpen]=useState(null);
  const [showRecordForm,setShowRecordForm]=useState(null);
  const [saving,setSaving]=useState(false);
  const [recordSuccess,setRecordSuccess]=useState(null);

  // ── MY AUDITS state ──
  const [customAudits,setCustomAudits]=useState([]);
  const [customRecords,setCustomRecords]=useState([]);
  const [showCreateForm,setShowCreateForm]=useState(false);
  const [createForm,setCreateForm]=useState({name:"",audit_category:"clinical",is_core:false,parameters:[]});
  const [newParam,setNewParam]=useState("");
  const [savingCreate,setSavingCreate]=useState(false);
  const [customExpanded,setCustomExpanded]=useState(null);
  const [showCustomRecord,setShowCustomRecord]=useState(null);
  const [customRecordForm,setCustomRecordForm]=useState({});
  const [savingCustomRecord,setSavingCustomRecord]=useState(false);
  const [customRecordSuccess,setCustomRecordSuccess]=useState(null);
  const [deleteConfirm,setDeleteConfirm]=useState(null);

  const emptyRecord=()=>({audit_date:"",auditor_name:"",department:"",sample_size:"",compliant_count:"",findings:"",capa_raised:false,capa_notes:"",capa_target_date:"",reaudit_date:"",status:"completed"});
  const [recordForm,setRecordForm]=useState(emptyRecord());

  const loadData=async()=>{
    supabase.from("audit_checklists").select("*").order("audit_code").then(({data})=>setAudits(data||[]));
    if(hospitalId){
      const[{data:ar},{data:ca},{data:cr}]=await Promise.all([
        supabase.from("audit_records").select("*").eq("hospital_id",hospitalId).is("custom_audit_id",null).order("audit_date",{ascending:false}),
        supabase.from("custom_audits").select("*").eq("hospital_id",hospitalId).order("created_at",{ascending:false}),
        supabase.from("audit_records").select("*").eq("hospital_id",hospitalId).not("custom_audit_id","is",null).order("audit_date",{ascending:false}),
      ]);
      setAuditRecords(ar||[]);
      setCustomAudits(ca||[]);
      setCustomRecords(cr||[]);
    }
    setLoading(false);
  };

  useEffect(()=>{loadData();},[hospitalId]); // eslint-disable-line

  const filtered=audits.filter(a=>{
    const coreMatch=filter==="ALL"||(filter==="CORE"&&a.is_core)||(filter==="NON_CORE"&&!a.is_core);
    const catMatch=catFilter==="ALL"||(a.audit_category||"clinical")===catFilter;
    return coreMatch&&catMatch;
  });
  const getRecords=(auditId)=>auditRecords.filter(r=>String(r.audit_id)===String(auditId));
  const getCustomRecords=(customAuditId)=>customRecords.filter(r=>String(r.custom_audit_id)===String(customAuditId));
  const totalAudits=audits.length;
  const completedAudits=new Set(auditRecords.filter(r=>r.status==="completed"&&new Date(r.audit_date)>new Date(Date.now()-365*24*60*60*1000)).map(r=>r.audit_id)).size;

  const saveRecord=async(auditId)=>{
    if(!recordForm.audit_date){alert("Audit date is required.");return;}
    setSaving(true);
    const {error}=await supabase.from("audit_records").insert({
      hospital_id:hospitalId,audit_id:auditId,
      audit_date:recordForm.audit_date,
      auditor_name:recordForm.auditor_name||null,
      department:recordForm.department||null,
      sample_size:recordForm.sample_size?parseInt(recordForm.sample_size):null,
      compliant_count:recordForm.compliant_count?parseInt(recordForm.compliant_count):null,
      findings:recordForm.findings||null,
      capa_raised:recordForm.capa_raised,
      capa_notes:recordForm.capa_notes||null,
      capa_target_date:recordForm.capa_target_date||null,
      reaudit_date:recordForm.reaudit_date||null,
      status:recordForm.status,
    });
    if(!error){
      const{data}=await supabase.from("audit_records").select("*").eq("hospital_id",hospitalId).is("custom_audit_id",null).order("audit_date",{ascending:false});
      setAuditRecords(data||[]);
      setShowRecordForm(null);
      setRecordForm(emptyRecord());
      setRecordSuccess(auditId);
      setTimeout(()=>setRecordSuccess(null),3000);
    } else { alert("Error: "+error.message); }
    setSaving(false);
  };

  const deleteRecord=async(id)=>{
    if(!window.confirm("Delete this audit record?"))return;
    await supabase.from("audit_records").delete().eq("id",id);
    setAuditRecords(r=>r.filter(x=>x.id!==id));
  };

  // ── CUSTOM AUDIT functions ──
  const createCustomAudit=async()=>{
    if(!createForm.name.trim()){alert("Audit name is required.");return;}
    setSavingCreate(true);
    const{data,error}=await supabase.from("custom_audits").insert({
      hospital_id:hospitalId,
      name:createForm.name.trim(),
      audit_category:createForm.audit_category,
      is_core:createForm.is_core,
      parameters:createForm.parameters,
    }).select().single();
    if(!error){
      setCustomAudits(p=>[data,...p]);
      setCreateForm({name:"",audit_category:"clinical",is_core:false,parameters:[]});
      setShowCreateForm(false);
    } else { alert("Error: "+error.message); }
    setSavingCreate(false);
  };

  const deleteCustomAudit=async(id)=>{
    await supabase.from("audit_records").delete().eq("custom_audit_id",id);
    await supabase.from("custom_audits").delete().eq("id",id);
    setCustomAudits(p=>p.filter(a=>a.id!==id));
    setCustomRecords(p=>p.filter(r=>r.custom_audit_id!==id));
    setDeleteConfirm(null);
  };

  const saveCustomRecord=async(audit)=>{
    if(!customRecordForm.audit_date){alert("Audit date is required.");return;}
    setSavingCustomRecord(true);
    const params=Array.isArray(audit.parameters)?audit.parameters:JSON.parse(audit.parameters||"[]");
    const checkedParams=params.filter((_,i)=>customRecordForm[`param_${i}`]);
    const compliantCount=checkedParams.length;
    const sampleSize=params.length||parseInt(customRecordForm.sample_size)||0;
    const{error}=await supabase.from("audit_records").insert({
      hospital_id:hospitalId,
      custom_audit_id:audit.id,
      audit_date:customRecordForm.audit_date,
      auditor_name:customRecordForm.auditor_name||null,
      department:customRecordForm.department||null,
      sample_size:sampleSize||null,
      compliant_count:params.length>0?compliantCount:(customRecordForm.compliant_count?parseInt(customRecordForm.compliant_count):null),
      findings:customRecordForm.findings||null,
      capa_raised:customRecordForm.capa_raised||false,
      capa_notes:customRecordForm.capa_notes||null,
      capa_target_date:customRecordForm.capa_target_date||null,
      reaudit_date:customRecordForm.reaudit_date||null,
      status:customRecordForm.status||"completed",
    });
    if(!error){
      const{data}=await supabase.from("audit_records").select("*").eq("hospital_id",hospitalId).not("custom_audit_id","is",null).order("audit_date",{ascending:false});
      setCustomRecords(data||[]);
      setShowCustomRecord(null);
      setCustomRecordForm({});
      setCustomRecordSuccess(audit.id);
      setTimeout(()=>setCustomRecordSuccess(null),3000);
    } else { alert("Error: "+error.message); }
    setSavingCustomRecord(false);
  };

  const deleteCustomRecord=async(id)=>{
    if(!window.confirm("Delete this record?"))return;
    await supabase.from("audit_records").delete().eq("id",id);
    setCustomRecords(r=>r.filter(x=>x.id!==id));
  };

  const AUDIT_CATEGORIES=[
    {value:"clinical",label:"🏥 Clinical Audit"},
    {value:"nursing",label:"💉 Nursing Audit"},
    {value:"qip",label:"🎯 Quality Improvement Project"},
    {value:"financial",label:"💰 Financial Audit"},
    {value:"structural",label:"🏗️ Structural Audit"},
    {value:"process",label:"⚙️ Process Audit"},
    {value:"outcome",label:"📊 Outcome Audit"},
    {value:"pharmacy",label:"💊 Pharmacy Audit"},
    {value:"dietary",label:"🍽️ Dietary Audit"},
    {value:"other",label:"📋 Other"},
  ];

  const inp={padding:"6px 9px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:11};
  const lbl={fontSize:9,color:T.muted,marginBottom:3,letterSpacing:1};

  if(loading) return <div style={{textAlign:"center",color:T.muted,padding:40}}>Loading audits…</div>;

  // ── WHAT IS AUDIT tab ──
  const LearnTab=()=>(
    <div style={{display:"grid",gap:12}}>
      <div style={{background:T.panel,border:`1px solid ${T.gold}40`,borderRadius:12,padding:"18px 20px"}}>
        <div style={{fontSize:9,letterSpacing:3,color:T.gold,marginBottom:8}}>WHAT IS AN AUDIT?</div>
        <div style={{fontSize:13,fontWeight:700,color:T.white,marginBottom:10,lineHeight:1.5}}>
          An audit is a systematic process of measuring current practice against a defined standard, identifying gaps, taking corrective action, and re-measuring to confirm improvement.
        </div>
        <div style={{fontSize:11,color:T.text,lineHeight:1.8}}>
          Audit is not just data collection. The improvement action and re-audit are mandatory parts of the cycle. A single data collection without follow-up action is <span style={{color:T.orange}}>not a complete audit</span>.
        </div>
      </div>

      {/* Audit Cycle */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"18px 20px"}}>
        <div style={{fontSize:9,letterSpacing:3,color:T.gold,marginBottom:14}}>THE AUDIT CYCLE — 5 STEPS</div>
        <div style={{display:"grid",gap:8}}>
          {[
            {step:1,color:T.blue,icon:"🎯",title:"Choose Topic & Set Standard",desc:"Identify what you want to measure. Define the standard — e.g. 'Hand hygiene compliance should be ≥85%'. Standard can come from NABH, hospital policy, or evidence-based guidelines."},
            {step:2,color:T.gold,icon:"📋",title:"Collect Data — Measure Current Practice",desc:"Observe, record, or review patient care against the standard. Define your sample size. This is your baseline measurement."},
            {step:3,color:T.orange,icon:"🔍",title:"Compare Data Against Standard",desc:"Calculate your compliance %. If below the standard, identify the root cause — is it a knowledge gap, process failure, resource issue, or behavioural problem?"},
            {step:4,color:T.red,icon:"🔧",title:"Implement Change",desc:"Take corrective action based on root cause. Could be re-training, SOP revision, infrastructure change, or process redesign. Document what change was made and when."},
            {step:5,color:T.green,icon:"✅",title:"Re-audit — Confirm Improvement",desc:"After allowing time for the change to embed (usually 3–6 months), repeat the audit. Compare new compliance % with baseline. This is the proof of improvement NABH assessors look for."},
          ].map(s=>(
            <div key={s.step} style={{display:"flex",gap:12,alignItems:"flex-start",padding:"12px 14px",background:T.panel2,borderRadius:8,border:`1px solid ${s.color}20`}}>
              <div style={{width:32,height:32,borderRadius:"50%",background:`${s.color}20`,border:`2px solid ${s.color}40`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:14,flexShrink:0}}>{s.icon}</div>
              <div>
                <div style={{fontSize:11,fontWeight:700,color:s.color,marginBottom:4}}>Step {s.step}: {s.title}</div>
                <div style={{fontSize:10,color:T.text,lineHeight:1.6}}>{s.desc}</div>
              </div>
            </div>
          ))}
        </div>
        <div style={{marginTop:12,padding:"10px 14px",background:T.greenD,border:`1px solid ${T.green}30`,borderRadius:8,fontSize:10,color:T.text,lineHeight:1.6}}>
          <span style={{fontWeight:700,color:T.green}}>Key message for NABH: </span>
          Assessors want to see the full cycle — not just records of audits done, but evidence that findings led to action and action led to improvement. Two complete cycles on the same topic is stronger than ten single-cycle audits.
        </div>
      </div>

      {/* Types */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"18px 20px"}}>
        <div style={{fontSize:9,letterSpacing:3,color:T.gold,marginBottom:12}}>TYPES OF AUDIT — NO FIXED NUMBER</div>
        <div style={{fontSize:11,color:T.text,lineHeight:1.7,marginBottom:12}}>
          NABH does not mandate a fixed number of audits. Audit can cover any area that is beneficial to patients and the hospital. What matters is: <span style={{color:T.gold,fontWeight:700}}>quality of the cycle, not quantity of audits.</span>
        </div>
        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:8}}>
          {[
            {cat:"Clinical Audit",icon:"🏥",desc:"Measures clinical care — hand hygiene, medication errors, consent, fall rates, surgical site infections"},
            {cat:"Nursing Audit",icon:"💉",desc:"Nursing-specific — IV care, catheter care, pressure ulcer prevention, nursing documentation"},
            {cat:"Quality Improvement Project",icon:"🎯",desc:"Structured project following improvement methodology. NABH mandates minimum 2 QIPs per year"},
            {cat:"Process Audit",icon:"⚙️",desc:"Measures whether processes are followed — discharge process, admission process, referral process"},
            {cat:"Structural Audit",icon:"🏗️",desc:"Physical infrastructure, equipment availability, facility compliance — biomedical, fire safety"},
            {cat:"Outcome Audit",icon:"📊",desc:"Patient outcomes — mortality rate, readmission rate, complication rates, patient satisfaction"},
            {cat:"Financial Audit",icon:"💰",desc:"Billing accuracy, cost per procedure, insurance claim compliance, revenue leakage"},
            {cat:"Pharmacy Audit",icon:"💊",desc:"Prescription accuracy, drug storage, expiry management, HIGH alert medication compliance"},
          ].map(t=>(
            <div key={t.cat} style={{padding:"10px 12px",background:T.panel2,borderRadius:8,border:`1px solid ${T.border}`}}>
              <div style={{fontSize:11,fontWeight:700,color:T.white,marginBottom:3}}>{t.icon} {t.cat}</div>
              <div style={{fontSize:10,color:T.muted,lineHeight:1.5}}>{t.desc}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Common mistakes */}
      <div style={{background:T.panel,border:`1px solid ${T.red}30`,borderRadius:12,padding:"18px 20px"}}>
        <div style={{fontSize:9,letterSpacing:3,color:T.red,marginBottom:12}}>COMMON AUDIT MISTAKES TO AVOID</div>
        <div style={{display:"grid",gap:6}}>
          {[
            "Doing the audit but taking no corrective action — assessors will reject this",
            "Not defining the standard before collecting data — data becomes meaningless",
            "Sample size too small — 5 observations out of 500 is not valid",
            "Re-audit done too soon — changes need 3–6 months to embed before re-measurement",
            "Recording 100% compliance on every audit — assessors will question authenticity",
            "Audit done only once before assessment — shows no improvement trend",
            "Avoid applying the same methodology (e.g. PDCA) to every audit — use the approach that best fits the problem",
          ].map((m,i)=>(
            <div key={i} style={{display:"flex",gap:8,alignItems:"flex-start",padding:"7px 10px",background:T.redD,borderRadius:6}}>
              <span style={{color:T.red,fontSize:12,flexShrink:0}}>✗</span>
              <span style={{fontSize:10,color:T.text,lineHeight:1.5}}>{m}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );

  // ── MY AUDITS tab ──
  const MyAuditsTab=()=>(
    <div>
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:12,flexWrap:"wrap",gap:8}}>
        <div>
          <div style={{fontSize:13,fontWeight:700,color:T.white}}>My Hospital Audits</div>
          <div style={{fontSize:10,color:T.muted,marginTop:2}}>{customAudits.length} custom audit{customAudits.length!==1?"s":""} · Any type, any number · Your hospital's own audit programme</div>
        </div>
        <button onClick={()=>setShowCreateForm(p=>!p)} style={{padding:"7px 16px",borderRadius:8,background:T.goldD,border:`1px solid ${T.gold}`,color:T.goldL,fontSize:11,fontWeight:700,cursor:"pointer"}}>
          {showCreateForm?"✕ Cancel":"+ Create New Audit"}
        </button>
      </div>

      {/* Create form */}
      {showCreateForm&&(
        <div style={{background:T.panel,border:`1px solid ${T.gold}40`,borderRadius:12,padding:"18px 20px",marginBottom:14}}>
          <div style={{fontSize:11,fontWeight:700,color:T.gold,marginBottom:14,letterSpacing:1}}>📋 NEW AUDIT</div>
          <div style={{display:"grid",gap:10}}>
            <div>
              <div style={lbl}>AUDIT NAME *</div>
              <input value={createForm.name} onChange={e=>setCreateForm(f=>({...f,name:e.target.value}))} placeholder="e.g. Hand Hygiene Compliance Audit, OT Checklist Audit…" style={{...inp,width:"100%",boxSizing:"border-box"}}/>
            </div>
            <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
              <div>
                <div style={lbl}>CATEGORY</div>
                <select value={createForm.audit_category} onChange={e=>setCreateForm(f=>({...f,audit_category:e.target.value}))} style={{...inp,width:"100%"}}>
                  {AUDIT_CATEGORIES.map(c=><option key={c.value} value={c.value}>{c.label}</option>)}
                </select>
              </div>
              <div style={{display:"flex",alignItems:"flex-end",paddingBottom:4}}>
                <label style={{display:"flex",alignItems:"center",gap:6,fontSize:11,color:T.text,cursor:"pointer"}}>
                  <input type="checkbox" checked={createForm.is_core} onChange={e=>setCreateForm(f=>({...f,is_core:e.target.checked}))}/> Mark as CORE (critical audit)
                </label>
              </div>
            </div>

            {/* Parameters */}
            <div>
              <div style={lbl}>CHECKLIST PARAMETERS (optional — add items to check during audit)</div>
              {createForm.parameters.map((p,i)=>(
                <div key={i} style={{display:"flex",gap:6,marginBottom:5,alignItems:"center"}}>
                  <input value={p} onChange={e=>{const ps=[...createForm.parameters];ps[i]=e.target.value;setCreateForm(f=>({...f,parameters:ps}));}} style={{...inp,flex:1}} placeholder={`Parameter ${i+1}`}/>
                  <button onClick={()=>setCreateForm(f=>({...f,parameters:f.parameters.filter((_,j)=>j!==i)}))} style={{padding:"4px 9px",borderRadius:5,background:"transparent",border:`1px solid ${T.red}40`,color:T.red,fontSize:11,cursor:"pointer"}}>✕</button>
                </div>
              ))}
              <div style={{display:"flex",gap:6,marginTop:4}}>
                <input value={newParam} onChange={e=>setNewParam(e.target.value)} onKeyDown={e=>{if(e.key==="Enter"&&newParam.trim()){setCreateForm(f=>({...f,parameters:[...f.parameters,newParam.trim()]}));setNewParam("");}}} placeholder="Type parameter and press Enter…" style={{...inp,flex:1}}/>
                <button onClick={()=>{if(newParam.trim()){setCreateForm(f=>({...f,parameters:[...f.parameters,newParam.trim()]}));setNewParam("");}}} style={{padding:"4px 12px",borderRadius:6,background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,fontSize:10,cursor:"pointer"}}>+ Add</button>
              </div>
              <div style={{fontSize:9,color:T.muted,marginTop:4}}>Parameters become checkboxes during audit recording. Leave empty if you prefer free-text findings only.</div>
            </div>

            <button onClick={createCustomAudit} disabled={savingCreate||!createForm.name.trim()} style={{padding:"9px 20px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:12,fontWeight:700,cursor:"pointer",opacity:savingCreate||!createForm.name.trim()?0.5:1,marginTop:4}}>
              {savingCreate?"Creating…":"✓ Create Audit"}
            </button>
          </div>
        </div>
      )}

      {customAudits.length===0&&!showCreateForm&&(
        <div style={{textAlign:"center",padding:"40px 20px",color:T.muted}}>
          <div style={{fontSize:32,marginBottom:12}}>📋</div>
          <div style={{fontSize:13,color:T.text,marginBottom:6}}>No custom audits yet</div>
          <div style={{fontSize:11,lineHeight:1.6}}>Create your hospital's own audit programme. You can add clinical, nursing, financial, structural — any type of audit relevant to your hospital.</div>
        </div>
      )}

      <div style={{display:"grid",gap:8}}>
        {customAudits.map(a=>{
          const isOpen=customExpanded===a.id;
          const params=Array.isArray(a.parameters)?a.parameters:JSON.parse(a.parameters||"[]");
          const records=getCustomRecords(a.id);
          const hasRecentRecord=records.some(r=>new Date(r.audit_date)>new Date(Date.now()-365*24*60*60*1000));
          const catLabel=AUDIT_CATEGORIES.find(c=>c.value===a.audit_category)?.label||a.audit_category;
          const avgCompliance=records.length>0?Math.round(records.filter(r=>r.sample_size>0).reduce((sum,r)=>sum+(r.compliant_count/r.sample_size)*100,0)/Math.max(1,records.filter(r=>r.sample_size>0).length)):null;

          return (
            <div key={a.id} style={{background:T.panel,border:`1px solid ${a.is_core?`${T.red}30`:T.border}`,borderRadius:10,overflow:"hidden"}}>
              {deleteConfirm===a.id&&(
                <div style={{background:T.redD,padding:"10px 16px",display:"flex",gap:10,alignItems:"center",justifyContent:"space-between"}}>
                  <span style={{fontSize:11,color:T.red}}>Delete "{a.name}" and all its records?</span>
                  <div style={{display:"flex",gap:6}}>
                    <button onClick={()=>deleteCustomAudit(a.id)} style={{padding:"4px 12px",borderRadius:6,background:T.red,border:"none",color:"#fff",fontSize:11,cursor:"pointer"}}>Delete</button>
                    <button onClick={()=>setDeleteConfirm(null)} style={{padding:"4px 12px",borderRadius:6,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:11,cursor:"pointer"}}>Cancel</button>
                  </div>
                </div>
              )}
              <div style={{padding:"12px 16px",cursor:"pointer"}} onClick={()=>setCustomExpanded(isOpen?null:a.id)}>
                <div style={{display:"flex",gap:10,alignItems:"flex-start"}}>
                  <div style={{width:44,height:44,borderRadius:8,background:a.is_core?T.redD:T.goldD,border:`1px solid ${a.is_core?T.red:T.gold}30`,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0,fontSize:20}}>
                    {AUDIT_CATEGORIES.find(c=>c.value===a.audit_category)?.label.split(" ")[0]||"📋"}
                  </div>
                  <div style={{flex:1}}>
                    <div style={{display:"flex",gap:8,alignItems:"center",marginBottom:4,flexWrap:"wrap"}}>
                      <span style={{fontSize:12,fontWeight:700,color:T.white}}>{a.name}</span>
                      {a.is_core&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:`${T.red}20`,color:T.red}}>CORE</span>}
                      {hasRecentRecord?<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.greenD,color:T.green}}>✓ {records.length} record{records.length!==1?"s":""}</span>
                        :<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.redD,color:T.red}}>No records</span>}
                      {customRecordSuccess===a.id&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.greenD,color:T.green}}>✅ Saved!</span>}
                    </div>
                    <div style={{display:"flex",gap:10,flexWrap:"wrap"}}>
                      <span style={{fontSize:10,color:T.muted}}>{catLabel}</span>
                      {params.length>0&&<span style={{fontSize:10,color:T.muted}}>📝 {params.length} parameters</span>}
                      {avgCompliance!==null&&<span style={{fontSize:10,color:avgCompliance>=80?T.green:avgCompliance>=60?T.orange:T.red,fontWeight:700}}>Avg: {avgCompliance}%</span>}
                    </div>
                  </div>
                  <div style={{display:"flex",gap:5,alignItems:"center"}}>
                    <button onClick={e=>{e.stopPropagation();setShowCustomRecord(a.id);setCustomRecordForm({status:"completed"});}} style={{padding:"4px 10px",borderRadius:6,fontSize:9,cursor:"pointer",background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold}}>+ Record</button>
                    <button onClick={e=>{e.stopPropagation();setDeleteConfirm(a.id);}} style={{padding:"4px 8px",borderRadius:6,fontSize:9,cursor:"pointer",background:"transparent",border:`1px solid ${T.red}30`,color:T.red}}>🗑</button>
                    <span style={{fontSize:14,color:T.muted}}>{isOpen?"▲":"▼"}</span>
                  </div>
                </div>
              </div>

              {/* Record form */}
              {showCustomRecord===a.id&&(
                <div style={{borderTop:`1px solid ${T.gold}40`,padding:"16px",background:T.panel2}}>
                  <div style={{fontSize:11,fontWeight:700,color:T.gold,marginBottom:12,letterSpacing:1}}>📋 RECORD AUDIT — {a.name}</div>
                  <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                    {[["Audit Date *","date","audit_date"],["Auditor Name","text","auditor_name"],["Department","text","department"]].map(([l,t,k])=>(
                      <div key={k}><div style={lbl}>{l}</div><input type={t} value={customRecordForm[k]||""} onChange={e=>setCustomRecordForm(f=>({...f,[k]:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                    ))}
                    <div>
                      <div style={lbl}>STATUS</div>
                      <select value={customRecordForm.status||"completed"} onChange={e=>setCustomRecordForm(f=>({...f,status:e.target.value}))} style={{...inp,width:"100%"}}>
                        <option value="completed">Completed</option>
                        <option value="planned">Planned</option>
                        <option value="missed">Missed</option>
                      </select>
                    </div>
                  </div>

                  {/* Checklist parameters */}
                  {params.length>0&&(
                    <div style={{marginBottom:12}}>
                      <div style={{fontSize:10,fontWeight:700,color:T.gold,marginBottom:8,letterSpacing:1}}>CHECKLIST — TICK COMPLIANT ITEMS</div>
                      <div style={{display:"grid",gap:5}}>
                        {params.map((p,i)=>{
                          const isDone=customRecordForm[`param_${i}`];
                          return(
                            <div key={i} onClick={()=>setCustomRecordForm(f=>({...f,[`param_${i}`]:!f[`param_${i}`]}))}
                              style={{display:"flex",gap:10,alignItems:"center",padding:"8px 12px",background:isDone?T.greenD:T.panel,border:`1px solid ${isDone?T.green:T.border}30`,borderRadius:7,cursor:"pointer"}}>
                              <div style={{width:16,height:16,borderRadius:3,border:`2px solid ${isDone?T.green:T.muted}`,background:isDone?T.green:"transparent",display:"flex",alignItems:"center",justifyContent:"center",fontSize:9,color:T.bg,flexShrink:0}}>{isDone?"✓":""}</div>
                              <span style={{fontSize:11,color:isDone?T.green:T.text}}>{p}</span>
                            </div>
                          );
                        })}
                      </div>
                      <div style={{fontSize:10,color:T.muted,marginTop:6}}>
                        Compliant: {params.filter((_,i)=>customRecordForm[`param_${i}`]).length}/{params.length}
                        {params.length>0&&<span style={{marginLeft:8,fontWeight:700,color:Math.round(params.filter((_,i)=>customRecordForm[`param_${i}`]).length/params.length*100)>=80?T.green:T.orange}}>
                          ({Math.round(params.filter((_,i)=>customRecordForm[`param_${i}`]).length/params.length*100)}%)
                        </span>}
                      </div>
                    </div>
                  )}

                  {params.length===0&&(
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                      <div><div style={lbl}>SAMPLE SIZE</div><input type="number" value={customRecordForm.sample_size||""} onChange={e=>setCustomRecordForm(f=>({...f,sample_size:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                      <div><div style={lbl}>COMPLIANT COUNT</div><input type="number" value={customRecordForm.compliant_count||""} onChange={e=>setCustomRecordForm(f=>({...f,compliant_count:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                    </div>
                  )}

                  <div style={{marginBottom:10}}><div style={lbl}>FINDINGS</div><textarea value={customRecordForm.findings||""} onChange={e=>setCustomRecordForm(f=>({...f,findings:e.target.value}))} rows={2} placeholder="Key findings from this audit…" style={{...inp,width:"100%",resize:"vertical",boxSizing:"border-box"}}/></div>

                  <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:10}}>
                    <label style={{display:"flex",alignItems:"center",gap:6,fontSize:11,color:T.text,cursor:"pointer"}}>
                      <input type="checkbox" checked={customRecordForm.capa_raised||false} onChange={e=>setCustomRecordForm(f=>({...f,capa_raised:e.target.checked}))}/> CAPA Required
                    </label>
                  </div>

                  {customRecordForm.capa_raised&&(
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                      <div><div style={lbl}>CAPA NOTES</div><input value={customRecordForm.capa_notes||""} onChange={e=>setCustomRecordForm(f=>({...f,capa_notes:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                      <div><div style={lbl}>TARGET DATE</div><input type="date" value={customRecordForm.capa_target_date||""} onChange={e=>setCustomRecordForm(f=>({...f,capa_target_date:e.target.value}))} style={{...inp,width:"100%"}}/></div>
                      <div><div style={lbl}>RE-AUDIT DATE</div><input type="date" value={customRecordForm.reaudit_date||""} onChange={e=>setCustomRecordForm(f=>({...f,reaudit_date:e.target.value}))} style={{...inp,width:"100%"}}/></div>
                    </div>
                  )}

                  <div style={{display:"flex",gap:8}}>
                    <button onClick={()=>saveCustomRecord(a)} disabled={savingCustomRecord} style={{padding:"8px 20px",borderRadius:8,background:T.green,border:"none",color:T.bg,fontSize:11,fontWeight:700,cursor:"pointer"}}>{savingCustomRecord?"Saving…":"💾 Save Record"}</button>
                    <button onClick={()=>{setShowCustomRecord(null);setCustomRecordForm({});}} style={{padding:"8px 16px",borderRadius:8,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:11,cursor:"pointer"}}>Cancel</button>
                  </div>
                </div>
              )}

              {/* Expanded detail */}
              {isOpen&&(
                <div style={{borderTop:`1px solid ${T.border}`,padding:"14px 16px"}}>
                  {params.length>0&&(
                    <div style={{marginBottom:12}}>
                      <div style={{fontSize:9,color:T.muted,marginBottom:6,letterSpacing:1}}>CHECKLIST PARAMETERS ({params.length})</div>
                      <div style={{display:"flex",gap:5,flexWrap:"wrap"}}>
                        {params.map((p,i)=><span key={i} style={{fontSize:10,padding:"3px 9px",borderRadius:6,background:T.panel2,border:`1px solid ${T.border}`,color:T.text}}>📌 {p}</span>)}
                      </div>
                    </div>
                  )}
                  {records.length>0&&(
                    <div>
                      <div style={{fontSize:9,color:T.muted,marginBottom:6,letterSpacing:1}}>AUDIT RECORDS ({records.length})</div>
                      {records.map(r=>{
                        const compPct=r.sample_size>0?Math.round((r.compliant_count/r.sample_size)*100):null;
                        return(
                          <div key={r.id} style={{background:T.panel2,borderRadius:8,padding:"10px 12px",marginBottom:6,border:`1px solid ${compPct!==null?(compPct>=80?`${T.green}20`:`${T.orange}20`):T.border}`}}>
                            <div style={{display:"flex",justifyContent:"space-between",alignItems:"flex-start"}}>
                              <div>
                                <div style={{fontSize:11,fontWeight:700,color:T.white}}>{r.audit_date}</div>
                                <div style={{fontSize:10,color:T.muted,marginTop:2}}>{r.auditor_name&&`Auditor: ${r.auditor_name}`}{r.department&&` · ${r.department}`}</div>
                                {compPct!==null&&<div style={{fontSize:11,fontWeight:700,color:compPct>=80?T.green:T.orange,marginTop:3}}>Compliance: {compPct}% ({r.compliant_count}/{r.sample_size})</div>}
                                {r.findings&&<div style={{fontSize:9,color:T.text,marginTop:3,lineHeight:1.4}}>{r.findings}</div>}
                                {r.capa_raised&&<div style={{fontSize:9,color:T.orange,marginTop:2}}>⚠️ CAPA: {r.capa_notes} — Due: {r.capa_target_date||"—"}</div>}
                              </div>
                              <button onClick={()=>deleteCustomRecord(r.id)} style={{fontSize:9,color:T.red,background:"transparent",border:`1px solid ${T.red}30`,borderRadius:4,padding:"2px 7px",cursor:"pointer"}}>Delete</button>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  )}
                  {records.length===0&&<div style={{fontSize:11,color:T.muted,textAlign:"center",padding:"16px 0"}}>No records yet. Click "+ Record" to log your first audit.</div>}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );

  return (
    <div>
      {/* Main tab bar */}
      <div style={{display:"flex",gap:6,marginBottom:14,borderBottom:`1px solid ${T.border}`,paddingBottom:10}}>
        {[
          {id:"nabh",label:"📋 NABH Audits",count:audits.length},
          {id:"mine",label:"➕ My Audits",count:customAudits.length},
          {id:"learn",label:"📖 What is Audit?"},
        ].map(t=>(
          <button key={t.id} onClick={()=>setMainTab(t.id)}
            style={{padding:"7px 16px",borderRadius:8,fontSize:11,fontWeight:600,cursor:"pointer",
              background:mainTab===t.id?T.goldD:"transparent",
              border:`1px solid ${mainTab===t.id?T.gold:T.border}`,
              color:mainTab===t.id?T.goldL:T.muted}}>
            {t.label}{t.count!==undefined&&<span style={{marginLeft:5,fontSize:9,opacity:0.7}}>({t.count})</span>}
          </button>
        ))}
      </div>

      {mainTab==="learn"&&<LearnTab/>}
      {mainTab==="mine"&&<MyAuditsTab/>}

      {mainTab==="nabh"&&(
        <div>
          {/* Summary — fixed framing */}
          <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:14}}>
            <div style={{display:"flex",gap:16,alignItems:"center",flexWrap:"wrap"}}>
              <div style={{flex:1}}>
                <div style={{fontSize:9,color:T.muted,marginBottom:3,letterSpacing:1}}>NABH AUDIT PROGRAMME — LAST 12 MONTHS</div>
                <div style={{fontSize:12,color:completedAudits>0?T.green:T.orange,fontWeight:700}}>
                  {completedAudits} of {totalAudits} NABH audits have records in last 12 months
                </div>
                <div style={{fontSize:10,color:T.muted,marginTop:3}}>NABH has no fixed minimum number — focus on completing the full audit cycle for each audit conducted.</div>
                <div style={{height:4,background:T.border,borderRadius:2,marginTop:6}}>
                  <div style={{height:"100%",borderRadius:2,background:completedAudits>0?T.green:T.orange,width:`${Math.min(100,(completedAudits/Math.max(totalAudits,1))*100)}%`,transition:"width 0.5s"}}/>
                </div>
              </div>
              <div style={{textAlign:"right"}}>
                <div style={{fontSize:20,fontWeight:700,color:T.gold}}>{completedAudits}/{totalAudits}</div>
                <div style={{fontSize:9,color:T.muted}}>With records</div>
              </div>
            </div>
          </div>

          {/* Category tabs */}
          <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"10px 14px",marginBottom:6,display:"flex",gap:8,flexWrap:"wrap"}}>
            {[["ALL","📋 All Categories"],["clinical","🏥 Clinical Audit"],["nursing","💉 Nursing Audit"],["qip","🎯 Quality Improvement Project"]].map(([f,l])=>(
              <button key={f} onClick={()=>setCatFilter(f)} style={{padding:"5px 14px",borderRadius:8,fontSize:10,cursor:"pointer",background:catFilter===f?T.goldD:"transparent",border:`1px solid ${catFilter===f?T.gold:T.border}`,color:catFilter===f?T.goldL:T.muted}}>{l}
                {f!=="ALL"&&<span style={{marginLeft:4,fontSize:9,color:catFilter===f?T.gold:T.muted}}>({audits.filter(a=>(a.audit_category||"clinical")===f).length})</span>}
              </button>
            ))}
          </div>
          {catFilter==="qip"&&(
            <div style={{background:T.goldD,border:`1px solid ${T.gold}40`,borderRadius:8,padding:"8px 14px",marginBottom:8,fontSize:10,color:T.goldL}}>
              ⭐ <b>NABH Mandatory:</b> Minimum 2 Quality Improvement Projects per year. Each QIP must be presented to the Quality Management Committee.
            </div>
          )}
          <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"10px 14px",marginBottom:14,display:"flex",gap:8}}>
            {[["ALL",`All (${filtered.length})`],["CORE",`🔴 CORE (${filtered.filter(a=>a.is_core).length})`],["NON_CORE",`🟡 Non-CORE (${filtered.filter(a=>!a.is_core).length})`]].map(([f,l])=>(
              <button key={f} onClick={()=>setFilter(f)} style={{padding:"5px 14px",borderRadius:8,fontSize:10,cursor:"pointer",background:filter===f?T.goldD:"transparent",border:`1px solid ${filter===f?T.gold:T.border}`,color:filter===f?T.goldL:T.muted}}>{l}</button>
            ))}
          </div>

          <div style={{display:"grid",gap:8}}>
            {filtered.map(a=>{
              const isOpen=expanded===a.id;
              const params=Array.isArray(a.parameters)?a.parameters:JSON.parse(a.parameters||"[]");
              const doneCount=params.filter((_,i)=>checked[`${a.id}-${i}`]).length;
              const records=getRecords(a.id);
              const hasRecentRecord=records.some(r=>new Date(r.audit_date)>new Date(Date.now()-365*24*60*60*1000));
              const compPctAvg=records.length>0?Math.round(records.filter(r=>r.sample_size>0).reduce((sum,r)=>sum+(r.compliant_count/r.sample_size)*100,0)/Math.max(1,records.filter(r=>r.sample_size>0).length)):null;
              return (
                <div key={a.id} style={{background:T.panel,border:`1px solid ${a.is_core?`${T.red}30`:T.border}`,borderRadius:10,overflow:"hidden"}}>
                  <div style={{padding:"12px 16px",cursor:"pointer"}} onClick={()=>setExpanded(isOpen?null:a.id)}>
                    <div style={{display:"flex",gap:10,alignItems:"flex-start"}}>
                      <div style={{width:44,height:44,borderRadius:8,background:a.is_core?T.redD:T.goldD,border:`1px solid ${a.is_core?T.red:T.gold}30`,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0,flexDirection:"column"}}>
                        <span style={{fontSize:9,fontWeight:800,color:a.is_core?T.red:T.gold}}>{a.audit_code}</span>
                        {a.is_core&&<span style={{fontSize:7,color:T.red}}>CORE</span>}
                      </div>
                      <div style={{flex:1}}>
                        <div style={{display:"flex",gap:8,alignItems:"center",marginBottom:4,flexWrap:"wrap"}}>
                          <span style={{fontSize:12,fontWeight:700,color:T.white}}>{a.name}</span>
                          {a.is_core&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:`${T.red}20`,color:T.red}}>CORE</span>}
                          {hasRecentRecord?<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.greenD,color:T.green}}>✓ {records.length} record{records.length>1?"s":""}</span>
                            :<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.redD,color:T.red}}>No records</span>}
                          {recordSuccess===a.id&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.greenD,color:T.green}}>✅ Saved!</span>}
                          {compPctAvg!==null&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:compPctAvg>=80?T.greenD:T.orangeD,color:compPctAvg>=80?T.green:T.orange,fontWeight:700}}>Avg {compPctAvg}%</span>}
                        </div>
                        <div style={{display:"flex",gap:10,flexWrap:"wrap"}}>
                          <span style={{fontSize:10,color:T.muted}}>📋 {a.nabh_ref}</span>
                          <span style={{fontSize:10,color:T.muted}}>📅 {a.frequency}</span>
                          <span style={{fontSize:10,color:T.muted}}>👤 {a.who_does_it}</span>
                        </div>
                      </div>
                      {doneCount>0&&<span style={{fontSize:10,color:T.green,flexShrink:0}}>{doneCount}/{params.length} ✓</span>}
                      <button onClick={e=>{e.stopPropagation();setShowRecordForm(a.id);setRecordForm(emptyRecord());}} style={{padding:"4px 10px",borderRadius:6,fontSize:9,cursor:"pointer",background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,flexShrink:0}}>+ Record Audit</button>
                      <span style={{fontSize:14,color:T.muted}}>{isOpen?"▲":"▼"}</span>
                    </div>
                  </div>

                  {showRecordForm===a.id&&(
                    <div style={{borderTop:`1px solid ${T.gold}40`,padding:"16px",background:T.panel2}}>
                      <div style={{fontSize:11,fontWeight:700,color:T.gold,marginBottom:12,letterSpacing:1}}>📋 RECORD AUDIT — {a.name}</div>
                      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                        {[["Audit Date *","date","audit_date"],["Auditor Name","text","auditor_name"],["Department","text","department"],["Status","select","status"]].map(([l,t,k])=>(
                          <div key={k}><div style={lbl}>{l}</div>
                            {t==="select"?<select value={recordForm[k]} onChange={e=>setRecordForm(f=>({...f,[k]:e.target.value}))} style={{...inp,width:"100%"}}>
                              <option value="completed">Completed</option><option value="planned">Planned</option><option value="missed">Missed</option>
                            </select>:<input type={t} value={recordForm[k]} onChange={e=>setRecordForm(f=>({...f,[k]:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/>}
                          </div>
                        ))}
                        <div><div style={lbl}>SAMPLE SIZE</div><input type="number" value={recordForm.sample_size} onChange={e=>setRecordForm(f=>({...f,sample_size:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                        <div><div style={lbl}>COMPLIANT COUNT</div><input type="number" value={recordForm.compliant_count} onChange={e=>setRecordForm(f=>({...f,compliant_count:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                      </div>
                      <div style={{marginBottom:10}}><div style={lbl}>FINDINGS</div><textarea value={recordForm.findings} onChange={e=>setRecordForm(f=>({...f,findings:e.target.value}))} rows={2} style={{...inp,width:"100%",resize:"vertical",boxSizing:"border-box"}}/></div>
                      <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:10}}>
                        <label style={{display:"flex",alignItems:"center",gap:6,fontSize:11,color:T.text,cursor:"pointer"}}>
                          <input type="checkbox" checked={recordForm.capa_raised} onChange={e=>setRecordForm(f=>({...f,capa_raised:e.target.checked}))}/> CAPA Required
                        </label>
                      </div>
                      {recordForm.capa_raised&&(
                        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                          <div><div style={lbl}>CAPA NOTES</div><input value={recordForm.capa_notes} onChange={e=>setRecordForm(f=>({...f,capa_notes:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                          <div><div style={lbl}>TARGET DATE</div><input type="date" value={recordForm.capa_target_date} onChange={e=>setRecordForm(f=>({...f,capa_target_date:e.target.value}))} style={{...inp,width:"100%"}}/></div>
                          <div><div style={lbl}>RE-AUDIT DATE</div><input type="date" value={recordForm.reaudit_date} onChange={e=>setRecordForm(f=>({...f,reaudit_date:e.target.value}))} style={{...inp,width:"100%"}}/></div>
                        </div>
                      )}
                      <div style={{display:"flex",gap:8}}>
                        <button onClick={()=>saveRecord(a.id)} disabled={saving} style={{padding:"8px 20px",borderRadius:8,background:T.green,border:"none",color:T.bg,fontSize:11,fontWeight:700,cursor:"pointer"}}>{saving?"Saving…":"💾 Save Record"}</button>
                        <button onClick={()=>{setShowRecordForm(null);setRecordForm(emptyRecord());}} style={{padding:"8px 16px",borderRadius:8,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:11,cursor:"pointer"}}>Cancel</button>
                      </div>
                    </div>
                  )}

                  {isOpen&&(
                    <div style={{borderTop:`1px solid ${T.border}`,padding:"14px 16px",display:"grid",gap:12}}>
                      {records.length>0&&(
                        <div>
                          <AuditComplianceChart records={records}/>
                          <div style={{fontSize:9,color:T.muted,marginBottom:6,letterSpacing:1,marginTop:12}}>AUDIT RECORDS ({records.length})</div>
                          {records.map(r=>{
                            const rPct=r.sample_size>0?Math.round((r.compliant_count/r.sample_size)*100):null;
                            return(
                              <div key={r.id} style={{background:T.panel2,borderRadius:8,padding:"10px 12px",marginBottom:6,border:`1px solid ${rPct!==null?(rPct>=80?`${T.green}20`:`${T.orange}20`):T.border}`}}>
                                <div style={{display:"flex",justifyContent:"space-between",alignItems:"flex-start"}}>
                                  <div>
                                    <div style={{fontSize:11,fontWeight:700,color:T.white}}>{r.audit_date}</div>
                                    <div style={{fontSize:10,color:T.muted,marginTop:2}}>{r.auditor_name&&`Auditor: ${r.auditor_name}`}{r.department&&` · ${r.department}`}</div>
                                    {rPct!==null&&<div style={{fontSize:11,fontWeight:700,color:rPct>=80?T.green:T.orange,marginTop:3}}>Compliance: {rPct}% ({r.compliant_count}/{r.sample_size})</div>}
                                    {r.findings&&<div style={{fontSize:9,color:T.text,marginTop:3,lineHeight:1.4}}>{r.findings}</div>}
                                    {r.capa_raised&&<div style={{fontSize:9,color:T.orange,marginTop:2}}>⚠️ CAPA: {r.capa_notes} — Due: {r.capa_target_date||"—"}</div>}
                                  </div>
                                  <button onClick={()=>deleteRecord(r.id)} style={{fontSize:9,color:T.red,background:"transparent",border:`1px solid ${T.red}30`,borderRadius:4,padding:"2px 7px",cursor:"pointer"}}>Delete</button>
                                </div>
                              </div>
                            );
                          })}
                        </div>
                      )}
                      {a.conduct_guide&&(()=>{
                        const cg=typeof a.conduct_guide==="string"?JSON.parse(a.conduct_guide):a.conduct_guide;
                        const isGuideOpen=guideOpen===a.id;
                        return (
                          <div style={{borderTop:`1px dashed ${T.border}`,paddingTop:10,marginTop:2}}>
                            <div onClick={()=>setGuideOpen(isGuideOpen?null:a.id)} style={{cursor:"pointer",display:"flex",alignItems:"center",gap:6,fontSize:10,color:T.gold,letterSpacing:1,fontWeight:700}}>
                              <span>{isGuideOpen?"▲":"▼"}</span><span>📖 HOW TO CONDUCT THIS AUDIT</span>
                            </div>
                            {isGuideOpen&&(
                              <div style={{display:"grid",gap:10,marginTop:10,padding:"12px 14px",background:T.panel2,borderRadius:8,border:`1px solid ${T.gold}20`}}>
                                {Array.isArray(cg.preparation)&&cg.preparation.length>0&&(
                                  <div><div style={{fontSize:9,color:T.gold,marginBottom:6,letterSpacing:1,fontWeight:700}}>PREPARATION</div>
                                    <div style={{display:"grid",gap:4}}>{cg.preparation.map((step,i)=>(
                                      <div key={i} style={{display:"flex",gap:8,padding:"6px 9px",background:T.panel,borderRadius:5,border:`1px solid ${T.border}`}}>
                                        <span style={{fontSize:9,color:T.gold,fontWeight:700,minWidth:14}}>{i+1}.</span>
                                        <span style={{fontSize:10,color:T.text,lineHeight:1.5}}>{step}</span>
                                      </div>
                                    ))}</div>
                                  </div>
                                )}
                                {Array.isArray(cg.execution_steps)&&cg.execution_steps.length>0&&(
                                  <div><div style={{fontSize:9,color:T.gold,marginBottom:6,letterSpacing:1,fontWeight:700}}>EXECUTION</div>
                                    <div style={{display:"grid",gap:5}}>{cg.execution_steps.map((step,i)=>(
                                      <div key={i} style={{padding:"7px 10px",background:T.panel,borderRadius:5,borderLeft:`3px solid ${T.gold}`,fontSize:10,color:T.text,lineHeight:1.55}}>{step}</div>
                                    ))}</div>
                                  </div>
                                )}
                                {cg.sample_size_calculation&&<div style={{padding:"10px 12px",background:T.blueD,borderRadius:6}}><div style={{fontSize:9,color:T.blue,marginBottom:4,fontWeight:700}}>📊 SAMPLE SIZE</div><div style={{fontSize:10,color:T.text}}>{cg.sample_size_calculation}</div></div>}
                                {cg.reporting_template&&<div style={{padding:"10px 12px",background:T.greenD,borderRadius:6}}><div style={{fontSize:9,color:T.green,marginBottom:4,fontWeight:700}}>📄 REPORTING</div><div style={{fontSize:10,color:T.text}}>{cg.reporting_template}</div></div>}
                                {cg.re_audit_timeline&&<div style={{padding:"10px 12px",background:T.orangeD,borderRadius:6}}><div style={{fontSize:9,color:T.orange,marginBottom:4,fontWeight:700}}>🔁 RE-AUDIT</div><div style={{fontSize:10,color:T.text}}>{cg.re_audit_timeline}</div></div>}
                              </div>
                            )}
                          </div>
                        );
                      })()}
                    </div>
                  )}
                </div>
              );
            })}
            {filtered.length===0&&<div style={{textAlign:"center",color:T.muted,padding:30,fontSize:12}}>No audits match this filter.</div>}
          </div>
        </div>
      )}
    </div>
  );
}

// ── CHECKLISTS ────────────────────────────────────────
function ChecklistsScreen() {
  const [checklists,setChecklists]=useState([]); const [loading,setLoading]=useState(true);
  const [selected,setSelected]=useState(null); const [checked,setChecked]=useState({});
  useEffect(()=>{
    supabase.from("department_checklists").select("*").order("dept").then(({data})=>{
      setChecklists(data||[]);if(data&&data.length>0)setSelected(data[0]);setLoading(false);
    });
  },[]);
  const items=selected?(Array.isArray(selected.items)?selected.items:JSON.parse(selected.items||"[]")):[];
  const doneCount=items.filter((_,i)=>checked[`${selected?.id}-${i}`]).length;
  const pct=items.length>0?Math.round(doneCount/items.length*100):0;
  if(loading) return <div style={{textAlign:"center",color:T.muted,padding:40}}>Loading checklists…</div>;
  return (
    <div style={{display:"grid",gridTemplateColumns:"210px 1fr",gap:12,alignItems:"start"}}>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:8}}>
        <div style={{fontSize:9,letterSpacing:2,color:T.muted,padding:"5px 8px",marginBottom:4}}>DEPARTMENTS</div>
        {checklists.map(c=>(
          <button key={c.id} onClick={()=>setSelected(c)} style={{width:"100%",textAlign:"left",padding:"7px 10px",borderRadius:7,marginBottom:3,cursor:"pointer",background:selected?.id===c.id?T.goldD:"transparent",border:`1px solid ${selected?.id===c.id?T.gold:T.border}`,color:selected?.id===c.id?T.goldL:T.text,fontSize:11,display:"flex",gap:6,alignItems:"center"}}>
            <span>{c.icon||"📋"}</span><span style={{flex:1}}>{c.dept}</span>
          </button>
        ))}
      </div>
      {selected&&(
        <div>
          <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"14px 16px",marginBottom:10}}>
            <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:8}}>
              <div>
                <div style={{fontSize:14,fontWeight:700,color:T.white}}>{selected.icon} {selected.dept}</div>
                <div style={{fontSize:10,color:T.muted,marginTop:2}}>NABH: {selected.nabh_chapter} · {items.length} items</div>
              </div>
              <div style={{textAlign:"center"}}>
                <div style={{fontSize:22,fontWeight:800,color:pct===100?T.green:pct>50?T.gold:T.red}}>{pct}%</div>
                <div style={{fontSize:8,color:T.muted}}>{doneCount}/{items.length}</div>
              </div>
            </div>
            <div style={{height:4,background:T.border,borderRadius:2}}><div style={{width:`${pct}%`,height:"100%",background:pct===100?T.green:pct>50?T.gold:T.red,borderRadius:2,transition:"width 0.3s"}}/></div>
          </div>
          <div style={{display:"grid",gap:5}}>
            {items.map((item,i)=>{
              const key=`${selected.id}-${i}`; const done=checked[key];
              return (
                <div key={i} onClick={()=>setChecked(p=>({...p,[key]:!done}))}
                  style={{background:T.panel,border:`1px solid ${done?`${T.green}40`:T.border}`,borderRadius:8,padding:"9px 13px",cursor:"pointer",display:"flex",gap:10,alignItems:"flex-start",opacity:done?0.7:1}}>
                  <div style={{width:17,height:17,borderRadius:4,border:`2px solid ${done?T.green:T.muted}`,background:done?T.green:"transparent",flexShrink:0,display:"flex",alignItems:"center",justifyContent:"center",fontSize:10,color:T.bg,marginTop:1}}>{done?"✓":""}</div>
                  <div style={{flex:1}}>
                    <div style={{fontSize:11,color:done?T.muted:T.text,textDecoration:done?"line-through":"none",lineHeight:1.5}}>{item.t}</div>
                    <div style={{fontSize:9,color:T.muted,marginTop:2}}>Ref: {item.ref}</div>
                  </div>
                </div>
              );
            })}
          </div>
          {pct===100&&<div style={{background:T.greenD,border:`1px solid ${T.green}40`,borderRadius:10,padding:"12px 16px",marginTop:10,textAlign:"center"}}><div style={{fontSize:13,color:T.green,fontWeight:700}}>✅ All items verified for {selected.dept}</div></div>}
        </div>
      )}
    </div>
  );
}

// ── PROFILE ──────────────────────────────────────────
function ProfileScreen({ user, context, onContextUpdate }) {
  const [hospitalName,setHospitalName]=useState(context?.hospitalName||"");
  const [displayName,setDisplayName]=useState("");
  const [profile,setProfile]=useState(null);
  const [savingHospital,setSavingHospital]=useState(false);
  const [savingProfile,setSavingProfile]=useState(false);
  const [pwCurrent,setPwCurrent]=useState("");
  const [pwNew,setPwNew]=useState("");
  const [pwConfirm,setPwConfirm]=useState("");
  const [pwBusy,setPwBusy]=useState(false);
  const [toast,setToast]=useState(null);

  useEffect(()=>{
    if(!user)return;
    supabase.from("profiles").select("*").eq("id",user.id).single().then(({data})=>{
      if(data){setProfile(data);setDisplayName(data.name||"");}
    });
  },[user]);

  const showToast=(type,msg,sev="SUCCESS")=>{setToast({type,msg,sev});setTimeout(()=>setToast(null),3500);};

  const saveHospital=async()=>{
    if(!hospitalName.trim()){showToast("ERROR","Hospital name cannot be empty","CRITICAL");return;}
    if(!context?.hospitalId){showToast("ERROR","No hospital linked to this account","CRITICAL");return;}
    setSavingHospital(true);
    const{error}=await supabase.from("hospitals").update({name:hospitalName.trim()}).eq("id",context.hospitalId);
    setSavingHospital(false);
    if(error){showToast("ERROR",error.message,"CRITICAL");return;}
    if(onContextUpdate)onContextUpdate({...context,hospitalName:hospitalName.trim()});
    showToast("SAVED","Hospital name updated. Refresh to see it in the header.");
  };

  const saveProfile=async()=>{
    if(!user)return;
    setSavingProfile(true);
    const{error}=await supabase.from("profiles").upsert({id:user.id,name:displayName.trim()||null,hospital_id:context?.hospitalId,role:profile?.role||"admin"});
    setSavingProfile(false);
    if(error){showToast("ERROR",error.message,"CRITICAL");return;}
    showToast("SAVED","Display name updated.");
  };

  const changePassword=async()=>{
    if(!pwCurrent||!pwNew||!pwConfirm){showToast("ERROR","Fill all three password fields","CRITICAL");return;}
    if(pwNew.length<6){showToast("ERROR","New password must be at least 6 characters","CRITICAL");return;}
    if(pwNew!==pwConfirm){showToast("ERROR","New password and confirmation do not match","CRITICAL");return;}
    if(pwNew===pwCurrent){showToast("ERROR","New password must differ from current","CRITICAL");return;}
    setPwBusy(true);
    const{error}=await supabase.auth.updateUser({password:pwNew});
    setPwBusy(false);
    if(error){showToast("ERROR",error.message,"CRITICAL");return;}
    setPwCurrent("");setPwNew("");setPwConfirm("");
    showToast("SAVED","Password changed successfully. Use the new password next time you sign in.");
  };

  const memberSince=user?.created_at?new Date(user.created_at).toLocaleDateString("en-IN",{year:"numeric",month:"long",day:"numeric"}):"—";

  return (
    <div>
      {toast&&<div style={{position:"fixed",top:80,right:16,zIndex:999,maxWidth:360,background:toast.sev==="CRITICAL"?T.redD:T.greenD,border:`1px solid ${toast.sev==="CRITICAL"?T.red:T.green}50`,borderRadius:10,padding:"12px 16px",boxShadow:"0 8px 32px rgba(0,0,0,0.5)"}}>
        <div style={{fontSize:10,fontWeight:700,marginBottom:4,color:toast.sev==="CRITICAL"?T.red:T.green}}>{toast.sev==="CRITICAL"?"🚨":"✅"} {toast.type}</div>
        <div style={{fontSize:11,color:T.text,lineHeight:1.5}}>{toast.msg}</div>
      </div>}

      <div style={{display:"grid",gap:14}}>
        {/* Account info */}
        <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"16px 18px"}}>
          <div style={{display:"flex",gap:14,alignItems:"center",marginBottom:14}}>
            <div style={{width:48,height:48,borderRadius:"50%",background:`linear-gradient(135deg,${T.gold},#f0d070)`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:22,flexShrink:0}}>👤</div>
            <div style={{flex:1}}>
              <div style={{fontSize:9,letterSpacing:2,color:T.gold,marginBottom:2}}>ACCOUNT</div>
              <div style={{fontSize:14,fontWeight:700,color:T.white}}>{user?.email}</div>
            </div>
          </div>
          <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:14,fontSize:11}}>
            <div><div style={{fontSize:9,color:T.muted,marginBottom:3}}>MEMBER SINCE</div><div style={{color:T.text}}>{memberSince}</div></div>
            <div><div style={{fontSize:9,color:T.muted,marginBottom:3}}>ROLE</div><div style={{color:T.text}}>{profile?.role||"admin"}</div></div>
          </div>
        </div>

        {/* Hospital + Display name */}
        <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"16px 18px"}}>
          <div style={{fontSize:9,letterSpacing:2,color:T.gold,marginBottom:12}}>YOUR HOSPITAL & DISPLAY NAME</div>
          <div style={{display:"grid",gap:12}}>
            <div>
              <div style={{fontSize:9,color:T.muted,marginBottom:5}}>HOSPITAL NAME — shown in app header and reports</div>
              <div style={{display:"flex",gap:8}}>
                <input value={hospitalName} onChange={e=>setHospitalName(e.target.value)} placeholder="e.g., HMP Foundation, Ankleshwar" style={{flex:1,padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12}}/>
                <button onClick={saveHospital} disabled={savingHospital||hospitalName===context?.hospitalName} style={{padding:"7px 16px",borderRadius:8,border:`1px solid ${T.gold}40`,background:T.goldD,color:T.gold,fontSize:11,fontWeight:700,cursor:savingHospital||hospitalName===context?.hospitalName?"not-allowed":"pointer",opacity:savingHospital||hospitalName===context?.hospitalName?0.5:1}}>{savingHospital?"Saving…":"Save"}</button>
              </div>
            </div>
            <div>
              <div style={{fontSize:9,color:T.muted,marginBottom:5}}>YOUR DISPLAY NAME — optional, used in audit logs</div>
              <div style={{display:"flex",gap:8}}>
                <input value={displayName} onChange={e=>setDisplayName(e.target.value)} placeholder="e.g., Dr. Mehul Upadhyay" style={{flex:1,padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12}}/>
                <button onClick={saveProfile} disabled={savingProfile} style={{padding:"7px 16px",borderRadius:8,border:`1px solid ${T.gold}40`,background:T.goldD,color:T.gold,fontSize:11,fontWeight:700,cursor:savingProfile?"not-allowed":"pointer",opacity:savingProfile?0.5:1}}>{savingProfile?"Saving…":"Save"}</button>
              </div>
            </div>
          </div>
        </div>

        {/* Change password */}
        <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"16px 18px"}}>
          <div style={{fontSize:9,letterSpacing:2,color:T.gold,marginBottom:12}}>🔒 CHANGE PASSWORD</div>
          <div style={{display:"grid",gap:10}}>
            <div>
              <div style={{fontSize:9,color:T.muted,marginBottom:4}}>CURRENT PASSWORD</div>
              <input type="password" value={pwCurrent} onChange={e=>setPwCurrent(e.target.value)} autoComplete="current-password" style={{width:"100%",padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12}}/>
            </div>
            <div>
              <div style={{fontSize:9,color:T.muted,marginBottom:4}}>NEW PASSWORD (min 6 characters)</div>
              <input type="password" value={pwNew} onChange={e=>setPwNew(e.target.value)} autoComplete="new-password" style={{width:"100%",padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12}}/>
            </div>
            <div>
              <div style={{fontSize:9,color:T.muted,marginBottom:4}}>CONFIRM NEW PASSWORD</div>
              <input type="password" value={pwConfirm} onChange={e=>setPwConfirm(e.target.value)} autoComplete="new-password" style={{width:"100%",padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12}}/>
            </div>
            <button onClick={changePassword} disabled={pwBusy} style={{padding:"9px 16px",borderRadius:8,border:`1px solid ${T.gold}40`,background:T.goldD,color:T.gold,fontSize:11,fontWeight:700,cursor:pwBusy?"not-allowed":"pointer",opacity:pwBusy?0.5:1,marginTop:4}}>{pwBusy?"Updating…":"Update Password"}</button>
            <div style={{fontSize:9,color:T.muted,lineHeight:1.5,marginTop:2}}>You will stay signed in after change. Use the new password next time you sign in on any device.</div>
          </div>
        </div>

        {/* Sign out */}
        <div style={{background:T.panel,border:`1px solid ${T.red}30`,borderRadius:10,padding:"14px 18px",display:"flex",justifyContent:"space-between",alignItems:"center",gap:12,flexWrap:"wrap"}}>
          <div>
            <div style={{fontSize:11,fontWeight:700,color:T.red,marginBottom:3}}>Sign out</div>
            <div style={{fontSize:10,color:T.muted}}>End your current session on this device.</div>
          </div>
          <button onClick={()=>supabase.auth.signOut()} style={{padding:"7px 18px",borderRadius:8,border:`1px solid ${T.red}50`,background:T.redD,color:T.red,fontSize:11,fontWeight:700,cursor:"pointer"}}>Sign out</button>
        </div>
      </div>
    </div>
  );
}

// ── PASSWORD RECOVERY ──────────────────────────────────
function RecoveryScreen({ user, onDone }) {
  const [pwNew,setPwNew]=useState("");
  const [pwConfirm,setPwConfirm]=useState("");
  const [busy,setBusy]=useState(false);
  const [err,setErr]=useState("");
  const [done,setDone]=useState(false);

  const submit=async()=>{
    setErr("");
    if(!pwNew||!pwConfirm){setErr("Fill both password fields.");return;}
    if(pwNew.length<6){setErr("Password must be at least 6 characters.");return;}
    if(pwNew!==pwConfirm){setErr("Passwords do not match.");return;}
    setBusy(true);
    const{error}=await supabase.auth.updateUser({password:pwNew});
    setBusy(false);
    if(error){setErr(error.message);return;}
    setDone(true);
  };

  return (
    <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",fontFamily:"Segoe UI,system-ui,sans-serif",padding:"20px"}}>
      <div style={{background:T.panel,border:`1px solid ${T.gold}40`,borderRadius:14,padding:"28px 32px",maxWidth:420,width:"100%"}}>
        <div style={{display:"flex",gap:12,alignItems:"center",marginBottom:18}}>
          <div style={{width:42,height:42,borderRadius:10,background:`linear-gradient(135deg,${T.gold},#f0d070)`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:20}}>🔐</div>
          <div>
            <div style={{fontSize:9,letterSpacing:3,color:T.gold,marginBottom:2}}>NABH 6TH EDITION</div>
            <div style={{fontSize:15,fontWeight:700,color:T.white}}>Set New Password</div>
          </div>
        </div>

        {!done ? (
          <>
            <div style={{fontSize:11,color:T.text,lineHeight:1.6,marginBottom:18,padding:"10px 12px",background:T.panel2,borderRadius:8,border:`1px solid ${T.border}`}}>
              You arrived here via a password reset link for <strong style={{color:T.gold}}>{user?.email||"your account"}</strong>. Set your new password below.
            </div>

            <div style={{display:"grid",gap:12}}>
              <div>
                <div style={{fontSize:9,color:T.muted,marginBottom:5,letterSpacing:1}}>NEW PASSWORD (min 6 characters)</div>
                <input type="password" value={pwNew} onChange={e=>setPwNew(e.target.value)} autoFocus autoComplete="new-password" style={{width:"100%",padding:"9px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13}}/>
              </div>
              <div>
                <div style={{fontSize:9,color:T.muted,marginBottom:5,letterSpacing:1}}>CONFIRM NEW PASSWORD</div>
                <input type="password" value={pwConfirm} onChange={e=>setPwConfirm(e.target.value)} onKeyDown={e=>{if(e.key==="Enter")submit();}} autoComplete="new-password" style={{width:"100%",padding:"9px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13}}/>
              </div>

              {err&&<div style={{padding:"8px 12px",background:T.redD,border:`1px solid ${T.red}40`,borderRadius:7,color:T.red,fontSize:11}}>⚠️ {err}</div>}

              <button onClick={submit} disabled={busy} style={{padding:"11px 16px",borderRadius:8,border:`1px solid ${T.gold}`,background:`linear-gradient(135deg,${T.gold},#f0d070)`,color:T.bg,fontSize:12,fontWeight:800,cursor:busy?"not-allowed":"pointer",opacity:busy?0.6:1,marginTop:4}}>{busy?"Updating…":"Set Password & Continue"}</button>
            </div>

            <div style={{marginTop:18,paddingTop:14,borderTop:`1px solid ${T.border}`,fontSize:10,color:T.muted,textAlign:"center"}}>
              Didn't request this? <button onClick={async()=>{await supabase.auth.signOut();window.location.reload();}} style={{background:"transparent",border:"none",color:T.blue,fontSize:10,cursor:"pointer",textDecoration:"underline",padding:0}}>Cancel and sign out</button>
            </div>
          </>
        ) : (
          <div style={{textAlign:"center",padding:"20px 0"}}>
            <div style={{fontSize:36,marginBottom:10}}>✅</div>
            <div style={{fontSize:14,color:T.green,fontWeight:700,marginBottom:6}}>Password Updated</div>
            <div style={{fontSize:11,color:T.text,lineHeight:1.6,marginBottom:18}}>Your password has been set. Sign in with your new password to continue.</div>
            <button onClick={async()=>{await supabase.auth.signOut();if(onDone)onDone();}} style={{padding:"10px 28px",borderRadius:8,border:`1px solid ${T.gold}`,background:T.goldD,color:T.gold,fontSize:12,fontWeight:700,cursor:"pointer"}}>Continue to Sign In</button>
          </div>
        )}
      </div>
    </div>
  );
}

// ── ROOT APP ──────────────────────────────────────────
export default function App() {
  const [authState,setAuthState]=useState("loading");
  const [user,setUser]=useState(null);
  const [context,setContext]=useState(null);
  const [screen,setScreen]=useState("dashboard");
  const [decision,setDecision]=useState({});
  const [gaps,setGaps]=useState([]);
  const [oes,setOes]=useState([]);
  const [standards,setStandards]=useState([]);
  const [loading,setLoading]=useState(false);

  const [authErrorMsg,setAuthErrorMsg]=useState("");

  useEffect(()=>{
    // Detect auth error fragment in URL (e.g., expired/invalid recovery link)
    // This MUST run before any session check — an expired link with an active session
    // would otherwise silently land on dashboard, hiding the error from the user.
    const hash=window.location.hash;
    if(hash&&hash.includes("error=")){
      const params=new URLSearchParams(hash.slice(1));
      const code=params.get("error_code");
      const desc=params.get("error_description")||"";
      let msg="";
      if(code==="otp_expired"||desc.toLowerCase().includes("expired")){
        msg="⏱️ Your password reset link has expired. Click 'Forgot password?' below to request a new one — and use it within 1 hour of receiving the email.";
      }else if(code==="access_denied"){
        msg="⚠️ This link is invalid or already used. Click 'Forgot password?' below to request a fresh reset email.";
      }else if(desc){
        msg=decodeURIComponent(desc.replace(/\+/g," "));
      }
      if(msg){
        setAuthErrorMsg(msg);
        window.history.replaceState(null,"",window.location.pathname);
        // Force sign-out so the LoginScreen actually renders with our banner
        supabase.auth.signOut().then(()=>{setUser(null);setAuthState("login");setContext(null);});
        return; // Skip the normal session check
      }
    }
    // Check for token_hash + type=recovery in query params (Supabase email template sends SiteURL?token_hash=...&type=recovery)
    const urlParams=new URLSearchParams(window.location.search);
    const tokenHash=urlParams.get("token_hash");
    const urlType=urlParams.get("type");
    const isRecoveryLink=tokenHash&&urlType==="recovery";
    if(isRecoveryLink){
      window.history.replaceState(null,"",window.location.pathname);
      supabase.auth.verifyOtp({token_hash:tokenHash,type:"recovery"}).then(({data,error})=>{
        if(error){setAuthErrorMsg("⚠️ Password reset link is invalid or expired. Request a new one.");setAuthState("login");}
        else{if(data?.user)setUser(data.user);setAuthState("recovery");}
      });
      return;
    }
    supabase.auth.getSession().then(({data:{session}})=>{
      if(session?.user){setUser(session.user);setAuthState("setup");}
      else setAuthState("login");
    });
    const{data:{subscription}}=supabase.auth.onAuthStateChange((event,session)=>{
      if(event==="PASSWORD_RECOVERY"){
        if(session?.user)setUser(session.user);
        setAuthState("recovery");
        return;
      }
      if(session?.user){setUser(session.user);setAuthState(s=>s==="recovery"?s:s==="loading"?"setup":s);}
      else{setUser(null);setAuthState("login");setContext(null);}
    });
    return()=>subscription.unsubscribe();
  },[]);

  const loadData=useCallback(async(ctx)=>{
    if(!ctx?.assessmentId)return;
    setLoading(true);const aid=ctx.assessmentId;
    const{data:dec}=await supabase.rpc("get_final_decision",{param_id:aid});if(dec)setDecision(dec);
    const{data:gapsData}=await supabase.rpc("get_active_gaps",{param_id:aid});setGaps(gapsData||[]);
    const{data:stdsData}=await supabase.from("standards").select("id, chapter_id, title").order("id");
    if(stdsData)setStandards(stdsData);
    const{data:oesData}=await supabase.from("objective_elements").select("id, chapter_id, level, text, doc_required, standard_id, achieve_tips").order("chapter_id");
    if(oesData){
      const{data:scoresData}=await supabase.from("scores").select("oe_id, score, evidence_links").eq("assessment_id",aid);
      const scoreMap={};const linksMap={};(scoresData||[]).forEach(s=>{scoreMap[s.oe_id]=s.score;linksMap[s.oe_id]=s.evidence_links||[];});
      const sorted=oesData.sort((a,b)=>{
        if(a.chapter_id!==b.chapter_id){
          const orderA=CHAPTER_ORDER[a.chapter_id]||999;
          const orderB=CHAPTER_ORDER[b.chapter_id]||999;
          return orderA-orderB;
        }
        return a.id.localeCompare(b.id,undefined,{numeric:true,sensitivity:"base"});
      });
      setOes(sorted.map(oe=>({id:oe.id,chapter:oe.chapter_id,level:oe.level,text:oe.text,doc:oe.doc_required,standard:oe.standard_id,achieveTips:oe.achieve_tips||null,score:scoreMap[oe.id]||null,evidenceLinks:linksMap[oe.id]||[]})));
    }
    setLoading(false);
  },[]);

  const handleReady=(ctx)=>{setContext(ctx);setAuthState("app");loadData(ctx);};
  const handleSignOut=async()=>{await supabase.auth.signOut();};

  if(authState==="loading") return <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",color:T.gold,fontFamily:"Segoe UI,sans-serif",fontSize:14}}>Loading…</div>;
  if(authState==="recovery") return <RecoveryScreen user={user} onDone={()=>{setUser(null);setAuthState("login");setContext(null);}}/>;
  if(authState==="login") return <LoginScreen onLogin={u=>{setUser(u);setAuthState("setup");}} initialError={authErrorMsg}/>;
  if(authState==="setup") return <SetupScreen user={user} onReady={handleReady}/>;

  const readinessColor=decision.readiness==="NOT READY"?T.red:decision.readiness==="RISKY"?T.orange:T.green;
  const verdictColor=decision.verdict==="FAIL"?T.red:decision.verdict==="PASS"?T.green:decision.verdict==="PARTIAL"?T.orange:T.blue;
  const NAV=[
    {id:"dashboard",label:"Dashboard",icon:"📊"},
    {id:"scoring",label:"Score OEs",icon:"✏️"},
    {id:"gaps",label:"Fix Gaps",icon:"🔧"},
    {id:"committees",label:"Committees",icon:"🏛️"},
    {id:"committee-calendar",label:"Cal",icon:"📅"},
    {id:"kpis",label:"KPIs",icon:"📈"},
    {id:"checklists",label:"Checklists",icon:"✅"},
    {id:"audits",label:"Audits",icon:"🔍"},
    {id:"drills",label:"Drills",icon:"🚨"},
    {id:"licenses",label:"Licenses",icon:"📋"},
    {id:"tracer",label:"Tracer",icon:"🩺"},
    {id:"profile",label:"Profile",icon:"👤"},
  ];

  return (
    <div style={{fontFamily:"Segoe UI,system-ui,sans-serif",background:T.bg,minHeight:"100vh",color:T.text}}>
      <style>{`
        *{box-sizing:border-box}
        ::-webkit-scrollbar{width:4px}
        ::-webkit-scrollbar-track{background:${T.bg}}
        ::-webkit-scrollbar-thumb{background:${T.border};border-radius:2px}
        button,select,textarea,input{font-family:inherit}
      `}</style>
      <div style={{background:"linear-gradient(90deg,#040d1a,#08192e)",borderBottom:`1px solid ${T.border}`,padding:"10px 20px",position:"sticky",top:0,zIndex:200,boxShadow:"0 2px 20px rgba(0,0,0,0.6)"}}>
        <div style={{maxWidth:1200,margin:"0 auto",display:"flex",alignItems:"center",gap:10,flexWrap:"wrap"}}>
          <div style={{width:32,height:32,borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:17,flexShrink:0}}>⚕</div>
          <div style={{flex:1,minWidth:100}}>
            <div style={{fontSize:7,letterSpacing:3,color:T.gold}}>NABH 6TH EDITION</div>
            <div style={{fontSize:12,fontWeight:700,color:T.white}}>{context?.hospitalName||"Compliance Engine"}{context?.assessmentName&&<span style={{fontSize:9,color:T.muted,marginLeft:6}}>{context.assessmentName}</span>}</div>
          </div>
          {loading&&<div style={{fontSize:9,color:T.muted}}>Refreshing…</div>}
          <div style={{padding:"3px 10px",borderRadius:20,background:`${readinessColor}15`,border:`1px solid ${readinessColor}40`,fontSize:9,fontWeight:700,color:readinessColor}}>{decision.readiness==="NOT READY"?"❌":decision.readiness==="RISKY"?"⚠️":"✅"} {decision.readiness||"—"}</div>
          <div style={{padding:"3px 10px",borderRadius:20,background:`${verdictColor}20`,border:`1px solid ${verdictColor}40`,fontSize:10,fontWeight:800,color:verdictColor}}>{decision.verdict==="PARTIAL"?"⚠️":""}{decision.verdict||"—"}</div>
          <div style={{display:"flex",gap:3,flexWrap:"wrap"}}>
            {NAV.map(n=>(
              <button key={n.id} onClick={()=>setScreen(n.id)} style={{padding:"4px 9px",borderRadius:7,border:`1px solid ${screen===n.id?T.gold:T.border}`,background:screen===n.id?T.goldD:"transparent",color:screen===n.id?T.goldL:T.muted,fontSize:9,cursor:"pointer"}}>{n.icon} {n.label}</button>
            ))}
          </div>
          <button onClick={()=>setAuthState("setup")} style={{padding:"4px 9px",borderRadius:7,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:9,cursor:"pointer"}}>Switch</button>
          <a href="https://drive.google.com/drive/folders/1DOfGmHg_dO5blXw_3Mz07dtre6IKYYlI" target="_blank" rel="noopener noreferrer" style={{padding:"4px 9px",borderRadius:7,background:T.goldD,border:`1px solid ${T.gold}`,color:T.goldL,fontSize:9,fontWeight:700,textDecoration:"none",whiteSpace:"nowrap"}}>📁 Docs</a>
          <button onClick={handleSignOut} style={{padding:"4px 9px",borderRadius:7,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:9,cursor:"pointer"}}>Sign out</button>
        </div>
      </div>

      {(!decision.core_pass&&(decision.core_failures||0)>0)&&(
        <div style={{background:T.redD,padding:"8px 20px",display:"flex",gap:10,alignItems:"center"}}>
          <span style={{fontSize:16}}>🚨</span>
          <span style={{fontSize:11,fontWeight:700,color:T.red}}>
            CORE FAILURE: {decision.core_failures} element{decision.core_failures>1?"s":""} at risk
            {decision.core_unscored>0&&` (${decision.core_unscored} unscored, ${decision.core_scored_failures||0} scored below 4)`}
            {" "}— assessment will be rejected.
          </span>
        </div>
      )}

      <div style={{maxWidth:1200,margin:"0 auto",padding:"16px"}}>
        {screen==="dashboard"&&<Dashboard decision={decision} gaps={gaps} onNav={setScreen}/>}
        {screen==="scoring"&&<ScoringScreen assessmentId={context?.assessmentId} oes={oes} standards={standards} onRefresh={()=>loadData(context)}/>}
        {screen==="gaps"&&<GapFixScreen assessmentId={context?.assessmentId} gaps={gaps} onRefresh={()=>loadData(context)}/>}
        {screen==="committees"&&<CommitteesScreen hospitalId={context?.hospitalId}/>}
        {screen==="committee-calendar"&&<CommitteeCalendarScreen hospitalId={context?.hospitalId}/>}
        {screen==="kpis"&&<KPIsScreen hospitalId={context?.hospitalId}/>}
        {screen==="checklists"&&<ChecklistsScreen/>}
        {screen==="audits"&&<AuditsScreen hospitalId={context?.hospitalId}/>}
        {screen==="drills"&&<MockDrillsScreen hospitalId={context?.hospitalId}/>}
        {screen==="licenses"&&<StatutoryLicensesScreen hospitalId={context?.hospitalId}/>}
        {screen==="tracer"&&<PatientTracerScreen hospitalId={context?.hospitalId}/>}
        {screen==="profile"&&<ProfileScreen user={user} context={context} onContextUpdate={setContext}/>}
      </div>

      <div style={{textAlign:"center",padding:"14px",color:T.muted,fontSize:9,borderTop:`1px solid ${T.border}`,marginTop:20}}>
        NABH Compliance Engine — Independent educational tool — Not affiliated with NABH/QCI | Dr. Mehul Upadhyay
      </div>
    </div>
  );
}

// ── MOCK DRILLS ───────────────────────────────────────────────
function MockDrillsScreen({ hospitalId }) {
  const [drills,setDrills]=useState([]);
  const [records,setRecords]=useState([]);
  const [view,setView]=useState("tracker"); // tracker | calendar | record
  const [selectedDrill,setSelectedDrill]=useState(null);
  const [form,setForm]=useState({drill_date:"",drill_time:"",location:"",conducted_by:"",supervised_by:"",participants_category:"",total_participants:"",pre_briefing:"Done",scenario_desc:"",drill_description:"",observations:["","",""],debriefing:"Done",corrective_actions:"",preventive_actions:"",additional_points:"",status:"completed"});
  const [saving,setSaving]=useState(false);
  const [expanded,setExpanded]=useState(null);
  const [loading,setLoading]=useState(true);

  useEffect(()=>{
    Promise.all([
      supabase.from("mock_drills").select("*").order("frequency_per_year",{ascending:false}),
      supabase.from("mock_drill_records").select("*").eq("hospital_id",hospitalId).order("drill_date",{ascending:false})
    ]).then(([{data:d,error:e1},{data:r,error:e2}])=>{
      if(e1)console.error("mock_drills error:",e1);
      if(e2)console.error("mock_drill_records error:",e2);
      setDrills(d||[]);setRecords(r||[]);setLoading(false);
    });
  },[hospitalId]);

  const drillRecords=(id)=>records.filter(r=>r.drill_id===id);
  const lastDrill=(id)=>drillRecords(id)[0];
  const daysSince=(d)=>d?Math.floor((Date.now()-new Date(d).getTime())/86400000):999;
  const freqDays=(d)=>d==="monthly"?31:d==="quarterly"?92:120;
  const drillStatus=(drill)=>{
    const last=lastDrill(drill.id);
    if(!last)return"NOT_STARTED";
    const days=daysSince(last.drill_date);
    const max=freqDays(drill.frequency);
    if(days<=max)return"ON_TRACK";
    return"OVERDUE";
  };
  const statusColor=(s)=>s==="ON_TRACK"?T.green:s==="NOT_STARTED"?T.red:T.orange;
  const statusLabel=(s)=>s==="ON_TRACK"?"✅ On Track":s==="NOT_STARTED"?"❌ Not Started":"⚠️ Overdue";

  const totalDrills=drills.length;
  const onTrack=drills.filter(d=>drillStatus(d)==="ON_TRACK").length;
  const pct=totalDrills>0?Math.round((onTrack/totalDrills)*100):0;

  const saveRecord=async()=>{
    if(!form.drill_date||!selectedDrill)return;
    setSaving(true);
    const obs=form.observations.filter(o=>o.trim());
    await supabase.from("mock_drill_records").insert({
      hospital_id:hospitalId,drill_id:selectedDrill.id,
      drill_date:form.drill_date,drill_time:form.drill_time,
      location:form.location,conducted_by:form.conducted_by,
      supervised_by:form.supervised_by,
      participants_category:form.participants_category,
      total_participants:form.total_participants?parseInt(form.total_participants):null,
      pre_briefing:form.pre_briefing,scenario_desc:form.scenario_desc,
      drill_description:form.drill_description,
      observations:obs,debriefing:form.debriefing,
      corrective_actions:form.corrective_actions,
      preventive_actions:form.preventive_actions,
      additional_points:form.additional_points,status:form.status
    });
    const {data:r}=await supabase.from("mock_drill_records").select("*").eq("hospital_id",hospitalId).order("drill_date",{ascending:false});
    setRecords(r||[]);setSaving(false);setView("tracker");setSelectedDrill(null);
  };

  if(loading)return <div style={{textAlign:"center",padding:40,color:T.muted}}>Loading…</div>;

  // RECORD FORM
  if(view==="record"&&selectedDrill)return(
    <div>
      <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:14}}>
        <button onClick={()=>{setView("tracker");setSelectedDrill(null);}} style={{padding:"5px 12px",borderRadius:7,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:11,cursor:"pointer"}}>← Back</button>
        <div style={{fontSize:14,fontWeight:700,color:T.gold}}>Record Drill: {selectedDrill.name}</div>
      </div>
      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
        {[["Drill Date *","date","drill_date"],["Drill Time","time","drill_time"],["Location","text","location"],["Conducted By","text","conducted_by"],["Supervised By","text","supervised_by"],["Participants Category","text","participants_category"],["Total Participants","number","total_participants"]].map(([l,t,k])=>(
          <div key={k}>
            <div style={{fontSize:9,color:T.muted,marginBottom:3}}>{l}</div>
            <input type={t} value={form[k]} onChange={e=>setForm(p=>({...p,[k]:e.target.value}))}
              style={{width:"100%",padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:11}}/>
          </div>
        ))}
        {[["Pre-Briefing","pre_briefing"],["Status","status"],["Debriefing","debriefing"]].map(([l,k])=>(
          <div key={k}>
            <div style={{fontSize:9,color:T.muted,marginBottom:3}}>{l}</div>
            <select value={form[k]} onChange={e=>setForm(p=>({...p,[k]:e.target.value}))}
              style={{width:"100%",padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:11}}>
              {k==="status"?<><option value="completed">Completed</option><option value="planned">Planned</option><option value="missed">Missed</option></>
              :<><option value="Done">Done</option><option value="Not Done">Not Done</option><option value="Not Required">Not Required</option></>}
            </select>
          </div>
        ))}
      </div>
      {[["Scenario Description","scenario_desc"],["Drill Description & Response","drill_description"],["Corrective Actions","corrective_actions"],["Preventive Actions","preventive_actions"],["Additional Points","additional_points"]].map(([l,k])=>(
        <div key={k} style={{marginBottom:8}}>
          <div style={{fontSize:9,color:T.muted,marginBottom:3}}>{l}</div>
          <textarea value={form[k]} onChange={e=>setForm(p=>({...p,[k]:e.target.value}))} rows={2}
            style={{width:"100%",padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:11,resize:"vertical"}}/>
        </div>
      ))}
      <div style={{marginBottom:10}}>
        <div style={{fontSize:9,color:T.muted,marginBottom:5}}>Deviations / Observations (one per line)</div>
        {form.observations.map((o,i)=>(
          <input key={i} value={o} onChange={e=>{const obs=[...form.observations];obs[i]=e.target.value;setForm(p=>({...p,observations:obs}));}}
            placeholder={`Observation ${i+1}`}
            style={{width:"100%",padding:"6px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:11,marginBottom:4}}/>
        ))}
        <button onClick={()=>setForm(p=>({...p,observations:[...p.observations,""]}))}
          style={{fontSize:10,color:T.gold,background:"transparent",border:"none",cursor:"pointer"}}>+ Add observation</button>
      </div>
      <button onClick={saveRecord} disabled={saving||!form.drill_date}
        style={{padding:"10px 24px",borderRadius:9,background:T.goldD,border:`1px solid ${T.gold}`,color:T.goldL,fontSize:12,fontWeight:700,cursor:"pointer"}}>
        {saving?"Saving…":"💾 Save Drill Record"}
      </button>
    </div>
  );

  // TRACKER VIEW
  return(
    <div>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"14px 18px",marginBottom:14,display:"flex",gap:20,alignItems:"center",flexWrap:"wrap"}}>
        <div>
          <div style={{fontSize:9,letterSpacing:2,color:T.muted,marginBottom:2}}>MOCK DRILL READINESS</div>
          <div style={{fontSize:28,fontWeight:800,color:pct===100?T.green:pct>50?T.gold:T.red}}>{pct}%</div>
          <div style={{fontSize:10,color:T.muted}}>{onTrack}/{totalDrills} drills on track</div>
        </div>
        <div style={{flex:1,minWidth:200}}>
          <div style={{height:8,background:T.border,borderRadius:4,marginBottom:8}}>
            <div style={{width:`${pct}%`,height:"100%",background:pct===100?T.green:pct>50?T.gold:T.red,borderRadius:4,transition:"width 0.5s"}}/>
          </div>
          <div style={{display:"flex",gap:16,fontSize:9,color:T.muted}}>
            <span>🔴 {drills.filter(d=>drillStatus(d)==="NOT_STARTED").length} Not Started</span>
            <span>⚠️ {drills.filter(d=>drillStatus(d)==="OVERDUE").length} Overdue</span>
            <span>✅ {onTrack} On Track</span>
          </div>
        </div>
      </div>

      <div style={{display:"grid",gap:8}}>
        {drills.map(drill=>{
          const st=drillStatus(drill);
          const last=lastDrill(drill.id);
          const recs=drillRecords(drill.id);
          const isOpen=expanded===drill.id;
          return(
            <div key={drill.id} style={{background:T.panel,border:`1px solid ${isOpen?T.gold:T.border}`,borderRadius:10,overflow:"hidden"}}>
              <div style={{padding:"10px 14px",display:"flex",alignItems:"center",gap:10,cursor:"pointer"}} onClick={()=>setExpanded(isOpen?null:drill.id)}>
                <div style={{width:44,height:44,borderRadius:8,background:drill.color||T.goldD,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}>
                  <div style={{fontSize:7,fontWeight:800,color:"#ffffff",textAlign:"center",lineHeight:1.2}}>{drill.code||"DRILL"}</div>
                </div>
                <div style={{flex:1}}>
                  <div style={{fontSize:12,fontWeight:700,color:T.white}}>{drill.name}</div>
                  <div style={{fontSize:9,color:T.muted,marginTop:2}}>
                    🔁 {drill.frequency} &nbsp;|&nbsp; 📋 NABH: {drill.nabh_ref}
                    {last&&<span style={{marginLeft:8}}>Last: {last.drill_date}</span>}
                    {!last&&<span style={{marginLeft:8,color:T.red}}>Never conducted</span>}
                  </div>
                </div>
                <div style={{fontSize:9,fontWeight:700,color:statusColor(st),padding:"3px 10px",borderRadius:20,background:`${statusColor(st)}15`,border:`1px solid ${statusColor(st)}40`,whiteSpace:"nowrap"}}>{statusLabel(st)}</div>
                <button onClick={e=>{e.stopPropagation();setSelectedDrill(drill);setForm({drill_date:"",drill_time:"",location:"",conducted_by:"",supervised_by:"",participants_category:"",total_participants:"",pre_briefing:"Done",scenario_desc:"",drill_description:"",observations:["","",""],debriefing:"Done",corrective_actions:"",preventive_actions:"",additional_points:"",status:"completed"});setView("record");}}
                  style={{padding:"5px 12px",borderRadius:7,background:T.goldD,border:`1px solid ${T.gold}`,color:T.goldL,fontSize:10,fontWeight:700,cursor:"pointer",whiteSpace:"nowrap"}}>+ Record</button>
                <div style={{color:T.muted,fontSize:11}}>{isOpen?"▲":"▼"}</div>
              </div>
              {isOpen&&(
                <div style={{borderTop:`1px solid ${T.border}`,padding:"12px 14px"}}>
                  <div style={{fontSize:10,color:T.muted,marginBottom:8,lineHeight:1.6}}>{drill.description}</div>
                  {recs.length>0&&(
                    <div>
                      <div style={{fontSize:9,fontWeight:700,color:T.gold,marginBottom:6}}>DRILL HISTORY</div>
                      {recs.slice(0,5).map(r=>(
                        <div key={r.id} style={{background:T.panel2,borderRadius:7,padding:"8px 12px",marginBottom:5,fontSize:9,color:T.muted,display:"flex",gap:10,alignItems:"flex-start"}}>
                          <div style={{fontWeight:700,color:T.text,minWidth:80}}>{r.drill_date}</div>
                          <div>{r.location&&`📍 ${r.location} · `}{r.total_participants&&`👥 ${r.total_participants} participants · `}{r.conducted_by&&`👤 ${r.conducted_by}`}</div>
                          {r.corrective_actions&&<div style={{color:T.orange}}>⚡ CAPA raised</div>}
                        </div>
                      ))}
                    </div>
                  )}
                  {recs.length===0&&<div style={{fontSize:10,color:T.red,padding:"8px 0"}}>No drills recorded yet — click "+ Record" to add the first drill.</div>}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

// ── COMMITTEE CALENDAR ────────────────────────────────────────
function CommitteeCalendarScreen({ hospitalId }) {
  const [committees,setCommittees]=useState([]);
  const [meetings,setMeetings]=useState([]);
  const [year,setYear]=useState(new Date().getFullYear());
  const [loading,setLoading]=useState(true);
  const [viewMode,setViewMode]=useState("committee");

  const MONTHS=["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar"];
  const MONTH_NUMS=[4,5,6,7,8,9,10,11,12,1,2,3];

  const DRILLS=[
    {id:"code-blue",name:"Code Blue",color:"#1A4A7A",freq:"M",months:[4,5,6,7,8,9,10,11,12,1,2,3]},
    {id:"code-red",name:"Code Red",color:"#8B1A1A",freq:"M",months:[4,5,6,7,8,9,10,11,12,1,2,3]},
    {id:"code-pink",name:"Code Pink",color:"#8B1A6B",freq:"Q",months:[4,7,10,1]},
    {id:"code-grey",name:"Code Grey",color:"#4A4A4A",freq:"H",months:[4,10]},
    {id:"code-orange",name:"Code Orange",color:"#8B5A1A",freq:"H",months:[5,11]},
    {id:"code-yellow",name:"Code Yellow",color:"#8B8B1A",freq:"H",months:[6,12]},
    {id:"code-purple",name:"Code Purple",color:"#4A1A6B",freq:"H",months:[7,1]},
    {id:"chemical-spill",name:"Chemical Spill",color:"#2D6B2D",freq:"H",months:[8,2]},
    {id:"bomb-threat",name:"Bomb Threat",color:"#5A1A1A",freq:"H",months:[9,3]},
    {id:"infection-outbreak",name:"Infection Outbreak",color:"#1A5A2D",freq:"H",months:[4,10]},
    {id:"missing-patient",name:"Missing Patient",color:"#1A4A6B",freq:"H",months:[5,11]},
    {id:"it-failure",name:"IT Failure",color:"#1A1A5A",freq:"H",months:[6,12]},
    {id:"mci-community",name:"MCI Community",color:"#6B1A1A",freq:"H",months:[7,1]},
  ];

  useEffect(()=>{
    Promise.all([
      supabase.from("committees").select("id,name,frequency,chapter_ref").order("name"),
      supabase.from("committee_meetings").select("committee_id,meeting_date").eq("hospital_id",hospitalId)
    ]).then(([{data:c,error:e1},{data:m,error:e2}])=>{
      if(e1)console.error("committees error:",e1);
      setCommittees(c||[]);setMeetings(m||[]);setLoading(false);
    });
  },[hospitalId]);

  const hasMeeting=(committeeId,monthNum)=>meetings.some(m=>{
    if(m.committee_id!==committeeId)return false;
    const d=new Date(m.meeting_date);
    const mYear=d.getFullYear(); const mMonth=d.getMonth()+1;
    if(monthNum>=4)return mYear===year&&mMonth===monthNum;
    return mYear===year+1&&mMonth===monthNum;
  });

  const freqMonths=(freq)=>{
    if(!freq)return[4,7,10,1];
    const f=freq.toLowerCase();
    if(f.includes("month"))return[4,5,6,7,8,9,10,11,12,1,2,3];
    if(f.includes("bi"))return[4,6,8,10,12,2];
    if(f.includes("quarter"))return[4,7,10,1];
    if(f.includes("six")||f.includes("half"))return[4,10];
    if(f.includes("annual"))return[10];
    return[4,7,10,1];
  };

  const now=new Date();
  const isPast=(monthNum)=>{const mYear=monthNum>=4?year:year+1;return new Date(mYear,monthNum,1)<now;};
  const totalExpected=committees.reduce((sum,c)=>sum+freqMonths(c.frequency).length,0);
  const totalDone=committees.reduce((sum,c)=>sum+MONTH_NUMS.filter(m=>hasMeeting(c.id,m)).length,0);
  const pct=totalExpected>0?Math.round((totalDone/totalExpected)*100):0;

  if(loading)return <div style={{textAlign:"center",padding:40,color:T.muted}}>Loading…</div>;

  const tableHdr=(
    <thead><tr>
      <th style={{padding:"6px 8px",textAlign:"left",fontSize:9,color:T.gold,background:T.panel,border:`1px solid ${T.border}`,minWidth:150,position:"sticky",left:0,zIndex:1}}>Name</th>
      <th style={{padding:"6px 2px",textAlign:"center",fontSize:7,color:T.muted,background:T.panel,border:`1px solid ${T.border}`,minWidth:22}}>Freq</th>
      {MONTHS.map(m=><th key={m} style={{padding:"5px 2px",textAlign:"center",fontSize:7.5,color:T.gold,background:T.panel,border:`1px solid ${T.border}`,minWidth:32}}>{m}</th>)}
      <th style={{padding:"6px 2px",textAlign:"center",fontSize:7,color:T.muted,background:T.panel,border:`1px solid ${T.border}`,minWidth:34}}>Done</th>
    </tr></thead>
  );

  return(
    <div>
      <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:10,flexWrap:"wrap",gap:8}}>
        <div>
          <div style={{fontSize:13,fontWeight:700,color:T.gold}}>{viewMode==="committee"?"Committee Calendar":"Mock Drill Calendar"}</div>
          <div style={{fontSize:10,color:T.muted}}>FY {year}–{year+1}{viewMode==="committee"?` · ${totalDone}/${totalExpected} done · ${pct}%`:""}</div>
        </div>
        <div style={{display:"flex",gap:6,alignItems:"center",flexWrap:"wrap"}}>
          <div style={{display:"flex",borderRadius:7,border:`1px solid ${T.border}`,overflow:"hidden"}}>
            <button onClick={()=>setViewMode("committee")} style={{padding:"4px 10px",fontSize:9,cursor:"pointer",background:viewMode==="committee"?T.goldD:"transparent",border:"none",color:viewMode==="committee"?T.goldL:T.muted}}>🏛️ Committees</button>
            <button onClick={()=>setViewMode("drill")} style={{padding:"4px 10px",fontSize:9,cursor:"pointer",background:viewMode==="drill"?T.goldD:"transparent",border:"none",color:viewMode==="drill"?T.goldL:T.muted}}>🚨 Drills</button>
          </div>
          <button onClick={()=>setYear(y=>y-1)} style={{padding:"3px 8px",borderRadius:5,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:10,cursor:"pointer"}}>◀</button>
          <div style={{fontSize:10,fontWeight:700,color:T.gold,padding:"3px 10px",borderRadius:5,border:`1px solid ${T.gold}`,background:T.goldD}}>FY {year}–{year+1}</div>
          <button onClick={()=>setYear(y=>y+1)} style={{padding:"3px 8px",borderRadius:5,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:10,cursor:"pointer"}}>▶</button>
        </div>
      </div>

      <div style={{display:"flex",gap:10,marginBottom:8,fontSize:8,flexWrap:"wrap"}}>
        <span style={{display:"flex",alignItems:"center",gap:3}}><span style={{width:12,height:12,borderRadius:2,background:T.green,display:"inline-block"}}/>Done</span>
        <span style={{display:"flex",alignItems:"center",gap:3}}><span style={{width:12,height:12,borderRadius:2,background:"#1A3A5A",border:`1px dashed ${T.gold}`,display:"inline-block"}}/>Planned</span>
        <span style={{display:"flex",alignItems:"center",gap:3}}><span style={{width:12,height:12,borderRadius:2,background:T.red,display:"inline-block"}}/>Missed</span>
        <span style={{display:"flex",alignItems:"center",gap:3}}><span style={{width:12,height:12,borderRadius:2,background:T.border,display:"inline-block"}}/>Not Expected</span>
      </div>

      <div style={{overflowX:"auto"}}>
        {viewMode==="committee"&&(
          <table style={{borderCollapse:"collapse",width:"100%",minWidth:860}}>
            {tableHdr}
            <tbody>
              {committees.length===0&&<tr><td colSpan={16} style={{textAlign:"center",padding:30,color:T.muted,fontSize:11}}>No committees loading — check connection.</td></tr>}
              {committees.map((c,ci)=>{
                const done=MONTH_NUMS.filter(m=>hasMeeting(c.id,m)).length;
                const exp=freqMonths(c.frequency).length;
                return(
                  <tr key={c.id} style={{background:ci%2===0?T.panel:T.panel2}}>
                    <td style={{padding:"4px 8px",fontSize:8.5,border:`1px solid ${T.border}`,position:"sticky",left:0,background:ci%2===0?T.panel:T.panel2,zIndex:1}}>
                      <div style={{fontWeight:600,color:T.white,whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis",maxWidth:145}}>{c.name}</div>
                      <div style={{fontSize:6.5,color:T.muted}}>{c.chapter_ref}</div>
                    </td>
                    <td style={{padding:"3px",textAlign:"center",fontSize:7,color:T.muted,border:`1px solid ${T.border}`}}>{c.frequency?.charAt(0).toUpperCase()||"Q"}</td>
                    {MONTH_NUMS.map((mn,mi)=>{
                      const isDone=hasMeeting(c.id,mn);
                      const isExp=freqMonths(c.frequency).includes(mn);
                      const past=isPast(mn);
                      let bg="transparent",txt="",brd="none";
                      if(isDone){bg=T.green;txt="✓";}
                      else if(isExp&&!past){bg="#1A3A5A";txt="·";brd=`1px dashed ${T.gold}`;}
                      else if(isExp&&past){bg=T.red;txt="✗";}
                      return(
                        <td key={mi} style={{padding:"2px",textAlign:"center",border:`1px solid ${T.border}`}}>
                          <div style={{width:24,height:24,borderRadius:3,background:bg,margin:"0 auto",display:"flex",alignItems:"center",justifyContent:"center",fontSize:8,color:"#fff",fontWeight:700,border:brd}}>{txt}</div>
                        </td>
                      );
                    })}
                    <td style={{padding:"3px",textAlign:"center",fontSize:8,fontWeight:700,color:done>=exp?T.green:done>0?T.orange:T.red,border:`1px solid ${T.border}`}}>{done}/{exp}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        )}
        {viewMode==="drill"&&(
          <table style={{borderCollapse:"collapse",width:"100%",minWidth:860}}>
            {tableHdr}
            <tbody>
              {DRILLS.map((d,ci)=>(
                <tr key={d.id} style={{background:ci%2===0?T.panel:T.panel2}}>
                  <td style={{padding:"4px 8px",fontSize:8.5,border:`1px solid ${T.border}`,position:"sticky",left:0,background:ci%2===0?T.panel:T.panel2,zIndex:1}}>
                    <div style={{display:"flex",alignItems:"center",gap:5}}>
                      <div style={{width:8,height:8,borderRadius:2,background:d.color,flexShrink:0}}/>
                      <div style={{fontWeight:600,color:T.white}}>{d.name}</div>
                    </div>
                  </td>
                  <td style={{padding:"3px",textAlign:"center",fontSize:7,color:T.muted,border:`1px solid ${T.border}`}}>{d.freq}</td>
                  {MONTH_NUMS.map((mn,mi)=>{
                    const isPlanned=d.months.includes(mn);
                    const past=isPast(mn);
                    let bg="transparent",txt="",brd="none";
                    if(isPlanned&&!past){bg=d.color;txt="📅";brd=`1px solid ${d.color}`;}
                    else if(isPlanned&&past){bg="#2A2A3A";txt="?";}
                    return(
                      <td key={mi} style={{padding:"2px",textAlign:"center",border:`1px solid ${T.border}`}}>
                        <div style={{width:24,height:24,borderRadius:3,background:bg,margin:"0 auto",display:"flex",alignItems:"center",justifyContent:"center",fontSize:7,color:"#fff",fontWeight:700,border:brd}}>{txt}</div>
                      </td>
                    );
                  })}
                  <td style={{padding:"3px",textAlign:"center",fontSize:8,fontWeight:700,color:T.gold,border:`1px solid ${T.border}`}}>{d.months.length}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}


// ── STATUTORY LICENSE TRACKER ─────────────────────────────────
const LICENSE_TEMPLATES = [
  {name:"Fire NOC",authority:"Fire Department / Municipality",type:"Safety"},
  {name:"BMW Authorization",authority:"State Pollution Control Board",type:"Waste"},
  {name:"PCB Consent to Operate",authority:"State Pollution Control Board",type:"Environmental"},
  {name:"CGWA Water Withdrawal",authority:"Central Ground Water Authority",type:"Environmental"},
  {name:"Lift License",authority:"State Electrical Inspectorate",type:"Infrastructure"},
  {name:"Clinical Establishment Registration",authority:"State Health Department",type:"Regulatory"},
  {name:"Blood Bank License",authority:"CDSCO / State Drugs Controller",type:"Clinical"},
  {name:"Pharmacy License",authority:"State Drugs Controller",type:"Clinical"},
  {name:"AERB Radiation Safety",authority:"Atomic Energy Regulatory Board",type:"Radiation"},
  {name:"NABH Accreditation Certificate",authority:"NABH / QCI",type:"Accreditation"},
  {name:"NABL Accreditation (Lab)",authority:"NABL",type:"Accreditation"},
  {name:"Narcotics License",authority:"State Drugs Controller / NCB",type:"Clinical"},
  {name:"Trade License",authority:"Municipality / Local Body",type:"Regulatory"},
  {name:"Biomedical Equipment Calibration",authority:"Internal / NABL Lab",type:"Quality"},
  {name:"Building Completion Certificate",authority:"Municipality",type:"Infrastructure"},
  {name:"Water Potability Certificate",authority:"Municipality / Accredited Lab",type:"Safety"},
  {name:"Sewage Treatment Plant Certificate",authority:"State PCB",type:"Environmental"},
  {name:"Medical Gas Pipeline Certificate",authority:"State Electrical Inspectorate",type:"Safety"},
  {name:"Boiler Certificate",authority:"State Boiler Inspectorate",type:"Infrastructure"},
  {name:"Diesel Generator Clearance",authority:"State PCB / Municipality",type:"Environmental"},
];

function StatutoryLicensesScreen({ hospitalId }) {
  const [licenses,setLicenses]=useState([]);
  const [loading,setLoading]=useState(true);
  const [saving,setSaving]=useState(false);
  const [editId,setEditId]=useState(null);
  const [showAdd,setShowAdd]=useState(false);
  const [form,setForm]=useState({license_name:"",issuing_authority:"",license_type:"",license_number:"",issue_date:"",expiry_date:"",evidence_url:"",notes:""});
  const [filter,setFilter]=useState("all");

  useEffect(()=>{load();},[hospitalId]);

  const load=async()=>{
    setLoading(true);
    const{data}=await supabase.from("statutory_licenses").select("*").eq("hospital_id",hospitalId).order("expiry_date",{ascending:true});
    setLicenses(data||[]);setLoading(false);
  };

  const getStatus=(expiry)=>{
    if(!expiry)return{label:"No Expiry Set",color:T.muted,bg:"transparent"};
    const d=new Date(expiry),now=new Date(),diff=Math.ceil((d-now)/(1000*60*60*24));
    if(diff<0)return{label:"EXPIRED",color:T.red,bg:T.redD};
    if(diff<=30)return{label:`Expires in ${diff}d`,color:T.orange,bg:T.orangeD};
    if(diff<=90)return{label:`Expires in ${diff}d`,color:T.gold,bg:T.goldD};
    return{label:"Valid",color:T.green,bg:T.greenD};
  };

  const save=async()=>{
    if(!form.license_name.trim())return;
    setSaving(true);
    if(editId){
      await supabase.from("statutory_licenses").update({...form,updated_at:new Date().toISOString()}).eq("id",editId);
    } else {
      await supabase.from("statutory_licenses").insert({...form,hospital_id:hospitalId});
    }
    setSaving(false);setEditId(null);setShowAdd(false);
    setForm({license_name:"",issuing_authority:"",license_type:"",license_number:"",issue_date:"",expiry_date:"",evidence_url:"",notes:""});
    load();
  };

  const del=async(id)=>{
    if(!window.confirm("Delete this license record?"))return;
    await supabase.from("statutory_licenses").delete().eq("id",id);
    load();
  };

  const startEdit=(l)=>{
    setEditId(l.id);
    setForm({license_name:l.license_name||"",issuing_authority:l.issuing_authority||"",license_type:l.license_type||"",license_number:l.license_number||"",issue_date:l.issue_date||"",expiry_date:l.expiry_date||"",evidence_url:l.evidence_url||"",notes:l.notes||""});
    setShowAdd(true);
  };

  const addTemplate=(t)=>{
    setForm(f=>({...f,license_name:t.name,issuing_authority:t.authority,license_type:t.type}));
  };

  const expired=licenses.filter(l=>getStatus(l.expiry_date).label==="EXPIRED").length;
  const expiring=licenses.filter(l=>getStatus(l.expiry_date).color===T.orange).length;
  const valid=licenses.filter(l=>getStatus(l.expiry_date).color===T.green).length;

  const filtered=filter==="all"?licenses:filter==="expired"?licenses.filter(l=>getStatus(l.expiry_date).label==="EXPIRED"):filter==="expiring"?licenses.filter(l=>getStatus(l.expiry_date).color===T.orange):licenses.filter(l=>getStatus(l.expiry_date).color===T.green);

  const inp={width:"100%",padding:"8px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12,boxSizing:"border-box"};

  if(loading)return<div style={{textAlign:"center",padding:40,color:T.muted}}>Loading…</div>;

  return(
    <div>
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:14,flexWrap:"wrap",gap:8}}>
        <div>
          <div style={{fontSize:14,fontWeight:700,color:T.gold}}>📋 Statutory License Tracker</div>
          <div style={{fontSize:10,color:T.muted}}>Track all mandatory licenses — get alerted before expiry</div>
        </div>
        <button onClick={()=>{setShowAdd(true);setEditId(null);setForm({license_name:"",issuing_authority:"",license_type:"",license_number:"",issue_date:"",expiry_date:"",evidence_url:"",notes:""}); }} style={{padding:"7px 16px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:11,fontWeight:700,cursor:"pointer"}}>+ Add License</button>
      </div>

      {/* Summary cards */}
      <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(120px,1fr))",gap:10,marginBottom:16}}>
        {[["Total",licenses.length,T.blue],["Valid",valid,T.green],["Expiring Soon",expiring,T.orange],["Expired",expired,T.red]].map(([label,count,color])=>(
          <div key={label} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",textAlign:"center"}}>
            <div style={{fontSize:22,fontWeight:800,color}}>{count}</div>
            <div style={{fontSize:9,color:T.muted,marginTop:2}}>{label}</div>
          </div>
        ))}
      </div>

      {/* Filter */}
      <div style={{display:"flex",gap:6,marginBottom:12}}>
        {[["all","All"],["valid","Valid"],["expiring","Expiring"],["expired","Expired"]].map(([val,label])=>(
          <button key={val} onClick={()=>setFilter(val)} style={{padding:"4px 12px",borderRadius:6,border:`1px solid ${filter===val?T.gold:T.border}`,background:filter===val?T.goldD:"transparent",color:filter===val?T.goldL:T.muted,fontSize:9,cursor:"pointer"}}>{label}</button>
        ))}
      </div>

      {/* Add/Edit form */}
      {showAdd&&(
        <div style={{background:T.panel,border:`1px solid ${T.gold}40`,borderRadius:12,padding:18,marginBottom:16}}>
          <div style={{fontSize:12,fontWeight:700,color:T.gold,marginBottom:12}}>{editId?"Edit License":"Add New License"}</div>

          {/* Quick templates */}
          {!editId&&(
            <div style={{marginBottom:14}}>
              <div style={{fontSize:9,color:T.muted,marginBottom:6,letterSpacing:1}}>QUICK ADD FROM TEMPLATE</div>
              <div style={{display:"flex",flexWrap:"wrap",gap:5}}>
                {LICENSE_TEMPLATES.map(t=>(
                  <button key={t.name} onClick={()=>addTemplate(t)} style={{padding:"3px 8px",borderRadius:5,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:9,cursor:"pointer"}}>{t.name}</button>
                ))}
              </div>
            </div>
          )}

          <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
            <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>LICENSE NAME *</div><input style={inp} value={form.license_name} onChange={e=>setForm(f=>({...f,license_name:e.target.value}))}/></div>
            <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>ISSUING AUTHORITY</div><input style={inp} value={form.issuing_authority} onChange={e=>setForm(f=>({...f,issuing_authority:e.target.value}))}/></div>
            <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>LICENSE NUMBER</div><input style={inp} value={form.license_number} onChange={e=>setForm(f=>({...f,license_number:e.target.value}))}/></div>
            <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>TYPE</div>
              <select style={inp} value={form.license_type} onChange={e=>setForm(f=>({...f,license_type:e.target.value}))}>
                <option value="">Select type…</option>
                {["Safety","Waste","Environmental","Clinical","Regulatory","Infrastructure","Radiation","Accreditation","Quality"].map(t=><option key={t} value={t}>{t}</option>)}
              </select>
            </div>
            <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>ISSUE DATE</div><input style={inp} type="date" value={form.issue_date} onChange={e=>setForm(f=>({...f,issue_date:e.target.value}))}/></div>
            <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>EXPIRY DATE</div><input style={inp} type="date" value={form.expiry_date} onChange={e=>setForm(f=>({...f,expiry_date:e.target.value}))}/></div>
            <div style={{gridColumn:"span 2"}}><div style={{fontSize:9,color:T.muted,marginBottom:4}}>EVIDENCE LINK (Google Drive / OneDrive URL)</div><input style={inp} placeholder="https://drive.google.com/…" value={form.evidence_url} onChange={e=>setForm(f=>({...f,evidence_url:e.target.value}))}/></div>
            <div style={{gridColumn:"span 2"}}><div style={{fontSize:9,color:T.muted,marginBottom:4}}>NOTES</div><input style={inp} placeholder="Renewal in progress, contact person, etc." value={form.notes} onChange={e=>setForm(f=>({...f,notes:e.target.value}))}/></div>
          </div>
          <div style={{display:"flex",gap:8,marginTop:12}}>
            <button onClick={save} disabled={saving||!form.license_name.trim()} style={{padding:"8px 20px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:11,fontWeight:700,cursor:"pointer",opacity:saving?0.6:1}}>{saving?"Saving…":"Save License"}</button>
            <button onClick={()=>{setShowAdd(false);setEditId(null);}} style={{padding:"8px 16px",borderRadius:8,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:11,cursor:"pointer"}}>Cancel</button>
          </div>
        </div>
      )}

      {/* License list */}
      {filtered.length===0?(
        <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"30px",textAlign:"center",color:T.muted,fontSize:11}}>
          {licenses.length===0?"No licenses added yet. Click '+ Add License' to start tracking.":"No licenses in this filter."}
        </div>
      ):(
        <div style={{display:"grid",gap:8}}>
          {filtered.map(l=>{
            const st=getStatus(l.expiry_date);
            return(
              <div key={l.id} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",display:"flex",gap:12,alignItems:"center",flexWrap:"wrap"}}>
                <div style={{flex:1,minWidth:180}}>
                  <div style={{fontSize:12,fontWeight:700,color:T.white}}>{l.license_name}</div>
                  <div style={{fontSize:10,color:T.muted,marginTop:2}}>{l.issuing_authority||"—"}{l.license_number&&<span style={{marginLeft:8,color:T.blue}}>#{l.license_number}</span>}</div>
                  {l.notes&&<div style={{fontSize:9,color:T.muted,marginTop:3}}>{l.notes}</div>}
                </div>
                <div style={{textAlign:"center",minWidth:80}}>
                  <div style={{fontSize:9,color:T.muted}}>EXPIRY</div>
                  <div style={{fontSize:11,color:T.text,marginTop:2}}>{l.expiry_date?new Date(l.expiry_date).toLocaleDateString("en-IN",{day:"2-digit",month:"short",year:"numeric"}):"Not set"}</div>
                </div>
                <div style={{padding:"4px 10px",borderRadius:8,background:st.bg,border:`1px solid ${st.color}30`,fontSize:9,fontWeight:700,color:st.color,minWidth:90,textAlign:"center"}}>{st.label}</div>
                {l.license_type&&<div style={{padding:"3px 8px",borderRadius:6,background:T.blueD,border:`1px solid ${T.blue}30`,fontSize:8,color:T.blue}}>{l.license_type}</div>}
                <div style={{display:"flex",gap:6,alignItems:"center"}}>
                  {l.evidence_url&&<a href={l.evidence_url} target="_blank" rel="noopener noreferrer" style={{padding:"4px 10px",borderRadius:6,background:T.greenD,border:`1px solid ${T.green}40`,color:T.green,fontSize:9,textDecoration:"none",fontWeight:600}}>📎 View</a>}
                  <button onClick={()=>startEdit(l)} style={{padding:"4px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:9,cursor:"pointer"}}>Edit</button>
                  <button onClick={()=>del(l.id)} style={{padding:"4px 10px",borderRadius:6,border:`1px solid ${T.red}30`,background:"transparent",color:T.red,fontSize:9,cursor:"pointer"}}>Delete</button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

// ── PATIENT TRACER ─────────────────────────────────────────────
const TRACER_TYPES = {
  "General IPD": {
    icon:"🛏️",
    color:"#4fc3f7",
    desc:"General inpatient admission tracer",
    questions:[
      {id:"t1",q:"Was the patient triaged and initial assessment completed within 30 minutes of admission?",oe:"AAC.1"},
      {id:"t2",q:"Is a complete nursing assessment documented within 8 hours of admission?",oe:"AAC.2"},
      {id:"t3",q:"Has a medical history and physical examination been completed and documented by a doctor?",oe:"AAC.3"},
      {id:"t4",q:"Is the care plan documented with goals, interventions, and responsible staff?",oe:"COP.1"},
      {id:"t5",q:"Is informed consent obtained and documented before any invasive procedure?",oe:"PRE.4"},
      {id:"t6",q:"Are the patient's rights and responsibilities communicated and acknowledged?",oe:"PRE.1"},
      {id:"t7",q:"Is medication reconciliation done and documented at admission?",oe:"MOM.1"},
      {id:"t8",q:"Are all medications prescribed with generic name, dose, route, frequency?",oe:"MOM.3"},
      {id:"t9",q:"Is the patient's pain assessed and documented using a validated scale?",oe:"COP.2"},
      {id:"t10",q:"Is fall risk assessment done and prevention measures documented?",oe:"PSQ.1"},
      {id:"t11",q:"Is pressure sore risk assessed (Braden/Waterlow scale)?",oe:"COP.3"},
      {id:"t12",q:"Are hand hygiene observations documented for this patient's care team?",oe:"IPC.1"},
      {id:"t13",q:"Is the discharge plan initiated within 24 hours of admission?",oe:"AAC.5"},
      {id:"t14",q:"Is patient/family education documented with language and literacy noted?",oe:"PRE.5"},
      {id:"t15",q:"Are all investigations ordered with clinical indication documented?",oe:"AAC.4"},
    ]
  },
  "Surgical Tracer": {
    icon:"🔪",
    color:"#e05a5a",
    desc:"Pre-op, intra-op, and post-op documentation audit",
    questions:[
      {id:"s1",q:"Is pre-operative assessment completed and documented?",oe:"COP.8"},
      {id:"s2",q:"Is anaesthesia pre-assessment done and signed by anaesthetist?",oe:"COP.9"},
      {id:"s3",q:"Is surgical consent obtained by the operating surgeon (not delegated)?",oe:"PRE.4"},
      {id:"s4",q:"Is anaesthesia consent separately obtained by the anaesthetist?",oe:"PRE.4"},
      {id:"s5",q:"Is the WHO Surgical Safety Checklist completed (Sign-In, Time-Out, Sign-Out)?",oe:"COP.10"},
      {id:"s6",q:"Is the operative note completed within 24 hours of surgery?",oe:"COP.11"},
      {id:"s7",q:"Is post-operative monitoring documented (vitals, pain, drainage)?",oe:"COP.12"},
      {id:"s8",q:"Are prophylactic antibiotics given as per protocol (1 hour pre-incision)?",oe:"IPC.4"},
      {id:"s9",q:"Is the site marking documented pre-operatively for laterality?",oe:"PSQ.3"},
      {id:"s10",q:"Is blood availability confirmed pre-operatively for major surgeries?",oe:"COP.8"},
      {id:"s11",q:"Is VTE prophylaxis assessed and documented?",oe:"COP.3"},
      {id:"s12",q:"Is implant register updated if any implant was used?",oe:"COP.11"},
      {id:"s13",q:"Is the specimen sent to histopathology with proper labeling?",oe:"AAC.4"},
      {id:"s14",q:"Is immediate post-op note written in OT itself?",oe:"COP.11"},
      {id:"s15",q:"Is patient transferred to recovery room with documented handover?",oe:"COP.12"},
    ]
  },
  "ICU Tracer": {
    icon:"🫀",
    color:"#f4a441",
    desc:"Critical care bundle compliance and documentation",
    questions:[
      {id:"i1",q:"Is ICU admission note with APACHE II score documented?",oe:"COP.5"},
      {id:"i2",q:"Are daily ICU rounds documented with goals of care?",oe:"COP.5"},
      {id:"i3",q:"Is VAP bundle compliance documented (HOB elevation, oral care, cuff pressure)?",oe:"IPC.5"},
      {id:"i4",q:"Is CLABSI bundle documented for all central lines (insertion + daily care)?",oe:"IPC.6"},
      {id:"i5",q:"Is CAUTI prevention bundle documented for all urinary catheters?",oe:"IPC.7"},
      {id:"i6",q:"Are ventilator settings and changes documented with rationale?",oe:"COP.5"},
      {id:"i7",q:"Is sedation/analgesia scale used and documented (RASS/VAS)?",oe:"COP.2"},
      {id:"i8",q:"Is daily spontaneous breathing trial documented for ventilated patients?",oe:"COP.5"},
      {id:"i9",q:"Is family communication documented at least once in 24 hours?",oe:"PRE.3"},
      {id:"i10",q:"Is fluid balance charted every 6 hours?",oe:"COP.5"},
      {id:"i11",q:"Are blood glucose monitoring results documented per protocol?",oe:"COP.6"},
      {id:"i12",q:"Is DVT prophylaxis assessed and documented?",oe:"COP.3"},
      {id:"i13",q:"Is restraint use (if any) documented with consent and hourly monitoring?",oe:"COP.7"},
      {id:"i14",q:"Is end-of-life care plan documented for terminal patients?",oe:"COP.4"},
      {id:"i15",q:"Is ICU transfer note written when patient is shifted to ward?",oe:"AAC.5"},
    ]
  },
  "Emergency Tracer": {
    icon:"🚨",
    color:"#e05a5a",
    desc:"Emergency department triage and documentation",
    questions:[
      {id:"e1",q:"Is triage done within 5 minutes of arrival using validated triage scale?",oe:"AAC.1"},
      {id:"e2",q:"Is triage category documented and consistent with patient condition?",oe:"AAC.1"},
      {id:"e3",q:"Are vitals documented at arrival and at regular intervals?",oe:"AAC.2"},
      {id:"e4",q:"Is MLC (Medico-Legal Case) identification and reporting documented?",oe:"ROM.6"},
      {id:"e5",q:"Is police intimation documented for MLC cases?",oe:"ROM.6"},
      {id:"e6",q:"Is time of doctor assessment from arrival documented?",oe:"AAC.1"},
      {id:"e7",q:"Is ABCDE assessment documented for critical patients?",oe:"COP.1"},
      {id:"e8",q:"Is informed consent obtained before any procedure?",oe:"PRE.4"},
      {id:"e9",q:"Is drug allergy checked before administering medications?",oe:"MOM.5"},
      {id:"e10",q:"Is reason for admission or discharge documented?",oe:"AAC.3"},
      {id:"e11",q:"Is social history (domestic violence, child abuse) screened if applicable?",oe:"PRE.1"},
      {id:"e12",q:"Is LAMA (Leave Against Medical Advice) documented with informed refusal?",oe:"PRE.1"},
      {id:"e13",q:"Is disaster/mass casualty procedure documentation available?",oe:"FMS.7"},
      {id:"e14",q:"Is crash cart checked and documented as per protocol?",oe:"FMS.3"},
      {id:"e15",q:"Is referral documentation complete if patient transferred to another facility?",oe:"AAC.6"},
    ]
  },
  "Maternity Tracer": {
    icon:"🤱",
    color:"#c084e8",
    desc:"Labour room and maternity care documentation",
    questions:[
      {id:"m1",q:"Is antenatal history documented completely on admission?",oe:"COP.13"},
      {id:"m2",q:"Is partograph initiated and maintained from active labour?",oe:"COP.13"},
      {id:"m3",q:"Is fetal heart rate monitoring documented every 30 minutes in active labour?",oe:"COP.13"},
      {id:"m4",q:"Is consent for delivery (normal/caesarean) documented?",oe:"PRE.4"},
      {id:"m5",q:"Is oxytocin administration documented with dose, rate, and monitoring?",oe:"MOM.3"},
      {id:"m6",q:"Is birth register updated with all mandatory fields?",oe:"IMS.2"},
      {id:"m7",q:"Is APGAR score documented at 1 and 5 minutes?",oe:"COP.14"},
      {id:"m8",q:"Is vitamin K prophylaxis given and documented for newborn?",oe:"COP.14"},
      {id:"m9",q:"Is breast feeding initiation documented within 1 hour of birth?",oe:"COP.14"},
      {id:"m10",q:"Is blood loss quantified and documented in delivery note?",oe:"COP.13"},
      {id:"m11",q:"Is PPH prevention protocol (oxytocin) documented?",oe:"COP.13"},
      {id:"m12",q:"Is newborn screening documented as per national programme?",oe:"COP.14"},
      {id:"m13",q:"Is placental disposal documented per BMW rules?",oe:"IPC.9"},
      {id:"m14",q:"Is maternal death reporting (if any) done as per protocol?",oe:"PSQ.6"},
      {id:"m15",q:"Is discharge summary for mother and baby both documented?",oe:"AAC.5"},
    ]
  },
  "Medication Tracer": {
    icon:"💊",
    color:"#4caf7d",
    desc:"Medication management and high-alert drug compliance",
    questions:[
      {id:"med1",q:"Are LASA (Look-Alike Sound-Alike) drugs identified and separately stored?",oe:"MOM.2"},
      {id:"med2",q:"Are high-alert medications labeled and stored with double-check protocol?",oe:"MOM.2"},
      {id:"med3",q:"Are narcotics/controlled substances in a locked cabinet with dual custody?",oe:"MOM.6"},
      {id:"med4",q:"Is narcotics register maintained with all mandatory columns?",oe:"MOM.6"},
      {id:"med5",q:"Is medication administration documented with time, dose, route, and nurse signature?",oe:"MOM.5"},
      {id:"med6",q:"Are medication errors reported through incident reporting system?",oe:"MOM.7"},
      {id:"med7",q:"Are near-miss medication events also captured in incident reports?",oe:"PSQ.4"},
      {id:"med8",q:"Is expiry date checked before dispensing — no expired drugs in wards?",oe:"MOM.3"},
      {id:"med9",q:"Is medication reconciliation done at discharge?",oe:"MOM.1"},
      {id:"med10",q:"Are PRN (as needed) medications administered with documented indication?",oe:"MOM.5"},
      {id:"med11",q:"Is IV fluid administration documented with rate and total volume?",oe:"MOM.5"},
      {id:"med12",q:"Are adverse drug reactions documented and reported to pharmacovigilance?",oe:"MOM.7"},
      {id:"med13",q:"Is patient counselling on medications documented at discharge?",oe:"PRE.5"},
      {id:"med14",q:"Are antibiotic prescriptions following hospital antibiotic policy?",oe:"IPC.4"},
      {id:"med15",q:"Is chemotherapy (if any) prescribed and administered per double-check protocol?",oe:"MOM.4"},
    ]
  },
  "Blood Transfusion": {
    icon:"🩸",
    color:"#e05a5a",
    desc:"Blood bank and transfusion safety compliance",
    questions:[
      {id:"b1",q:"Is consent for blood transfusion obtained separately?",oe:"PRE.4"},
      {id:"b2",q:"Is blood request form complete with clinical indication?",oe:"COP.15"},
      {id:"b3",q:"Is pre-transfusion blood grouping and cross-matching documented?",oe:"COP.15"},
      {id:"b4",q:"Is bedside verification (2-person check) documented before starting transfusion?",oe:"PSQ.3"},
      {id:"b5",q:"Are vital signs documented before, during (15 min), and after transfusion?",oe:"COP.15"},
      {id:"b6",q:"Is transfusion reaction protocol available and followed?",oe:"COP.15"},
      {id:"b7",q:"Are transfusion reactions reported through haemovigilance system?",oe:"PSQ.4"},
      {id:"b8",q:"Is blood issue time and transfusion completion time documented?",oe:"COP.15"},
      {id:"b9",q:"Is blood returned to blood bank if not transfused within 30 min?",oe:"COP.15"},
      {id:"b10",q:"Is blood bag discarded as per BMW rules after transfusion?",oe:"IPC.9"},
    ]
  },
  "Document Tracer": {
    icon:"📄",
    color:"#90caf9",
    desc:"Medical record completeness and documentation standards",
    questions:[
      {id:"d1",q:"Is the admission note completed within 24 hours with all mandatory fields?",oe:"IMS.1"},
      {id:"d2",q:"Are all entries dated, timed, and signed with designation?",oe:"IMS.3"},
      {id:"d3",q:"Are corrections made by crossing out (not erasing) with date/sign?",oe:"IMS.3"},
      {id:"d4",q:"Is the discharge summary completed within 24 hours of discharge?",oe:"AAC.5"},
      {id:"d5",q:"Does the discharge summary contain all 10 mandatory elements?",oe:"AAC.5"},
      {id:"d6",q:"Are medical records stored securely with access control?",oe:"IMS.5"},
      {id:"d7",q:"Are medical records available within 30 minutes for emergency access?",oe:"IMS.5"},
      {id:"d8",q:"Is patient identity verified using at least 2 identifiers on all documents?",oe:"PSQ.2"},
      {id:"d9",q:"Are all diagnostic reports signed by the reporting doctor?",oe:"IMS.2"},
      {id:"d10",q:"Is the medical record complete before filing (deficiency tracking)?",oe:"IMS.4"},
    ]
  }
};

function PatientTracerScreen({ hospitalId }) {
  const [view,setView]=useState("list"); // list | new | conduct | history
  const [tracerType,setTracerType]=useState("General IPD");
  const [tracers,setTracers]=useState([]);
  const [loading,setLoading]=useState(true);
  const [activeTracer,setActiveTracer]=useState(null);
  const [responses,setResponses]=useState({});
  const [meta,setMeta]=useState({patient_ref:"",conducted_by:"",conducted_date:new Date().toISOString().split("T")[0],notes:""});
  const [saving,setSaving]=useState(false);

  useEffect(()=>{loadTracers();},[hospitalId]);

  const loadTracers=async()=>{
    setLoading(true);
    const{data}=await supabase.from("patient_tracers").select("*").eq("hospital_id",hospitalId).order("created_at",{ascending:false});
    setTracers(data||[]);setLoading(false);
  };

  const startNew=()=>{
    setResponses({});
    setMeta({patient_ref:"",conducted_by:"",conducted_date:new Date().toISOString().split("T")[0],notes:""});
    setActiveTracer(null);
    setView("new");
  };

  const startConduct=()=>{
    setView("conduct");
  };

  const setResp=(qid,val)=>setResponses(r=>({...r,[qid]:val}));

  const calcScore=()=>{
    const qs=TRACER_TYPES[tracerType].questions;
    const answered=qs.filter(q=>responses[q.id]==="yes"||responses[q.id]==="partial"||responses[q.id]==="no");
    if(answered.length===0)return 0;
    const score=qs.reduce((sum,q)=>sum+(responses[q.id]==="yes"?1:responses[q.id]==="partial"?0.5:0),0);
    return Math.round((score/qs.length)*100);
  };

  const saveTracer=async()=>{
    setSaving(true);
    const pct=calcScore();
    await supabase.from("patient_tracers").insert({
      hospital_id:hospitalId,
      tracer_type:tracerType,
      patient_ref:meta.patient_ref,
      conducted_date:meta.conducted_date,
      conducted_by:meta.conducted_by,
      responses,
      score_pct:pct,
      notes:meta.notes
    });
    setSaving(false);
    loadTracers();
    setView("list");
  };

  const scoreColor=(pct)=>pct>=80?T.green:pct>=60?T.orange:T.red;

  const inp={width:"100%",padding:"8px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12,boxSizing:"border-box"};

  if(loading)return<div style={{textAlign:"center",padding:40,color:T.muted}}>Loading…</div>;

  // LIST VIEW
  if(view==="list")return(
    <div>
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:14,flexWrap:"wrap",gap:8}}>
        <div>
          <div style={{fontSize:14,fontWeight:700,color:T.gold}}>🩺 Patient Tracer</div>
          <div style={{fontSize:10,color:T.muted}}>Simulate assessor patient file review — identify gaps before they do</div>
        </div>
        <button onClick={startNew} style={{padding:"7px 16px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:11,fontWeight:700,cursor:"pointer"}}>+ New Tracer</button>
      </div>

      {/* Tracer type cards */}
      <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(160px,1fr))",gap:10,marginBottom:20}}>
        {Object.entries(TRACER_TYPES).map(([type,data])=>{
          const done=tracers.filter(t=>t.tracer_type===type);
          const avg=done.length>0?Math.round(done.reduce((s,t)=>s+t.score_pct,0)/done.length):null;
          return(
            <div key={type} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px",cursor:"pointer"}} onClick={()=>{setTracerType(type);startNew();}}>
              <div style={{fontSize:20,marginBottom:6}}>{data.icon}</div>
              <div style={{fontSize:11,fontWeight:700,color:T.white,marginBottom:3}}>{type}</div>
              <div style={{fontSize:9,color:T.muted,marginBottom:8,lineHeight:1.4}}>{data.questions.length} questions</div>
              {avg!==null?(
                <div style={{fontSize:10,fontWeight:700,color:scoreColor(avg)}}>{avg}% avg ({done.length} done)</div>
              ):(
                <div style={{fontSize:9,color:T.muted}}>Not conducted yet</div>
              )}
            </div>
          );
        })}
      </div>

      {/* History */}
      {tracers.length>0&&(
        <>
          <div style={{fontSize:11,fontWeight:700,color:T.gold,marginBottom:10}}>Recent Tracers</div>
          <div style={{display:"grid",gap:8}}>
            {tracers.slice(0,10).map(t=>(
              <div key={t.id} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",display:"flex",gap:12,alignItems:"center",flexWrap:"wrap"}}>
                <div style={{fontSize:18}}>{TRACER_TYPES[t.tracer_type]?.icon||"🩺"}</div>
                <div style={{flex:1,minWidth:150}}>
                  <div style={{fontSize:11,fontWeight:700,color:T.white}}>{t.tracer_type}</div>
                  <div style={{fontSize:9,color:T.muted}}>{t.patient_ref&&`Patient: ${t.patient_ref} · `}{t.conducted_by&&`By: ${t.conducted_by} · `}{new Date(t.conducted_date).toLocaleDateString("en-IN")}</div>
                </div>
                <div style={{textAlign:"center"}}>
                  <div style={{fontSize:18,fontWeight:800,color:scoreColor(t.score_pct)}}>{t.score_pct}%</div>
                  <div style={{fontSize:8,color:T.muted}}>Score</div>
                </div>
                <div style={{padding:"3px 10px",borderRadius:7,background:t.score_pct>=80?T.greenD:t.score_pct>=60?T.orangeD:T.redD,color:scoreColor(t.score_pct),fontSize:9,fontWeight:700}}>
                  {t.score_pct>=80?"READY":t.score_pct>=60?"PARTIAL":"NOT READY"}
                </div>
              </div>
            ))}
          </div>
        </>
      )}

      {tracers.length===0&&(
        <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"30px",textAlign:"center",color:T.muted,fontSize:11}}>
          No tracers conducted yet. Click a tracer type above or '+ New Tracer' to start.
        </div>
      )}
    </div>
  );

  // NEW TRACER — select type + meta
  if(view==="new")return(
    <div>
      <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:16}}>
        <button onClick={()=>setView("list")} style={{padding:"4px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:10,cursor:"pointer"}}>← Back</button>
        <div style={{fontSize:13,fontWeight:700,color:T.gold}}>New Patient Tracer</div>
      </div>

      {/* Select tracer type */}
      <div style={{fontSize:9,color:T.muted,marginBottom:8,letterSpacing:1}}>SELECT TRACER TYPE</div>
      <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(140px,1fr))",gap:8,marginBottom:18}}>
        {Object.entries(TRACER_TYPES).map(([type,data])=>(
          <div key={type} onClick={()=>setTracerType(type)} style={{background:tracerType===type?`${data.color}15`:T.panel,border:`1px solid ${tracerType===type?data.color:T.border}`,borderRadius:9,padding:"10px",cursor:"pointer",textAlign:"center"}}>
            <div style={{fontSize:18,marginBottom:4}}>{data.icon}</div>
            <div style={{fontSize:10,fontWeight:700,color:tracerType===type?data.color:T.text}}>{type}</div>
            <div style={{fontSize:8,color:T.muted,marginTop:2}}>{data.questions.length}Q</div>
          </div>
        ))}
      </div>

      {/* Meta info */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:16,marginBottom:14}}>
        <div style={{fontSize:11,fontWeight:700,color:T.gold,marginBottom:12}}>Tracer Details (Optional)</div>
        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
          <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>PATIENT REF / FILE NO.</div><input style={inp} placeholder="e.g. IPD/2026/1234" value={meta.patient_ref} onChange={e=>setMeta(m=>({...m,patient_ref:e.target.value}))}/></div>
          <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>CONDUCTED BY</div><input style={inp} placeholder="Name / Designation" value={meta.conducted_by} onChange={e=>setMeta(m=>({...m,conducted_by:e.target.value}))}/></div>
          <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>DATE</div><input style={inp} type="date" value={meta.conducted_date} onChange={e=>setMeta(m=>({...m,conducted_date:e.target.value}))}/></div>
          <div><div style={{fontSize:9,color:T.muted,marginBottom:4}}>NOTES</div><input style={inp} placeholder="Any observations…" value={meta.notes} onChange={e=>setMeta(m=>({...m,notes:e.target.value}))}/></div>
        </div>
      </div>

      <button onClick={startConduct} style={{width:"100%",padding:"12px",borderRadius:10,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:13,fontWeight:700,cursor:"pointer"}}>
        Start {tracerType} Tracer ({TRACER_TYPES[tracerType].questions.length} questions) →
      </button>
    </div>
  );

  // CONDUCT TRACER — answer questions
  if(view==="conduct"){
    const tdata=TRACER_TYPES[tracerType];
    const answered=tdata.questions.filter(q=>responses[q.id]).length;
    const pct=calcScore();

    return(
      <div>
        <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:12,flexWrap:"wrap"}}>
          <button onClick={()=>setView("new")} style={{padding:"4px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:10,cursor:"pointer"}}>← Back</button>
          <div style={{flex:1}}>
            <div style={{fontSize:13,fontWeight:700,color:tdata.color}}>{tdata.icon} {tracerType}</div>
            <div style={{fontSize:9,color:T.muted}}>{answered}/{tdata.questions.length} answered · Score: {pct}%</div>
          </div>
          <button onClick={saveTracer} disabled={saving} style={{padding:"7px 16px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:11,fontWeight:700,cursor:"pointer",opacity:saving?0.6:1}}>{saving?"Saving…":"Save & Finish"}</button>
        </div>

        {/* Progress bar */}
        <div style={{background:T.border,borderRadius:4,height:6,marginBottom:16}}>
          <div style={{height:6,borderRadius:4,background:`linear-gradient(90deg,${tdata.color},${T.gold})`,width:`${(answered/tdata.questions.length)*100}%`,transition:"width 0.3s"}}/>
        </div>

        <div style={{display:"grid",gap:8}}>
          {tdata.questions.map((q,idx)=>{
            const resp=responses[q.id];
            return(
              <div key={q.id} style={{background:T.panel,border:`1px solid ${resp?"#0f2640":T.border}`,borderRadius:10,padding:"12px 16px"}}>
                <div style={{display:"flex",gap:10,alignItems:"flex-start"}}>
                  <div style={{width:22,height:22,borderRadius:11,background:resp==="yes"?T.greenD:resp==="partial"?T.orangeD:resp==="no"?T.redD:T.panel2,border:`1px solid ${resp==="yes"?T.green:resp==="partial"?T.orange:resp==="no"?T.red:T.border}`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:9,fontWeight:700,color:resp==="yes"?T.green:resp==="partial"?T.orange:resp==="no"?T.red:T.muted,flexShrink:0,marginTop:1}}>{idx+1}</div>
                  <div style={{flex:1}}>
                    <div style={{fontSize:11,color:T.white,lineHeight:1.5,marginBottom:8}}>{q.q}</div>
                    <div style={{fontSize:8,color:T.muted,marginBottom:8}}>OE: {q.oe}</div>
                    <div style={{display:"flex",gap:8}}>
                      {[["yes","✓ Yes",T.green],["partial","~ Partial",T.orange],["no","✗ No",T.red]].map(([val,label,color])=>(
                        <button key={val} onClick={()=>setResp(q.id,resp===val?null:val)}
                          style={{padding:"5px 14px",borderRadius:7,border:`1px solid ${resp===val?color:T.border}`,background:resp===val?`${color}20`:"transparent",color:resp===val?color:T.muted,fontSize:10,fontWeight:resp===val?700:400,cursor:"pointer"}}>
                          {label}
                        </button>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        <div style={{marginTop:16,background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"14px 18px",display:"flex",justifyContent:"space-between",alignItems:"center"}}>
          <div>
            <div style={{fontSize:11,color:T.text}}>{answered} of {tdata.questions.length} questions answered</div>
            <div style={{fontSize:9,color:T.muted,marginTop:2}}>Score: <span style={{color:scoreColor(pct),fontWeight:700}}>{pct}%</span> — {pct>=80?"Ready for assessment":pct>=60?"Needs improvement":"Critical gaps found"}</div>
          </div>
          <button onClick={saveTracer} disabled={saving} style={{padding:"9px 22px",borderRadius:9,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:12,fontWeight:700,cursor:"pointer",opacity:saving?0.6:1}}>{saving?"Saving…":"Save & Finish"}</button>
        </div>
      </div>
    );
  }

  return null;
}
