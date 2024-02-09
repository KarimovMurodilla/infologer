from schemas.knows import KnowSchemaEdit, KnowsSchemaAdd
from utils.unitofwork import IUnitOfWork


class KnowsService:
    async def add_know(self, uow: IUnitOfWork, know: KnowsSchemaAdd, user):
        knows_dict = know.model_dump()
        knows_dict['user_id'] = user.id
        
        async with uow:
            know_id = await uow.knows.add_one(knows_dict)
            await uow.commit()
            return know_id

    async def get_knows(self, uow: IUnitOfWork, user_id: int, offset: int):
        async with uow:
            knows = await uow.knows.find_all_by(offset=offset, user_id=user_id)
            return knows
        
    async def get_all_knows(self, uow: IUnitOfWork, offset: int):
        async with uow:
            knows = await uow.knows.find_all_by(offset=offset)
            return knows
        
    async def edit_know(self, uow: IUnitOfWork, know_id: str, user_id: int, know: KnowSchemaEdit):
        knows_dict = know.model_dump()
        
        [knows_dict.pop(i) for i in [k for k in knows_dict.keys() if knows_dict[k] is None]]

        async with uow:
            await uow.knows.edit_one(data=knows_dict, id=know_id, user_id=user_id)

            await uow.commit()

    async def delete_know(self, uow: IUnitOfWork, know_id: str, user_id: int):
        async with uow:
            know_id = await uow.knows.delete_one(id=know_id, user_id=user_id)
            await uow.commit()
            return know_id