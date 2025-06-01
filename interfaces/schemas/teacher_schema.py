from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional
from infrastructure.db.models.specialty_model import Specialty

class TeacherCreateSchema(BaseModel):
    full_name: str
    email: EmailStr
    hashed_password: str
    bio: Optional[str] = None
    specialties: Optional[list[str]] = None


class TeacherResponseSchema(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    bio: Optional[str] = None
    specialties: Optional[list[Specialty]] = None
