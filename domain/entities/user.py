from uuid import UUID
from typing import Optional


class User:
    def __init__(self, id: Optional[UUID], full_name: str, email: str, 
                 password_hash: str):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return f"User(id={self.id}, email={self.email})"

    def __str__(self):
        return f"User: {self.email}"

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.id == other.id and self.email == other.email
