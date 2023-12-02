import pytest
from scheduler.main import Technician
from scheduler.database import Database

def test_technician():
    db = Database('tests/test.db')
    technician = Technician(1, db)
    assert technician.id == 1
    assert technician.name is not None
    assert technician.availability is not None
    assert technician.tasks == []