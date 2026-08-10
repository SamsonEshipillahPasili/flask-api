from faker import Faker

from app import repository
from app.extensions import db
from app.models import Todo

fake = Faker()

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

def test_list_todos():
    # assert no todos in the database
    assert Todo.query.count() == 0

    # an empty db must return an empty list.
    result = repository.list_todos()
    assert len(result) == 0

    # Add a Todo
    db_todo = Todo(
        title=fake.sentence(),
        description=fake.paragraph(),
        completed=True
    )
    db.session.add(db_todo)
    db.session.commit()

    # assert the listed todo matches the one added directly to the db
    result = repository.list_todos()
    assert len(result) == 1
    assert result[0]['id'] == db_todo.id
    assert result[0]['title'] == db_todo.title
    assert result[0]['description'] == db_todo.description
    assert result[0]['completed'] == db_todo.completed
