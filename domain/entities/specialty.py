from typing import Optional


class Specialty:
    def __init__(self, name: str):
        self.name = name
        self.description: Optional[str] = None
