import datetime
from typing import List

from pydantic import BaseModel, UUID4


class LikesSchema(BaseModel):
    id: UUID4
    user_id: int
    know_id: UUID4
    created_at: datetime.datetime

    class ConfigDict:
        from_attributes = True


class LikesSchemaAdd(BaseModel):
    know_id: UUID4