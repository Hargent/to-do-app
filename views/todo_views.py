from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

import crud.todo_crud as todo_crud
from crud.user_crud import get_current_user
from db import get_db
from models.usermodel import UserModel
from schemas.todo_schemas import TodoSchema, TodoBaseSchema, TodoResponseSchema

todo_router = APIRouter()


@todo_router.get('', response_model=List[TodoResponseSchema], summary="get todos for current user")
def get_my_todos_view(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    """
    Returns a list of all todos for the currently logged in user
    """
    todos = todo_crud.get_user_todos(db, current_user)
    return todos

@todo_router.get('/{todo_id}', response_model=TodoResponseSchema, summary="Get a todo by ID")
def get_todo_by_id_view(
        todo_id: int,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user),
):
    """
    Get a todo by its ID.
    """
    todo = todo_crud.get_todo_by_id(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    return todo


@todo_router.post('', response_model=List[TodoResponseSchema], summary="create todo")
def add_todo_view(
        todo_data: TodoBaseSchema,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user),
):
    """
    Create a new Todo with the following information:

    - **title**: 
    - **description**: 
    - **is_completed**: A boolean
    - **due_date**: due_date
    
    """
    todo_crud.add_todo(
        db,
        current_user,
        todo_data,
    )
    todos = todo_crud.get_user_todos(db, current_user)
    return todos


@todo_router.put('{todo_id}', response_model=TodoResponseSchema, summary="Update a todo by ID")
def update_todo_view(
        todo_id: int,
        todo_data: TodoBaseSchema,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user),
):
    """
    Update existing Todo with the following information:

    - **title**
    - **description**
    - **is_completed**
    - **due_date**

    
    """
    existing_todo = todo_crud.get_todo_by_id(db, todo_id)
    if existing_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # Update todo fields
    updated_todo = todo_crud.update_todo(db, current_user, todo_data)
    

    return updated_todo


@todo_router.delete('/{todo_id:int}', response_model=List[TodoResponseSchema], summary="delete a todo item")
def delete_todo_view(
        todo_id: int,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user)
):
    """
    Delete a todo itemp
    """
    todo_crud.delete_todo(db, todo_id)
    todos = todo_crud.get_user_todos(db, current_user)
    return todos