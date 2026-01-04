from fastapi import APIRouter
from app.models.requests import TimetableRequest
from app.services.timetable_service import generate_timetable

router = APIRouter()

@router.post("/generate")
def generate_timetable_api(req: TimetableRequest):
    return generate_timetable(req)
