from typing import Optional
from uuid import UUID
from enum import Enum


class LessonStatus(Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Modality(Enum):
    ONLINE = "online"
    IN_PERSON = "in_person"


class Lesson:
    def __init__(self, title: str, description: Optional[str] = None):
        self.id: UUID = None
        self.title = title
        self.description = description
        self.teacher_id: Optional[UUID] = None
        self.student_id: Optional[UUID] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.status: LessonStatus = LessonStatus.SCHEDULED
        self.modality: Modality = Modality.ONLINE

    def __repr__(self):
        return f"Lesson(title={self.title}, description={self.description}, status={self.status}, modality={self.modality})"

    def __str__(self):
        return f"Lesson: {self.title}, Status: {self.status.value}, Modality: {self.modality.value}"
