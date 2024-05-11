from sqlalchemy.orm import Session 

from . import models, schema

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_users(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_work_history_by_id(db: Session, work_history_id: int):
    return db.query(models.WorkHistory).filter(models.WorkHistory.id == work_history_id).first()

def get_work_histories(db:Session, skip: int = 0, limit : int = 100):
    return db.query(models.WorkHistory).offset(skip).limit(limit).all()

def create_user(db: Session, user: schema.UserBase):
    db_user = models.User(name=user.name,lastname=user.lastname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_work_history(db:Session, work_history: schema.WorkHistoryBase):
    db_work_history = models.WorkHistory(company_name=work_history.company_name, 
                                         start_date=work_history.start_date,
                                         end_date=work_history.end_date, 
                                         role=work_history.role,
                                         description=work_history.description)
    db.add(db_work_history)
    db.commit()
    db.refresh(db_work_history)
    return db_work_history



def update_user(db: Session, user_id: int, user: schema.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
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
    

def update_work_history(db: Session, work_history_id: int, work_history: schema.WorkHistoryUpdate):
    db_work_history = db.query(models.WorkHistory).filter(models.WorkHistory.id == work_history_id).first()
    if db_work_history is None:
        return None
    if work_history.company_name:
        db_work_history.company_name = work_history.company_name
    if work_history.start_date:
        db_work_history.start_date = work_history.start_date
    if work_history.end_date:
        db_work_history.end_date = work_history.end_date
    if work_history.role:
        db_work_history.role = work_history.role
    if work_history.description:
        db_work_history.description = work_history.description
    db.add(db_work_history)
    db.commit()
    db.refresh(db_work_history)
    return db_work_history