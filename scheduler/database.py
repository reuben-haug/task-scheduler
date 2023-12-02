import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def setup(self):
        # Create table for Technicians if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Technicians(
                id INTEGER PRIMARY KEY,
                name TEXT,
                availability INTEGER
            )
        ''')

        # Create table for Sites if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sites(
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                devices TEXT
            )
        ''')

        # Create table for Tasks if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tasks(
                id INTEGER PRIMARY KEY,
                name TEXT,
                duration INTEGER,
                site_id INTEGER,
                FOREIGN KEY(site_id) REFERENCES Sites(id)
            )
        ''')

        # Commit the changes
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = Database('schedule.db')
    db.setup()
    db.close()