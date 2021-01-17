from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.requests import Request
from starlette.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuthError

from app.api.auth.models import User
from app.api.auth.oauth import google_oauth
from app.core.log import logger

router = APIRouter()


@router.route("/login")
async def login(request: Request):
    """
    Authenticate user and redirects request to the main page
    """

    redirect_uri = request.url_for("auth")
    return await google_oauth.authorize_redirect(request, redirect_uri)


@router.route("/logout")
async def logout(request: Request):
    """
    Removes user from session for further use
    """

    request.session.pop("user", None)

    return RedirectResponse(url="/")


@router.route("/oauth/google")
async def auth(request: Request):
    """
    Authenticate user via google oauth and saves user to session.
    """

    try:
        token = await google_oauth.authorize_access_token(request)
    except OAuthError as error:
        logger.error(f'Something went wrong {error}')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Cannot authenticate",
        )

    data = await google_oauth.parse_id_token(request, token)
    request.session["user"] = User(data).dict()

    return RedirectResponse(url="/")
