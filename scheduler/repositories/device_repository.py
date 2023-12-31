# Path: /scheduler/repositories/device_repository.py

from ..models.device_model import Device

# DeviceRepository class for handling device database operations
class DeviceRepository:
    def __init__(self, database):
        self.database = database

    def insert(self, **kwargs):
        self.database.insert_technician(**kwargs)

    def get_by_id(self, id):
        row = self.database.fetch_by_id('Devices', id)
        if row is None:
            return None
        return Device(*row, self.database)

    def update(self, id, **kwargs):
        self.database.update_technician(id, **kwargs)

    def delete(self, id):
        self.database.delete_technician(id)