# Changelog

All notable changes to this project will be documented in this file.

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