from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Trace(BaseModel):
    updated_by: UUID
    updated_at: datetime
    created_by: UUID
    created_at: datetime
