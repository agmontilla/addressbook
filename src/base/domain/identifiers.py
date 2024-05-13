from uuid import UUID
from uuid import uuid4

from pydantic import BaseModel
from pydantic import Field


class Identifiable(BaseModel):
    id: UUID = Field(default_factory=uuid4)
