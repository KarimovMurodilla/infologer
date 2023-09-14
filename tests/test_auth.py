from httpx import AsyncClient
from redis import Redis

from db.models.users import User
from conftest import client


def test_register():
    response = client.post("/auth/register", json={
        "email": "73hdddhhs",
        "password": "1234",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "name": "wefwf",
        "username": "wefwf",
        "about": "wefwf"
    })

    assert response.status_code == 201


async def test_login(redis_client: Redis):
    response = client.post("/auth/jwt/login", data={
        "grant_type": "",
        "username": "73hdddhhs",
        "password": "1234",
        "scope": "",
        "client_id": "",
        "client_secret": "",
    })

    await redis_client.set("bonds", response.cookies.get("bonds"))

    assert response.status_code == 204


async def test_add_know(ac: AsyncClient, redis_client: Redis):
    cookie_value = await redis_client.get("bonds")

    response = await ac.post("/knows", 
        json={
            "title": "test title",
            "description": "test description"
        },

        cookies={
            "bonds": cookie_value
        }
    )

    assert response.status_code == 200