from fastapi import FastAPI
from app.api.routes_timetable import router as timetable_router
from app.api.routes_health import router as health_router

app = FastAPI(title="University Timetable Optimization System")

app.include_router(health_router, prefix="/health", tags=["Health"])
app.include_router(timetable_router, prefix="/timetable", tags=["Timetable"])
