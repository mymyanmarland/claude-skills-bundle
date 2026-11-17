---
name: excel-performance-optimisation
description: Teaches techniques for making large or slow Excel workbooks faster. Use when the user says things like 'Excel is slow', 'speed up Excel', 'optimise large Excel workbook'.
---

# Excel Performance Optimisation Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Excel performance optimisation: Identify the cause (Formulas / Check for Errors / or CTRL+END to find the used range) → Volatile functions (avoid INDIRECT / OFFSET / NOW / TODAY / RAND in large models — they recalculate on every change) → Calculation mode (Formulas / Calculation Options / Manual — press F9 to recalculate when ready) → Replace VLOOKUPs with INDEX MATCH or XLOOKUP (VLOOKUPs on large ranges are slow) → Reduce used range (Ctrl+End shows the last used cell — delete unused rows and columns beyond the data) → Power Query over formulas (aggregations in Power Query are faster than SUMIF on 100k+ rows) → Binary format (.xlsb files are smaller and open faster than .xlsx).

## Step 3 — Quality & Polish

- Manual calculation mode for large models: prevents recalculation on every keystroke
- Volatile function audit: find and replace INDIRECT and OFFSET with non-volatile alternatives
- .xlsb for large files: smaller file size and faster open/save than .xlsx

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
