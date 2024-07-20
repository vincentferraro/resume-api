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
    db_user = User(name=user["name"],
                   lastname=user["lastname"],
                   location= user["location"],
                   email= user["email"],
                   linkedin=user["linkedin"],
                   website= user["website"],
                   username_id=user["username_id"]
                    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: user.UserUpdate):
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return None

        user_data = user.model_dump(exclude_unset=True)

        for key, value in user_data.items():
            setattr(db_user, key, value)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except :
        print("Error occured in update_user")

    