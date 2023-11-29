from pydantic import BaseModel


class TodoBaseSchema(BaseModel):
    title: str
    description: str
    is_completed: bool
    due_date: str


class TodoSchema(TodoBaseSchema):
    owner_id: int

    class Config:
        orm_mode = True


class TodoResponseSchema(TodoSchema):
    id: int


class TodoUpdateSchema(TodoBaseSchema):
    id: int

