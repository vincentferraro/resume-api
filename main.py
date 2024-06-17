from typing import Annotated, Union, List

from fastapi import FastAPI, Depends, Header
from fastapi.security import  HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext

from .routes import users, skill,education, work_history, project, username, token

from .db.db import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


auth_scheme = HTTPBearer()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ROUTES

@app.get("/")
def welcome_routes():
    return "Hello World"

@app.get("/token/")
def read_token(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    print(token)
    return { "token": token }


app.include_router(users.router)
app.include_router(skill.router)
app.include_router(education.router)
app.include_router(work_history.router)
app.include_router(project.router)
app.include_router(username.router)