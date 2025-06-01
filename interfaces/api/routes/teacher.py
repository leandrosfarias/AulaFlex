from fastapi import APIRouter, Depends, status
from interfaces.api.deps import get_teacher_repo
from interfaces.schemas.teacher_schema import TeacherCreateSchema, TeacherResponseSchema
from infrastructure.db.models.teacher_model import Teacher
from infrastructure.db.models.specialty_model import Specialty

router = APIRouter()


@router.post("/teacher", response_model=TeacherResponseSchema,
             status_code=status.HTTP_201_CREATED)
def create_teacher(teacher: TeacherCreateSchema, teacher_repo=Depends(get_teacher_repo)):
    """
    Create a new teacher.
    """
    specialties = teacher.specialties or []
    # Convert specialties to a list of Specialty objects if they are not empty
    if specialties:
        specialties = [Specialty(name=specialty) for specialty in specialties]
    teacher = teacher.model_dump()
    teacher['specialties'] = specialties
    teacher_entity = Teacher(**teacher)

    teacher_entity.specialties = specialties
    created_teacher = teacher_repo.create_teacher(teacher_entity)
    teacher_response = TeacherResponseSchema(id=created_teacher.id, full_name=created_teacher.full_name,
                                             specialties=created_teacher.specialties, bio=created_teacher.bio,
                                             email=created_teacher.email)
    return teacher_response
