from functools import wraps
from flask import request, g
from pydantic import BaseModel

def validate_json(schema: type[BaseModel]):
    """Validates request.json against a Pydantic schema.
    On success, the parsed object is available as `g.payload`.
    On failure, raises ValidationError, caught by the global error handler.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            data = request.get_json(silent=True)
            if data is None:
                data = {}
            g.payload = schema.model_validate(data)
            return fn(*args, **kwargs)
        return wrapper
    return decorator
