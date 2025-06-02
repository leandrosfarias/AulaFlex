from fastapi import APIRouter, Depends, status
from interfaces.api.deps import get_teacher_repo
from interfaces.schemas.teacher_schema import TeacherCreateSchema, TeacherResponseSchema
from use_cases.create_teacher import create_teacher_use_case
from uuid import UUID

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


@router.get("/teacher/{teacher_id}",
            response_model=TeacherResponseSchema,
            status_code=status.HTTP_200_OK)
def get_teacher(teacher_id: str, teacher_repo=Depends(get_teacher_repo)):
    """
    Get a teacher by ID.
    """
    # Convert the teacher_id to UUID
    teacher_uuid = UUID(teacher_id)

    # Fetch the teacher from the repository
    teacher = teacher_repo.get_teacher_by_id(teacher_uuid)
    teacherResponse = TeacherResponseSchema(
        id=teacher.id,
        full_name=teacher.full_name,
        email=teacher.email,
        bio=teacher.bio,
        specialties=teacher.specialties
    )
    # debug log
    print(f"Fetched teacher: {teacherResponse}")

    if not teacher:
        return {"error": "Teacher not found"}, status.HTTP_404_NOT_FOUND

    return teacherResponse
