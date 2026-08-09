# server/errors.py
from pydantic import ValidationError

def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return {"errors": e.errors()}, 400
