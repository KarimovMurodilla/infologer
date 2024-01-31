from schemas.tasks import TaskSchemaAdd, TaskSchemaEdit
from utils.repository import AbstractRepository
from utils.unitofwork import IUnitOfWork


class TasksService:
    async def add_task(self, uow: IUnitOfWork, task: TaskSchemaAdd, user_id):
        tasks_dict = task.model_dump()
        tasks_dict['user_id'] = user_id
        
        async with uow:
            task_id = await uow.tasks.add_one(tasks_dict)
            await uow.commit()
            return task_id

    async def get_tasks(self, uow: IUnitOfWork, user_id: int, offset: int):
        async with uow:
            tasks = await uow.tasks.find_all_by(offset=offset, user_id=user_id)
            return tasks

    async def edit_task(self, uow: IUnitOfWork, task_id: int, user_id: int, task: TaskSchemaEdit):
        tasks_dict = task.model_dump()
        
        [tasks_dict.pop(i) for i in [k for k in tasks_dict.keys() if tasks_dict[k] is None]]

        async with uow:
            await uow.tasks.edit_one(data=tasks_dict, id=task_id, user_id=user_id)

            await uow.commit()