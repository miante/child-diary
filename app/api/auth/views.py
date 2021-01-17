from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from starlette.requests import Request
from starlette.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuthError

from app.api.auth.models import Identity
from app.api.auth.oauth import oauth
from app.db.engine import Session, get_session
from app.db.models import User


router = APIRouter()


@router.get("/login")
async def login(request: Request):
    """
    Authenticate user and redirects request to the main page
    """

    redirect_uri = request.url_for("google_oauth_login")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/logout")
async def logout(request: Request):
    """
    Removes user from session for further use
    """

    request.session.pop("user", None)

    return RedirectResponse(url="/")


@router.get("/oauth/google")
async def google_oauth_login(
    request: Request,
    session: Session = Depends(get_session),
):
    """
    Register/login user via google oauth and saves user to a session.
    """

    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    data = await oauth.google.parse_id_token(request, token)
    email = data['email']

    db_user = session.query(User).filter(User.email == email).scalar()
    if db_user is None:
        db_user = User(email=email)
        session.add(db_user)
        session.commit()

    request.session["user"] = Identity(**db_user.__dict__).dict()

    return RedirectResponse(url="/")
