const { test, expect } = require('@playwright/test');

test('Homepage loads without errors', async ({ page }) => {
  const errors = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  page.on('pageerror', err => errors.push(err.message));
  
  await page.goto('https://www.successionholdingllc.com');
  await expect(page.locator('h1, .hero h1, .main-title')).toBeVisible();
  expect(errors).toHaveLength(0);
});

test('Market analysis page loads', async ({ page }) => {
  const errors = [];
  page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  page.on('pageerror', err => errors.push(err.message));
  
  await page.goto('https://www.successionholdingllc.com/market-analysis.html');
  expect(errors).toHaveLength(0);
});

test('Navigation links work', async ({ page }) => {
  await page.goto('https://www.successionholdingllc.com');
  const navLinks = await page.locator('nav a, .nav a').count();
  expect(navLinks).toBeGreaterThan(0);
});

test('Mobile nav works', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 812 });
  await page.goto('https://www.successionholdingllc.com');
  await expect(page.locator('nav, .nav')).toBeVisible();
});