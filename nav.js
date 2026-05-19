// nav.js — Succession Holding LLC
// Row 1: dark forest green bar with wordmark + centered tagline
// Row 2: white bar with green bottom border, section tabs
(function () {

 // ── Row 1: Top Green Bar ──────────────────────────────────
 var utility = document.getElementById('site-utility');
 if (utility) {
  utility.innerHTML = [
   '<nav class="top-bar">',
   ' <a href="/" class="top-wordmark">Succession Holding LLC</a>',
   ' <span class="top-tagline">Real estate insight for independent investors</span>',
   ' <div class="top-links">',
   '  <a href="/contact" class="top-contact">Contact</a>',
   ' </div>',
   '</nav>'
  ].join('\n');
 }

 // ── Row 2: Section Tab Bar ───────────────────────────────
 var nav = document.getElementById('site-nav');
 if (nav) {
  nav.innerHTML = [
   '<div class="tab-bar">',
   ' <div class="tab-bar-inner">',
   '  <a href="/">Home</a>',
   '  <a href="/investing">Investing</a>',
   '  <a href="/market-analysis">Market Analysis</a>',
   '  <a href="/education">Education</a>',
   '  <a href="/about">About</a>',
   ' </div>',
   '</div>'
  ].join('\n');
 }

 // ── Active tab highlight ───────────────────────────────────
 var path = window.location.pathname;
 var tabs = document.querySelectorAll('.tab-bar a');
 tabs.forEach(function (tab) {
  var href = tab.getAttribute('href');
  if (href === path || (href !== '/' && path.startsWith(href))) {
   tab.classList.add('active');
  }
  if (href === '/' && (path === '/' || path === '/index')) {
   tab.classList.add('active');
  }
 });

})();