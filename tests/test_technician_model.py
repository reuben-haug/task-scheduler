# /tests/test_technician_model.py

import pytest
from unittest.mock import Mock
from ..scheduler.models.technician_model import Technician
from ..scheduler.models.task_model import Task

class TestTechnicianModel:
    @pytest.fixture
    def technician(self):
        return Technician(1, 'John Doe', 8, [])
    
    @pytest.fixture
    def task(self):
        return Task(1, 'Task 1', 3, 'Test Description 1', status='Pending')

    def test_init(self, technician):
        assert technician.id == 1
        assert technician.name == 'John Doe'
        assert technician.assignable.availability == 8
        assert technician.assignable.tasks == []

    def test_add_task(self, technician, task):
        technician.add_task(task)
        assert technician.assignable.availability == 5
        assert technician.assignable.tasks == [task]

    def test_add_task_not_enough_availability(self, technician, task):
        task.duration = 10 # Task duration is greater than technician's assignable
        with pytest.raises(ValueError, match='Not enough availability'):
            technician.add_task(task)
        assert technician.assignable.availability == 8  # availability should not change
        assert technician.assignable.tasks == []  # No task should be added

    def test_add_task_already_assigned(self, technician, task):
        technician.add_task(task)
        with pytest.raises(ValueError, match='Task already assigned'):
            technician.add_task(task)
        assert technician.assignable.availability == 5