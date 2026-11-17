---
name: if-function
description: Teaches the IF function and logical operators for conditional formulas. Use when the user says things like 'IF function Excel', 'how to use IF in Excel', 'conditional formula Excel'.
---

# IF Function and Logic Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

IF function: =IF(logical_test, value_if_true, value_if_false) → Simple IF (=IF(A1>100,'High','Low')) → Nested IF (=IF(A1>100,'High',IF(A1>50,'Medium','Low')) — limit nesting to 3 levels) → IFS function (=IFS(A1>100,'High',A1>50,'Medium',TRUE,'Low') — cleaner than nested IF) → AND / OR with IF (=IF(AND(A1>100,B1='Yes'),'Both Met','Not Met')) → IFERROR (=IFERROR(formula, 'Error') — replaces errors with a message) → IFBLANK pattern (=IF(A1='','',formula) — prevents formula from running on empty cells).

## Step 3 — Quality & Polish

- IFS instead of nested IF: cleaner and easier to read — use for 3+ conditions
- IFERROR wraps fragile formulas: prevents #N/A and #DIV/0 from showing to users
- AND and OR as IF logical tests: multiple conditions without multiple nested IFs

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
