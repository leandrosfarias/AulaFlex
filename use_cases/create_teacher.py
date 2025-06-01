from domain.repositories.teacher_repo import ITeacherRepository
from interfaces.schemas.teacher_schema import TeacherCreateSchema
from interfaces.mappers.teacher_mapper import TeacherMapper


def create_teacher_use_case(
    teacher_dto: dict,
    teacher_repository: ITeacherRepository,
    teacher_schema: TeacherCreateSchema,
):
    """
    Use case to create a new teacher.

    Args:
        teacher_dto: Data Transfer Object containing teacher data.
        teacher_repository: Repository for managing teachers.
        teacher_schema: Schema for validating teacher data.
    Returns:
        The created Teacher entity.
    """
    # debug log
    print(f"Creating teacher with data: {teacher_dto}")
    # Validate the input data
    if not teacher_schema.model_validate(teacher_dto):
        raise ValueError("Invalid teacher data")

    # Map the DTO to an entity
    teacher_entity = TeacherMapper.map_to_entity(teacher_dto)

    # debug log
    print(f"Teacher entity to be saved: {teacher_entity}")

    # Save the entity using the repository
    return teacher_repository.save(teacher_entity)
