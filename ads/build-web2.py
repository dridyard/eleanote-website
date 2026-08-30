"""Build web-ehr.html — website loop video #2 (any-EMR automation):
prechart -> dx/order/note combo (with formatting mention) -> NEW
split-into-sections scene. 1080x1350, flat --paper background."""
from pathlib import Path

src = Path("ad2-quality.html").read_text(encoding="utf-8")

css_end = src.index("</style>")
head = src[:css_end]
head = head.replace("<title>eleanote — ad 2 v2 (quality notes) 1080x1350</title>",
                    "<title>eleanote — web loop 2: any EMR 1080x1350</title>")
head = head.replace("ELEANOTE AD #2 v2 — QUALITY-NOTES ANGLE", "ELEANOTE WEB LOOP #2 — ANY EMR")
head = head.replace("""#canvas::before {
  content: "";
  position: absolute; inset: 0;
  background-image: radial-gradient(rgba(13,43,48,0.05) 1.5px, transparent 1.5px);
  background-size: 30px 30px;
  pointer-events: none;
}""", "")

extra_css = """
/* ---------- prechart scene (prior note with highlight sweep) ---------- */
.prior-note { font-size: 26px; line-height: 1.75; color: var(--emr-ink); }
.prior-note .pl { display: inline; border-radius: 4px; padding: 2px 4px; margin: 0 -4px; }

/* ---------- split-into-sections scene ---------- */
.chunk-field {
  position: relative;
  border: 2px solid var(--emr-line);
  border-radius: 14px;
  background: #fff;
  padding: 20px 24px;
  margin-bottom: 20px;
}
.chunk-field.hot { border-color: var(--emr-accent); box-shadow: 0 0 0 6px rgba(91, 75, 138, 0.14); }
.chunk-field .cf-ph { position: absolute; left: 24px; top: 20px; font-size: 23px; color: #a2a9ba; font-style: italic; }
.chunk-field .cf-text { white-space: pre-line; font-size: 24px; line-height: 1.6; color: var(--emr-ink); opacity: 0; will-change: opacity; }
#cfHpi { height: 220px; }
#cfAp { height: 300px; }
"""
head = head + extra_css + "\n</style>\n</head>\n"

body = """<body>
<div id="viewport">
<div id="canvas">

  <!-- SCENE 1 - PRECHART (0-6.4) -->
  <div class="beat" id="s1">
    <div class="scene-title kline" id="s1title">It precharts from <span class="serif">prior notes.</span></div>
    <div class="emr-win kline" id="s1win" style="height: 900px;">
      <div class="emr-titlebar">
        <span class="emr-mark">EHR</span>
        <span class="emr-patient">Doe, John</span>
        <span class="emr-meta">64M &middot; MRN 10428501</span>
        <span class="emr-winctl"><span></span><span></span><span></span></span>
      </div>
      <div class="emr-tabs">
        <span class="emr-tab active">Notes</span>
        <span class="emr-tab">Chart</span>
        <span class="emr-tab">Orders</span>
        <span class="emr-tab">Diagnoses</span>
      </div>
      <div class="emr-body">
        <div class="emr-h-row"><h3>Office visit</h3><span class="d">06/12/2025 &middot; Dr. Carter</span></div>
        <div class="prior-note" id="priorNote">
          <span class="pl" id="pl1">64yo M, follow-up. RCC s/p partial nephrectomy 2023.</span><br>
          <span class="pl" id="pl2">CKD stage 3 stable, baseline Cr 1.5, GFR 48.</span><br>
          <span class="pl" id="pl3">HTN well-controlled on lisinopril 20 mg daily.</span><br>
          <span class="pl" id="pl4">No new symptoms today, exam unremarkable.</span><br>
          <span class="pl" id="pl5">Plan: continue current regimen and lisinopril.</span><br>
          <span class="pl" id="pl6">Surveillance MRI abdomen and BMP as scheduled.</span>
        </div>
      </div>
    </div>
    <div class="asst kline" id="s1asst" style="top: 520px;">
      <div class="asst-pill"><span class="dot"></span> eleanote <span class="x">&times;</span></div>
      <div class="asst-queue" id="s1queue" style="opacity:0;">
        <div class="asst-item"><span class="bullet green"></span> Precharted <span class="hint">&#10003;</span></div>
      </div>
    </div>
    <div class="fly-chip purple" id="s1fly"><span class="bullet"></span> prior note</div>
    <div class="phase-chip" id="s1chip">context added &mdash; <span class="gold">even in remote sessions</span></div>
  </div>

  <!-- SCENE 2 - EVERYTHING ENTERED (6.4-13.2) -->
  <div class="beat" id="s2">
    <div class="scene-title kline" id="s2title">Then it enters <span class="serif">everything.</span></div>
    <div class="emr-win kline" id="s2win">
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
            <span class="note-typed" id="cNoteText" style="opacity:0;"><b>SUBJECTIVE:</b> 64M RCC follow-up &mdash; feels well, no hematuria.
<b>OBJECTIVE:</b> BP 128/78 &middot; exam unremarkable.
<b>A/P:</b>
1) RCC &mdash; stable. MRI abdomen in 1 year.
2) CKD-3 &mdash; stable. BMP in 1 year.</span>
          </div>
        </div>
      </div>
    </div>
    <div class="asst kline" id="s2asst" style="top: 560px;">
      <div class="asst-pill"><span class="dot" id="s2dot"></span> eleanote <span class="x">&times;</span></div>
      <div class="asst-queue" id="s2queue">
        <div class="asst-item" id="qDx"><span class="bullet green"></span> RCC &middot; C64.9 <span class="hint">F6</span></div>
        <div class="asst-item" id="qOrd"><span class="bullet blue"></span> BMP &mdash; in 1 year <span class="hint">F6</span></div>
        <div class="asst-item" id="qNote"><span class="bullet"></span> Clinical note <span class="hint">F6</span></div>
      </div>
    </div>
    <div class="fly-chip" id="flyDx" style="border-left-color:#5fc787;"><span class="bullet" style="background:#5fc787;"></span> RCC &middot; C64.9</div>
    <div class="fly-chip blue" id="flyOrd"><span class="bullet"></span> BMP</div>
    <div class="fly-chip" id="flyNote"><span class="bullet"></span> Clinical note</div>
    <div class="phase-chip" id="s2chip">with your formatting &mdash; <span class="gold">bold and all</span></div>
  </div>

  <!-- SCENE 3 - SPLIT INTO SECTIONS (13.2-22.4) -->
  <div class="beat" id="s3">
    <div class="scene-title kline" id="s3title">Or split the note <span class="serif">into sections.</span></div>
    <div class="emr-win kline" id="s3win" style="height: 940px;">
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
        <div class="combo-label">HPI</div>
        <div class="chunk-field" id="cfHpi">
          <span class="cf-ph" id="cfHpiPh">Click to enter HPI&hellip;</span>
          <span class="cf-text" id="cfHpiText">64M with h/o RCC s/p partial nephrectomy presents for surveillance. Feels well &mdash; no hematuria, no flank pain.</span>
        </div>
        <div class="combo-label">ASSESSMENT &amp; PLAN</div>
        <div class="chunk-field" id="cfAp">
          <span class="cf-ph" id="cfApPh">Click to enter assessment &amp; plan&hellip;</span>
          <span class="cf-text" id="cfApText">1) RCC &mdash; stable, no recurrence. MRI abdomen in 1 year.
2) CKD-3 &mdash; stable. BMP in 1 year.
3) HTN &mdash; continue lisinopril.</span>
        </div>
      </div>
    </div>
    <div class="asst kline" id="s3asst" style="top: 640px;">
      <div class="asst-pill"><span class="dot" id="s3dot"></span> eleanote <span class="x">&times;</span></div>
      <div class="asst-queue" id="s3queue">
        <div class="asst-item" id="qHpi"><span class="bullet"></span> Note &mdash; HPI <span class="hint">F6</span></div>
        <div class="asst-item" id="qAp"><span class="bullet"></span> Note &mdash; A/P <span class="hint">F6</span></div>
      </div>
    </div>
    <div class="fly-chip" id="flyHpi"><span class="bullet"></span> HPI</div>
    <div class="fly-chip" id="flyAp"><span class="bullet"></span> Assessment &amp; Plan</div>
    <div class="phase-chip" id="s3chip">each section &mdash; <span class="gold">pasted into the right field</span></div>
  </div>

</div>
</div>
"""

engine = """
<script>
/* ================= ENGINE - web loop 2, 22.4s ================= */
var DUR = 22.4;
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

var BEATS = [ ['s1', 0.0, 6.4], ['s2', 6.4, 13.2], ['s3', 13.2, 22.41] ];
function inout(el, tIn, tOut, yIn) {
  return { el: el,
    o: [[tIn, 0], [tIn + 0.35, 1, 'outCubic'], [tOut - 0.3, 1], [tOut, 0, 'inCubic']],
    y: [[tIn, yIn], [tIn + 0.4, 0, 'outCubic'], [tOut - 0.3, 0], [tOut, -26, 'inCubic']] };
}
var TRACKS = [
  /* s1 prechart */
  inout('s1title', 0.05, 6.35, 36),
  { el:'s1win', o:[[0.20,0],[0.60,1,'outCubic'],[6.05,1],[6.35,0,'inCubic']], y:[[0.20,60],[0.65,0,'outCubic']] },
  { el:'s1asst', o:[[0.55,0],[0.90,1,'outCubic'],[6.05,1],[6.35,0,'inCubic']], y:[[0.55,-60],[1.00,0,'outBack']] },
  { el:'s1chip', o:[[3.85,0],[4.20,1,'outCubic'],[6.05,1],[6.35,0,'inCubic']], y:[[3.85,34],[4.25,0,'outBack']] },
  /* s2 combo */
  inout('s2title', 6.45, 13.15, 36),
  { el:'s2win', o:[[6.55,0],[6.90,1,'outCubic'],[12.85,1],[13.15,0,'inCubic']], y:[[6.55,60],[6.95,0,'outCubic']] },
  { el:'s2asst', o:[[6.80,0],[7.15,1,'outCubic'],[12.85,1],[13.15,0,'inCubic']], y:[[6.80,-60],[7.25,0,'outBack']] },
  { el:'s2chip', o:[[11.05,0],[11.40,1,'outCubic'],[12.85,1],[13.15,0,'inCubic']], y:[[11.05,34],[11.45,0,'outBack']] },
  /* s3 chunks */
  inout('s3title', 13.25, 22.05, 36),
  { el:'s3win', o:[[13.40,0],[13.80,1,'outCubic'],[21.75,1],[22.05,0,'inCubic']], y:[[13.40,60],[13.85,0,'outCubic']] },
  { el:'s3asst', o:[[13.75,0],[14.10,1,'outCubic'],[21.75,1],[22.05,0,'inCubic']], y:[[13.75,-60],[14.20,0,'outBack']] },
  { el:'s3chip', o:[[19.35,0],[19.70,1,'outCubic'],[21.75,1],[22.05,0,'inCubic']], y:[[19.35,34],[19.75,0,'outBack']] }
];

function straight(x0, y0, x1, y1, t0, t1) { return {x0:x0, y0:y0, x1:x1, y1:y1, t0:t0, t1:t1}; }
function applyF(el, F, t) {
  var on = t >= F.t0 && t <= F.t1 + 0.05;
  el.style.opacity = on ? kv([[F.t0,0],[F.t0+0.12,1,'linear'],[F.t1-0.06,1],[F.t1+0.02,0,'linear']], t) : 0;
  if (on) {
    var x = kv([[F.t0, F.x0],[F.t1, F.x1,'inOut']], t);
    var y = kv([[F.t0, F.y0],[F.t1, F.y1,'inOut']], t);
    var s = kv([[F.t0,1],[F.t0+0.18,1.07,'outCubic'],[F.t1,0.87,'inOut']], t);
    el.style.transform = 'translate(' + (x - 100) + 'px,' + (y - 26) + 'px) scale(' + s + ')';
  }
}
function collapseItem(el, t0, t) {
  el.style.opacity = kv([[t0,1],[t0+0.25,0,'inCubic']], t);
  el.style.maxHeight = kv([[t0,60],[t0+0.32,0,'inOut']], t) + 'px';
  el.style.paddingTop = el.style.paddingBottom = kv([[t0,15],[t0+0.32,0,'inOut']], t) + 'px';
}

/* s1: prior note (~420, 520) -> assistant queue (~880, 640) */
var F1  = straight(420, 520, 872, 640, 2.5, 3.3);
/* s2: assistant (~866, 700) -> dx slot / order row / note field */
var FDX  = straight(866, 700, 300, 470, 7.4, 7.85);
var FORD = straight(866, 700, 300, 610, 8.3, 8.75);
var FNOTE= straight(866, 700, 320, 790, 9.2, 9.65);
/* s3: assistant (~866, 610) -> HPI field / A&P field */
var FHPI = straight(866, 700, 330, 500, 14.9, 15.5);
var FAP  = straight(866, 700, 360, 800, 17.3, 17.9);

function applySpecials(t) {
  /* ===== s1 prechart ===== */
  if (t < 6.6) {
    for (var i = 1; i <= 6; i++) {
      var tOn = 0.9 + (i - 1) * 0.2;
      var a = kv([[tOn, 0], [tOn + 0.18, 1, 'linear']], t);
      $('pl' + i).style.background = 'rgba(91, 75, 138, ' + (0.28 * a) + ')';
    }
    applyF($('s1fly'), F1, t);
    $('s1queue').style.opacity = kv([[3.35,0],[3.65,1,'outCubic']], t);
    $('s1queue').style.transform = 'translateY(' + kv([[3.35,-18],[3.70,0,'outBack']], t) + 'px)';
  }
  /* ===== s2 combo ===== */
  if (t > 6.2 && t < 13.4) {
    applyF($('flyDx'), FDX, t);
    applyF($('flyOrd'), FORD, t);
    applyF($('flyNote'), FNOTE, t);
    collapseItem($('qDx'), 7.35, t);
    collapseItem($('qOrd'), 8.25, t);
    collapseItem($('qNote'), 9.15, t);
    $('s2queue').style.opacity = kv([[9.5,1],[9.8,0,'inCubic']], t);
    var dx = $('cDx');
    dx.style.opacity = kv([[7.9,0],[8.2,1,'outCubic']], t);
    dx.style.transform = 'translateY(' + kv([[7.9,14],[8.25,0,'outBack']], t) + 'px)';
    var g1 = kv([[7.9,0],[8.15,1,'outCubic'],[8.55,1],[8.95,0,'inCubic']], t);
    dx.style.boxShadow = '0 0 0 ' + (5 * g1) + 'px rgba(47, 164, 107, ' + (0.16 * g1) + ')';
    var row = $('cOrder');
    row.style.opacity = kv([[8.78,0],[9.08,1,'outCubic']], t);
    row.style.transform = 'translateY(' + kv([[8.78,16],[9.12,0,'outCubic']], t) + 'px)';
    var badge = $('cOrderBadge');
    badge.style.opacity = kv([[9.15,0],[9.38,1,'outCubic']], t);
    badge.style.transform = 'scale(' + kv([[9.15,0.6],[9.48,1,'outBack']], t) + ')';
    var g2 = kv([[9.15,0],[9.38,1,'outCubic'],[9.65,1],[10.0,0,'inCubic']], t);
    row.style.boxShadow = '0 0 0 ' + (5 * g2) + 'px rgba(47, 164, 107, ' + (0.16 * g2) + ')';
    var nf = $('cNoteField');
    nf.className = (t >= 9.7 && t < 10.7) ? 'combo-noteslot hot' : 'combo-noteslot';
    $('cNotePh').style.opacity = kv([[9.7,1],[9.82,0,'linear']], t);
    $('cNoteText').style.opacity = kv([[9.75,0],[10.0,1,'outCubic']], t);
    $('s2dot').style.background = t < 9.8 ? '#38d27a' : '#9aa1ab';
    $('s2dot').style.boxShadow = t < 9.8 ? '0 0 0 5px rgba(56,210,122,0.22)' : 'none';
  }
  /* ===== s3 chunks ===== */
  if (t > 13.0) {
    applyF($('flyHpi'), FHPI, t);
    applyF($('flyAp'), FAP, t);
    collapseItem($('qHpi'), 14.85, t);
    collapseItem($('qAp'), 17.25, t);
    $('s3queue').style.opacity = kv([[17.6,1],[17.9,0,'inCubic']], t);
    var h = $('cfHpi');
    h.className = (t >= 15.5 && t < 16.5) ? 'chunk-field hot' : 'chunk-field';
    $('cfHpiPh').style.opacity = kv([[15.5,1],[15.62,0,'linear']], t);
    $('cfHpiText').style.opacity = kv([[15.55,0],[15.8,1,'outCubic']], t);
    var a2 = $('cfAp');
    a2.className = (t >= 17.9 && t < 18.9) ? 'chunk-field hot' : 'chunk-field';
    $('cfApPh').style.opacity = kv([[17.9,1],[18.02,0,'linear']], t);
    $('cfApText').style.opacity = kv([[17.95,0],[18.2,1,'outCubic']], t);
    $('s3dot').style.background = t < 18.0 ? '#38d27a' : '#9aa1ab';
    $('s3dot').style.boxShadow = t < 18.0 ? '0 0 0 5px rgba(56,210,122,0.22)' : 'none';
  }
  var veil = $('loopVeil');
  veil.style.opacity = kv([[21.95,0],[22.38,1,'linear']], t);
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
      if (tr.el === 's1chip' || tr.el === 's2chip' || tr.el === 's3chip') parts = 'translateX(-50%) ' + parts;
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

Path("web-ehr.html").write_text(head + body + engine, encoding="utf-8")
print("web-ehr.html written:", len(head + body + engine), "chars")
