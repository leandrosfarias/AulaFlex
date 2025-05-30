from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4


class Feedback(SQLModel, table=True):
    """Model representing feedback for a lesson given by a student."""
    __tablename__ = "feedback"
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    lesson_id: UUID = Field(
        foreign_key="lesson.id",
    )
    student_id: UUID = Field(
        foreign_key="student.id",
    )
    comment: str | None = Field(
        default=None,
        max_length=500,
        description="Comment provided by the student"
    )
    rating: int = Field(
        ge=1,  # Greater than or equal to 1
        le=5,  # Less than or equal to 5
        description="Rating given by the student, from 1 to 5"
    )

    # Navigation properties
    lesson: "Lesson" = Relationship(back_populates="feedbacks")
    student: "Student" = Relationship(back_populates="feedbacks")
