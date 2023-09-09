from fastapi import APIRouter

from api.dependencies import UOWDep, CurrentUser
from schemas.tasks import TaskSchemaAdd
from services.tasks import TasksService


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.get("")
async def get_tasks(
    uow: UOWDep,
    user: CurrentUser
):
    tasks = await TasksService().get_tasks(uow, user.id)
    return tasks


@router.post("")
async def add_task(
    task: TaskSchemaAdd,
    uow: UOWDep,
    user: CurrentUser
):
    task_id = await TasksService().add_task(uow, task, user.id)
    return {"task_id": task_id}


# @router.patch("/{id}")
# async def edit_task(
#     id: int,
#     task: TaskSchemaEdit,
#     uow: UOWDep,
# ):
#     await TasksService().edit_task(uow, id, task)
#     return {"ok": True}
