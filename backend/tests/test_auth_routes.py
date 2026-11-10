import pytest

from backend.app.models import RPModel


pytestmark = pytest.mark.anyio


def signup_payload(username: str = "alice", email: str = "alice@example.com"):
    return {
        "username": username,
        "email": email,
        "password": "password123",
        "name": "Alice",
        "bio": "Hello",
        "location": "Test City",
    }


async def test_signup_returns_bearer_token(client):
    response = await client.post("/auth/signup", json=signup_payload())

    assert response.status_code == 201
    assert response.json()["token type"] == "bearer"
    assert response.json()["username"] == "alice"
    assert response.json()["access token"]


async def test_signup_rejects_duplicate_username_or_email(client):
    await client.post("/auth/signup", json=signup_payload())

    duplicate = await client.post(
        "/auth/signup", json=signup_payload(email="different@example.com")
    )

    assert duplicate.status_code == 409


async def test_login_accepts_form_credentials(client):
    await client.post("/auth/signup", json=signup_payload())

    response = await client.post(
        "/auth/token",
        data={"username": "alice", "password": "password123"},
    )

    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]


async def test_login_rejects_invalid_credentials(client):
    response = await client.post(
        "/auth/token",
        data={"username": "missing", "password": "wrong-password"},
    )

    assert response.status_code == 401


async def test_password_reset_flow(client, db_session):
    await client.post("/auth/signup", json=signup_payload())

    sent = await client.post("/auth/sendcode", params={"email": "alice@example.com"})
    code = db_session.query(RPModel).filter_by(email="alice@example.com").one().code
    verified = await client.post(
        "/auth/verifycode",
        params={"email": "alice@example.com", "code": code},
    )
    reset = await client.post(
        "/auth/reset",
        params={"email": "alice@example.com", "password": "new-password123"},
    )

    assert sent.status_code == 200
    assert verified.json() is True
    assert reset.status_code == 204
    assert (
        await client.post(
            "/auth/token",
            data={"username": "alice", "password": "new-password123"},
        )
    ).status_code == 200
