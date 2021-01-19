from .body_index import BodyIndex
from .child import Child
from .user import User


def reload_database_data():
    """
    Removes all tables and creates them. This should be user for test purposes
    """

    from app.db.engine import Model

    Model.metadata.drop_all()
    Model.metadata.create_all()


# reload_database_data()
