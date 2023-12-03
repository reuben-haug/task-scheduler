import sqlite3
from scheduler.database import Database

if __name__ == "__main__":
    db = Database('tests/test.db')  # Create a Database object
    db.insert_test_data()  # Call the function with the Database object as an argument
