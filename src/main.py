import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from api.routers import all_routers
from config import FRONTEND_BASE_URL


app = FastAPI(
    title="Todogram",
    docs_url = "/anonymous_url_for_basic_docs_9723",
    redoc_url = "/anonymous_url_for_basic_redoc_9723",
    swagger_ui_oauth2_redirect_url = "/anonymous_url_for_basic_docs_9723/oauth2-redirect",
)


for router in all_routers:
    if isinstance(router, dict):
        app.include_router(**router)

    else:
        app.include_router(router)

origins = [
    # FRONTEND_BASE_URL,
    "http://localhost:3000"
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
#     allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
#                    "Authorization"],
# )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to allow requests from specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
