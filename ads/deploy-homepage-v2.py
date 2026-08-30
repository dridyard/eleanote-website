"""Deploy the approved homepage v2 to docs/ (the LIVE site).

Applies to docs/index.html, in place:
  1. testing -> beta wording (4 spots; legal/terms.html deliberately untouched)
  2. the exact surgery Doug approved in preview2/: Why-eleanote + how-it-works
     + the four animation chapters removed, two loop-video sections inserted
     before the demo, nav collapsed to "See it work", matchMedia video loader
  3. copies the 4 loop videos to docs/videos/
  4. bumps the homepage sitemap lastmod

Rollback: git tag homepage-v1 (pre-deploy state).
Run once from ads/; every replacement is asserted so a re-run fails loudly.
"""
from pathlib import Path
import shutil

root = Path("..").resolve()
docs = root / "docs"
path = docs / "index.html"
s = path.read_text(encoding="utf-8")


def swap(old, new):
    global s
    assert s.count(old) == 1, f"expected exactly 1 of: {old[:60]!r} (found {s.count(old)})"
    s = s.replace(old, new)


# ---------- 1. testing -> beta ----------
swap("Now on Windows &amp; Mac &mdash; free during testing",
     "Now on Windows &amp; Mac &mdash; free while in beta")
swap("Eleanote is free while it's in its testing phase.",
     "Eleanote is free while it's in beta.")
swap("Early testers will hear about pricing",
     "Beta users will hear about pricing")
swap('<h2 class="reveal d1">Free to try during testing.</h2>',
     '<h2 class="reveal d1">Free while in beta.</h2>')
swap("Eleanote is in its testing phase &mdash; it's free to sign up",
     "Eleanote is in beta &mdash; it's free to sign up")

# ---------- 2. CSS: loop-video presentation ----------
swap("""        /* ---------- SCROLL REVEAL ---------- */""",
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

        /* ---------- SCROLL REVEAL ---------- */""")

# ---------- 3. remove Why-eleanote + how-it-works + the four chapters ----------
start = s.index("        <!-- ============== WHY ELEANOTE ============== -->")
end = s.index("        <!-- ============== DEMO VIDEO ============== -->")
assert start < end
s = s[:start] + s[end:]

# ---------- 4. insert the two video sections before the demo ----------
marker = "        <!-- ============== DEMO VIDEO ============== -->"
new_sections = """        <!-- ============== NOTES YOU CONTROL (loop video 1) ============== -->
        <section class="block band-paper band-edge" id="notes">
            <div class="container">
                <div class="section-head centered reveal">
                    <p class="eyebrow centered">Quality notes</p>
                    <h2>Notes you control, <span class="accent">completely.</span></h2>
                    <p class="lede">Eleanote is built around one obsession: notes that come out right. You program exactly how yours are written &mdash; structure, tone, phrasing, saved text &mdash; and correct anything in plain language. The goal: notes that need minimal edits, in your voice.</p>
                </div>
                <video class="loopvid vid-desktop reveal d1" muted loop playsinline preload="metadata" data-src="/videos/web-notes-sq.mp4" aria-label="Eleanote personalization: the preference interview, feedback on a note, and saved text filled in by AI"></video>
                <video class="loopvid vid-mobile reveal d1" muted loop playsinline preload="metadata" data-src="/videos/web-notes.mp4" aria-label="Eleanote personalization: the preference interview, feedback on a note, and saved text filled in by AI"></video>
            </div>
        </section>

        <!-- ============== ANY EMR (loop video 2) ============== -->
        <section class="block band-paper band-edge" id="anyemr">
            <div class="container">
                <div class="section-head centered reveal">
                    <p class="eyebrow centered">Any EMR</p>
                    <h2>Works with any EMR &mdash; <span class="accent">even in remote sessions.</span></h2>
                    <p class="lede">No integration, no IT project &mdash; eleanote types into whatever EHR you already use, even remote desktops. It precharts from the chart to add context, enters diagnoses and orders, and pastes the note with your formatting &mdash; whole, or section by section into separate fields.</p>
                </div>
                <video class="loopvid vid-desktop reveal d1" muted loop playsinline preload="metadata" data-src="/videos/web-ehr-sq.mp4" aria-label="Eleanote EMR automation: precharting, diagnoses, orders and the note entered, and the note split into sections"></video>
                <video class="loopvid vid-mobile reveal d1" muted loop playsinline preload="metadata" data-src="/videos/web-ehr.mp4" aria-label="Eleanote EMR automation: precharting, diagnoses, orders and the note entered, and the note split into sections"></video>
            </div>
        </section>

"""
swap(marker, new_sections + marker)

# ---------- 5. nav: drop "Why eleanote", "How it works" -> "See it work" ----------
swap("""                <a href="#why">Why eleanote</a>
                <a href="#how">How it works</a>""",
     """                <a href="#notes">See it work</a>""")
swap("""        <a href="#why" role="menuitem">Why eleanote <span class="arrow">&rarr;</span></a>
        <a href="#how" role="menuitem">How it works <span class="arrow">&rarr;</span></a>""",
     """        <a href="#notes" role="menuitem">See it work <span class="arrow">&rarr;</span></a>""")
assert "#why" not in s and 'href="#how"' not in s

# ---------- 6. loader: only the visible variant downloads/plays ----------
swap("</body>", """<script>
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

assert "testing" not in s.lower()
assert "Citrix" not in s and "VMware" not in s
path.write_text(s, encoding="utf-8")

# ---------- 7. videos ----------
vids = docs / "videos"
vids.mkdir(exist_ok=True)
for name in ("web-notes.mp4", "web-notes-sq.mp4", "web-ehr.mp4", "web-ehr-sq.mp4"):
    shutil.copy(f"out/{name}", vids / name)

# ---------- 8. sitemap ----------
sm_path = docs / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
old_entry = "    <loc>https://eleanote.ai/</loc>\n    <lastmod>2026-08-20</lastmod>"
assert sm.count(old_entry) == 1
sm = sm.replace(old_entry,
                "    <loc>https://eleanote.ai/</loc>\n    <lastmod>2026-08-30</lastmod>")
sm_path.write_text(sm, encoding="utf-8")

print("docs/index.html deployed:", len(s), "chars; 4 videos in docs/videos/; sitemap bumped")
