import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.db import engine


class User(engine.Model):
    """
    Base user model within application for authentication and other purposes
    """

    __tablename__ = 'user'

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)

    email = sa.Column('email', sa.String(255), nullable=False)

    updated = sa.Column(sa.Date, onupdate=sa.func.now())
    created = sa.Column(sa.Date, server_default=sa.func.now())

    # Relationships
    children = relationship(
        'Child',
        cascade="all, delete-orphan",
        back_populates="user",
    )
