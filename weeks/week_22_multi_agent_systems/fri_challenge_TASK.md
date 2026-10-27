# Friday challenge: orchestrate two specialists

## Goal

Write a small supervisor function that delegates one question to two deterministic specialist functions and combines their results.

## Requirements

1. Give each specialist a distinct responsibility.
2. Make each return a structured result with a summary and evidence.
3. Validate that both results contain non-empty summaries and evidence.
4. Return a combined report that keeps the evidence attached to each specialist.
5. Demonstrate a missing or invalid result and show that it is rejected explicitly.

## Done when

- The example runs without network access or an API key.
- The result identifies both specialists and includes their evidence.
- Invalid worker output raises a clear error rather than producing a success-shaped report.

## Stretch

Add a maximum worker count or a review step that checks whether the report answers the original question.
