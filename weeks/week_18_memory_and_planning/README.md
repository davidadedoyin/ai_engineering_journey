# Week 18: Memory and planning

## Analogy

A good AI system is not only reactive; it also remembers the important context and decides what to do next.

## Mon: memory in software

Memory is how a system keeps state across steps. In app development, state might be:
- user preferences
- conversation history
- previous tool results
- retrieved documents

Without memory, every request feels like a fresh conversation.

## Tue: short-term memory

Short-term memory is what the model sees in the current conversation. It might be the recent chat history or the latest tool results.

```python
conversation = [
    {"role": "user", "content": "I want to learn RAG."},
    {"role": "assistant", "content": "Start with retrieval, then generation."},
]
print(conversation)
```

## Wed: long-term memory

Long-term memory might be stored in a database, a file, or a vector store. It lets an app remember user preferences or important facts over time.

## Thu: planning with tools

A planning system can break a task into smaller steps such as:
- identify the user goal
- gather facts
- choose a tool or model call
- synthesize the final answer

That is more robust than trying to do everything in one step.

## Friday challenge

Design a mini planning workflow for a user who asks, "I need to learn AI engineering and build a portfolio." Create 3 steps and 2 supporting tools.

## Saturday project

Build a lightweight planning assistant in `projects/month9_memory_planner/`.

## Did it stick? Repeat checklist

- I can explain what memory means in software.
- I can contrast short-term vs long-term memory.
- I can explain why planning helps multi-step tasks.
- I can describe how tool use and state work together in an agent.
