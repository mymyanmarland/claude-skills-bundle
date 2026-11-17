---
name: ai-agent-designer
description: Designs complete AI agent architectures with tools, memory, decision loops, and system prompts for autonomous task execution. Use when the user says "design an AI agent for", "build an agent that can [task]", "autonomous AI for [process]", "multi-step AI agent", "agent with tools for [use case]", or "how do I build an AI agent that does [thing]". Always use this skill — AI agents require specific architectural decisions (ReAct vs plan-and-execute, tool selection, memory design, stopping conditions) that generic LLM prompting advice doesn't cover.
---
# AI Agent Designer Skill

## Step 1 — Gather Inputs
- **Goal**: What should the agent accomplish autonomously?
- **Inputs**: What information does the agent start with?
- **Available tools**: (web search / code execution / API calls / file read/write / database / email)
- **Framework**: LangChain / LlamaIndex / CrewAI / AutoGen / n8n AI Agent / Custom / No preference
- **Autonomy level**: Fully autonomous / Human-in-the-loop / Supervised execution
- **Memory needs**: Single session / Persistent / Long-term learning

## Step 2 — Agent Architecture Decision

```
## Agent Architecture: [Goal]

AGENT TYPE SELECTION:
[ ] ReAct Agent — Think → Act → Observe → Repeat
    Best for: Open-ended research, multi-step tasks with unknown path
[ ] Plan-and-Execute — Plan all steps first, then execute
    Best for: Predictable tasks, faster execution, fewer LLM calls
[ ] Multi-Agent System — Multiple specialized agents collaborate
    Best for: Complex workflows, parallel tasks, specialized expertise
[ ] Tool-Calling Agent — Single LLM with function/tool calling
    Best for: Structured tasks, API integrations, faster/cheaper

RECOMMENDED FOR THIS USE CASE: [Type + reason why]
```

## Step 3 — Full Agent Design

```
## AI Agent Design: [Agent Name]
Framework: [X] | Autonomy: [X] | Model: [GPT-4o / Claude / Gemini]

---

SYSTEM PROMPT
[The core instruction that defines the agent's identity, capabilities, and constraints]

"You are [Agent Name], an AI agent specialized in [domain].

Your goal: [Specific objective]

You have access to the following tools:
- [Tool 1]: [When and how to use it]
- [Tool 2]: [When and how to use it]
- [Tool 3]: [When and how to use it]

Decision rules:
- Always [rule 1 — e.g., verify information before acting]
- Never [rule 2 — e.g., take irreversible actions without confirmation]
- If [condition], then [action]

Output format: [How the agent should structure its final response]"

---

TOOLS CONFIGURATION

Tool 1: [Name]
Type: [Web search / API call / Code executor / File reader / Database query]
Function signature:
  name: "[tool_name]"
  description: "[When the agent should call this tool]"
  parameters:
    query: string — [description]
    [other params]
Returns: [What data comes back]

Tool 2: [Name]
[Same structure]

Tool 3: [Name]
[Same structure]

---

MEMORY DESIGN

Short-term (in-context):
[What the agent keeps in its context window during execution]

Long-term (persistent):
[Vector store / database for facts across sessions — or none needed]

Entity memory:
[Track specific entities: people, companies, tasks — or none needed]

---

EXECUTION LOOP

Step 1 — RECEIVE task input
Step 2 — THINK: What do I need to know? What tools should I use?
Step 3 — ACT: Call the appropriate tool
Step 4 — OBSERVE: What did the tool return?
Step 5 — DECIDE: Is the goal achieved? If yes → output. If no → back to Step 2
Step 6 — OUTPUT: Format and return final result

Max iterations: [X] — prevents infinite loops
Stopping condition: [When the agent considers the task complete]

---

HUMAN-IN-THE-LOOP CHECKPOINTS (if applicable)
- Before [irreversible action]: Ask human for confirmation
- After [number] iterations: Report progress and ask to continue
- When confidence < [threshold]: Flag for human review

---

ERROR HANDLING
- Tool failure: Retry [X] times, then try alternative tool, then report failure
- Ambiguous task: Ask clarifying question before proceeding
- Out of scope: Politely decline and explain boundaries

---

AGENT PSEUDOCODE
```python
agent = Agent(
    llm=ChatOpenAI(model="gpt-4o"),
    tools=[tool_1, tool_2, tool_3],
    system_prompt=SYSTEM_PROMPT,
    memory=ConversationBufferMemory(),
    max_iterations=10,
    verbose=True
)

result = agent.run(task_input)
```

---

EVALUATION CHECKLIST
- [ ] Does the agent stay on task without drifting?
- [ ] Does it use the right tool for each step?
- [ ] Does it stop when the goal is achieved (not over-execute)?
- [ ] Does it handle tool failures gracefully?
- [ ] Is the final output in the expected format?
```

## Step 4 — Multi-Agent System Design (if applicable)

```
ORCHESTRATOR AGENT
Role: Breaks down the goal, assigns subtasks, synthesizes results
Model: [Most capable — GPT-4o / Claude Opus]

SPECIALIST AGENT 1: [Name]
Role: [Specific expertise — e.g., Research, Writing, Code]
Tools: [Subset of tools relevant to this specialty]

SPECIALIST AGENT 2: [Name]
Role: [Different specialty]
Tools: [Different tool subset]

COMMUNICATION PATTERN:
Orchestrator → assigns task → Specialist → returns result → Orchestrator → synthesizes
```

## Step 5 — Popular Agent Patterns

**Research Agent**: Web search + summarize + cite sources → final report
**Coding Agent**: Understand requirement + write code + test + iterate → working code
**Data Agent**: Query DB + analyze + visualize + explain → insights report
**Customer Service Agent**: Understand query + check knowledge base + draft reply → response
**Scheduling Agent**: Check calendar + find availability + draft invite + send → confirmed meeting

Always offer: "Want me to write the full system prompt and tool definitions for this agent?"
