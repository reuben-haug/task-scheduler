import sqlite3

def setup_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('schedule.db')

    # Create a cursor object
    c = conn.cursor()

    # Create table for Technicians if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS Technicians(
            id INTEGER PRIMARY KEY,
            name TEXT,
            availability INTEGER
        )
    ''')

    # Create table for Sites if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS Sites(
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            devices TEXT
        )
    ''')

    # Create table for Tasks if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS Tasks(
            id INTEGER PRIMARY KEY,
            name TEXT,
            duration INTEGER,
            site_id INTEGER,
            FOREIGN KEY(site_id) REFERENCES Sites(id)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()