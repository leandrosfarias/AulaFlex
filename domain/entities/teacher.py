from uuid import UUID
from typing import List, Optional
from .specialty import Specialty
from .lesson import Lesson
from .disponibility import Disponibility
from .user import User


class Teacher(User):
    """Entity representing a teacher in the system."""
    def __init__(self, full_name: str, email: str,
                 password_hash: str, bio: Optional[str] = None,
                 specialties: Optional[List[Specialty]] = None,
                 id: Optional[UUID] = None):
        """
        Initialize a Teacher instance.
        """
        super().__init__(id, full_name, email, password_hash)
        self.bio: Optional[str] = bio
        self.specialties: List[Specialty] = specialties if specialties is not None else []
        self.lessons: List[Lesson] = []
        self.disponibilities: List[Disponibility] = []

    def add_specialty(self, specialty: Specialty):
        self.specialties.append(specialty)

    def add_lesson(self, lesson: Lesson):
        self.lessons.append(lesson)
        lesson.teacher_id = self.id

    def add_disponibility(self, disponibility: Disponibility):
        self.disponibilities.append(disponibility)
        disponibility.teacher_id = self.id

    def __repr__(self):
        return f"Teacher(name={self.full_name}, email={self.email}, bio={self.bio})"

    def __str__(self):
        return f"Teacher: {self.full_name}, Email: {self.email}"

    def __eq__(self, other):
        if not isinstance(other, Teacher):
            return NotImplemented
        return self.id == other.id and self.email == other.email
