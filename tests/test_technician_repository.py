# /tests/test_technician_repository.py

import pytest
from ..scheduler.repositories.technician_repository import TechnicianRepository
from ..scheduler.models.technician_model import Technician
from ..scheduler.repositories.base_repository import BaseRepository

class TestTechnicianRepository(BaseRepository):
    @pytest.fixture
    def db(self, mocker):
        return mocker.Mock()

    @pytest.fixture
    def technician_repository(self, db):
        return TechnicianRepository(db)

    def test_init(self, technician_repository, db):
        assert technician_repository.db == db

    # Add more tests here for other methods in TechnicianRepository
    # For example, if you have a method to get all technicians:
    # def test_get_all_technicians(self, technician_repository, db):
    #     db.fetch_all.return_value = [(1, 'John Doe', 8, [])]
    #     technicians = technician_repository.get_all_technicians()
    #     db.fetch_all.assert_called_once_with('Technicians')
    #     assert len(technicians) == 1
    #     assert isinstance(technicians[0], Technician)
    #     assert technicians[0].id == 1
    #     assert technicians[0].name == 'John Doe'
    #     assert technicians[0].availability == 8
    #     assert technicians[0].tasks == []