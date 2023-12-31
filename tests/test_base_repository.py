# Path: tests/test_base_repository.py

import pytest
from ..scheduler.repositories.base_repository import BaseRepository

class TestBaseRepository:
    @pytest.fixture
    def db(self, mocker):
        return mocker.Mock()

    @pytest.fixture
    def base_repository(self, db):
        return BaseRepository(db)
    
    def test_init(self, base_repository, db):
        assert base_repository.db == db

    def test_fetch_by_id(self, base_repository):
        base_repository.fetch_by_id('table', 1)
        base_repository.db.fetch_by_id.assert_called_once_with('table', 1)

    def test_fetch_all(self, base_repository):
        base_repository.fetch_all('table')
        base_repository.db.fetch_all.assert_called_once_with('table')

    def test_insert(self, base_repository):
        base_repository.insert('table', field1='value1', field2='value2')
        base_repository.db.insert.assert_called_once_with('table', field1='value1', field2='value2')

    def test_update(self, base_repository):
        base_repository.update('table', 1, field1='value1', field2='value2')
        base_repository.db.update.assert_called_once_with('table', 1, field1='value1', field2='value2')

    def test_delete(self, base_repository):
        base_repository.delete('table', 1)
        base_repository.db.delete.assert_called_once_with('table', 1)