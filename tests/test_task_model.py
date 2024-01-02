# PATH: /scheduler/tests/test_task_model.py

import pytest
from unittest.mock import Mock
from ..scheduler.models.technician_model import Technician
from ..scheduler.models.task_model import Task 
from ..scheduler.models.base_model import BaseModel

class TestTaskModel(BaseModel):
    @pytest.fixture
    def db(self):
        return Mock()

    @pytest.fixture
    def task(self, db):
        return Task(1, 'Task 1', 3, 'Test Description 1', self.db)

    def test_init(self, task):
        assert task.id == 1
        assert task.name == 'Task 1'
        assert task.duration == 3
        assert task.description == 'Test Description 1'
        #assert task.db == db

    def test_add_task_enough_availability(self, task, db):
        technician = Technician(1, 'John Doe', 8, [], self.db)
        result = task.add_task(technician)
        assert result == True
        assert technician.availability == 5
        assert technician.tasks == [task]
        #technician.db.update_technician.assert_called_once_with(technician)

    def test_add_task_not_enough_availability(self, task, db):
        technician = Technician(1, 'John Doe', 2, [], self.db)  # Technician's availability is less than task duration
        result = task.add_task(technician)
        assert result == False
        assert technician.availability == 2  # Availability should not change
        assert technician.tasks == []  # No task should be added
        #technician.db.update_technician.assert_not_called()  # update_technician should not be called