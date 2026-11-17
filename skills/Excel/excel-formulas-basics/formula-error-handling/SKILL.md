---
name: formula-error-handling
description: Teaches identifying and handling Excel formula errors. Use when the user says things like 'fix Excel formula errors', 'what does #N/A mean', 'handle errors in Excel formulas'.
---

# Formula Error Handling Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Error handling: Error types (#N/A: value not found / #REF!: invalid reference / #DIV/0!: division by zero / #VALUE!: wrong data type / #NAME?: unknown function / #NUM!: invalid number / ######: column too narrow) → IFERROR(formula, value_if_error) — catch any error → IFNA(formula, value_if_na) — catch only #N/A → ISERROR / ISNA / ISNUMBER — test for an error type → ISBLANK — test for an empty cell → Trace Precedents / Trace Dependents (Formulas ribbon / auditing tools — see which cells a formula uses) → Evaluate Formula (step through a complex formula to find the error).

## Step 3 — Quality & Polish

- Evaluate Formula: the most useful debugging tool — steps through the formula calculation
- IFNA vs IFERROR: IFNA only catches #N/A — better for lookup error handling
- Trace Precedents: shows visually which cells feed into the selected formula

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
