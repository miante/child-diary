from typing import Optional

from pydantic import BaseModel


class AbstractUser(BaseModel):
    email: Optional[str] = None
    is_authorized: bool = False


class AuthorizedUser(AbstractUser):
    email: str
    is_authorized: bool = True
