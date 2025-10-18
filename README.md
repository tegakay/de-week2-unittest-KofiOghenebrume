# de-week2-unittest-KofiOghenebrume

Short overview
- This repository contains a small project and its unit tests using `pytest`.
- Implementation lives in [main/artificial_pancreas.py](main/artificial_pancreas.py).
- Tests and test helpers are in the [tests](tests) folder:
  - Main test file: [tests/test_artificial_pancreas.py](tests/test_artificial_pancreas.py)
  - Test fixtures / shared setup: [tests/conftest.py](tests/conftest.py)

Setup
1. Create a virtual environment (recommended):
   - python -m venv .venv
   - On Windows: .venv\Scripts\activate
   - On macOS / Linux: source .venv/bin/activate


Run tests
- Run the full test suite:
  - pytest -q
- Run a single test file:
  - pytest [tests/test_artificial_pancreas.py](tests/test_artificial_pancreas.py) -q
- Run a single test by node id:
  - pytest [tests/test_artificial_pancreas.py](tests/test_artificial_pancreas.py)::test_name -q

VS Code
- Use the Testing sidebar to discover and run tests.
- The integrated terminal and the Python Test Log will show pytest output.

What the tests cover
- Tests validate the behavior implemented in [main/artificial_pancreas.py](main/artificial_pancreas.py).
- Shared fixtures in [tests/conftest.py](tests/conftest.py) provide setup for test scenarios.

Files
- [main/artificial_pancreas.py](main/artificial_pancreas.py)
- [main/__init__.py](main/__init__.py)
- [tests/test_artificial_pancreas.py](tests/test_artificial_pancreas.py)
- [tests/conftest.py](tests/conftest.py)
- [tests/__init__.py](tests/__init__.py)
- [requirements.txt](requirements.txt)
- [.gitignore](.gitignore)

