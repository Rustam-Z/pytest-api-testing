# Test-Driven Development with Blog App in Python

### Libraries used:
- `pytest` - unit, integration, E2E testing
- `pydantic` - runtime data validation (similar to @dataclass)
- `Flask` - RESTful API interface
- `sqlite3` - database

### Objectives:
- Configure pytest and set up a project structure for testing
- Define database models with pydantic
- Use pytest fixtures for managing test state and performing side effects
- Verify JSON responses against JSON Schema definitions
- Organize database operations with commands (modify state, has side effects) and queries (read-only, no side effects)
- Write unit, integration, and end-to-end tests with pytest


### Our app will have the following requirements:
- Articles can be created
- Articles can be fetched
- Articles can be listed


### How to run?
- `python -m pytest -v --tb=no tests/`

## Read more here
- https://testdriven.io/blog/modern-tdd/
- https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5