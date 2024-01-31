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
    know_id: str,
    uow: UOWDep,
    current_user: CurrentUser
):
    count = await LikesService().get_count(uow, know_id=know_id)
    user = await LikesService().get_user(uow, know_id=know_id, user_id=current_user.id)

    return {"count": count, "status": bool(user)}


@router.post("")
async def add_like(
    like: LikesSchemaAdd,
    uow: UOWDep,
    user: CurrentUser
):
    like_id = await LikesService().add_like(uow, like, user.id)
    return {"like_id": like_id}