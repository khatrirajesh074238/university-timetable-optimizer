def check_hard_constraints(slot, teacher, timetable):
    violations = []

    # Teacher double booking
    for s in timetable:
        if (
            s.day == slot.day and s.slot == slot.slot and 
            s.teacher_id == slot.teacher_id
        ):
            violations.append("Teacher conflict")

    # TODO: add room clash, availability, max load rules

    return violations
