import pytest

from httpx import AsyncClient
from redis import Redis


async def test_get_know(ac: AsyncClient, redis_client: Redis):
    cookie_value = await redis_client.get("bonds")

    response = await ac.get(
        "/knows",
        cookies={
            "bonds": cookie_value
        }
    )

    assert response.status_code == 200