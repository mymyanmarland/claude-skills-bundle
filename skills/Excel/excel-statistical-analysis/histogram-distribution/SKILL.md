---
name: histogram-distribution
description: Teaches creating histograms and frequency distributions in Excel. Use when the user says things like 'histogram Excel', 'frequency distribution Excel', 'FREQUENCY function guide'.
---

# Histograms and Frequency Distribution Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Histograms: Insert histogram (select data / Insert / Charts / Histogram — Excel 2016+) → Bin width adjustment (double-click the axis / Format Axis / Bin Width — adjust the bin size) → FREQUENCY function (=FREQUENCY(data_array, bins_array) — Ctrl+Shift+Enter array formula) → Bin setup (create bin boundaries in a column / FREQUENCY counts values in each bin) → Cumulative frequency (=SUM of FREQUENCY running total / useful for percentile analysis) → Normal distribution overlay (NORM.DIST function to generate the expected normal curve for comparison) → Interpretation (roughly bell-shaped: normally distributed / skewed: non-normal).

## Step 3 — Quality & Polish

- Adjust bin width in the histogram chart: default bins are rarely the most informative
- FREQUENCY as an array formula: Ctrl+Shift+Enter in older Excel / or wrap in SUMPRODUCT
- Compare to normal distribution: plotting NORM.DIST over the histogram reveals the distribution shape

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
