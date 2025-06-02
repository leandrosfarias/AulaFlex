from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
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
    try:
        teacher_uuid = UUID(teacher_id)
        print(f"Fetching teacher with ID: {teacher_uuid}")
    except ValueError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Invalid teacher ID format"}
        )

    # Fetch the teacher from the repository
    teacher = teacher_repo.get_teacher_by_id(teacher_uuid)
    # debug log
    print(f"Fetched teacher: {teacher}")

    if not teacher:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "Teacher not found"}
        )

    teacherResponse = TeacherResponseSchema(
        id=teacher.id,
        full_name=teacher.full_name,
        email=teacher.email,
        bio=teacher.bio,
        specialties=teacher.specialties
    )

    return teacherResponse


@router.get("/teachers", response_model=list[TeacherResponseSchema],
            status_code=status.HTTP_200_OK)
def get_teachers(page: int = 1, page_size: int = 10, teacher_repo=Depends(get_teacher_repo)):
    """
    Get a list of all teachers with pagination.
    """
    # Fetch the list of teachers from the repository
    teachers = teacher_repo.get_teachers(page, page_size)
    # debug log
    print(f"Fetched teachers: {teachers}")

    if not teachers:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "No teachers found"}
        )

    # Map the list of Teacher entities to the response schema
    teacher_responses = [
        TeacherResponseSchema(
            id=teacher.id,
            full_name=teacher.full_name,
            email=teacher.email,
            bio=teacher.bio,
            specialties=teacher.specialties
        ) for teacher in teachers
    ]

    return teacher_responses
