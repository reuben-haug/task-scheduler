# Path: scheduler/repositories/base_repository.py

class BaseRepository:
    def __init__(self, db):
        self.db = db

    def fetch_by_id(self, table, id):
        return self.db.fetch_by_id(table, id)
    
    def fetch_all(self, table):
        return self.db.fetch_all(table)
    
    def insert(self, table, **kwargs):
        self.db.insert(table, **kwargs)
    
    def update(self, table, id, **kwargs):
        self.db.update(table, id, **kwargs)

    def delete(self, table, id):
        self.db.delete(table, id)