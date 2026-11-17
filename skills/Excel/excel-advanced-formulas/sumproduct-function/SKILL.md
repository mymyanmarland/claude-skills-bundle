---
name: sumproduct-function
description: Teaches the versatile SUMPRODUCT function for multi-condition calculations. Use when the user says things like 'SUMPRODUCT Excel', 'how to use SUMPRODUCT', 'multi-condition sum Excel'.
---

# SUMPRODUCT Function Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

SUMPRODUCT: =SUMPRODUCT(array1, array2...) — multiplies arrays element-by-element then sums → Multi-condition SUMIF alternative (=SUMPRODUCT((A:A='X')*(B:B>100)*C:C) — sum C where A is X and B>100) → Count with multiple conditions (=SUMPRODUCT((A:A='X')*(B:B>100)) — counts rows meeting both conditions) → Weighted average (=SUMPRODUCT(weights, values)/SUM(weights)) → Boolean logic (TRUE=1 / FALSE=0 in multiplication — the foundation of SUMPRODUCT conditions) → Performance note (SUMPRODUCT on full columns is slow — limit to used range) → SUMPRODUCT vs COUNTIFS (COUNTIFS is faster for simple counts — use SUMPRODUCT when COUNTIFS cannot handle the logic).

## Step 3 — Quality & Polish

- Limit to used range: SUMPRODUCT on full columns (A:A) is very slow on large sheets
- Boolean multiplication: (condition1)*(condition2) requires BOTH conditions — AND logic
- Boolean addition: (condition1)+(condition2)>0 requires EITHER condition — OR logic

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
