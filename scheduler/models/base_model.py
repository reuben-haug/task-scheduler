# Path: scheduler/models/base_model.py

class BaseModel:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_attribute(self, key):
        return getattr(self, key, None)