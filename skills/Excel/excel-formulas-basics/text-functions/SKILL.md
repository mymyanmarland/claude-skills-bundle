---
name: text-functions
description: Teaches text manipulation functions for cleaning and transforming data. Use when the user says things like 'text functions Excel', 'clean text data in Excel', 'manipulate strings in Excel'.
---

# Text Functions in Excel Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Text functions: LEFT(text, num_chars) / RIGHT(text, num_chars) / MID(text, start, num_chars) → LEN(text) — number of characters → TRIM(text) — removes leading, trailing, and double spaces → UPPER / LOWER / PROPER — change case → CONCATENATE or & operator (='Hello '&A1&' World') → TEXTJOIN(delimiter, ignore_empty, text1, text2...) — joins text with a delimiter → SUBSTITUTE(text, old_text, new_text) — replace text → FIND / SEARCH (find a text position: SEARCH is case-insensitive) → TEXT(value, format) — convert number to formatted text.

## Step 3 — Quality & Polish

- TRIM before any text analysis: invisible spaces cause lookup failures and comparison errors
- TEXTJOIN over CONCATENATE: handles arrays and ignores blanks automatically
- TEXT for number formatting: =TEXT(A1,'DD/MM/YYYY') converts a date to a display string

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
