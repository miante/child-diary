import sqlalchemy as sa
from sqlalchemy import BigInteger

from app.db import engine


class Child(engine.Model):
    """
    Base child model within application for connecting it to other details
    """

    id = sa.Column(sa.BigInteger, primary_key=True)

    full_name = sa.Column('full_name', sa.String(255))
    birth_date = sa.Column(sa.Date)
    sex = sa.Column('sex', sa.String(10))

    updated = sa.Column(sa.Date, onupdate=sa.func.now())
    created = sa.Column(sa.Date, server_default=sa.func.now())

    # Foreign Keys
    user = sa.Column(BigInteger, sa.ForeignKey('user.id'))
