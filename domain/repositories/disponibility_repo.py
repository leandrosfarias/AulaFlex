from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from domain.entities.disponibility import Disponibility


class IDisponibilityRepository(ABC):
    """Abstract base class for Disponibility repository."""

    @abstractmethod
    def get_disponibility(self, student_id: UUID) -> Optional[Disponibility]:
        """Retrieve disponibility by student ID."""
        pass

    @abstractmethod
    def create_disponibility(self, disponibility: Disponibility) -> Disponibility:
        """Create a new disponibility."""
        pass

    @abstractmethod
    def update_disponibility(self, disponibility: Disponibility) -> Disponibility:
        """Update existing disponibility."""
        pass

    @abstractmethod
    def delete_disponibility(self, student_id: UUID) -> None:
        """Delete disponibility by student ID."""
        pass
