import sqlite3

# Database class for handling SQLite operations
class Database:
    def __init__(self, db_name):
        # Connect to the SQLite database
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def fetch_by_id(self, table, id):
        # Fetch a row from a table by id
        self.cursor.execute(f'SELECT * FROM {table} WHERE id=?', (id,))
        return self.cursor.fetchone()

    def close(self):
        # Close the database connection
        self.conn.close()

# Technician class for handling technician data and operations
class Technician:
    def __init__(self, id, db):
        # Fetch technician data from the database
        row = db.fetch_by_id('Technicians', id)
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
        # Fetch task data from the database
        row = db.fetch_by_id('Tasks', id)
        self.id = row[0]
        self.name = row[1]
        self.duration = row[2]
        self.site = Site(row[3], db)

# Site class for handling site data and operations
class Site:
    def __init__(self, id, db):
        # Fetch site data from the database
        row = db.fetch_by_id('Sites', id)
        self.id = row[0]
        self.name = row[1]
        self.address = row[2]
        self.devices = row[3]

# Function to schedule tasks to technicians
def schedule_tasks(technicians, tasks, db):
    for task in tasks:
        for tech in technicians:
            if tech.assign_task(task):
                print(f"Task {task.name} assigned to {tech.name} at {task.site.name}.  Devices: {task.site.devices}")
                break
    db.close()

def main():
    # The site and task assignments will be handled in the test_data.py file
    pass

if __name__ == "__main__":
    main()