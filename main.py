from typing import Union

from fastapi import FastAPI , Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import crud, models, schema
from .db import engine, SessionLocal


models.Base.metadata.create_all(bind= engine)


app = FastAPI()


#Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer:Union[bool,None]= None


@app.post("/users/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db= db, user = user)

@app.get("/users/", response_model= list[schema.User])
def read_users(skip: int = 0, limit : int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip= skip, limit = limit)
    return users


@app.get("/users/{user_id}", response_model=schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id = user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/")
def read_root():
    return { "Hello world "}
