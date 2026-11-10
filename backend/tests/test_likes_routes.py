import pytest


pytestmark = pytest.mark.anyio


async def test_like_unlike_and_list_likers(client, user_factory, post_factory):
    author = user_factory("author")
    liker = user_factory("liker")
    post = post_factory(author.id)

    liked = await client.post(
        "/likes/like", params={"post_id": post.id, "username": liker.username}
    )
    likers = await client.get(f"/likes/likes/{post.id}")
    unliked = await client.post(
        "/likes/unlike", params={"post_id": post.id, "username": liker.username}
    )

    assert liked.status_code == 200
    assert liked.json()["likes_count"] == 1
    assert likers.status_code == 200
    assert likers.json()[0]["username"] == liker.username
    assert unliked.status_code == 200
    assert unliked.json()["likes_count"] == 0


async def test_like_routes_validate_post_and_user(client, user_factory, post_factory):
    author = user_factory("author")
    post = post_factory(author.id)

    missing_post = await client.post(
        "/likes/like", params={"post_id": 999, "username": "author"}
    )
    missing_user = await client.post(
        "/likes/like", params={"post_id": post.id, "username": "missing"}
    )

    assert missing_post.status_code == 404
    assert missing_user.status_code == 404
