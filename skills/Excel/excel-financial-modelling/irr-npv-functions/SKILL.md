---
name: irr-npv-functions
description: Teaches using IRR, NPV, XIRR, and XNPV for investment analysis. Use when the user says things like 'IRR function Excel', 'NPV calculation Excel', 'XIRR and XNPV guide'.
---

# IRR and NPV Functions Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

IRR and NPV functions: NPV(rate, value1, value2...) (present value of future cash flows — does NOT include the initial investment) → =NPV(rate, future_CFs) + initial_investment (correct NPV formula — add the t=0 cash flow separately) → IRR(values, [guess]) (the discount rate at which NPV equals zero — requires at least one negative cash flow) → XNPV(rate, values, dates) (NPV with actual dates — more accurate for irregular cash flows) → XIRR(values, dates, [guess]) (IRR with actual dates) → Multiple IRRs (some cash flow patterns produce multiple IRRs — XIRR with a guess near the expected rate helps) → MIRR(values, finance_rate, reinvest_rate) (modified IRR — avoids the reinvestment rate assumption).

## Step 3 — Quality & Polish

- NPV does not include t=0: always add the initial investment outside the NPV function
- XIRR over IRR: actual dates give more accurate results than assuming equal periods
- MIRR for more realistic analysis: assumes reinvestment at the cost of capital not the IRR

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
