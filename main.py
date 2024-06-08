from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from .routes import users, skill,education, work_history, project, username

from .db.db import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

# TOKEN

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db,username)
    if not user:
        return False
    if not verify_password(password,user.hashed_password):
        return False
    return user

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