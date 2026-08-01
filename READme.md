# Smart Expense Tracker

A Smart Expense Tracker REST API built using Python and FastAPI. The project allows users to add, view, filter, update, and delete expenses, as well as calculate overall and category-wise spending.

## Features

- Add an expense
- View all expenses
- Filter expenses by category
- Update an expense
- Delete an expense by ID
- Calculate total expenses
- Calculate category-wise expense totals
- Interactive API documentation using Swagger UI
- Automated API testing using Pytest
- Simple frontend dashboard with category-wise spending chart

## Technologies Used

- Python
- FastAPI
- Pydantic
- Pytest
- HTTPX
- HTML
- CSS
- JavaScript
- Chart.js

## Expense Fields

Each expense contains:

- `id`
- `title`
- `amount`
- `category`
- `date`

## Project Structure

```text
smart-expense-tracker/
│
├── README.md
├── AI_NOTES.md
├── expenses.json
│
├── src/
│   ├── main.py
│   └── frontend/
│       └── index.html
│
├── tests/
│   └── test_expenses.py
│
└── venv/

## Installation

1. Clone the repository

```bash
git clone https://github.com/22eg105h06-blip/smart-expense-tracker.git
cd smart-expense-tracker

2. Create a virtual environment
python -m venv venv

3. Activate the virtual environment
For Windows PowerShell:
venv\Scripts\Activate.ps1
For Windows Command Prompt:
venv\Scripts\activate

4. Install dependencies
pip install fastapi uvicorn pytest httpx
Run the Application
Start the FastAPI server:
uvicorn src.main:app --reload
The server will run at:
http://127.0.0.1:8000
Swagger API Documentation
Open the following URL in your browser:
http://127.0.0.1:8000/docs
Swagger UI can be used to test the REST API endpoints.

API Endpoints
Method
Endpoint
Description
POST
/expenses
Add a new expense
GET
/expenses
Get all expenses
GET
/expenses?category=Food
Filter expenses by category
PUT
/expenses/{id}
Update an expense
DELETE
/expenses/{id}
Delete an expense
GET
/summary
Get total and category-wise expenses
Example Expense
{
    "amount": 500,
    "title": "Lunch",
    "category": "Food",
    "date": "2026-07-31"
}


Run Tests
Run the automated tests from the project root directory:
python -m pytest -v


Expected result:
4 passed
