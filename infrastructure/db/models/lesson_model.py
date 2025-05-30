from sqlmodel import Field, SQLModel, Relationship
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum

class LessonStatus(Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    RESCHEDULED = "rescheduled"


class Modality(Enum):
    ONLINE = "online"
    IN_PERSON = "in_person"


class Lesson(SQLModel, table=True):
    """Model representing a lesson between a teacher and a student."""
    __tablename__ = "lesson"
    id: UUID | None = Field(default=uuid4, primary_key=True)
    teacher_id: UUID = Field(
        foreign_key="teacher.id",
    )
    student_id: UUID = Field(
        foreign_key="student.id",
    )
    date: datetime = Field(
        nullable=False,
        description="The date and time when the lesson is scheduled.",
    )
    duration_in_minutes: int = Field(
        nullable=False,
        gt=0,
        description="Duration of the lesson in minutes"
    )

    status: LessonStatus = Field(
        default=LessonStatus.SCHEDULED,
        description="Current status of the lesson"
    )

    modality: Modality = Field(
        default=Modality.ONLINE,
        description="Modality of the lesson (online or in-person)"
    )

    # Navigation properties
    teacher: "Teacher" = Relationship(
        back_populates="lessons"
    )
    student: "Student" = Relationship(
        back_populates="lessons"
    )
