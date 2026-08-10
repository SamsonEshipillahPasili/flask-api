from app import repository
from app.models import Todo


def test_create_todo(app, new_todo_schema):
    # assert no todos in the DB
    assert Todo.query.count() == 0

    # create a new todo
    result = repository.create_todo(new_todo_schema)
    assert result['title'] == new_todo_schema.title
    assert result['description'] == new_todo_schema.description
    assert not result['completed']
    assert isinstance(result['id'], int)

    # assert the todo was created in the db
    todo_db = Todo.query.filter_by(id=result['id']).first()
    assert todo_db is not None
    assert todo_db.title == new_todo_schema.title
    assert todo_db.description == new_todo_schema.description
    assert todo_db.completed == new_todo_schema.completed
