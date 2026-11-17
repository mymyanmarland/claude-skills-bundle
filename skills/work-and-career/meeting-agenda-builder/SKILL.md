---
name: meeting-agenda-builder
description: Creates structured meeting agendas with time blocks, clear objectives, pre-read materials, and follow-up action item templates for any type of meeting. Use this skill whenever the user needs to plan a meeting, or says things like "help me plan a meeting", "create a meeting agenda", "I have a team meeting about [topic]", "agenda for [meeting type]", "how do I run a good meeting", or asks for help with standups, retrospectives, 1-on-1s, kickoffs, board meetings, or any other meeting format. Always use this skill — unstructured meetings waste everyone's time; a clear agenda keeps meetings on track and produces actual outcomes.
---

# Meeting Agenda Builder Skill

Design meetings that have a purpose, stay on time, and end with clear next steps.

## Step 1 — Gather Inputs

Ask in one message if not provided:
- **Meeting type** (standup / 1-on-1 / team meeting / project kickoff / retrospective / board meeting / client call / brainstorm / decision meeting)
- **Duration** (15 min / 30 min / 1 hour / half day / full day)
- **Attendees** (who's in the room — roles, not names)
- **Main objective** (what must be decided, discussed, or delivered by end?)
- **Key topics to cover**
- **Any pre-work needed** (documents, data, decisions to be made in advance)

---

## Step 2 — Meeting Type Templates

### ⚡ Daily Standup (15 min)

```
## ⚡ Daily Standup Agenda
**Duration**: 15 minutes | **Format**: Round-robin, standing

**Ground rules**: Timekeeper enforces 2 min per person. No problem-solving in standup — park issues for follow-up.

| Time | Item | Owner |
|------|------|-------|
| 0:00 | What did I complete yesterday? | Each person (2 min) |
| 0:02 | What am I working on today? | Each person (2 min) |
| 0:04 | Any blockers or help needed? | Each person (1 min) |
| 0:15 | END — park any follow-ups | Facilitator |

**Post-standup**: Blockers raised → owner + helper sync separately.
```

---

### 👥 1-on-1 Meeting (30–45 min)

```
## 👥 1-on-1 Agenda
**Duration**: 30 minutes | **Frequency**: Weekly/biweekly
**Principle**: This is the direct report's meeting, not the manager's.

| Time | Item | Notes |
|------|------|-------|
| 0:00–0:05 | Check-in — how are you doing? | Personal, not performance |
| 0:05–0:15 | Their priorities & updates | What's on their plate? What's going well? |
| 0:15–0:22 | Blockers & support needed | What do they need from you? |
| 0:22–0:27 | Manager updates & context | Org news, context they need |
| 0:27–0:30 | Action items & close | Specific next steps, owners, dates |

**Standing items to rotate in**:
- Career development / growth goals
- Feedback (give and receive)
- Team dynamics
- Learning & development
```

---

### 🚀 Project Kickoff Meeting (60 min)

```
## 🚀 Project Kickoff Agenda
**Project**: [Name] | **Duration**: 60 minutes
**Goal**: Align all stakeholders on scope, roles, timeline, and ways of working.

**Pre-read (send 48 hrs before)**:
- [ ] Project brief / charter
- [ ] Proposed timeline
- [ ] Stakeholder map

| Time | Item | Owner | Notes |
|------|------|-------|-------|
| 0:00–0:05 | Welcome & introductions | Facilitator | Especially if cross-team |
| 0:05–0:15 | Project overview & why it matters | Project lead | Vision, goals, success metrics |
| 0:15–0:25 | Scope: what's IN and OUT | PM | Prevent scope creep from day 1 |
| 0:25–0:35 | Roles & responsibilities (RACI) | PM | Who owns what — no ambiguity |
| 0:35–0:45 | Timeline & key milestones | PM | High-level only; detail in project plan |
| 0:45–0:55 | Ways of working | Team | Tools, meeting cadence, comms norms |
| 0:55–1:00 | Q&A and close | Facilitator | Capture open questions |

**Output**: Shared kickoff notes + action items distributed within 24 hours.
```

---

### 🔄 Retrospective Meeting (60 min)

```
## 🔄 Retrospective Agenda
**Sprint/Period**: [X] | **Duration**: 60 minutes
**Format**: What went well / What could improve / Action items

**Ground rules**: Blame-free. Focus on systems, not people. Psychological safety is required.

| Time | Item | Method |
|------|------|--------|
| 0:00–0:05 | Set the stage — check-in | One word to describe the sprint |
| 0:05–0:20 | What went well? | Silent sticky notes → group + discuss |
| 0:20–0:35 | What could improve? | Silent sticky notes → group + discuss |
| 0:35–0:50 | Action items — pick top 3 | Vote on most impactful improvements |
| 0:50–1:00 | Assign owners & close | Each action: owner + due date |

**Tools**: Miro, Mural, FigJam, or physical sticky notes.
**Rule**: Max 3 action items — more than that and nothing gets done.
```

---

### 🎯 Decision Meeting (45 min)

```
## 🎯 Decision Meeting Agenda
**Decision to make**: [State explicitly]
**Duration**: 45 minutes
**Decision maker**: [Named person — avoids endless discussion]

**Pre-read (required before attending)**:
- [ ] Options document with pros/cons
- [ ] Relevant data/research
- [ ] Recommendation from owner

| Time | Item | Owner |
|------|------|-------|
| 0:00–0:05 | Context: why this decision now | Decision owner |
| 0:05–0:15 | Present options (max 3) | Owner |
| 0:15–0:30 | Discussion: clarifying questions only | All |
| 0:30–0:40 | Debate: surface concerns | All |
| 0:40–0:45 | Decision + rationale documented | Decision maker |

**Rule**: If you haven't read the pre-read, you attend as an observer only.
**Output**: Written decision + rationale shared within 2 hours.
```

---

### 💡 Brainstorm Meeting (60 min)

```
## 💡 Brainstorm Agenda
**Topic**: [Problem or opportunity to explore]
**Duration**: 60 minutes
**Goal**: Generate [X] viable ideas; select top 3 to develop further.

| Time | Item | Method |
|------|------|--------|
| 0:00–0:10 | Frame the problem clearly | Facilitator — "How might we [X]?" |
| 0:10–0:20 | Solo idea generation | Silent writing — no judgment |
| 0:20–0:35 | Share & build | Round-robin sharing; "yes, and" not "no, but" |
| 0:35–0:50 | Cluster & prioritize | Group similar ideas; dot vote on favorites |
| 0:50–1:00 | Select top 3 & assign owners | Action planning |

**Rules**: No idea is too wild in generation phase. Evaluation comes later.
```

---

## Step 3 — Universal Agenda Template

For any meeting type not listed above:

```
## 📋 Meeting Agenda: [Meeting Name]
**Date**: [Date] | **Time**: [Time] | **Duration**: [X min]
**Location/Link**: [Room / Zoom / Teams]
**Facilitator**: [Name]

**Meeting Goal**: By the end of this meeting, we will have [specific outcome].

**Attendees**: [List with roles]

**Pre-read (complete before joining)**:
- [ ] [Document 1]
- [ ] [Document 2]

| Time | Agenda Item | Owner | Type |
|------|-------------|-------|------|
| 0:00 | [Item 1] | [Name] | Inform / Discuss / Decide |
| 0:10 | [Item 2] | [Name] | Inform / Discuss / Decide |
| 0:25 | [Item 3] | [Name] | Inform / Discuss / Decide |
| 0:50 | Action items & close | Facilitator | |
| 1:00 | END | | |

**Parking lot** (issues raised but out of scope for today):
- [Item] → [Owner to follow up]

**Action items from this meeting**:
| Action | Owner | Due date |
|--------|-------|----------|
| [Action] | [Name] | [Date] |
```

---

## Step 4 — Meeting Best Practices

```
## 💡 Make Every Meeting Count

**Before**:
- Send agenda 48 hours in advance
- State the goal — what decision or output are we leaving with?
- Invite only people who NEED to be there
- Require pre-reads to be read before attending

**During**:
- Start on time — waiting rewards late arrivals
- Assign a timekeeper and a note-taker
- Distinguish: inform vs. discuss vs. decide (different items, different time needs)
- Park off-topic items — don't derail the agenda

**After**:
- Send notes + action items within 24 hours
- Every action item has ONE owner and ONE due date
- Follow up on previous action items at the next meeting

**The "should this be a meeting?" test**:
- Can this be handled in a Slack message or email? → Skip the meeting
- Does it require real-time back-and-forth? → Meeting justified
- Can some attendees just get the notes? → Reduce invite list
```

Always offer: "Want me to write the meeting invite description for this?" or "Want a note-taking template to use during the meeting?"
