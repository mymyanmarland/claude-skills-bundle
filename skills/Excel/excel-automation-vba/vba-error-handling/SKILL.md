---
name: vba-error-handling
description: Teaches handling runtime errors in VBA code. Use when the user says things like 'VBA error handling', 'On Error in VBA', 'handle errors in Excel macros'.
---

# VBA Error Handling Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

VBA error handling: On Error GoTo label (redirects to an error handler when an error occurs) → Error handler label (ErrorHandler: / MsgBox 'Error: ' & Err.Description / Resume Next or Exit Sub) → On Error Resume Next (skip the error and continue — use sparingly / only around a specific line) → On Error GoTo 0 (re-enables normal error handling after Resume Next) → Err object (Err.Number / Err.Description — the error details) → Defensive coding (check before acting: If fso.FileExists(path) Then / avoids errors entirely) → Debug.Print (writes to the Immediate Window — useful for tracking variable values during development).

## Step 3 — Quality & Polish

- On Error Resume Next sparingly: masking all errors hides real bugs
- Err.Description in the message: tells the user what went wrong not just that something went wrong
- Debug.Print for development: the VBA equivalent of a console.log — invaluable for debugging

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
