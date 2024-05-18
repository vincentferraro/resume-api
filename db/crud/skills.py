from sqlalchemy.orm import Session
from ..models.skill import Skill
from ...schemas import skill



# Skills

def read_skills(db: Session, skip: int = 0, limit: int = 100):
    skills = db.query(Skill).offset(skip).limit(limit).all()
    return skills

def read_skill_by_id(db:Session, skill_id:int):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if skill is None:
        return None
    return skill

def create_skill(db: Session, skill: skill.SkillCreate):
    db_skill = Skill(name=skill.name,
                            user_id= skill.user_id)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def update_skill(db:Session, skill_id: int, skill: skill.SkillUpdate):
    db_skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if db_skill is None:
        return None
    if skill.name:
        db_skill.name = skill.name
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def delete_skill(db: Session, skill_id: int):
    db_skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if db_skill is None:
        return None
    db.delete(db_skill)
    db.commit()
    return True