import datetime
from typing import Annotated, Optional
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.comments import CommentsSchema


class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    know_id: Mapped[int] = mapped_column(ForeignKey("know.id"))
    created_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=False, default=datetime.datetime.utcnow)]]]

    def to_read_model(self) -> CommentsSchema:
        return CommentsSchema(
            id=self.id,
            text=self.text,
            user_id=self.user_id,
            know_id=self.know_id,
            created_at=self.created_at
        )