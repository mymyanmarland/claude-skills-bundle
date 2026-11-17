---
name: google-sheets-formulas
description: Teaches the key Google Sheets functions that differ from Excel. Use when the user says things like 'Google Sheets formulas guide', 'Sheets functions different from Excel', 'QUERY and IMPORTRANGE Google Sheets'.
---

# Key Google Sheets Functions Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Google Sheets key functions: QUERY(data, query, [headers]) — SQL-like queries: =QUERY(A:D,'SELECT A,B WHERE C>100 ORDER BY B') → IMPORTRANGE(spreadsheet_url, range_string) — import data from another Google Sheet → IMPORTHTML / IMPORTXML / IMPORTDATA — import web data → ARRAYFORMULA — apply a formula to a range without Ctrl+Shift+Enter → SPLIT(text, delimiter) — splits text into columns (equivalent to TEXTSPLIT in Excel) → REGEXEXTRACT / REGEXREPLACE / REGEXMATCH — regular expression text functions → SPARKLINE(data, options) — in-cell sparklines with formatting options.

## Step 3 — Quality & Polish

- QUERY: the most powerful Sheets function — SQL syntax for spreadsheet data
- IMPORTRANGE: share data between Google Sheets without copying — automatically refreshes
- ARRAYFORMULA instead of Ctrl+Shift+Enter: Sheets equivalent of Excel array entry

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
