import datetime
from typing import List, Optional

from fastapi_users import schemas


class UserSchema(schemas.BaseUser[int]):
    id: int
    name: str
    username: str
    email: str
    about: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    created_at: datetime.datetime

    class Config:
        from_attributes = True


class UserSchemaAdd(schemas.BaseUserCreate):
    name: str
    username: str
    about: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False