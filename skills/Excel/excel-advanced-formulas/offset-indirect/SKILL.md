---
name: offset-indirect
description: Teaches OFFSET and INDIRECT for dynamic range references. Use when the user says things like 'OFFSET function Excel', 'INDIRECT formula guide', 'dynamic range reference Excel'.
---

# OFFSET and INDIRECT Functions Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

OFFSET and INDIRECT: OFFSET(reference, rows, cols, [height], [width]) — returns a range offset from a starting point → Dynamic SUM with OFFSET (=SUM(OFFSET(A1, 0, 0, COUNTA(A:A), 1)) — sums a dynamic range) → Rolling 12-month window (=SUM(OFFSET(B1, 0, MATCH(TODAY()-365, dates, 1), 1, 12))) → INDIRECT(ref_text) — returns the range referred to by a text string → Indirect sheet reference (=INDIRECT(A1&'!B2') — references cell B2 on the sheet named in A1) → Indirect named range (=SUM(INDIRECT(A1)) — sum a named range whose name is in A1) → Performance (both OFFSET and INDIRECT are volatile — recalculate every time — use sparingly).

## Step 3 — Quality & Polish

- OFFSET and INDIRECT are volatile: every sheet change recalculates them — slow on large workbooks
- INDIRECT for dynamic sheet references: =INDIRECT(A1&'!B2') uses the sheet named in cell A1
- OFFSET for rolling windows: sum the last N periods without updating the formula manually

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
