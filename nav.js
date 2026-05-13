(function() {
 var nav = document.getElementById('site-nav');
 if (nav) {
 nav.innerHTML = [
 '<div class="container">',
 '<div class="nav-brand">',
 '<a href="/" class="nav-wordmark">Succession Holding LLC</a>',
 '<span class="nav-tagline">Real estate insight for independent investors</span>',
 '</div>',
 '<nav class="main-nav">',
 '<ul>',
 '<li><a href="/">Home</a></li>',
 '<li><a href="/investing.html">Investing</a></li>',
 '<li><a href="/market-analysis.html">Market Analysis</a></li>',
 '<li><a href="/education.html">Education</a></li>',
 '<li><a href="/about.html">About</a></li>',
 '</ul>',
 '</nav>',
 '</div>'
 ].join('\n');
 }
})();