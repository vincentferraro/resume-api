from sqlalchemy.orm import Session 

from . import models, schema

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_work_history_by_company_name(db: Session, company_name: str):
    return db.query(models.WorkHistory).filter(models.WorkHistory.company_name == company_name).first()

def create_user(db: Session, user: schema.UserBase):
    db_user = models.User(name=user.name,lastname=user.lastname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
