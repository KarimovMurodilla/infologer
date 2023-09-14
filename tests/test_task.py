from httpx import AsyncClient
from redis import Redis


async def test_add_task(ac: AsyncClient, redis_client: Redis):
    cookie_value = await redis_client.get("bonds")
    response = await ac.post("/tasks", json={
            "title": "string",
            "description": "string"
        },

        cookies={
            "bonds": cookie_value
        }
    )

    assert response.status_code == 200


async def test_get_tasks(ac: AsyncClient, redis_client: Redis):
    cookie_value = await redis_client.get("bonds")

    response = await ac.get("/tasks", cookies={"bonds": cookie_value})

    assert response.status_code == 200
