from typing import List

from pydantic import BaseModel, EmailStr

from schemas.todo_schemas import TodoSchema

class UserBase(BaseModel):
    email: EmailStr

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

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

class UserWithTokenSchema(UserSchema, TokenSchema):
    class Config:
        orm_mode = True
