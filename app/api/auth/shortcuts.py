from fastapi import Request, HTTPException
from pydantic import ValidationError
from starlette import status

from app.api.auth.models import AuthorizedUser


def login_required(request: Request):
    """
    Verifies that user passes hjs authentication and is verified
    """

    try:
        request.state.user = AuthorizedUser(**request.session.get('user'))
    except (TypeError, ValidationError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
