from fastapi.testclient import TestClient
from main import app
import re


def test_read_root_returns_hello_world():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200


def test_openapi_spec_formatted_with_markdown():
    client = TestClient(app)
    response = client.post(
        "/generate_openapi",
        json={
            "user_instruction": "give me a spec to register a shop with shop id and shop name"
        },
    )
    assert response.status_code == 200
    assert re.search(r"```", response.text)


def test_openapi_spec_is_valid():
    client = TestClient(app)
    response = client.post(
        "/generate_openapi",
        json={
            "user_instruction": "give me a spec to register a shop with shop id and shop name"
        },
    )
    assert response.status_code == 200
    assert re.search(r"openapi", response.text)
