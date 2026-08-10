from app import repository

def test_db_access(app):
    todos = repository.list_todos()
    assert len(todos) == 0
