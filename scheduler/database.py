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

            # Create table for Devices if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Devices(
                id INTEGER PRIMARY KEY,
                make TEXT,
                model TEXT,
                device_type TEXT,
                site_id INTEGER,
                FOREIGN KEY(site_id) REFERENCES Sites(id)
            )
        ''')

        # Commit the changes
        self.conn.commit()

    # Create, read, update, delete methods
    
    # Create methods
    def insert_site(self, name, address):
        self.cursor.execute("INSERT INTO Sites (name, address) VALUES (?, ?)", (name, address))
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_task(self, name, duration, site_id, description):
        self.cursor.execute("INSERT INTO Tasks (name, duration, site_id, description) VALUES (?, ?, ?, ?)", (name, duration, site_id, description))
        self.conn.commit()

    def insert_technician(self, name, availability):
        self.cursor.execute("INSERT INTO Technicians (name, availability) VALUES (?, ?)", (name, availability))
        self.conn.commit()

    def insert_device(self, make, model, site_id=None):
        query = "INSERT INTO Devices (make, model, site_id) VALUES (?, ?, ?)"
        self.cursor.execute(query, (make, model, site_id))
        self.conn.commit()

    # Read methods
    def fetch_by_id(self, table_name, id):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (id,))
            result = self.cursor.fetchone()
            if result is None:
                raise ValueError(f"No record found with id {id} in table {table_name}")
            return result
        except Exception as e:
            print(f"An error occurred in fetch_by_id: {e}")
            return None

    def fetch_all(self, table_name):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            results =  self.cursor.fetchall()
            if len(results) == 0:
                raise ValueError(f"No {table_name} found")
        except Exception as e:
            print(f"An error occurred in fetch_all: {e}")
            return None

    # Update methods
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