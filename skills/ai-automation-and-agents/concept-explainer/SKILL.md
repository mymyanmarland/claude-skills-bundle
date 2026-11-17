---
name: concept-explainer
description: Explains any complex topic — scientific, mathematical, philosophical, historical, or technical — at a chosen level using clear language, analogies, and examples. Use this skill whenever the user asks to explain something, or says things like "explain [topic] to me", "what is [concept]", "I don't understand [topic]", "explain this simply", "explain like I'm 5", "explain like I'm an expert", "how does [X] work", or "what does [term] mean". Also trigger when the user shares a confusing paragraph, document, or equation and asks what it means. Always use this skill for any explanation request — tailoring depth and language to the audience transforms confusion into genuine understanding.
---

# Concept Explainer Skill

Explain any concept at exactly the right level — no more, no less.

## Step 1 — Calibrate the Level

If not stated, infer from context clues (vocabulary used, what they're studying, how they phrased the question). When unsure, ask:
- "Would you like a beginner-friendly explanation, or do you have some background in this area?"

### Level Definitions

| Level | Audience | Style |
|-------|----------|-------|
| **ELI5** (Explain Like I'm 5) | Child / complete beginner | Pure analogy, no jargon, concrete examples only |
| **Beginner** | Curious non-expert | Plain language, minimal jargon, define all terms |
| **Intermediate** | Some background | Introduce proper terminology, more nuance |
| **Advanced** | Domain knowledge | Full terminology, discuss edge cases, mechanisms |
| **Expert** | Professional / researcher | Peer-level depth, cite tradeoffs, acknowledge debates |

## Step 2 — Structure the Explanation

Use this framework for every explanation:

### 1. Hook — Why Does This Matter?
One sentence on why this concept is worth understanding. Make it relevant to the user's world.

### 2. The Core Idea (Plain English First)
State the concept in the simplest possible terms before adding complexity. One clear sentence.

### 3. The Analogy
Connect the concept to something the user already knows. Good analogies are the heart of understanding.

**Analogy selection by domain**:
- Math/stats concepts → everyday counting, cooking, money
- Physics → everyday objects (light switches, balls rolling, water flowing)
- Biology → cities, factories, postal systems
- Computer science → filing cabinets, post offices, assembly lines
- Economics → markets, queues, simple transactions
- Chemistry → LEGO bricks, locks and keys

### 4. How It Actually Works (Step by Step)
Walk through the mechanism. Use numbered steps for processes, bullet points for properties.

### 5. A Concrete Example
Apply it to a specific, real scenario. Numbers help enormously.

### 6. Common Misconceptions
What do people typically get wrong about this? Clearing misconceptions is as valuable as the explanation itself.

### 7. The "So What?" — Real-World Relevance
Where does this show up in the real world? Why does it matter?

---

## Step 3 — Output Format by Level

### ELI5 Format
```
## [Topic] — Super Simple Version

Imagine you have [relatable analogy]...

[2–3 paragraphs maximum, zero jargon, one concrete story]

So basically: [one-sentence summary]
```

### Beginner Format
```
## What is [Topic]?

**The simple version**: [One sentence]

**Think of it like this**: [Analogy]

**Here's how it works**:
1. [Step/point 1]
2. [Step/point 2]
3. [Step/point 3]

**A real example**: [Concrete scenario]

**Why it matters**: [Practical relevance]

**Common mix-up**: People often confuse this with [X], but the difference is [Y].
```

### Intermediate/Advanced Format
```
## [Topic]

### Core Concept
[Definition using proper terminology, clearly stated]

### Mechanism
[How it works, with appropriate technical depth]

### Formal Definition / Formula (if applicable)
[Math, notation, or technical specification]

### Example
[Worked example with numbers or specifics]

### Edge Cases & Nuances
[Where the simple explanation breaks down]

### Related Concepts
- **[Related 1]**: How it connects
- **[Related 2]**: How it connects

### Common Misconceptions
[What even intermediate learners get wrong]
```

## Step 4 — Special Cases

### Explaining a Formula or Equation
1. State what the formula calculates in plain English
2. Define every variable before using it
3. Walk through with real numbers
4. Explain the intuition behind WHY the formula has that structure
5. Show what happens at edge cases (what if X = 0? What if X → ∞?)

### Explaining a Process or Historical Event
1. Set the context — what situation led to this?
2. Walk through chronologically
3. Identify the key turning points
4. Explain consequences and why it mattered

### Explaining a Philosophical or Abstract Concept
1. Start with the question it's trying to answer
2. Give the intuitive version
3. Present the formal/technical version
4. Give the strongest objection to it
5. Explain how proponents respond

### Explaining Code or Technical Output
1. What does this code/output DO (in plain English)?
2. Walk line by line or section by section
3. Explain why it was written this way (design decisions)
4. Flag any tricky or non-obvious parts

## Step 5 — Check for Understanding

End every explanation with one of:
- "Does that make sense so far? Happy to go deeper on any part."
- "Want me to go further into [specific subtopic]?"
- "Want to test your understanding with a quick question?"

## Quality Rules
- Never use a technical term without immediately defining it (at beginner/intermediate level)
- If an analogy is imperfect (all are), acknowledge the limitation
- Short paragraphs — 3–4 sentences max per paragraph
- One idea per paragraph
- Always lead with intuition, follow with formalism — never the reverse
