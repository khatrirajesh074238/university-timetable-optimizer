from pydantic import BaseModel
from typing import List, Optional

class Course(BaseModel):
    id: str
    name: str
    hours_per_week: int
    teacher_id: str

class Teacher(BaseModel):
    id: str
    name: str
    max_hours_per_day: int
    availability: List[List[int]]  # matrix: days x slots

class Room(BaseModel):
    id: str
    capacity: int

class TimetableSlot(BaseModel):
    day: int
    slot: int
    course_id: Optional[str] = None
    teacher_id: Optional[str] = None
    room_id: Optional[str] = None
