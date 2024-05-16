from typing import Union

from fastapi import FastAPI , Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import crud, models, schema
from .db import engine, SessionLocal
from .routes import users

models.Base.metadata.create_all(bind= engine)


app = FastAPI()


#Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

# IMPORT ROUTES

app.include_router(users.router)




# ROUTES
        
@app.get("/")
def read_root():
    return { "Hello world "}


@app.get("/work_history/", response_model=list[schema.WorkHistory])
def read_work_histories(skip : int = 0, limit: int = 100, db: Session = Depends(get_db)):
    work_histories = crud.get_work_histories(db,skip, limit)
    return work_histories

@app.get("/work_history/{work_history_id}", response_model=schema.WorkHistory)
async def read_work_history_by_id(work_history_id : int, db: Session = Depends(get_db)):
    work_history = crud.get_work_history_by_id(db,work_history_id)
    if work_history is None:
        raise HTTPException(status_code=404, detail= "Work history not found")
    print(work_history.__str__)
    return work_history

@app.post("/work_history/", response_model=schema.WorkHistory)
def create_work_history(work_history: schema.WorkHistoryCreate, db: Session = Depends(get_db)):
    work_history = crud.create_work_history(db, work_history= work_history)
    return work_history


@app.put("/work_history/{work_history_id}", response_model= schema.WorkHistory)
def update_work_history(work_history_id:int, work_history: schema.WorkHistoryUpdate, db : Session = Depends(get_db)):
    work_history = crud.update_work_history(db, work_history_id=work_history_id, work_history=work_history)
    if work_history is None:
        raise HTTPException(status_code=404, detail="Work history id not found")
    return work_history

@app.put("/users/{user_id}", response_model=schema.User)
def update_user(user_id: int, user: schema.UserUpdate, db : Session = Depends(get_db)):
    user = crud.update_user(db, user_id = user_id, user = user)
    if user is None:
        raise HTTPException(status_code=404, details= "User id not found")
    return user


@app.post("/users/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db= db, user = user)

@app.get("/users/", response_model= list[schema.User])
def read_users(skip: int = 0, limit : int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip= skip, limit = limit)
    return users


@app.get("/users/{user_id}", response_model=schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id = user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/educations/", response_model=list[schema.Education])
def get_educations(skip:int=0, limit: int=100,db: Session=Depends(get_db)):
    educations = crud.read_educations(db,skip,limit)
    return educations

@app.get("/educations/{education_id}", response_model=schema.Education)
def get_education_by_id(education_id:int, db: Session = Depends(get_db)):
    education = crud.read_education_by_id(db, education_id)
    if education is None:
        raise HTTPException(404,"Education id not found")
    return education

@app.post("/educations/",response_model=schema.Education)
def create_education(education:schema.EducationBase,db:Session=Depends(get_db)):
    education = crud.create_education(db, education)
    return education

@app.put("/educations/{education_id}", response_model=schema.Education)
def update_education(education_id:int, education:schema.EducationUpdate, db: Session = Depends(get_db)):
    education = crud.update_education(db, education_id, education)
    if education is None:
        raise HTTPException(404, "Education not found")
    return education

@app.delete("/education/{education_id}")
def delete_education(education_id:int, db:Session = Depends(get_db)):
    education = crud.delete_education(db, education_id)
    if education is None:
        raise HTTPException(404, "education id not found")
    return "education id " +str(education_id)+" successfully deleted"