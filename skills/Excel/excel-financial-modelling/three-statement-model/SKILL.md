---
name: three-statement-model
description: Teaches linking P&L, Balance Sheet, and Cash Flow in a three-statement model. Use when the user says things like 'three statement model Excel', 'link P&L balance sheet cash flow', 'integrated financial model'.
---

# Three-Statement Financial Model Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Three-statement model: P&L (revenue / costs / net income — flows to retained earnings on balance sheet) → Balance Sheet (assets = liabilities + equity / the balancing check: =Assets-Liabilities-Equity should equal zero) → Cash Flow Statement (Operating: Net Income + D&A - Working Capital changes / Investing: CapEx / Financing: debt and equity changes) → The balance check (a three-statement model that does not balance has an error — the cash flow statement is the reconciliation) → Working capital (=Current Assets - Current Liabilities / changes flow to the Cash Flow Statement) → Circular reference (interest on debt → interest expense → net income → cash → debt repayment → interest — use iterative calculation or a revolving credit facility).

## Step 3 — Quality & Polish

- The balance check must equal zero: if the balance sheet does not balance there is a model error
- Cash flow statement as the reconciliation: the change in cash must equal the movement on the balance sheet
- Iterative calculation for circularity: File / Options / Formulas / Enable Iterative Calculation

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
