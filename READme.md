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