---
name: kpi-cards
description: Teaches building KPI summary cards at the top of a dashboard. Use when the user says things like 'KPI cards Excel', 'summary metrics dashboard Excel', 'build KPI tiles in Excel'.
---

# KPI Cards and Summary Metrics Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

KPI cards: Cell-based KPI card (merge cells / large bold number / label below / border or fill) → Conditional icon (IF formula returns an arrow emoji or symbol based on the value) → Comparison metric (actual vs target: =IFERROR(actual/target-1, 0) as a percentage) → Delta arrow (=IF(delta>0,'▲','▼')&TEXT(ABS(delta),'0.0%')) → Colour-coded background (Conditional Formatting / formula rule: =$B2>$C2 / green fill) → No merged cells for linked data (merged cells prevent formula references — use Centre Across Selection instead) → Linked to a single source cell (change the source / the KPI updates automatically).

## Step 3 — Quality & Polish

- Centre Across Selection instead of Merge: looks merged but is not — formulas still work
- Delta arrows with emoji: ▲▼ in a TEXT formula creates dynamic directional indicators
- Link to one source cell: all KPI calculations point to a single data source

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
