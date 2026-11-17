---
name: regression-analysis
description: Teaches performing linear regression in Excel. Use when the user says things like 'regression analysis Excel', 'linear regression Excel', 'LINEST and trendline guide'.
---

# Regression Analysis in Excel Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Regression analysis: Add a trendline (chart / right-click a data series / Add Trendline / Linear / Display Equation and R-squared) → LINEST function (=LINEST(known_ys, known_xs, TRUE, TRUE) — array formula / returns slope / intercept / R² and more) → FORECAST.LINEAR (=FORECAST.LINEAR(x_value, known_ys, known_xs) — predicts y for a given x) → Data Analysis ToolPak Regression (Data / Data Analysis / Regression / select Y and X ranges / output: coefficients / R² / p-values) → Interpreting R² (1.0 = perfect fit / 0.7+ = strong / below 0.5 = weak) → Multiple regression (multiple X columns in the ToolPak regression tool).

## Step 3 — Quality & Polish

- Display equation on the trendline: the slope and intercept tell you the relationship
- R-squared above 0.7: a reasonable threshold for a useful predictive relationship
- ToolPak regression for multiple variables: LINEST handles it but ToolPak output is easier to read

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
