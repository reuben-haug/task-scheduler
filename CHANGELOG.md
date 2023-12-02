# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
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