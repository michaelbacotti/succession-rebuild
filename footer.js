(function() {
 var footer = document.getElementById('site-footer');
 if (footer) {
 footer.innerHTML = [
 '<div class="container">',
 '<p>&copy; 2026 Succession Holding LLC. All rights reserved.</p>',
 '<p>This site is for educational purposes only. Not financial advice. Consult a licensed professional before making investment decisions.</p>',
 '</div>'
 ].join('\n');
 }
})();