from pydantic import BaseSettings, Field


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
    POSTGRES_HOST: str = Field(env='POSTGRES_HOST')
    POSTGRES_PORT: int = Field(env='POSTGRES_PORT')
    POSTGRES_USERNAME: str = Field(env='POSTGRES_USERNAME')
    POSTGRES_PASSWORD: str = Field(env='POSTGRES_PASSWORD')
    POSTGRES_DATABASE: str = Field(env='POSTGRES_DATABASE')

    secrets: Secrets = Secrets()
