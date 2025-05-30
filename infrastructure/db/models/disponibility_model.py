from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4
from datetime import datetime
from enum import IntEnum


class DayOfWeek(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class Disponibility(SQLModel, table=True):
    """Model representing a teacher's availability for lessons."""
    __tablename__ = "disponibility"
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    day_of_week: DayOfWeek
    start_time: datetime = Field(
        nullable=False,
        description="Start time of the disponibility, in ISO 8601 format (e.g., '2023-10-01T09:00:00')"
    )
    end_time: datetime = Field(
        nullable=False,
        description="End time of the disponibility, in ISO 8601 format (e.g., '2023-10-01T17:00:00')"
    )
    teacher_id: UUID = Field(foreign_key="teacher.id")

    # Navigation properties
    teacher: "Teacher" = Relationship(back_populates="disponibilities")

    @property
    def duration(self) -> int:
        """Calculate the duration in minutes."""
        return int((self.end_time - self.start_time).total_seconds() / 60)
