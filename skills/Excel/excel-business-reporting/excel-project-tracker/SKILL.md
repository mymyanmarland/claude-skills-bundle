---
name: excel-project-tracker
description: Teaches building a project management tracker in Excel. Use when the user says things like 'project tracker Excel', 'Gantt chart Excel', 'task management spreadsheet'.
---

# Project Tracker in Excel Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Project tracker: Task list (task / owner / start date / end date / duration / status / % complete) → Gantt chart (conditional formatting bar chart: =AND(date>=start, date<=end) creates the bar) → Status column (dropdown: Not Started / In Progress / Complete / Blocked) → Colour coding (Conditional Formatting: green=Complete / amber=In Progress / red=Blocked) → % complete (progress bar with Data Bar conditional formatting) → Summary (COUNTIF by status / % complete overall) → Critical path (manually flag tasks where delay impacts the end date) → Milestones (zero-duration tasks / different Gantt colour).

## Step 3 — Quality & Polish

- Gantt via conditional formatting: more maintainable than complex chart-based Gantts
- Dropdown for status: standardises entries — free text produces inconsistent data
- COUNTIF summary by status: instant visibility of project health

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
