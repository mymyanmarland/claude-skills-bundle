---
name: pnl-model
description: Teaches building a P&L statement model in Excel. Use when the user says things like 'P&L model Excel', 'build a profit and loss in Excel', 'income statement model'.
---

# Profit and Loss Model Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

P&L model: Revenue (units × price / or revenue growth rate applied to prior year) → Cost of Goods Sold (COGS) (direct costs as % of revenue / or separate unit economics) → Gross Profit (Revenue - COGS) → Operating Expenses (fixed costs: headcount / rent / software / variable costs: % of revenue) → EBITDA (Gross Profit - OpEx) → Depreciation and Amortisation (D&A from the balance sheet build) → EBIT (EBITDA - D&A) → Interest (from the debt schedule) → EBT (EBIT - Interest) → Tax (EBT × tax rate — use IFERROR for negative EBT) → Net Income (EBT - Tax).

## Step 3 — Quality & Polish

- EBITDA is the key operational metric: separate it clearly in the model
- IFERROR on tax: negative EBT should produce zero tax not a negative tax
- Link every line to the Inputs sheet: no hard-coded percentages in the P&L rows

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
