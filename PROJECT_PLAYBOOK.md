# PROJECT_PLAYBOOK — Succession Holding Property Intelligence (successionholdingllc.com)

> How to work in the Succession Holding Property Dossiers
> Last updated: 2026-07-05

---

## How to Create a Property Dossier

1. **Get property details** from:
   - `entities/succession/` folder (tax files, notes, entity records)
   - `entities/[property-entity]/notes/` for entity-specific notes
   - Known public records

2. **Fill the template** using `templates/property_dossier_template.md`:
   - Property name/address
   - Entity that holds it (LLC)
   - Basic specs: parcel size, zoning, improvements, access
   - Current status: active / under contract / sold / archived
   - History: acquisition date, context, what has happened since
   - Strategic angles: what a buyer could do with it, development potential, etc.
   - Risks and constraints: zoning restrictions, access issues, environmental, financial
   - Inquiry CTA: clear next step for interested buyers

3. **Save to:** `properties/active/[property-slug].md`
   - Example: `eagle-river-home.md`, `ashuelot-cabin.md`

4. **Update index.** Add entry to `properties/index.md` (property master list).

5. **Quality check:**
   - Are facts verified against entity records?
   - Are risks disclosed honestly?
   - Does the inquiry path work?
   - Is this appropriate for public disclosure? (Some entity details may need to stay private — use judgment.)

6. **Approval:** Property dossiers involving sensitive financial details, unlisted seller information, or anything that could affect negotiating position should get human review before publishing.

---

## How to Archive a Property

When a property is disposed or no longer active:
1. Move the file from `properties/active/` to `properties/archived/`
2. Update `properties/index.md` to reflect archived status
3. Add a final status note: disposal date, sale price (if public), outcome summary

---

## How to Create a Portfolio View

1. **Gather active properties** from `properties/active/`

2. **Group by theme** (region, property type, strategy)

3. **Create a summary page** at `properties/portfolios/[theme-slug].md`:
   - Theme name
   - Properties in this portfolio view
   - Common characteristics
   - Individual links to each dossier

---

## Templates to Use

| Template | Location | Use for |
|----------|----------|---------|
| `property_dossier_template.md` | `entities/succession/website/properties/templates/` | Property dossiers |
| `portfolio_view_template.md` | `entities/succession/website/properties/templates/` | Portfolio summary pages |

---

## Approval Workflow

| Action | Who approves |
|--------|-------------|
| New dossier (factual, non-sensitive) | Agent can publish |
| Dossier involving sensitive financial details | Human review required |
| Dossier involving unlisted seller information | Human review required |
| Archiving a property | Agent can act |
| Portfolio view creation | Human review recommended |
| Changes to home page, nav, or legal pages | Human required |

---

## Quality Bar

- Dossiers: honest, intelligence-grade, not promotional
- Risks: disclosed, not minimized
- Specs: accurate from entity records, not estimated
- CTA: functional inquiry path on every active dossier

---

## Data Sources

Primary sources (in priority order):
1. Entity records in `entities/[entity-name]/`
2. Tax files in `entities/[entity-name]/tax/`
3. Notes in `entities/[entity-name]/notes/`
4. MEMORY.md (for high-level property facts)

---

## Reference

- Implementation §6.1, §6.2
- `Reports/LIVING_INTELLIGENCE_PROPERTIES.md` — Succession section
- `entities/succession/website/PROJECT_INDEX.md`
