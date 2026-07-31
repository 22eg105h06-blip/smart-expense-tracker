from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from pathlib import Path
import json

app = FastAPI(title="Smart Expense Tracker API")

DATA_FILE = Path(__file__).resolve().parent.parent / "expenses.json"


from pydantic import BaseModel, Field


class Expense(BaseModel):
    amount: float = Field(gt=0)
    category: str = Field(min_length=1)
    title: str = Field(min_length=1)
    date: str = Field(min_length=1)


def load_expenses():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

@app.get("/dashboard")
def dashboard():
    frontend_file = Path(__file__).resolve().parent / "frontend" / "index.html"
    return FileResponse(frontend_file)

@app.get("/")
def home():
    return {"message": "Welcome to Smart Expense Tracker API"}


@app.get("/expenses")
def get_expenses(category: str | None = None):
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return expenses
@app.get("/summary")
def get_summary():
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    by_category = {}

    for expense in expenses:
        category = expense["category"]

        if category not in by_category:
            by_category[category] = 0

        by_category[category] += expense["amount"]

    return {
        "total": total,
        "by_category": by_category
    }

@app.post("/expenses")
def add_expense(expense: Expense):
    expenses = load_expenses()

    new_expense = {
        "id": len(expenses) + 1,
        "amount": expense.amount,
        "category": expense.category,
        "title": expense.title,
        "date": expense.date
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    return {
        "message": "Expense added successfully",
        "expense": new_expense
    }


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)

            return {
                "message": "Expense deleted successfully",
                "deleted_expense": expense
            }

            
@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, updated_expense: Expense):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expense["amount"] = updated_expense.amount
            expense["category"] = updated_expense.category
            expense["title"] = updated_expense.title
            expense["date"] = updated_expense.date

            save_expenses(expenses)

            return {
                "message": "Expense updated successfully",
                "expense": expense
            }

    raise HTTPException(status_code=404, detail="Expense not found")
    raise HTTPException(status_code=404, detail="Expense not found")