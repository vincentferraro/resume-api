from sqlalchemy.orm import Session
from ..db import get_db
from ..models.projects import Project
from ...schemas import project

def read_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Project).offset(skip).limit(limit).all()

def read_project_by_id(db: Session, project_id: int):
    project = db.query(Project).filter(Project.id == project_id).first()
    if project is None:
        return None
    return project

def create_project(db: Session, project: project.ProjectCreate):
    project = Project( 
                    name= project.name,
                    description= project.description,
                    link= project.link,
                    user_id=project.user_id)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def update_project(db: Session, project_id: int, project: project.ProjectUpdate):
    project_db = db.query(Project).filter(Project.id == project_id).first()
    if project_db is None:
        return None
    if project.name:
        project_db.name = project.name
    if project.description:
        project_db.description = project.description
    if project.link:
        project_db.link = project.link

    db.add(project_db)
    db.commit()
    db.refresh(project_db)
    return project_db

def delete_project(db: Session, project_id:int):
    project_db = db.query(Project).filter(Project.id == project_id).first()
    if project_db is None:
        return None
    db.delete(project_db)
    db.commit()
    return True