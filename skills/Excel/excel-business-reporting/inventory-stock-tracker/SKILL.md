---
name: inventory-stock-tracker
description: Teaches building an inventory management spreadsheet. Use when the user says things like 'inventory tracker Excel', 'stock management spreadsheet', 'Excel inventory control'.
---

# Inventory and Stock Tracker Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

Inventory tracker: Item master (SKU / description / category / unit / reorder level / supplier) → Stock movements (date / SKU / in or out / quantity / reference) → Current stock (=SUMIF(movements, SKU, quantity_in) - SUMIF(movements, SKU, quantity_out)) → Reorder alert (=IF(stock<reorder_level,'REORDER','OK') — conditional formatting red for reorder) → Stock valuation (=stock × unit cost — FIFO or average cost) → Category summary (PivotTable: total stock / total value by category) → Slow-moving stock (last movement date vs today / DATEDIF).

## Step 3 — Quality & Polish

- SUMIF for current stock: the most reliable method — sum all ins minus all outs
- Reorder alert with conditional formatting: the alert is useless if it does not stand out visually
- Stock valuation method: document whether FIFO or average cost is used — be consistent

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
