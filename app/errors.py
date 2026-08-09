from pydantic import ValidationError

class TodoNotFound(Exception):
    """Raised when a todo item is not found"""

    def __init__(self, todo_id: int) -> None:
        self.todo_id = todo_id
        super().__init__(f'Todo with id: {todo_id} not found')


def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return {"errors": e.errors()}, 400

    @app.errorhandler(TodoNotFound)
    def handle_todo_not_found(e: TodoNotFound):
        return {"error": str(e)}, 404
