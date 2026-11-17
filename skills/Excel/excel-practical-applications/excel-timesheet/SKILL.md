---
name: excel-timesheet
description: Teaches building time tracking spreadsheets in Excel. Use when the user says things like 'timesheet Excel', 'track time in Excel', 'time tracking spreadsheet'.
---

# Timesheet and Time Tracking Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Timesheet template: Time entry (date / project / task / start time / end time / hours: =end-start in TIME format) → Hours calculation (TIME subtraction / format the result as [h]:mm for hours exceeding 24) → Day total (SUM of hours per day) → Weekly total (SUM of all daily totals) → Overtime calculation (=IF(total>40, total-40, 0) for weekly overtime) → Project allocation (SUMIF by project code) → Rate and billing (hours × rate per project / =SUMPRODUCT(hours_range, rate_range)) → Format as [h]:mm (Format Cells / Custom / [h]:mm — essential for totals exceeding 24 hours).

## Step 3 — Quality & Polish

- Format as [h]:mm not h:mm: the square brackets allow totals beyond 24 hours
- SUMIF by project: the most useful timesheet analysis — time spent per project
- SUMPRODUCT for billing: multiplies hours by varying rates across multiple projects

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
