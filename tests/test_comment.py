from httpx import AsyncClient
from redis import Redis

from conftest import client


async def test_add_comment(ac: AsyncClient, redis_client: Redis):
    cookie_value = await redis_client.get("bonds")

    response = await ac.post("/comments", json={
        "text": "test comment",
        "know_id": 1
    },
        cookies={
            "bonds": cookie_value
        }
    )

    assert response.status_code == 200


async def test_get_comments(ac: AsyncClient):
    response = await ac.get("/comments/1", cookies=client.cookies)

    assert response.status_code == 200
