from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="Deployment Ready Service")

REQUEST_COUNT = 0


@app.get("/")
def root():
    return {"message": "deployment-ready-service"}


@app.get("/health")
def health():
    return {"status": "ok", "service": "deployment-ready-service"}


@app.get("/metrics")
def metrics():
    global REQUEST_COUNT
    REQUEST_COUNT += 1
    return {
        "service": "deployment-ready-service",
        "request_count": REQUEST_COUNT,
        "uptime_seconds": 3600,
    }
