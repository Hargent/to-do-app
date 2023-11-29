from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    title: str
    description: str
    due_date: str
    is_complete: bool
    
# Complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: int
    task: str
    description: str
    due_date: str
    is_complete: bool

    class Config:
        orm_mode = True

#title description date is_complete