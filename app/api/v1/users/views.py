from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.api.auth.identity import AuthenticatedUser
from app.api.auth.shortcuts import is_authenticated

router = APIRouter()


@router.get(
    "/me",
    dependencies=[Depends(is_authenticated)],
    response_model=AuthenticatedUser,
)
async def get_current_user(request: Request):
    """
    Returns information of current user
    """

    return request.user
