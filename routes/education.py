from fastapi import APIRouter, HTTPException, Depends
from ..schemas import education
from ..db.crud import educations
from ..db.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/educations/", response_model=list[education.Education])
def get_educations(skip:int=0, limit: int=100,db: Session=Depends(get_db)):
    educations = educations.read_educations(db,skip,limit)
    return educations

@router.get("/educations/{education_id}", response_model=education.Education)
def get_education_by_id(education_id:int, db: Session = Depends(get_db)):
    education = educations.read_education_by_id(db, education_id)
    if education is None:
        raise HTTPException(404,"Education id not found")
    return education

@router.post("/educations/",response_model=education.Education)
def create_education(education:education.EducationBase,db:Session=Depends(get_db)):
    education = educations.create_education(db, education)
    return education

@router.put("/educations/{education_id}", response_model=education.Education)
def update_education(education_id:int, education:education.EducationUpdate, db: Session = Depends(get_db)):
    education = educations.update_education(db, education_id, education)
    if education is None:
        raise HTTPException(404, "Education not found")
    return education

@router.delete("/education/{education_id}")
def delete_education(education_id:int, db:Session = Depends(get_db)):
    education = educations.delete_education(db, education_id)
    if education is None:
        raise HTTPException(404, "education id not found")
    return "education id " +str(education_id)+" successfully deleted"

