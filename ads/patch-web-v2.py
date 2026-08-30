"""v2 of the web loops per Doug:
1. Saved-text scene = cystoscopy template (his wording), single window
   that morphs Saved Text -> Today's note, ALL brackets fill at once.
2. Both loops also emitted as SQUARE (1080x1080) desktop variants via a
   0.8-scale wrapper (1350 * 0.8 = 1080, zero re-choreography).
3. render.mjs reads page-declared dimensions.
"""
from pathlib import Path

# ---------------- render.mjs: dynamic dimensions ----------------
r = Path("render.mjs")
s = r.read_text(encoding="utf-8")
if "window.__w" not in s:
    s = s.replace("""await page.waitForFunction('window.__ready === true', { timeout: 60000 });
const total = await page.evaluate('window.__total');
console.log(`page ready — total ${total}s`);

const clip = { x: 0, y: 0, width: W, height: H };""",
"""await page.waitForFunction('window.__ready === true', { timeout: 60000 });
const total = await page.evaluate('window.__total');
const dims = await page.evaluate('({w: window.__w || 1080, h: window.__h || 1350})');
await page.setViewport({ width: dims.w, height: dims.h, deviceScaleFactor: 1 });
console.log(`page ready — total ${total}s @ ${dims.w}x${dims.h}`);

const clip = { x: 0, y: 0, width: dims.w, height: dims.h };""")
    r.write_text(s, encoding="utf-8")
    print("render.mjs: dynamic dims")

# ---------------- build-web1.py: cystoscopy scene ----------------
p = Path("build-web1.py")
s = p.read_text(encoding="utf-8")

# scene-3 CSS: single morphing window; drop the note window + tighten text
s = s.replace("""/* ---------- saved-text scene ---------- */
.st-win {
  position: absolute;
  left: 70px; top: 200px;
  width: 940px;""",
"""/* ---------- saved-text scene (cystoscopy template) ---------- */
.st-win {
  position: absolute;
  left: 70px; top: 230px;
  width: 940px;""")
s = s.replace(""".st-text { font-size: 26px; line-height: 1.75; color: #26393e; }""",
""".st-text { font-size: 25px; line-height: 1.72; color: #26393e; white-space: pre-line; }
.st-title-swap { position: absolute; left: 50%; transform: translateX(-50%); font-size: 25px; font-weight: 700; color: var(--ink); opacity: 0; }""")
# remove the landing-note window CSS
s = s.replace("""/* note window the phrase lands in */
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
""", "")

# scene-3 markup: cystoscopy template, single window, title crossfade
s = s.replace("""  <!-- SCENE 3 - SAVED TEXT (15.9-25.9) -->
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
  </div>""",
"""  <!-- SCENE 3 - SAVED TEXT: CYSTOSCOPY (15.9-25.9) -->
  <div class="beat" id="s3">
    <div class="scene-title kline" id="s3title">Saved text &mdash; <span class="serif">filled in for you.</span></div>
    <div class="st-win kline" id="stWin">
      <div class="st-titlebar">
        <span class="st-mark">e</span>
        <span class="st-titletext" id="stT1">Saved Text</span>
        <span class="st-title-swap" id="stT2">Today's note</span>
        <span class="st-winctl"><span></span><span></span><span></span></span>
      </div>
      <div class="st-body">
        <div class="st-labelrow">
          <span class="st-label">Cystoscopy note</span>
          <span class="st-mode" id="stMode">AI fills the brackets</span>
        </div>
        <div class="st-text"><b>Cystoscopy Procedure:</b>
Patient presents for cystoscopy. <span class="brk" id="bk0">[He, she]</span> was prepped and draped in standard fashion; standard timeout was performed. Findings are as follows:

Urethra: <span class="brk" id="bk1">[ ]</span>
<span class="brk" id="bk2">[Prostate findings]</span>
Ureteral orifices: <span class="brk" id="bk3">[ ]</span>
Bladder: <span class="brk" id="bk4">[ ]</span></div>
      </div>
    </div>
    <div class="phase-chip" id="s3chip">your template &mdash; <span class="gold">AI fills every blank at once</span></div>
  </div>""")

# scene-3 tracks: drop the note window track
s = s.replace("""  inout('s3title', 15.95, 25.55, 36),
  { el:'stWin', o:[[16.15,0],[16.60,1,'outCubic'],[25.25,1],[25.55,0,'inCubic']], y:[[16.15,60],[16.65,0,'outCubic']] },
  { el:'stnWin', o:[[16.85,0],[17.30,1,'outCubic'],[25.25,1],[25.55,0,'inCubic']], y:[[16.85,60],[17.35,0,'outCubic']] },
  { el:'s3chip', o:[[23.65,0],[24.00,1,'outCubic'],[25.25,1],[25.55,0,'inCubic']], y:[[23.65,34],[24.05,0,'outBack']] }""",
"""  inout('s3title', 15.95, 25.55, 36),
  { el:'stWin', o:[[16.15,0],[16.60,1,'outCubic'],[25.25,1],[25.55,0,'inCubic']], y:[[16.15,60],[16.65,0,'outCubic']] },
  { el:'s3chip', o:[[21.60,0],[21.95,1,'outCubic'],[25.25,1],[25.55,0,'inCubic']], y:[[21.60,34],[22.00,0,'outBack']] }""")

# scene-3 specials: simultaneous fill + titlebar morph
s = s.replace("""/* saved-text fills */
var ST_FILLS = [
  ['bk1', 20.3, 'a 4 mm distal ureteral stone'],
  ['bk2', 21.5, 'observation vs. ureteroscopy'],
  ['bk3', 22.7, 'a trial of passage with a strainer']
];
var ST_FLY = { x0: 540, y0: 430, x1: 400, y1: 745, t0: 18.0, t1: 18.7 };""",
"""/* saved-text fills — ALL at the same moment */
var ST_FILL_T = 19.8;
var ST_FILLS = [
  ['bk0', 'He'],
  ['bk1', 'no stricture'],
  ['bk2', 'Prostate: mild BPH'],
  ['bk3', 'orthotopic position bilaterally'],
  ['bk4', 'mild trabeculations, no urothelial lesions']
];
var ST_EMPTY = ['[He, she]', '[ ]', '[Prostate findings]', '[ ]', '[ ]'];""")
s = s.replace("""  /* ===== scene 3 saved text ===== */
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
  }""",
"""  /* ===== scene 3 saved text (cystoscopy, simultaneous fill) ===== */
  if (t > 15.7) {
    /* titlebar morphs Saved Text -> Today's note just before the fill */
    $('stT1').style.opacity = kv([[18.7,1],[19.1,0,'linear']], t);
    $('stT2').style.opacity = kv([[18.7,0],[19.1,1,'linear']], t);
    var mode = $('stMode');
    var modeWant = t < 19.0 ? 'AI fills the brackets' : 'inserted \\u2713';
    if (mode.textContent !== modeWant) mode.textContent = modeWant;
    /* every bracket pulses and fills AT ONCE */
    for (var k = 0; k < ST_FILLS.length; k++) {
      var el = $(ST_FILLS[k][0]);
      var pulse = kv([[ST_FILL_T-0.45,0],[ST_FILL_T-0.2,1,'outCubic'],[ST_FILL_T+0.15,0,'inCubic']], t);
      el.style.boxShadow = '0 0 0 ' + (5 * pulse) + 'px rgba(78, 163, 255, ' + (0.22 * pulse) + ')';
      var filled = t >= ST_FILL_T;
      if (filled && el.className !== 'brk filled') { el.className = 'brk filled'; el.textContent = ST_FILLS[k][1]; }
      if (!filled && el.className !== 'brk') { el.className = 'brk'; el.textContent = ST_EMPTY[k]; }
      var pop = kv([[ST_FILL_T,0.94],[ST_FILL_T+0.3,1,'outBack']], t);
      el.style.transform = filled ? ('scale(' + pop + ')') : '';
    }
  }""")
p.write_text(s, encoding="utf-8")
print("build-web1.py: cystoscopy scene, simultaneous fill")

# ---------------- square-variant emission for both build scripts ----------------
SQ_EMIT = '''
# ---- square desktop variant (1080x1080): whole 1350 composition x0.8 ----
html = head + body + engine
sq = html
sq = sq.replace("width: 1080px; height: 1350px;", "width: 1080px; height: 1080px;")
sq = sq.replace('<div id="canvas">', '<div id="canvas"><div id="zoomer" style="position:absolute;left:50%;top:0;width:1080px;height:1350px;transform:translateX(-50%) scale(0.8);transform-origin:top center;">')
sq = sq.replace("</div>\\n</div>\\n\\n<script>", "</div></div>\\n</div>\\n\\n<script>")
sq = sq.replace("window.innerHeight / 1350", "window.innerHeight / 1080")
sq = sq.replace("window.__total = DUR;", "window.__w = 1080; window.__h = 1080;\\nwindow.__total = DUR;")
Path(SQ_NAME).write_text(sq, encoding="utf-8")
print(SQ_NAME, "written (square)")
'''
for fname, out_name, sq_name in [("build-web1.py", "web-notes.html", "web-notes-sq.html"),
                                 ("build-web2.py", "web-ehr.html", "web-ehr-sq.html")]:
    f = Path(fname)
    s2 = f.read_text(encoding="utf-8")
    if "zoomer" not in s2:
        tail = 'Path("%s").write_text(head + body + engine, encoding="utf-8")' % out_name
        assert tail in s2, fname
        s2 = s2.replace(tail, tail + '\nSQ_NAME = "%s"' % sq_name + SQ_EMIT)
        f.write_text(s2, encoding="utf-8")
        print(fname, "-> also emits", sq_name)
