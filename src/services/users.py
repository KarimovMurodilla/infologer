from schemas.users import UserSchemaAdd
from utils.unitofwork import IUnitOfWork


class UsersService:
    async def add_user(self, uow: IUnitOfWork, user: UserSchemaAdd):
        user_dict = user.model_dump()
        async with uow:
            user_id = await uow.users.add_one(user_dict)
            await uow.commit()
            return user_id

    async def get_users(self, uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users

    async def get_user_by_email(self, uow: IUnitOfWork, email: str):
        async with uow:
            user = await uow.users.find_one(email=email)
            return user

    async def get_user_by_username(self, uow: IUnitOfWork, username: str):
        async with uow:
            user = await uow.users.find_one(username=username)
            return user
        
    async def get_users_by_username(self, uow: IUnitOfWork, value: str):
        async with uow:
            users = await uow.users.find_like(value)
            return users
