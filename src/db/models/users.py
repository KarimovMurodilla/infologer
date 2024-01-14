import datetime
from typing import Annotated, List, Optional
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declared_attr

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyBaseOAuthAccountTable

from db.db import Base
from schemas.users import UserSchema

from .knows import Know
from .tasks import Task


class OAuthAccount(SQLAlchemyBaseOAuthAccountTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False)


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(25), nullable=True)
    last_name: Mapped[str] = mapped_column(String(25), nullable=True)
    username: Mapped[str] = mapped_column(String(35), nullable=True)
    about: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    knows: Mapped[List[Know]] = relationship("Know", cascade="all, delete")
    tasks: Mapped[List[Task]] = relationship("Task", cascade="all, delete")
    knows_is_private: Mapped[bool] = mapped_column(default=False, nullable=True)
    tasks_is_private: Mapped[bool] = mapped_column(default=False, nullable=True)
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship("OAuthAccount", lazy="joined")
    created_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=False, default=datetime.datetime.utcnow)]]]

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            about=self.about,
            email=self.email,
            created_at=self.created_at
        )