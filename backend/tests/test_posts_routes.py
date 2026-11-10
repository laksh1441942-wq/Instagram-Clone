import pytest


pytestmark = pytest.mark.anyio


def post_payload(content: str = "A post with #testing"):
    return {
        "title": "Test post",
        "content": content,
        "image": "",
        "location": "",
    }


async def test_create_and_read_post_routes(client, user_factory):
    user = user_factory()
    created = await client.post(
        f"/posts/?author_id={user.id}", json=post_payload()
    )
    post_id = created.json()["id"]

    by_id = await client.get(f"/posts/{post_id}")
    by_author = await client.get(f"/posts/{user.id}/posts")
    by_hashtag = await client.get("/posts/hashtags/testing")

    assert created.status_code == 200
    assert created.json()["content"] == "A post with #testing"
    assert by_id.status_code == 200
    assert len(by_author.json()) == 1
    assert by_hashtag.status_code == 200
    assert by_hashtag.json()[0]["id"] == post_id


async def test_post_routes_return_not_found_for_missing_records(client):
    assert (await client.get("/posts/999")).status_code == 404
    assert (await client.get("/posts/999/posts")).status_code == 404
    assert (await client.delete("/posts/999")).status_code == 404


async def test_delete_post_route(client, user_factory):
    user = user_factory()
    created = await client.post(
        f"/posts/?author_id={user.id}", json=post_payload()
    )

    response = await client.delete(f"/posts/{created.json()['id']}")

    assert response.status_code == 204
    assert (await client.get(f"/posts/{created.json()['id']}")).status_code == 404
