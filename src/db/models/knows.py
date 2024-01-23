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


class Know(Base):
    __tablename__ = "know"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str]
    likes: Mapped[List["Like"]] = relationship()
    comments: Mapped[List["Comment"]] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="knows")
    created_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=False, default=datetime.datetime.utcnow)]]]
    
    def to_read_model(self) -> KnowsSchema:
        return KnowsSchema(
            id=self.id,
            title=self.title,
            description=self.description,
            user=self.user,
            created_at=self.created_at
        )