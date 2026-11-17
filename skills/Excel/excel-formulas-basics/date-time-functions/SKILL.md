---
name: date-time-functions
description: Teaches date and time functions for calculations and formatting. Use when the user says things like 'date functions Excel', 'how to calculate dates in Excel', 'Excel date formulas'.
---

# Date and Time Functions Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Date and time functions: TODAY() / NOW() (dynamic — updates every time the file opens) → DATE(year, month, day) — constructs a date from parts → YEAR / MONTH / DAY / HOUR / MINUTE / SECOND — extract date parts → DATEDIF(start, end, 'unit') — difference between dates ('Y' years / 'M' months / 'D' days) → NETWORKDAYS(start, end, [holidays]) — working days between two dates → EDATE(start, months) — add months to a date → EOMONTH(start, months) — last day of a month → Dates are stored as numbers (1 = 1 January 1900 — format cells as dates).

## Step 3 — Quality & Polish

- DATEDIF for age calculations: the most useful date difference function
- NETWORKDAYS for business days: includes or excludes a list of holidays
- Dates are numbers: if a date formula returns a number format it as a date

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
