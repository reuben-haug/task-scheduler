# /scheduler/repositories/technician_repository.py

from ..models.technician_model import Technician

# Technician class for handling technician data and operations
class TechnicianRepository:
    def __init__(self, database):
        self.database = database

    def insert(self, **kwargs):
        self.database.insert_technician(**kwargs)

    def get_by_id(self, id):
        row = self.database.fetch_by_id('Technicians', id)
        if row is None:
            return None
        return Technician(*row, self.database)

    def update(self, id, **kwargs):
        self.database.update_technician(id, **kwargs)

    def delete(self, id):
        self.database.delete_technician(id)