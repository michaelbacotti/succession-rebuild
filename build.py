#!/usr/bin/env python3
"""
Succession Holding LLC — Newsletter build system.

Reads Markdown issues from content/newsletters/<YYYY-MM-DD>-<slug>.md,
renders a per-issue HTML page at newsletters/<slug>/index.html,
and builds a listing page at newsletters/index.html with a wide
.newsletter-hero (latest issue) above a .newsletter-grid (archive).

Newsletter doctrine (Mike 2026-07-12):
  - Anti-hype "decision cockpit" for independent RE investors
  - No top-10 markets fluff; not motivational filler
  - Quality bar: ≥1,500 words per issue
  - SEO: per-issue canonical, meta description, OG tags
  - AdSense: existing 7590828986 (responsive) + 1328672966 (sidebar 300x250)
"""
import os
import re
import sys
from datetime import datetime
from pathlib import Path

WEBSITE_DIR = Path(__file__).parent
CONTENT_DIR = WEBSITE_DIR / "content" / "newsletters"
OUTPUT_DIR = WEBSITE_DIR / "newsletters"
TEMPLATE_FILE = WEBSITE_DIR / "_newsletter_template.html"

DOMAIN = "https://successionholdingllc.com"
AD_CLIENT = "ca-pub-9312870448453345"
AD_SLOT_RESPONSIVE = "7590828986"
AD_SLOT_300x250 = "1328672966"

# ─── Frontmatter ──────────────────────────────────────────────────────────────
def parse_frontmatter(md_text):
    """Extract YAML-style frontmatter and body from MD text."""
    if not md_text.startswith("---"):
        return {}, md_text
    end = md_text.find("\n---", 3)
    if end == -1:
        return {}, md_text
    fm_block = md_text[3:end].strip()
    body = md_text[end + 4:].lstrip("\n")
    meta = {}
    for line in fm_block.split("\n"):
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body

# ─── MD → HTML (limited subset for newsletters) ────────────────────────────────
def md_to_html(md):
    """Convert newsletter MD to HTML with frontmatter already stripped.

    Supported:
      - Paragraphs separated by blank lines
      - # ## ### headings
      - **bold** and *italic*
      - [text](url) links → escapes nothing special (we trust the author)
      - Single-line blockquotes (>-prefixed paragraphs)
      - Bullet lists (- foo, - bar)
      - Numbered lists (1. foo)
      - HR (---)
    """
    lines = md.split("\n")
    out = []
    para = []
    list_kind = None  # None, "ul", "ol"
    in_blockquote = False

    def flush_para():
        nonlocal para, list_kind, in_blockquote
        if para:
            text = " ".join(para).strip()
            if text:
                out.append(f"<p>{inline(text)}</p>")
            para = []
        if list_kind is not None:
            out.append(f"</{list_kind}>")
            list_kind = None
        if in_blockquote:
            out.append("</blockquote>")
            in_blockquote = False

    def inline(text):
        # **bold**
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        # *italic* (but not already inside <strong>)
        text = re.sub(r"(?<![*<\w])\*([^*]+?)\*(?![*\w])", r"<em>\1</em>", text)
        # [text](url) — strip mailto:, do not escape quotes
        text = re.sub(
            r"\[([^\]]+)\]\(([^)]+)\)",
            lambda m: f'<a href="{m.group(2).strip()}" rel="noopener" target="_blank">{m.group(1)}</a>',
            text,
        )
        return text

    def close_list_to(new_kind):
        nonlocal list_kind
        if list_kind and list_kind != new_kind:
            out.append(f"</{list_kind}>")
            list_kind = None

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush_para()
            continue
        # HR
        if line.strip() == "---":
            flush_para()
            out.append("<hr>")
            continue
        # Headings
        if line.startswith("# "):
            flush_para()
            out.append(f"<h2>{inline(line[2:].strip())}</h2>")
            continue
        if line.startswith("## "):
            flush_para()
            out.append(f"<h2>{inline(line[3:].strip())}</h2>")
            continue
        if line.startswith("### "):
            flush_para()
            out.append(f"<h3>{inline(line[4:].strip())}</h3>")
            continue
        # Bullet
        if re.match(r"^[-*]\s+", line):
            flush_para()
            close_list_to("ul")
            if list_kind is None:
                out.append("<ul>")
                list_kind = "ul"
            item = re.sub(r"^[-*]\s+", "", line)
            out.append(f"<li>{inline(item)}</li>")
            continue
        # Numbered
        if re.match(r"^\d+\.\s+", line):
            flush_para()
            close_list_to("ol")
            if list_kind is None:
                out.append("<ol>")
                list_kind = "ol"
            item = re.sub(r"^\d+\.\s+", "", line)
            out.append(f"<li>{inline(item)}</li>")
            continue
        # Blockquote (must start with "> ")
        if line.startswith("> "):
            flush_para()
            if not in_blockquote:
                out.append("<blockquote>")
                in_blockquote = True
            out.append(f"<p>{inline(line[2:])}</p>")
            continue
        # Plain paragraph line — accumulate until blank
        para.append(line)

    flush_para()
    return "\n".join(out)

# ─── Slug from filename ────────────────────────────────────────────────────────
def slug_from_filename(path):
    name = path.stem
    return name

# ─── Per-issue page rendering ──────────────────────────────────────────────────
def render_issue_page(meta, body_html, slug, date_str):
    """Render a single issue page at newsletters/<slug>/index.html."""
    title = meta.get("title", "Untitled Issue")
    summary = meta.get("summary", "")
    description = meta.get("description", summary)
    author = meta.get("author", "Succession Holding Editorial")
    issue_type = meta.get("issue_type", "")
    canonical = f"{DOMAIN}/newsletters/{slug}/"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>{title} — Succession Daily Brief | Succession Holding LLC</title>
 <meta name="description" content="{description}">
 <link rel="canonical" href="{canonical}">
 <meta property="og:type" content="article">
 <meta property="og:title" content="{title}">
 <meta property="og:description" content="{description}">
 <meta property="og:url" content="{canonical}">
 <meta property="og:image" content="{DOMAIN}/og-image.jpg">
 <link rel="stylesheet" href="/style.css">
 <link rel="icon" type="image/svg+xml" href="/favicon.svg">
 <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={AD_CLIENT}" crossorigin="anonymous"></script>
 <script type="application/ld+json">
  {{
   "@context": "https://schema.org",
   "@type": "NewsArticle",
   "headline": "{title}",
   "author": {{"@type": "Organization", "name": "{author}"}},
   "publisher": {{"@type": "Organization", "name": "Succession Holding LLC", "url": "{DOMAIN}/"}},
   "datePublished": "{date_str}",
   "description": "{description}",
   "mainEntityOfPage": {{"@type": "WebPage", "@id": "{canonical}"}},
   "image": "{DOMAIN}/og-image.jpg"
  }}
 </script>
 <!-- Google tag (gtag.js) — GA4 (shared BacottiBot property) -->
 <script async src="https://www.googletagmanager.com/gtag/js?id=G-S6Y52LHEX1"></script>
 <script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-S6Y52LHEX1');
 </script>
</head>
<body>
 <div id="site-utility"></div>
 <div id="site-nav"></div>
 <main>
 <div class="container">
 <div class="article-body">

 <div class="article-header">
  <span class="category" style="display:inline-block;background:var(--green);color:white;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;padding:0.2rem 0.6rem;margin-bottom:0.75rem;">Succession Daily Brief</span>
  <h1>{title}</h1>
  <div class="article-meta">
   <span>{date_str}</span> · <span>{author}</span>{f" · <span>{issue_type.replace('-', ' ').title()}</span>" if issue_type else ""}
  </div>
 </div>

 <div style="margin:2rem 0;padding:.75rem;background:var(--surface);border-radius:var(--radius);text-align:center;">
  <div style="font-size:0.7rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:#888;margin-bottom:8px;">Advertisement</div>
  <ins class="adsbygoogle" style="display:block" data-ad-client="{AD_CLIENT}" data-ad-slot="{AD_SLOT_RESPONSIVE}" data-ad-format="auto" data-full-width-responsive="true"></ins>
 </div>
 <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>

 {body_html}

 <div style="margin:2rem 0;padding:.75rem;background:var(--surface);border-radius:var(--radius);text-align:center;">
  <div style="font-size:0.7rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:#888;margin-bottom:8px;">Advertisement</div>
  <ins class="adsbygoogle" style="display:block" data-ad-client="{AD_CLIENT}" data-ad-slot="{AD_SLOT_RESPONSIVE}" data-ad-format="auto" data-full-width-responsive="true"></ins>
 </div>
 <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>

 <p style="margin-top:3rem;padding-top:1.5rem;border-top:1px solid var(--bg-secondary);font-size:0.85rem;color:var(--text-light);">
  The Succession Daily Brief is a 5-minute intelligence memo for independent real estate investors. <a href="/newsletters/">Browse the full archive →</a>
 </p>

 </div>
 </div>
 </main>
 <div id="site-footer"></div>
 <script src="/nav.js"></script>
 <script src="/footer.js"></script>
</body>
</html>
"""

# ─── Listing page rendering ────────────────────────────────────────────────────
def render_listing(issues):
    """issues: list of dicts with slug, title, date, author, summary, issue_type — newest first."""
    if not issues:
        issues_html = "<p>No issues yet. Check back tomorrow.</p>"
        latest = None
    else:
        latest = issues[0]
        prev = issues[1:]
        # Latest issue hero
        hero = f"""
<article class="nl-hero">
 <div class="nl-hero__meta"><span class="nl-hero__date">{latest['date']}</span> · <span class="nl-hero__author">by {latest['author']}</span> · <span class="nl-hero__chip">Latest Issue</span></div>
 <h2 class="nl-hero__title"><a href="/newsletters/{latest['slug']}/">{latest['title']}</a></h2>
 <p class="nl-hero__summary">{latest['summary']}</p>
 <a href="/newsletters/{latest['slug']}/" class="nl-hero__cta">Read the full brief &rarr;</a>
</article>"""
        # Archive grid
        cards = []
        for issue in prev:
            cards.append(f"""<article class="nl-grid-card">
 <h3 class="nl-grid-card__title"><a href="/newsletters/{issue['slug']}/">{issue['title']}</a></h3>
 <div class="nl-grid-card__meta">{issue['date']} · {issue['author']}{f" · <span class='nl-grid-tag'>{issue['issue_type'].replace('-', ' ').title()}</span>" if issue['issue_type'] else ""}</div>
 <p class="nl-grid-card__summary">{issue['summary']}</p>
 <a href="/newsletters/{issue['slug']}/" class="nl-grid-card__cta">Read the brief &rarr;</a>
</article>""")
        if cards:
            grid = "<div class=\"nl-grid\">\n" + "\n".join(cards) + "\n</div>"
        else:
            grid = "<p style=\"color:var(--text-light);\">More issues coming tomorrow.</p>"
        issues_html = hero + grid

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Newsletters | Succession Holding LLC</title>
 <meta name="description" content="The Succession Daily Brief: a 5-minute intelligence memo for independent real estate investors. Risk, market signals, deal anatomy, fraud & compliance radar — every morning.">
 <link rel="canonical" href="{DOMAIN}/newsletters/">
 <meta property="og:type" content="website">
 <meta property="og:title" content="The Succession Daily Brief">
 <meta property="og:description" content="A 5-minute intelligence memo for independent real estate investors — published every morning.">
 <meta property="og:url" content="{DOMAIN}/newsletters/">
 <meta property="og:image" content="{DOMAIN}/og-image.jpg">
 <link rel="stylesheet" href="/style.css">
 <link rel="icon" type="image/svg+xml" href="/favicon.svg">
 <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={AD_CLIENT}" crossorigin="anonymous"></script>
 <script type="application/ld+json">
  {{
   "@context": "https://schema.org",
   "@type": "CollectionPage",
   "name": "The Succession Daily Brief",
   "description": "Daily intelligence memo for independent real estate investors.",
   "url": "{DOMAIN}/newsletters/"
  }}
 </script>
 <script async src="https://www.googletagmanager.com/gtag/js?id=G-S6Y52LHEX1"></script>
 <script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-S6Y52LHEX1');
 </script>
</head>
<body>
 <div id="site-utility"></div>
 <div id="site-nav"></div>
 <main>
 <div class="container">

 <div class="article-header" style="padding-bottom:1rem;">
  <h1>Succession Daily Brief</h1>
  <p style="color:var(--text-light);font-size:1.05rem;margin-top:0.5rem;">A 5-minute intelligence memo for independent real estate investors. Published every morning at 6 a.m. ET. Risk, market signals, deal anatomy, fraud & compliance — the day's one actionable lens on what changes in the next 30 to 180 days for small owners.</p>
 </div>

 <div style="margin:2rem 0;padding:.75rem;background:var(--surface);border-radius:var(--radius);text-align:center;">
  <div style="font-size:0.7rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:#888;margin-bottom:8px;">Advertisement</div>
  <ins class="adsbygoogle" style="display:block" data-ad-client="{AD_CLIENT}" data-ad-slot="{AD_SLOT_RESPONSIVE}" data-ad-format="auto" data-full-width-responsive="true"></ins>
 </div>
 <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>

 {issues_html}

 <div style="margin:2rem 0;padding:.75rem;background:var(--surface);border-radius:var(--radius);text-align:center;">
  <div style="font-size:0.7rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:#888;margin-bottom:8px;">Advertisement</div>
  <ins class="adsbygoogle" style="display:block" data-ad-client="{AD_CLIENT}" data-ad-slot="{AD_SLOT_RESPONSIVE}" data-ad-format="auto" data-full-width-responsive="true"></ins>
 </div>
 <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>

 </div>
 </main>
 <div id="site-footer"></div>
 <script src="/nav.js"></script>
 <script src="/footer.js"></script>
</body>
</html>
"""

# ─── Load + sort + write ──────────────────────────────────────────────────────
def load_issues():
    issues = []
    if not CONTENT_DIR.exists():
        return issues
    for md_file in sorted(CONTENT_DIR.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        slug = slug_from_filename(md_file)
        date_str = meta.get("date", md_file.stem.split("-")[0:3])
        if isinstance(date_str, list):
            date_str = "-".join(date_str)
        # Pretty date
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            pretty_date = dt.strftime("%B %-d, %Y")
        except Exception:
            pretty_date = date_str
        issues.append({
            "slug": slug,
            "title": meta.get("title", slug),
            "date": pretty_date,
            "date_iso": date_str,
            "author": meta.get("author", "Succession Editorial"),
            "summary": meta.get("summary", ""),
            "description": meta.get("description", meta.get("summary", "")),
            "issue_type": meta.get("issue_type", ""),
            "meta": meta,
            "body": body,
            "filename": md_file.name,
        })
    issues.sort(key=lambda i: i["date_iso"], reverse=True)
    return issues

def build():
    issues = load_issues()
    if not issues:
        print(f"No issues found in {CONTENT_DIR}", file=sys.stderr)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for issue in issues:
        body_html = md_to_html(issue["body"])
        page = render_issue_page(issue["meta"], body_html, issue["slug"], issue["date"])
        issue_dir = OUTPUT_DIR / issue["slug"]
        issue_dir.mkdir(parents=True, exist_ok=True)
        (issue_dir / "index.html").write_text(page, encoding="utf-8")
        print(f"wrote newsletters/{issue['slug']}/index.html")
    listing = render_listing(issues)
    (OUTPUT_DIR / "index.html").write_text(listing, encoding="utf-8")
    print(f"wrote newsletters/index.html ({len(issues)} issues)")
    return issues

if __name__ == "__main__":
    build()
