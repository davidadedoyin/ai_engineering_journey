"""A deterministic example of delegating work and validating agent results."""

from typing import TypedDict


class Finding(TypedDict):
    summary: str
    evidence: list[str]


def architecture_worker() -> Finding:
    return {
        "summary": "A retrieval service can keep its document index local.",
        "evidence": ["The prototype reads its knowledge files from disk."],
    }


def operations_worker() -> Finding:
    return {
        "summary": "A health endpoint helps detect whether the API is ready.",
        "evidence": ["The service exposes a /health route."],
    }


def validate_finding(role: str, finding: Finding) -> None:
    if not finding["summary"].strip():
        raise ValueError(f"{role} worker returned an empty summary")
    if not finding["evidence"] or any(not item.strip() for item in finding["evidence"]):
        raise ValueError(f"{role} worker must return non-empty evidence")


def supervise() -> dict[str, Finding]:
    findings = {
        "architecture": architecture_worker(),
        "operations": operations_worker(),
    }
    for role, finding in findings.items():
        validate_finding(role, finding)
    return findings


if __name__ == "__main__":
    for role, finding in supervise().items():
        print(f"{role}: {finding['summary']}")
        for evidence in finding["evidence"]:
            print(f"  evidence: {evidence}")
