# /tests/test_technician_model.py

import pytest
from ..scheduler.models.technician_model import Technician

class TestTechnician:
    @pytest.fixture
    def technician(self, mocker):
        db = mocker.Mock()
        return Technician(1, 'John Doe', 8, [], db)

    def test_init(self, technician, mocker):
        assert technician.id == 1
        assert technician.name == 'John Doe'
        assert technician.availability == 8
        assert technician.tasks == []
        assert isinstance(technician.db, mocker.Mock)

    def test_add_task(self, technician, mocker):
        task = mocker.Mock()
        task.duration = 2
        technician.add_task(task)
        assert technician.availability == 6
        assert task in technician.tasks

    def test_add_task_not_enough_availability(self, technician, mocker):
        task = mocker.Mock()
        task.duration = 10
        with pytest.raises(ValueError):
            technician.add_task(task)
        assert technician.availability == 8
        assert task not in technician.tasks