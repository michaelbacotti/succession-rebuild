# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: tests/e2e/succession.spec.js >> Homepage loads without errors
- Location: tests/e2e/succession.spec.js:3:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: locator('h1, .hero h1, .main-title')
Expected: visible
Timeout: 5000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 5000ms
  - waiting for locator('h1, .hero h1, .main-title')

```

```yaml
- navigation:
  - link "Succession Holding LLC":
    - /url: /
  - text: Real estate insight for independent investors
  - link "Contact":
    - /url: /contact.html
- link "Home":
  - /url: /
- link "Investing":
  - /url: /investing.html
- link "Market Analysis":
  - /url: /market-analysis.html
- link "Education":
  - /url: /education.html
- link "About":
  - /url: /about.html
- main:
  - text: ADVERTISEMENT Market Analysis
  - heading "Wall Street Out of Your Neighborhood? What the Corporate Housing Ban Means for Real Estate Investors" [level=2]
  - text: May 13, 2026
  - img "Corporate housing ban"
  - paragraph: The Senate passed a sweeping ban on institutional investors buying single-family homes 89-10. Here is what independent investors need to understand before it becomes law.
  - link "Read the full analysis →":
    - /url: /articles/2026-05-13-corporate-housing-ban/
  - heading "Latest" [level=4]
  - paragraph: MARKET ANALYSIS · MAY 13, 2026
  - link "Wall Street Out of Your Neighborhood?":
    - /url: /articles/2026-05-13-corporate-housing-ban/
  - paragraph: "Something rare happened in Washington this spring: a piece of housing legislation passed the U.S. Senate 89 to 10."
  - paragraph: EDUCATION · MAY 6, 2026
  - link "Landlord vs. Tenant Markets":
    - /url: /articles/2026-05-06-landlord-vs-tenant-markets.html
  - paragraph: In some markets, landlords hold the leverage — vacancy is low, demand is strong, and rent increases are easy to implement. In others, tenants hold the upper hand.
  - paragraph: INVESTING · MAY 5, 2026
  - link "How to Analyze a Rental Property":
    - /url: /articles/2026-05-05-how-to-analyze-rental-property.html
  - paragraph: Evaluating a rental property is not a single calculation — it is a multi-step process combining financial analysis, physical inspection, and market context.
  - paragraph: EDUCATION · MAY 4, 2026
  - link "What Is a Cap Rate?":
    - /url: /articles/2026-05-04-what-is-a-cap-rate.html
  - paragraph: The capitalization rate is one of the most frequently referenced metrics in real estate investing — understanding it prevents costly first-time mistakes.
  - heading "Investing" [level=2]
  - link "View all →":
    - /url: /investing
  - paragraph: INVESTING · May 5, 2026
  - 'heading "How to Analyze a Rental Property: The Complete Investor Checklist" [level=3]':
    - 'link "How to Analyze a Rental Property: The Complete Investor Checklist"':
      - /url: /articles/2026-05-05-how-to-analyze-rental-property.html
  - paragraph: Evaluating a rental property requires running the right numbers and checking the right boxes. Here is a complete checklist for serious investors.
  - paragraph: INVESTING · May 5, 2026
  - 'heading "Leveraging Equity: Cash-Out Refinances and HELOCs for Investment" [level=3]':
    - 'link "Leveraging Equity: Cash-Out Refinances and HELOCs for Investment"':
      - /url: /articles/2026-05-05-leveraging-equity.html
  - paragraph: Using the equity in your existing properties to fund new acquisitions is one of the most common wealth-building strategies in real estate.
  - paragraph: INVESTING · May 12, 2026
  - 'heading "The Multi-Family Outlook: 2026 and Beyond" [level=3]':
    - 'link "The Multi-Family Outlook: 2026 and Beyond"':
      - /url: /articles/2026-05-12-multi-family-outlook.html
  - paragraph: Rising construction costs and persistent demand in mid-sized metros are reshaping the multi-family investment landscape heading into the second half of 2026.
  - heading "Market Analysis" [level=2]
  - link "View all →":
    - /url: /market-analysis
  - paragraph: MARKET ANALYSIS · May 13, 2026
  - heading "Wall Street Out of Your Neighborhood? What the Corporate Housing Ban Means for Real Estate Investors" [level=3]:
    - link "Wall Street Out of Your Neighborhood? What the Corporate Housing Ban Means for Real Estate Investors":
      - /url: /articles/2026-05-13-corporate-housing-ban/
  - paragraph: "Something rare happened in Washington this spring: a piece of housing legislation passed the U.S. Senate 89 to 10."
  - paragraph: MARKET ANALYSIS · May 12, 2026
  - 'heading "Suburban Housing Trends: What the 2026 Data Says" [level=3]':
    - 'link "Suburban Housing Trends: What the 2026 Data Says"':
      - /url: /articles/2026-05-12-suburban-housing-trends.html
  - paragraph: The suburban housing market has undergone a significant shift over the past eighteen months.
  - paragraph: MARKET ANALYSIS · May 6, 2026
  - heading "The Rental Market Landscape in 2026" [level=3]:
    - link "The Rental Market Landscape in 2026":
      - /url: /articles/2026-05-06-rental-market-landscape.html
  - paragraph: Rental rates have stabilized in many markets after several years of volatility. Understanding where supply and demand are balanced is essential for evaluating rental investment opportunities.
  - heading "Education" [level=2]
  - link "View all →":
    - /url: /education
  - paragraph: EDUCATION · May 4, 2026
  - heading "What Is a Cap Rate? A Clear Explanation for Real Estate Investors" [level=3]:
    - link "What Is a Cap Rate? A Clear Explanation for Real Estate Investors":
      - /url: /articles/2026-05-04-what-is-a-cap-rate.html
  - paragraph: The capitalization rate is one of the most frequently referenced metrics in real estate investing.
  - paragraph: EDUCATION · May 3, 2026
  - 'heading "Understanding NOI: The Foundation of Real Estate Investment Analysis" [level=3]':
    - 'link "Understanding NOI: The Foundation of Real Estate Investment Analysis"':
      - /url: /articles/2026-05-03-understanding-noi.html
  - paragraph: Net Operating Income is the single most important number in real estate investment analysis.
  - paragraph: EDUCATION · May 1, 2026
  - 'heading "Property Taxes and Investment Returns: A Practical Guide" [level=3]':
    - 'link "Property Taxes and Investment Returns: A Practical Guide"':
      - /url: /articles/2026-05-01-property-taxes-and-returns.html
  - paragraph: Property taxes are one of the largest carrying costs for any real estate investment — often the second-largest expense after mortgage interest.
- insertion:
  - iframe
- navigation:
  - link "Privacy Policy":
    - /url: /privacy.html
  - text: ·
  - link "About":
    - /url: /about.html
- paragraph: © 2026 Succession Holding LLC. All rights reserved.
- paragraph: This site is for educational purposes only. Not financial advice. Consult a licensed professional before making investment decisions.
```

# Test source

```ts
  1  | const { test, expect } = require('@playwright/test');
  2  | 
  3  | test('Homepage loads without errors', async ({ page }) => {
  4  |   const errors = [];
  5  |   page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  6  |   page.on('pageerror', err => errors.push(err.message));
  7  |   
  8  |   await page.goto('https://www.successionholdingllc.com');
> 9  |   await expect(page.locator('h1, .hero h1, .main-title')).toBeVisible();
     |                                                           ^ Error: expect(locator).toBeVisible() failed
  10 |   expect(errors).toHaveLength(0);
  11 | });
  12 | 
  13 | test('Market analysis page loads', async ({ page }) => {
  14 |   const errors = [];
  15 |   page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  16 |   page.on('pageerror', err => errors.push(err.message));
  17 |   
  18 |   await page.goto('https://www.successionholdingllc.com/market-analysis.html');
  19 |   expect(errors).toHaveLength(0);
  20 | });
  21 | 
  22 | test('Navigation links work', async ({ page }) => {
  23 |   await page.goto('https://www.successionholdingllc.com');
  24 |   const navLinks = await page.locator('nav a, .nav a').count();
  25 |   expect(navLinks).toBeGreaterThan(0);
  26 | });
  27 | 
  28 | test('Mobile nav works', async ({ page }) => {
  29 |   await page.setViewportSize({ width: 375, height: 812 });
  30 |   await page.goto('https://www.successionholdingllc.com');
  31 |   await expect(page.locator('nav, .nav')).toBeVisible();
  32 | });
```