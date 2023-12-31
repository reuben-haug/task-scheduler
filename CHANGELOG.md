# Changelog

All notable changes to this project will be documented in this file.

## [0.2.5 - 2024-01-01]

### Added

- Generic `get_attribute` method to BaseModel.
- `status` attribute to `Task` model.
- Added unit test for `assignable.py`.
- Created `assignable.py` to abstract adding tasks directly from technicians.
- Models now inherit their name and id from BaseModel.

### Changed

- `test_technician_model` now uses Mock db calls.

## [0.2.4 - 2024-01-01]

### Added

- Added generic `id` attribute to `BaseModel` class.

### Removed

- Calls for `update_technician` in `test_technician_model'`.

### TODO

- Restructure `technician_model` and remove database references.
- Add new unit tests for `technician_model`.

## [0.2.3 - 2023-12-31]

### Added

- Test entries in SOURCES.txt.
- Unit test for TechnicianRepository class.
- Unit test for BaseRepository class.
- Refactor unit tests to use generic methods from BaseRepository.

### Changed

- test_technician_repository.py now uses generic methods from BaseRepository.

### Removed

- Removed the following tests:
    -test_base_model.py
    -test_device_model.py
    -test_device_repository.py
    -test_task_model.py
    -test_task_repository.py
    -test_technician_model.py

## [0.2.2 - 2023-12-31]

### Added

- Generic methods for `get_all`, `get_by_id`, `update`, and `delete` to the `BaseModel` class.
- Unit test for `BaseModel` class.

### Changed
- Moved CRUD methods from BaseModel to BaseRepository.

### Deprecated
-  test_technician_repository.py
-  test_task_repository.py

### TODO
- Refactor unit tests to use generic methods from BaseRepository.

## [0.2.1 - 2023-12-31]

### Added
- DB test fixture for testing `Device` repository methods.
- Added functionality for `Device` to be updated in the database.
- Added test cases for updating `Device` in the database.

### Changed

- get_by_id repository methods return all rows with the given id.

### TODO

- Add generic get_all method to base model class.
- Add generic get_by_id method to base model class.
- Add generic update method to base model class.
- Add generic delete method to base model class.


## [0.2 - 2023-12-31]

### Added
- Added unit tests for the `Device` class and `device_repository.py`.
- Added unit tests for the `Technician` class and `technician_repository.py`.

### Changed
- Refactor main.py to remove all classes and separated them into their own files.  Structure as follows:
    - /scheduler/models
        - base_model.py
        - technician_model.py
        - task_model.py
        - site_model.py
        - device_model.py
    - /scheduler/repositories
        - technician_repository.py
        - task_repository.py
        - site_repository.py
        - device_repository.py
    The base_model.py file contains the base class for all models.  The repositories contain the logic for interacting with the database.

### Deprecated

### Removed

## [0.1 - 2023-12-02]

### Added
- Added unit tests for the `Database` class in `test_database.py`.
- Added unit tests for the `Technician`, `Task`, `Site`, and `schedule_tasks` functions in `test_main.py`.
- Added a `db` fixture in `conftest.py` for setting up and tearing down a test database.
- Added tests for `Technician`, `Task`, and `Site` classes.
- Initial project setup with SQLite database integration.
- `Database` class for handling SQLite operations.
- `Technician`, `Task`, and `Site` classes for handling technician, task, and site data and operations.
- `schedule_tasks` function for scheduling tasks to technicians.

#### Changed
- Updated `Technician`, `Task`, and `Site` classes to fetch data from `test.db` during testing.
- Moved `main.py` and `database.py` into `scheduler` sub-directory.

### Deprecated
- ...

### Removed
- ...

### Fixed
- Fixed import statements in test files.

### Security
- ...