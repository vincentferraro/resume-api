from sqlalchemy.orm import Session
from ..models.username import Username
from ...schemas.username import UsernameBase


def read_username(db: Session, username: str, plain_password: str):
    print(username, plain_password)
    username = db.query(Username).filter(Username.username.like(username)).first()
    if username is None:
        return False
    print(username)
    return username