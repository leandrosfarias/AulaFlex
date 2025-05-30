from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4


class TeacherSpecialty(SQLModel, table=True):
    """Model representing the many-to-many relationship between teachers and
    specialties."""
    __tablename__ = "teacher_specialty"
    teacher_id: UUID = Field(default_factory=uuid4,
                             foreign_key="teacher.id",
                             primary_key=True)

    specialty_id: UUID = Field(default_factory=uuid4,
                               foreign_key="specialty.id",
                               primary_key=True)
