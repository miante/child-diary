from pydantic import BaseModel


class User(BaseModel):
    email: str
    full_name: str
    is_active: bool = False
