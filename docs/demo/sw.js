// Service Worker for Mauve Health demo PWA
//
// Why this file exists:
// Chrome only shows the "Install app" prompt for sites that register a
// service worker with at least one fetch listener. This is the lightest
// possible SW that satisfies that requirement — it doesn't actively
// cache or transform anything yet.
//
// If we want true offline support later, we can add a cache strategy
// here. For now, every fetch just passes through to the network.

self.addEventListener('install', (event) => {
    // Activate immediately on first install — no waiting for old tabs
    self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    // Take control of all open pages right away
    event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', (event) => {
    // Pass through — no caching. Required to satisfy install criteria.
    // (Chrome only counts the SW as "controlling the page" if there's a
    // fetch handler present, even an empty one like this.)
});
