import pytest


pytestmark = pytest.mark.anyio


async def test_root_and_health_routes(client):
    root = await client.get("/")
    health = await client.get("/health")

    assert root.status_code == 200
    assert root.json() == {"message": "Instagram Clone API is running"}
    assert health.status_code == 200
    assert health.json() == {"status": "healthy"}
