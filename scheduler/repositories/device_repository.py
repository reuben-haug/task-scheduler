# Path: /scheduler/repositories/device_repository.py

from ..models.device_model import Device

# Device class for handling device data and operations
class DeviceRepository:
    def __init__(self, database):
        self.database = database

    def insert(self, name, availability):
        self.database.insert_technician(name, availability)

    def get_by_id(self, id):
        row = self.database.fetch_by_id('Devices', id)
        if row is None:
            return None
        return Device(row[0], row[1], row[2], [], self.database)

    def update(self, id, name, availability):
        self.database.update_technician(id, name, availability)

    def delete(self, id):
        self.database.delete_technician(id)