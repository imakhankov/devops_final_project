from app import app

def test_health():
    client = app.test_client()
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"

def test_hello():
    client = app.test_client()
    response = client.get('/api/hello')
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello from Backend!"
