---
name: excel-learning-tracker
description: Teaches tracking learning progress and skills development in Excel. Use when the user says things like 'learning tracker Excel', 'skills development spreadsheet', 'track my courses and certifications'.
---

# Skills and Learning Tracker Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Learning tracker: Course log (course name / provider / start date / end date / status / certificate) → Skill inventory (skill / current level 1-5 / target level / gap: =target-current) → Learning time log (date / topic / duration / type: course/book/practice) → Monthly hours (SUMIF by month) → Progress chart (radar chart of current skill levels) → Certificate tracker (certification / issuing body / earned date / expiry date / renewal alert) → Goal setting (target skill levels / target completion dates / DATEDIF for days remaining) → Resource list (books / courses / links by skill area).

## Step 3 — Quality & Polish

- Radar chart for skills overview: instantly shows strength and gap across all skill areas
- Renewal alert: =IF(expiry<TODAY()+90,'Renew Soon','') — 90-day advance warning
- Monthly hours SUMIF: tracking time invested by month shows consistency

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
