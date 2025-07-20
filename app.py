from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Request schemas using Pydantic
class NumbersInput(BaseModel):
    a: float
    b: float


class StringsInput(BaseModel):
    s1: str
    s2: str


class RemoveSubstringInput(BaseModel):
    s: str
    substr: str


@app.post("/add_numbers")
def add_numbers(data: NumbersInput):
    result = data.a + data.b
    return {"result": result}


@app.post("/subtract_numbers")
def subtract_numbers(data: NumbersInput):
    result = data.a - data.b
    return {"result": result}


@app.post("/concat_strings")
def concat_strings(data: StringsInput):
    result = data.s1 + data.s2
    return {"result": result}


@app.post("/remove_substring")
def remove_substring(data: RemoveSubstringInput):
    if not data.substr:
        raise HTTPException(
            status_code=400, detail="Substring to remove cannot be empty.")
    result = data.s.replace(data.substr, "")
    return {"result": result}
