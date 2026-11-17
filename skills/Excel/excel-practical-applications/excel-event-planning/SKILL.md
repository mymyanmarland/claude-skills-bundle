---
name: excel-event-planning
description: Teaches using Excel for event planning and management. Use when the user says things like 'event planning spreadsheet', 'event tracker Excel', 'manage an event in Excel'.
---

# Event Planning in Excel Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Event planning in Excel: Guest list (name / email / RSVP status / dietary requirements / table number / gift recorded) → RSVP tracker (COUNTIF by status: Attending / Declined / No Response) → Budget tracker (item / estimated cost / actual cost / variance) → Task checklist (task / owner / due date / status / =DATEDIF for days remaining) → Timeline (Gantt chart: start date / end date / task bar via conditional formatting) → Vendor list (vendor / service / contact / contract value / payment status) → Seating plan (table layout / assigned guests per table / COUNTIF to check capacity) → Run of show (time / action / responsible person).

## Step 3 — Quality & Polish

- COUNTIF for RSVP status: instant guest count by response category
- Gantt for task timeline: conditional formatting Gantt shows the whole event timeline at a glance
- Days remaining formula: =MAX(0, due_date-TODAY()) — shows 0 not a negative when overdue

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
