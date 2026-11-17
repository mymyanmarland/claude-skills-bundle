---
name: lambda-function
description: Teaches creating custom reusable functions with LAMBDA and simplifying formulas with LET. Use when the user says things like 'LAMBDA Excel guide', 'LET function Excel', 'create custom functions Excel'.
---

# LAMBDA and LET Functions Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

LAMBDA and LET: LET(name1, value1, name2, value2..., calculation) — assign names to intermediate values → LET example (=LET(rate, A1/12, nper, B1*12, PMT(rate, nper, -C1)) — readable PMT formula with named parts) → LAMBDA(parameter, formula) — creates a reusable custom function → Name a LAMBDA (define it as a Named Range / then call it by name anywhere in the workbook) → LAMBDA example (=Name Manager / New / Name: Tax / Refers To: =LAMBDA(income, IF(income>50000, income*0.4, income*0.2))) → Call the function (=Tax(A1)) → Recursive LAMBDA (LAMBDA that calls itself — can replace loops for some problems).

## Step 3 — Quality & Polish

- LET for readable complex formulas: name the intermediate calculations and the formula becomes self-documenting
- Named LAMBDA: define once in the Name Manager and use it like a built-in function anywhere in the workbook
- LAMBDA replaces some VBA: custom functions without writing a UDF in VBA

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
