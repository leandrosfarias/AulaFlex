from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.teacher import Teacher
from uuid import UUID


class ITeacherRepository(ABC):
    """Abstract base class for Teacher repository."""

    @abstractmethod
    def get_teacher_by_id(self, teacher_id: UUID) -> Optional[Teacher]:
        """Retrieve a teacher by their ID."""
        pass

    @abstractmethod
    def get_teachers(self, page: int, page_size: int) -> list[Teacher]:
        """Retrieve a list of all teachers."""
        pass

    @abstractmethod
    def create_teacher(self, teacher: Teacher) -> Teacher:
        """Create a new teacher."""
        pass

    @abstractmethod
    def update_teacher(self, teacher: Teacher) -> Teacher:
        """Update an existing teacher."""
        pass

    @abstractmethod
    def delete_teacher(self, teacher_id: UUID) -> None:
        """Delete a teacher by their ID."""
        pass
