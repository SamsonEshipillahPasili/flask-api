from flask import Blueprint, jsonify, g

from extensions import db
from models import Todo
from schemas import TodoCreate, TodoUpdate, TodoPatch
from validation import validate_json
import repository

routes = Blueprint('routes', __name__)

@routes.route('todos', methods=['POST'])
@validate_json(TodoCreate)
def create_todo():
    return repository.create_todo(g.payload), 200

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
    todos = [
        {'id': todo.id, 'title': todo.title, 'description': todo.description, 'completed': todo.completed}
        for todo in
        Todo.query.all()
    ]
    return jsonify(todos), 200

@routes.route('todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id: int):
    todo = db.session.get(Todo, todo_id)
    if todo is None:
        return {"error": "Todo not found"}, 404

    db.session.delete(todo)
    db.session.commit()
    return None, 204

@routes.route('todos/<int:id>', methods=['GET'])
def retrieve_todo(todo_id: int):
    todo = db.session.get(Todo, todo_id)
    if todo is None:
        return {"error": "Todo not found"}, 404

    return {
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'completed': todo.completed
    }, 200
