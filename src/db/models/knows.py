import uuid
import datetime
from typing import Annotated, List, Optional
from sqlalchemy import ForeignKey, String, func, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from db.db import Base
from schemas.knows import KnowsSchema

from .likes import Like
from .comments import Comment
from .feedback import Feedback


class Know(Base):
    __tablename__ = "know"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str]
    likes: Mapped[List["Like"]] = relationship(lazy="joined")
    comments: Mapped[List["Comment"]] = relationship()
    feedback: Mapped["Feedback"] = relationship(lazy="joined")
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="knows", lazy="joined")
    created_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=False, default=datetime.datetime.utcnow)]]]
    updated_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=True, default=datetime.datetime.utcnow)]]]
    
    def to_read_model(self) -> KnowsSchema:
        return KnowsSchema(
            id=self.id,
            title=self.title,
            description=self.description,
            user=self.user,
            likes=[like.to_read_model() for like in self.likes],
            feedback=self.feedback.to_read_model() if self.feedback else None,
            created_at=self.created_at,
            updated_at=self.updated_at
        )