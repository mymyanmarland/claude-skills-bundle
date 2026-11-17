---
name: vba-workbook-worksheet
description: Teaches automating multi-sheet and multi-workbook operations with VBA. Use when the user says things like 'VBA multiple sheets', 'automate across workbooks VBA', 'loop through worksheets VBA'.
---

# VBA Workbook and Worksheet Automation Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Workbook and worksheet VBA: Reference a worksheet (Worksheets('Sheet1') / Sheets(1) / ActiveSheet) → Loop through sheets (For Each ws In ThisWorkbook.Worksheets / process / Next ws) → Add a sheet (Worksheets.Add(After:=Worksheets(Worksheets.Count)).Name = 'NewSheet') → Delete a sheet (Application.DisplayAlerts = False / Sheets('Old').Delete / Application.DisplayAlerts = True) → Open a workbook (Workbooks.Open Filename:='C:\path\file.xlsx') → Close a workbook (Workbooks('file.xlsx').Close SaveChanges:=True) → Copy sheet to another workbook (Sheet.Copy After:=OtherWb.Sheets(OtherWb.Sheets.Count)).

## Step 3 — Quality & Polish

- DisplayAlerts = False before deleting: prevents the confirmation dialog — remember to re-enable it
- Loop through worksheets: automate the same action on every sheet in one macro
- Qualify sheet references: Worksheets('Sheet1').Range('A1') not just Range('A1') — prevents wrong-sheet errors

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
