# tests/conftest.py
import pytest
import os
from ..scheduler.database import Database
from .insert_test_data import insert_test_data

@pytest.fixture
def db():
    # Setup: create a new Database object before each test
    db = Database('test.db')
    db.setup()
    db.setup_tables()

    # Insert test data into the database
    insert_test_data(db)
    # Return the Database object to the test so it can be used
    yield db

    # Teardown: close the database connection after each test
    db.close()
    os.remove('test.db')