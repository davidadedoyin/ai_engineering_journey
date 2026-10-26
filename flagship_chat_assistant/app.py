from fastapi import FastAPI

app = FastAPI(title="Flagship Chat Assistant")


@app.get("/health")
def health():
    return {"status": "ok"}
