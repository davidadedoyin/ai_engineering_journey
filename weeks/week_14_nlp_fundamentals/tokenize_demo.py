import re

texts = [
    "I love this product and it works really well!",
    "This was a bad experience and I am disappointed.",
]

for text in texts:
    cleaned = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    print(cleaned.split())
