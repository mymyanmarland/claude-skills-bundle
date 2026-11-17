---
name: dcf-model
description: Teaches building a Discounted Cash Flow valuation model in Excel. Use when the user says things like 'DCF model Excel', 'discounted cash flow guide', 'build a valuation in Excel'.
---

# DCF Valuation Model Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

DCF model: Free Cash Flow (EBIT × (1-tax) + D&A - CapEx - Change in Working Capital) → Projection period (typically 5-10 years) → Terminal Value (Gordon Growth: FCF_final × (1+g) / (WACC-g) / or Exit Multiple: EBITDA × multiple) → WACC (Weighted Average Cost of Capital: Ke×E/(D+E) + Kd×(1-t)×D/(D+E)) → Discount factors (=1/(1+WACC)^period — period is 0.5 for mid-year convention) → PV of FCFs (FCF × discount factor for each period) → Enterprise Value (Sum of PV of FCFs + PV of Terminal Value) → Equity Value (Enterprise Value - Net Debt).

## Step 3 — Quality & Polish

- Mid-year convention: discounting at 0.5 / 1.5 / 2.5 is more accurate than 1 / 2 / 3
- Sensitivity table on WACC and growth rate: the two most impactful DCF assumptions
- Terminal Value is typically 70-80% of Enterprise Value: challenge it carefully

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
