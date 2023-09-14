import datetime
from typing import List

from pydantic import BaseModel


class CommentsSchema(BaseModel):
    id: int
    text: str
    user_id: int
    know_id: int
    created_at: datetime.datetime

    class ConfigDict:
        from_attributes = True


class CommentsSchemaAdd(BaseModel):
    text: str
    know_id: int