from fastapi import APIRouter

from api.tasks import UOWDep, CurrentUser
from services.users import UsersService



router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("")
async def get_users(
    uow: UOWDep
):
    users = await UsersService().get_users(uow)
    return users


@router.get("/filter")
async def get_user_by_username(
    uow: UOWDep,
    username: str
):
    users = await UsersService().get_user_like_username(uow, username)
    return users


@router.get("/me")
async def read_users_me(current_user: CurrentUser):
    return current_user