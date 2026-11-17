---
name: ai-tool-stack-builder
description: Recommends and designs a complete AI tool stack for any role, business, or use case — with specific tools, integration points, and implementation order. Use when the user says "what AI tools should I use for [goal]", "AI stack for [business type]", "best AI tools for [role]", "how do I build an AI-powered [workflow]", or "I want to use AI to automate [process] — where do I start". Always use this skill — the AI tools landscape changes rapidly and most people use 1-2 tools when they could be using a coordinated stack that multiplies their output.
---
# AI Tool Stack Builder Skill

## Step 1 — Gather Inputs
- **Role or business type**: (solopreneur / marketer / developer / operations / agency / etc.)
- **Primary goals**: (save time / increase output / reduce costs / scale operations)
- **Current tools**: (what they already use — don't replace what's working)
- **Budget**: Free only / Under $50/month / Under $200/month / Enterprise
- **Technical level**: Non-technical / Somewhat technical / Developer

## Step 2 — Stack Architecture

```
## AI Tool Stack: [Role/Business]
Budget: [X/month] | Level: [Technical level]

---

STACK OVERVIEW
[3-sentence summary of what this stack does and why these tools work together]

---

LAYER 1 — FOUNDATION (LLM / Core AI)
The brain of your stack — everything else plugs into this.

Primary LLM: [Claude / ChatGPT / Gemini]
Why: [Specific reason for this use case]
Use for: [Primary tasks in this person's workflow]
Cost: [$/month]
Upgrade path: [When to upgrade to a more powerful tier]

---

LAYER 2 — CONTENT & WRITING
AI-assisted writing and content creation tools.

Tool: [Specific tool — e.g., Claude.ai / ChatGPT / Jasper]
Use for: [Blog posts / emails / social captions / ad copy / reports]
Cost: [X]

Tool: [Grammarly / LanguageTool]
Use for: [Final proofread — catches what LLMs miss]
Cost: [X]

---

LAYER 3 — IMAGE & VISUAL GENERATION
AI image and design tools.

Tool: [Midjourney / DALL-E 3 / Ideogram / Adobe Firefly]
Use for: [Social media images / thumbnails / product mockups / illustrations]
Cost: [X]
Note: [When to use which for this person's specific use case]

Tool (optional): [Canva AI / Adobe Express]
Use for: [Templated designs with AI-generated elements]
Cost: [X]

---

LAYER 4 — AUTOMATION & WORKFLOW
Tools that connect everything and run processes automatically.

Tool: [n8n / Make / Zapier]
Use for: [Connecting tools, automating repetitive tasks]
Cost: [X]
Key automations to build first:
1. [Most valuable automation for this role]
2. [Second automation]
3. [Third automation]

Tool (if AI agent needed): [n8n AI Agent / LangChain / Dify]
Use for: [Autonomous multi-step tasks]
Cost: [X]

---

LAYER 5 — RESEARCH & KNOWLEDGE
AI tools for finding, processing, and managing information.

Tool: [Perplexity / ChatGPT with search / Claude with search]
Use for: [Research, fact-checking, competitive analysis]
Cost: [X]

Tool (if document heavy): [NotebookLM / Claude with documents]
Use for: [Chat with PDFs, contracts, reports, notes]
Cost: [X]

---

LAYER 6 — SPECIALIZED TOOLS (role-specific)
[Add 2-3 AI tools specific to their industry/role]

[For marketers]: [AdCreative.ai / Lately / Buffer AI]
[For developers]: [GitHub Copilot / Cursor / Tabnine]
[For operations]: [Notion AI / ClickUp AI / Mem.ai]
[For sales]: [Apollo AI / Lavender / Gong]
[For video]: [Descript / HeyGen / Opus Clip]

---

TOTAL MONTHLY COST ESTIMATE:
Essential tier: $[X]/month
Full stack: $[X]/month
[Breakdown: which tools to start with vs add later]

---

IMPLEMENTATION ORDER (don't add everything at once)
Week 1: [Core LLM + most important specialist tool]
Week 2-3: [Add automation layer once LLM workflows are established]
Month 2: [Add visual layer]
Month 3: [Add specialized tools and refine automations]

---

INTEGRATION MAP
[Tool A] → outputs to → [Tool B]
[Tool C] + [Tool D] → combined in → [n8n workflow]
[Core LLM] → powers → [all writing + research layers]
```

## Step 3 — Stack by Role Quick Reference

**Solopreneur/Creator**:
Claude.ai + Midjourney + n8n + Descript + Perplexity + Canva AI

**Marketing team**:
ChatGPT Teams + AdCreative.ai + Make + Jasper + Surfer SEO + Buffer AI

**Developer**:
Claude API + Cursor + GitHub Copilot + LangChain + n8n self-hosted

**Operations/Admin**:
Claude.ai + Notion AI + Make + NotebookLM + Otter.ai

**Agency**:
Claude API + Midjourney + n8n + Descript + Perplexity + custom LLM app

## Step 4 — The "Start Small" Rule

Most people fail with AI tools by adopting too many at once.
Start with ONE tool that solves your biggest time drain.
Master it in 2-3 weeks before adding the next.
The stack compounds — each tool becomes more useful when combined with others.

Always offer: "Want a week-by-week implementation plan to roll this stack out without overwhelm?"
