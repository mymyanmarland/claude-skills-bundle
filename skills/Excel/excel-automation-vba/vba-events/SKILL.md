---
name: vba-events
description: Teaches using VBA event procedures to trigger code automatically. Use when the user says things like 'VBA events guide', 'run code when a cell changes', 'Worksheet_Change VBA'.
---

# VBA Worksheet and Workbook Events Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

VBA events: Worksheet_Change (Private Sub Worksheet_Change(ByVal Target As Range) — runs when any cell changes) → Target checking (If Not Intersect(Target, Range('A1:A10')) Is Nothing Then — only react to specific cells) → Worksheet_SelectionChange (runs when the user moves to a different cell) → Workbook_Open (Private Sub Workbook_Open() — runs when the file opens) → Workbook_BeforeSave (runs before saving — validate the data) → Workbook_BeforeClose (runs before closing — prompt to save) → Disable events inside events (Application.EnableEvents = False inside a Change event prevents the event from firing recursively).

## Step 3 — Quality & Polish

- Intersect check in Worksheet_Change: without it the event fires for every cell change on the sheet
- EnableEvents = False inside events: prevents recursive event firing — always re-enable with True
- Workbook_Open for startup tasks: show a welcome form / update data / navigate to a specific sheet

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
