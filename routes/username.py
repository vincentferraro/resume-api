from fastapi import APIRouter, HTTPException, Depends
from ..schemas import username
from ..db.crud import usernames
from ..db.db import get_db
from sqlalchemy.orm import Session
from ..utils import password as genpwd
from ..utils import token_management

router = APIRouter()

@router.get("/login")
def  read_username(username: str, password: str, db: Session = Depends(get_db)):
    username_db =  usernames.read_username(db,username)
    if username_db is None or not genpwd.check_password(password,username_db.password):
        raise HTTPException(404,"username or password incorrect")
    
    return {"access_token":token_management.create_token(username_db.username),"token_type":"bearer"}


@router.post("/register")
def create_username(username: str, password: str, db: Session = Depends(get_db)):
    pwd = genpwd.hash_password(password)
    usernames.create_username(db,username, pwd)
    return {"message":"username registered successfully"}
