from pydantic import BaseSettings, Field, AnyUrl


class Secrets(BaseSettings):
    # Google OAuth2 credentials
    GOOGLE_CLIENT_ID: str = Field(env='GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET: str = Field(env='GOOGLE_CLIENT_SECRET')

    # Internal application keys
    SESSION_MIDDLEWARE_SECRET: str = Field(env='SESSION_MIDDLEWARE_SECRET')


class Settings(BaseSettings):
    DEBUG: int = False
    VERSION: str = '0.1.0'

    # Postgres Database connection configuration
    POSTGRES_HOST: AnyUrl
    POSTGRES_PORT: int
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_DATABASE: str

    secrets: Secrets = Secrets()
