# PROJECT_INDEX — Succession Holding (successionholdingllc.com)

> Property Intelligence — Buyer-Facing Property Dossiers
> Last updated: 2026-07-05

## Purpose & Audience

Succession Holding presents physical properties in a structured, intelligence-forward format — not generic real estate listings. Property dossiers provide location, specs, status, history, strategic angles, risks, and inquiry paths for informed buyers and partners.

**Audience:** Sophisticated buyers and partners interested in properties associated with Succession Holding LLC's portfolio. Not mass-market listings — intelligence-grade presentation.

---

## Live-Site Paths

```
entities/succession/website/   ← succession-rebuild GitHub repo
  properties/                   ← Property Dossiers (ALLOWED WRITE PATH)
    active/                    ← currently offering / active
    archived/                  ← disposed or inactive
    templates/                 ← dossier templates
```

**Protected (do not edit without explicit human approval):**
- `about/`, `contact/`, `disclaimer/`, `privacy/`, `education/`
- `build.py`, `_template*`, nav files
- Home page, sitemap, robots.txt

---

## Core Content Lanes

### Property Dossiers
- Location, basic specs (size, type, zoning)
- Current status (active, under contract, sold, archived)
- History and context
- Strategic angles (what could be done with the property)
- Risk and constraint notes
- Inquiry path (contact/lead form)

### Thematic Summaries
- Properties grouped by type, region, or strategy

---

## Monetization

| Method | Where |
|--------|-------|
| Inquiry funnel | Primary — clear CTA on every dossier linking to contact/inquiry |
| AdSense | Sparse — property pages only; trust and positioning more important than ad revenue |

**Note:** Inquiry quality over quantity. These are intelligence-grade presentations, not listing-farm pages.

---

## Key Entities (from entity tracking)

Known properties tracked in `entities/succession/`:
- 38 Alexander Road LLC
- Ashuelot Cabin
- Bacotti Family Trust holdings
- Blackhawk Ranch Cabin
- Colorado City Lots
- Costilla Acres
- Hawthorne Acres
- Sweetwater Acres
- Eagle River Home LLC
- MNC Housing

---

## Status & Pending Tasks

- [ ] LIP-08: First property dossier pilot (recommend starting with a well-documented property)
- [ ] Template files for property dossier
- [ ] Property registry (JSON/spreadsheet)
- [ ] Portfolio view page

---

## Related Documents

- `Reports/LIVING_INTELLIGENCE_PROPERTIES.md` — Succession section
- `Reports/LIVING_INTELLIGENCE_IMPLEMENTATION.md` — §1, §6
- `entities/succession/website/PROJECT_PLAYBOOK.md`
- `skills/succession.property_intel` — deferred skill (revisit when LIP-08 templates finalized)

## Source

Wiki synthesis: `wiki/main/syntheses/living-intelligence-properties-strategy.md`
