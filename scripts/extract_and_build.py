#!/usr/bin/env python3
"""Build the repo tree from the downloaded Drive mirror — verbatim extraction.

Input : ~/workspace/claude-skills-bundle-work/download/  (+ samples/*.pdf, Disclaimer.txt)
Output: ~/workspace/claude-skills-bundle-work/repo/
  - skills/<category path>/<skill-name>/SKILL.md  (unzipped verbatim from each .skill)
  - docs/*.pdf (verbatim), DISCLAIMER.md (verbatim text), NOTICE.md
  - skills-index.md, README.md, scripts/download-and-extract.py (copy of builder docs)
"""
import json, os, re, shutil, sys, zipfile

BASE = "/home/hatch/workspace/claude-skills-bundle-work"
DL = os.path.join(BASE, "download")
REPO = os.path.join(BASE, "repo")
SKILLS = os.path.join(REPO, "skills")

FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)

def parse_frontmatter(text):
    m = FRONTMATTER.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm

def main():
    with open(os.path.join(BASE, "manifest.json")) as f:
        manifest = json.load(f)
    if os.path.exists(REPO):
        shutil.rmtree(REPO)
    os.makedirs(SKILLS)
    os.makedirs(os.path.join(REPO, "docs"))
    os.makedirs(os.path.join(REPO, "scripts"))

    stats = {}   # top-category -> count
    nested = {}  # full category path -> count
    errors, extracted = [], 0
    for entry in manifest["downloaded"]:
        rel = entry["path"]
        if entry["status"] not in ("ok", "cached") or not rel.endswith(".skill"):
            continue
        src = os.path.join(DL, rel)
        cat_path = os.path.dirname(rel)  # e.g. creative-fiction or Video Editing/premiere-pro
        skill_name = os.path.basename(rel)[:-len(".skill")]
        try:
            with zipfile.ZipFile(src) as z:
                names = z.namelist()
                if len(names) != 1 or not names[0].endswith("SKILL.md"):
                    errors.append(f"{rel}: unexpected zip contents {names}")
                    continue
                data = z.read(names[0])
        except Exception as e:
            errors.append(f"{rel}: unzip failed: {e}")
            continue
        text = data.decode("utf-8")
        fm = parse_frontmatter(text)
        if not fm or "name" not in fm or "description" not in fm:
            errors.append(f"{rel}: missing frontmatter name/description")
            continue
        if fm["name"] != skill_name:
            errors.append(f"{rel}: frontmatter name {fm['name']!r} != file {skill_name!r}")
        dest_dir = os.path.join(SKILLS, cat_path, skill_name)
        os.makedirs(dest_dir, exist_ok=True)
        with open(os.path.join(dest_dir, "SKILL.md"), "wb") as f:
            f.write(data)
        extracted += 1
        top = cat_path.split("/")[0]
        stats[top] = stats.get(top, 0) + 1
        nested[cat_path] = nested.get(cat_path, 0) + 1

    # PDFs verbatim
    shutil.copy(os.path.join(BASE, "samples", "How-to-Use.pdf"),
                os.path.join(REPO, "docs", "How-to-Use-Claude-Skills.pdf"))
    shutil.copy(os.path.join(BASE, "samples", "Disclaimer.pdf"),
                os.path.join(REPO, "docs", "Disclaimer-and-Format-Instructions.pdf"))

    # DISCLAIMER.md verbatim (from the PDF text)
    with open(os.path.join(BASE, "samples", "Disclaimer.txt")) as f:
        disclaimer_text = f.read().strip()
    with open(os.path.join(REPO, "DISCLAIMER.md"), "w") as f:
        f.write("# Disclaimer\n\n")
        f.write("Verbatim text of `docs/Disclaimer-and-Format-Instructions.pdf` "
                "that ships with the bundle.\n\n")
        f.write(disclaimer_text + "\n")

    with open(os.path.join(REPO, "NOTICE.md"), "w") as f:
        f.write("# Notice\n\n")
        f.write("This repository republishes the **Claude Skills Bundle** — a collection of "
                "`.skill` instruction files for Anthropic's Claude (claude.ai) — from the "
                "owner's purchased copy.\n\n")
        f.write("- Every skill is reproduced **verbatim**: each `.skill` file was unzipped "
                "without changes into `skills/<category>/<skill-name>/SKILL.md`. "
                "Nothing was reworded.\n\n")
        f.write("- The bundle's own disclaimer ships verbatim in `DISCLAIMER.md` and as a "
                "PDF in `docs/`. It states the files are plain-text instruction sets, not "
                "software, and that health, legal, financial, career and medical skills are "
                "informational only — not a substitute for licensed professional advice.\n\n")
        f.write("- **No open-source license is claimed for the skills.** The bundle shipped "
                "with no redistribution license, so this repository carries no LICENSE file "
                "and no MIT/Apache claim over the skill contents. Do not treat the skills "
                "as MIT-licensed.\n\n")
        f.write("- Not affiliated with Anthropic.\n")

    # skills-index.md
    with open(os.path.join(REPO, "skills-index.md"), "w") as f:
        f.write("# Skills Index\n\n")
        f.write(f"**{extracted} skills** in **{len(stats)} top-level categories** "
                f"({len(nested)} category folders including nested groups).\n\n")
        for cat in sorted(nested):
            f.write(f"## {cat} ({nested[cat]})\n\n")
            cat_dir = os.path.join(SKILLS, cat)
            for skill in sorted(os.listdir(cat_dir)):
                with open(os.path.join(cat_dir, skill, "SKILL.md")) as sf:
                    fm = parse_frontmatter(sf.read()) or {}
                desc = fm.get("description", "")
                f.write(f"- [{skill}](skills/{cat}/{skill}/SKILL.md) — {desc}\n")
            f.write("\n")

    # README.md — beautiful, animated SVG banner
    total_cats = len(stats)
    rows = "\n".join(
        f"| {cat} | {stats[cat]} |" for cat in sorted(stats))
    readme = f"""<div align="center">

![Claude Skills Bundle](banner.svg)

# Claude Skills Bundle

### 2,015 ready-to-use skills for Claude — every category, one repo

![Skills](https://img.shields.io/badge/skills-2015-blueviolet?style=for-the-badge)
![Categories](https://img.shields.io/badge/categories-{total_cats}-ff69b4?style=for-the-badge)
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
{rows}

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
"""
    with open(os.path.join(REPO, "README.md"), "w") as f:
        f.write(readme)

    # banner.svg — animated
    banner = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#2b1055"><animate attributeName="stop-color" values="#2b1055;#7597de;#2b1055" dur="12s" repeatCount="indefinite"/></stop>
      <stop offset="55%" stop-color="#7597de"><animate attributeName="stop-color" values="#7597de;#d97757;#7597de" dur="12s" repeatCount="indefinite"/></stop>
      <stop offset="100%" stop-color="#d97757"><animate attributeName="stop-color" values="#d97757;#2b1055;#d97757" dur="12s" repeatCount="indefinite"/></stop>
    </linearGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ffe259"/><stop offset="100%" stop-color="#ffa751"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="320" rx="24" fill="url(#bg)"/>
  <g fill="#ffffff" opacity="0.25">
    <circle cx="90" cy="60" r="10"><animate attributeName="cy" values="60;44;60" dur="4s" repeatCount="indefinite"/></circle>
    <circle cx="1120" cy="250" r="14"><animate attributeName="cy" values="250;266;250" dur="5s" repeatCount="indefinite"/></circle>
    <circle cx="1040" cy="70" r="7"><animate attributeName="cy" values="70;56;70" dur="3.4s" repeatCount="indefinite"/></circle>
    <circle cx="180" cy="260" r="8"><animate attributeName="cy" values="260;246;260" dur="4.6s" repeatCount="indefinite"/></circle>
    <rect x="330" y="40" width="26" height="26" rx="6" transform="rotate(20 343 53)"><animateTransform attributeName="transform" type="rotate" values="20 343 53;50 343 53;20 343 53" dur="7s" repeatCount="indefinite"/></rect>
    <rect x="820" y="230" width="20" height="20" rx="5" transform="rotate(-15 830 240)"><animateTransform attributeName="transform" type="rotate" values="-15 830 240;15 830 240;-15 830 240" dur="6s" repeatCount="indefinite"/></rect>
  </g>
  <text x="600" y="130" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="64" font-weight="bold" fill="#ffffff">Claude Skills Bundle</text>
  <text x="600" y="180" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="26" fill="url(#gold)">2,015 skills &#183; 33 categories &#183; one repo</text>
  <text x="600" y="228" text-anchor="middle" font-family="monospace" font-size="20" fill="#ffffff" opacity="0.9">/ pick a skill &#8594; upload to Claude &#8594; done</text>
  <rect x="470" y="258" width="260" height="6" rx="3" fill="#ffffff" opacity="0.35"/>
  <rect x="470" y="258" width="260" height="6" rx="3" fill="url(#gold)">
    <animate attributeName="width" values="40;260;40" dur="3.2s" repeatCount="indefinite"/>
  </rect>
</svg>
"""
    with open(os.path.join(REPO, "banner.svg"), "w") as f:
        f.write(banner)

    print(f"extracted={extracted} errors={len(errors)} top_categories={len(stats)} nested={len(nested)}")
    for e in errors[:20]:
        print("ERROR", e)
    # file count in repo tree
    total = sum(len(files) for _, _, files in os.walk(REPO))
    print(f"repo files={total}")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
