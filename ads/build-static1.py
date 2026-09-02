"""Build static-1..5.html — 1080x1350 STATIC picture ads (no animation) in the
approved house style: cream + dot grid + floating feedback window. Five copy
variants; render each with `node render.mjs static-N.html --stills 0.05`.
Copy strategy: free-in-beta + $100/month at launch pricing transparency."""
from pathlib import Path

VARIANTS = [
    {   # 1 — Doug's own, cleaned (note-quality angle that won the A/B)
        "n": 1,
        "headline": 'The AI scribe that actually gets your notes <span class="serif">right.</span>',
        "sub": "",
        "checks": ["Learns from your feedback", "Types into any EHR"],
    },
    {   # 2 — frustration hook
        "n": 2,
        "headline": 'Tired of fixing your AI scribe&rsquo;s <span class="serif">notes?</span>',
        "sub": "Give feedback once. It remembers.",
        "checks": ["Notes in your voice, your format", "Types into any EHR"],
    },
    {   # 3 — the trainable-scribe claim
        "n": 3,
        "headline": 'The AI scribe you can <span class="serif">train.</span>',
        "sub": "Correct a note and it learns. Over time, it writes the way you would.",
        "checks": ["Works with any EHR"],
    },
    {   # 4 — repeated-edits hook
        "n": 4,
        "headline": 'Editing the same thing <span class="serif">every note?</span>',
        "sub": "Your scribe should have learned by now.",
        "checks": ["Learns from every correction", "Types into any EHR"],
    },
    {   # 5 — plainest promise
        "n": 5,
        "headline": 'Notes written the way <span class="serif">you&rsquo;d write them.</span>',
        "sub": "",
        "checks": ["Learns from your feedback", "Types into any EHR"],
    },
]

PAGE = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>eleanote — static ad {n} 1080x1350</title>
<style>
  :root {{
    --paper: #fbf7ec;
    --paper-2: #f6f0e2;
    --ink: #0d2b30;
    --teal: #14515c;
    --teal-deep: #0e3d46;
    --gold: #b98a2f;
    --line: rgba(13, 43, 48, 0.14);
    --muted: #5c6f73;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ background: #1a1a1a; }}
  #viewport {{ width: 1080px; height: 1350px; overflow: hidden; position: relative; }}
  #canvas {{
    width: 1080px; height: 1350px; position: absolute; left: 0; top: 0;
    background: var(--paper);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: var(--ink);
    overflow: hidden;
  }}
  #canvas::before {{
    content: "";
    position: absolute; inset: 0;
    background-image: radial-gradient(rgba(13,43,48,0.05) 1.5px, transparent 1.5px);
    background-size: 30px 30px;
    pointer-events: none;
  }}
  .glow {{
    position: absolute; border-radius: 50%; filter: blur(90px); pointer-events: none;
  }}
  .g1 {{ width: 560px; height: 560px; left: -160px; top: -140px; background: rgba(20,81,92,0.10); }}
  .g2 {{ width: 620px; height: 620px; right: -200px; bottom: -160px; background: rgba(185,138,47,0.10); }}
  .serif {{ font-family: Georgia, "Times New Roman", serif; font-style: italic; font-weight: 600; }}

  .wordmark {{
    position: absolute; top: 64px; left: 0; width: 1080px;
    display: flex; align-items: center; justify-content: center; gap: 14px;
  }}
  .wm-mark {{
    width: 46px; height: 46px; border-radius: 50%;
    background: var(--teal); color: #fff;
    font-size: 30px; font-weight: 800; letter-spacing: -0.06em;
    display: inline-flex; align-items: center; justify-content: center;
  }}
  .wm-text {{ font-size: 44px; font-weight: 800; letter-spacing: -0.03em; color: var(--ink); }}

  .headline {{
    position: absolute; top: {head_top}px; left: 70px; width: 940px;
    font-size: {head_size}px; line-height: 1.14; font-weight: 800;
    letter-spacing: -0.025em; text-align: center;
  }}
  .subline {{
    position: absolute; top: {sub_top}px; left: 110px; width: 860px;
    font-size: 34px; line-height: 1.4; font-weight: 500; color: var(--muted);
    text-align: center;
  }}

  .win {{
    position: absolute; left: 120px; top: {win_top}px; width: 840px;
    background: var(--paper);
    border: 1px solid rgba(0,0,0,0.16);
    border-radius: 18px;
    box-shadow: 0 34px 90px rgba(13,43,48,0.26);
    overflow: hidden; text-align: left;
  }}
  .titlebar {{
    background: var(--paper-2); border-bottom: 1px solid var(--line);
    height: 56px; display: flex; align-items: center; gap: 14px; padding: 0 24px; position: relative;
  }}
  .tb-mark {{
    width: 30px; height: 30px; border-radius: 50%; background: var(--teal); color: #fff;
    font-size: 20px; font-weight: 800; display: inline-flex; align-items: center; justify-content: center;
  }}
  .tb-title {{ position: absolute; left: 50%; transform: translateX(-50%); font-size: 24px; font-weight: 700; }}
  .tb-ctl {{ margin-left: auto; display: inline-flex; gap: 8px; }}
  .tb-ctl span {{ width: 14px; height: 14px; border-radius: 50%; background: rgba(0,0,0,0.16); }}
  .win-body {{ padding: 24px 30px 26px; }}
  .sec-h {{ font-size: 20px; font-weight: 800; letter-spacing: 0.08em; color: var(--teal-deep); margin-bottom: 6px; }}
  .sec-b {{ font-size: 25px; line-height: 1.5; color: #26393e; }}
  .sec-b.fresh {{
    background: rgba(78, 163, 255, 0.11);
    border: 1.5px solid rgba(78, 163, 255, 0.45);
    border-radius: 10px; padding: 10px 14px;
    color: #14456e; font-weight: 600;
  }}
  .inputrow {{ display: flex; gap: 14px; margin-top: 22px; }}
  .input {{
    flex: 1; border: 2px solid var(--teal); border-radius: 12px;
    background: #fff; padding: 13px 18px; font-size: 25px; color: var(--ink);
  }}
  .donebtn {{
    background: var(--teal-deep); color: #fff; font-size: 24px; font-weight: 700;
    border-radius: 12px; padding: 13px 24px; display: flex; align-items: center;
  }}

  .checks {{
    position: absolute; top: {checks_top}px; left: 0; width: 1080px;
    display: flex; flex-direction: column; align-items: center; gap: 18px;
  }}
  .check {{
    display: flex; align-items: center; gap: 16px;
    font-size: 38px; font-weight: 700; color: var(--ink);
  }}
  .check .tick {{ color: var(--gold); font-size: 40px; }}

  .price {{
    position: absolute; top: {price_top}px; left: 0; width: 1080px; text-align: center;
    font-size: 44px; font-weight: 800; letter-spacing: -0.01em;
  }}
  .price .free {{ color: var(--gold); }}
  .price .at {{ color: var(--muted); font-weight: 600; }}
  .site {{
    position: absolute; top: {site_top}px; left: 0; width: 1080px; text-align: center;
    font-size: 30px; font-weight: 700; color: var(--teal-deep);
  }}
</style>
</head>
<body>
<div id="viewport">
<div id="canvas">
  <div class="glow g1"></div>
  <div class="glow g2"></div>

  <div class="wordmark"><span class="wm-mark">e</span><span class="wm-text">eleanote</span></div>

  <div class="headline">{headline}</div>
  {subline}

  <div class="win">
    <div class="titlebar">
      <span class="tb-mark">e</span>
      <span class="tb-title">Today's note</span>
      <span class="tb-ctl"><span></span><span></span><span></span></span>
    </div>
    <div class="win-body">
      <div class="sec-h">ASSESSMENT</div>
      <div class="sec-b fresh">RCC s/p partial nephrectomy &mdash; stable, no evidence of recurrence. CKD-3 stable. HTN controlled.</div>
      <div class="inputrow">
        <div class="input">Make the assessment more concise</div>
        <div class="donebtn">Done&nbsp;&#10003;</div>
      </div>
    </div>
  </div>

  <div class="checks">{checks}</div>

  <div class="price"><span class="free">Free</span> while in beta <span class="at">&nbsp;&middot;&nbsp; $100/month at launch</span></div>
  <div class="site">eleanote.ai</div>
</div>
</div>
<script>
  window.__w = 1080; window.__h = 1350;
  window.__total = 0.1;
  window.__seek = function () {{}};
  window.__ready = true;
</script>
</body>
</html>
"""

for v in VARIANTS:
    has_sub = bool(v["sub"])
    head_size = 74 if len(v["headline"]) > 60 else 84
    win_h = 320
    if has_sub:
        head_top = 190
        sub_top = 424
        win_top = 585 if len(v["sub"]) > 45 else 540
    else:
        head_top = 216
        sub_top = 0
        win_top = 505
    checks_top = win_top + win_h + 66
    n_checks = len(v["checks"])
    price_top = checks_top + n_checks * 62 + 62
    site_top = price_top + 106

    checks_html = "".join(
        f'<div class="check"><span class="tick">&#10003;</span>{c}</div>' for c in v["checks"]
    )
    subline_html = f'<div class="subline">{v["sub"]}</div>' if has_sub else ""

    html = PAGE.format(
        n=v["n"], headline=v["headline"], subline=subline_html, checks=checks_html,
        head_top=head_top, head_size=head_size, sub_top=sub_top, win_top=win_top,
        checks_top=checks_top, price_top=price_top, site_top=site_top,
    )
    Path(f"static-{v['n']}.html").write_text(html, encoding="utf-8")
    print(f"static-{v['n']}.html written ({len(html)} chars)")
