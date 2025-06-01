from typing import List
from uuid import UUID
from .lesson import Lesson
from .user import User


class Student(User):
    """Entity representing a student in the system."""

    def __init__(self, id: UUID, full_name: str, email: str, password_hash: str,
                 birth_date: str):
        super().__init__(id, full_name, email, password_hash)
        self.birth_date = birth_date
        self.lessons: List[Lesson] = []

    def add_lesson(self, lesson: Lesson):
        """Add a lesson to the student's list of lessons."""
        self.lessons.append(lesson)

    def __repr__(self):
        return f"Student(id={self.id}, full_name={self.full_name}, email={self.email}, birth_date={self.birth_date})"
