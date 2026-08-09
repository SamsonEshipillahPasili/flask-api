from typing import Any

from models import Todo
from schemas import TodoCreate, TodoUpdate, TodoPatch
from extensions import db

def create_todo(create_schema: TodoCreate) -> dict[str, Any]:
    todo = Todo(create_schema.model_dump())
    db.session.add(todo)
    db.session.commit()
    return {
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'completed': todo.completed
    }


def update_todo(update_schema: TodoUpdate):
    ...

def patch_todo(update_schema: TodoPatch):
    ...

def delete_todo(todo_id: int):
    ...

def list_todos() -> list[dict[str, Any]]:
    ...

def retrieve_todo(todo_id: int) -> dict[str, Any]:
    ...

