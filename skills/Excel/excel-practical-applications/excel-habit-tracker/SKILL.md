---
name: excel-habit-tracker
description: Teaches building a daily habit tracker in Excel. Use when the user says things like 'habit tracker Excel', 'daily tracking spreadsheet', 'build a habit tracker Excel'.
---

# Habit Tracker in Excel Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Habit tracker in Excel: Layout (habits in rows / dates in columns — or habits in columns / dates in rows) → Check-off method (1 for done / 0 for missed / or X vs blank) → Streak calculation (=COUNTIF for the current streak: count consecutive 1s from today backwards) → Weekly summary (COUNTIF per habit per week) → Completion rate (=COUNTIF(row,'1')/COUNT(row)) → Conditional formatting (green for done / red for missed / heat map using colour scale) → Yearly overview (52 columns for weeks / GitHub-style contribution map via colour scale) → Monthly summary chart (bar chart of completion rate per habit per month).

## Step 3 — Quality & Polish

- Colour scale for the yearly overview: creates a GitHub-style activity heat map
- Streak formula: the most motivating tracker metric — consecutive days done
- Completion rate per habit: percentage done reveals the habits that need the most attention

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
