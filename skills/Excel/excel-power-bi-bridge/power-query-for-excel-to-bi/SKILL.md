---
name: power-query-for-excel-to-bi
description: Teaches Power Query techniques that work well in both Excel and Power BI. Use when the user says things like 'Power Query best practices', 'write good Power Query M code', 'Power Query for both Excel and Power BI'.
---

# Power Query Best Practices for Excel and Power BI Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Power Query best practices: Rename all steps (Applied Steps panel: double-click a step to rename / 'Filtered to last 12 months' not 'Filtered Rows') → Disable load for intermediate queries (right-click query / Load Enabled / uncheck — prevents loading to the Data Model) → Parameters for flexible queries (Manage Parameters / create a parameter / reference in filter steps) → Append queries for combining tables (Append is Union / Merge is Join) → Document the M code (add comments in Advanced Editor: // comment) → Handle errors in Power Query (Add Column / Column from Examples / or try ... otherwise expressions) → Test on a subset (filter to 100 rows while building the query).

## Step 3 — Quality & Polish

- Rename Applied Steps: Power Query steps become unreadable with default names
- Disable load for staging queries: intermediate transformation steps do not need to load to the model
- Parameters for dynamic queries: a parameter lets the user change a value without editing the M code

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
