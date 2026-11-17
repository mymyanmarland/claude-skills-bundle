---
name: conditional-formatting-dashboard
description: Teaches advanced conditional formatting techniques for dashboard visual signals. Use when the user says things like 'conditional formatting for dashboards', 'traffic light Excel', 'RAG status in Excel'.
---

# Conditional Formatting for Dashboards Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Dashboard conditional formatting: RAG status (Red/Amber/Green traffic light: three conditional rules on each cell) → Icon sets (3-icon set: up/neutral/down arrows / configure the thresholds precisely) → Data bars (in-cell bar chart: length represents the value / useful for ranking tables) → Whole row highlighting (formula rule with fixed column: =$D2='Late' / apply to the full row range) → Colour scales (automatic gradient across a range / draws attention to extremes) → Heat maps (colour scale applied to a matrix of values) → Conditional formatting on PivotTables (applies to the value area / updates with filter changes).

## Step 3 — Quality & Polish

- Formula rules for whole-row highlighting: the most powerful dashboard visual signal technique
- Fix the column in the formula: =$D2 not =D2 — the $ keeps the reference column fixed as the rule applies to the whole row
- Icon sets with custom thresholds: the default icon set thresholds are rarely appropriate — configure them

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
