from fastapi import APIRouter

from api.dependencies import UOWDep, CurrentUser
from schemas.knows import KnowsSchemaAdd
from services.knows import KnowsService
from services.users import UsersService


router = APIRouter(
    prefix="/knows",
    tags=["Knows"],
)


@router.get("")
async def get_knows(
    uow: UOWDep,
    user: CurrentUser,
    page: int
):
    knows = await KnowsService().get_knows(uow, user.id, offset=page)
    return knows

@router.post("")
async def add_know(
    know: KnowsSchemaAdd,
    uow: UOWDep,
    user: CurrentUser
):
    know_id = await KnowsService().add_know(uow, know, user)
    return {"know_id": know_id}


@router.get("/all")
async def get_knows(
    uow: UOWDep,
    page: int
):
    knows = await KnowsService().get_all_knows(uow, offset=page)
    return knows


@router.get("/{user_id}")
async def get_knows_by_user_id(
    user_id: int,
    uow: UOWDep,
    page: int
):
    user = await UsersService().get_user_by_id(uow, id=user_id)
    
    if user.is_knows_private:
        return {"detail": "private"}
    
    knows = await KnowsService().get_knows(uow, user_id, offset=page)
    return knows