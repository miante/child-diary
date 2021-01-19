import datetime
from typing import List, Optional

from pydantic.main import BaseModel


class BodyIndexInput(BaseModel):
    height: float
    weight: float
    timestamp: datetime.date
    child_id: int


class BodyIndexUpdateInput(BaseModel):
    id: int
    height: float
    weight: float
    timestamp: datetime.date


class BodyIndexOutput(BaseModel):
    id: int
    height: float
    weight: float
    timestamp: datetime.date
    child_id: int

    class Config:
        orm_mode = True


class ChildBodyIndexesSerializer(BaseModel):
    body_indexes: List[BodyIndexOutput] = []
