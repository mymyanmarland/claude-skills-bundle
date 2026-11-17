---
name: prompt-chain-architect
description: Designs multi-step prompt chains and sequential LLM pipelines where the output of one prompt feeds the next, for complex AI workflows. Use when the user says "prompt chain for [task]", "multi-step AI pipeline", "chain of prompts for [use case]", "sequential AI processing for [workflow]", or "how do I break [complex task] into AI steps". Always use this skill — complex AI tasks fail when given to a single prompt; prompt chains isolate each concern and produce dramatically better results.
---
# Prompt Chain Architect Skill

## Step 1 — Gather Inputs
- **End goal**: What should the final output be?
- **Input data**: What does the chain start with?
- **Complexity**: How many distinct thinking steps does this require?
- **Model constraints**: Same model for all steps, or mix of models?
- **Platform**: Python / LangChain / n8n / Make / Manual / API

## Step 2 — Chain Design Principles

Why chain prompts instead of one big prompt:
1. **Isolation**: Each step has one job → fewer errors
2. **Inspection**: You can see and debug each intermediate output
3. **Optimization**: Use cheap models for simple steps, powerful for complex
4. **Parallelization**: Independent steps can run simultaneously
5. **Caching**: Cache expensive steps, re-run only what changes

## Step 3 — Prompt Chain Blueprint

```
## Prompt Chain: [Goal]
Steps: [X] | Input: [Type] | Final output: [Type]

---

CHAIN OVERVIEW
[One sentence: what this chain does from input to final output]

INPUT → [Step 1] → [Step 2] → [Step 3] → ... → FINAL OUTPUT

---

STEP 1 — [Name, e.g., "Extract & Structure"]
Purpose: [What this step does and why it's needed]
Model: [GPT-4o-mini / Claude Haiku — use cheap model for simple steps]
Temperature: [0.0-0.3 for factual extraction, 0.7-1.0 for creative]

System prompt:
"[System context for this specific step only]"

User prompt template:
"[Instruction for this step]

Input:
{input_from_previous_step_or_raw_input}

Output format:
[Exact format required — JSON schema / bullet list / structured text]
Return ONLY the [format], no explanation."

Expected output:
[Example of what this step should return]

→ feeds into Step 2 as: {step_1_output}

---

STEP 2 — [Name, e.g., "Analyze & Score"]
Purpose: [What this step does]
Model: [Model selection + reason]
Temperature: [X]

System prompt:
"[Context specific to this step]"

User prompt template:
"[Instruction]

Previous step output:
{step_1_output}

[Additional input if needed]

Output format:
[Format specification]"

Expected output:
[Example]

→ feeds into Step 3 as: {step_2_output}

---

STEP 3 — [Name, e.g., "Generate Final Output"]
Purpose: [Final synthesis or generation step]
Model: [Most capable model — this is where quality matters most]
Temperature: [X]

System prompt:
"[Full context assembled from all previous steps]"

User prompt template:
"Based on the following analysis:

Structured data: {step_1_output}
Analysis results: {step_2_output}

[Final instruction]

Output format:
[Exact specification of final output]"

---

PARALLEL STEPS (if applicable):
Steps [X] and [Y] can run simultaneously — they don't depend on each other.
Merge their outputs before Step [Z].

---

CONDITIONAL BRANCHES:
If [step_N_output.field] == "[value]":
  → Run BRANCH A (steps X, Y, Z)
Else:
  → Run BRANCH B (steps A, B, C)

---

CHAIN IMPLEMENTATION (Python pseudocode):
```python
# Step 1
step1_result = llm.invoke(
    step1_prompt.format(input=raw_input)
)

# Step 2
step2_result = llm.invoke(
    step2_prompt.format(step_1_output=step1_result)
)

# Step 3 (final)
final_output = llm.invoke(
    step3_prompt.format(
        step_1_output=step1_result,
        step_2_output=step2_result
    )
)
```

---

VALIDATION CHECKPOINTS
After Step [X]: Validate output matches expected schema before continuing
If validation fails: [Retry with clarification prompt / Log error / Fall back to default]
```

## Step 4 — Common Chain Patterns

**Extract → Analyze → Generate** (most common):
Raw text → Structured data → Analysis → Final output

**Research → Draft → Critique → Revise**:
Topic → First draft → Self-critique prompt → Improved version

**Classify → Route → Specialize**:
Input → Category → Route to specialized prompt → Output

**Parallel Research → Synthesize**:
Run N research prompts in parallel → Merge → Synthesize into one report

**Iterative Refinement Loop**:
Draft → Evaluate (score 1-10) → If score < 8, improve → Repeat max 3×

## Step 5 — Cost Optimization

| Step type | Best model | Why |
|-----------|-----------|-----|
| Extraction/parsing | GPT-4o-mini / Haiku | Simple, cheap, fast |
| Classification | GPT-4o-mini | Low complexity |
| Analysis | GPT-4o / Sonnet | Medium complexity |
| Final generation | GPT-4o / Claude Opus | Quality matters here |
| Summarization | GPT-4o-mini | Well-defined task |

Always offer: "Want me to write the full Python implementation of this chain?"
