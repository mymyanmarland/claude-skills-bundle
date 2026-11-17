---
name: automation-use-case-finder
description: Identifies and prioritizes the highest-value automation opportunities for any business, role, or workflow — with ROI estimates and implementation difficulty ratings. Use when the user says "what should I automate", "automation ideas for my [business/role]", "find automation opportunities in my workflow", "what processes should I automate first", or "help me identify where AI/automation can save time". Always use this skill — most people automate the wrong things first; this skill identifies quick wins with the highest time-savings-to-complexity ratio.
---
# Automation Use Case Finder Skill

## Step 1 — Gather Inputs
- **Role or business type**: (job title, company type, team size)
- **Current tools used**: (CRM, spreadsheets, email, project management, etc.)
- **Biggest time drains**: (what takes most time that feels repetitive?)
- **Technical comfort level**: No-code / Low-code / Developer
- **Budget**: Free tools only / $0-50/month / $50-200/month / Enterprise
- **Goal**: Save time / Reduce errors / Scale operations / Remove manual bottlenecks

## Step 2 — Use Case Audit

```
## Automation Opportunity Audit: [Role/Business]

PROCESS INVENTORY
[List every repeated process mentioned or implied, then rate each:]

| Process | Frequency | Time/occurrence | Monthly time cost | Automation potential |
|---------|-----------|-----------------|-------------------|---------------------|
| [Process 1] | Daily | [X min] | [X hrs] | High/Medium/Low |
| [Process 2] | Weekly | [X min] | [X hrs] | High/Medium/Low |
[Continue for all identified processes]

TOTAL TIME CURRENTLY SPENT ON REPETITIVE TASKS: ~[X] hrs/month
```

## Step 3 — Prioritized Recommendations

```
## Top Automation Opportunities (Ranked by ROI)

---

TIER 1 — QUICK WINS (automate this week)
High value, low complexity, tools already available

1. [Process Name]
   What it is: [What's done manually today]
   Automation: [What the automated version looks like]
   Tools: [Specific tools — n8n, Zapier, Make, native feature]
   Time saved: ~[X] hrs/month
   Implementation effort: [2-4 hours to set up]
   Difficulty: ⭐ Easy
   ROI: [Time saved ÷ setup time — e.g., "Pays back in week 1"]

2. [Process Name]
   [Same structure]

3. [Process Name]
   [Same structure]

---

TIER 2 — MEDIUM TERM (this month)
Higher complexity, larger payoff

4. [Process Name]
   What it is: [Manual process]
   Automation: [Automated version]
   Tools: [Tools needed + any new subscriptions]
   Time saved: ~[X] hrs/month
   Implementation effort: [1-2 days]
   Difficulty: ⭐⭐⭐ Medium
   ROI: [Estimate]

5. [Process Name]
   [Same structure]

---

TIER 3 — STRATEGIC (next quarter)
Complex automations requiring planning

6. [Process Name]
   What it is: [Process]
   Automation: [Full automation description]
   Tools: [More complex stack]
   Time saved: ~[X] hrs/month
   Implementation effort: [Days-weeks]
   Difficulty: ⭐⭐⭐⭐⭐ Complex
   ROI: [Long-term estimate]

---

WHAT NOT TO AUTOMATE (yet):
- [Process that requires human judgment or relationship]
- [Process done so rarely it's not worth the setup time]
- [Process that changes too often to keep automation maintained]

---

AUTOMATION ROADMAP
Month 1: [Quick wins 1-3]
Month 2: [Medium-term 4-5]
Month 3: [Strategic 6]
Estimated total time saved when all implemented: [X] hrs/month
Monthly value at $[hourly rate]: $[X]/month
```

## Step 4 — The Automation Scoring Framework

Rate any process on these 4 criteria (1-5 each):
1. **Frequency**: How often does this happen?
2. **Time cost**: How long does each instance take?
3. **Rule-based**: Can it be done with clear if-then rules?
4. **Error cost**: How expensive is a human error here?

Score of 16-20: Automate immediately
Score of 10-15: High priority
Score of 5-9: Medium priority
Score under 5: May not be worth automating

## Step 5 — Tool Matching Guide

| Need | Best no-code tool | Best dev tool |
|------|-----------------|---------------|
| Connect apps | Zapier / Make / n8n | Custom API calls |
| AI processing | n8n + OpenAI | LangChain / direct API |
| Spreadsheet automation | Google Apps Script | Python + gspread |
| Email automation | Mailchimp / ActiveCampaign | SendGrid API |
| Web scraping | Apify / Browse AI | Playwright / Puppeteer |
| Document processing | Adobe Acrobat / Docparser | PyPDF2 / LLM parsing |
| Scheduling | Calendly + Zapier | n8n Schedule trigger |

Always offer: "Want me to build a detailed implementation plan for your top 3 automations?"
