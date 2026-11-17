---
name: excel-invoice-template
description: Teaches building professional invoice and quote templates in Excel. Use when the user says things like 'invoice template Excel', 'create a quote in Excel', 'billing template Excel'.
---

# Excel Invoice and Quote Templates Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Invoice and quote templates: Header (company logo / name / address / registration number / date / invoice number) → Auto-numbering (=YEAR(TODAY())&TEXT(ROW()-n,'000') — auto-generates sequential invoice numbers) → Line items table (description / quantity / unit price / line total: =qty×price) → Subtotal (=SUM of line totals) → Tax (=subtotal×tax rate / or =VLOOKUP(tax_code, tax_table, 2, 0)) → Total (=subtotal + tax) → Payment terms (due date: =invoice_date+30 / bank details / payment methods) → PDF export macro (one button converts to PDF and saves with the invoice number as filename) → Drop-down for client details (VLOOKUP populates address from a client database).

## Step 3 — Quality & Polish

- Client database VLOOKUP: type the client name and all contact details auto-populate
- Sequential invoice numbering formula: consistent numbering is a legal and accounting requirement
- PDF macro with invoice number as filename: automates the filing and distribution step

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
