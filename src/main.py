import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from api.routers import all_routers


app = FastAPI(
    title="Todogram"
)


for router in all_routers:
    if isinstance(router, dict):
        app.include_router(**router)

    else:
        app.include_router(router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
