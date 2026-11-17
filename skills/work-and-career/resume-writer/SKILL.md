---
name: resume-writer
description: Builds ATS-optimized, professionally formatted resumes tailored to a specific job description, from a career summary or existing resume. Use this skill whenever the user wants to create or improve a resume, or says things like "write my resume", "help me with my CV", "update my resume for this job", "make my resume ATS-friendly", "I need a resume for [role]", "rewrite my resume", or pastes their work history and asks for help. Also trigger when the user wants to tailor an existing resume to a new job posting. Always use this skill — resume writing has specific conventions (ATS optimization, action verbs, quantification) that dramatically affect interview callback rates.
---

# Resume Writer Skill

Build a polished, ATS-optimized resume that gets past filters and impresses hiring managers.

## Step 1 — Gather Inputs

Ask in one message if not provided:
- **Target role/job title** (and job description if they have one)
- **Years of experience** (entry-level, mid, senior, executive)
- **Current resume or work history** (paste what they have, or describe experience)
- **Key skills** (technical skills, tools, certifications)
- **Top 2–3 achievements** they're proud of (with numbers if possible)
- **Education** (degree, institution, year)
- **Resume format preference** (chronological / functional / hybrid)

---

## Step 2 — ATS Optimization Strategy

Before writing, analyze the job description (if provided):

```
## 🔍 Job Description Analysis

**Key keywords to include**:
- Hard skills: [list from JD]
- Soft skills: [list from JD]
- Tools/technologies: [list from JD]
- Exact phrases to mirror: [list]

**ATS rules applied**:
- No tables, columns, headers/footers, or graphics (ATS can't parse these)
- Standard section headings: Experience, Education, Skills (not creative names)
- Keywords from JD used naturally in bullet points
- File format: .docx recommended over PDF for most ATS systems
```

---

## Step 3 — Resume Structure

### Contact Header
```
[FULL NAME]
[City, State/Country] | [Phone] | [Email] | [LinkedIn URL] | [Portfolio/GitHub — if relevant]
```
Rules: No photo, no date of birth, no full street address, no marital status.

### Professional Summary (3–4 lines)
```
[Job Title] with [X] years of experience in [key domain]. Proven track record of [top achievement]. 
Skilled in [top 3 skills]. Seeking to [what you want to bring to the new role].
```
Rules: Tailor to each job. No "I" statements. No clichés ("hardworking", "team player", "passionate").

### Work Experience
Each role follows this format:
```
JOB TITLE | Company Name | City, Country | Month Year – Month Year

• [Strong action verb] + [what you did] + [result/impact with number]
• [Action verb] + [task] + [outcome]
• [Action verb] + [task] + [outcome]
```

**Action verb bank by function**:
- Leadership: Led, Directed, Managed, Oversaw, Spearheaded, Championed
- Achievement: Achieved, Exceeded, Delivered, Surpassed, Grew, Increased
- Creation: Built, Developed, Designed, Launched, Established, Implemented
- Analysis: Analyzed, Identified, Assessed, Evaluated, Researched, Diagnosed
- Improvement: Streamlined, Optimized, Reduced, Improved, Transformed, Restructured
- Collaboration: Collaborated, Partnered, Coordinated, Facilitated, Liaised

**Quantification guide** — always try to add numbers:
- How many? (managed a team of 12, 500+ clients)
- How much? ($2M budget, $400K revenue increase)
- How fast? (reduced processing time by 40%)
- How often? (weekly reports, 200 calls/month)
- How large? (enterprise clients, Fortune 500)

### Education
```
DEGREE, Major | Institution | Year Graduated
[GPA if >3.5 and within 3 years of graduation]
[Relevant coursework, honors, or thesis — only if entry-level]
```

### Skills Section
```
Technical Skills: [List relevant tools, software, languages, platforms]
Certifications: [Name | Issuing org | Year]
Languages: [Language (Proficiency level)]
```

---

## Step 4 — Full Resume Output

```
## 📄 Resume: [Name] — [Target Role]

---

[FULL NAME]
[City] | [Phone] | [Email] | [LinkedIn]

---

PROFESSIONAL SUMMARY
[3–4 tailored lines]

---

WORK EXPERIENCE

[JOB TITLE] | [Company] | [Location] | [Date – Date]
• [Bullet 1 — strongest achievement, quantified]
• [Bullet 2]
• [Bullet 3]
• [Bullet 4 — max 5 bullets per role]

[JOB TITLE] | [Company] | [Location] | [Date – Date]
• [Bullets]

---

EDUCATION
[Degree] | [Institution] | [Year]

---

SKILLS
[Technical] | [Tools] | [Certifications] | [Languages]
```

---

## Step 5 — Resume Review Checklist

After drafting, verify:

```
## ✅ ATS & Quality Checklist

### ATS Compliance
- [ ] No tables, text boxes, columns, or graphics
- [ ] Standard section headings used
- [ ] Saved as .docx (not PDF unless specified)
- [ ] Keywords from job description included naturally
- [ ] No headers/footers (ATS often can't read them)

### Content Quality
- [ ] Every bullet starts with a strong action verb
- [ ] At least 50% of bullets have a number/metric
- [ ] No "responsible for" or "duties included" language
- [ ] No first-person pronouns
- [ ] No clichés (hardworking, passionate, team player)
- [ ] Dates consistent format throughout (Jan 2022, not 01/2022)
- [ ] No unexplained gaps > 6 months

### Length
- [ ] 1 page for < 10 years experience
- [ ] 2 pages max for 10+ years (never 3 pages)
- [ ] Most recent role has most bullets (4–5); older roles fewer (2–3)

### Tailoring
- [ ] Job title in summary matches target role
- [ ] Top skills in JD appear in resume
- [ ] Company research reflected (optional but impressive)
```

Always offer: "Want me to tailor this to a specific job posting?" or "Want a matching cover letter for this role?"
