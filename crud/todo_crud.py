from typing import List

from sqlalchemy.orm import Session

from models.todomodel import TodoModel
from models.usermodel import UserModel
from schemas.todo_schemas import TodoSchema, TodoUpdateSchema


def add_todo(
        db: Session,
        current_user: UserModel,
        todo_data: TodoSchema,
):
    todo: TodoModel = TodoModel(
        title=todo_data.title,
        description=todo_data.description,
        is_completed=todo_data.is_completed,
        due_date=todo_data.due_date
    )
    todo.owner = current_user
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update_todo(
        db: Session,
        new_todo: TodoUpdateSchema,
):
    todo: TodoModel = db.query(TodoModel).filter(
        TodoModel.id == new_todo.id,
    ).first()
    todo.title = new_todo.title
    todo.description = new_todo.description
    todo.is_completed = new_todo.is_completed
    todo.due_date = new_todo.due_date
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(
        db: Session,
        todo_id: int,
):
    todo: TodoModel = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    db.delete(todo)
    db.commit()


def get_user_todos(
        db: Session,
        current_user: UserModel,
) -> List[TodoModel]:
    todos = db.query(TodoModel).filter(TodoModel.owner == current_user).all()
    return todos