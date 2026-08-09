from flask import Blueprint, jsonify, request, g

from extensions import db
from models import Todo
from schemas import TodoCreate, TodoUpdate, TodoPatch
from validation import validate_json

routes = Blueprint('routes', __name__)

@routes.route('todos', methods=['POST'])
@validate_json(TodoCreate)
def create_todo():
    todo = Todo(**g.payload.model_dump())
    db.session.add(todo)
    db.session.commit()
    return {"id": todo.id}, 201

@routes.route('todos/<int:todo_id>', methods=['PUT'])
@validate_json(TodoUpdate)
def update_todo(todo_id: int):
    todo = db.session.get(Todo, todo_id)
    if todo is None:
        return {"error": "Todo not found"}, 404

    for field, value in g.payload.model_dump().items():
        setattr(todo, field, value)

    db.session.commit()
    return {"id": todo.id}, 200


@routes.route('todos', methods=['GET'])
def list_todos():
    return jsonify([]), 200

@routes.route('todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id: int):
    ...

@routes.route('todos/<int:id>', methods=['GET'])
def retrieve_todo(todo_id: int):
    ...
