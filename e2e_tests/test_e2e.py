import requests


def test_e2e():
    response = requests.get("http://localhost:5000")
    response_body = response.json()
    assert response_body["a"] == 2
    assert response_body["b"] == 3
