# SITE MEMORY — Succession Holding LLC

## Identity
- Entity: Succession Holding LLC (real estate education publication)
- Purpose: Independent real estate education — investing, market analysis, financing, property management
- Live URL: successionholdingllc.com (Cloudflare Pages)
- Repo: github.com/michaelbacotti/succession-rebuild
- Architecture: Flat HTML — see skills/website-flat-html.md

## Design System
- Accent: forest green (#2d5a3d) or terracotta (#b85c38)
- Background: white
- Text: dark charcoal
- Fonts: Georgia serif headings, system-ui body
- Ad placement zones: above-fold, in-article, sidebar, between cards

## File Roles
- /style.css — ALL styles
- /nav.js — Site-wide nav
- /footer.js — Site-wide footer
- /_template.html — Base for new pages

## Critical Rules
- All paths to style.css, nav.js, footer.js must start with /
- No build step. No Hugo. No GitHub Actions.
- No financial advice — include disclaimer where appropriate

## Change Log
- 2026-05-13 — Initial build