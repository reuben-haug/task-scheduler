def test_insert_task(db):
    # Insert a new task
    db.insert_task('Test Task', 60, 1, 'Test Description')

    # Fetch the task by id
    task = db.fetch_by_id('Tasks', 1)

    # Check that the task was inserted correctly
    assert task is not None
    assert task[1:] == ('Test Task', 60, 1, 'Test Description')

def test_fetch_by_id(db):
    # Fetch a task by id
    task = db.fetch_by_id('Tasks', 1)

    # Check that the task was fetched correctly
    assert task is not None
    assert task[1:] == ('Task 1', 2, 1, 'Task 1 description')

def test_fetch_all(db):
    # Fetch all tasks
    tasks = db.fetch_all('Tasks')

    # Check that all tasks were fetched correctly
    assert len(tasks) == 6

def test_execute_query(db):
    # Execute a query
    tasks = db.execute_query('SELECT * FROM Tasks WHERE duration = 2')

    # Check that the query returned the correct results
    assert len(tasks) == 2