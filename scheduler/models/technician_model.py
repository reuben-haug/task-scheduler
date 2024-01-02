# Path: scheduler/models/technician_model.py

from .base_model import BaseModel
from .assignable import Assignable

# Technician class for representing technician data
class Technician(BaseModel):
    def __init__(self, id, name, availability, tasks=None):
        super().__init__(id, name)

        # Assignable class for handling object assignments
        self.assignable = Assignable(availability, tasks)

    def add_task(self, task):
        return self.assignable.add_task(task)
