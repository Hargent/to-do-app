from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from views.todo_views import todo_router
from views.user_views import user_router

from db import init_db


app = FastAPI(openapi_url="/openapi.json")


origins = [
    "http://localhost:3000",
    "localhost:3000",
    "https://to-do-app-cre8gen-interns.netlify.app"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

init_db()

app.router.prefix = "/api"

app.include_router(user_router, prefix="/users")
app.include_router(todo_router, prefix="/todos")