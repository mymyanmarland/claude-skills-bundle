---
name: excel-school-grades
description: Teaches building grade books and student tracking tools in Excel. Use when the user says things like 'grade book Excel', 'student tracker spreadsheet', 'school administration Excel'.
---

# Grade Book and School Administration Skill

## Step 1 — Gather Inputs

- Excel version and platform
- Experience level
- Specific task
- Data type
- Intended output

## Step 2 — Core Output

Grade book in Excel: Student roster (name / ID / class / contact) → Assignment scores (one column per assignment / dates as headers) → Weighted average (=SUMPRODUCT(scores, weights)/SUM(weights)) → Letter grade (=IFS(avg>=90,'A',avg>=80,'B',avg>=70,'C',avg>=60,'D',TRUE,'F')) → Class average (=AVERAGE of the weighted average column) → Attendance (binary 1/0 per day / =COUNTIF for absences / =COUNTA-COUNTIF for attendance) → Progress chart (line chart of each student's scores over time) → Missing assignment flag (=IF(ISBLANK(cell),'Missing','')) → Conditional formatting for failing grades (red below 60).

## Step 3 — Quality & Polish

- Weighted average with SUMPRODUCT: assignments worth different percentages require weighted calculation
- IFS for letter grades: cleaner than nested IF for multiple grade thresholds
- ISBLANK for missing assignment detection: automatically flags any empty score cell

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Excel features may vary between versions. Always test formulas on sample data and back up your data before running bulk operations.
