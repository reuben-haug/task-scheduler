# /scheduler/tests/test_task_repository.py

import pytest
from ..scheduler.repositories.task_repository import TaskRepository
from ..scheduler.models.task_model import Task

class TestTaskRepository:
    @pytest.fixture
    def db(self, mocker):
        return mocker.Mock()

    @pytest.fixture
    def task_repository(self, db):
        return TaskRepository(db)

    def test_get_by_id(self, task_repository, db, mocker):
        db.fetch_by_id.return_value = (1, 'Task 1', 2, 'Description 1', [])
        task = task_repository.get_by_id(1)
        db.fetch_by_id.assert_called_once_with('Tasks', 1)
        print(type(task))
        assert isinstance(task, Task)
        assert task.id == 1
        assert task.name == 'Task 1'
        assert task.duration == 2
        assert task.description == 'Description 1'
        assert task.tasks == []

    def test_get_by_id_none(self, task_repository, db):
        db.fetch_by_id.return_value = None
        task = task_repository.get_by_id(1)
        db.fetch_by_id.assert_called_once_with('Tasks', 1)
        assert task is None