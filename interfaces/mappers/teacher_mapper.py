from infrastructure.db.models.teacher_model import Teacher
from infrastructure.db.models.specialty_model import Specialty

class TeacherMapper:
    """Mapper class for converting Teacher data transfer objects to Teacher entities."""

    @staticmethod
    def map_to_entity(teacher_dto: dict) -> Teacher:
        """
        Map a dictionary containing teacher data to a Teacher entity.

        Args:
            teacher_dto (dict): Dictionary containing teacher data.

        Returns:
            Teacher: A Teacher entity populated with the data from the DTO.
        """

        specialties_data = teacher_dto.pop('specialties', [])
        # Convert specialties data to a list of Specialty objects if they exist
        specialties = []
        for item in specialties_data:
            if isinstance(item, dict):
                specialties.append(Specialty(**item))
            elif isinstance(item, Specialty):  # já pode estar convertido
                specialties.append(item)

        return Teacher(**teacher_dto, specialties=specialties)
