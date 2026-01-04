from app.models.entities import TimetableSlot

def greedy_schedule(request):
    timetable = []

    for day in range(request.days):
        for slot in range(request.slots_per_day):
            timetable.append(TimetableSlot(day=day, slot=slot))

    # naive placement (baseline)
    course_index = 0
    for slot in timetable:
        if course_index < len(request.courses):
            c = request.courses[course_index]
            slot.course_id = c.id
            slot.teacher_id = c.teacher_id
            course_index += 1

    return timetable
