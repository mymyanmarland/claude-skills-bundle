---
name: excel-crm
description: Teaches using Excel as a simple CRM for small businesses. Use when the user says things like 'Excel CRM guide', 'customer tracker Excel', 'simple CRM in Excel'.
---

# Excel CRM for Small Business Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Excel CRM: Contact database (company / contact / email / phone / source / status / last contact date) → Activity log (date / contact / type: call/email/meeting / notes / next action) → Pipeline (opportunity / contact / stage / value / expected close / probability) → Follow-up alerts (=IF(last_contact<TODAY()-30,'Overdue','OK') — identifies contacts not contacted in 30 days) → VLOOKUP/XLOOKUP linking (activity log linked to contact database by company name) → Email merge preparation (export filtered data for mail merge) → Monthly reports (new contacts / activities / pipeline value — PivotTable summaries).

## Step 3 — Quality & Polish

- Last contact date alert: the most valuable CRM feature — never let a contact go cold
- Activity log linked to contact database: =XLOOKUP to pull contact details into the activity log
- Export for mail merge: Excel CRM data feeds directly into Word mail merge or email tools

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
