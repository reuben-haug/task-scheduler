#Path /scheduler/models/assignable.py

class Assignable:
    def __init__(self, availability, tasks=None):
        self.availability = availability
        self.tasks = tasks if tasks is not None else []

    def add_task(self, task):
        if task in self.tasks:
            raise ValueError('Task already assigned')
        if task.duration > self.availability:
            raise ValueError('Not enough availability')
        self.tasks.append(task)
        self.availability -= task.duration
        return True