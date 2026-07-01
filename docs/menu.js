// Shared site menu for all content pages (guide, about, demo-video, security,
// and the legal docs). Replaces the per-page "Back to site" link with the same
// dropdown menu used on the homepage, so any page can navigate to any other.
// The logo (left of the header) remains the home link. Absolute (/...) paths
// so it works identically from the site root and from /legal/.
(function () {
  var header = document.querySelector('.legal-header');
  if (!header) return;

  // Remove the old "Back to site" link — the menu replaces it. (If this script
  // ever fails to load, the link stays as a graceful fallback.)
  var back = header.querySelector('.back');
  if (back) back.remove();

  var wrap = document.createElement('div');
  wrap.className = 'menu-wrap';
  wrap.innerHTML =
    '<button class="menu-btn" type="button" aria-expanded="false" aria-haspopup="true">' +
      '<span class="menu-icon" aria-hidden="true"><span></span><span></span><span></span></span>' +
      '<span>Menu</span>' +
    '</button>' +
    '<div class="menu-panel" role="menu">' +
      '<a href="/demo-video.html" role="menuitem">Demo video <span class="arrow">→</span></a>' +
      '<a href="/guide.html" role="menuitem">User guide <span class="arrow">→</span></a>' +
      '<a href="/security.html" role="menuitem">Privacy &amp; security <span class="arrow">→</span></a>' +
      '<a href="/about.html" role="menuitem">About <span class="arrow">→</span></a>' +
      '<a href="/auth/dashboard.html#download" role="menuitem">Download program <span class="arrow">→</span></a>' +
      '<hr>' +
      '<a href="/auth/login.html" role="menuitem" class="auth-out-only">Sign in <span class="arrow">→</span></a>' +
      '<a href="/auth/signup.html" role="menuitem" class="auth-out-only">Create account <span class="arrow">→</span></a>' +
      '<a href="/auth/dashboard.html" role="menuitem" class="auth-in-only" hidden>Account <span class="arrow">→</span></a>' +
      '<a href="#" role="menuitem" class="auth-in-only" id="menuSignout" hidden>Sign out <span class="arrow">→</span></a>' +
      '<hr>' +
      '<a href="/index.html#contact" role="menuitem">Contact <span class="arrow">→</span></a>' +
    '</div>';
  header.appendChild(wrap);

  var btn = wrap.querySelector('.menu-btn');
  var panel = wrap.querySelector('.menu-panel');
  function setOpen(open) {
    wrap.classList.toggle('open', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  btn.addEventListener('click', function (e) { e.stopPropagation(); setOpen(!wrap.classList.contains('open')); });
  document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) setOpen(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  panel.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });

  // Auth-aware: same localStorage keys as auth.js / the homepage menu.
  var idToken = localStorage.getItem('eleanote.idToken');
  var expiresAt = parseInt(localStorage.getItem('eleanote.expiresAt') || '0', 10);
  var loggedIn = !!idToken && Date.now() < expiresAt;
  wrap.querySelectorAll('.auth-out-only').forEach(function (el) { el.hidden = loggedIn; });
  wrap.querySelectorAll('.auth-in-only').forEach(function (el) { el.hidden = !loggedIn; });

  var signout = document.getElementById('menuSignout');
  if (signout) {
    signout.addEventListener('click', function (e) {
      e.preventDefault();
      ['eleanote.idToken', 'eleanote.accessToken', 'eleanote.refreshToken',
       'eleanote.email', 'eleanote.expiresAt'].forEach(function (k) { localStorage.removeItem(k); });
      window.location.reload();
    });
  }
})();
