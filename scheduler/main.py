import sqlite3
from scheduler.database import Database

# Technician class for handling technician data and operations
class Technician:
    def __init__(self, id, db):
        # Fetch technician data from the database
        row = db.fetch_by_id('Technicians', id)
        if row is None:
            raise Exception(f"Technician with id {id} not found")
        self.id = row[0]
        self.name = row[1]
        self.availability = row[2]
        self.tasks = []

    def assign_task(self, task):
        # Assign a task to the technician if they have enough availability
        if self.availability >= task.duration:
            self.tasks.append(task)
            self.availability -= task.duration
            return True
        else:
            return False

# Task class for handling task data and operations
class Task:
    def __init__(self, id, db):
        self.db = db
        self.id = id
        task_data = self.db.fetch_by_id('tasks', self.id)
        if task_data is None:
            raise Exception(f'Task with id {self.id} not found')
        self.name = task_data[1]
        self.description = task_data[2]  # Assuming description is the third column in your tasks table
        self.duration = task_data[3]
        self.site = Site(task_data[4], self.db)

class Site:
    def __init__(self, id, db):
        self.db = db
        self.id = id
        # Fetch site data from the database
        site_data = self.db.fetch_by_id('Sites', self.id)
        if site_data is None:
            raise Exception(f"Site with id {self.id} not found")
        self.name = site_data[1]
        self.address = site_data[2]
        self.devices = site_data[3]


# Function to schedule tasks to technicians
def schedule_tasks(technicians, tasks, db):
    for task in tasks:
        for tech in technicians:
            if tech.assign_task(task):
                print(f"Task {task.name} assigned to {tech.name} at {task.site.name}.  Devices: {task.site.devices}")
                break
    db.close()

def main():
    # Create a Database object and setup the database
    db = Database('scheduler/db/schedule.db')
    db.setup_tables()

if __name__ == "__main__":
    main()