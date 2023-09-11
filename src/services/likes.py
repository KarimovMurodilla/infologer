from schemas.likes import LikesSchemaAdd
from utils.repository import AbstractRepository
from utils.unitofwork import IUnitOfWork


class LikesService:
    async def add_like(self, uow: IUnitOfWork, like: LikesSchemaAdd, user_id: int):
        likes_dict = like.model_dump()
        likes_dict['user_id'] = user_id

        if await self.get_like(uow, user_id=user_id):
            like_id = await self.delete_like(uow, user_id=user_id)
            return like_id
        
        async with uow:
            like_id = await uow.likes.add_one(likes_dict)
            await uow.commit()
            return like_id

    async def get_likes(self, uow: IUnitOfWork, **filters: dict):
        async with uow:
            likes = await uow.likes.find_all_by(**filters)
            return likes
        
    async def get_like(self, uow: IUnitOfWork, **filters: dict):
        async with uow:
            like = await uow.likes.find_one(**filters)
            return like
        
    async def delete_like(self, uow: IUnitOfWork, **filters: dict):
        async with uow:
            like_id = await uow.likes.delete_one(**filters)
            await uow.commit()
            return like_id