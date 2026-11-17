---
name: hr-workforce-reporting
description: Teaches building HR and headcount reports in Excel. Use when the user says things like 'HR reporting Excel', 'headcount report', 'workforce analytics Excel'.
---

# HR and Workforce Reporting Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

HR workforce reporting: Headcount table (employee / department / grade / start date / status) → Headcount summary (PivotTable: count by department / grade / location) → Attrition rate (=Leavers in period / Average headcount × 100) → Tenure analysis (=TODAY()-start date / DATEDIF for years of service) → Age and gender distribution (COUNTIF by band) → Salary analysis (AVERAGEIF by department / grade) → Recruitment pipeline (open roles / time-to-hire / source of hire) → Absence tracking (days absent / absence rate = days absent / available days).

## Step 3 — Quality & Polish

- DATEDIF for tenure: =DATEDIF(start_date, TODAY(), 'Y') gives complete years of service
- Attrition rate formula: document whether it uses average or end-period headcount — both are common
- Anonymise salary data before sharing: salary data requires strict access controls

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
