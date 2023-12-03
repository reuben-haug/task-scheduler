import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def setup(self):
        pass

    def setup_tables(self):
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
                devices INTEGER
            )
        ''')

        # Create table for Tasks if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tasks(
                id INTEGER PRIMARY KEY,
                name TEXT,
                duration INTEGER,
                site_id INTEGER,
                description TEXT,
                FOREIGN KEY(site_id) REFERENCES Sites(id)
            )
        ''')

        # Commit the changes
        self.conn.commit()

    def insert_task(self, name, duration, site_id, description):
        self.cursor.execute("INSERT INTO Tasks (name, duration, site_id, description) VALUES (?, ?, ?, ?)", (name, duration, site_id, description))
        self.conn.commit()

    def fetch_by_id(self, table_name, id):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"An error occurred in fetch_by_id: {e}")
            return None

    def fetch_all(self, table_name):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"An error occurred in fetch_all: {e}")
            return None

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"An error occurred in execute_query: {e}")
            return None

    def close(self):
        # Check if the connection exists before trying to close it
        if self.conn:
            # Close the cursor if it exists
            if self.cursor:
                self.cursor.close()
            # Close the connection
            self.conn.close()

    # Function to insert test data into the database
    
    def insert_test_data(self):
        self.setup_tables()

        # Insert test data for Technicians
        self.cursor.execute("INSERT INTO Technicians (name, availability) VALUES ('Bob', 8)")
        self.cursor.execute("INSERT INTO Technicians (name, availability) VALUES ('Sally', 8)")
        self.cursor.execute("INSERT INTO Technicians (name, availability) VALUES ('Joe', 8)")

        # Insert test data for Sites
        self.cursor.execute("INSERT INTO Sites (name, address, devices) VALUES ('Site 1', '123 Main St.', '2')")
        self.cursor.execute("INSERT INTO Sites (name, address, devices) VALUES ('Site 2', '456 Main St.', '1')")
        self.cursor.execute("INSERT INTO Sites (name, address, devices) VALUES ('Site 3', '789 Main St.', '1')")

        # Insert test data for Tasks
        self.cursor.execute("INSERT INTO Tasks (name, duration, site_id, description) VALUES ('Task 1', 2, 1, 'Task 1 description')")
        self.cursor.execute("INSERT INTO Tasks (name, duration, site_id, description) VALUES ('Task 2', 1, 1, 'Task 2 description')")
        self.cursor.execute("INSERT INTO Tasks (name, duration, site_id, description) VALUES ('Task 3', 3, 2, 'Task 3 description')")
        self.cursor.execute("INSERT INTO Tasks (name, duration, site_id, description) VALUES ('Task 4', 1, 3, 'Task 4 description')")
        self.cursor.execute("INSERT INTO Tasks (name, duration, site_id, description) VALUES ('Task 5', 2, 3, 'Task 5 description')")
        self.cursor.execute("INSERT INTO Tasks (name, duration, site_id, description) VALUES ('Task 6', 3, 3, 'Task 6 description')")


        # Commit the changes
        self.conn.commit()
