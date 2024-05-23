from fastapi import APIRouter, HTTPException, Depends
from ..db.db import get_db
from sqlalchemy.orm import Session
from ..schemas import project
from ..db.crud import projects

router = APIRouter()

@router.get("/projects/", response_model=list[project.Project])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return projects.read_projects(db, skip, limit)

@router.get("/projects/{project_id}", response_model=project.Project)
def read_project_by_id(project_id:int, db: Session = Depends(get_db)):
    project_db = projects.read_project_by_id(db, project_id)
    if project_db is None:
        raise HTTPException(404,"project id "+str(project_id)+" not found")
    return project_db

@router.post("/projects/", response_model=project.Project)
def create_project(create_project: project.ProjectCreate, db: Session = Depends(get_db)):
    project_db = projects.create_project(db, create_project)
    return project_db

@router.put("/projects/{project_id}", response_model= project.Project)
def update_project(project_id:int, project: project.ProjectUpdate , db: Session = Depends(get_db)):
    project_db = projects.update_project(db, project_id, project)
    if project_db is None:
        raise HTTPException(404,"project id "+str(project_id)+" not found")
    return project_db

@router.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project_db = projects.delete_project(db, project_id)
    if project_db is None:
        raise HTTPException(404,"project id "+project_id+" not found")
    return "project id " +str(project_id)+" successfully deleted"
