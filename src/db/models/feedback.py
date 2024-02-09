import uuid
import datetime
from typing import Annotated, Optional
from sqlalchemy import ForeignKey, func, Column, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from db.db import Base
from schemas.likes import LikesSchema


class Like(Base):
    __tablename__ = "like"

    __table_args__ = (
        UniqueConstraint('user_id', 'know_id', name='unique_user_know_constraint'),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    know_id: Mapped[int] = mapped_column(ForeignKey("know.id"))
    created_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=False, default=datetime.datetime.utcnow)]]]


    def to_read_model(self) -> LikesSchema:
        return LikesSchema(
            id=self.id,
            user_id=self.user_id,
            know_id=self.know_id,
            created_at=self.created_at
        )