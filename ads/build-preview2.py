"""Build preview2/ — homepage mockup: hero kept; Why-eleanote, how-it-works
and the four animation chapters ALL removed; replaced by two loop-video
sections (square video on desktop, portrait on phone) with CTA microcopy.
NOT deployed; Doug reviews from preview2/index.html."""
from pathlib import Path
import shutil

root = Path("..").resolve()
docs = root / "docs"
out = root / "preview2"
out.mkdir(exist_ok=True)

s = (docs / "index.html").read_text(encoding="utf-8")

# ---------- 1. CSS: loop-video presentation + section CTA ----------
s = s.replace("""        /* ---------- SCROLL REVEAL ---------- */""",
"""        /* ---------- LOOP VIDEO SECTIONS ---------- */
        .loopvid {
            display: block;
            width: 100%;
            margin: clamp(2rem, 4vw, 3rem) auto 0;
        }
        .vid-desktop { max-width: 640px; }
        .vid-mobile { display: none; }
        @media (max-width: 700px) {
            .vid-desktop { display: none; }
            .vid-mobile {
                display: block;
                width: 100vw;
                max-width: 100vw;
                margin-left: calc(50% - 50vw);
            }
        }
        .vid-cta { text-align: center; margin-top: clamp(1.8rem, 3.5vw, 2.6rem); }
        .vid-cta .micro {
            margin-top: 0.85rem;
            font-size: 0.92rem;
            font-weight: 500;
            color: var(--muted);
        }

        /* ---------- SCROLL REVEAL ---------- */""")

# ---------- 2. remove Why-eleanote + how-it-works + the four chapters ----------
start = s.index("        <!-- ============== WHY ELEANOTE ============== -->")
end = s.index("        <!-- ============== DEMO VIDEO ============== -->")
assert start < end
s = s[:start] + s[end:]

# ---------- 3. insert the two video sections before the demo ----------
marker = "        <!-- ============== DEMO VIDEO ============== -->"
new_sections = """        <!-- ============== NOTES YOU CONTROL (loop video 1) ============== -->
        <section class="block band-paper band-edge" id="notes">
            <div class="container">
                <div class="section-head centered reveal">
                    <p class="eyebrow centered">Quality notes</p>
                    <h2>Notes you control, <span class="accent">completely.</span></h2>
                    <p class="lede">Eleanote is built around one obsession: notes that come out right. You program exactly how yours are written &mdash; structure, tone, phrasing, saved text &mdash; and correct anything in plain language. The goal: notes that need minimal edits, in your voice.</p>
                </div>
                <video class="loopvid vid-desktop reveal d1" muted loop playsinline preload="metadata" data-src="videos/web-notes-sq.mp4" aria-label="Eleanote personalization: the preference interview, feedback on a note, and saved text filled in by AI"></video>
                <video class="loopvid vid-mobile reveal d1" muted loop playsinline preload="metadata" data-src="videos/web-notes.mp4" aria-label="Eleanote personalization: the preference interview, feedback on a note, and saved text filled in by AI"></video>
                <div class="vid-cta reveal d2">
                    <a class="btn" href="/auth/signup.html">Create free account <span class="arr">&rarr;</span></a>
                    <div class="micro">Free while in beta &middot; no card required</div>
                </div>
            </div>
        </section>

        <!-- ============== ANY EMR (loop video 2) ============== -->
        <section class="block band-paper band-edge" id="anyemr">
            <div class="container">
                <div class="section-head centered reveal">
                    <p class="eyebrow centered">Any EMR</p>
                    <h2>Works with any EMR &mdash; <span class="accent">even in remote sessions.</span></h2>
                    <p class="lede">No integration, no IT project &mdash; eleanote types into whatever EHR you already use, including EMRs running in Citrix, VMware, and other remote desktops. It precharts from the chart to add context, enters diagnoses and orders, and pastes the note with your formatting &mdash; whole, or section by section into separate fields.</p>
                </div>
                <video class="loopvid vid-desktop reveal d1" muted loop playsinline preload="metadata" data-src="videos/web-ehr-sq.mp4" aria-label="Eleanote EMR automation: precharting, diagnoses, orders and the note entered, and the note split into sections"></video>
                <video class="loopvid vid-mobile reveal d1" muted loop playsinline preload="metadata" data-src="videos/web-ehr.mp4" aria-label="Eleanote EMR automation: precharting, diagnoses, orders and the note entered, and the note split into sections"></video>
                <div class="vid-cta reveal d2">
                    <a class="btn" href="/auth/signup.html">Create free account <span class="arr">&rarr;</span></a>
                    <div class="micro">Free while in beta &middot; no card required</div>
                </div>
            </div>
        </section>

"""
s = s.replace(marker, new_sections + marker)

# ---------- 4. nav: drop "Why eleanote", "How it works" -> "See it work" ----------
s = s.replace("""                <a href="#why">Why eleanote</a>
                <a href="#how">How it works</a>""",
              """                <a href="#notes">See it work</a>""")
s = s.replace("""        <a href="#why" role="menuitem">Why eleanote <span class="arrow">&rarr;</span></a>
        <a href="#how" role="menuitem">How it works <span class="arrow">&rarr;</span></a>""",
              """        <a href="#notes" role="menuitem">See it work <span class="arrow">&rarr;</span></a>""")
assert "#why" not in s and 'href="#how"' not in s

# ---------- 5. loader: only the visible variant downloads/plays ----------
s = s.replace("</body>", """<script>
(function () {
    var mq = window.matchMedia("(max-width: 700px)");
    function loadVids(sel) {
        document.querySelectorAll(sel).forEach(function (v) {
            if (!v.getAttribute("src")) { v.src = v.dataset.src; }
            var p = v.play(); if (p && p.catch) { p.catch(function () {}); }
        });
    }
    loadVids(mq.matches ? ".vid-mobile" : ".vid-desktop");
    if (mq.addEventListener) {
        mq.addEventListener("change", function (e) {
            loadVids(e.matches ? ".vid-mobile" : ".vid-desktop");
        });
    }
})();
</script>
</body>""")

(out / "index.html").write_text(s, encoding="utf-8")

vids = out / "videos"
vids.mkdir(exist_ok=True)
for name in ("web-notes.mp4", "web-notes-sq.mp4", "web-ehr.mp4", "web-ehr-sq.mp4"):
    shutil.copy(f"out/{name}", vids / name)
print("preview2/ built:", len(s), "chars; 4 videos copied")
