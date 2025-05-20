import requests
import pytest

BASE_URL = "https://httpbin.org"  # простой сервис для демонстрации

@pytest.mark.api
def test_get_status_code():
    response = requests.get(f"{BASE_URL}/get")
    assert response.status_code == 200

@pytest.mark.parametrize("param,expected", [
    ("hello", "hello"),
    ("test123", "test123"),
])
@pytest.mark.api
def test_get_with_params(param, expected):
    response = requests.get(f"{BASE_URL}/get", params={"q": param})
    assert response.status_code == 200
    assert response.json()["args"]["q"] == expected

@pytest.mark.api
def test_post_request():
    payload = {"username": "test", "password": "1234"}
    response = requests.post(f"{BASE_URL}/post", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["json"]["username"] == "test"
    assert json_data["json"]["password"] == "1234"