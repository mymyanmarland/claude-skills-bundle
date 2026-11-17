---
name: excel-reporting-automation
description: Teaches automating repetitive reporting tasks in Excel. Use when the user says things like 'automate Excel reports', 'monthly report automation', 'Excel report generation'.
---

# Excel Reporting Automation Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Reporting automation: Power Query for data refresh (one-click data refresh vs manual copy-paste) → Macro for formatting (record the formatting steps / run once per report) → Dynamic dates (=TODAY() / =EOMONTH(TODAY(),-1) — reports that update their period automatically) → Template approach (master template with all formulas / copy for each period / paste values only into the data sheet) → Email distribution macro (VBA: open Outlook / compose email / attach the report / send) → Scheduled refresh (Power Query + VBA macro triggered by Workbook_Open) → PDF export macro (VBA: ActiveSheet.ExportAsFixedFormat Type:=xlTypePDF).

## Step 3 — Quality & Polish

- Power Query refresh replaces manual copy-paste: the highest-impact automation for most reporters
- Template plus paste values: the simplest reporting automation — copy the template monthly
- PDF export via VBA: ActiveSheet.ExportAsFixedFormat — one line of code

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
