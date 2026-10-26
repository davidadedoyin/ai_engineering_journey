faq = [
    ("python installation", "Download Python and add it to PATH."),
    ("virtual environment", "Use python -m venv .venv and activate it."),
    ("fastapi deployment", "Run uvicorn app:app --host 127.0.0.1 --port 8000."),
]

queries = [
    "How do I create a virtual environment?",
    "How do I deploy a FastAPI app?",
    "How do I install Python?",
]

# Simple keyword-based hit-rate evaluation.
for query in queries:
    hits = []
    q = query.lower()
    for topic, answer in faq:
        if any(word in q for word in topic.split()):
            hits.append(topic)
    print(query, "->", hits)

print("Example evaluation summary: retrieval hit rate is high when the query matches the indexed FAQ topic.")
