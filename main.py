from fastapi import FastAPI

from views.todo_views import todo_router
from views.user_views import user_router


app = FastAPI(openapi_url="/openapi.json")

app.router.prefix = "/api"

app.include_router(user_router, prefix="/users")
app.include_router(todo_router, prefix="/todos")