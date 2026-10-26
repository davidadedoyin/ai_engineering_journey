# Week 15: Retrieval and embeddings

## Analogy

A large language model is smart, but it still needs relevant context. Retrieval is like giving the model a textbook chapter before it answers a question.

## Mon: why retrieval matters

Without retrieval, a language model has to answer from memory alone. With retrieval, it can look up the most relevant documents before answering.

This is the idea behind RAG:
- retrieve relevant documents
- augment the prompt with them
- generate a grounded answer

## Tue: embedding basics

Embeddings are numeric vectors that represent the meaning of text. Similar texts tend to have nearby vectors.

```python
# Conceptual example, not a real pretrained model.
# Each piece of text is represented by a vector.
texts = [
    "Python is a programming language",
    "Python helps with data science",
    "Cats are common pets",
]
print(texts)
```

In real systems, we use models such as sentence-transformers or OpenAI embeddings to create this representation.

## Wed: document retrieval

The retrieval stage compares the query with stored documents and selects the best matches.

A simple implementation is keyword overlap:

```python
faq = [
    "How do I install Python?",
    "How do I set up a virtual environment?",
    "How do I deploy a FastAPI app?",
]
question = "How do I set up a virtual environment?"
print([doc for doc in faq if "virtual" in doc.lower()])
```

## Thu: retrieval quality

Good retrieval is about more than matching words. You also care about:
- relevance
- ranking quality
- handling synonyms
- not retrieving too many irrelevant chunks

## Friday challenge

Create a tiny FAQ dataset and rank the best matching answer for a user question.

## Saturday project

Build the `projects/month6_rag_faq_bot/` FAQ bot and test retrieval on sample questions.

## Did it stick? Repeat checklist

- I can explain why retrieval matters for LLMs.
- I can explain what an embedding is in plain English.
- I can describe why ranking documents by relevance matters.
- I can explain the difference between a normal model response and a retrieval-grounded response.
