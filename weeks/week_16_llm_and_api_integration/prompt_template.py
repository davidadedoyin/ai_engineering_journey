SYSTEM_PROMPT = """
You are a helpful AI teaching assistant.
Explain concepts clearly and keep everything beginner-friendly.
"""

USER_PROMPT = "What is a model evaluation metric?"

payload = {
    "system": SYSTEM_PROMPT,
    "user": USER_PROMPT,
}

print(payload)
