---
name: excel-travel-planner
description: Teaches building a travel planning tool in Excel. Use when the user says things like 'travel planner Excel', 'trip planning spreadsheet', 'holiday planning Excel'.
---

# Travel Planning Spreadsheet Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Travel planner in Excel: Itinerary (date / day / city / activity / booking reference / cost) → Budget tracker (estimated vs actual cost / by category: flights/hotel/food/activities) → Currency conversion (=cost×VLOOKUP(currency, exchange_rates, 2, 0)) → Packing checklist (item / category / packed: checkbox or Y/N / COUNTIF for packed vs total) → Accommodation tracker (hotel / check-in / check-out / address / booking reference / nights: =DATEDIF) → Flight tracker (flight number / departure / arrival / terminal / seat) → Emergency contacts (embassy / travel insurance / local contacts).

## Step 3 — Quality & Polish

- Currency conversion with exchange rate table: one formula converts everything to the home currency
- DATEDIF for nights: check-out minus check-in gives the exact number of nights
- Packing checklist with COUNTIF progress: how many items packed vs total gives a clear completion indicator

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
