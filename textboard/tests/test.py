from app import app, get_db, init_db

def test_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json.get("status") == "ok"

def test_post_and_list():
    init_db()
    client = app.test_client()
    # post a message
    r = client.post("/", data={"message": "hello world"}, follow_redirects=True)
    assert r.status_code == 200
    # page should contain the message
    assert b"hello world" in r.data
