---
name: vlookup-xlookup
description: Teaches lookup functions for finding values across tables. Use when the user says things like 'how to use VLOOKUP', 'XLOOKUP guide', 'look up a value in Excel'.
---

# VLOOKUP and XLOOKUP Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Lookup functions: VLOOKUP(lookup_value, table_array, col_index, [range_lookup]) → The four arguments (what to find / where to look / which column to return / exact match: FALSE) → VLOOKUP limitation (can only look left to right / the lookup column must be the leftmost) → XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found]) — the modern replacement → XLOOKUP advantages (looks in any direction / returns multiple columns / has a built-in if-not-found argument) → INDEX MATCH (=INDEX(return_column, MATCH(lookup_value, lookup_column, 0)) — the flexible alternative) → MATCH return types (0: exact / 1: less than / -1: greater than).

## Step 3 — Quality & Polish

- XLOOKUP replaces VLOOKUP in modern Excel: more flexible and cleaner syntax
- FALSE for exact match in VLOOKUP: omitting the 4th argument returns wrong results
- INDEX MATCH when XLOOKUP is unavailable: the classic flexible lookup combination

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
