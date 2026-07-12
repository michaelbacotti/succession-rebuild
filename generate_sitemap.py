#!/usr/bin/env python3
"""
Succession Holding LLC — Sitemap Generator
Scans website/ directory, generates sitemap.xml with proper directory-style URLs.
Run manually whenever articles are added/removed.
"""
import os
from datetime import datetime

WEBSITE_DIR = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://successionholdingllc.com"

# Static section pages that map directory → URL
# These are the top-level sections of the site
STATIC_SECTIONS = [
    ("about", 0.8, "monthly"),
    ("contact", 0.5, "monthly"),
    ("disclaimer", 0.5, "monthly"),
    ("education", 0.7, "monthly"),
    ("investing", 0.9, "weekly"),
    ("market-analysis", 0.9, "weekly"),
    ("newsletters", 0.9, "daily"),  # Daily Brief — 6am ET, Mike 2026-07-12
    ("privacy", 0.5, "monthly"),
    ("terms", 0.5, "monthly"),
]

ARTICLES_DIR = os.path.join(WEBSITE_DIR, "articles")
NEWSLETTERS_DIR = os.path.join(WEBSITE_DIR, "newsletters")

def scan_articles():
    """Find all article subdirectories that contain an index.html."""
    articles = []
    if not os.path.isdir(ARTICLES_DIR):
        return articles
    for name in sorted(os.listdir(ARTICLES_DIR)):
        article_path = os.path.join(ARTICLES_DIR, name)
        if os.path.isdir(article_path) and os.path.isfile(os.path.join(article_path, "index.html")):
            if name != "index.html":  # skip the articles index page subdirectory
                articles.append(name)
    return articles

def scan_newsletters():
    """Find all newsletter issues — subdirectories of newsletters/ with index.html."""
    issues = []
    if not os.path.isdir(NEWSLETTERS_DIR):
        return issues
    for name in sorted(os.listdir(NEWSLETTERS_DIR)):
        issue_path = os.path.join(NEWSLETTERS_DIR, name)
        if os.path.isdir(issue_path) and os.path.isfile(os.path.join(issue_path, "index.html")):
            if name != "index.html":
                issues.append(name)
    return issues

def generate_sitemap():
    urls = []

    # Homepage
    urls.append({
        "loc": f"{DOMAIN}/",
        "priority": "1.0",
        "changefreq": "weekly",
    })

    # Static section pages
    for section, priority, freq in STATIC_SECTIONS:
        section_path = os.path.join(WEBSITE_DIR, section, "index.html")
        if os.path.isfile(section_path):
            urls.append({
                "loc": f"{DOMAIN}/{section}/",
                "priority": str(priority),
                "changefreq": freq,
            })

    # Articles listing (if articles/index.html exists)
    articles_listing = os.path.join(ARTICLES_DIR, "index.html")
    if os.path.isfile(articles_listing):
        urls.append({
            "loc": f"{DOMAIN}/articles/",
            "priority": "0.9",
            "changefreq": "weekly",
        })

    # Individual articles
    for slug in scan_articles():
        urls.append({
            "loc": f"{DOMAIN}/articles/{slug}/",
            "priority": "0.7",
            "changefreq": "monthly",
        })

    # Newsletter issues — daily cadence; each issue contributes a page
    for slug in scan_newsletters():
        urls.append({
            "loc": f"{DOMAIN}/newsletters/{slug}/",
            "priority": "0.6",
            "changefreq": "monthly",
        })

    # Build XML
    today = datetime.now().strftime("%Y-%m-%d")
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<!-- Generated: {today} by generate_sitemap.py -->',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{url['loc']}</loc>")
        lines.append(f"    <changefreq>{url['changefreq']}</changefreq>")
        lines.append(f"    <priority>{url['priority']}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")

    return "\n".join(lines) + "\n"

def main():
    sitemap_xml = generate_sitemap()
    out_path = os.path.join(WEBSITE_DIR, "sitemap.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print(f"Generated: {out_path}")
    print(f"URL count: {sitemap_xml.count('<url>')}")
    print("\nAll URLs:")
    for line in sitemap_xml.split("\n"):
        if "<loc>" in line:
            print(" ", line.strip().replace("<loc>", "").replace("</loc>", ""))

if __name__ == "__main__":
    main()