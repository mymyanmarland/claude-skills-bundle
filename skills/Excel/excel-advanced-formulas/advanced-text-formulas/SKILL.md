---
name: advanced-text-formulas
description: Teaches complex text manipulation using formula combinations. Use when the user says things like 'advanced text formulas Excel', 'extract text from a cell Excel', 'parse text with formulas'.
---

# Advanced Text Formula Techniques Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Advanced text formulas: Extract before a delimiter (=LEFT(A1, FIND(',',A1)-1) — extracts the text before the first comma) → Extract after a delimiter (=MID(A1, FIND(',',A1)+1, LEN(A1)) — extracts after the first comma) → Extract between delimiters (=MID(A1, FIND('(',A1)+1, FIND(')',A1)-FIND('(',A1)-1)) → Count occurrences of a character (=LEN(A1)-LEN(SUBSTITUTE(A1,',','')) — counts commas in A1) → Pad with leading zeros (=TEXT(A1,'00000') — 5-digit padded number) → TEXTSPLIT (=TEXTSPLIT(A1, ',') — splits text into an array by delimiter / Microsoft 365 only) → TEXTBEFORE / TEXTAFTER (Microsoft 365: cleaner delimiter extraction).

## Step 3 — Quality & Polish

- TEXTSPLIT in Microsoft 365: replaces the FIND/MID approach with a single readable function
- LEN minus SUBSTITUTE to count characters: a classic Excel technique for any delimiter count
- TEXT function for zero-padded numbers: =TEXT(A1,'000') ensures three digits always

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
