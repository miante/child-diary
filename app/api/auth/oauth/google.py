from starlette.config import Config
from authlib.integrations.starlette_client import OAuth

config = Config("app/api/auth/.secrets")

oauth = OAuth(config)
oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email",
    }
)
google_oauth = oauth.google
