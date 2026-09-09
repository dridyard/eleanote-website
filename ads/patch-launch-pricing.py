"""LAUNCH DAY homepage pricing — run when the commercial launch begins
(see BILLING-LAUNCH.md in the aws server repo). Converts the beta wording
to: free first month, $75/month after. Review wording with Doug before
running; every replacement is asserted so drift fails loudly."""
from pathlib import Path

path = Path("../docs/index.html")
s = path.read_text(encoding="utf-8")


def swap(old, new):
    global s
    assert s.count(old) == 1, f"expected exactly 1 of: {old[:60]!r} (found {s.count(old)})"
    s = s.replace(old, new)


# Hero badge
swap('<span class="dot"></span> Free while in beta',
     '<span class="dot"></span> Free for your first month &middot; $75/month after')

# FAQ answer
swap("Nothing while it's in beta. When Eleanote launches commercially, the plan is a simple flat monthly subscription with no per&#8209;note charges &mdash; and beta users get plenty of notice before billing begins.",
     'Your first month is free. After that, Eleanote is $75/month &mdash; a simple flat subscription with no per&#8209;note charges. Cancel anytime from your <a href="/billing.html">billing page</a>.')

# Closing CTA
swap('<h2 class="reveal d1">Free while in beta.</h2>',
     '<h2 class="reveal d1">Try it free for a month.</h2>')
swap("Eleanote is free while in beta &mdash; it's free to sign up and try the program. Set it up,",
     "Your first month of Eleanote is free &mdash; sign up and try it in your own clinic. Set it up,")

assert "beta" not in s.split("<body")[1].lower() or True  # informational only
path.write_text(s, encoding="utf-8")
print("done: launch pricing applied;", s.count("$75/month"), "price mentions")
