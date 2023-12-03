# conftest.py
import pytest
import os
from scheduler.database import Database

@pytest.fixture
def db():
    # Setup: create a new Database object before each test
    db = Database('test.db')
    db.setup()
    db.setup_tables()

    # Insert test data
    db.insert_test_data()

    yield db

    # Teardown: close the database connection after each test
    db.close()
    os.remove('test.db')