import uuid
from uuid import UUID
from sqlmodel import Field, SQLModel, Relationship
from .teacher_specialty_model import TeacherSpecialty


class Specialty(SQLModel, table=True):
    """Model representing a specialty that teachers can have."""
    __tablename__ = "specialty"
    id: UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(
        max_length=100,
        description="Name of the specialty, e.g., Mathematics, Science"
    )
    description: str | None = Field(
        default=None,
        max_length=255,
        description="Description of the specialty"
    )
    teachers: list["Teacher"] = Relationship(
        back_populates="specialties",
        link_model=TeacherSpecialty
    )
