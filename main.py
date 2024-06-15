from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from .routes import users, skill,education, work_history, project, username

from .db.db import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ROUTES

@app.get("/")
def welcome_routes():
    return "Hello World"

@app.get("/token/")
def read_token(token: Annotated[str, Depends(oauth2_scheme)]):
    return { "token": token}


app.include_router(users.router)
app.include_router(skill.router)
app.include_router(education.router)
app.include_router(work_history.router)
app.include_router(project.router)
app.include_router(username.router)