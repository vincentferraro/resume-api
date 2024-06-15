from sqlalchemy.orm import Session
from ..models.username import Username
from ...schemas import username


def read_username(db: Session, username: str):
    username_db = db.query(Username).filter(Username.username == username).first()
    if username is None:
        return False
    return username_db

def create_username(db:Session, username: str, password:str):
    db_username = Username(username=username, password=password)
    db.add(db_username)
    db.commit()
    db.refresh(db_username)
    return db_username

def update_username(db:Session, username_id : int, username: username.UsernameUpdate):
    db_username = db.query(Username).filter(Username.id == username_id).first()
    if db_username is None: 
        return None
    if username.username :
        db_username.username = username.username
    if username.password :
        db_username.password = username.password

def delete_user(db:Session, username_id: int):
    db_username = db.query(Username).filter(Username.id == username_id).first()
    if db_username is None: 
        return None
    db.delete(db_username)
    db.commit()
    return True