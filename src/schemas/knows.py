from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, EmailStr, UUID4
from fastapi_users import schemas

from .likes import LikesSchema

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
    likes: List[LikesSchema]
    created_at: datetime
    updated_at: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True


class KnowsSchemaAdd(BaseModel):
    title: str
    description: str


class KnowSchemaEdit(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "title": "Your Title",
                "description": "Your Description"
            }
        }
        exclude = ['updated_at']
    
    updated_at: datetime = Field(default_factory=datetime.utcnow)
