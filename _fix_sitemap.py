#!/usr/bin/env python3
"""Fix successionholdingllc.com sitemap: remove .html suffix from all URLs to match canonicals."""
sitemap = "/Users/mike/.openclaw/workspace-bacottibot/websites/succession-rebuild-2026-05-13/sitemap.xml"

with open(sitemap, "r") as f:
    content = f.read()

# Remove .html from all non-article URLs
# articles/ URLs don't redirect but canonicals match sitemap, so keep those
content = content.replace("https://successionholdingllc.com/index.html", "https://successionholdingllc.com/")
content = content.replace("https://successionholdingllc.com/about.html", "https://successionholdingllc.com/about")
content = content.replace("https://successionholdingllc.com/articles.html", "https://successionholdingllc.com/articles")
content = content.replace("https://successionholdingllc.com/contact.html", "https://successionholdingllc.com/contact")
content = content.replace("https://successionholdingllc.com/disclaimer.html", "https://successionholdingllc.com/disclaimer")
content = content.replace("https://successionholdingllc.com/education.html", "https://successionholdingllc.com/education")
content = content.replace("https://successionholdingllc.com/investing.html", "https://successionholdingllc.com/investing")
content = content.replace("https://successionholdingllc.com/market-analysis.html", "https://successionholdingllc.com/market-analysis")
content = content.replace("https://successionholdingllc.com/privacy.html", "https://successionholdingllc.com/privacy")
# articles/ URLs - remove .html from sitemap to match canonical-less URLs that actually work
content = content.replace("https://successionholdingllc.com/articles/", "https://successionholdingllc.com/articles/")
# Actually keep article URLs as-is since they work with .html and canonical is also .html
# Only fix the subdirectory with .html that causes issues
content = content.replace("https://successionholdingllc.com/articles/2026-05-13-corporate-housing-ban/index.html", "https://successionholdingllc.com/articles/2026-05-13-corporate-housing-ban/")

with open(sitemap, "w") as f:
    f.write(content)

print("Done. Sitemap URLs:")
with open(sitemap) as f:
    for line in f:
        if '<loc>' in line:
            print(line.strip().replace('<loc>','').replace('</loc>',''))