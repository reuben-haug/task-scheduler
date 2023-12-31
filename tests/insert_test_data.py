# tests/insert_test_data.py

from ..scheduler.database import Database

def insert_technician(db: Database):
    db.insert_technician('Test Technician', 8)

def insert_site(db: Database):
    site_id = db.insert_site('Site 1', 'Address 1')
    return site_id

def insert_task(db: Database):
    db.insert_task('Test Task', 2, 'Test Task Description', 1)

def insert_devices(db: Database, site_id):
    db.insert_device('Device 1', site_id, 'site_id')
    db.insert_device('Device 2', site_id, 'site_id')

def insert_test_data(db: Database):
    insert_technician(db)
    site_id = insert_site(db)
    insert_task(db)
    insert_devices(db, site_id)