from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from domain.entities.feedback import Feedback


class IFeedbackRepository(ABC):
    """Abstract base class for Feedback repository."""

    @abstractmethod
    def get_feedback(self, feedback_id: UUID) -> Optional[Feedback]:
        """Retrieve feedback by its ID."""
        pass

    @abstractmethod
    def create_feedback(self, feedback: Feedback) -> Feedback:
        """Create a new feedback."""
        pass

    @abstractmethod
    def update_feedback(self, feedback: Feedback) -> Feedback:
        """Update existing feedback."""
        pass

    @abstractmethod
    def delete_feedback(self, feedback_id: UUID) -> None:
        """Delete feedback by its ID."""
        pass
