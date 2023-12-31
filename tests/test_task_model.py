# Path: tests/test_task_model.py

import pytest
from ..scheduler.models.task_model import Task
from ..scheduler.models.technician_model import Technician

class TestTask:
    @pytest.fixture
    def task(self, mocker):
        db = mocker.Mock()
        return Task(1, 'Task 1', 2, 'Description 1', db)

    @pytest.fixture
    def technician(self, mocker):
        db = mocker.Mock()
        return Technician(1, 'John Doe', 8, [], db)

    def test_init(self, task, mocker):
        assert task.id == 1
        assert task.name == 'Task 1'
        assert task.duration == 2
        assert task.description == 'Description 1'
        assert isinstance(task.db, mocker.Mock)

    def test_assign_task(self, task, technician):
        assert task.assign_task(technician) == True
        assert task in technician.tasks
        assert technician.availability == 6

    def test_assign_task_not_enough_availability(self, task, mocker):
        technician = Technician(1, 'John Doe', 1, [], mocker.Mock())
        assert task.assign_task(technician) == False
        assert task not in technician.tasks
        assert technician.availability == 1