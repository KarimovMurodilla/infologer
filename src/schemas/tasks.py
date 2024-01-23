import datetime
from typing import Optional

from pydantic import BaseModel, UUID4


class TaskSchema(BaseModel):
    id: UUID4
    title: str
    description: Optional[str] = None
    user_id: int
    status: bool
    created_at: datetime.datetime

    class ConfigDict:
        from_attributes = True


class TaskSchemaAdd(BaseModel):
    title: str


class TaskSchemaEdit(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None