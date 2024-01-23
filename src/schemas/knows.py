import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, EmailStr, UUID4
from fastapi_users import schemas


class User(schemas.BaseUser[int]):
    email: EmailStr = Field(exclude=True)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None

    class ConfigDict:
        from_attributes = True


class KnowsSchema(BaseModel):
    id: UUID4
    title: str
    description: str
    user: User
    created_at: datetime.datetime

    class ConfigDict:
        from_attributes = True


class KnowsSchemaAdd(BaseModel):
    title: str
    description: str