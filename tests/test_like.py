from httpx import AsyncClient
from redis import Redis


async def test_add_likes(ac: AsyncClient, redis_client: Redis):
    cookie_value = await redis_client.get("bonds")

    response = await ac.post("/likes", json={
        "know_id": 1
        },
        cookies={
            "bonds": cookie_value
        }
    )

    assert response.status_code == 200


async def test_get_likes(ac: AsyncClient):
    response = await ac.get("/likes/1")

    assert response.status_code == 200
