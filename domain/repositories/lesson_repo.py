from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from domain.entities.lesson import Lesson


class ILessonRepository(ABC):
    """Abstract base class for Lesson repository."""

    @abstractmethod
    def get_lesson(self, lesson_id: UUID) -> Optional[Lesson]:
        """Retrieve a lesson by its ID."""
        pass

    @abstractmethod
    def create_lesson(self, lesson: Lesson) -> Lesson:
        """Create a new lesson."""
        pass

    @abstractmethod
    def update_lesson(self, lesson: Lesson) -> Lesson:
        """Update an existing lesson."""
        pass

    @abstractmethod
    def delete_lesson(self, lesson_id: UUID) -> None:
        """Delete a lesson by its ID."""
        pass
