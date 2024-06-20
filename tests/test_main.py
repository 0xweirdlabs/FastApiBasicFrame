import pytest


def test_metrics(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "request_count" in response.text


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
