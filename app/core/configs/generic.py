from pydantic import BaseSettings, Field


class Secrets(BaseSettings):
    # Google OAuth2 credentials
    GOOGLE_CLIENT_ID: str = Field(env='GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET: str = Field(env='GOOGLE_CLIENT_SECRET')

    # Internal application keys
    SESSION_MIDDLEWARE_SECRET: str = Field(env='SESSION_MIDDLEWARE_SECRET')


class Settings(BaseSettings):
    DEBUG: int = False

    secrets: Secrets = Secrets()
