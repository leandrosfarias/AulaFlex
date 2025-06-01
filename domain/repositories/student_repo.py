from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from domain.entities.student import Student


class IStudentRepository(ABC):
    """Abstract base class for Student repository."""

    @abstractmethod
    def get_student(self, student_id: UUID) -> Optional[Student]:
        """Retrieve a student by their ID."""
        pass

    @abstractmethod
    def create_student(self, student: Student) -> Student:
        """Create a new student."""
        pass

    @abstractmethod
    def update_student(self, student: Student) -> Student:
        """Update an existing student."""
        pass

    @abstractmethod
    def delete_student(self, student_id: UUID) -> None:
        """Delete a student by their ID."""
        pass
