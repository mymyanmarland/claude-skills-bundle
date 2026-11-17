---
name: book-summarizer
description: Produces structured book summaries with key ideas, chapter breakdowns, actionable takeaways, and memorable quotes for any non-fiction or fiction book. Use this skill whenever the user asks for a book summary, or says things like "summarize [book]", "what is [book] about", "key lessons from [book]", "what are the main ideas in [book]", "I don't have time to read [book] — what's in it", "book notes for [title]", or "explain [book] to me". Also trigger when the user asks for reading recommendations related to a book they just read. Always use this skill — a structured summary with takeaways is far more useful than a generic plot overview.
---

# Book Summarizer Skill

Deliver rich, structured book summaries that give the user real value — not just a plot recap.

## Step 1 — Gather Inputs

Ask if not provided:
- **Book title and author**
- **What they want from the summary**:
  - A) Quick overview (5-min read)
  - B) Deep summary with all key ideas
  - C) Actionable takeaways only
  - D) Chapter-by-chapter breakdown
- **Why they're reading it** (personal growth, work, curiosity, academic) — tailors emphasis

---

## Step 2 — Non-Fiction Summary Format

For non-fiction, business, self-help, science, history, and biography books:

```
## 📖 Book Summary: [Title]
**Author**: [Name] | **Year**: [Year] | **Genre**: [Category]
**Read time**: ~X hours | **Summary read time**: ~X min

---

### 🎯 The Core Idea (One Paragraph)
[The single most important thing this book argues or teaches. If someone read only this, what must they understand?]

---

### 🧠 Key Ideas

#### Idea 1: [Title]
[2–3 paragraph explanation of the idea]
> *"[Memorable quote from the book if applicable]"*
**So what**: [Why this idea matters / how to apply it]

#### Idea 2: [Title]
[Explanation]
**So what**: [Application]

#### Idea 3: [Title]
[Explanation]
**So what**: [Application]

[Continue for all major ideas — typically 4–8 for most books]

---

### 📚 Chapter-by-Chapter Breakdown (if requested)

| Chapter | Title | Key Point |
|---------|-------|-----------|
| 1 | [Title] | [One-sentence summary] |
| 2 | [Title] | [One-sentence summary] |
[Continue]

---

### 💡 Actionable Takeaways

What can the reader DO differently after reading this?

1. **[Action]**: [Specific, concrete, implementable step]
2. **[Action]**: [Specific step]
3. **[Action]**: [Specific step]
[Up to 7 takeaways]

---

### 🔑 Most Memorable Quotes

> *"[Quote 1]"* — [Context]

> *"[Quote 2]"* — [Context]

> *"[Quote 3]"* — [Context]

---

### 👤 Who Should Read This

**Best for**: [Type of reader who will get most value]
**Skip if**: [Who won't benefit / will find it obvious or irrelevant]
**Pairs well with**: [1–2 related books]

---

### ⭐ Honest Assessment

**Strengths**: [What the book does well]
**Weaknesses**: [Where it's repetitive, overhyped, or weak on evidence]
**Overall**: [Is it worth reading in full, or does the summary suffice?]
```

---

## Step 3 — Fiction Summary Format

For novels, short story collections, and literary fiction:

```
## 📖 Book Summary: [Title]
**Author**: [Name] | **Year**: [Year] | **Genre**: [Genre]
⚠️ *[Spoiler warning if applicable]*

---

### 📝 Overview (Spoiler-Free)
[2–3 paragraph overview — what kind of story, themes, and reading experience — without revealing plot twists or endings]

---

### 🗺️ Plot Summary
**Setting**: [Time, place, world]
**Main characters**: [Brief description of each key character]

**Act 1 — Setup**: [What is established]
**Act 2 — Conflict**: [What happens, how it escalates]
**Act 3 — Resolution**: [How it ends]

---

### 🎭 Major Themes

#### Theme 1: [e.g., Identity and belonging]
[How the book explores this theme — specific scenes and characters]

#### Theme 2: [e.g., Power and corruption]
[Explanation]

---

### 👥 Character Analysis

| Character | Role | Arc |
|-----------|------|-----|
| [Name] | [Protagonist/Antagonist/etc.] | [How they change] |

---

### 💬 Notable Quotes

> *"[Quote]"* — [Character/narrator, context]

---

### 🌍 Why It Matters
[Cultural significance, literary legacy, or why it's still relevant today]

### 📚 If You Liked This, Read:
[2–3 similar books with one-line explanation of why]
```

---

## Step 4 — Quick Mode (5-Minute Summary)

When the user wants just the essentials:

```
## ⚡ Quick Summary: [Title] by [Author]

**In one sentence**: [The whole book in 25 words or fewer]

**The 3 things you must know**:
1. [Key idea 1]
2. [Key idea 2]
3. [Key idea 3]

**The one thing to do differently after reading this**:
[Single most actionable takeaway]

**Worth reading in full?** [Yes / No / Depends — with one reason]
```

---

## Quality Rules

- Never invent quotes — only include quotes you are confident are real
- Flag if your knowledge of a very recent book may be limited
- For self-help books: be honest if the core idea could be a blog post — most can
- For dense academic/scientific books: simplify without distorting
- Always end with reading recommendations — readers who want summaries usually want more books too

Always offer: "Want me to go deeper on any specific idea?" or "Want a comparison between this book and [related book]?"
