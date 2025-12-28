from fastapi import FastAPI,Form
from backend.llm_part import extract_expense

app = FastAPI()

@app.get("/")
def root():
    return{"message": "Backend is running"}

@app.post("/parse-expense")
def parse_expense(text: str = Form(...)):
    result = extract_expense(text)
    return result
