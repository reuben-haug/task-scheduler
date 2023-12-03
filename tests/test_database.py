import pytest
from scheduler.database import Database

@pytest.fixture
def db():
    # Use an in-memory database for testing
    db = Database(':memory:')
    db.setup_tables()
    db.insert_test_data()
    yield db
    db.close()

def test_insert_task(db):
    db.insert_task('Test Task', 1, 1, 'Test Description')
    task = db.fetch_by_id('Tasks', 1)
    assert task is not None
    assert task[1:] == ('Test Task', 1, 1, 'Test Description')

def test_fetch_by_id(db):
    task = db.fetch_by_id('Tasks', 1)
    assert task is not None
    assert task[1:] == ('Task 1', 2, 1, 'Task 1 description')

def test_fetch_all(db):
    tasks = db.fetch_all('Tasks')
    assert len(tasks) == 6

def test_execute_query(db):
    tasks = db.execute_query('SELECT * FROM Tasks WHERE duration = 2')
    assert len(tasks) == 2