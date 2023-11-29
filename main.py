from fastapi import FastAPI, status, HTTPException, Depends

from sqlalchemy.orm import Session

from database import Base, engine, sessionLocal
import models
import schemas 

# Create the database
Base.metadata.create_all(engine)

# Helper function to get database session
def get_session():
    session = sessionLocal()
    try: 
        yield session
    finally:
        session.close()

# Initialize the app
app = FastAPI()

@app.get("/")
def root():
    return "todooo"

@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoCreate, session: Session = Depends(get_session)):

    # Create an instance of the ToDo database model
    tododb = models.ToDo(task=todo.task)

    # Add it to the session and commit it
    session.add(tododb)
    session.commit()
    session.refresh(tododb)


    # Return the id
    return tododb


@app.get("/todo/{id}", response_model=schemas.ToDo)
def read_todo(id: int, session: Session = Depends(get_session)):

    # Get todo item with given id
    todo = session.query(models.ToDo).get(id)

    # if item with id does not exist raise an exception
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")


    return todo

@app.put("/todo/{id}")
def update_todo(id: int, task: str, session: Session = Depends(get_session)):


    # Get todo item with given id
    todo = session.query(models.ToDo).get(id)

    # Update todo item if found
    if todo:
        todo.task = task
        session.commit()

    # If item with id does not exist, raise a 404
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo 

@app.delete("/todo/{id}")
def delete_todo(id: int, session: Session = Depends(get_session)):


    # Get todo item with given id
    todo = session.query(models.ToDo).get(id)

    # Delete todo item if found
    if todo:
        session.delete(todo)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return None
    

@app.get("/todo", response_model=list[schemas.ToDo])
def read_todo_list(session: Session = Depends(get_session)):


    # Get list of todos
    todo_list = session.query(models.ToDo).all()

    return todo_list
    
