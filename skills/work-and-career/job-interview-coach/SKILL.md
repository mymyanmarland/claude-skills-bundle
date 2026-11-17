---
name: job-interview-coach
description: Prepares users for job interviews by generating likely questions, coaching STAR-method answers, running mock interviews, and giving feedback on responses. Use this skill whenever the user is preparing for a job interview, or says things like "help me prepare for an interview", "what questions will they ask", "mock interview", "interview practice", "how do I answer [interview question]", "interview tips for [role]", or "I have an interview tomorrow". Also trigger when the user wants to practice behavioral, technical, or case interview questions. Always use this skill — interview performance is a skill that improves dramatically with preparation, and most people under-prepare.
---

# Job Interview Coach Skill

Prepare candidates to walk into any interview with confidence and strong answers.

## Step 1 — Gather Inputs

Ask in one message if not provided:
- **Role and company** they're interviewing for
- **Interview type**: Behavioral / Technical / Case / Panel / HR screening / Final round
- **Their background**: Relevant experience, top achievements, career story
- **Biggest concern**: What do they find hardest to answer? (gaps, pivots, weakness questions, etc.)
- **Mode**: Generate questions / Coach a specific answer / Full mock interview

---

## Step 2 — Question Bank by Interview Type

### 🎯 Behavioral Questions (STAR method required)

**Top 20 universal behavioral questions**:

```
## 📋 Likely Behavioral Questions for [Role]

**About your experience**:
1. Tell me about yourself.
2. Walk me through your resume / career journey.
3. Why are you leaving your current role?
4. Why do you want to work here?
5. Where do you see yourself in 5 years?

**Competency: Leadership**:
6. Tell me about a time you led a team through a challenge.
7. Describe a situation where you had to influence without authority.

**Competency: Problem-solving**:
8. Tell me about a complex problem you solved.
9. Describe a time you had to make a decision with incomplete information.

**Competency: Collaboration**:
10. Tell me about a conflict with a colleague and how you resolved it.
11. Describe a time you had to work with a difficult stakeholder.

**Competency: Failure & resilience**:
12. Tell me about a time you failed. What did you learn?
13. Describe a project that didn't go as planned.

**Competency: Achievement**:
14. What's your greatest professional accomplishment?
15. Tell me about a time you exceeded expectations.

**Competency: Adaptability**:
16. Tell me about a time you had to pivot quickly.
17. How have you handled a major change at work?

**Competency: Initiative**:
18. Tell me about something you built or started that didn't exist before.
19. Describe a time you went beyond your job description.

**The tough ones**:
20. What's your greatest weakness?
```

---

## Step 3 — STAR Method Coaching

For every behavioral question, coach the STAR-I structure:

```
## 🌟 STAR-I Framework

**S — Situation** (10% of answer — 1–2 sentences)
Set the scene. What was the context? What was at stake?
❌ Don't: Spend 3 minutes explaining backstory.
✅ Do: Give just enough for the story to make sense.

**T — Task** (10% of answer — 1 sentence)
What was YOUR specific responsibility? What were you accountable for?
Key: Use "I", not "we". Your role, not the team's.

**A — Action** (60% of answer — most detail here)
What did YOU specifically do? Step by step. This is where you shine.
Key: Be specific about your decisions, not generic. "I analyzed X, identified Y, and proposed Z because..."

**R — Result** (15% of answer)
What happened? Quantify if possible. % change, $ amount, time saved, customer outcome.
If you don't have an exact number: estimate and frame it ("roughly", "approximately").

**I — Impact** (5% of answer — the "so what")
What did this mean beyond the number? Team morale, company goal, customer experience, long-term change.
```

---

## Step 4 — Answer Coaching

When the user gives a draft answer, provide structured feedback:

```
## 📝 Answer Review: "[Question]"

**Your draft**: [their answer]

---

**What's working**:
- [Specific strength — e.g., "Strong concrete result with a number"]
- [Another positive]

**What to improve**:
- [Issue 1 — e.g., "The Action section is too vague — what specifically did YOU do?"]
- [Issue 2 — e.g., "The Situation takes too long — cut the first 3 sentences"]
- [Issue 3 — e.g., "No result mentioned — what was the outcome?"]

**Suggested stronger version**:
"[Rewritten answer incorporating improvements — same story, tighter and more impactful]"

**Length check**: [Too long / Right length / Too short]
Target: 1.5–2.5 minutes spoken (90–150 words written)
```

---

## Step 5 — "Tell Me About Yourself" Formula

This is always the first question. Have it polished:

```
## 🎤 "Tell Me About Yourself" Formula

**Structure** (90 seconds max):
1. [Current role and key focus — 1 sentence]
2. [Most relevant prior experience — 1–2 sentences, most recent 2 roles]
3. [Top achievement or differentiator — 1 sentence with a number]
4. [Why you're here / why this role — 1 sentence connecting past to this opportunity]

**Example**:
"I'm currently a Product Manager at [Company], where I lead the growth team
focused on user acquisition and retention. Before that, I spent 4 years at [Company]
in a similar role, where I launched [product] that grew to 200K users in 12 months.
I've developed a particular strength in data-driven decision making and cross-functional
collaboration. I'm excited about this role at [Target Company] because [specific reason]
— it's a natural next step given my background in [relevant area]."
```

---

## Step 6 — Handling Hard Questions

### "What's your greatest weakness?"

```
**The formula**: Real weakness + what you've done about it + evidence of growth
❌ Avoid: "I work too hard" / "I'm a perfectionist" (nobody believes you)
✅ Do: Pick a genuine developmental area that isn't core to the role

Example: "I've historically been less confident in public speaking. I recognized
this was holding me back from advocating for my team, so over the past year I joined
a Toastmasters group and volunteered to present at our quarterly all-hands. I still
find it a stretch, but I've gotten consistent positive feedback on my last 3 presentations."
```

### "Why are you leaving your current job?"

```
**The rule**: Never speak negatively about current employer — ever.
**The formula**: Pull (what attracts you) + Push (framed positively)

✅ "I've learned a tremendous amount at [Company] and I'm proud of what we've built.
I'm at a point where I'm looking for [more scope / new industry / leadership opportunity],
and [Target Company] offers exactly that."
```

### "Do you have any questions for us?"

```
**Always have 3–5 questions ready**:
1. "What does success look like in this role in the first 90 days?"
2. "What are the biggest challenges the team is currently navigating?"
3. "How would you describe the culture here — how do decisions get made?"
4. "What do you personally enjoy most about working here?"
5. "What are the next steps in the process and your timeline?"

❌ Never ask: salary (too early), benefits (too early), "what does your company do?" (do your research)
```

---

## Step 7 — Mock Interview Mode

When user wants a full mock interview:

```
I'll run a mock interview for [Role] at [Company]. I'll ask you questions one at a time — answer as if it's the real thing. After each answer I'll give you feedback on content, structure, and delivery before moving to the next question.

Ready? Let's start:

"Thank you for coming in today. To get us started — tell me about yourself and what brought you to apply for this role."
```

After each answer, give:
- ✅ What landed well
- ⚠️ What to tighten or change
- 📏 Timing feedback (too long / too short)
- 🔄 Improved version of the weakest part

---

## Step 8 — Day-Before Checklist

```
## ✅ Interview Preparation Checklist

**Research**:
- [ ] Read company website, About page, recent news
- [ ] Know their products/services and target customers
- [ ] Research your interviewers on LinkedIn
- [ ] Read recent Glassdoor reviews for culture insight

**Stories**:
- [ ] 5 STAR stories ready covering: leadership, failure, achievement, conflict, initiative
- [ ] Each story has a specific result with a number

**Logistics**:
- [ ] Interview location confirmed (or video link tested)
- [ ] Professional attire prepared
- [ ] Arrive/log in 10 minutes early
- [ ] Notepad and pen (or water for video)
- [ ] Copies of your resume printed (in-person)

**Mindset**:
- [ ] You are also interviewing THEM — it's a two-way evaluation
- [ ] Nervousness = excitement — reframe it
- [ ] They already liked your resume — now just have a conversation
```

Always offer: "Want to do a full mock interview?" or "Want me to generate questions specific to [company or role]?"
