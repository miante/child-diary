import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


connection_url = 'sqlite:///:memory:'
engine = sqlalchemy.create_engine(connection_url, echo=False)
Model = declarative_base(engine)
Session = sessionmaker(engine, autoflush=False)


# TODO: Remove after going to local database storage
# Create all tables stored in this metadata.
# Conditional by default, will not attempt to recreate tables already
# present in the target database.
Model.metadata.create_all(engine)
