# /scheduler/repositories/technician_repository.py

from ..models.technician_model import Technician
from .base_repository import BaseRepository

# TechnicianRepository holds all the database access logic for the Technician model
class TechnicianRepository(BaseRepository):
    # Access the database from BaseRepository
    def __init__(self):
        super().__init__(self.db)

