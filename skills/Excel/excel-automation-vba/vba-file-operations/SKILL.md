---
name: vba-file-operations
description: Teaches using VBA to automate file management and batch processing. Use when the user says things like 'VBA file operations', 'open and process files with VBA', 'batch process Excel files'.
---

# VBA File Operations Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

VBA file operations: FileSystemObject (Dim fso As Object / Set fso = CreateObject('Scripting.FileSystemObject')) → Check file exists (fso.FileExists(path)) → Get all files in a folder (Dir(path & '*.xlsx') — loops through matching files) → Loop through files (Dim f As String / f = Dir(path) / Do While f <> '' / process / f = Dir / Loop) → Copy a file (fso.CopyFile source, destination) → Move a file (fso.MoveFile source, destination) → Create a folder (fso.CreateFolder path) → Save as new name (ActiveWorkbook.SaveAs filename).

## Step 3 — Quality & Polish

- Dir loop for batch processing: the standard method for processing all files in a folder
- FileExists check before opening: prevents runtime errors on missing files
- SaveAs within the loop: save each processed file with a new name before moving to the next

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
