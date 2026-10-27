# Week 22: Multi-agent systems and advanced tool use

## Analogy

A multi-agent workflow is like a small project team: each specialist has a defined job, and an orchestrator decides what to delegate and checks the combined result. Adding agents does not automatically make a system more capable; it adds coordination and failure modes too.

## Mon: agents, tools, and workflows

- A tool is a bounded function the system can call.
- An agent uses a model to choose actions toward a goal.
- A workflow is a sequence of explicit steps; it can use tools without being an autonomous agent.

Prefer a predictable workflow when the steps are known.

## Tue: define roles and contracts

Give each worker one responsibility and a clear input/output contract. Structured results are easier to validate than free-form messages.

```python
from typing import TypedDict

class Finding(TypedDict):
    summary: str
    evidence: list[str]
```

## Wed: orchestration patterns

Common patterns include:

- sequential: each step uses the previous step's result
- parallel: independent tasks run separately and are combined
- supervisor: a coordinator delegates and checks completion

Start with the least complex pattern that meets the task.

## Thu: reliability and safety boundaries

- Allowlist available tools; do not expose arbitrary code execution.
- Validate tool arguments and results.
- Set limits for steps, retries, time, and delegated work.
- Require human approval for consequential external actions.
- Record enough information to understand what happened.

## Friday challenge

Implement a supervisor that sends a task to two specialist functions, validates both structured results, and returns a combined report. Keep the workers deterministic; the point is to practice orchestration, not to call an LLM.

## Saturday project

Build a small multi-agent research assistant with two specialist roles and a reviewer. Use a fixed local set of facts, include the evidence in the final answer, and reject incomplete worker results.

## Did it stick? Repeat checklist

- I can distinguish an agent from a tool and a fixed workflow.
- I can explain when sequential, parallel, or supervisor orchestration fits.
- I can name limits that make tool-using systems safer and more reliable.
- I can explain why multiple agents can increase cost and failure risk.
