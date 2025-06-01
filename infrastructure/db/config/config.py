from sqlmodel import SQLModel, create_engine, Session
from infrastructure.db.models import *

DATABASE_URL = "sqlite:///./test.db"  # Example for SQLite, change as needed
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    """Create the database and tables."""
    # Print the names of the tables to be created
    print(SQLModel.metadata.tables.keys())
    # Create all tables in the database
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """Get a new database session."""
    return Session(engine)
