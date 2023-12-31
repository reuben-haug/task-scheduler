# /scheduler/tests/test_technician_repository.py

import pytest
from ..scheduler.repositories.technician_repository import TechnicianRepository
from ..scheduler.models.technician_model import Technician

class TestTechnicianRepository:
    @pytest.fixture
    def db(self, mocker):
        return mocker.Mock()

    @pytest.fixture
    def technician_repository(self, db):
        return TechnicianRepository(db)

    def test_init(self, technician_repository, db):
        assert technician_repository.database == db

    def test_get_by_id(self, technician_repository, db, mocker):
        db.fetch_by_id.return_value = (1, 'John Doe', 8, [])
        technician = technician_repository.get_by_id(1)
        db.fetch_by_id.assert_called_once_with('Technicians', 1)
        assert isinstance(technician, Technician)
        assert technician.id == 1
        assert technician.name == 'John Doe'
        assert technician.availability == 8
        assert technician.tasks == []

    def test_get_by_id_none(self, technician_repository, db):
        db.fetch_by_id.return_value = None
        technician = technician_repository.get_by_id(1)
        db.fetch_by_id.assert_called_once_with('Technicians', 1)
        assert technician is None

    def test_insert(self, technician_repository, db):
        technician_repository.insert('John Doe', 8)
        db.insert_technician.assert_called_once_with('John Doe', 8)