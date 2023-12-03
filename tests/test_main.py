def test_technician(db):
    tech = Technician(1, db)
    assert tech.id == 1
    assert tech.name == 'Technician 1'
    assert tech.availability == 8
    assert tech.tasks == []

def test_task(db):
    task = Task(1, db)
    assert task.id == 1
    assert task.name == 'Task 1'
    assert task.description == 'Task 1 description'
    assert task.duration == 2
    assert task.site.id == 1
    assert task.site.name == 'Site 1'
    assert task.site.address == 'Address 1'
    assert task.site.devices == 10

def test_site(db):
    site = Site(1, db)
    assert site.id == 1
    assert site.name == 'Site 1'
    assert site.address == 'Address 1'
    assert site.devices == 10

def test_schedule_tasks(db):
    technicians = [Technician(i, db) for i in range(1, 4)]
    tasks = [Task(i, db) for i in range(1, 7)]
    schedule_tasks(technicians, tasks, db)
    for tech in technicians:
        assert sum(task.duration for task in tech.tasks) <= 8