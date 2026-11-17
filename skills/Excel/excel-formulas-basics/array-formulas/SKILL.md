---
name: array-formulas
description: Teaches array formulas for multi-cell calculations. Use when the user says things like 'array formula Excel', 'Ctrl Shift Enter Excel', 'multi-cell formula Excel'.
---

# Array Formulas and CTRL+SHIFT+ENTER Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Array formulas: What arrays are (formulas that operate on multiple values simultaneously) → Ctrl+Shift+Enter (legacy array entry — wraps formula in curly braces {}) → Dynamic arrays in Microsoft 365 (FILTER / SORT / UNIQUE / SEQUENCE — spill automatically into cells below) → FILTER(array, include, [if_empty]) — return rows that meet a condition → SORT(array) — sort a range → UNIQUE(array) — return unique values → SEQUENCE(rows, cols, start, step) — generate a sequence of numbers → Spill range reference (#) — the entire spill range of a dynamic array formula.

## Step 3 — Quality & Polish

- Dynamic arrays replace most Ctrl+Shift+Enter formulas in Microsoft 365
- FILTER replaces complex VLOOKUP and IF combinations: the most powerful modern Excel function
- # reference to the spill range: =A1# refers to all spilled values from A1

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
