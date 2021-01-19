from pydantic import ValidationError
from starlette.authentication import AuthenticationBackend, AuthCredentials

from .identity import AuthenticatedUser


class SessionAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        """
        Authenticates user regarding his session state
        """

        user = conn.session.get('user')
        if not user:
            return None

        try:
            user = AuthenticatedUser(**user)
        except (TypeError, ValidationError):
            return None

        return AuthCredentials(), user
