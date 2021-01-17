import sqlalchemy as sa
from sqlalchemy import BigInteger

from app.db import engine


class BodyIndex(engine.Model):
    """
    Model represents child body index of particular date
    """

    id = sa.Column(sa.BigInteger, primary_key=True)

    height = sa.Column('height', sa.Float(precision=2))
    weight = sa.Column('weight', sa.Float(precision=2))
    timestamp = sa.Column(sa.Date, server_default=sa.func.now())

    # Foreign Keys
    child = sa.Column(BigInteger, sa.ForeignKey('child.id'))
