import pytest
from scheduler.main import Site, Task
from scheduler.database import Database

def test_task():
    db = Database('tests/test.db')
    task = Task(1, db)
    assert task.id == 1
    assert task.name is not None
    assert task.duration is not None
    assert task.site is not None