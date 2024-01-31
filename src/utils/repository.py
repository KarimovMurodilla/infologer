from abc import ABC, abstractmethod

from sqlalchemy import delete, insert, select, update, text, desc, func
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
    
    async def find_all(self, offset: int):
        stmt = select(self.model).order_by(desc(self.model.created_at)).limit(5).offset(offset)
            
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.unique().all()]
        
        return res
    
    async def find_all_by(self, offset: int, **filters: dict):
        if self.model.__name__ == "Know" and not filters:
            stmt = (
                select(self.model)
                    .order_by(desc(self.model.created_at))
                    .filter(self.model.user.has(is_knows_private=False))
                    .limit(5)
                    .offset(offset)            
            )
        else:
            stmt = (
                select(self.model)
                    .order_by(desc(self.model.created_at))
                    .filter_by(**filters)
                    .limit(5)
                    .offset(offset)
            )

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

    async def find_like(self, value: str, offset: int):
        stmt = select(self.model).where(text(f"username LIKE '%{value}%' OR first_name LIKE '%{value}%'")).limit(10).offset(offset)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.unique().all()]
        return res

    async def count(self, **filters: dict):
        stmt = (
            select(self.model)
                .filter_by(**filters)
        )

        res = await self.session.execute(stmt)
        result = res.all()
        count = len(result)
        return count
    
    async def delete_one(self, **filters: dict) -> int:
        stmt = delete(self.model).filter_by(**filters).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.unique().scalar_one()