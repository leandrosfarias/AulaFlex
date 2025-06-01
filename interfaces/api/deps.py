from infrastructure.db.repositories.teacher_repo_impl import TeacherRepoImpl
from sqlmodel import Session
from fastapi import Depends
from typing import Generator
from infrastructure.db.config.config import engine  # Assuming this is the correct import for your session


def get_db_session() -> Generator[Session, None, None]:
    """
    Dependency to get the database session.
    """
    with Session(engine) as session:
        yield session


def get_teacher_repo(db_session: Session = Depends(get_db_session)) -> TeacherRepoImpl:
    """
    Dependency to get the teacher repository.
    """
    return TeacherRepoImpl(db_session)
