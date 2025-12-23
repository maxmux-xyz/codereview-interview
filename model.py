from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from enum import Enum


# Example model - delete this and build your own
class Example(BaseModel):
    """Example"""
    id: UUID = Field(default_factory=uuid4)
    fk_id: UUID
    created_at: datetime = Field(default_factory=datetime.timezone.utc)
    updated_at: datetime = Field(default_factory=datetime.timezone.utc)
    created_by: Optional[UUID] = None  # User ID who created this

