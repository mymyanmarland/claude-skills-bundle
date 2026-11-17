---
name: vba-loops-conditionals
description: Teaches using loops and conditionals to automate repetitive tasks. Use when the user says things like 'VBA loops guide', 'For Each loop Excel VBA', 'loop through rows VBA'.
---

# VBA Loops and Conditionals Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

VBA loops and conditionals: For Next loop (For i = 1 To lastRow / process row i / Next i) → For Each loop (For Each cell In Range('A1:A100') / If cell.Value > 100 Then ... / Next cell) → Do While loop (Do While condition / code / Loop — runs while condition is true) → Do Until loop (Do Until condition / code / Loop) → Select Case (Select Case x / Case 1: / Case 2: / Case Else: / End Select — cleaner than nested If) → Exit For (exits the loop early when a condition is met) → Application.ScreenUpdating = False (turn off screen refresh for speed).

## Step 3 — Quality & Polish

- ScreenUpdating = False: makes loops dramatically faster — turn back to True at the end
- For Each over a named range: cleaner and faster than indexing by row number
- Select Case for multiple conditions: much cleaner than ElseIf chains

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
