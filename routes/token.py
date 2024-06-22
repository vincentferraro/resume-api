from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from ..db.db import get_db
from ..db.crud import usernames
from ..utils import token_management

router = APIRouter()


@router.post("/token/refresh")
def refresh_token(token: str, username:str ,db: Session = Depends(get_db)):
    try:
        db_username= usernames.read_username(db,username=username)
        token_refreshed = tokenutils.refresh_token(token,db_username)
        return {
            "message":"token successfully refreshed",
            "access_token":token_refreshed,
            "token_type":"bearer"
            }
        
    except:
        raise Exception("refresh token process has failed")
        
