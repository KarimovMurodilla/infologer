import datetime
from typing import Annotated, List, Optional
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastapi_users.db import SQLAlchemyBaseUserTable

from db.db import Base
from schemas.users import UserSchema

from .knows import Know
from .tasks import Task


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[str] = mapped_column(String(15), nullable=False)
    about: Mapped[str]
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    knows: Mapped[List[Know]] = relationship("Know", cascade="all, delete")
    tasks: Mapped[List[Task]] = relationship("Task", cascade="all, delete")
    created_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=False, default=datetime.datetime.utcnow)]]]

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
            username=self.username,
            about=self.about,
            created_at=self.created_at
        )