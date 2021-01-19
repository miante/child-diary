from fastapi import Request, HTTPException
from starlette import status


def is_authenticated(request: Request):
    """
    Raises an exemption if user is not authenticated
    """

    if not request.user.is_authenticated:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
