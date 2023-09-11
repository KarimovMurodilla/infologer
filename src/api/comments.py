from fastapi import APIRouter

from api.dependencies import UOWDep, CurrentUser
from schemas.comments import CommentsSchemaAdd
from services.comments import CommentsService


router = APIRouter(
    prefix="/comments",
    tags=["Comments"],
)


@router.get("/{know_id}")
async def get_comments(
    know_id: int,
    uow: UOWDep
):
    comments = await CommentsService().get_comments(uow, know_id)
    return comments


@router.post("")
async def add_comment(
    comment: CommentsSchemaAdd,
    uow: UOWDep,
    user: CurrentUser
):
    comment_id = await CommentsService().add_comment(uow, comment, user.id)
    return {"comment_id": comment_id}