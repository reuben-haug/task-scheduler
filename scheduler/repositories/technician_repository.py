# /scheduler/repositories/technician_repository.py

from ..models.technician_model import Technician

# Technician class for handling technician data and operations
class TechnicianRepository:
    def __init__(self, database):
        self.database = database

    def insert(self, name, availability):
        self.database.insert_technician(name, availability)

    def get_by_id(self, id):
        row = self.database.fetch_by_id('Technicians', id)
        if row is None:
            return None
        return Technician(row[0], row[1], row[2], [], self.database)

    def update(self, id, name, availability):
        self.database.update_technician(id, name, availability)

    def delete(self, id):
        self.database.delete_technician(id)