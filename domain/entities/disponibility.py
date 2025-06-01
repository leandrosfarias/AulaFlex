from typing import Optional
from uuid import UUID


class Disponibility:
    def __init__(self, day: str, start_time: str, end_time: str):
        self.id: UUID = UUID()
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.teacher_id: Optional[UUID] = None

    def __repr__(self):
        return f"Disponibility(day={self.day}, start_time={self.start_time}, end_time={self.end_time})"
