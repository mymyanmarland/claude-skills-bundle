---
name: model-error-checking
description: Teaches systematic error checking for financial models. Use when the user says things like 'check my financial model', 'error checking Excel model', 'audit an Excel financial model'.
---

# Financial Model Error Checking Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Model error checking: Balance check (=IF(Assets-Liabilities-Equity=0,'OK','ERROR') — on the balance sheet) → Sum check (=SUM of subtotals vs =SUM of all line items — should match) → Sign check (revenue should be positive / costs negative or positive depending on convention — verify consistently) → Circular reference check (Formulas / Error Checking / Circular References — identify and resolve) → Precedent tracing (Formulas / Trace Precedents — verify each formula draws from the right cell) → Error cells (Formulas / Error Checking — finds all formula errors in the sheet) → Hard-code audit (Ctrl+` to toggle formula view — spot any unexplained numbers).

## Step 3 — Quality & Polish

- Ctrl+` to see all formulas: the fastest way to spot hard-coded numbers in calculation cells
- Balance check formula at the top of the balance sheet: if it says ERROR stop everything
- Circular reference check before sharing: circulars produce inconsistent results on different machines

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
