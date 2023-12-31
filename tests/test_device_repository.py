# Path: tests/test_device_repository.py

import pytest
from ..scheduler.repositories.device_repository import DeviceRepository
from ..scheduler.models.device_model import Device

class TestDeviceRepository:
    @pytest.fixture
    def device(self, mocker):
        return mocker.Mock()

    @pytest.fixture
    def device_repository(self, device):
        return DeviceRepository(device)

    def test_insert(self, device_repository, mocker):
        device_repository.insert('Device 1', 'Make 1', 'Model 1', 'Description 1', True)
        device_repository.database.insert_device.assert_called_once_with('Device 1', 'Make 1', 'Model 1', 'Description 1', True)

    def test_get_by_id(self, device_repository, mocker):
        mock_data = [1, 'Device 1', 'Make 1', 'Model 1', 'Description 1', True]
        device_repository.database.fetch_by_id.return_value = mock_data
        device = device_repository.get_by_id(1)
        device_repository.database.fetch_by_id.assert_called_once_with('Devices', 1)
        assert isinstance(device, Device)
        assert list(device.__dict__.values()) == mock_data

    def test_update(self, device_repository, mocker):
        device_repository.update(1, 'Device 2', False)
        device_repository.database.update_technician.assert_called_once_with(1, 'Device 2', False)

    def test_delete(self, device_repository, mocker):
        device_repository.delete(1)
        device_repository.database.delete_technician.assert_called_once_with(1)

    def test_get_by_id_none(self, device_repository, mocker):
        device_repository.database.fetch_by_id.return_value = None
        device = device_repository.get_by_id(1)
        assert device is None