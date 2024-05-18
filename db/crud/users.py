from sqlalchemy.orm import Session
from ..models.user import User
from ...schemas import user



def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()


def get_users(db:Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user.UserBase):
    db_user = User(name=user.name,lastname=user.lastname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: user.UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return None
    if user.name:
        db_user.name = user.name
    if user.lastname:
        db_user.lastname = user.lastname
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    