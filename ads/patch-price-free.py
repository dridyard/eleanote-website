"""Remove the $100/month pricing from the homepage (Doug 2026-09-09: plans
$75 at launch, doesn't want current beta users to see $100 then a drop).
All three spots revert to plain free-while-in-beta wording."""
from pathlib import Path

path = Path("../docs/index.html")
s = path.read_text(encoding="utf-8")


def swap(old, new):
    global s
    assert s.count(old) == 1, f"expected exactly 1 of: {old[:60]!r} (found {s.count(old)})"
    s = s.replace(old, new)


swap('<span class="dot"></span> Free while in beta &middot; $100/month at launch',
     '<span class="dot"></span> Free while in beta')

swap("Nothing while it's in beta. At launch, Eleanote will be $100/month &mdash; a simple flat subscription with no per&#8209;note charges. Beta users get plenty of notice before billing begins.",
     "Nothing while it's in beta. When Eleanote launches commercially, the plan is a simple flat monthly subscription with no per&#8209;note charges &mdash; and beta users get plenty of notice before billing begins.")

swap("Eleanote is free while in beta &mdash; $100/month at launch. Sign up, set it up,",
     "Eleanote is free while in beta &mdash; it's free to sign up and try the program. Set it up,")

assert "$100" not in s and "$75" not in s
path.write_text(s, encoding="utf-8")
print("done:", s.count("Free while in beta"), "badge/heading mentions; no prices left")
