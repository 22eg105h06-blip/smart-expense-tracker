from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200


def test_add_expense():
    expense = {
        "amount": 500,
        "title": "Lunch",
        "category": "Food",
        "date": "2026-07-31"
    }

    response = client.post("/expenses", json=expense)

    assert response.status_code == 200


def test_filter_by_category():
    response = client.get("/expenses?category=Food")

    assert response.status_code == 200


def test_summary():
    response = client.get("/summary")

    assert response.status_code == 200