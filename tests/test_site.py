import pytest
from scheduler.main import Site
from scheduler.database import Database

def test_site():
    db = Database('tests/test.db')
    site = Site(1, db)
    assert site.id == 1
    assert site.name is not None
    assert site.address is not None
    assert site.devices is not None