---
name: dynamic-array-functions
description: Teaches the modern dynamic array functions in Microsoft 365 Excel. Use when the user says things like 'dynamic array Excel', 'FILTER SORT UNIQUE functions', 'spill formula Excel'.
---

# Dynamic Array Functions Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Dynamic array functions: FILTER(array, include, [if_empty]) — returns rows where condition is TRUE → SORT(array, [sort_index], [sort_order]) — sorts a range dynamically → SORTBY(array, by_array, [sort_order]) — sorts by one or more other ranges → UNIQUE(array, [by_col], [exactly_once]) — returns unique values → SEQUENCE(rows, [cols], [start], [step]) — generates a number sequence → RANDARRAY(rows, cols, min, max, integer) — generates random number arrays → Spill reference (=A1# — refers to the entire spill range of a dynamic array) → Nested dynamic arrays (=SORT(FILTER(data, condition)) — chain functions together).

## Step 3 — Quality & Polish

- FILTER is the most transformative function in modern Excel: replaces complex array formulas and VBA loops
- Spill reference with #: =A1# captures all spilled values dynamically
- Chain dynamic functions: =SORT(UNIQUE(FILTER(data, condition))) — complex results in one formula

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
