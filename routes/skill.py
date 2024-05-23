
from fastapi import APIRouter, HTTPException, Depends
from ..db.db import get_db
from sqlalchemy.orm import Session
from ..schemas import skill
from ..db.crud import skills

router = APIRouter()


@router.get("/skills/", response_model=list[skill.Skill])
def read_skills(skip: int=0, limit: int = 100, db: Session = Depends(get_db)):
    skill_list = skills.read_skills(db, skip, limit)
    return skill_list

@router.get("/skills/{skill_id}", response_model=skill.Skill)
def read_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = skills.read_skill_by_id(db, skill_id)
    if skill is None:
        raise HTTPException(404, "skill id not found")
    return skill

@router.post("/skills/", response_model= skill.Skill)
def create_skill(skill: skill.SkillCreate, db: Session = Depends(get_db)):
    skill = skills.create_skill(db, skill)
    return skill

@router.put("/skills/{skill_id}",response_model=skill.Skill)
def update_skill(skill_id: int, skill: skill.SkillUpdate, db: Session = Depends(get_db)):
    skill = skills.update_skill(db, skill_id, skill)
    if skill is None:
        raise HTTPException(404, 'skill id not found')
    return skill

@router.delete("/skills/{skill_id}", response_model= str)
def delete_skill(skill_id: int, db : Session = Depends(get_db)):
    skill = skills.delete_skill(db,skill_id)
    if skill is None:
        raise HTTPException(404," skill id not found")
    return "skill id " +str(skill_id)+" successfully deleted"
