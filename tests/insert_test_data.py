import sqlite3

# Connect to the test database
conn = sqlite3.connect('tests/test.db')
cursor = conn.cursor()

# Create the Technicians, Tasks, and Sites tables
cursor.execute('''
    CREATE TABLE Technicians (
        id INTEGER PRIMARY KEY,
        name TEXT,
        availability INTEGER
    )
''')
cursor.execute('''
    CREATE TABLE Tasks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        duration INTEGER,
        site_id INTEGER
    )
''')
cursor.execute('''
    CREATE TABLE Sites (
        id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        devices TEXT
    )
''')

# Insert test data into the tables
cursor.execute('''
    INSERT INTO Technicians (id, name, availability) VALUES
    (1, 'Technician 1', 8),
    (2, 'Technician 2', 8)
''')
cursor.execute('''
    INSERT INTO Tasks (id, name, duration, site_id) VALUES
    (1, 'Task 1', 2, 1),
    (2, 'Task 2', 3, 1)
''')
cursor.execute('''
    INSERT INTO Sites (id, name, address, devices) VALUES
    (1, 'Site 1', '123 Main St', 10),
    (2, 'Site 2', '456 Maple Ave', 20)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()