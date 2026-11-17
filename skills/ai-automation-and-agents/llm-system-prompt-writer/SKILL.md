---
name: llm-system-prompt-writer
description: Writes production-quality system prompts for LLM-powered apps, chatbots, agents, and automated pipelines. Use when the user says "write a system prompt for my AI", "system prompt for [use case]", "how do I instruct an LLM to [behavior]", "prompt for my chatbot", "instructions for my AI assistant", or "I can't get consistent output from my LLM". Always use this skill — system prompts are the most leveraged part of any LLM product and most developers write them too short, too vague, or missing critical behavioral guardrails.
---
# LLM System Prompt Writer Skill

## Step 1 — Gather Inputs
- **Use case**: What is this LLM being used for? (customer support / code assistant / data extractor / content writer / agent / classifier)
- **Model**: GPT-4o / Claude / Gemini / Llama / Mistral
- **Output format needed**: Free text / JSON / Markdown / Code / Structured fields
- **Tone and persona**: (if customer-facing)
- **What it should NEVER do**: (safety/scope constraints)
- **Context it always needs**: (company name, product, user role, date format, etc.)

## Step 2 — System Prompt Architecture

A production system prompt has these components:

```
1. IDENTITY & ROLE — who/what the LLM is
2. TASK DEFINITION — exactly what it does
3. CONTEXT — background information it needs
4. BEHAVIORAL RULES — what it always/never does
5. OUTPUT FORMAT — exactly how to structure responses
6. EXAMPLES — few-shot demonstrations (optional but powerful)
7. EDGE CASE HANDLING — what to do when things are ambiguous
```

## Step 3 — System Prompt Output

```
## System Prompt: [Use Case]
Model: [X] | Use case: [X] | Output: [Format]

---

[IDENTITY]
You are [Name], [brief description of role and expertise].
[If customer-facing: "You work for [Company]. You help [users] with [tasks]."]
[If internal tool: "You are a specialized assistant for [specific function]."]

[TASK]
Your primary job is to [specific task description].
You [do X] when [condition A].
You [do Y] when [condition B].

[CONTEXT]
[Static information the model always needs:]
- Company/product: [Name and description]
- Current date: {{current_date}} [inject dynamically]
- User role: {{user_role}} [inject if applicable]
- [Any domain knowledge, terminology, or facts the model needs]

[BEHAVIORAL RULES]
Always:
- [Rule 1 — specific and testable: "Always respond in the same language the user writes in"]
- [Rule 2 — e.g., "Always ask for clarification if the request is ambiguous before proceeding"]
- [Rule 3 — e.g., "Always cite the source section when answering from documents"]

Never:
- [Rule 1 — e.g., "Never make up information you don't have"]
- [Rule 2 — e.g., "Never discuss competitors by name"]
- [Rule 3 — e.g., "Never provide [out-of-scope content]"]

If [edge case]:
- [What to do — e.g., "If the user asks about pricing, direct them to [URL/contact]"]

[OUTPUT FORMAT]
Respond in the following format:
[Exact format specification — JSON schema / markdown structure / plain text rules]

[If JSON output:]
Return ONLY valid JSON with no markdown fences or explanation:
{
  "field_1": "string",
  "field_2": "number",
  "field_3": ["array", "of", "strings"]
}

[If structured text:]
Use this structure:
**Summary**: [1 sentence]
**Details**: [Explanation]
**Next step**: [Action item]

[LENGTH GUIDANCE]
[Short answers: "Be concise. 1-3 sentences unless detail is requested."]
[Or: "Provide thorough responses. Cover all aspects of the question."]

[FEW-SHOT EXAMPLES — optional but highly effective]
Example input: "[Sample input]"
Example output: "[Exact desired output]"

Example input: "[Edge case input]"
Example output: "[How to handle it]"
```

## Step 4 — System Prompt by Use Case

**Customer Support Bot**:
- Emphasize: empathy, escalation paths, never making promises, tone consistency
- Critical rules: out-of-scope handling, competitor mentions, data privacy

**Data Extraction / Parsing**:
- Emphasize: exact JSON schema, null handling, confidence levels
- Critical rules: never infer missing data, flag ambiguous fields

**Code Assistant**:
- Emphasize: language preference, commenting style, security considerations
- Critical rules: never suggest deprecated patterns, always test edge cases

**Content Writer**:
- Emphasize: tone/voice guide, audience, format, length
- Critical rules: brand voice do's and don'ts, topics to avoid

**AI Agent**:
- Emphasize: tool usage decision logic, stopping conditions, output format
- Critical rules: irreversible action confirmation, scope boundaries

## Step 5 — System Prompt Testing Protocol

1. **Happy path test**: Normal expected input → correct output?
2. **Edge case test**: Empty input / ambiguous input / very long input
3. **Adversarial test**: "Ignore previous instructions" / prompt injection attempts
4. **Format compliance test**: Does it always return the specified format?
5. **Constraint test**: Does it respect the "never" rules?
6. **Tone test**: Consistent across 10 different phrasings of the same request?

## Step 6 — Common System Prompt Mistakes

❌ "Be helpful and accurate" — too vague, tells the model nothing it doesn't already know
❌ No output format specification — results are inconsistent
❌ No edge case handling — model makes up behavior for unusual inputs
❌ Too long with irrelevant context — dilutes attention on what matters
❌ No examples — model interprets instructions differently than intended

✅ Specific behavioral rules with testable conditions
✅ Exact output format with a schema or example
✅ Explicit scope: what it does AND what it doesn't do
✅ A few examples showing edge cases handled correctly

Always offer: "Want me to write test cases to validate this system prompt?"
