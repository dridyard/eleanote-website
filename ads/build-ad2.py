"""Build ad2-quality.html from ad1-v3.html: shared chrome kept, beats replaced."""
from pathlib import Path

src = Path("ad1-v3.html").read_text(encoding="utf-8")

css_end = src.index("</style>")
head = src[:css_end]
head = head.replace("<title>eleanote — ad 1 v3 (all-custom scenes) 1080x1350</title>",
                    "<title>eleanote — ad 2 (quality notes) 1080x1350</title>")
head = head.replace("ELEANOTE AD #1 v3", "ELEANOTE AD #2 — QUALITY-NOTES ANGLE")

ad2_css = """
/* ---------- ad2: Documentation Preferences interview window ---------- */
.dp-app {
  position: absolute;
  left: 70px; top: 205px;
  width: 940px;
  background: var(--paper);
  border: 1px solid rgba(0,0,0,0.16);
  border-radius: 18px;
  box-shadow: 0 40px 110px rgba(13,43,48,0.28);
  overflow: hidden;
  text-align: left;
  will-change: transform, opacity;
}
.dp-titlebar { background: var(--paper-2); border-bottom: 1px solid var(--line); height: 64px; display: flex; align-items: center; gap: 16px; padding: 0 24px; position: relative; }
.dp-mark { width: 34px; height: 34px; border-radius: 50%; background: var(--teal); color: #fff; font-size: 22px; font-weight: 800; letter-spacing: -0.06em; display: inline-flex; align-items: center; justify-content: center; }
.dp-titletext { position: absolute; left: 50%; transform: translateX(-50%); font-size: 26px; font-weight: 700; color: var(--ink); white-space: nowrap; }
.dp-winctl { margin-left: auto; display: inline-flex; gap: 9px; }
.dp-winctl span { width: 16px; height: 16px; border-radius: 50%; background: rgba(0,0,0,0.16); }
.dp-chat { padding: 26px 30px 12px; height: 640px; }
.dp-msg { margin-bottom: 24px; opacity: 0; will-change: transform, opacity; }
.dp-who { font-size: 20px; font-weight: 800; letter-spacing: 0.11em; color: var(--teal-deep); margin-bottom: 6px; }
.dp-text { font-size: 26px; line-height: 1.5; color: #26393e; }
.dp-msg.user .dp-inner { background: var(--paper-2); border: 1px solid var(--line); border-radius: 12px; padding: 16px 20px; }
.dp-msg.user .dp-who { color: var(--muted); }
.dp-saved {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  margin-top: 14px;
  background: rgba(47, 164, 107, 0.12);
  color: var(--ok);
  border: 1.5px solid rgba(47, 164, 107, 0.5);
  font-size: 22px;
  font-weight: 700;
  border-radius: 999px;
  padding: 9px 20px;
  opacity: 0;
  will-change: transform, opacity;
}
.dp-inputrow { display: flex; gap: 16px; padding: 18px 30px 22px; border-top: 1px solid var(--line); background: var(--warm-white); align-items: center; }
.dp-input { position: relative; white-space: nowrap; overflow: hidden; flex: 1; border: 2px solid var(--line); background: #fff; border-radius: 14px; padding: 18px 22px; font-size: 25px; color: var(--ink); min-height: 66px; display: flex; align-items: center; }
.dp-input.focus { border-color: var(--teal); box-shadow: 0 0 0 5px rgba(20,81,92,0.12); }
.dp-input .ph { color: #9aa5a0; position: absolute; left: 22px; top: 50%; transform: translateY(-50%); }
.dp-caret { display: inline-block; width: 3px; height: 31px; background: var(--teal-deep); margin-left: 3px; flex: 0 0 auto; opacity: 0; }
.dp-send { flex: 0 0 auto; background: var(--teal-deep); color: #fff; font-size: 25px; font-weight: 700; border-radius: 14px; padding: 19px 34px; will-change: transform; }

/* ---------- ad2: combined transfer scene ---------- */
.combo-label { font-size: 20px; font-weight: 800; letter-spacing: 0.11em; color: var(--emr-muted); margin: 0 0 10px; }
.combo-sec { margin-bottom: 22px; }
.combo-dxslot { min-height: 64px; }
.dx-pill-big {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: var(--emr-accent-soft);
  color: var(--emr-accent);
  font-size: 24px;
  font-weight: 700;
  border-radius: 999px;
  padding: 14px 24px;
  opacity: 0;
  will-change: transform, opacity, box-shadow;
}
.combo-noteslot {
  position: relative;
  height: 420px;
  border: 2px solid var(--emr-line);
  border-radius: 14px;
  background: #fff;
  padding: 22px 26px;
}
.combo-noteslot.hot { border-color: var(--emr-accent); box-shadow: 0 0 0 6px rgba(91, 75, 138, 0.14); }
.combo-noteslot .note-ph { position: absolute; left: 26px; top: 22px; font-size: 24px; color: #a2a9ba; font-style: italic; }
.combo-noteslot .note-typed { white-space: pre-line; font-size: 25px; line-height: 1.6; color: var(--emr-ink); will-change: opacity; }
"""
head = head + ad2_css + "\n</style>\n</head>\n"

body = """<body>
<div id="viewport">
<div id="canvas">
  <div class="bg-glow g1"></div>
  <div class="bg-glow g2"></div>

  <!-- BEAT 1 - HOOK (0-3.2) -->
  <div class="beat centered" id="b1">
    <div class="kline" id="b1l1" style="font-size:80px;">Is your AI scribe</div>
    <div class="kline" id="b1l2" style="font-size:80px;"><span class="accent-word" id="b1cp">still</span> not getting</div>
    <div class="kline" id="b1l3" style="font-size:80px;">your notes right?</div>
  </div>

  <!-- BEAT 2 - TURN (3.2-6.6) -->
  <div class="beat centered" id="b2">
    <div class="hud-pill kline" id="b2pill"><span class="dot"></span> eleanote</div>
    <div class="kline" id="b2l1"><span class="brandword">eleanote</span> writes them</div>
    <div class="kline" id="b2l2"><span class="serif">exactly the way you want.</span></div>
  </div>

  <!-- BEAT 3 - PREFERENCE INTERVIEW (6.6-17.4) -->
  <div class="beat" id="b3">
    <div class="scene-title kline" id="b3title">Tell it how <span class="serif">you write.</span></div>
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
    <div class="phase-chip" id="b3chip">a short interview &mdash; <span class="gold">your style, learned</span></div>
  </div>

  <!-- BEAT 7 - FEEDBACK (17.4-25.4) -->
  <div class="beat" id="b7">
    <div class="fb-cap kline" id="b7cap">Give feedback on <span class="serif">any note.</span></div>
    <div class="fb-app kline" id="b7app">
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
    <div class="fb-under kline" id="b7under">It <span class="serif">learns.</span> Every note gets better.</div>
  </div>

  <!-- BEAT 8 - ONE-SCREEN TRANSFER (25.4-35.6) -->
  <div class="beat" id="b8">
    <div class="scene-title kline" id="b8title">Then it enters <span class="serif">everything.</span></div>
    <div class="emr-win kline" id="b8win">
      <div class="emr-titlebar">
        <span class="emr-mark">EHR</span>
        <span class="emr-patient">Doe, John</span>
        <span class="emr-meta">64M &middot; MRN 10428501</span>
        <span class="emr-winctl"><span></span><span></span><span></span></span>
      </div>
      <div class="emr-tabs">
        <span class="emr-tab active">Encounter</span>
        <span class="emr-tab">Chart</span>
        <span class="emr-tab">Notes</span>
        <span class="emr-tab">Orders</span>
      </div>
      <div class="emr-body">
        <div class="combo-sec">
          <div class="combo-label">DIAGNOSES</div>
          <div class="combo-dxslot"><span class="dx-pill-big" id="cDx">&#10003; Renal cell carcinoma &middot; C64.9</span></div>
        </div>
        <div class="combo-sec">
          <div class="combo-label">ORDERS</div>
          <div class="order-row" id="cOrder" style="margin-top:0;">
            <span class="nm">BMP</span>
            <span class="mt">Lab &middot; 05/01/2027</span>
            <span class="badge" id="cOrderBadge">&#10003; Placed</span>
          </div>
        </div>
        <div class="combo-sec">
          <div class="combo-label">TODAY'S NOTE</div>
          <div class="combo-noteslot" id="cNoteField">
            <span class="note-ph" id="cNotePh">Click to begin note&hellip;</span>
            <span class="note-typed" id="cNoteText" style="opacity:0;">S: 64M RCC follow-up &mdash; feels well, no hematuria.
O: BP 128/78 &middot; exam unremarkable.
A/P:
1) RCC &mdash; stable. MRI abdomen in 1 year.
2) CKD-3 &mdash; stable. BMP in 1 year.</span>
          </div>
        </div>
      </div>
    </div>
    <div class="asst kline" id="b8asst">
      <div class="asst-pill"><span class="dot" id="b8dot"></span> eleanote <span class="x">&times;</span></div>
      <div class="asst-queue" id="b8queue">
        <div class="asst-item" id="qDx"><span class="bullet green"></span> RCC &middot; C64.9 <span class="hint">F6</span></div>
        <div class="asst-item" id="qOrd"><span class="bullet blue"></span> BMP &mdash; in 1 year <span class="hint">F6</span></div>
        <div class="asst-item" id="qNote"><span class="bullet"></span> Clinical note <span class="hint">F6</span></div>
      </div>
    </div>
    <div class="fly-chip" id="flyDx" style="border-left-color:#5fc787;"><span class="bullet" style="background:#5fc787;"></span> RCC &middot; C64.9</div>
    <div class="fly-chip blue" id="flyOrd"><span class="bullet"></span> BMP</div>
    <div class="fly-chip" id="flyNote"><span class="bullet"></span> Clinical note</div>
    <div class="phase-chip" id="b8chip">into any EHR &mdash; <span class="gold">no IT integration</span></div>
  </div>

  <!-- BEAT 9 - CTA (35.6-40.0) -->
  <div class="beat centered" id="b9">
    <div class="hud-pill kline" id="b9pill"><span class="dot"></span> eleanote</div>
    <div class="cta-word kline" id="b9word">eleanote</div>
    <div class="cta-tag kline" id="b9tag">The ambient AI scribe for any EHR</div>
    <div class="cta-free kline" id="b9free">Free while in testing &middot; Windows &amp; Mac</div>
    <div class="cta-url kline" id="b9url">eleanote.ai</div>
  </div>

</div>
</div>
"""

engine = """
<script>
/* ================= ENGINE - ad2, 40.0s ================= */
var DUR = 40.0;
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

var BEATS = [
  ['b1', 0.0, 3.2], ['b2', 3.2, 6.6], ['b3', 6.6, 17.4],
  ['b7', 17.4, 25.4], ['b8', 25.4, 35.6], ['b9', 35.6, 40.01]
];
function inout(el, tIn, tOut, yIn) {
  return { el: el,
    o: [[tIn, 0], [tIn + 0.35, 1, 'outCubic'], [tOut - 0.3, 1], [tOut, 0, 'inCubic']],
    y: [[tIn, yIn], [tIn + 0.4, 0, 'outCubic'], [tOut - 0.3, 0], [tOut, -26, 'inCubic']] };
}
var TRACKS = [
  { el:'b1l1', o:[[0.05,0],[0.38,1,'outCubic'],[2.85,1],[3.15,0,'inCubic']], y:[[0.05,64],[0.42,0,'outBack'],[2.85,0],[3.15,-44,'inCubic']] },
  { el:'b1l2', o:[[0.45,0],[0.78,1,'outCubic'],[2.85,1],[3.15,0,'inCubic']], y:[[0.45,64],[0.82,0,'outBack'],[2.85,0],[3.15,-44,'inCubic']] },
  { el:'b1l3', o:[[0.85,0],[1.18,1,'outCubic'],[2.85,1],[3.15,0,'inCubic']], y:[[0.85,64],[1.22,0,'outBack'],[2.85,0],[3.15,-44,'inCubic']] },
  { el:'b1cp', r:[[1.35,0],[1.44,-2.6,'linear'],[1.53,2.2,'linear'],[1.62,-1.7,'linear'],[1.71,1.1,'linear'],[1.80,0,'linear']],
               x:[[1.35,0],[1.44,-5,'linear'],[1.53,4,'linear'],[1.62,-3,'linear'],[1.71,2,'linear'],[1.80,0,'linear']] },
  { el:'b2pill', o:[[3.30,0],[3.65,1,'outCubic'],[6.25,1],[6.55,0,'inCubic']], y:[[3.30,-150],[3.75,0,'outBack'],[6.25,0],[6.55,-30,'inCubic']], s:[[3.30,0.75],[3.75,1,'outBack']] },
  { el:'b2l1', o:[[3.70,0],[4.05,1,'outCubic'],[6.25,1],[6.55,0,'inCubic']], y:[[3.70,54],[4.10,0,'outBack'],[6.25,0],[6.55,-40,'inCubic']] },
  { el:'b2l2', o:[[3.95,0],[4.30,1,'outCubic'],[6.25,1],[6.55,0,'inCubic']], y:[[3.95,54],[4.35,0,'outBack'],[6.25,0],[6.55,-40,'inCubic']] },
  inout('b3title', 6.65, 17.35, 36),
  { el:'dpApp', o:[[6.85,0],[7.30,1,'outCubic'],[17.05,1],[17.35,0,'inCubic']], y:[[6.85,66],[7.35,0,'outCubic']] },
  { el:'b3chip', o:[[15.40,0],[15.75,1,'outCubic'],[17.05,1],[17.35,0,'inCubic']], y:[[15.40,34],[15.80,0,'outBack']] },
  { el:'dpSend', s:[[10.45,1],[10.60,0.93,'outCubic'],[10.75,1,'outBack'],[13.75,1],[13.90,0.93,'outCubic'],[14.05,1,'outBack']] },
  { el:'b7cap', o:[[17.45,0],[17.80,1,'outCubic'],[25.02,1],[25.35,0,'inCubic']], y:[[17.45,40],[17.85,0,'outCubic'],[25.02,0],[25.35,-26,'inCubic']] },
  { el:'b7app', o:[[17.52,0],[17.92,1,'outCubic'],[25.02,1],[25.35,0,'inCubic']], y:[[17.52,66],[17.98,0,'outCubic'],[25.02,0],[25.35,-26,'inCubic']], s:[[17.52,0.97],[17.98,1,'outCubic'],[23.3,1],[23.8,1.006,'inOut']] },
  { el:'fbBtn', s:[[20.70,1],[20.86,0.93,'outCubic'],[21.02,1,'outBack']] },
  { el:'b7under', o:[[22.95,0],[23.35,1,'outCubic'],[25.02,1],[25.35,0,'inCubic']], y:[[22.95,42],[23.40,0,'outBack'],[25.02,0],[25.35,-26,'inCubic']] },
  inout('b8title', 25.45, 35.55, 36),
  { el:'b8win', o:[[25.60,0],[26.05,1,'outCubic'],[35.25,1],[35.55,0,'inCubic']], y:[[25.60,70],[26.10,0,'outCubic']] },
  { el:'b8asst', o:[[26.05,0],[26.40,1,'outCubic'],[35.25,1],[35.55,0,'inCubic']], y:[[26.05,-70],[26.50,0,'outBack']] },
  { el:'b8chip', o:[[33.30,0],[33.65,1,'outCubic'],[35.25,1],[35.55,0,'inCubic']], y:[[33.30,34],[33.70,0,'outBack']] },
  { el:'b9pill', o:[[35.70,0],[36.10,1,'outCubic']], y:[[35.70,-70],[36.20,0,'outBack']] },
  { el:'b9word', o:[[35.92,0],[36.32,1,'outCubic']], s:[[35.92,0.955],[36.40,1,'outCubic']] },
  { el:'b9tag',  o:[[36.20,0],[36.60,1,'outCubic']], y:[[36.20,30],[36.65,0,'outCubic']] },
  { el:'b9free', o:[[36.48,0],[36.88,1,'outCubic']], y:[[36.48,26],[36.92,0,'outCubic']] },
  { el:'b9url',  o:[[36.70,0],[37.10,1,'outCubic']], s:[[36.70,0.85],[37.20,1,'outBack'],[37.80,1],[38.15,1.05,'inOut'],[38.55,1,'inOut']] }
];

var DP_MSGS = [
  ['dpM1', 7.6], ['dpU1', 10.75], ['dpM2', 11.5], ['dpU2', 14.05], ['dpM3', 14.8]
];
var DP_T1 = { text: 'Problem-based. Number each problem, short bullet plans.', t0: 8.3, t1: 10.35 };
var DP_T2 = { text: '2-3 sentences. No fluff.', t0: 12.4, t1: 13.7 };

var FDX  = { x0: 866, y0: 372, x1: 300, y1: 470, t0: 26.9, t1: 27.6 };
var FORD = { x0: 866, y0: 372, x1: 300, y1: 610, t0: 29.4, t1: 30.1 };
var FNOTE= { x0: 866, y0: 372, x1: 320, y1: 790, t0: 31.6, t1: 32.3 };
function applyF(el, F, t) {
  var on = t >= F.t0 && t <= F.t1 + 0.05;
  el.style.opacity = on ? kv([[F.t0,0],[F.t0+0.14,1,'linear'],[F.t1-0.07,1],[F.t1+0.02,0,'linear']], t) : 0;
  if (on) {
    var x = kv([[F.t0, F.x0],[F.t1, F.x1,'inOut']], t);
    var y = kv([[F.t0, F.y0],[F.t1, F.y1,'inOut']], t);
    var s = kv([[F.t0,1],[F.t0+0.22,1.07,'outCubic'],[F.t1,0.86,'inOut']], t);
    el.style.transform = 'translate(' + (x - 90) + 'px,' + (y - 26) + 'px) scale(' + s + ')';
  }
}
function collapseItem(el, t0, t) {
  el.style.opacity = kv([[t0,1],[t0+0.3,0,'inCubic']], t);
  el.style.maxHeight = kv([[t0,60],[t0+0.4,0,'inOut']], t) + 'px';
  el.style.paddingTop = el.style.paddingBottom = kv([[t0,15],[t0+0.4,0,'inOut']], t) + 'px';
}

var TYPE_TEXT = 'Make the assessment more concise';
function applySpecials(t) {
  if (t > 6.4 && t < 17.6) {
    for (var i = 0; i < DP_MSGS.length; i++) {
      var m = $(DP_MSGS[i][0]), mt = DP_MSGS[i][1];
      m.style.opacity = kv([[mt,0],[mt+0.35,1,'outCubic']], t);
      m.style.transform = 'translateY(' + kv([[mt,20],[mt+0.4,0,'outCubic']], t) + 'px)';
    }
    var typing1 = t >= DP_T1.t0 && t < 10.7;
    var typing2 = t >= DP_T2.t0 && t < 14.0;
    $('dpInput').className = (t >= 8.1 && t < 14.1) ? 'dp-input focus' : 'dp-input';
    var want = '';
    if (typing1) {
      var p1 = Math.min(1, (t - DP_T1.t0) / (DP_T1.t1 - DP_T1.t0));
      want = DP_T1.text.slice(0, Math.floor(p1 * DP_T1.text.length));
    } else if (typing2) {
      var p2 = Math.min(1, (t - DP_T2.t0) / (DP_T2.t1 - DP_T2.t0));
      want = DP_T2.text.slice(0, Math.floor(p2 * DP_T2.text.length));
    }
    var te = $('dpTyped');
    if (te.textContent !== want) te.textContent = want;
    $('dpPh').style.opacity = (t >= 8.1 && t < 14.1) ? (want ? 0 : 0.55) : 1;
    var caretOn = (t >= 8.1 && t < 14.05) && !(t >= 10.7 && t < 12.35) && (Math.floor(t * 2.5) % 2 === 0);
    $('dpCaret').style.opacity = caretOn ? 1 : 0;
    var sv = $('dpSaved');
    sv.style.opacity = kv([[15.15,0],[15.45,1,'outCubic']], t);
    sv.style.transform = 'scale(' + kv([[15.15,0.7],[15.55,1,'outBack']], t) + ')';
  }
  if (t > 17.2 && t < 25.6) {
    $('fbInput').className = (t >= 18.35 && t < 25.0) ? 'fb-input focus' : 'fb-input';
    $('fbPh').style.opacity = t < 18.45 ? 1 : Math.max(0, 1 - (t - 18.45) / 0.15);
    var p = Math.min(1, Math.max(0, (t - 18.6) / 1.8));
    var wantF = TYPE_TEXT.slice(0, Math.floor(p * TYPE_TEXT.length));
    var typedEl = $('fbTyped');
    if (typedEl.textContent !== wantF) typedEl.textContent = wantF;
    var caretOnF = (t >= 18.35 && t <= 21.1) && (Math.floor(t * 2.5) % 2 === 0);
    $('fbCaret').style.opacity = caretOnF ? 1 : 0;
    var btn = $('fbBtn');
    var label = t < 20.9 ? 'Apply feedback' : (t < 22.4 ? 'Rewriting…' : 'Done ✓');
    if (btn.textContent !== label) btn.textContent = label;
    $('fbWordy').style.maxHeight = kv([[21.3,300],[22.15,0,'inOut']], t) + 'px';
    $('fbWordy').style.opacity = kv([[21.3,1],[21.95,0,'linear']], t);
    $('fbConcise').style.maxHeight = kv([[21.75,0],[22.35,110,'inOut']], t) + 'px';
    $('fbConcise').style.opacity = kv([[21.85,0],[22.35,1,'linear']], t);
    var sh = $('fbShimmer');
    sh.style.opacity = kv([[21.2,0],[21.45,1,'linear'],[22.5,1],[22.85,0,'linear']], t);
    sh.style.backgroundPosition = kv([[21.25,140],[22.75,-140,'linear']], t) + '% 0';
  }
  if (t > 25.2 && t < 35.8) {
    applyF($('flyDx'), FDX, t);
    applyF($('flyOrd'), FORD, t);
    applyF($('flyNote'), FNOTE, t);
    collapseItem($('qDx'), 26.85, t);
    collapseItem($('qOrd'), 29.35, t);
    collapseItem($('qNote'), 31.55, t);
    $('b8queue').style.opacity = kv([[31.9,1],[32.2,0,'inCubic']], t);
    var dx = $('cDx');
    dx.style.opacity = kv([[27.65,0],[28.0,1,'outCubic']], t);
    dx.style.transform = 'translateY(' + kv([[27.65,16],[28.05,0,'outBack']], t) + 'px)';
    var g1 = kv([[27.65,0],[27.95,1,'outCubic'],[28.6,1],[29.1,0,'inCubic']], t);
    dx.style.boxShadow = '0 0 0 ' + (5 * g1) + 'px rgba(47, 164, 107, ' + (0.16 * g1) + ')';
    var row = $('cOrder');
    row.style.opacity = kv([[30.15,0],[30.5,1,'outCubic']], t);
    row.style.transform = 'translateY(' + kv([[30.15,20],[30.55,0,'outCubic']], t) + 'px)';
    var badge = $('cOrderBadge');
    badge.style.opacity = kv([[30.7,0],[30.95,1,'outCubic']], t);
    badge.style.transform = 'scale(' + kv([[30.7,0.6],[31.05,1,'outBack']], t) + ')';
    var g2 = kv([[30.7,0],[30.95,1,'outCubic'],[31.3,1],[31.8,0,'inCubic']], t);
    row.style.boxShadow = '0 0 0 ' + (5 * g2) + 'px rgba(47, 164, 107, ' + (0.16 * g2) + ')';
    var nf = $('cNoteField');
    nf.className = (t >= 32.25 && t < 33.3) ? 'combo-noteslot hot' : 'combo-noteslot';
    $('cNotePh').style.opacity = kv([[32.25,1],[32.4,0,'linear']], t);
    $('cNoteText').style.opacity = kv([[32.35,0],[32.6,1,'outCubic']], t);
    $('b8dot').style.background = t < 32.4 ? '#38d27a' : '#9aa1ab';
    $('b8dot').style.boxShadow = t < 32.4 ? '0 0 0 5px rgba(56,210,122,0.22)' : 'none';
  }
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
    if (tr.r) parts += 'rotate(' + kv(tr.r, t) + 'deg) ';
    if (parts) {
      if (tr.el === 'b3chip' || tr.el === 'b8chip') parts = 'translateX(-50%) ' + parts;
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

Path("ad2-quality.html").write_text(head + body + engine, encoding="utf-8")
print("ad2-quality.html written:", len(head + body + engine), "chars")
