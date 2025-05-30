from sqlmodel import Field, Relationship
from uuid import UUID, uuid4
from .user_model import UserModel
from .lesson_model import Lesson
from datetime import datetime


class Student(UserModel, table=True):
    """Model representing a student in the system."""
    __tablename__ = "student"
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    birth_date: datetime = Field(
        nullable=False,
    )
    lessons: list["Lesson"] = Relationship(
        back_populates="student"
    )
