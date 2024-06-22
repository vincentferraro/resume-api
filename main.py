import uvicorn

from fastapi import FastAPI, Depends, Request, Header
from passlib.context import CryptContext

from .routes import users, skill,education, work_history, project, username, token
from .db.db import Base, engine
from .utils import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ROUTES

@app.get("/")
def welcome_routes(username: str = Header()):
    print(username)
    return "Hello World"

@app.get("/token/")
def read_token(username: str = Depends(auth.token_check)):
    print(username)
    return { "token": username }



app.include_router(users.router)
app.include_router(skill.router)
app.include_router(education.router)
app.include_router(work_history.router)
app.include_router(project.router)
app.include_router(username.router)
app.include_router(token.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0", port="8000")