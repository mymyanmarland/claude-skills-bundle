---
name: automation-sop-converter
description: Converts existing Standard Operating Procedures (SOPs) and manual process documentation into automation-ready workflow specifications, identifying which steps to automate, which to keep human, and how to bridge them. Use when the user says "automate my SOP for [process]", "convert this procedure to an automation", "I have a manual process I want to automate", "translate my workflow doc into an automation plan", or pastes an existing SOP and asks how to automate it. Always use this skill — automating an SOP without analysis first leads to automating the wrong steps and breaking processes that depended on human judgment.
---
# Automation SOP Converter Skill

## Step 1 — Gather Inputs
- **The SOP or process description**: (paste the full document or describe the process step by step)
- **Current tools used in the process**: (CRM, spreadsheets, email, etc.)
- **Volume**: How many times per day/week/month is this done?
- **Who does it now**: (the role — to understand skill level and judgment required)
- **Pain points**: What goes wrong most often? What takes longest?
- **Automation platform**: n8n / Make / Zapier / Custom code / No preference

## Step 2 — SOP Analysis

```
## SOP Automation Analysis: [Process Name]

ORIGINAL PROCESS SUMMARY
[Brief description of what the SOP accomplishes end-to-end]
Current execution time per instance: ~[X] minutes
Monthly volume: ~[X] times
Monthly time cost: ~[X] hours

---

STEP-BY-STEP ANALYSIS

| Step # | Current action | Automation verdict | Reason |
|--------|---------------|-------------------|--------|
| 1 | [Action] | ✅ Automate | Rule-based, no judgment |
| 2 | [Action] | ✅ Automate | Data transformation |
| 3 | [Action] | 👤 Keep human | Requires relationship judgment |
| 4 | [Action] | ⚠️ Semi-automate | Automate prep, human decides |
| 5 | [Action] | ✅ Automate | Simple notification |

VERDICT LEGEND:
✅ Automate — rule-based, consistent input, no judgment needed
👤 Keep human — requires context, relationships, or judgment
⚠️ Semi-automate — automate the data prep, keep human for the decision
🔄 Automate with approval — automate but add human checkpoint before action
```

## Step 3 — Automation-Ready Specification

```
## Automation Workflow Specification: [Process Name]

TRIGGER
What starts this workflow?
[Specific trigger: new email received / form submitted / daily at 9am / new row added / etc.]

AUTOMATED STEPS

Step A — [Name] (replaces manual Step [X])
Tool: [n8n node / Make module / API call]
Action: [Exactly what the automation does]
Input: [Where data comes from]
Output: [What data is produced]
Logic: [Any conditions/branching]

Step B — [Name] (replaces manual Step [X])
[Same structure]

Step C — [Name] (replaces manual Steps [X] and [Y])
[Same structure — sometimes one automation step replaces multiple manual ones]

---

HUMAN CHECKPOINTS (kept in the workflow)

Checkpoint 1 — After Step [X]:
Reason kept human: [Specific judgment required]
What human receives: [Summary/data the automation prepares for them]
What human decides: [The specific decision]
How they signal decision: [Reply to email / Update field to Approved / Click button]
Automation waits: [How long before timing out / defaulting]

Checkpoint 2 — Before Step [Y]:
[Same structure]

---

HANDOFF DESIGN
For each human checkpoint, the automation should:
1. Prepare a summary of relevant data
2. Present 2-3 clear options (not open-ended questions)
3. Set a deadline for response
4. Have a default action if no response

Example handoff email:
Subject: "Action needed: [Process name] — [specific item]"
Body:
  - [Summary: here's what the automation found]
  - [Context: here's what you need to know]
  - Option A: [Reply YES] → automation continues with [action]
  - Option B: [Reply NO] → automation routes to [alternative action]
  - Deadline: Please respond by [time/date]. If no response, [default action].

---

ERROR HANDLING (automation-specific)
What happens if [Step A] fails: [Specific fallback]
What happens if human doesn't respond within [timeframe]: [Default action + alert]
What happens if data is incomplete: [Request clarification step]

---

ESTIMATED IMPACT
Steps automated: [X] of [Y] total steps
Time saved per instance: ~[X] minutes
Monthly time saved: ~[X] hours
Remaining human time per instance: ~[X] minutes (down from [original])
Error reduction: [Specific errors that automation eliminates]
```

## Step 4 — What Can't Be Automated (criteria)

Keep human when ANY of these are true:
1. **Novel situations**: First time this type of case has occurred
2. **Relationship stakes**: Response will affect a long-term relationship
3. **Irreversible consequences**: Mistake is costly and hard to undo
4. **Ethical judgment**: Decision involves values, not just rules
5. **Incomplete data**: Critical information is missing and unclear
6. **Regulatory requirement**: Rules require human review and sign-off

## Step 5 — Implementation Plan

```
PHASE 1 (Week 1): Automate the easy steps
[List the fully automatable steps to build first — quick win, proves concept]

PHASE 2 (Week 2-3): Build the handoff system
[Build the human checkpoint notifications and response handling]

PHASE 3 (Month 2): Add intelligence
[Add AI judgment for any steps currently kept human that could be improved with LLM analysis]

PHASE 4 (Ongoing): Monitor and improve
[Track error rates, response times at checkpoints, identify new automation opportunities]
```

Always offer: "Want me to build the n8n workflow for Phase 1 of this implementation?"
