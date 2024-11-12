from fastapi import FastAPI

from app.routers import category
from routers import task, user

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# Подключаем маршруты из category
app.include_router(category.router)

