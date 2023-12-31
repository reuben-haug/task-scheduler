# Path: /scheduler/models/device_model.py

from .base_model import BaseModel

# Device class for handling device data and operations
class Device(BaseModel):
    def __init__(self, id, name, make, model, description, db):
        super().__init__(db)
        self.db = db
        self.id = id
        self.name = name
        self.make = make
        self.model = model
        self.description = description

    # Update the device's data
    def update(self, name, make, model, description):
        self.name = name
        self.make = make
        self.model = model
        self.description = description
        self.db.update_device(self)