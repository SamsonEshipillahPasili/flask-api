from flask import Blueprint, g

from app.schemas import TodoCreate, TodoUpdate, TodoPatch
from app.validation import validate_json
from app import repository

routes = Blueprint('routes', __name__)

@routes.route('todos', methods=['POST'])
@validate_json(TodoCreate)
def create_todo():
    return repository.create_todo(g.payload), 201

@routes.route('todos/<int:todo_id>', methods=['PUT'])
@validate_json(TodoUpdate)
def update_todo(todo_id: int):
    return repository.update_todo(todo_id, g.payload), 200

@routes.route('todos/<int:todo_id>', methods=['PUT'])
@validate_json(TodoPatch)
def patch_todo(todo_id: int):
    return repository.patch_todo(todo_id, g.payload), 200


@routes.route('todos', methods=['GET'])
def list_todos():
    return repository.list_todos(), 200

@routes.route('todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id: int):
    repository.delete_todo(todo_id)
    return '', 204

@routes.route('todos/<int:id>', methods=['GET'])
def retrieve_todo(todo_id: int):
    return repository.retrieve_todo(todo_id), 200
