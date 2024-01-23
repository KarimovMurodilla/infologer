import datetime
from typing import List

from pydantic import BaseModel, UUID4


class CommentsSchema(BaseModel):
    id: UUID4
    text: str
    user_id: int
    know_id: UUID4
    created_at: datetime.datetime

    class ConfigDict:
        from_attributes = True


class CommentsSchemaAdd(BaseModel):
    text: str
    know_id: UUID4