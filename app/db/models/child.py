import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.db import engine


class Child(engine.Model):
    """
    Base child model within application for connecting it to other details
    """

    __tablename__ = 'child'

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)

    full_name = sa.Column('full_name', sa.String(255), nullable=False)
    birth_date = sa.Column(sa.Date, nullable=False)
    sex = sa.Column('sex', sa.String(10), nullable=False)

    updated = sa.Column(sa.Date, onupdate=sa.func.now())
    created = sa.Column(sa.Date, server_default=sa.func.now())

    # Foreign Keys
    user_id = sa.Column(sa.BigInteger, sa.ForeignKey('user.id'), nullable=False)

    # Relationships
    body_indexes = relationship(
        'BodyIndex',
        cascade="all, delete-orphan",
        back_populates="child",
    )
    user = relationship('User', back_populates="children")
