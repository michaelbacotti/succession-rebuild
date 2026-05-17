# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: tests/e2e/succession.spec.js >> Mobile nav works
- Location: tests/e2e/succession.spec.js:28:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: locator('nav, .nav')
Expected: visible
Error: strict mode violation: locator('nav, .nav') resolved to 2 elements:
    1) <nav class="top-bar">…</nav> aka getByText('Succession Holding LLC Real')
    2) <nav class="footer-nav">…</nav> aka getByText('Privacy Policy · About')

Call log:
  - Expect "toBeVisible" with timeout 5000ms
  - waiting for locator('nav, .nav')

```

# Page snapshot

```yaml
- generic [active] [ref=e1]:
  - navigation [ref=e3]:
    - link "Succession Holding LLC" [ref=e4] [cursor=pointer]:
      - /url: /
    - link "Contact" [ref=e6] [cursor=pointer]:
      - /url: /contact.html
  - generic [ref=e9]:
    - link "Home" [ref=e10] [cursor=pointer]:
      - /url: /
    - link "Investing" [ref=e11] [cursor=pointer]:
      - /url: /investing.html
    - link "Market Analysis" [ref=e12] [cursor=pointer]:
      - /url: /market-analysis.html
    - link "Education" [ref=e13] [cursor=pointer]:
      - /url: /education.html
    - link "About" [ref=e14] [cursor=pointer]:
      - /url: /about.html
  - main [ref=e15]:
    - generic [ref=e16]:
      - generic [ref=e17]: ADVERTISEMENT
      - generic [ref=e18]:
        - generic [ref=e20]:
          - generic [ref=e21]: Market Analysis
          - heading "Wall Street Out of Your Neighborhood? What the Corporate Housing Ban Means for Real Estate Investors" [level=2] [ref=e22]
          - text: May 13, 2026
          - img "Corporate housing ban" [ref=e23]
          - paragraph [ref=e24]: The Senate passed a sweeping ban on institutional investors buying single-family homes 89-10. Here is what independent investors need to understand before it becomes law.
          - link "Read the full analysis →" [ref=e25] [cursor=pointer]:
            - /url: /articles/2026-05-13-corporate-housing-ban/
        - generic [ref=e27]:
          - heading "Latest" [level=4] [ref=e28]
          - generic [ref=e29]:
            - paragraph [ref=e30]: MARKET ANALYSIS · MAY 13, 2026
            - link "Wall Street Out of Your Neighborhood?" [ref=e31] [cursor=pointer]:
              - /url: /articles/2026-05-13-corporate-housing-ban/
            - paragraph [ref=e32]: "Something rare happened in Washington this spring: a piece of housing legislation passed the U.S. Senate 89 to 10."
          - generic [ref=e33]:
            - paragraph [ref=e34]: EDUCATION · MAY 6, 2026
            - link "Landlord vs. Tenant Markets" [ref=e35] [cursor=pointer]:
              - /url: /articles/2026-05-06-landlord-vs-tenant-markets.html
            - paragraph [ref=e36]: In some markets, landlords hold the leverage — vacancy is low, demand is strong, and rent increases are easy to implement. In others, tenants hold the upper hand.
          - generic [ref=e37]:
            - paragraph [ref=e38]: INVESTING · MAY 5, 2026
            - link "How to Analyze a Rental Property" [ref=e39] [cursor=pointer]:
              - /url: /articles/2026-05-05-how-to-analyze-rental-property.html
            - paragraph [ref=e40]: Evaluating a rental property is not a single calculation — it is a multi-step process combining financial analysis, physical inspection, and market context.
          - generic [ref=e41]:
            - paragraph [ref=e42]: EDUCATION · MAY 4, 2026
            - link "What Is a Cap Rate?" [ref=e43] [cursor=pointer]:
              - /url: /articles/2026-05-04-what-is-a-cap-rate.html
            - paragraph [ref=e44]: The capitalization rate is one of the most frequently referenced metrics in real estate investing — understanding it prevents costly first-time mistakes.
      - generic [ref=e45]:
        - heading "Investing" [level=2] [ref=e46]
        - link "View all →" [ref=e47] [cursor=pointer]:
          - /url: /investing
      - generic [ref=e48]:
        - generic [ref=e49]:
          - paragraph [ref=e50]: INVESTING · May 5, 2026
          - 'heading "How to Analyze a Rental Property: The Complete Investor Checklist" [level=3] [ref=e51]':
            - 'link "How to Analyze a Rental Property: The Complete Investor Checklist" [ref=e52] [cursor=pointer]':
              - /url: /articles/2026-05-05-how-to-analyze-rental-property.html
          - paragraph [ref=e53]: Evaluating a rental property requires running the right numbers and checking the right boxes. Here is a complete checklist for serious investors.
        - generic [ref=e54]:
          - paragraph [ref=e55]: INVESTING · May 5, 2026
          - 'heading "Leveraging Equity: Cash-Out Refinances and HELOCs for Investment" [level=3] [ref=e56]':
            - 'link "Leveraging Equity: Cash-Out Refinances and HELOCs for Investment" [ref=e57] [cursor=pointer]':
              - /url: /articles/2026-05-05-leveraging-equity.html
          - paragraph [ref=e58]: Using the equity in your existing properties to fund new acquisitions is one of the most common wealth-building strategies in real estate.
        - generic [ref=e59]:
          - paragraph [ref=e60]: INVESTING · May 12, 2026
          - 'heading "The Multi-Family Outlook: 2026 and Beyond" [level=3] [ref=e61]':
            - 'link "The Multi-Family Outlook: 2026 and Beyond" [ref=e62] [cursor=pointer]':
              - /url: /articles/2026-05-12-multi-family-outlook.html
          - paragraph [ref=e63]: Rising construction costs and persistent demand in mid-sized metros are reshaping the multi-family investment landscape heading into the second half of 2026.
      - generic [ref=e64]:
        - heading "Market Analysis" [level=2] [ref=e65]
        - link "View all →" [ref=e66] [cursor=pointer]:
          - /url: /market-analysis
      - generic [ref=e67]:
        - generic [ref=e68]:
          - paragraph [ref=e69]: MARKET ANALYSIS · May 13, 2026
          - heading "Wall Street Out of Your Neighborhood? What the Corporate Housing Ban Means for Real Estate Investors" [level=3] [ref=e70]:
            - link "Wall Street Out of Your Neighborhood? What the Corporate Housing Ban Means for Real Estate Investors" [ref=e71] [cursor=pointer]:
              - /url: /articles/2026-05-13-corporate-housing-ban/
          - paragraph [ref=e72]: "Something rare happened in Washington this spring: a piece of housing legislation passed the U.S. Senate 89 to 10."
        - generic [ref=e73]:
          - paragraph [ref=e74]: MARKET ANALYSIS · May 12, 2026
          - 'heading "Suburban Housing Trends: What the 2026 Data Says" [level=3] [ref=e75]':
            - 'link "Suburban Housing Trends: What the 2026 Data Says" [ref=e76] [cursor=pointer]':
              - /url: /articles/2026-05-12-suburban-housing-trends.html
          - paragraph [ref=e77]: The suburban housing market has undergone a significant shift over the past eighteen months.
        - generic [ref=e78]:
          - paragraph [ref=e79]: MARKET ANALYSIS · May 6, 2026
          - heading "The Rental Market Landscape in 2026" [level=3] [ref=e80]:
            - link "The Rental Market Landscape in 2026" [ref=e81] [cursor=pointer]:
              - /url: /articles/2026-05-06-rental-market-landscape.html
          - paragraph [ref=e82]: Rental rates have stabilized in many markets after several years of volatility. Understanding where supply and demand are balanced is essential for evaluating rental investment opportunities.
      - generic [ref=e83]:
        - heading "Education" [level=2] [ref=e84]
        - link "View all →" [ref=e85] [cursor=pointer]:
          - /url: /education
      - generic [ref=e86]:
        - generic [ref=e87]:
          - paragraph [ref=e88]: EDUCATION · May 4, 2026
          - heading "What Is a Cap Rate? A Clear Explanation for Real Estate Investors" [level=3] [ref=e89]:
            - link "What Is a Cap Rate? A Clear Explanation for Real Estate Investors" [ref=e90] [cursor=pointer]:
              - /url: /articles/2026-05-04-what-is-a-cap-rate.html
          - paragraph [ref=e91]: The capitalization rate is one of the most frequently referenced metrics in real estate investing.
        - generic [ref=e92]:
          - paragraph [ref=e93]: EDUCATION · May 3, 2026
          - 'heading "Understanding NOI: The Foundation of Real Estate Investment Analysis" [level=3] [ref=e94]':
            - 'link "Understanding NOI: The Foundation of Real Estate Investment Analysis" [ref=e95] [cursor=pointer]':
              - /url: /articles/2026-05-03-understanding-noi.html
          - paragraph [ref=e96]: Net Operating Income is the single most important number in real estate investment analysis.
        - generic [ref=e97]:
          - paragraph [ref=e98]: EDUCATION · May 1, 2026
          - 'heading "Property Taxes and Investment Returns: A Practical Guide" [level=3] [ref=e99]':
            - 'link "Property Taxes and Investment Returns: A Practical Guide" [ref=e100] [cursor=pointer]':
              - /url: /articles/2026-05-01-property-taxes-and-returns.html
          - paragraph [ref=e101]: Property taxes are one of the largest carrying costs for any real estate investment — often the second-largest expense after mortgage interest.
  - insertion [ref=e103]
  - generic [ref=e106]:
    - navigation [ref=e107]:
      - link "Privacy Policy" [ref=e108] [cursor=pointer]:
        - /url: /privacy.html
      - text: ·
      - link "About" [ref=e109] [cursor=pointer]:
        - /url: /about.html
    - paragraph [ref=e110]: © 2026 Succession Holding LLC. All rights reserved.
    - paragraph [ref=e111]: This site is for educational purposes only. Not financial advice. Consult a licensed professional before making investment decisions.
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
  9  |   await expect(page.locator('h1, .hero h1, .main-title')).toBeVisible();
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
> 31 |   await expect(page.locator('nav, .nav')).toBeVisible();
     |                                           ^ Error: expect(locator).toBeVisible() failed
  32 | });
```