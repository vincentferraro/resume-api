from sqlalchemy.orm import Session
from ..models.education import Education
from ...schemas import education

def read_educations(db: Session, skip: int = 0, limit:int = 100):
    return db.query(Education).offset(skip).limit(limit).all()
    
def read_education_by_id(db:Session, education_id:int):
    education = db.query(Education).filter(Education.id == education_id).first()
    if education is None:
        return None
    return education

def create_education(db:Session,education:education.EducationBase):
    db_education = Education(title=education.title,
                                    school=education.school,
                                    year=education.year,
                                    user_id=education.user_id)
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education

def update_education(db:Session, education_id:int, education: education.EducationUpdate):
    db_education = db.query(Education).filter(Education.id == education_id).first()
    if db_education is None:
        return None
    if education.title:
        db_education.title = education.title
    if education.school:
        db_education.school = education.school
    if education.year:
        db_education.year = education.year
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education

def delete_education(db:Session, education_id: int):
    db_education = db.query(Education).filter(Education.id == education_id).first()
    if db_education is None:
        return None
    db.delete(db_education)
    db.commit()
    # db.refresh(db) ? Need verification
    return True
