from pydantic import BaseModel, EmailStr, field_validator
from uuid import UUID
from typing import Optional
from infrastructure.db.models.specialty_model import Specialty


class TeacherCreateSchema(BaseModel):
    full_name: str
    email: EmailStr
    hashed_password: str
    bio: Optional[str] = None
    specialties: Optional[list[Specialty]] = None

    @field_validator('specialties', mode='before')
    @classmethod
    def validate_specialties(cls, specialties):
        if not specialties:
            return []
        return [Specialty(name=specialty) for specialty in specialties]


class TeacherResponseSchema(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    bio: Optional[str] = None
    specialties: Optional[list[Specialty]] = None
