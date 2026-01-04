# Automated University Timetable Optimizer

**A constraint-driven scheduling engine with heuristic repair optimization for university timetables, built using Python and FastAPI.**

## Project Overview
Academic scheduling is a complex constraint satisfaction problem involving faculty availability, room capacities, and course load distribution. This project implements an automated solution to generate conflict-free timetables while optimizing for resource efficiency and schedule quality.

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