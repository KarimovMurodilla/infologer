from fastapi import APIRouter

from api.dependencies import UOWDep, CurrentUser
from schemas.knows import KnowsSchemaAdd
from services.knows import KnowsService


router = APIRouter(
    prefix="/knows",
    tags=["Knows"],
)


@router.get("")
async def get_knows(
    uow: UOWDep,
    user: CurrentUser
):
    knows = await KnowsService().get_knows(uow, user.id)
    return knows


@router.post("")
async def add_know(
    know: KnowsSchemaAdd,
    uow: UOWDep,
    user: CurrentUser
):
    know_id = await KnowsService().add_know(uow, know, user.id)
    return {"know_id": know_id}