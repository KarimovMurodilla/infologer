from fastapi import APIRouter

from api.dependencies import UOWDep, CurrentUser
from schemas.likes import LikesSchemaAdd
from services.likes import LikesService


router = APIRouter(
    prefix="/likes",
    tags=["Likes"],
)


@router.get("/{know_id}")
async def get_likes(
    know_id: int,
    uow: UOWDep,
):
    likes = await LikesService().get_likes(uow, know_id=know_id)
    return likes


@router.post("")
async def add_like(
    like: LikesSchemaAdd,
    uow: UOWDep,
    user: CurrentUser
):
    like_id = await LikesService().add_like(uow, like, user.id)
    return {"like_id": like_id}