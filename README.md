# API Testing for blog app

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
- `python -m pytest tests --cov=src --cov-report html`
- `python src/init_db.py && FLASK_APP=src/app.py python -m flask run`
- `python -m pytest tests -m 'e2e'`

### Creating a Flask API
- `/create-article/` - creates a new article
- `/articles/` - retrieve all articles
- `/article/<article_id>/` - fetch a single article, `article_id` is string type

## Read more here
- https://testdriven.io/blog/modern-tdd/
- https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5