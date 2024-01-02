#PATH: /scheduler/tests/test_assignable.py

import pytest
from ..scheduler.models.assignable import Assignable
from ..scheduler.models.task_model import Task

class TestAssignable:
    @pytest.fixture
    def assignable(self):
        return Assignable(8, [])

    @pytest.fixture
    def task(self):
        return Task(1, 'Task 1', 3, 'Test Description 1', status='Pending')

    def test_init(self, assignable):
        assert assignable.availability == 8
        assert assignable.tasks == []

    def test_add_task(self, assignable, task):
        assignable.add_task(task)
        assert assignable.availability == 5
        assert assignable.tasks == [task]

    def test_add_task_not_enough_availability(self, assignable, task):
        task.duration = 10  # Task duration is greater than assignable's availability
        with pytest.raises(ValueError, match='Not enough availability'):
            assignable.add_task(task)
        assert assignable.availability == 8  # Availability should not change
        assert assignable.tasks == []  # No task should be added

    def test_add_task_already_assigned(self, assignable, task):
        assignable.add_task(task)
        with pytest.raises(ValueError, match='Task already assigned'):
            assignable.add_task(task)
        assert assignable.availability == 5  # Availability should not change
        assert assignable.tasks == [task]  # No additional task should be added