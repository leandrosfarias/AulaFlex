from fastapi import APIRouter, Depends, status
from interfaces.api.deps import get_teacher_repo
from interfaces.schemas.teacher_schema import TeacherCreateSchema, TeacherResponseSchema
from infrastructure.db.models.teacher_model import Teacher
from infrastructure.db.models.specialty_model import Specialty
from use_cases.create_teacher import create_teacher_use_case


router = APIRouter()


@router.post("/teacher", response_model=TeacherResponseSchema,
             status_code=status.HTTP_201_CREATED)
def create_teacher(teacher: TeacherCreateSchema, teacher_repo=Depends(get_teacher_repo)):
    """
    Create a new teacher.
    """
    # Convert the TeacherCreateSchema to a dictionary
    teacher_dto = teacher.model_dump()
    # debug log
    print(f"Teacher DTO: {teacher_dto}")

    # Create the teacher using the use case
    response = create_teacher_use_case(
        teacher_dto=teacher_dto,
        teacher_repository=teacher_repo,
        teacher_schema=TeacherCreateSchema
    )
    return response
