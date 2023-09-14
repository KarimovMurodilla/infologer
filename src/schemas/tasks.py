import datetime
from typing import Optional

from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    status: bool
    created_at: datetime.datetime

    class ConfigDict:
        from_attributes = True


class TaskSchemaAdd(BaseModel):
    title: str
    description: str