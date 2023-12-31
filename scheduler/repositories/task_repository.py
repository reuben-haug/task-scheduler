# /scheduler/repositories/task_repository.py

from ..models.task_model import Task

# Task class for handling device data and operations
class TaskRepository:
    def __init__(self, database):
        self.database = database

    def insert(self, name, availability):
        self.database.insert_task(name, availability)

    def get_by_id(self, id):
        # Fetch the task by id
        task_data = self.database.fetch_by_id('Tasks', id)
        
        if task_data is not None:
        # Create a Task object with the fetched data
            task = Task(id=task_data[0], name=task_data[1], duration=task_data[2], description=task_data[3], db=self.database)
        else:
            task = None
            
        return task 

    def update(self, id, name, availability):
        self.database.update_task(id, name, availability)

    def delete(self, id):
        self.database.delete_task(id)