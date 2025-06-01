from sqlmodel import Session
from infrastructure.db.models.teacher_model import Teacher
from typing import Optional
from uuid import UUID
from domain.repositories.teacher_repo import ITeacherRepository


class TeacherRepoImpl(ITeacherRepository):
    """Implementation of the Teacher repository interface using SQLModel."""
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_teacher_by_id(self, teacher_id: UUID) -> Optional[Teacher]:
        return self.db_session.get(Teacher, teacher_id)

    def get_teachers(self, page: int, page_size: int) -> list[Teacher]:
        teachers = self.db_session.select(Teacher).offset((page - 1) * page_size).limit(page_size).all()
        return teachers

    def save(self, teacher: Teacher) -> Teacher:
        # debug log
        print(f"Teacher in repo: {teacher}")
        self.db_session.add(teacher)
        self.db_session.commit()
        self.db_session.refresh(teacher)
        return teacher

    def update_teacher(self, teacher: Teacher) -> Teacher:
        self.db_session.merge(teacher)
        self.db_session.commit()
        self.db_session.refresh(teacher)
        return teacher

    def delete_teacher(self, teacher_id: UUID) -> None:
        teacher = self.get_teacher_by_id(teacher_id)
        if teacher:
            self.db_session.delete(teacher)
            self.db_session.commit()
        else:
            raise ValueError(f"Teacher with ID {teacher_id} does not exist.")
        return None
