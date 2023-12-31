import sqlite3
from database import Database


def main():
    # Create a Database object and setup the database
    db = Database('scheduler/db/schedule.db')
    db.setup_tables()

if __name__ == "__main__":
    main()