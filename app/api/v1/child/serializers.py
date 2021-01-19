import datetime
from typing import List, Optional

from pydantic import BaseModel, validator


class ChildInput(BaseModel):
    """
    Child model for representing a base info
    """

    full_name: str
    birth_date: datetime.date
    sex: str

    @validator('sex')
    def validate_child_sex(cls, value):
        """
        Validates that value should be `male` or `female`
        """

        if value not in ['male', 'female']:
            raise ValueError(f'Unrecognized child sex {value}')

        return value


class ChildOutput(BaseModel):
    """
    Child model for representing a base info
    """

    id: int
    full_name: str
    birth_date: datetime.date
    sex: str
    created: datetime.date
    user_id: int

    class Config:
        orm_mode = True


class ChildrenSerializer(BaseModel):
    children: List[ChildOutput] = []
