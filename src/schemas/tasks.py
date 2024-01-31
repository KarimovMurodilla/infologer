from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, UUID4


class TaskSchema(BaseModel):
    id: UUID4
    title: str
    description: Optional[str] = None
    user_id: int
    status: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True


class TaskSchemaAdd(BaseModel):
    title: str


class TaskSchemaEdit(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)