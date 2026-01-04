from pydantic import BaseModel
from typing import List
from .entities import Course, Teacher, Room

class TimetableRequest(BaseModel):
    days: int
    slots_per_day: int
    courses: List[Course]
    teachers: List[Teacher]
    rooms: List[Room]
