import uuid
import datetime
from typing import Annotated, Optional
from sqlalchemy import ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from db.db import Base
from schemas.feedback import FeedbackSchema


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    description: Mapped[str]
    know_id: Mapped[int] = mapped_column(ForeignKey("know.id"))
    created_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=False, default=datetime.datetime.utcnow)]]]

    def to_read_model(self) -> FeedbackSchema:
        return FeedbackSchema(
            id=self.id,
            description=self.description,
            know_id=self.know_id,
            created_at=self.created_at
        )