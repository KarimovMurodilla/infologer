import datetime
from typing import List

from pydantic import BaseModel


class KnowsSchema(BaseModel):
    id: int
    title: str
    description: str
    likes: List[int]
    comments: List[int]
    user_id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True


class KnowsSchemaAdd(BaseModel):
    title: str
    description: str