(function() {
 var footer = document.getElementById('site-footer');
 if (footer) {
 footer.innerHTML = [
 '<div class="container">',
 '<nav class="footer-nav" style="margin-bottom:1rem;">',
 '<a href="/privacy">Privacy Policy</a>',
 '&nbsp;&middot;&nbsp;',
 '<a href="/about">About</a>',
 '</nav>',
 '<p>&copy; 2026 Succession Holding LLC. All rights reserved.</p>',
 '<p>This site is for educational purposes only. Not financial advice. tredey.com is operated by Succession Holding LLC. Consult a licensed professional before making investment decisions.</p>',
 '</div>'
 ].join('\n');
 }
})();