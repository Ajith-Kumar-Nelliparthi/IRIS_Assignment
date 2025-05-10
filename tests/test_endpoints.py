import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_list_tables():
    response = client.get("/list_tables")
    assert response.status_code == 200
    assert "tables" in response.json()

def test_get_table_details():
    response = client.get("/get_table_details?table_name=INITIAL INVESTMENT")
    assert response.status_code == 200
    assert "table_name" in response.json()
    assert "row_names" in response.json()

def test_get_table_details_invalid_table():
    response = client.get("/get_table_details?table_name=NonExistent")
    assert response.status_code == 404

def test_row_sum():
    response = client.get("/row_sum?table_name=INITIAL INVESTMENT&row_name=Tax Credit (if any )=")
    assert response.status_code == 200
    assert "sum" in response.json()

def test_row_sum_invalid_row():
    response = client.get("/row_sum?table_name=INITIAL INVESTMENT&row_name=Invalid Row")
    assert response.status_code == 404