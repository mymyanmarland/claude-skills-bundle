<div align="center">

![Claude Skills Bundle](banner.svg)

# Claude Skills Bundle

### 2,015 ready-to-use skills for Claude — every category, one repo

![Skills](https://img.shields.io/badge/skills-2015-blueviolet?style=for-the-badge)
![Categories](https://img.shields.io/badge/categories-33-ff69b4?style=for-the-badge)
![Format](https://img.shields.io/badge/format-SKILL.md-00b894?style=for-the-badge)
![Claude](https://img.shields.io/badge/works_with-claude.ai-D97757?style=for-the-badge)

</div>

---

## What is this?

A bundle of **2,015 `.skill` instruction files** for [Claude](https://claude.ai) — plain-text
instruction sets that guide Claude's behaviour when you upload them to a conversation or
project. They are not software, apps or plugins. They do not run on their own.

Each skill is one focused job: a writing coach, a fitness planner, a video-editing guide,
a tax checklist, a story doctor — pick one, upload it, and Claude follows its steps.

> **How a skill works:** every skill is a `SKILL.md` with a short `name` + `description`
> header and step-by-step instructions. Claude reads the steps and follows them.

## Categories

| Category | Skills |
|---|---:|
| DIY | 348 |
| Excel | 100 |
| Sports | 384 |
| Video Editing | 97 |
| ai-automation-and-agents | 13 |
| career-and-jobs | 47 |
| content-writing | 50 |
| copywriting | 9 |
| creative-and-storytelling | 14 |
| creative-fiction | 50 |
| design-and-visual | 51 |
| education-and-teaching | 49 |
| email-marketing | 50 |
| entrepreneurship | 48 |
| family-and-home | 49 |
| finance-and-money | 49 |
| health-and-fitness | 50 |
| hobbies-and-crafts | 50 |
| humor-and-entertainment | 49 |
| legal-writing | 51 |
| marketing-and-branding | 61 |
| nonprofit-and-social | 10 |
| personal-growth | 38 |
| podcasting | 10 |
| productivity-and-planning | 49 |
| research-and-analysis | 48 |
| sales-and-persuasion | 47 |
| social-media | 46 |
| travel-and-adventure | 43 |
| travel-and-lifestyle | 10 |
| web-and-app-development | 10 |
| work-and-career | 23 |
| writing-and-content | 12 |

Full list with one-line descriptions: **[skills-index.md](skills-index.md)**

Nested groups live inside their parent: `Video Editing` splits into CapCut, Premiere Pro,
Final Cut Pro, DaVinci Resolve, After Effects and more; `DIY` into 35 crafts; `Excel` into
10 workbooks; `Sports` into 39 sports.

## Use a skill on claude.ai

1. Pick a skill folder, e.g. `skills/creative-fiction/story-plot-fixer/`
2. Zip it back into a `.skill` file — the folder name must match the file name:
   ```bash
   cd skills/creative-fiction && zip -r story-plot-fixer.skill story-plot-fixer
   ```
3. On [claude.ai](https://claude.ai): **Customize → Skills → + → Create skill** → upload the `.skill` file
4. Turn the skill **on**, then in a new chat type `/` and pick it

Or use a skill folder directly in Claude Code: copy it into `.claude/skills/`.

Full illustrated guide: [`docs/How-to-Use-Claude-Skills.pdf`](docs/How-to-Use-Claude-Skills.pdf)

## Repo layout

```
claude-skills-bundle/
├── README.md / banner.svg
├── DISCLAIMER.md / NOTICE.md     # rights + disclaimer, read before sharing
├── docs/                          # the bundle's own PDFs, verbatim
├── skills/
│   ├── creative-fiction/story-plot-fixer/SKILL.md
│   ├── health-and-fitness/...
│   └── ... 2,015 skills in 33 categories
├── skills-index.md                # every skill, with descriptions
└── scripts/
```

## Important — read this

- The skills are reproduced **verbatim** from the purchased bundle — nothing was reworded.
- The bundle's disclaimer ships as-is in [`DISCLAIMER.md`](DISCLAIMER.md). Skills in
  health, legal, financial, career and medical categories are **informational only** —
  not a substitute for licensed professional advice.
- **No open-source license is claimed for the skills.** The bundle shipped with no
  redistribution license, so there is no LICENSE file here. See [`NOTICE.md`](NOTICE.md).
- Not affiliated with Anthropic.
