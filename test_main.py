from fastapi.testclient import TestClient
from main import app 


def test_read_root_returns_hello_world(): 
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200