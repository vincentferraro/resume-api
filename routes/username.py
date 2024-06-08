from fastapi import APIRouter, HTTPException, Depends
from ..schemas import username
from ..db.crud import usernames
from ..db.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/username", response_model= username.Username)
def read_username(username: str, password: str, db: Session = Depends(get_db)):
    print("here")
    username_db = usernames.read_username(db,username, password)
    if username_db is None: 
        raise HTTPException(404,"username or password incorrect")
    return username_db

