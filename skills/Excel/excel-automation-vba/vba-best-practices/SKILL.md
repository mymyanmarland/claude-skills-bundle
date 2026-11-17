---
name: vba-best-practices
description: Teaches professional VBA coding standards for maintainable Excel solutions. Use when the user says things like 'VBA best practices', 'professional VBA code', 'write clean VBA Excel'.
---

# VBA Best Practices Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

VBA best practices: Option Explicit (at the top of every module — forces variable declaration) → Meaningful names (Sub ProcessMonthlyReport not Sub Macro1 / Dim lastRow not Dim x) → Comments (explain the why not the what / '-- This adds 1 because the header row is excluded) → Modular code (one Sub per task — not one 500-line Sub) → Constants (Const TAX_RATE As Double = 0.2 — named constants not magic numbers) → No Select or Activate (Range('A1').Value = x not Range('A1').Select / Selection.Value = x — faster and more reliable) → Error handling on every Sub → Turn off ScreenUpdating and Calculation at the start of batch operations.

## Step 3 — Quality & Polish

- Option Explicit mandatory: undeclared variables cause silent bugs that are very hard to find
- No Select or Activate: the biggest performance and reliability improvement in VBA — avoid it completely
- Modular Subs: a Sub that does one thing is testable / a Sub that does everything is not

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
