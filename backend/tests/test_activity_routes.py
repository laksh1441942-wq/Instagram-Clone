import pytest

from backend.tests.conftest import get_token


pytestmark = pytest.mark.anyio


async def test_follow_unfollow_and_relationship_routes(client, user_factory):
    follower = user_factory("follower")
    following = user_factory("following")
    token = await get_token(client, follower.username)

    followed = await client.post(
        f"/activity/follow/{following.username}", params={"token": token}
    )
    followers = await client.get(
        "/activity/followers", params={"token": token}
    )
    following_list = await client.get(
        "/activity/following", params={"token": token}
    )
    unfollowed = await client.post(
        f"/activity/unfollow/{following.username}", params={"token": token}
    )

    assert followed.status_code == 204
    assert followers.status_code == 200
    assert followers.json()["followers"] == []
    assert following_list.status_code == 200
    assert following_list.json()["following"][0]["username"] == following.username
    assert unfollowed.status_code == 204


async def test_activity_route_lists_activity(client, user_factory):
    user = user_factory()

    response = await client.get(
        f"/activity/{user.username}", params={"page": 1, "limit": 10}
    )

    assert response.status_code == 200
    assert response.json() == []
