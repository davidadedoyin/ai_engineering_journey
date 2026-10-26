# Reference solution.
# Look only after you have tried.

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "hello"}

@app.get("/is_even")
def is_even(number: int):
    return {"number": number, "is_even": number % 2 == 0}
