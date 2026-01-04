# Automated University Timetable Optimizer

**A constraint-driven scheduling engine with heuristic repair optimization for university timetables, built using Python and FastAPI.**

## Project Overview
Academic scheduling is a complex constraint satisfaction problem involving faculty availability, room capacities, and course load distribution. This project implements an automated solution to generate conflict-free timetables while optimizing for resource efficiency and schedule quality.

## Project Status & Roadmap

* **Phase 1:** FastAPI Scaffold & Greedy Scheduler (Baseline) — *Completed*
* **Phase 2:** Hard Constraint Validation — *In Progress*
* **Phase 3:** Heuristic Repair (Hill Climbing) — *Planned*
* **Phase 4:** Soft Constraints & Multi-objective Scoring  — *Planned*


## Key Features

* **Constraint Validation:** Enforces hard rules including room capacity, teacher availability, and time conflicts.
* **Hybrid Scheduling Engine:** Utilizes a Greedy algorithm for initial construction and Hill Climbing heuristics for iterative repair.
* **Evaluation Metrics:** Quantifies schedule quality based on workload distribution and gap minimization.

## Technical Stack

* **Language:** Python 3.12
* **Framework:** FastAPI
* **Validation:** Pydantic

## Project Structure

* `app/core/`: Core algorithms (Greedy Scheduler, Repair Heuristics)
* `app/api/`: API Endpoints and Routes
* `data/`: Sample Input Data sets

## Installation and Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/khatrirajesh074238/university-timetable-optimizer.git
   cd university-timetable-optimizer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

## Example API Usage

### Sample Request (POST /schedule/generate)
```json
{
  "days": 5,
  "slots_per_day": 6,
  "courses": [
    {"id": "C1", "name": "Algorithms", "hours_per_week": 3, "teacher_id": "T1"}
  ],
  "teachers": [
    {"id": "T1", "name": "Dr. Alice", "max_hours_per_day": 4}
  ],
  "rooms": [
    {"id": "R1", "capacity": 60}
  ]
}
```


### Sample Response (Output)
```json
{
  "status": "success",
  "summary": {
    "total_courses_scheduled": 3,
    "total_conflicts": 0,
    "score": 87.5
  },
  "timetable": [
    {
      "day": "Monday",
      "slot": 1,
      "course_id": "C1",
      "course_name": "Algorithms",
      "teacher_id": "T1",
      "room_id": "R1"
    },
    {
      "day": "Monday",
      "slot": 2,
      "course_id": "C2",
      "course_name": "Operating Systems",
      "teacher_id": "T2",
      "room_id": "R2"
    },
    {
      "day": "Tuesday",
      "slot": 1,
      "course_id": "C3",
      "course_name": "Machine Learning",
      "teacher_id": "T1",
      "room_id": "R1"
    }
  ]
}
```
## Schedule Quality Metrics
The optimizer evaluates timetable quality using:
- Conflict Count (lower is better)
- Teacher Workload Balance
- Idle Gap Penalty
- Room Utilization Score


## License
MIT License — feel free to use and enhance.

## Contributions
Open to research collaboration and feature suggestions.

