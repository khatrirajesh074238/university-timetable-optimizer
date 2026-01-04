from app.core.scheduler_greedy import greedy_schedule
from app.core.constraints import check_hard_constraints

def generate_timetable(request):
    timetable = greedy_schedule(request)

    violations = []
    for slot in timetable:
        teacher = next(
            t for t in request.teachers if t.id == slot.teacher_id
        )
        v = check_hard_constraints(slot, teacher, timetable)
        violations.extend(v)

    return {"timetable": timetable, "violations": violations}
