from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
from ..db.dependency import get_db
from ..db.crud import work_histories
from ..schemas import work_history

router = APIRouter()

@router.get("/work_history/", response_model=list[work_history.WorkHistory])
def read_work_histories(skip : int = 0, limit: int = 100, db: Session = Depends(get_db)):
    work_histories = work_histories.get_work_histories(db,skip, limit)
    return work_histories

@router.get("/work_history/{work_history_id}", response_model=work_history.WorkHistory)
async def read_work_history_by_id(work_history_id : int, db: Session = Depends(get_db)):
    work_history = work_histories.get_work_history_by_id(db,work_history_id)
    if work_history is None:
        raise HTTPException(status_code=404, detail= "Work history not found")
    print(work_history.__str__)
    return work_history

@router.post("/work_history/", response_model=work_history.WorkHistory)
def create_work_history(work_history: work_history.WorkHistoryCreate, db: Session = Depends(get_db)):
    work_history = work_histories.create_work_history(db, work_history= work_history)
    return work_history


@router.put("/work_history/{work_history_id}", response_model= work_history.WorkHistory)
def update_work_history(work_history_id:int, work_history: work_history.WorkHistoryUpdate, db : Session = Depends(get_db)):
    work_history = work_histories.update_work_history(db, work_history_id=work_history_id, work_history=work_history)
    if work_history is None:
        raise HTTPException(status_code=404, detail="Work history id not found")
    return work_history
