from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from pydantic import Field


class TraceableByDate(BaseModel):
    updated_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)


class TraceableById(BaseModel):
    updated_by: UUID
    created_by: UUID


class Traceable(TraceableByDate, TraceableById):
    pass
