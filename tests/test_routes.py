import pytest


def test_read_item(client):
    response = client.get("/items/1")
    assert response.status_code == 200
    json_response = response.json()
    assert "id" in json_response
    assert "item_name" in json_response
    assert json_response["id"] == 1

def test_read_items(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)