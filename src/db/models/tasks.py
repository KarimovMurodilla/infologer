import uuid
import datetime

from typing import Annotated, Optional
from sqlalchemy import ForeignKey, String, func, Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from db.db import Base
from schemas.tasks import TaskSchema


class Task(Base):
    __tablename__ = "task"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    status: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=False, default=datetime.datetime.utcnow)]]]
    updated_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=True, default=datetime.datetime.utcnow)]]]

    def to_read_model(self) -> TaskSchema:
        return TaskSchema(
            id=self.id,
            title=self.title,
            description=self.description,
            user_id=self.user_id,
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
