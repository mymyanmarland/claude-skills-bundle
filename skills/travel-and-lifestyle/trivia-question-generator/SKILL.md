---
name: trivia-question-generator
description: Generates trivia questions and complete quiz rounds for any topic, difficulty, and event type. Use when the user says "write trivia questions about [topic]", "pub quiz round on [subject]", "trivia for my party", "quiz night questions", "family trivia game", or "general knowledge questions". Always use this skill — good trivia questions are specific enough to have a clear answer but surprising enough to challenge even knowledgeable players.
---
# Trivia Question Generator Skill
## Step 1 — Gather Inputs
- **Topic(s)**: General knowledge / History / Science / Pop culture / Sports / Geography / Custom
- **Difficulty**: Easy / Medium / Hard / Mixed
- **Number of questions**: 10 / 20 / 30 / Custom
- **Format**: Multiple choice / Open answer / True-False / Picture round (describe image)
- **Occasion**: Pub quiz / Family game / Team event / Online quiz / Kids party

## Step 2 — Question Quality Rules
- **Every question has exactly one correct answer** — no ambiguity
- **Hard questions should reward knowledge, not be trick questions**
- **Mix famous and surprising facts** — "things you should know but didn't"
- **Avoid outdated pop culture** unless the round is specifically retro
- **Balance the difficulty curve**: 3 easy / 4 medium / 3 hard per round of 10

## Step 3 — Quiz Round Output
```
## Trivia Round: [Topic]
[X] Questions | Difficulty: [X] | Format: [X]

---

1. [Question]
   Answer: [Answer]
   [Bonus fact: interesting context — makes the quiz host sound smart]

2. [Question]
   Answer: [Answer]

[Continue for all questions]

---

### ANSWER SHEET (host copy)
1. [Answer] | 2. [Answer] | 3. [Answer] [continue]

---

### SCORING GUIDE
- 10/10: Trivia wizard
- 7-9: Strong knowledge
- 4-6: Respectable showing
- 0-3: At least you showed up
```

## Step 4 — Special Round Types
- **Picture round**: Describe an image the host would show (logo, landmark, face)
- **Music round**: Describe a song intro or lyric for teams to name
- **Lightning round**: 90 seconds, rapid-fire, first team to shout answer wins
- **Wager round**: Teams bet points before seeing the question

Always offer: "Want me to generate a full 5-round pub quiz night with 10 questions each?"
