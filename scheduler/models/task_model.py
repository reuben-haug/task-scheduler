# Path: scheduler/models/technician_model.py

from .base_model import BaseModel

# Task class for handling task data
class Task(BaseModel):
    def __init__(self, id, name, duration, description, status="Pending"):
        super().__init__(id, name)

        self.duration = duration
        self.description = description
        self.status = status # Could be 'Pending', 'In Progress', 'Completed'