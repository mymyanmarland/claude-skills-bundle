---
name: vba-fundamentals
description: Teaches the core VBA concepts for writing Excel macros. Use when the user says things like 'learn VBA Excel', 'VBA basics guide', 'write VBA code Excel'.
---

# VBA Fundamentals Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

VBA fundamentals: VBA Editor (Alt+F11) → Module (Insert / Module — where code is written) → Sub procedure (Sub MacroName() ... End Sub) → Variables (Dim x As Integer / Dim s As String / Dim rng As Range) → Objects (Workbook / Worksheet / Range / Cell — the Excel object hierarchy) → Properties (Range('A1').Value = 'Hello' / Worksheets('Sheet1').Name) → Methods (Range('A1').Select / Worksheets.Add) → Looping (For i = 1 To 10 ... Next i / For Each cell In Range ... Next cell) → Conditionals (If x > 10 Then ... Else ... End If) → MsgBox (MsgBox 'Done!' — shows a popup message).

## Step 3 — Quality & Polish

- Dim all variables: undeclared variables in VBA default to Variant — slower and error-prone
- For Each for ranges: faster and more readable than For i looping through cells
- MsgBox for debugging: the simplest VBA debugging tool — shows the current value

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
