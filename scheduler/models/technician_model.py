# Path: scheduler/models/technician_model.py

from .base_model import BaseModel

# Technician class for representing technician data
class Technician(BaseModel):
    def __init__(self, id, name, availability, tasks, db):
        super().__init__(db)

        self.db = db
        self.id = id
        self.name = name
        self.availability = availability
        self.tasks = tasks

    # Add a task to the technician's schedule
    def add_task(self, task):
        if self.availability < task.duration:
            raise ValueError('Not enough availability')
        self.tasks.append(task)
        self.availability -= task.duration
        self.db.update_technician(self)