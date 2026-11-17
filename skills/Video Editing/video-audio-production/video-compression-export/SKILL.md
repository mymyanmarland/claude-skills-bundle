---
name: video-compression-export
description: Teaches optimising video file size and quality for different delivery contexts. Use when the user says things like 'reduce video file size', 'optimise video for web', 'best export settings for file size vs quality'.
---

# Video Compression and Export Optimisation Skill

## Step 1 — Gather Inputs

- Software version and platform (Windows/Mac)
- Experience level: beginner/intermediate/advanced
- Type of project: social media/film/documentary/YouTube/corporate
- Specific task or technique
- Output format or delivery requirement

## Step 2 — Core Output

Video compression and export: Two-pass encoding (VBR 2-pass: analyses the whole clip first / more efficient than single-pass) → Target bitrate (1080p: 8-12 Mbps for streaming / 20 Mbps for downloads / 40+ Mbps for 4K) → Resolution for purpose (1080p is fine for most web delivery — 4K adds file size without visible benefit on most displays) → Frame rate matching (deliver at the same frame rate as the source — converting frame rates causes judder) → Audio codec (AAC 128kbps for streaming / 320kbps for quality / PCM for broadcast) → HandBrake (free encoder for batch compression) → Colour space tagging (tag the output file with the correct colour space).

## Step 3 — Quality & Polish

- VBR 2-pass for quality at size: takes longer but produces noticeably better results
- Match frame rate to source: converting 25fps to 30fps causes noticeable judder
- HandBrake for batch encoding: free and produces excellent H.264 and H.265 output

Always offer a relevant next step or tip to try.

---
📌 Note: This content is for educational purposes only. Software features and interfaces change with updates — always refer to the official documentation for your specific software version. Some features mentioned may require paid subscriptions or specific hardware.
