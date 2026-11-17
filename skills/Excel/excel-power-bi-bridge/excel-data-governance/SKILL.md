---
name: excel-data-governance
description: Teaches managing data quality, access control, and governance in Excel workbooks. Use when the user says things like 'Excel data governance', 'data quality Excel', 'control access to Excel data'.
---

# Excel Data Governance Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Excel data governance: Data validation (restrict input / prevent garbage data entering the model) → Sheet and workbook protection (Review / Protect — prevent accidental changes) → Password protection (File / Info / Protect Workbook / Encrypt with Password — for sensitive data) → Audit trail (a log sheet where VBA records changes: who changed what and when) → File naming convention (ProjectName_Report_YYYYMM_v01.xlsx — version and date in the filename) → Backup strategy (OneDrive version history / regular local backups) → Sensitivity labels (Microsoft Purview: label files as Confidential / Restricted — enforces access policies) → Documentation (a ReadMe sheet explaining the workbook structure).

## Step 3 — Quality & Polish

- Audit trail via VBA: Worksheet_Change event logs every change with a timestamp
- Sensitivity labels for confidential data: especially important for HR and financial data
- ReadMe sheet in every workbook: future users need to understand the structure without asking the author

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
