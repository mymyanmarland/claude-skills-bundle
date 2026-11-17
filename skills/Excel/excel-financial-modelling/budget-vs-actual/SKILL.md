---
name: budget-vs-actual
description: Teaches building a budget versus actual variance analysis in Excel. Use when the user says things like 'budget vs actual Excel', 'variance analysis model', 'compare budget to actual in Excel'.
---

# Budget vs Actual Model Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Budget vs actual: Structure (Budget / Actual / Variance / Variance% columns for each period) → Variance (=Actual - Budget — be consistent: positive = favourable or unfavourable depending on the line) → Variance direction (Revenue: positive variance is good / Cost: positive variance is bad — flag this clearly) → Percentage variance (=IFERROR(Variance/ABS(Budget), 0)) → YTD columns (use SUMIF or SUM up to the current period) → Traffic light (Conditional Formatting on variance % / green > 5% / red < -5%) → Full-year forecast (=Actual YTD + Remaining Budget — update monthly).

## Step 3 — Quality & Polish

- Consistent variance direction: decide and document whether positive variance is favourable or unfavourable
- IFERROR on variance %: zero budget creates a #DIV/0 error
- Full-year forecast column: the most actionable output of a budget vs actual model

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
