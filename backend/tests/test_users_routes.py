import pytest

from backend.tests.conftest import get_token


pytestmark = pytest.mark.anyio


async def test_get_all_users_and_user_by_id(client, user_factory):
    user = user_factory()

    users = await client.get("/users/users")
    detail = await client.get(f"/users/{user.id}")

    assert users.status_code == 200
    assert users.json()[0]["username"] == "alice"
    assert detail.status_code == 200
    assert detail.json()["email"] == "alice@example.com"


async def test_profile_requires_a_valid_token(client, user_factory):
    user_factory()
    invalid = await client.post("/users/profile", params={"token": "invalid"})

    assert invalid.status_code == 401


async def test_profile_and_update_use_token(client, user_factory):
    user = user_factory()
    token = await get_token(client, user.username)

    profile = await client.post("/users/profile", params={"token": token})
    update = await client.put(
        f"/users/{user.username}",
        params={"token": token},
        json={"name": "Updated Alice"},
    )

    assert profile.status_code == 200
    assert profile.json()["username"] == user.username
    assert update.status_code == 204
    assert (await client.get(f"/users/{user.id}")).json()["name"] == "Updated Alice"


async def test_delete_user(client, user_factory):
    user = user_factory()

    response = await client.delete(f"/users/{user.id}")

    assert response.status_code == 200
    assert response.json()["id"] == user.id
    assert (await client.get(f"/users/{user.id}")).status_code == 404
