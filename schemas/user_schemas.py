from typing import List

from pydantic import BaseModel
from pydantic import EmailStr

from schemas.todo_schemas import TodoSchema


class UserBase(BaseModel):
    email: EmailStr


class UserSchema(UserBase):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class UserCreateSchema(UserSchema):
    password: str

    class Config:
        orm_mode = False


class UserFullSchema(UserSchema):
    todos: List[TodoSchema]