# Week 19: Advanced RAG and evaluation

## Analogy

A retrieval system is useful only if it retrieves the right passages and the answer is checked for quality. A good RAG system needs both retrieval quality and answer quality.

## Mon: chunking and context windows

Documents are often split into smaller chunks so retrieval can find the right snippet quickly.

Examples of chunking strategies:
- fixed-size chunks
- semantic chunks
- heading-aware splits

A chunk should be small enough to be relevant, but large enough to contain context.

## Tue: relevance and ranking

Ranking answers is about matching the query to the most useful passage. We can measure quality with:
- hit rate
- precision@k
- answer relevance
- citation coverage

## Wed: answer evaluation

A final answer should be assessed on:
- correctness
- groundedness
- conciseness
- safety

Even a strong LLM can produce a confident but wrong answer if the retrieval is weak.

## Thu: RAG pipeline diagram

A simple pipeline looks like this:

1. user asks a question
2. query is encoded
3. relevant chunks are retrieved
4. prompt is built with those chunks
5. LLM answers using those sources
6. answer is checked for quality

## Friday challenge

Create a tiny FAQ dataset and score its retrieval quality using a simple hit-rate check.

## Saturday project

Upgrade the flagship assistant to use a more grounded local retrieval flow with a final answer generator.

## Did it stick? Repeat checklist

- I can explain why chunking matters in RAG.
- I can explain the difference between retrieval quality and answer quality.
- I can describe how a retrieval pipeline feeds context to an LLM.
- I can explain why evaluation matters before shipping a chatbot.
