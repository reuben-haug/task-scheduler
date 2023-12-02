import sqlite3

from database import setup_database

def insert_test_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('schedule.db')

    # Create a cursor object
    c = conn.cursor()

    # Insert test data into Technicians table
    technicians = [("Tech 1", 4), ("Tech 2", 2), ("Tech 3", 3)]
    c.executemany('''
        INSERT INTO Technicians(name, availability) VALUES (?,?)
    ''', technicians)

    # Insert test data into Sites table
    sites = [("Site A", "123 Main Street", "Device 1,Device 2"), 
             ("Site B", "321 Real Street", "Device 3,Device 4"), 
             ("Site C", "456 Fake Street", "Device 5,Device 6")]
    c.executemany('''
        INSERT INTO Sites(name, address, devices) VALUES (?,?,?)
    ''', sites)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def test_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('schedule.db')

    # Create a cursor object
    c = conn.cursor()

    # Fetch all data from Technicians table
    c.execute('SELECT * FROM Technicians')
    print("Technicians:")
    for row in c.fetchall():
        print(row)

    # Fetch all data from Sites table
    c.execute('SELECT * FROM Sites')
    print("\nSites:")
    for row in c.fetchall():
        print(row)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    setup_database()
    insert_test_data()
    test_database()