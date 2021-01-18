import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core import settings


connection_kwargs = {
    'username': settings.POSTGRES_USERNAME,
    'password': settings.POSTGRES_PASSWORD,
    'host': settings.POSTGRES_HOST,
    'port': settings.POSTGRES_PORT,
    'name': settings.POSTGRES_DATABASE,
}
connection_url = 'postgresql://{username}:{password}@{host}:{port}/{name}'.format(**connection_kwargs)

engine = sqlalchemy.create_engine(connection_url, echo=True)
Model = declarative_base(engine)
Session = sessionmaker(engine, autoflush=False)


def get_session():
    """
    Creates a session holder and returns it. Will automatically close session
    after returning execution to this generator
    """

    session = Session()
    try:
        yield session
    finally:
        session.close()
