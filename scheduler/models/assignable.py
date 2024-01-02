#Path /scheduler/models/assignable.py

class Assignable:
    def __init__(self):
        self.tasks = []
        self.availability = 0

    def add_task(self, task):
        if self.availability >= task.duration:
            self.tasks.append(task)
            self.availability -= task.duration
            return True
        else:
            return False