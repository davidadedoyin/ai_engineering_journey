faq = [
    {
        "question": "How do I install Python?",
        "answer": "Download Python from python.org and run the installer. Ensure the executable is on your PATH.",
    },
    {
        "question": "How do I create a virtual environment?",
        "answer": "Run python -m venv .venv and activate it with .venv\\Scripts\\Activate.ps1 on Windows.",
    },
    {
        "question": "How do I deploy a FastAPI app?",
        "answer": "Use uvicorn app:app --host 127.0.0.1 --port 8000 or deploy it behind a server like Docker or a cloud service.",
    },
]


def rank_answers(query: str, limit: int = 2):
    lowered = query.lower()
    scored = []
    for item in faq:
        score = 0
        for word in lowered.split():
            if word in item["question"].lower():
                score += 2
            if word in item["answer"].lower():
                score += 1
        scored.append((score, item))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:limit]


for query in [
    "How do I create a virtual environment?",
    "How do I deploy my FastAPI app?",
    "How do I install Python?",
]:
    print("Query:", query)
    for score, item in rank_answers(query):
        print(score, item["question"], "->", item["answer"])
    print("---")
