// Assembles docs/fb-video.html from the homepage's scene animations.
// Extracts the main <style> block + the .scenes-wrap markup from index.html,
// then wraps them in a 9:16 self-playing "video page" shell with:
//   intro card -> scene 1..4 (titles pinned at top) -> end card.
// Re-run any time the homepage scenes change.
import { readFileSync, writeFileSync } from 'fs';

const SRC = 'C:/Users/dougr/OneDrive/Desktop/eleanote-website/docs/index.html';
const OUT = 'C:/Users/dougr/OneDrive/Desktop/eleanote-website/docs/fb-video.html';

const html = readFileSync(SRC, 'utf8');

// --- extract the big site <style> block (first one) ---
const sOpen = html.indexOf('<style>');
const sClose = html.indexOf('</style>');
if (sOpen < 0 || sClose < 0) throw new Error('style block not found');
const siteCss = html.slice(sOpen + 7, sClose);

// --- extract the scenes markup ---
const mOpen = html.indexOf('<div class="scenes-wrap wrap" id="scenes">');
const endMarker = '</div><!-- /.scenes-wrap -->';
const mClose = html.indexOf(endMarker);
if (mOpen < 0 || mClose < 0) throw new Error('scenes markup not found');
const scenesHtml = html.slice(mOpen, mClose + endMarker.length);

// --- scene titles (exact site copy, accents preserved) ---
const T1 = 'A small <span class="accent">assistant</span> sits on your screen, controlled by hotkeys — no toggling between EMR and eleanote.';
const T2 = 'Precharting takes seconds — just <span class="accent">highlight text</span> and transfer to eleanote.';
const T3 = 'While you record, AI <span class="accent">stages orders</span> for automated transfer in real time.';
const T4 = 'At end of encounter, transfer <span class="accent">diagnoses and the note</span> in one keystroke.';

const overrideCss = `
/* ===== video-shell overrides (win by coming after site CSS) ===== */
html,body{margin:0!important;padding:0!important;height:100%;overflow:hidden!important;background:#081f24!important;cursor:none}
/* 9:16 frame centered in the window; page bg matches so window shape is forgiving */
.vframe{position:fixed;left:50%;top:50%;transform:translate(-50%,-50%);
  height:min(100vh, calc(100vw * 16 / 9));aspect-ratio:9/16;
  background:linear-gradient(180deg,#0E3D46,#0b2f36);display:flex;flex-direction:column;overflow:hidden;
  font-family:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#fff}
/* caption bar */
.vcap{flex:0 0 auto;min-height:17%;display:flex;flex-direction:column;justify-content:center;gap:6px;
  padding:3.5% 5% 2% 5%;text-align:center}
.vcap .vbrand{font-family:"Source Serif 4",Georgia,serif;font-weight:600;font-size:clamp(14px,2.2vh,22px);
  letter-spacing:.02em;opacity:.85}
.vcap .scene-title{margin:0!important;font-size:clamp(13px,2.35vh,24px)!important;line-height:1.35!important;
  color:#fff!important;text-align:center!important;max-width:none!important}
.vcap .vtitle{opacity:0}
.vcap .vtitle.show{animation:vt-in .6s ease forwards}
@keyframes vt-in{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:none}}
/* stage area */
.vstage{flex:1 1 auto;position:relative;min-height:0}
/* neutralize the homepage scroll-carousel layout */
.vframe .scenes-wrap{display:block!important;position:absolute!important;inset:0!important;width:100%!important;
  height:100%!important;max-width:none!important;padding:0!important;margin:0!important;transform:none!important;background:transparent!important}
.vframe .scenes-wrap .scene{display:none!important;position:absolute!important;inset:0!important;width:100%!important;
  height:100%!important;padding:0!important;margin:0!important;transform:none!important;opacity:1!important}
.vframe .scenes-wrap .scene.on{display:flex!important;align-items:center!important;justify-content:center!important}
.vframe .scene .scene-title{display:none!important}
.vframe .scene-progress{display:none!important}
/* force the PHONE build of each scene */
.vframe .stage.d{display:none!important}
.vframe .scene.on .stage.p{display:block!important;position:relative!important;height:96%!important;width:auto!important;
  aspect-ratio:9/13!important;margin:0!important;max-width:none!important}
/* intro / outro cards */
.vcard{position:absolute;inset:0;display:none;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;padding:0 8%;gap:2.2vh}
.vcard.on{display:flex}
.vcard .big{font-family:"Source Serif 4",Georgia,serif;font-weight:600;font-size:clamp(34px,7.5vh,84px);letter-spacing:.01em}
.vcard .line{font-size:clamp(15px,2.6vh,26px);line-height:1.45;color:#dbe9ec;opacity:0}
.vcard .accentbar{width:56px;height:4px;border-radius:4px;background:#7fd4c1;opacity:0}
.vcard.on .a1{animation:vc-in .7s ease .15s forwards}
.vcard.on .a2{animation:vc-in .7s ease .75s forwards}
.vcard.on .a3{animation:vc-in .7s ease 1.35s forwards}
.vcard.on .a4{animation:vc-in .7s ease 1.95s forwards}
@keyframes vc-in{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.vcard .site{font-size:clamp(18px,3.4vh,34px);font-weight:700;color:#7fd4c1;opacity:0}
/* start hint (visible only before play; never in the recording once started) */
.vhint{position:absolute;left:0;right:0;bottom:4%;text-align:center;font-size:clamp(12px,1.8vh,16px);
  color:#9fc3c9;opacity:.9;z-index:5}
.vhint.gone{display:none}
`;

const controllerJs = `
(function(){
  var fast = /[?&]fast/.test(location.search);
  // Pixel-size the scenes + phone stages with inline styles. The homepage CSS
  // has carousel/containment rules that can zero these out; explicit inline
  // pixel values are immune to all of it.
  function sizeAll(){
    var stg = document.querySelector('.vstage');
    var H = stg.clientHeight, W = stg.clientWidth;
    var sh = Math.round(H * 0.97);
    var sw = Math.round(sh * 9 / 13);
    if (sw > W * 0.97){ sw = Math.round(W * 0.97); sh = Math.round(sw * 13 / 9); }
    document.querySelectorAll('.scenes-wrap .scene').forEach(function(sc){
      var s = sc.style;
      s.setProperty('position','absolute','important');
      s.setProperty('top','0','important'); s.setProperty('left','0','important');
      s.setProperty('width', W + 'px','important');
      s.setProperty('height', H + 'px','important');
      s.setProperty('padding','0','important'); s.setProperty('margin','0','important');
      s.setProperty('transform','none','important');
      var p = sc.querySelector('.stage.p');
      if (p){
        var ps = p.style;
        ps.setProperty('position','absolute','important');
        ps.setProperty('left', Math.round((W - sw) / 2) + 'px','important');
        ps.setProperty('top', Math.round((H - sh) / 2) + 'px','important');
        ps.setProperty('width', sw + 'px','important');
        ps.setProperty('height', sh + 'px','important');
        ps.setProperty('margin','0','important');
        ps.setProperty('aspect-ratio','auto','important');
        ps.setProperty('max-height','none','important');
        ps.setProperty('max-width','none','important');
        ps.setProperty('min-height','0','important');
      }
    });
  }
  window.addEventListener('resize', sizeAll);
  window.addEventListener('load', sizeAll);
  sizeAll();
  var TL = [
    { el: '#c-intro',  dur: 4600,  title: '' },
    { el: '.scene-1',  dur: 9000,  title: ${JSON.stringify(T1)} },
    { el: '.scene-2',  dur: 8650,  title: ${JSON.stringify(T2)} },
    { el: '.scene-3',  dur: 15000, title: ${JSON.stringify(T3)} },
    { el: '.scene-4',  dur: 20500, title: ${JSON.stringify(T4)} },
    { el: '#c-outro',  dur: 0,     title: '' }   // 0 = hold forever
  ];
  var timer = null, started = false;
  var titleEl = document.getElementById('vtitle');
  function clearAll(){
    document.querySelectorAll('.scene.on, .vcard.on').forEach(function(n){ n.classList.remove('on'); });
  }
  function showStep(i){
    clearAll();
    var step = TL[i];
    var node = document.querySelector(step.el);
    // toggling display (none -> flex/block) restarts every CSS animation inside
    if (node) node.classList.add('on');
    if (step.title){
      titleEl.innerHTML = step.title;
      titleEl.classList.remove('show');
      void titleEl.offsetWidth;             // reflow so the entrance animation re-runs
      titleEl.classList.add('show');
    } else {
      titleEl.innerHTML = '';
      titleEl.classList.remove('show');
    }
    var dur = fast ? 1400 : step.dur;
    if (timer) clearTimeout(timer);
    if (dur > 0 && i + 1 < TL.length) timer = setTimeout(function(){ showStep(i+1); }, dur);
  }
  function start(){
    started = true;
    document.getElementById('vhint').classList.add('gone');
    showStep(0);
  }
  // idle state: intro card visible (static), hint showing; click / Space starts; R restarts
  document.addEventListener('click', function(){ start(); });
  document.addEventListener('keydown', function(e){
    if (e.code === 'Space'){ e.preventDefault(); start(); }
    if (e.key === 'r' || e.key === 'R'){ start(); }
  });
  // initial: show intro statically (no timeline) so the screen isn't blank
  document.querySelector('#c-intro').classList.add('on');
})();
`;

const page = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow, noarchive">
<title>eleanote — video</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600&display=swap">
<style>
${siteCss}
</style>
<style>
${overrideCss}
</style>
</head>
<body>
<div class="vframe">
  <div class="vcap">
    <div class="vbrand">eleanote</div>
    <h2 class="scene-title vtitle" id="vtitle"></h2>
  </div>
  <div class="vstage">
    ${scenesHtml}
    <div class="vcard" id="c-intro">
      <div class="big a1" style="opacity:0">eleanote</div>
      <div class="accentbar a2"></div>
      <div class="line a3">An AI medical scribe that runs on your laptop.</div>
      <div class="line a4">Fully customizable — it writes notes your way.</div>
    </div>
    <div class="vcard" id="c-outro">
      <div class="big a1" style="opacity:0">eleanote</div>
      <div class="accentbar a2"></div>
      <div class="line a3">Free to try during testing.</div>
      <div class="site a4">eleanote.ai</div>
    </div>
    <div class="vhint" id="vhint">click anywhere to play &middot; R to restart</div>
  </div>
</div>
<script>
${controllerJs}
</script>
</body>
</html>
`;

writeFileSync(OUT, page, 'utf8');
console.log('wrote', OUT, '| css chars:', siteCss.length, '| scenes chars:', scenesHtml.length, '| total:', page.length);
