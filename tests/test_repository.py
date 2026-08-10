from app import repository

def test_db_access(app):
    todos = repository.list_todos()
    assert len(todos) == 0

def test_create_todo(app):
    ...
