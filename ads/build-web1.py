"""Build web-notes.html — website loop video #1 (quality/control angle):
interview -> feedback -> NEW saved-text scene (AI fills the brackets).
1080x1350, flat --paper background (no glows/grid) so it blends
seamlessly into the homepage. Loops via fade-to-cream at the end."""
from pathlib import Path

src = Path("ad2-quality.html").read_text(encoding="utf-8")

css_end = src.index("</style>")
head = src[:css_end]
head = head.replace("<title>eleanote — ad 2 v2 (quality notes) 1080x1350</title>",
                    "<title>eleanote — web loop 1: notes your way 1080x1350</title>")
head = head.replace("ELEANOTE AD #2 v2 — QUALITY-NOTES ANGLE", "ELEANOTE WEB LOOP #1 — NOTES YOUR WAY")
# flat background: kill the dot grid
head = head.replace("""#canvas::before {
  content: "";
  position: absolute; inset: 0;
  background-image: radial-gradient(rgba(13,43,48,0.05) 1.5px, transparent 1.5px);
  background-size: 30px 30px;
  pointer-events: none;
}""", "")

st_css = """
/* ---------- saved-text scene ---------- */
.st-win {
  position: absolute;
  left: 70px; top: 200px;
  width: 940px;
  background: var(--paper);
  border: 1px solid rgba(0,0,0,0.16);
  border-radius: 18px;
  box-shadow: 0 34px 90px rgba(13,43,48,0.26);
  overflow: hidden;
  text-align: left;
  will-change: transform, opacity;
}
.st-titlebar { background: var(--paper-2); border-bottom: 1px solid var(--line); height: 60px; display: flex; align-items: center; gap: 14px; padding: 0 24px; position: relative; }
.st-mark { width: 32px; height: 32px; border-radius: 50%; background: var(--teal); color: #fff; font-size: 21px; font-weight: 800; letter-spacing: -0.06em; display: inline-flex; align-items: center; justify-content: center; }
.st-titletext { position: absolute; left: 50%; transform: translateX(-50%); font-size: 25px; font-weight: 700; color: var(--ink); }
.st-winctl { margin-left: auto; display: inline-flex; gap: 8px; }
.st-winctl span { width: 15px; height: 15px; border-radius: 50%; background: rgba(0,0,0,0.16); }
.st-body { padding: 22px 28px 24px; }
.st-labelrow { display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; }
.st-label { font-size: 27px; font-weight: 700; color: var(--ink); }
.st-mode {
  font-size: 20px; font-weight: 700;
  color: var(--teal-deep);
  background: rgba(20,81,92,0.09);
  border: 1.5px solid rgba(20,81,92,0.28);
  border-radius: 999px;
  padding: 8px 18px;
}
.st-text { font-size: 26px; line-height: 1.75; color: #26393e; }
.brk {
  display: inline-block;
  color: #a06b12;
  background: rgba(240, 164, 74, 0.14);
  border: 1.5px dashed rgba(160, 107, 18, 0.5);
  border-radius: 8px;
  padding: 1px 12px;
  font-weight: 600;
  will-change: transform, box-shadow;
}
.brk.filled {
  color: #1a5fae;
  background: rgba(78, 163, 255, 0.13);
  border: 1.5px solid rgba(78, 163, 255, 0.5);
  border-style: solid;
  font-weight: 700;
}
/* note window the phrase lands in */
.stn-win {
  position: absolute;
  left: 70px; top: 560px;
  width: 940px;
  background: var(--paper);
  border: 1px solid rgba(0,0,0,0.16);
  border-radius: 18px;
  box-shadow: 0 34px 90px rgba(13,43,48,0.26);
  overflow: hidden;
  text-align: left;
  will-change: transform, opacity;
}
.stn-head { background: var(--paper-2); border-bottom: 1px solid var(--line); padding: 16px 28px; font-size: 22px; font-weight: 800; letter-spacing: 0.1em; color: var(--teal-deep); }
.stn-body { padding: 22px 28px 26px; min-height: 420px; }
.stn-pre { font-size: 25px; line-height: 1.7; color: var(--emr-muted); margin-bottom: 14px; }
.stn-target { font-size: 26px; line-height: 1.75; color: #26393e; opacity: 0; will-change: opacity, transform; }
"""
head = head + st_css + "\n</style>\n</head>\n"

body = """<body>
<div id="viewport">
<div id="canvas">

  <!-- SCENE 1 - INTERVIEW (0-8.8) -->
  <div class="beat" id="s1">
    <div class="scene-title kline" id="s1title">Tell it how <span class="serif">you write.</span></div>
    <div class="dp-app kline" id="dpApp">
      <div class="dp-titlebar">
        <span class="dp-mark">e</span>
        <span class="dp-titletext">Documentation Preferences</span>
        <span class="dp-winctl"><span></span><span></span><span></span></span>
      </div>
      <div class="dp-chat">
        <div class="dp-msg" id="dpM1">
          <div class="dp-who">ELEANOTE</div>
          <div class="dp-text">How do you like your assessment &amp; plan written?</div>
        </div>
        <div class="dp-msg user" id="dpU1">
          <div class="dp-inner">
            <div class="dp-who">YOU</div>
            <div class="dp-text">Problem-based. Number each problem, short bullet plans.</div>
          </div>
        </div>
        <div class="dp-msg" id="dpM2">
          <div class="dp-who">ELEANOTE</div>
          <div class="dp-text">Got it &mdash; numbered problems, bullet plans. How long should the HPI be?</div>
        </div>
        <div class="dp-msg user" id="dpU2">
          <div class="dp-inner">
            <div class="dp-who">YOU</div>
            <div class="dp-text">2&ndash;3 sentences. No fluff.</div>
          </div>
        </div>
        <div class="dp-msg" id="dpM3">
          <div class="dp-who">ELEANOTE</div>
          <div class="dp-text">Done &mdash; tight HPIs, problem-based A/P, bullet plans.</div>
          <div class="dp-saved" id="dpSaved">&#10003; Saved to your preferences</div>
        </div>
      </div>
      <div class="dp-inputrow">
        <div class="dp-input" id="dpInput"><span class="ph" id="dpPh">Type your response or paste a sample note&hellip;</span><span id="dpTyped"></span><span class="dp-caret" id="dpCaret"></span></div>
        <div class="dp-send" id="dpSend">Send</div>
      </div>
    </div>
    <div class="phase-chip" id="s1chip">a short interview &mdash; <span class="gold">your style, learned</span></div>
  </div>

  <!-- SCENE 2 - FEEDBACK (8.8-15.9) -->
  <div class="beat" id="s2">
    <div class="fb-cap kline" id="s2cap">Give feedback on <span class="serif">any note.</span></div>
    <div class="fb-app kline" id="fbApp">
      <div class="fb-titlebar">
        <span class="fb-mark">e</span>
        <span class="fb-titletext">eleanote</span>
        <span class="fb-winctl"><span></span><span></span><span></span></span>
      </div>
      <div class="fb-tabs"><span class="fb-tab">Doe, John &middot; 64M</span></div>
      <div class="fb-note">
        <div class="fb-sec">
          <div class="fb-sec-h">SUBJECTIVE</div>
          <div class="fb-sec-b">64M here for follow-up of RCC s/p partial nephrectomy. Feels well &mdash; no hematuria, no flank pain.</div>
        </div>
        <div class="fb-sec">
          <div class="fb-sec-h">OBJECTIVE</div>
          <div class="fb-sec-b">BP 128/78 &middot; exam unremarkable.</div>
        </div>
        <div class="fb-sec fb-assess">
          <div class="fb-sec-h">ASSESSMENT</div>
          <div class="fb-wordy" id="fbWordy">
            <div class="fb-sec-b">The patient is a 64-year-old male with a history of renal cell carcinoma status post partial nephrectomy in 2023 who presents today for routine oncologic surveillance and is found to be clinically stable without evidence of recurrence, along with chronic kidney disease stage 3 which remains stable, and essential hypertension which is well controlled on current therapy.</div>
          </div>
          <div class="fb-concise" id="fbConcise">
            <div class="fb-sec-b">RCC s/p partial nephrectomy &mdash; stable, no evidence of recurrence. CKD-3 stable. HTN controlled.</div>
          </div>
          <div class="fb-shimmer" id="fbShimmer"></div>
        </div>
        <div class="fb-sec">
          <div class="fb-sec-h">PLAN</div>
          <div class="fb-sec-b">1) MRI abdomen + BMP in 1 year &nbsp; 2) Continue lisinopril.</div>
        </div>
      </div>
      <div class="fb-inputrow">
        <div class="fb-input" id="fbInput"><span class="ph" id="fbPh">Give feedback on this note&hellip;</span><span id="fbTyped"></span><span class="fb-caret" id="fbCaret"></span></div>
        <div class="fb-btn" id="fbBtn">Apply feedback</div>
      </div>
    </div>
    <div class="fb-under kline" id="s2under">It <span class="serif">learns.</span> Every note gets better.</div>
  </div>

  <!-- SCENE 3 - SAVED TEXT (15.9-25.9) -->
  <div class="beat" id="s3">
    <div class="scene-title kline" id="s3title">Saved text &mdash; <span class="serif">filled in for you.</span></div>
    <div class="st-win kline" id="stWin">
      <div class="st-titlebar">
        <span class="st-mark">e</span>
        <span class="st-titletext">Saved Text</span>
        <span class="st-winctl"><span></span><span></span><span></span></span>
      </div>
      <div class="st-body">
        <div class="st-labelrow">
          <span class="st-label">Shared decision counseling</span>
          <span class="st-mode">AI fills the brackets</span>
        </div>
        <div class="st-text">Discussed <span class="brk">[diagnosis]</span> in detail, including <span class="brk">[options]</span>. Risks, benefits, and alternatives reviewed. Patient elects <span class="brk">[plan]</span> and verbalizes understanding.</div>
      </div>
    </div>
    <div class="stn-win kline" id="stnWin">
      <div class="stn-head">TODAY'S NOTE</div>
      <div class="stn-body">
        <div class="stn-pre">&hellip;exam unremarkable. Urinalysis with microscopic hematuria, CT with a 4&nbsp;mm distal ureteral stone.</div>
        <div class="stn-target" id="stnTarget">Discussed <span class="brk" id="bk1">[diagnosis]</span> in detail, including <span class="brk" id="bk2">[options]</span>. Risks, benefits, and alternatives reviewed. Patient elects <span class="brk" id="bk3">[plan]</span> and verbalizes understanding.</div>
      </div>
    </div>
    <div class="fly-chip" id="stFly" style="border-left-color:#f0a44a;"><span class="bullet"></span> counseling phrase</div>
    <div class="phase-chip" id="s3chip">your words &mdash; <span class="gold">AI fills the blanks</span></div>
  </div>

</div>
</div>
"""

engine = """
<script>
/* ================= ENGINE - web loop 1, 25.9s ================= */
var DUR = 25.9;
var RENDER = /[?&]render/.test(location.search);
var FREEZE = (function(){ var m = location.search.match(/[?&]t=([0-9.]+)/); return m ? parseFloat(m[1]) : null; })();
var E = {
  linear:  function(p){ return p; },
  outCubic:function(p){ return 1 - Math.pow(1 - p, 3); },
  inCubic: function(p){ return p * p * p; },
  inOut:   function(p){ return p < 0.5 ? 4*p*p*p : 1 - Math.pow(-2*p + 2, 3) / 2; },
  outBack: function(p){ var c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(p - 1, 3) + c1 * Math.pow(p - 1, 2); }
};
function kv(kfs, t) {
  if (t <= kfs[0][0]) return kfs[0][1];
  var last = kfs[kfs.length - 1];
  if (t >= last[0]) return last[1];
  for (var i = 1; i < kfs.length; i++) {
    if (t <= kfs[i][0]) {
      var a = kfs[i-1], b = kfs[i];
      return a[1] + (b[1] - a[1]) * E[b[2] || 'inOut']((t - a[0]) / (b[0] - a[0]));
    }
  }
  return last[1];
}
var $ = function(id){ return document.getElementById(id); };

var BEATS = [ ['s1', 0.0, 8.8], ['s2', 8.8, 15.9], ['s3', 15.9, 25.91] ];
function inout(el, tIn, tOut, yIn) {
  return { el: el,
    o: [[tIn, 0], [tIn + 0.35, 1, 'outCubic'], [tOut - 0.3, 1], [tOut, 0, 'inCubic']],
    y: [[tIn, yIn], [tIn + 0.4, 0, 'outCubic'], [tOut - 0.3, 0], [tOut, -26, 'inCubic']] };
}
var TRACKS = [
  /* scene 1 interview (ad2-v3 timings shifted -5.0) */
  inout('s1title', 0.05, 8.75, 36),
  { el:'dpApp', o:[[0.25,0],[0.70,1,'outCubic'],[8.45,1],[8.75,0,'inCubic']], y:[[0.25,66],[0.75,0,'outCubic']] },
  { el:'s1chip', o:[[7.15,0],[7.50,1,'outCubic'],[8.45,1],[8.75,0,'inCubic']], y:[[7.15,34],[7.55,0,'outBack']] },
  { el:'dpSend', s:[[2.82,1],[2.97,0.93,'outCubic'],[3.12,1,'outBack'],[5.50,1],[5.65,0.93,'outCubic'],[5.80,1,'outBack']] },
  /* scene 2 feedback (ad2-v3 timings shifted -5.1) */
  { el:'s2cap', o:[[8.85,0],[9.20,1,'outCubic'],[15.52,1],[15.85,0,'inCubic']], y:[[8.85,40],[9.25,0,'outCubic'],[15.52,0],[15.85,-26,'inCubic']] },
  { el:'fbApp', o:[[8.92,0],[9.32,1,'outCubic'],[15.52,1],[15.85,0,'inCubic']], y:[[8.92,66],[9.38,0,'outCubic'],[15.52,0],[15.85,-26,'inCubic']], s:[[8.92,0.97],[9.38,1,'outCubic'],[13.8,1],[14.3,1.006,'inOut']] },
  { el:'fbBtn', s:[[11.20,1],[11.36,0.93,'outCubic'],[11.52,1,'outBack']] },
  { el:'s2under', o:[[13.45,0],[13.85,1,'outCubic'],[15.52,1],[15.85,0,'inCubic']], y:[[13.45,42],[13.90,0,'outBack'],[15.52,0],[15.85,-26,'inCubic']] },
  /* scene 3 saved text */
  inout('s3title', 15.95, 25.55, 36),
  { el:'stWin', o:[[16.15,0],[16.60,1,'outCubic'],[25.25,1],[25.55,0,'inCubic']], y:[[16.15,60],[16.65,0,'outCubic']] },
  { el:'stnWin', o:[[16.85,0],[17.30,1,'outCubic'],[25.25,1],[25.55,0,'inCubic']], y:[[16.85,60],[17.35,0,'outCubic']] },
  { el:'s3chip', o:[[23.65,0],[24.00,1,'outCubic'],[25.25,1],[25.55,0,'inCubic']], y:[[23.65,34],[24.05,0,'outBack']] }
];

var DP_MSGS = [ ['dpM1', 1.0], ['dpU1', 3.12], ['dpM2', 3.85], ['dpU2', 5.80], ['dpM3', 6.55] ];
var DP_T1 = { text: 'Problem-based. Number each problem, short bullet plans.', t0: 1.7, t1: 2.72 };
var DP_T2 = { text: '2-3 sentences. No fluff.', t0: 4.75, t1: 5.40 };
var TYPE_TEXT = 'Make the assessment more concise';

/* saved-text fills */
var ST_FILLS = [
  ['bk1', 20.3, 'a 4 mm distal ureteral stone'],
  ['bk2', 21.5, 'observation vs. ureteroscopy'],
  ['bk3', 22.7, 'a trial of passage with a strainer']
];
var ST_FLY = { x0: 540, y0: 430, x1: 400, y1: 745, t0: 18.0, t1: 18.7 };

function applySpecials(t) {
  /* ===== scene 1 ===== */
  if (t < 9.0) {
    for (var i = 0; i < DP_MSGS.length; i++) {
      var m = $(DP_MSGS[i][0]), mt = DP_MSGS[i][1];
      m.style.opacity = kv([[mt,0],[mt+0.35,1,'outCubic']], t);
      m.style.transform = 'translateY(' + kv([[mt,20],[mt+0.4,0,'outCubic']], t) + 'px)';
    }
    var typing1 = t >= DP_T1.t0 && t < 3.08;
    var typing2 = t >= DP_T2.t0 && t < 5.76;
    $('dpInput').className = (t >= 1.5 && t < 5.85) ? 'dp-input focus' : 'dp-input';
    var want = '';
    if (typing1) want = DP_T1.text.slice(0, Math.floor(Math.min(1, (t - DP_T1.t0) / (DP_T1.t1 - DP_T1.t0)) * DP_T1.text.length));
    else if (typing2) want = DP_T2.text.slice(0, Math.floor(Math.min(1, (t - DP_T2.t0) / (DP_T2.t1 - DP_T2.t0)) * DP_T2.text.length));
    var te = $('dpTyped');
    if (te.textContent !== want) te.textContent = want;
    $('dpPh').style.opacity = (t >= 1.5 && t < 5.85) ? (want ? 0 : 0.55) : 1;
    var caretOn = (t >= 1.5 && t < 5.80) && !(t >= 3.08 && t < 4.70) && (Math.floor(t * 2.5) % 2 === 0);
    $('dpCaret').style.opacity = caretOn ? 1 : 0;
    var sv = $('dpSaved');
    sv.style.opacity = kv([[6.90,0],[7.20,1,'outCubic']], t);
    sv.style.transform = 'scale(' + kv([[6.90,0.7],[7.30,1,'outBack']], t) + ')';
  }
  /* ===== scene 2 ===== */
  if (t > 8.6 && t < 16.1) {
    $('fbInput').className = (t >= 9.75 && t < 15.5) ? 'fb-input focus' : 'fb-input';
    $('fbPh').style.opacity = t < 9.85 ? 1 : Math.max(0, 1 - (t - 9.85) / 0.15);
    var p = Math.min(1, Math.max(0, (t - 10.0) / 0.9));
    var wantF = TYPE_TEXT.slice(0, Math.floor(p * TYPE_TEXT.length));
    var typedEl = $('fbTyped');
    if (typedEl.textContent !== wantF) typedEl.textContent = wantF;
    var caretOnF = (t >= 9.75 && t <= 11.55) && (Math.floor(t * 2.5) % 2 === 0);
    $('fbCaret').style.opacity = caretOnF ? 1 : 0;
    var btn = $('fbBtn');
    var label = t < 11.4 ? 'Apply feedback' : (t < 12.9 ? 'Rewriting…' : 'Done ✓');
    if (btn.textContent !== label) btn.textContent = label;
    $('fbWordy').style.maxHeight = kv([[11.8,300],[12.65,0,'inOut']], t) + 'px';
    $('fbWordy').style.opacity = kv([[11.8,1],[12.45,0,'linear']], t);
    $('fbConcise').style.maxHeight = kv([[12.25,0],[12.85,110,'inOut']], t) + 'px';
    $('fbConcise').style.opacity = kv([[12.35,0],[12.85,1,'linear']], t);
    var sh = $('fbShimmer');
    sh.style.opacity = kv([[11.7,0],[11.95,1,'linear'],[13.0,1],[13.35,0,'linear']], t);
    sh.style.backgroundPosition = kv([[11.75,140],[13.25,-140,'linear']], t) + '% 0';
  }
  /* ===== scene 3 saved text ===== */
  if (t > 15.7) {
    /* the phrase chip flies from the Saved Text window into the note */
    var f = $('stFly');
    var on = t >= ST_FLY.t0 && t <= ST_FLY.t1 + 0.05;
    f.style.opacity = on ? kv([[ST_FLY.t0,0],[ST_FLY.t0+0.12,1,'linear'],[ST_FLY.t1-0.06,1],[ST_FLY.t1+0.02,0,'linear']], t) : 0;
    if (on) {
      var x = kv([[ST_FLY.t0, ST_FLY.x0],[ST_FLY.t1, ST_FLY.x1,'inOut']], t);
      var y = kv([[ST_FLY.t0, ST_FLY.y0],[ST_FLY.t1, ST_FLY.y1,'inOut']], t);
      var s = kv([[ST_FLY.t0,1],[ST_FLY.t0+0.2,1.07,'outCubic'],[ST_FLY.t1,0.88,'inOut']], t);
      f.style.transform = 'translate(' + (x - 110) + 'px,' + (y - 26) + 'px) scale(' + s + ')';
    }
    /* the phrase text lands in the note (brackets intact) */
    var tg = $('stnTarget');
    tg.style.opacity = kv([[18.6,0],[18.95,1,'outCubic']], t);
    tg.style.transform = 'translateY(' + kv([[18.6,14],[19.0,0,'outCubic']], t) + 'px)';
    /* each bracket pulses, then fills with AI-blue text */
    for (var k = 0; k < ST_FILLS.length; k++) {
      var el = $(ST_FILLS[k][0]);
      var ft = ST_FILLS[k][1];
      var pulse = kv([[ft-0.45,0],[ft-0.2,1,'outCubic'],[ft+0.15,0,'inCubic']], t);
      el.style.boxShadow = '0 0 0 ' + (5 * pulse) + 'px rgba(78, 163, 255, ' + (0.22 * pulse) + ')';
      var filled = t >= ft;
      if (filled && el.className !== 'brk filled') { el.className = 'brk filled'; el.textContent = ST_FILLS[k][2]; }
      if (!filled && el.className !== 'brk') { el.className = 'brk'; el.textContent = ['[diagnosis]','[options]','[plan]'][k]; }
      var pop = kv([[ft,0.94],[ft+0.3,1,'outBack']], t);
      el.style.transform = filled ? ('scale(' + pop + ')') : '';
    }
  }
  /* loop fade: whole canvas dips to cream at the very end */
  var fade = kv([[25.45,0],[25.88,1,'linear']], t);
  var veil = $('loopVeil');
  veil.style.opacity = fade;
}

function seek(t) {
  t = Math.max(0, Math.min(DUR, t));
  for (var i = 0; i < BEATS.length; i++) {
    var b = BEATS[i];
    document.getElementById(b[0]).style.visibility = (t >= b[1] && t < b[2]) ? 'visible' : 'hidden';
  }
  for (var j = 0; j < TRACKS.length; j++) {
    var tr = TRACKS[j];
    var el = tr._el || (tr._el = $(tr.el));
    if (tr.o) el.style.opacity = kv(tr.o, t);
    var parts = '';
    if (tr.x) parts += 'translateX(' + kv(tr.x, t) + 'px) ';
    if (tr.y) parts += 'translateY(' + kv(tr.y, t) + 'px) ';
    if (tr.s) parts += 'scale(' + kv(tr.s, t) + ') ';
    if (parts) {
      if (tr.el === 's1chip' || tr.el === 's3chip') parts = 'translateX(-50%) ' + parts;
      el.style.transform = parts;
    }
  }
  applySpecials(t);
}

function fitPreview() {
  if (RENDER) return;
  var sc = Math.min(window.innerWidth / 1080, window.innerHeight / 1350) * 0.98;
  $('canvas').style.transform = 'scale(' + sc + ')';
}
function boot() {
  if (RENDER) document.body.classList.add('render');
  var veil = document.createElement('div');
  veil.id = 'loopVeil';
  veil.style.cssText = 'position:absolute;inset:0;background:var(--paper);opacity:0;pointer-events:none;z-index:200;';
  $('canvas').appendChild(veil);
  seek(FREEZE != null ? FREEZE : 0);
  fitPreview();
  window.addEventListener('resize', fitPreview);
  window.__ready = true;
  if (!RENDER && FREEZE == null) {
    var start = performance.now();
    (function loop(now){
      seek(((now - start) / 1000) % DUR);
      requestAnimationFrame(loop);
    })(start);
  }
}
window.__total = DUR;
window.__seek = function(t){ seek(t); };
if (document.fonts && document.fonts.ready) {
  document.fonts.ready.then(function(){ setTimeout(boot, 60); });
} else {
  window.addEventListener('load', function(){ setTimeout(boot, 120); });
}
</script>
</body>
</html>
"""

Path("web-notes.html").write_text(head + body + engine, encoding="utf-8")
print("web-notes.html written:", len(head + body + engine), "chars")
