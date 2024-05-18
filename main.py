from typing import Union

from fastapi import FastAPI

from .db import db
from .routes import users, skill,education, work_history




app = FastAPI()

# ROUTES

def main():
    db.Base.metadata.create_all(bind= db.engine)
    app.include_router(users.router)
    app.include_router(skill.router)
    app.include_router(education.router)
    app.include_router(work_history.router)


main()
