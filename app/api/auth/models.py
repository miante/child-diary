from pydantic import BaseModel


class Identity(BaseModel):
    email: str
