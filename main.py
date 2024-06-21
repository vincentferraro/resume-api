from typing import Annotated, Union, List

from fastapi import FastAPI, Depends, Request, Header
from fastapi.security import  HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext

from .routes import users, skill,education, work_history, project, username, token

from .db.db import Base, engine

from .utils import token as token_utils

Base.metadata.create_all(bind=engine)

app = FastAPI()


auth_scheme = HTTPBearer()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_token(bearer: HTTPAuthorizationCredentials= Depends(auth_scheme)):
    print(bearer.credentials)
    return bearer


#Middleware

@app.middleware("http")
async def verify_token(request: Request, call_next):
    token = request.headers.get("Authorization")
    username = request.headers.get("username")
    url = str(request.url)
    print(token)
    print(username)
    if token:
        if token_utils.verify_valid_token(token,username) is False:
            return "token invalid"
    else:
        print("not find")
    
    response = await call_next(request)
    return response


# ROUTES

@app.get("/")
def welcome_routes(username: str = Header()):
    print(username)
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
app.include_router(token.router)