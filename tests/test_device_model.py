# Path: tests/test_device_model.py

import pytest
from ..scheduler.models.device_model import Device

class TestDevice:
    @pytest.fixture
    def device(self, mocker):
        db = mocker.Mock()
        return Device(1, 'Device 1', 'Make 1', 'Model 1', 'Description 1', db)

    def test_init(self, device, mocker):
        assert device.id == 1
        assert device.name == 'Device 1'
        assert device.make == 'Make 1'
        assert device.model == 'Model 1'
        assert device.description == 'Description 1'
        assert isinstance(device.db, mocker.Mock)

    def test_update(self, device, mocker):
        device.update('Device 2', 'Make 2', 'Model 2', 'Description 2')
        assert device.name == 'Device 2'
        assert device.make == 'Make 2'
        assert device.model == 'Model 2'
        assert device.description == 'Description 2'
        device.db.update_device.assert_called_once_with(device)