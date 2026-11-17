---
name: n8n-workflow-builder
description: Designs complete n8n workflow blueprints with node-by-node logic, trigger configuration, data mapping, and error handling for any automation use case. Use when the user says "build an n8n workflow for", "n8n automation for [task]", "how do I automate [process] in n8n", "n8n nodes for [use case]", or "help me design an n8n workflow". Always use this skill — n8n workflows require specific node sequencing, data transformation logic, and credential configuration that generic automation advice misses entirely.
---
# n8n Workflow Builder Skill

## Step 1 — Gather Inputs
- **What to automate**: (the business process or task)
- **Trigger**: What starts this workflow? (schedule / webhook / form submission / email / new row in sheet / manual)
- **Data sources**: Where does data come from? (Gmail / Sheets / Airtable / HTTP / database)
- **Actions to perform**: What should the workflow do? (send email / update record / post message / create task)
- **Output destinations**: Where does the result go?
- **Error handling needs**: Should failures send alerts?
- **n8n version**: Cloud / Self-hosted

## Step 2 — Workflow Blueprint

```
## n8n Workflow: [Name]
Trigger: [Type] | Complexity: [Simple/Medium/Complex] | Est. nodes: [X]

---

WORKFLOW OVERVIEW
Purpose: [One sentence — what this workflow does end-to-end]
Trigger condition: [Exactly when it fires]
End result: [What has changed in the world when it completes]

---

NODE-BY-NODE BLUEPRINT

NODE 1 — TRIGGER
Type: [Schedule / Webhook / Gmail Trigger / Google Sheets Trigger / Manual]
Configuration:
  - [Key setting 1 — e.g., "Cron: 0 9 * * 1-5 (weekdays at 9am)"]
  - [Key setting 2]
Output data: [What fields come out of this node]

→ connects to →

NODE 2 — [Name, e.g., "Fetch New Rows"]
Type: [Google Sheets / HTTP Request / Airtable / MySQL / etc.]
Operation: [Read / Create / Update / Delete]
Configuration:
  - Spreadsheet ID: [reference]
  - Sheet: [Sheet name]
  - Filter: [Only rows where Status = "Pending"]
Output: [Array of row objects with fields: name, email, status, etc.]

→ connects to →

NODE 3 — [Name, e.g., "Loop Over Items"]
Type: Split In Batches / Item Lists
Purpose: Process each row individually
Batch size: 1 (process one at a time)

→ connects to →

NODE 4 — [Name, e.g., "AI Processing / Transform Data"]
Type: [OpenAI / Set / Function / Code]
Configuration:
  - [If AI: Model, system prompt, input mapping]
  - [If Set: map fields from previous node]
  - [If Code: JavaScript logic]
Key expression: {{ $json["fieldName"] }}
Output: [Transformed data fields]

→ connects to →

NODE 5 — [Name, e.g., "Send Email"]
Type: [Gmail / SMTP / SendGrid / Slack / etc.]
Configuration:
  - To: {{ $json["email"] }}
  - Subject: [Template with expressions]
  - Body: [HTML or text template]

→ connects to →

NODE 6 — [Name, e.g., "Update Status"]
Type: [Google Sheets / Airtable / HTTP Request]
Operation: Update row
Filter: Match by ID
Field to update: Status → "Completed"

---

ERROR HANDLING NODES

ERROR TRIGGER node:
- Connected to all main nodes
- On error: Send Slack message to #alerts with:
  - Workflow name
  - Failed node: {{ $workflow.name }}
  - Error: {{ $execution.error.message }}
  - Timestamp

---

CREDENTIALS NEEDED
- [ ] [Service 1 credential — OAuth2 / API key / Basic auth]
- [ ] [Service 2 credential]
- [ ] [Service 3 credential]

---

EXPRESSIONS CHEAT SHEET FOR THIS WORKFLOW
{{ $json["fieldName"] }} — access current item field
{{ $items("Node Name")[0].json.field }} — access specific node output
{{ $now.toISO() }} — current timestamp
{{ $json["email"].toLowerCase() }} — transform string

---

TESTING CHECKLIST
- [ ] Test trigger manually first (use "Execute Node")
- [ ] Check output structure after each node before connecting next
- [ ] Test with 1 item before enabling for full dataset
- [ ] Verify error handler fires correctly (intentionally break a node)
- [ ] Set workflow to Active only after full test pass
```

## Step 3 — Common n8n Patterns

**Pattern: AI-powered email triage**
Gmail Trigger → OpenAI (classify/summarize) → Switch (route by category) → Multiple outputs

**Pattern: Scheduled data sync**
Schedule → Fetch from Source API → Transform with Code node → Upsert to destination

**Pattern: Form to CRM + notification**
Webhook → Set (clean data) → HubSpot/Airtable (create record) → Slack (notify team)

**Pattern: Multi-step AI agent**
Trigger → AI Agent node → Tool nodes (web search, calculator, API) → Format → Output

## Step 4 — n8n Node Quick Reference

| Task | Node to use |
|------|-------------|
| Run on schedule | Schedule Trigger |
| Receive HTTP data | Webhook |
| Send HTTP request | HTTP Request |
| Process each item | Item Lists / Split In Batches |
| Branch logic | IF / Switch |
| Call OpenAI | OpenAI or HTTP Request |
| Run JavaScript | Code |
| Set/transform fields | Set |
| Merge streams | Merge |
| Delay between steps | Wait |
| Get/send email | Gmail |
| Read/write sheets | Google Sheets |

Always offer: "Want me to write the JavaScript for any Code node in this workflow?"
