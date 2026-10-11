def test_health(client):
    assert client.get("/health").json()["status"] == "ok"

def test_add_event(client):
    r = client.post("/api/events", json={
        "date": "2026-10-01", "active_users": 1000, "new_users": 50,
        "churned_users": 10, "mrr": 100000,
        "new_mrr": 5000, "churn_mrr": -1000})
    assert r.status_code == 201

def test_kpi_endpoint(client):
    r = client.get("/api/metrics/kpi")
    assert r.status_code == 200
    assert "dau" in r.json()
