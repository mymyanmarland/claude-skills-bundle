---
name: vba-userforms
description: Teaches creating dialog boxes and user input forms with VBA. Use when the user says things like 'VBA UserForm guide', 'create a form in Excel VBA', 'dialog box VBA Excel'.
---

# VBA UserForms Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level: beginner/intermediate/advanced
- Specific task or use case
- Data type and approximate size
- Intended output or deliverable

## Step 2 — Core Output

VBA UserForms: Create (VBA Editor / Insert / UserForm) → Controls (Toolbox: TextBox / Label / CommandButton / ListBox / ComboBox / CheckBox) → Properties window (set Name / Caption / Font / Size for each control) → Show the form (UserForm1.Show from a Sub) → Read control values (TextBox1.Value / CheckBox1.Value) → Populate a ListBox (ListBox1.AddItem 'Option 1') → OK button code (Sub CommandButton1_Click() — collect values / validate / write to sheet / Unload Me) → Cancel button (Unload Me — closes the form) → Input validation (If TextBox1.Value = '' Then MsgBox 'Required' / Exit Sub).

## Step 3 — Quality & Polish

- Name controls meaningfully: TextBox1 becomes unmanageable — name it txtFirstName
- Validate inputs before writing: never write unvalidated user input to the sheet
- Unload Me to close: Me refers to the current form — the standard close method

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features and functions may vary between versions (Excel 2019, 2021, Microsoft 365) and platforms (Windows, Mac, web). Always test formulas on sample data before applying to important files. Back up your data before running bulk operations.
