import sqlalchemy as sa

from app.db import engine


class User(engine.Model):
    """
    Base user model within application for authentication and other purposes
    """

    id = sa.Column(sa.BigInteger, primary_key=True)

    full_name = sa.Column('full_name', sa.String(255))
    email = sa.Column('email', sa.String(255))

    updated = sa.Column(sa.Date, onupdate=sa.func.now())
    created = sa.Column(sa.Date, server_default=sa.func.now())
