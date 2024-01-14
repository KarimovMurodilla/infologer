import datetime
from typing import Optional

from fastapi_users import schemas
from pydantic import EmailStr


class UserSchema(schemas.BaseUser[int]):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: EmailStr
    about: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    created_at: datetime.datetime

    class ConfigDict:
        from_attributes = True


class UserSchemaAdd(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    last_name: str
    username: str
    about: Optional[str] = None