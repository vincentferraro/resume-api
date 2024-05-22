from fastapi import APIRouter, HTTPException, Depends
from ..schemas import user
from ..db.crud import users
from ..db.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()




@router.put("/users/{user_id}", response_model=user.User)
def update_user(user_id: int, user: user.UserUpdate, db : Session = Depends(get_db)):
    user = users.update_user(db, user_id = user_id, user = user)
    if user is None:
        raise HTTPException(status_code=404, details= "User id not found")
    return user


@router.post("/users/", response_model=user.User)
def create_user(user: user.UserCreate, db: Session = Depends(get_db)):
    db_user = users.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return users.create_user(db= db, user = user)

@router.get("/users/", response_model= list[user.User])
def read_users(skip: int = 0, limit : int = 100, db: Session = Depends(get_db)):
    users = users.get_users(db, skip= skip, limit = limit)
    return users
    


@router.get("/users/{user_id}", response_model=user.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = users.get_user(db, user_id = user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
