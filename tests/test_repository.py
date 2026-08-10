import pytest
from faker import Faker

from app import repository
from app.errors import TodoNotFound
from app.extensions import db
from app.models import Todo
from app.schemas import TodoUpdate

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

def test_list_todos_when_db_empty():
    # assert no todos in the database
    assert Todo.query.count() == 0

    # an empty db must return an empty list.
    result = repository.list_todos()
    assert len(result) == 0

def test_list_todos(todo):
    # assert the listed todo matches the one added directly to the db
    result = repository.list_todos()
    assert len(result) == 1
    assert result[0]['id'] == todo.id
    assert result[0]['title'] == todo.title
    assert result[0]['description'] == todo.description
    assert result[0]['completed'] == todo.completed

def test_retrieve_todo_not_found():
    # assert no todos in the database
    assert Todo.query.count() == 0

    with pytest.raises(TodoNotFound):
        repository.retrieve_todo(1)

def test_retrieve_todo(todo):
    api_todo = repository.retrieve_todo(todo.id)
    assert api_todo['title'] == todo.title
    assert api_todo['description'] == todo.description
    assert api_todo['completed'] == todo.completed

def test_delete_todo_not_found():
    # assert no todos in the database
    assert Todo.query.count() == 0

    with pytest.raises(TodoNotFound):
        repository.delete_todo(1)


def test_delete_todo(todo):
    assert Todo.query.count() == 1
    assert Todo.query.filter_by(id=todo.id).first() is not None

    repository.delete_todo(todo.id)
    assert Todo.query.count() == 0

def test_update_todo_not_found(todo):

    update = TodoUpdate(
        title=fake.sentence(),
        description=fake.sentence(),
        completed=fake.boolean(),
    )

    api_todo = repository.update_todo(todo.id, update)

    # assert the result matches the update
    assert api_todo['title'] == update.title
    assert api_todo['description'] == update.description
    assert api_todo['completed'] == update.completed

    # assert the todo was updated in the database.
    db_todo = Todo.query.filter_by(id=api_todo['id']).first()
    assert db_todo is not None
    assert db_todo.title == update.title
    assert db_todo.description == update.description
    assert db_todo.completed == update.completed
