---
name: dynamic-charts
description: Teaches creating charts that update automatically as data changes. Use when the user says things like 'dynamic charts Excel', 'auto-updating charts', 'chart that updates with new data'.
---

# Dynamic Charts in Excel Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Dynamic charts: Table-based charts (convert data to a Table / charts based on Tables auto-expand) → Named range with OFFSET (=OFFSET(Sheet1!$A$1,0,0,COUNTA(Sheet1!$A:$A),1) — dynamic range that grows) → INDIRECT for dynamic source (=INDIRECT('Sheet1!'&A1&':'&B1) — reference built from cell values) → Dropdown-driven chart (CHOOSE or INDEX formula selects different data series based on a dropdown) → Camera tool (Insert / Camera / takes a live snapshot of a range — place the chart anywhere) → Sparklines (Insert / Sparklines — mini charts in single cells that update automatically).

## Step 3 — Quality & Polish

- Table-based charts: the simplest dynamic chart method — just convert the data to a Table
- Dropdown-driven series: one chart shows different metrics based on a dropdown selection
- Camera tool for layout flexibility: place a live-updating chart image anywhere on the sheet

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
