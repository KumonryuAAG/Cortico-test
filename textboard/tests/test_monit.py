from app import app

def test_monitor_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert "status" in r.get_json()

def test_metrics_keys():
    client = app.test_client()
    r = client.get("/metrics")
    j = r.get_json()
    for key in ("cpu_percent", "memory_percent", "disk_usage_percent"):
        assert key in j
