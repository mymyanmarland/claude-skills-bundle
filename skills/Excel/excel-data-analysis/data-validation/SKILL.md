---
name: data-validation
description: Teaches restricting input with data validation rules. Use when the user says things like 'data validation Excel', 'dropdown list Excel', 'restrict input in Excel cells'.
---

# Data Validation in Excel Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Data validation: Access (Data / Data Validation) → Allow types (Whole Number / Decimal / List / Date / Time / Text Length / Custom formula) → Dropdown list (Allow: List / Source: comma-separated values or a range) → Dynamic dropdown (Source: a named range or Table column — expands automatically) → Custom formula (=LEN(A1)<=10 — validates that text is no more than 10 characters) → Input message (shows a message when the cell is selected) → Error alert (Stop: prevents invalid entry / Warning: allows override / Information: informs only) → Circle Invalid Data (Data / Data Validation / Circle Invalid Data — highlights existing invalid entries).

## Step 3 — Quality & Polish

- Table column as dropdown source: the dropdown grows automatically when new items are added
- Stop vs Warning: Stop prevents entry / Warning allows the user to proceed anyway
- Circle Invalid Data: audits existing data against the validation rule — very useful for imported data

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
