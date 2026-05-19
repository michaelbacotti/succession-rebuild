# Succession Holding LLC — Website Template & Style Guide

_This document is the canonical reference for rebuilding or extending successionholdingllc.com._

---

## 1. Site Structure

### Directory Tree

```
succession-rebuild-2026-05-13/
├── index.html                    # Homepage
├── about.html                    # About page
├── contact.html                  # Contact page
├── investing.html                # Investing section landing page
├── market-analysis.html          # Market Analysis section landing page
├── education.html                # Education section landing page
├── articles.html                 # All articles index
├── privacy.html                  # Privacy Policy
├── terms.html                    # Terms of Service
├── disclaimer.html               # Investment Disclaimer
├── style.css                     # Main stylesheet
├── nav.js                        # Nav injection script (NOT embedded in pages)
├── footer.js                     # Fallback footer script (NOT used on live pages)
├── _template.html               # Page template reference
├── _adsense.txt                  # AdSense block reference
├── _SITE-MEMORY.md               # Site memory notes
├── TONE.md                       # Editorial tone guide
├── favicon.svg
├── site.webmanifest
├── apple-touch-icon.png
├── android-chrome-192x192.png
├── android-chrome-512x512.png
├── ads.txt
├── sitemap.xml
├── package.json
├── node_modules/
├── articles/                     # Individual article pages
│   ├── 2026-04-29-first-investment-property-guide.html
│   ├── 2026-04-30-reading-a-rent-roll.html
│   ├── 2026-05-01-property-taxes-and-returns.html
│   ├── 2026-05-02-single-family-vs-multi-family.html
│   ├── 2026-05-03-understanding-noi.html
│   ├── 2026-05-04-first-investment-property.html
│   ├── 2026-05-04-what-is-a-cap-rate.html
│   ├── 2026-05-05-how-to-analyze-rental-property.html
│   ├── 2026-05-05-leveraging-equity.html
│   ├── 2026-05-06-landlord-vs-tenant-markets.html
│   ├── 2026-05-06-rental-market-landscape.html
│   ├── 2026-05-07-property-valuation-methods.html
│   ├── 2026-05-08-commercial-vs-residential.html
│   ├── 2026-05-09-mortgage-financing-basics.html
│   ├── 2026-05-10-cap-rates-explained.html
│   ├── 2026-05-11-1031-exchange-guide.html
│   ├── 2026-05-12-multi-family-outlook.html
│   ├── 2026-05-12-suburban-housing-trends.html
│   ├── 2026-05-13-corporate-housing-ban/
│   │   ├── index.html
│   │   └── corporate-housing-ban-image.png
└── images/                       # Site images
```

### File Naming Conventions

- **Pages:** `kebab-case.html` (e.g., `market-analysis.html`, `contact.html`)
- **Articles:** ISO date prefix + kebab-case slug (e.g., `2026-05-13-corporate-housing-ban/index.html`)
- **Article subdirectories:** Same as above — each article gets its own folder with an `index.html` inside

### Pages Summary

| File | Title | Type |
|------|-------|------|
| `index.html` | Homepage | Homepage |
| `about.html` | About | Content page |
| `contact.html` | Contact | Content page |
| `investing.html` | Real Estate Investing | Section landing |
| `market-analysis.html` | Market Analysis | Section landing |
| `education.html` | Education | Section landing |
| `articles.html` | All Articles | Listing page |
| `articles/[slug]/index.html` | Individual article | Article page |
| `privacy.html` | Privacy Policy | Legal |
| `terms.html` | Terms of Service | Legal |
| `disclaimer.html` | Investment Disclaimer | Legal |

---

## 2. Page Template (Standard HTML Shell)

### Complete `<head>` Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>PAGE TITLE | Succession Holding LLC</title>
 <meta name="description" content="PAGE DESCRIPTION">
 <link rel="stylesheet" href="/style.css">
 <link rel="icon" type="image/svg+xml" href="/favicon.svg">
 <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9312870448453345" crossorigin="anonymous"></script>
 <link rel="canonical" href="https://successionholdingllc.com/PAGE-PATH.html">
</head>
<body>
```

### Body Structure

```html
 <div id="site-utility"></div>
 <div id="site-nav"></div>

 <main>
 <div class="container">

  <!-- PAGE CONTENT -->

 </div>
 </main>

 <div style="margin:2rem 0;padding:.75rem;background:var(--surface);border-radius:var(--radius);text-align:center;">
 <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9312870448453345" data-ad-slot="7590828986" data-ad-format="auto" data-full-width-responsive="true"></ins>
 </div>
 <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>

 <div id="site-footer">
  <!-- Footer HTML (see Section 5) -->
 </div>

 <script src="/nav.js"></script>

</body>
</html>
```

### Notes

- **Nav is injected via `nav.js`** — each page has empty `<div id="site-utility">` and `<div id="site-nav">` placeholders; `nav.js` populates them on load. The nav.js script is always the last script tag before `</body>`.
- **Footer is inline static HTML** — NOT served via `footer.js`. Each page contains the full footer HTML directly in `#site-footer`. The `footer.js` file exists but is NOT used on live pages.
- **`#site-utility` is optional** — article pages (under `/articles/`) may omit the `#site-utility` div and start directly with `#site-nav`. Content pages include both.
- **`--surface` variable** — referenced in the AdSense wrapper div but NOT defined in `:root`. The ad wrapper uses `var(--surface)` which falls back to undefined; this appears to be an oversight. Consider defining `--surface: #f8f8f6;` in `:root` if ad background needs to match `.ad-zone`.

---

## 3. CSS Reference

### `:root` Variables

```css
:root {
 --green: #2d5a3d;
 --green-light: #3d7a52;
 --charcoal: #1a1a1a;
 --text: #333333;
 --text-light: #666666;
 --bg: #ffffff;
 --bg-secondary: #f8f8f6;
 --border: #e0ddd8;
 --max-width: 1100px;
}
```

### Key Classes

| Class | Purpose | Notes |
|-------|---------|-------|
| `.container` | Content width wrapper | `max-width: 1100px; margin: 0 auto; padding: 0 1.5rem;` |
| `.ad-zone` | In-content ad placeholder | Dashed border, secondary bg, centered text |
| `.article-header` | Page title block | `padding: 3rem 0 2rem; border-bottom: 1px solid var(--border);` |
| `.article-body` | Main content area | `max-width: 720px; padding: 2rem 0;` |
| `.article-meta` | Byline/date row | `display: flex; gap: 1.5rem;` |
| `.article-card` | Card in listing grids | `border-bottom: 1px solid var(--border); padding: 1.5rem 0;` |
| `.card-category` | Category label | Green, uppercase, small |
| `.card-meta` | Card date/meta | Uppercase, 10px, letter-spaced |
| `.card-title` | Card headline | 17px, serif, charcoal |
| `.card-summary` | Card excerpt | 14px, text-light |
| `.listing-grid` | 3-col article grid | `display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;` |
| `.section-header` | Section title row | Flex, green bottom border |
| `.section-cards` | Homepage section grid | 3-col, 24px gap, cards have no border-bottom |
| `.sidebar-widget` | Sidebar widget | Used on homepage |
| `.sidebar-item` | Sidebar item | Has border-bottom |
| `.featured-article` | Homepage hero | Border-bottom, 2rem padding |
| `.featured-image` | Hero image | 16:9 aspect ratio, object-fit cover |
| `.article-hero` | Article hero image | 16:9, border-radius, margin: 1.5rem 0 2rem |
| `.home-grid` | Homepage 2-col layout | `grid-template-columns: 1fr 300px;` with sidebar |
| `.home-sidebar` | Homepage sidebar | `padding-top: 48px;` |
| `.share-bar` | Social share row | Flex, border top + bottom |
| `.footer-inner` | Footer wrapper | `padding: 48px 0;` |
| `.footer-grid` | Footer 3-col grid | `grid-template-columns: 1.5fr 1fr 1fr;` |
| `.footer-brand` | Brand column | Left-most footer column |
| `.footer-nav` | Nav columns | 2nd and 3rd footer columns |
| `.footer-bottom` | Copyright row | Border-top |

### Max-Widths and Padding Patterns

- **Content max-width:** `1100px` (--max-width)
- **Article body max-width:** `720px`
- **Container horizontal padding:** `0 1.5rem`
- **Section padding:** `3rem 0` for major sections, `2rem 0` for grids
- **Card padding:** `1.5rem 0` (cards), `1.5rem` (section-cards variant)

### Responsive Breakpoints

```css
@media (max-width: 768px) {
 .home-grid { grid-template-columns: 1fr; }
 .listing-grid { grid-template-columns: 1fr; }
 .section-cards { grid-template-columns: 1fr; }
 .featured-article h2 { font-size: 1.5rem; }
 .article-header h1 { font-size: 1.75rem; }
}
```

---

## 4. Nav Structure

Nav is injected by `nav.js` into empty `<div id="site-utility">` and `<div id="site-nav">` placeholders.

### Row 1 — Top Green Bar (`#site-utility`)

```html
<nav class="top-bar">
 <a href="/" class="top-wordmark">Succession Holding LLC</a>
 <span class="top-tagline">Real estate insight for independent investors</span>
 <div class="top-links">
  <a href="/contact.html" class="top-contact">Contact</a>
 </div>
</nav>
```

CSS: `.top-bar` uses `display: flex; align-items: center; justify-content: space-between; padding: 0 24px;`. Tagline is absolutely centered via `position: absolute; left: 50%; transform: translateX(-50%);`.

### Row 2 — Tab Bar (`#site-nav`)

```html
<div class="tab-bar">
 <div class="tab-bar-inner">
  <a href="/">Home</a>
  <a href="/investing.html">Investing</a>
  <a href="/market-analysis.html">Market Analysis</a>
  <a href="/education.html">Education</a>
  <a href="/about.html">About</a>
 </div>
</div>
```

**Active tab highlighting:** `nav.js` adds `.active` class to the tab matching the current pathname. Tabs use `border-bottom: 2px solid var(--green)` when active.

---

## 5. Footer Structure

The footer is **inline static HTML** in each page — NOT loaded via `footer.js`. Each page has a complete `<div id="site-footer">` with the full footer structure.

```html
<div id="site-footer">
 <div class="footer-inner container">
  <div class="footer-grid" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:32px;margin-bottom:32px;">
   <div class="footer-brand">
    <h4 style="font-size:1rem;font-weight:600;margin-bottom:12px;color:#1a1a1a;">Succession Holding LLC</h4>
    <p style="font-size:0.875rem;line-height:1.65;color:#555;">Independent real estate education and market analysis. Our work focuses on investing fundamentals, property analysis, and market research for informed decision-making.</p>
   </div>
   <div class="footer-nav">
    <h5 style="font-size:0.7rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#888;margin-bottom:12px;">Education</h5>
    <ul style="list-style:none;padding:0;margin:0;">
     <li style="margin-bottom:8px;"><a href="/investing.html" style="font-size:0.875rem;color:#555;text-decoration:none;">Real Estate Investing</a></li>
     <li style="margin-bottom:8px;"><a href="/education.html" style="font-size:0.875rem;color:#555;text-decoration:none;">Education Center</a></li>
     <li style="margin-bottom:8px;"><a href="/market-analysis.html" style="font-size:0.875rem;color:#555;text-decoration:none;">Market Analysis</a></li>
    </ul>
   </div>
   <div class="footer-nav">
    <h5 style="font-size:0.7rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#888;margin-bottom:12px;">Company</h5>
    <ul style="list-style:none;padding:0;margin:0;">
     <li style="margin-bottom:8px;"><a href="/about.html" style="font-size:0.875rem;color:#555;text-decoration:none;">About</a></li>
     <li style="margin-bottom:8px;"><a href="/contact.html" style="font-size:0.875rem;color:#555;text-decoration:none;">Contact</a></li>
     <li style="margin-bottom:8px;"><a href="/terms.html" style="font-size:0.875rem;color:#555;text-decoration:none;">Terms of Service</a></li>
     <li style="margin-bottom:8px;"><a href="/disclaimer.html" style="font-size:0.875rem;color:#555;text-decoration:none;">Investment Disclaimer</a></li>
     <li style="margin-bottom:8px;"><a href="/privacy.html" style="font-size:0.875rem;color:#555;text-decoration:none;">Privacy Policy</a></li>
    </ul>
   </div>
  </div>
  <div class="footer-bottom" style="border-top:1px solid #e0e0e0;padding-top:20px;">
   <p style="font-size:0.8rem;color:#888;margin-bottom:6px;">&copy; 2026 Succession Holding LLC. All rights reserved.</p>
   <p style="font-size:0.8rem;color:#888;">For educational purposes only. Not financial advice. Consult a licensed professional before making investment decisions.</p>
  </div>
 </div>
</div>
```

**Note:** `footer.js` exists but is NOT used. It only contains a minimal 3-link version (Privacy Policy, About, Contact). The actual pages use the full 3-column inline footer.

---

## 6. AdSense Block

### Script in `<head>`

```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9312870448453345" crossorigin="anonymous"></script>
```

### Ad Placement (between `</main>` and `<div id="site-footer">`)

```html
<div style="margin:2rem 0;padding:.75rem;background:var(--surface);border-radius:var(--radius);text-align:center;">
 <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9312870448453345" data-ad-slot="7590828986" data-ad-format="auto" data-full-width-responsive="true"></ins>
 </div>
 <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
```

**Ad slot ID:** `7590828986`
**Publisher ID:** `ca-pub-9312870448453345`

### In-Content Ad Zone (`.ad-zone`)

For ad placeholders within article content, use:

```html
<div class="ad-zone">ADVERTISEMENT</div>
```

This is a visual placeholder (dashed border, grey text). The AdSense block above is the actual served ad.

---

## 7. Content Page Structure

Use `about.html` or `contact.html` as the template.

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>PAGE TITLE | Succession Holding LLC</title>
 <meta name="description" content="PAGE DESCRIPTION">
 <link rel="stylesheet" href="/style.css">
 <link rel="icon" type="image/svg+xml" href="/favicon.svg">
 <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9312870448453345" crossorigin="anonymous"></script>
 <link rel="canonical" href="https://successionholdingllc.com/PAGE-PATH.html">
</head>
<body>

 <div id="site-utility"></div>
 <div id="site-nav"></div>

 <main>
 <div class="container">

 <div class="article-header" style="padding-bottom:1rem;">
  <h1>PAGE HEADING</h1>
 </div>

 <div class="article-body">

  <!-- Content here -->

  <div class="ad-zone">ADVERTISEMENT</div>

 </div>
 </div>
 </main>

 <div style="margin:2rem 0;padding:.75rem;background:var(--surface);border-radius:var(--radius);text-align:center;">
 <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9312870448453345" data-ad-slot="7590828986" data-ad-format="auto" data-full-width-responsive="true"></ins>
 </div>
 <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>

 <div id="site-footer">
  <!-- Full footer HTML (see Section 5) -->
 </div>

 <script src="/nav.js"></script>

</body>
</html>
```

### Content Page Classes

- `.article-header` — page title block with `<h1>`
- `.article-body` — wrapper for content paragraphs, headings, lists
- `.ad-zone` — inline placeholder for ads within body

---

## 8. Article Page Structure

Individual articles live under `/articles/[slug]/index.html`.

### Article Page Shell

```html
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>ARTICLE TITLE | Succession Holding LLC</title>
 <meta name="description" content="ARTICLE DESCRIPTION">
 <link rel="stylesheet" href="/style.css">
 <link rel="icon" type="image/svg+xml" href="/favicon.svg">
 <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9312870448453345" crossorigin="anonymous"></script>
 <link rel="canonical" href="https://successionholdingllc.com/articles/[slug]/">
</head>
<body>

 <div id="site-nav"></div>

 <main>
 <div class="container">
 <div class="article-body">

  <div class="article-header">
   <span class="category" style="display:inline-block;background:var(--green);color:white;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;padding:0.2rem 0.6rem;margin-bottom:0.75rem;">CATEGORY</span>
   <h1>ARTICLE TITLE</h1>
   <div class="article-meta"><span>PUBLICATION DATE</span></div>
  </div>

  <div class="article-hero">
   <img src="/articles/[slug]/hero-image.png" alt="Alt text" style="width:100%;height:auto;display:block;">
  </div>

  <!-- Article content paragraphs -->

  <div class="ad-zone">ADVERTISEMENT</div>

  <!-- More article content -->

  <!-- Share bar -->
  <div class="share-bar">
   <span class="share-label">Share</span>
   <a class="share-btn" href="https://twitter.com/intent/tweet?url=URL">Twitter</a>
   <a class="share-btn" href="https://www.facebook.com/sharer/sharer.php?u=URL">Facebook</a>
   <a class="share-btn" href="https://www.linkedin.com/shareArticle?url=URL">LinkedIn</a>
  </div>

 </div>
 </div>
 </main>

 <div style="margin:2rem 0;padding:.75rem;background:var(--surface);border-radius:var(--radius);text-align:center;">
 <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9312870448453345" data-ad-slot="7590828986" data-ad-format="auto" data-full-width-responsive="true"></ins>
 </div>
 <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>

 <div id="site-footer">
  <!-- Full footer HTML -->
 </div>

 <script src="/nav.js"></script>

</body>
</html>
```

### Article Page Notes

- **No `#site-utility`** — article pages only have `#site-nav` (the top green bar is omitted)
- **Category label** — inline style: `display:inline-block;background:var(--green);color:white;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;padding:0.2rem 0.6rem;margin-bottom:0.75rem;`
- **`.article-hero`** — 16:9 image, border-radius: 4px, margin: 1.5rem 0 2rem
- **Article body max-width:** 720px (via `.article-body` CSS)
- **Share bar:** present at the end of article content, before the AdSense block

---

## 9. Homepage Structure

The homepage (`index.html`) uses a unique layout not replicated on other pages.

### Key Sections

1. **Featured Article** (`<div class="home-main">`) — large hero with category label, H2 headline, date, image, excerpt, and link
2. **Home Sidebar** (`<div class="home-sidebar">`) — `<div class="sidebar-widget">` with `<h4>Latest</h4>` and 4 `<div class="sidebar-item">` entries
3. **Section Rows** (Investing, Market Analysis, Education) — each has a `.section-header` + `.section-cards` grid of 3 `.article-card` items

### Homepage Grid

```html
<div class="home-grid">
 <div class="home-main">
  <div class="featured-article">
   <span class="category">CATEGORY</span>
   <h2>HEADLINE</h2>
   <span class="date">DATE</span>
   <img src="/IMAGE" alt="Alt" class="featured-image">
   <p>EXCERPT</p>
   <a href="/LINK" class="read-more">Read the full analysis &rarr;</a>
  </div>
 </div>
 <div class="home-sidebar">
  <div class="sidebar-widget">
   <h4>Latest</h4>
   <div class="sidebar-item">
    <p class="sidebar-meta">CATEGORY &nbsp;·&nbsp; DATE</p>
    <a href="/LINK" class="sidebar-title">TITLE</a>
    <p class="sidebar-preview">EXCERPT TEXT</p>
   </div>
   <!-- more sidebar-item entries -->
  </div>
 </div>
</div>
```

### Section Row Template

```html
<div class="section-header">
 <h2>SECTION NAME</h2>
 <a href="/SECTION-PAGE">View all &#8594;</a>
</div>
<div class="section-cards">
 <div class="article-card">
  <p class="card-meta">CATEGORY &nbsp;·&nbsp; Month DD, YYYY</p>
  <h3 class="card-title"><a href="/ARTICLE-LINK">ARTICLE TITLE</a></h3>
  <p class="card-summary">SUMMARY TEXT</p>
 </div>
 <!-- 2 more article-card divs -->
</div>
```

---

## 10. Section Landing Pages (investing.html, education.html, market-analysis.html)

These pages combine an `.article-header` with introductory text followed by a `.listing-grid` of article cards.

```html
<div class="article-header" style="padding-bottom:1rem;">
 <h1>SECTION TITLE</h1>
 <p style="color:var(--text-light);font-size:1.05rem;margin-top:0.5rem;">SECTION DESCRIPTION</p>
</div>

<p style="margin-bottom:1.5rem;">Introductory paragraph...</p>

<div class="ad-zone">ADVERTISEMENT</div>

<div class="listing-grid">
 <article class="article-card">
  <span class="card-category">CATEGORY</span>
  <h3><a href="/articles/[slug].html">ARTICLE TITLE</a></h3>
  <span class="date">Month DD, YYYY</span>
  <p>ARTICLE SUMMARY</p>
 </article>
 <!-- more article-card entries -->
</div>
```

---

## 11. Complete CSS Stylesheet

```css
/* ================================================
 Succession Holding LLC — Main Stylesheet
 Real estate education publication
 ================================================ */

:root {
 --green: #2d5a3d;
 --green-light: #3d7a52;
 --charcoal: #1a1a1a;
 --text: #333333;
 --text-light: #666666;
 --bg: #ffffff;
 --bg-secondary: #f8f8f6;
 --border: #e0ddd8;
 --max-width: 1100px;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
 background: var(--bg);
 color: var(--text);
 font-family: system-ui, -apple-system, sans-serif;
 font-size: 17px;
 line-height: 1.7;
}

h1, h2, h3, h4 {
 font-family: Georgia, serif;
 color: var(--charcoal);
 line-height: 1.3;
 font-weight: 400;
}

a { color: var(--green); text-decoration: none; }
a:hover { text-decoration: underline; }

/* Layout */
.container {
 max-width: var(--max-width);
 margin: 0 auto;
 padding: 0 1.5rem;
}

/* Ad zones */
.ad-zone {
 background: var(--bg-secondary);
 border: 1px dashed var(--border);
 padding: 1rem;
 text-align: center;
 color: var(--text-light);
 font-size: 0.8rem;
 letter-spacing: 0.04em;
 margin: 1.5rem 0;
}
.ad-sidebar { margin: 0; }

/* Row 1: Top Green Bar */
#site-utility {
 background-color: var(--green);
 padding: 14px 0;
}

.top-bar {
 display: flex;
 align-items: center;
 justify-content: space-between;
 padding: 0 24px;
 position: relative;
}

.top-wordmark {
 font-family: Georgia, serif;
 font-size: 1rem;
 font-weight: 700;
 color: #ffffff;
 letter-spacing: 0.02em;
 white-space: nowrap;
 flex-shrink: 0;
}

.top-tagline {
 position: absolute;
 left: 50%;
 transform: translateX(-50%);
 font-family: Georgia, 'Times New Roman', serif;
 font-style: italic;
 font-size: 11px;
 font-weight: 400;
 color: rgba(255,255,255,0.85);
 letter-spacing: 0.02em;
 white-space: nowrap;
}

.top-links {
 flex-shrink: 0;
}

.top-contact {
 font-size: 0.8rem;
 color: rgba(255,255,255,0.8);
 letter-spacing: 0.05em;
 text-decoration: none;
}

.top-contact:hover { color: #ffffff; }

@media (max-width: 768px) {
 .top-tagline { display: none; }
}

/* Row 2: Section Tab Bar */
#site-nav {
 border-bottom: 2px solid var(--green);
 background-color: #ffffff;
}

.tab-bar {
 display: flex;
 align-items: center;
 padding: 0 24px;
}

.tab-bar-inner {
 display: flex;
 flex-direction: row;
 align-items: center;
 gap: 0;
}

.tab-bar-inner a {
 display: inline-block;
 padding: 14px 20px;
 font-size: 0.85rem;
 font-weight: 500;
 color: var(--text-light);
 text-decoration: none;
 border-bottom: 2px solid transparent;
 transition: color 0.2s, border-color 0.2s;
 white-space: nowrap;
 letter-spacing: 0.04em;
 text-transform: uppercase;
}

.tab-bar-inner a:hover {
 color: var(--green);
 border-bottom-color: var(--green);
}

.tab-bar-inner a.active {
 color: var(--green);
 border-bottom-color: var(--green);
}

/* Footer */
#site-footer {
 border-top: 1px solid var(--border);
 padding: 2.5rem 0;
 margin-top: 4rem;
 color: var(--text-light);
 font-size: 0.85rem;
 text-align: center;
}

/* Homepage layout */
.home-grid {
 display: grid;
 grid-template-columns: 1fr 300px;
 gap: 3rem;
 padding: 3rem 0;
}

.home-main { min-width: 0; }
.home-sidebar { min-width: 0; padding-top: 48px; }

/* Featured article */
.featured-article {
 border-bottom: 1px solid var(--border);
 padding-bottom: 2rem;
 margin-bottom: 2rem;
}

.featured-article .category {
 display: inline-block;
 background: var(--green);
 color: white;
 font-size: 0.75rem;
 letter-spacing: 0.08em;
 text-transform: uppercase;
 padding: 0.2rem 0.6rem;
 margin-bottom: 0.75rem;
}

.featured-article h2 {
 font-size: 1.85rem;
 margin-bottom: 0.75rem;
 line-height: 1.25;
}

.featured-article .date {
 color: var(--text-light);
 font-size: 0.85rem;
 margin-bottom: 1rem;
}

.featured-article p {
 color: var(--text);
 font-size: 1.05rem;
 line-height: 1.75;
 margin-bottom: 1rem;
}

.read-more {
 color: var(--green);
 font-size: 0.9rem;
 font-weight: 600;
 letter-spacing: 0.03em;
}

/* Article cards */
.article-card {
 border-bottom: 1px solid var(--border);
 padding: 1.5rem 0;
}


.card-category {
 display: inline-block;
 color: var(--green);
 font-size: 0.75rem;
 letter-spacing: 0.08em;
 text-transform: uppercase;
 font-weight: 600;
 margin-bottom: 0.4rem;
}

.article-card h3 {
 font-size: 1.15rem;
 margin-bottom: 0.4rem;
 line-height: 1.35;
}

.article-card .date {
 color: var(--text-light);
 font-size: 0.82rem;
 margin-bottom: 0.5rem;
}

.article-card p {
 font-size: 0.95rem;
 color: var(--text-light);
 line-height: 1.65;
}

/* Sidebar widgets */
.sidebar-widget {
 margin-bottom: 2.5rem;
}

.sidebar-widget h4 {
 font-size: 0.85rem;
 letter-spacing: 0.08em;
 text-transform: uppercase;
 color: var(--text-light);
 margin-bottom: 1rem;
 border-bottom: 2px solid var(--green);
 padding-bottom: 0.5rem;
}

.sidebar-widget ul {
 list-style: none;
}

.sidebar-widget li {
 padding: 0.6rem 0;
 border-bottom: 1px solid var(--border);
 font-size: 0.95rem;
}

.sidebar-widget li:last-child { border-bottom: none; }

.sidebar-meta {
 font-size: 10px;
 font-weight: 600;
 letter-spacing: 0.1em;
 text-transform: uppercase;
 color: #888;
 margin: 0 0 3px 0;
}

.sidebar-item {
 border-bottom: 1px solid #e0ddd6;
 padding-bottom: 14px;
 margin-bottom: 14px;
}

.sidebar-item:last-child {
 border-bottom: none;
 margin-bottom: 0;
 padding-bottom: 0;
}

.sidebar-title {
 font-size: 14px;
 color: #2d5a3d;
 text-decoration: none;
 line-height: 1.4;
 display: block;
 margin-bottom: 16px;
}

.sidebar-title:hover { text-decoration: underline; }

/* Section header */
.section-header {
 display: flex;
 justify-content: space-between;
 align-items: baseline;
 border-bottom: 2px solid #2d5a3d;
 padding-bottom: 8px;
 margin: 24px 0 24px;
}

.section-header h2 {
 font-size: 12px;
 font-weight: 700;
 letter-spacing: 0.12em;
 text-transform: uppercase;
 color: #1a1a1a;
 margin: 0;
}

.section-header a {
 font-size: 12px;
 color: #2d5a3d;
 text-decoration: none;
}

.section-header a:hover { text-decoration: underline; }

.article-card { margin-bottom: 0; }

.card-meta {
 font-size: 10px;
 font-weight: 600;
 letter-spacing: 0.1em;
 text-transform: uppercase;
 color: #888;
 margin: 0 0 4px;
}

.card-title {
 font-size: 17px;
 margin: 0 0 6px;
 font-weight: 600;
}

.card-title a { color: #2d5a3d; text-decoration: none; }

.card-title a:hover { text-decoration: underline; }

.card-summary {
 font-size: 14px;
 color: #555;
 line-height: 1.5;
 margin: 0 0 16px;
}

.card-divider {
 border: none;
 border-top: 1px solid #e8e4dd;
 margin: 0 0 20px;
}

/* Article page */
.article-header {
 padding: 3rem 0 2rem;
 border-bottom: 1px solid var(--border);
 margin-bottom: 2rem;
}

.article-header h1 {
 font-size: 2.25rem;
 margin-bottom: 1rem;
 line-height: 1.2;
}

.article-meta {
 display: flex;
 gap: 1.5rem;
 align-items: center;
 font-size: 0.85rem;
 color: var(--text-light);
}

.article-body {
 max-width: 720px;
 padding: 2rem 0;
}

.article-body p {
 margin-bottom: 1.5rem;
 font-size: 1.05rem;
 line-height: 1.85;
}

.article-body h2 {
 font-size: 1.5rem;
 margin: 2.5rem 0 1rem;
 color: var(--green);
 font-family: system-ui, sans-serif;
 font-weight: 600;
 letter-spacing: 0.02em;
 text-transform: none;
}

.article-body h3 {
 font-size: 1.2rem;
 margin: 2rem 0 0.75rem;
}

.article-body ul, .article-body ol {
 margin: 1.25rem 0 1.5rem 1.5rem;
}

.article-body li {
 margin-bottom: 0.5rem;
 line-height: 1.75;
}

/* Category/listing page */
.listing-grid {
 display: grid;
 grid-template-columns: repeat(3, 1fr);
 gap: 2rem;
 padding: 2rem 0;
}

/* Article hero image */
.article-hero {
 margin: 1.5rem 0 2rem;
 border-radius: 4px;
 overflow: hidden;
 width: 100%;
 aspect-ratio: 16 / 9;
}
.article-hero img {
 width: 100%;
 height: 100%;
 object-fit: cover;
 object-position: center;
 display: block;
}

/* Featured image on homepage */
.featured-image {
 width: 100%;
 aspect-ratio: 16 / 9;
 object-fit: cover;
 object-position: center;
 display: block;
 margin: 16px 0 20px 0;
}

/* Footer nav */
.footer-nav a {
 color: var(--text-light);
 font-size: 0.85rem;
 letter-spacing: 0.04em;
}
.footer-nav a:hover {
 color: var(--green);
}

/* Responsive */
@media (max-width: 768px) {
 .home-grid { grid-template-columns: 1fr; }
 .listing-grid { grid-template-columns: 1fr; }
 .main-nav ul { gap: 1rem; }
 .featured-article h2 { font-size: 1.5rem; }
 .article-header h1 { font-size: 1.75rem; }

/* Share Bar */
.share-bar { display: flex; align-items: center; gap: 10px; margin: 40px 0 32px; padding: 16px 0; border-top: 1px solid #e8e4dd; border-bottom: 1px solid #e8e4dd; }
.share-label { font-size: 11px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: #999; margin-right: 4px; }
.share-btn { display: inline-flex; align-items: center; gap: 5px; padding: 7px 12px; border-radius: 4px; font-size: 12px; text-decoration: none; border: 1px solid #2d5a3d; background: transparent; cursor: pointer; font-family: inherit; color: #2d5a3d; transition: opacity 0.15s; }
.share-btn:hover { opacity: 0.7; }

}
/* Section cards — grid-specific overrides */
.section-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 24px;
  align-items: stretch;
}
.section-cards .article-card {
  border-bottom: none !important;
  padding: 1.5rem !important;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.section-cards .article-card .card-meta {
  margin: 0 !important;
  padding-top: 0 !important;
  font-size: 0.75rem;
  color: var(--text-light);
  letter-spacing: 0.04em;
}
.section-cards .article-card h3.card-title {
  margin: 0 !important;
  padding-top: 0 !important;
  font-size: 1rem;
  font-weight: 600;
  line-height: 1.4;
}
.section-cards .article-card p.card-summary {
  margin: 0 !important;
  font-size: 0.875rem;
  line-height: 1.6;
}
.section-cards .article-card .card-divider { display: none; }
@media (max-width: 768px) {
  .section-cards { grid-template-columns: 1fr; }
}

/* Sidebar preview text — match main content font size */
.sidebar-preview {
  font-size: 0.875rem !important;
  color: var(--text-light) !important;
  line-height: 1.6 !important;
  margin: 4px 0 0 !important;
}
.sidebar-meta {
  font-size: 0.75rem;
  color: #777;
  letter-spacing: 0.04em;
}

/* Footer layout overrides */
#site-footer {
  text-align: left;
  padding: 0;
  margin-top: 0;
}
.footer-inner {
  padding: 48px 0;
}
.footer-inner {
  max-width: 1100px;
  margin: 0 auto;
  padding: 48px 24px;
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr;
  gap: 32px;
  margin-bottom: 32px;
}
.footer-brand h4 {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 12px;
  color: #1a1a1a;
}
.footer-brand p {
  font-size: 0.875rem;
  line-height: 1.65;
  color: #555;
  text-align: left;
}
.footer-nav h5 {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #888;
  margin-bottom: 12px;
}
.footer-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.footer-nav li {
  margin-bottom: 8px;
}
.footer-nav a {
  font-size: 0.875rem;
  color: #555;
  text-decoration: none;
}
.footer-nav a:hover {
  color: #8b6914;
}
.footer-bottom {
  border-top: 1px solid #e0e0e0;
  padding-top: 20px;
}
.footer-bottom p {
  font-size: 0.8rem;
  color: #888;
  margin-bottom: 6px;
}
```

---

## Quick-Reference Checklist for New Pages

- [ ] `<!DOCTYPE html><html lang="en">` with `<head>` meta charset, viewport
- [ ] `<title>` with `| Succession Holding LLC` suffix
- [ ] `<meta name="description">` — 1-2 sentences
- [ ] `<link rel="stylesheet" href="/style.css">`
- [ ] `<link rel="icon" type="image/svg+xml" href="/favicon.svg">`
- [ ] AdSense script tag in `<head>`
- [ ] `<link rel="canonical">` with full URL
- [ ] `#site-utility` and `#site-nav` div placeholders
- [ ] `<main><div class="container">` wrapper
- [ ] `.article-header` with `<h1>`
- [ ] `.article-body` content wrapper
- [ ] `.ad-zone` placeholder(s) where needed
- [ ] AdSense ins block between `</main>` and `#site-footer`
- [ ] Full inline footer HTML in `#site-footer`
- [ ] `<script src="/nav.js"></script>` as last item before `</body>`
- [ ] `</html>` closing tag

---

## Key Differences from Dependability Structure

For reference when cross-referencing against the Dependability site build:

| Aspect | Succession Holding | Dependability |
|--------|-------------------|---------------|
| Nav | `nav.js` injection into empty divs | May differ |
| Footer | Inline static HTML (NOT `footer.js`) | Verify |
| Content wrapper | `.container` + `.article-body` | May use `.main` |
| Article max-width | 720px (`.article-body`) | Verify |
| Ad wrapper | Uses `var(--surface)` (undefined) | Verify |
| Listing grid | `.listing-grid` (3-col) | May differ |
| Homepage grid | `.home-grid` (1fr 300px) | May differ |