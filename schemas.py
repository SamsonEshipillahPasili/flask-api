from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str
    completed: bool = False

class TodoUpdate(BaseModel):
    title: str
    description: str
    completed: bool = False

# class TodoPatch(BaseModel):
#     title: str | None = None
#     description: str | None = None
#     completed: bool | None = None
