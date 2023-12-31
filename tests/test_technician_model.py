# /tests/test_technician_model.py

import pytest
from unittest.mock import Mock
from ..scheduler.models.technician_model import Technician
from ..scheduler.models.task_model import Task  # Assuming you have a Task model

class TestTechnician:
    @pytest.fixture
    def db(self):
        return Mock()

    @pytest.fixture
    def technician(self, db):
        return Technician(1, 'John Doe', 8, [], db)

    def test_init(self, technician, db):
        assert technician.id == 1
        assert technician.name == 'John Doe'
        assert technician.availability == 8
        assert technician.tasks == []
        assert technician.db == db

    def test_add_task(self, technician):
        task = Task(1, 'Task 1', 3)  # Assuming Task takes id, name, and duration
        technician.add_task(task)
        assert technician.availability == 5
        assert technician.tasks == [task]
        technician.db.update_technician.assert_called_once_with(technician)

    def test_add_task_not_enough_availability(self, technician):
        task = Task(1, 'Task 1', 10)  # Task duration is greater than technician's availability
        with pytest.raises(ValueError, match='Not enough availability'):
            technician.add_task(task)
        assert technician.availability == 8  # Availability should not change
        assert technician.tasks == []  # No task should be added
        technician.db.update_technician.assert_not_called()  # update_technician should not be called