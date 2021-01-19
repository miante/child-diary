from typing import Optional

from pydantic import BaseModel
from starlette.authentication import BaseUser


class AuthenticatedUser(BaseModel, BaseUser):
    id: Optional[str]
    email: Optional[str]

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def display_name(self) -> str:
        return self.email

    @property
    def identity(self) -> str:
        raise NotImplementedError()  # pragma: no cover
