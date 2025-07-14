from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_post_workflow():
    response = client.post("/workflows?nome=test-workflow")
    assert response.status_code == 200
    assert "registrado com sucesso" in response.json()["message"]

def test_get_workflows():
    client.post("/workflows?nome=workflow1")
    response = client.get("/workflows")
    assert response.status_code == 200
    assert "workflow1" in response.json()
