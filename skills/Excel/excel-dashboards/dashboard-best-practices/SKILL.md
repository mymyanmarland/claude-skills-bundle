---
name: dashboard-best-practices
description: Compiles best practices for building, maintaining, and sharing Excel dashboards. Use when the user says things like 'Excel dashboard best practices', 'professional Excel dashboard tips', 'share and maintain an Excel dashboard'.
---

# Excel Dashboard Best Practices Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Dashboard best practices: Single source of truth (all data flows from one place — no manual entry on the dashboard) → Clear data refresh instructions (document how and when to refresh the data) → Error handling (IFERROR on every formula — a dashboard showing #N/A is unprofessional) → Locked input cells (protect formula cells / only allow editing in the designated input cells) → Sharing (OneDrive / SharePoint for collaborative access / PDF for read-only distribution) → Version log (a notes cell or sheet recording changes) → Performance (avoid volatile functions: NOW/RAND/INDIRECT on large datasets — they recalculate constantly).

## Step 3 — Quality & Polish

- IFERROR on every dashboard formula: #N/A on a dashboard destroys credibility
- Avoid volatile functions on large dashboards: INDIRECT and NOW recalculate on every change — very slow
- Single source of truth: if data is entered in multiple places it will eventually disagree

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
