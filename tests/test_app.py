import os
import pytest
from app import app, init_db, connect_db

@pytest.fixture()
def client(tmp_path, monkeypatch):
    db_path = tmp_path / "test.sqlite"
    monkeypatch.setattr("app.DATABASE", str(db_path))
    app.config.update(TESTING=True, SECRET_KEY="test-secret")
    init_db()
    with app.test_client() as client:
        yield client

def register(client, username="alice", password="password123"):
    return client.post("/register", data={"username": username, "password": password}, follow_redirects=True)

def login(client, username="alice", password="password123"):
    return client.post("/login", data={"username": username, "password": password}, follow_redirects=True)

def test_register_hashes_password(client):
    response = register(client)
    assert response.status_code == 200
    with connect_db() as db:
        row = db.execute("SELECT password_hash FROM users WHERE username='alice'").fetchone()
    assert row["password_hash"] != "password123"
    assert row["password_hash"].startswith("scrypt:")

def test_duplicate_username_is_rejected(client):
    register(client)
    response = register(client)
    assert b"already taken" in response.data

def test_login_and_logout(client):
    register(client)
    response = login(client)
    assert b"Hi, alice" in response.data
    response = client.post("/logout", follow_redirects=True)
    assert b"Log in" in response.data

def test_post_requires_authentication(client):
    response = client.post("/posts", data={"content": "hello"}, follow_redirects=True)
    assert b"Please sign in" in response.data

def test_post_is_saved_and_shown_in_feed(client):
    register(client)
    login(client)
    response = client.post("/posts", data={"content": "Hello, timeline!"}, follow_redirects=True)
    assert b"Hello, timeline!" in response.data
    assert b"alice" in response.data

def test_empty_and_oversized_posts_are_rejected(client):
    register(client)
    login(client)
    response = client.post("/posts", data={"content": " "}, follow_redirects=True)
    assert b"1" in response.data and b"280" in response.data
    response = client.post("/posts", data={"content": "x" * 281}, follow_redirects=True)
    assert b"1" in response.data and b"280" in response.data

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
