import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


connection_url = 'postgresql://postgres:postgres@localhost/diary'
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
