from sqlalchemy.orm import Session
from ..models.work_history import WorkHistory
from ...schemas import work_history



def get_work_history_by_id(db: Session, work_history_id: int):
    return db.query(WorkHistory).filter(WorkHistory.id == work_history_id).first()

def get_work_histories(db:Session, skip: int = 0, limit : int = 100):
    return db.query(WorkHistory).offset(skip).limit(limit).all()


def create_work_history(db:Session, work_history: work_history.WorkHistoryCreate):
    db_work_history = WorkHistory(company_name=work_history.company_name, 
                                         start_date=work_history.start_date,
                                         end_date=work_history.end_date, 
                                         role=work_history.role,
                                         description=work_history.description,
                                         user_id=work_history.user_id)
    db.add(db_work_history)
    db.commit()
    db.refresh(db_work_history)
    return db_work_history



def update_work_history(db: Session, work_history_id: int, work_history: work_history.WorkHistoryUpdate):
    db_work_history = db.query(WorkHistory).filter(WorkHistory.id == work_history_id).first()
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
