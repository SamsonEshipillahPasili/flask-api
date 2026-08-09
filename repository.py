from typing import Any, Tuple

from models import Todo
from schemas import TodoCreate, TodoUpdate, TodoPatch
from extensions import db

def _to_dict(todo: Todo) -> dict[str, Any]:
    return {
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'completed': todo.completed
    }


def create_todo(create_schema: TodoCreate) -> dict[str, Any]:
    todo = Todo(create_schema.model_dump())
    db.session.add(todo)
    db.session.commit()
    return _to_dict(todo)


def update_todo(todo_id: int, update_schema: TodoUpdate) -> Tuple[dict[str, Any], int]:
    todo = db.session.get(Todo, todo_id)
    # todo:- raise an Exception, let the exception handler deal with it.
    if todo is None:
        return {"error": "Todo not found"}, 404

    for field, value in g.payload.model_dump().items():
        setattr(todo, field, value)

    db.session.commit()
    return _to_dict(todo), 200

def patch_todo(todo_id: int, update_schema: TodoPatch) -> Tuple[dict[str, Any], int]:
    todo = db.session.get(Todo, todo_id)
    if todo is None:
        return {"error": "Todo not found"}, 404

    for field, value in update_schema.model_dump(exclude_unset=True).items():
        setattr(todo, field, value)

    db.session.commit()
    return _to_dict(todo), 200


def delete_todo(todo_id: int) -> Tuple[dict[str, Any] | None, int]:
    todo = db.session.get(Todo, todo_id)
    if todo is None:
        return {"error": "Todo not found"}, 404

    db.session.delete(todo)
    db.session.commit()
    return None, 204

def list_todos() -> list[dict[str, Any]]:
    ...

def retrieve_todo(todo_id: int) -> dict[str, Any]:
    ...

