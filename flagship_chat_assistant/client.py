import json
import sys
import urllib.request


def send_chat(message: str, base_url: str = "http://127.0.0.1:8000") -> str:
    payload = json.dumps({"message": message}).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url}/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
        return data["answer"]


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "What is the roadmap about?"
    print(send_chat(question))
