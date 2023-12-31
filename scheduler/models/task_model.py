# Path: scheduler/models/technician_model.py

from .base_model import BaseModel

# Task class for handling task data
class Task(BaseModel):
    def __init__(self, id, name, duration, description, db, tasks=None):
        super().__init__(db)
        
        self.db = db
        self.id = id
        self.name = name
        self.duration = duration
        self.description = description
        self.tasks = tasks if tasks is not None else []

    # Assign a task to a technician if they have enough availability
    def assign_task(self, technician):
        if technician.availability >= self.duration:
            technician.tasks.append(self)
            technician.availability -= self.duration
            return True
        else:
            return False