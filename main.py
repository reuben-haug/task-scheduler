class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def fetch_by_id(self, table, id):
        self.cursor.execute(f'SELECT * FROM {table} WHERE id=?', (id,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

class Technician:
    def __init__(self, id, db):
        row = db.fetch_by_id('Technicians', id)
        self.id = row[0]
        self.name = row[1]
        self.availability = row[2]
        self.tasks = []

    def assign_task(self, task):
        if self.availability >= task.duration:
            self.tasks.append(task)
            self.availability -= task.duration
            return True
        else:
            return False

class Task:
    def __init__(self, id, db):
        row = db.fetch_by_id('Tasks', id)
        self.id = row[0]
        self.name = row[1]
        self.duration = row[2]
        self.site = Site(row[3], db)

class Site:
    def __init__(self, id, db):
        row = db.fetch_by_id('Sites', id)
        self.id = row[0]
        self.name = row[1]
        self.address = row[2]
        self.devices = row[3]

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