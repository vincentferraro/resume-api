from typing import Optional
from pydantic import BaseModel

class SkillBase(BaseModel):
    name: str
    user_id: int

class Skill(SkillBase):
    id: int

    class Config:
        orm_mode:True

class SkillCreate(BaseModel):
    name:str
    user_id:int

class SkillUpdate(BaseModel):
    name: Optional[str] = None
