---
name: loan-amortisation
description: Teaches building a loan amortisation schedule in Excel. Use when the user says things like 'loan amortisation Excel', 'mortgage schedule Excel', 'build a repayment schedule in Excel'.
---

# Loan Amortisation Schedule Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Loan amortisation: PMT function (=PMT(rate/12, nper, -pv) — monthly payment for a loan) → Schedule layout (Period / Payment / Principal / Interest / Closing Balance) → Interest (=Opening Balance × monthly rate) → Principal (=Payment - Interest) → Closing Balance (=Opening Balance - Principal) → Opening Balance (=prior period Closing Balance) → Dynamic schedule (IF formula to stop when balance reaches zero: =IF(D10>0, PMT(...), 0)) → Extra payments (add an extra payment column / deduct from principal / recalculate balance) → Total interest paid (=SUM of all interest column - sum of principal).

## Step 3 — Quality & Polish

- PMT function for the payment: the core of any amortisation schedule
- IF formula to stop at zero: without it the schedule runs negative after payoff
- Extra payment column: the most practical addition for mortgage planning

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
