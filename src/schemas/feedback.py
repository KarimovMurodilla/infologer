import datetime
from typing import List

from pydantic import BaseModel, UUID4


class FeedbackSchema(BaseModel):
    id: UUID4
    description: str
    created_at: datetime.datetime

    class ConfigDict:
        from_attributes = True


class FeedbackSchemaAdd(BaseModel):
    description: str
    know_id: UUID4
