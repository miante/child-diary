from .body_index import BodyIndex
from .child import Child
from .user import User


# TODO: Remove after going to local database storage
# Create all tables stored in this metadata.
# Conditional by default, will not attempt to recreate tables already
# present in the target database.
from app.db.engine import Model, engine
Model.metadata.create_all(engine)
