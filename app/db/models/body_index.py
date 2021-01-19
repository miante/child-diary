import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.db import engine


class BodyIndex(engine.Model):
    """
    Model represents child body index of particular date
    """

    __tablename__ = 'body_index'

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)

    height = sa.Column('height', sa.Float(precision=2), nullable=False)
    weight = sa.Column('weight', sa.Float(precision=2), nullable=False)
    timestamp = sa.Column(sa.Date, server_default=sa.func.now())

    # Foreign Keys
    child_id = sa.Column(sa.BigInteger, sa.ForeignKey('child.id'), nullable=False)

    # Relationships
    child = relationship('Child', back_populates="body_indexes")
