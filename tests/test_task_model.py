# PATH: /scheduler/tests/test_task_model.py

import pytest
from ..scheduler.models.task_model import Task

class TestTaskModel:
    @pytest.fixture
    def task(self):
        return Task(1, 'Task 1', 3, 'Test Description 1', 'Pending')

    def test_init(self, task):
        assert task.id == 1
        assert task.name == 'Task 1'
        assert task.duration == 3
        assert task.description == 'Test Description 1'
        assert task.status == 'Pending'