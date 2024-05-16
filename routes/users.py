from fastapi import APIRouter, HTTPException, Depends
from .. import schema, crud
# from ..main import get_db
from sqlalchemy.orm import Session

router = APIRouter()


# @router.post("/users/", response_model=schema.User)
# def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_name(db, name=user.name)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Name already registered")
#     return crud.create_user(db= db, user = user)

# @router.get("/users/", response_model= list[schema.User])
# def read_users(skip: int = 0, limit : int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip= skip, limit = limit)
#     return users


# @router.get("/users/{user_id}", response_model=schema.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     user = crud.get_user(db, user_id = user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user