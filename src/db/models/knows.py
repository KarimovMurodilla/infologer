import datetime
from typing import Annotated, List, Optional
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
from schemas.knows import KnowsSchema

from .likes import Like
from .comments import Comment


class Know(Base):
    __tablename__ = "know"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str]
    likes: Mapped[List["Like"]] = relationship()
    comments: Mapped[List["Comment"]] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    created_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=False, default=datetime.datetime.utcnow)]]]
    
    def to_read_model(self) -> KnowsSchema:
        return KnowsSchema(
            id=self.id,
            title=self.title,
            description=self.description,
            likes=self.likes,
            comments=self.comments,
            user_id=self.user_id,
            created_at=self.created_at
        )