from fastapi import APIRouter

from api.dependencies import UOWDep, CurrentUser
from schemas.feedback import FeedbackSchemaAdd
from services.feedback import FeedbackService


router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"],
)


@router.get("/{know_id}")
async def get_feedback(
    know_id: str,
    uow: UOWDep,
    current_user: CurrentUser
):
    feedback = await FeedbackService().get_feedback(uow, know_id=know_id)

    if not feedback:
        print("generated NEW")
        feedback = await FeedbackService().generate_feedback(uow, know_id)
    else:
        print("didn't generated")
    return {"feedback": feedback}