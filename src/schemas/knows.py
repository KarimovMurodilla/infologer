import datetime
from typing import List

from pydantic import BaseModel


class KnowsSchema(BaseModel):
    id: int
    first_name: str
    title: str
    description: str
    user_id: int
    created_at: datetime.datetime

    class ConfigDict:
        from_attributes = True


class KnowsSchemaAdd(BaseModel):
    title: str
    description: str