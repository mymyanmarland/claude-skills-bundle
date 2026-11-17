---
name: excel-personal-finance
description: Teaches building a personal finance tracking system in Excel. Use when the user says things like 'personal finance Excel', 'track my spending Excel', 'expense tracker spreadsheet'.
---

# Personal Finance Tracker Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Personal finance tracker: Transaction log (date / description / category / amount / account) → Category dropdown (Data Validation / List) → Monthly summary (SUMIF by category / SUMIF by month) → Income vs expenses (total income / total expenses / net) → Savings rate (=(income-expenses)/income) → Category chart (pie or bar chart of spending by category) → Net worth tracker (assets: savings / investments / property / liabilities: debts / net = assets-liabilities) → Year-over-year comparison (SUMIFS by year and month) → Bank import (copy from bank statement / use Flash Fill to standardise the categories).

## Step 3 — Quality & Polish

- Category dropdown for consistency: free text categories create dozens of variations of the same thing
- SUMIFS for flexible filtering: filter by month AND category simultaneously
- Flash Fill for bank import: quickly standardise imported bank transaction descriptions

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
