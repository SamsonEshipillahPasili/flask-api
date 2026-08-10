from typing import Any, Tuple

from app.errors import TodoNotFound
from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate, TodoPatch
from app.extensions import db

def _to_dict(todo: Todo) -> dict[str, Any]:
    return {
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'completed': todo.completed
    }

def _get_by_id(todo_id: int) -> Todo:
    todo = db.session.get(Todo, todo_id)
    if todo is None:
        raise TodoNotFound(todo_id)

    return todo

def create_todo(create_schema: TodoCreate) -> dict[str, Any]:
    todo = Todo(**create_schema.model_dump())
    db.session.add(todo)
    db.session.commit()
    return _to_dict(todo)


def update_todo(todo_id: int, update_schema: TodoUpdate) -> dict[str, Any]:
    todo = _get_by_id(todo_id)

    for field, value in update_schema.model_dump().items():
        setattr(todo, field, value)

    db.session.commit()
    return _to_dict(todo)

def patch_todo(todo_id: int, update_schema: TodoPatch) -> dict[str, Any]:
    todo = _get_by_id(todo_id)

    for field, value in update_schema.model_dump(exclude_unset=True).items():
        setattr(todo, field, value)

    db.session.commit()
    return _to_dict(todo)


def delete_todo(todo_id: int) -> None:
    todo = _get_by_id(todo_id)
    db.session.delete(todo)
    db.session.commit()

def list_todos() -> list[dict[str, Any]]:
    return [
        _to_dict(todo)
        for todo in
        Todo.query.all()
    ]

def retrieve_todo(todo_id: int) -> Tuple[dict[str, Any], int]:
    todo = _get_by_id(todo_id)
    return _to_dict(todo), 200


