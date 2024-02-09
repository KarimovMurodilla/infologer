from fastapi import APIRouter

from api.dependencies import UOWDep, CurrentUser
from schemas.tasks import TaskSchemaAdd, TaskSchemaEdit
from services.tasks import TasksService
from services.users import UsersService


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.get("")
async def get_tasks(
    uow: UOWDep,
    user: CurrentUser,
    page: int
):
    tasks = await TasksService().get_tasks(uow, user.id, offset=page)
    return tasks

@router.post("")
async def add_task(
    task: TaskSchemaAdd,
    uow: UOWDep,
    user: CurrentUser
):
    task_id = await TasksService().add_task(uow, task, user.id)
    return {"task_id": task_id}


@router.patch("/{id}")
async def edit_task(
    id: str,
    task: TaskSchemaEdit,
    uow: UOWDep,
    user: CurrentUser
):
    await TasksService().edit_task(uow, id, user.id, task)
    return {"ok": True}


@router.get("/{user_id}")
async def get_tasks_by_user_id(
    user_id: int,
    uow: UOWDep,
    page: int
):

    user = await UsersService().get_user_by_id(uow, id=user_id)
    
    if user.is_tasks_private:
        return {"detail": "private"}
    
    tasks = await TasksService().get_tasks(uow, user_id, offset=page)
    return tasks


@router.delete("/{id}")
async def delete_task(
    id: str,
    uow: UOWDep,
    user: CurrentUser
):
    res = await TasksService().delete_task(uow, id, user.id)
    return {"task_id": res}