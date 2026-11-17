---
name: resolve-collaboration
description: Teaches multi-user collaboration features in Resolve. Use when the user says things like 'collaborate in DaVinci Resolve', 'shared project Resolve', 'multi-user editing Resolve'.
---

# DaVinci Resolve Collaboration Skill

## Step 1 — Gather Inputs

- Software version and platform (Windows/Mac)
- Experience level: beginner/intermediate/advanced
- Type of project: social media/film/documentary/YouTube/corporate
- Specific task or technique
- Output format or delivery requirement

## Step 2 — Core Output

Resolve collaboration: PostgreSQL database (required for multi-user projects — local or server) → User accounts (each user logs in / changes are tracked) → Bin locking (a user locks a bin while working — others see it as locked) → Chat (built-in text chat between collaborators in the UI) → Remote Grades (share a grade from one timeline to another) → Timeline compare (see what changed between versions) → Project sharing (one project / multiple editors on different pages simultaneously) → Cloud collaboration (Resolve 18+ / cloud-based shared projects).

## Step 3 — Quality & Polish

- PostgreSQL database required for multi-user: the local SQLite database does not support collaboration
- Bin locking prevents conflicts: always lock the bin you are working in
- One editor per page simultaneously: two editors cannot be on the Edit page at the same time

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Software features and interfaces change with updates — always refer to the official documentation for your specific software version. Some features mentioned may require paid subscriptions or specific hardware.
