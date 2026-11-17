---
name: forecast-functions
description: Teaches using Excel's forecasting functions for trend projection. Use when the user says things like 'forecast in Excel', 'FORECAST.ETS guide', 'predict future values Excel'.
---

# Forecasting Functions in Excel Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Forecasting functions: FORECAST.LINEAR(x, known_ys, known_xs) — linear trend extrapolation → FORECAST.ETS(target_date, values, timeline) — exponential triple smoothing / handles seasonality → FORECAST.ETS.SEASONALITY — detects the seasonal period automatically → Forecast Sheet (select time series data / Data / Forecast Sheet — generates a complete forecast with confidence intervals) → Confidence interval (the shaded area on the Forecast Sheet / wider = less certain) → Smoothing (FORECAST.ETS_ALPHA / BETA / GAMMA parameters control smoothing) → Limitation (forecasting assumes the past predicts the future — conditions change).

## Step 3 — Quality & Polish

- Forecast Sheet: the fastest forecasting tool in Excel — one click for a complete projection with confidence intervals
- FORECAST.ETS over FORECAST.LINEAR: handles seasonality that linear forecasting misses
- Confidence interval width signals certainty: narrow = more certain / wide = less certain

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
