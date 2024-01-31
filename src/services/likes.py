from sqlalchemy.exc import IntegrityError

from schemas.likes import LikesSchemaAdd
from utils.repository import AbstractRepository
from utils.unitofwork import IUnitOfWork


class LikesService:
    async def add_like(self, uow: IUnitOfWork, like: LikesSchemaAdd, user_id: int):
        likes_dict = like.model_dump()
        likes_dict['user_id'] = user_id

        try:
            async with uow:
                await uow.likes.add_one(likes_dict)
                await uow.commit()
            return "liked"
        except IntegrityError as e:
            res = await self.get_like(uow, user_id=user_id, know_id=like.know_id)
            if res:
                await self.delete_like(uow, user_id=user_id, know_id=like.know_id)
            return "duplicate entry, not inserted"

        # res = await self.get_like(uow, user_id=user_id, know_id=like.know_id)
        # print("---------------------------------------")
        # print("res: ", bool(res))
        # if res:
        #     print("deleted like")
        #     print("---------------------------------------")

        #     await self.delete_like(uow, user_id=user_id, know_id=like.know_id)
        #     return "unliked"
        # else:
        #     print("not deleted. added")
        #     print("---------------------------------------")
        #     async with uow:
        #         await uow.likes.add_one(likes_dict)
        #         await uow.commit()
        #         return "liked"

    async def get_count(self, uow: IUnitOfWork, know_id: str):
        async with uow:
            likes = await uow.likes.count(know_id=know_id)
            return likes

    async def get_user(self, uow: IUnitOfWork, know_id: str, user_id: int):
        async with uow:
            user = await uow.likes.find_one(know_id=know_id, user_id=user_id)
            return user
        
    async def get_like(self, uow: IUnitOfWork, **filters: dict):
        async with uow:
            like = await uow.likes.find_one(**filters)
            return like
        
    async def delete_like(self, uow: IUnitOfWork, **filters: dict):
        async with uow:
            like_id = await uow.likes.delete_one(**filters)
            await uow.commit()
            return like_id