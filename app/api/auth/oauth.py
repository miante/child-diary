from authlib.integrations.starlette_client import OAuth

from app.core import settings

oauth = OAuth()
oauth.register(
    "google",
    client_id=settings.secrets.GOOGLE_CLIENT_ID,
    client_secret=settings.secrets.GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "email",
    }
)
