---
name: index-match-advanced
description: Teaches advanced INDEX MATCH techniques beyond basic lookups. Use when the user says things like 'advanced INDEX MATCH', 'two-way lookup Excel', 'multiple criteria MATCH'.
---

# Advanced INDEX MATCH Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Advanced INDEX MATCH: Two-way lookup (=INDEX(table, MATCH(row_value, row_labels, 0), MATCH(col_value, col_labels, 0)) — finds the intersection) → Multi-criteria MATCH (=INDEX(C:C, MATCH(1, (A:A=x)*(B:B=y), 0)) — Ctrl+Shift+Enter for array or wrap in SUMPRODUCT) → MATCH with wildcards (MATCH('*partial*', range, 0) — finds a partial text match) → MATCH for column number (=MATCH('Column Name', headers, 0) — dynamic column reference) → INDEX returning an array (=INDEX(A:A, N(IF(1, {1,5,10}))) — return multiple non-contiguous cells).

## Step 3 — Quality & Polish

- Two-way lookup with double MATCH: the most powerful lookup technique
- Multi-criteria array MATCH with Ctrl+Shift+Enter: returns the row where multiple conditions are all met
- MATCH for dynamic column references: =INDEX(data, row, MATCH(header, headers, 0)) adapts to column order changes

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
