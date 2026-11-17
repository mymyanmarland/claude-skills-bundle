---
name: power-pivot-dax
description: Teaches creating calculated measures in Power Pivot using DAX. Use when the user says things like 'Power Pivot DAX guide', 'DAX formulas Excel', 'calculated measures Power Pivot'.
---

# Power Pivot and DAX Basics Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Power Pivot and DAX: Enable Power Pivot (File / Options / Add-ins / COM Add-ins / Microsoft Power Pivot) → DAX syntax (similar to Excel formulas but operates on tables and columns: Table[Column]) → SUM measure (Total Sales:=SUM(Sales[Amount])) → CALCULATE (Total Sales in 2023:=CALCULATE(SUM(Sales[Amount]), Sales[Year]=2023) — the most important DAX function) → ALL (Remove all filters: =CALCULATE([Total Sales], ALL(Sales))) → RELATED (access a column from a related table) → DATEADD (previous year: CALCULATE([Total Sales], DATEADD(Dates[Date], -1, YEAR))) → Measure vs calculated column (measures are context-sensitive / columns are row-by-row).

## Step 3 — Quality & Polish

- CALCULATE is the cornerstone of DAX: almost every useful measure uses CALCULATE
- Measures not calculated columns: measures respond to filter context / columns are static
- ALL to remove filters: the most common DAX technique for percentage-of-total calculations

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
