from sqlmodel import Field, Relationship
from uuid import UUID, uuid4
from .user_model import UserModel
from .lesson_model import Lesson
from .disponibility_model import Disponibility
from .teacher_specialty_model import TeacherSpecialty


class Teacher(UserModel, table=True):
    """Model representing a teacher in the system."""
    __tablename__ = "teacher"
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    bio: str = Field(
        default=None,
        max_length=500,
        nullable=True,
        description="Biography of the teacher"
    )
    specialty_id: int = Field(foreign_key="specialty.id")

    # Navigation properties
    specialties: list["Specialty"] = Relationship(
        back_populates="teachers",
        link_model=TeacherSpecialty
    )
    lessons: list["Lesson"] = Relationship(
        back_populates="teacher"
    )
    disponibilities: list["Disponibility"] = Relationship(
        back_populates="teacher"
    )
