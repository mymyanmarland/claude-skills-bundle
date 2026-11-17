---
name: t-test-excel
description: Teaches performing t-tests for comparing means in Excel. Use when the user says things like 't-test Excel', 'compare two groups Excel', 'statistical significance Excel'.
---

# T-Test in Excel Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

T-test in Excel: T.TEST(array1, array2, tails, type) — returns the p-value → Tails (1: one-tailed / 2: two-tailed — use 2 for most comparisons) → Type (1: paired / 2: two-sample equal variance / 3: two-sample unequal variance — use 3 if unsure) → P-value interpretation (p < 0.05: statistically significant at 95% confidence / p < 0.01: 99% confidence) → Data Analysis ToolPak t-test (Data / Data Analysis / t-Test: Two-Sample — more detailed output including t-statistic and critical value) → Effect size (statistical significance does not mean practical significance — always check effect size).

## Step 3 — Quality & Polish

- Use type 3 if unsure: two-sample assuming unequal variance is the safe default
- P < 0.05 is the conventional threshold: not a universal truth — context matters
- Effect size alongside p-value: a small p-value from a large sample may not be practically meaningful

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
