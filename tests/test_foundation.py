from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_health_contract():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert "runtime" in data or "error" in data


def test_path_traversal_is_rejected():
    response = client.post(
        "/api/files/write",
        json={"project": "default", "filename": "../escape.py", "code": "print(1)"},
    )
    assert response.status_code == 400


def test_invalid_python_fails_build_when_runtime_is_available():
    response = client.post(
        "/api/build",
        json={"project": "test", "filename": "bad.py", "code": "this is not valid python !!!"},
    )
    if response.status_code == 503:
        return
    assert response.status_code == 200
    assert response.json()["success"] is False
