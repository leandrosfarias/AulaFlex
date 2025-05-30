from sqlmodel import Field, SQLModel
from enum import Enum


class UserType(str, Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"


class UserModel(SQLModel):
    """Base model for users in the system."""
    email: str = Field(
        max_length=100,
        unique=True,
        nullable=False,
        description="Unique email address of the user"
    )
    full_name: str = Field(
        max_length=100,
        nullable=False,
        description="Full name of the user"
    )
    hashed_password: str = Field(
        nullable=False,
        description="Hashed password of the user"
    )
    # To logical deletion of the user
    is_active: bool = Field(
        default=True,
        description="Indicates if the user is active.\n" +
        "If false, the user is logically deleted."
    )
    type: UserType = Field(
        default=UserType.STUDENT,
        nullable=False,
        description="Type of user: student, teacher, or admin"
    )
