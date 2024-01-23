from abc import ABC, abstractmethod

from sqlalchemy import delete, insert, select, update, text
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.users import User

class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.unique().scalar_one()

    async def edit_one(self, data: dict, **filters) -> int:
        stmt = update(self.model).values(**data).filter_by(**filters).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.unique().scalar_one()
    
    async def find_all(self):
        if self.model.__name__ == "Know":
            stmt = (
                select(self.model)
                    .options(joinedload(self.model.user))  # Load the associated user data
            )

        else:
            stmt = select(self.model)
            
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.unique().all()]
        
        return res
    
    async def find_all_by(self, **filters: dict):
        if self.model.__name__ == "Know":
            stmt = (
                select(self.model)
                    .options(joinedload(self.model.user))
                    .filter_by(**filters) 
            )
        else:
            stmt = select(self.model).filter_by(**filters)

        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.unique().all()]
        return res
    
    async def find_one(self, **filters: dict):
        stmt = select(self.model).filter_by(**filters)
        res = await self.session.execute(stmt)
        res = res.unique().scalar_one_or_none()
    
        if res:
            res = res.to_read_model()
            
        return res

    async def find_like(self, value: str):
        stmt = select(self.model).where(text(f"username LIKE '%{value}%' OR first_name LIKE '%{value}%'"))
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.unique().all()]
        return res

    async def delete_one(self, **filters: dict) -> int:
        stmt = delete(self.model).filter_by(**filters).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.unique().scalar_one()