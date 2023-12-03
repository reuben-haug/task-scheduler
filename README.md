# Task Scheduler

## Description

This project is a task scheduler for technicians. It uses SQLite for data storage and Python for data processing and scheduling logic. The main components are a `Database` class for handling SQLite operations, and `Technician`, `Task`, and `Site` classes for handling technician, task, and site data and operations.

## Installation

1. Clone the repository: `git clone https://github.com/reuben-haug/taskscheduler.git`
2. Navigate to the project directory: `cd taskscheduler`
3. Install the required Python packages: `pip install -r requirements.txt`

## Usage

Run the main script with Python:

```bash
python scheduler/main.py
```

## Testing

To run the tests, navigate to the project directory and run pytest:
```bash
pytest
```

## TODO

- [ ] Fix failing test cases in `test_database.py` and `test_main.py`.