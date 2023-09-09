import datetime
from typing import List

from pydantic import BaseModel


class LikesSchema(BaseModel):
    id: int
    user_id: int
    know_id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True


class LikesSchemaAdd(BaseModel):
    user_id: int
    know_id: int