from typing import Union

from fastapi import FastAPI

from .routes import users, skill,education, work_history, project

from .db.db import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

# ROUTES

@app.get("/")
def welcome_routes():
    return "Hello World"

app.include_router(users.router)
app.include_router(skill.router)
app.include_router(education.router)
app.include_router(work_history.router)
app.include_router(project.router)
