from typing import Optional
from pydantic import BaseModel
from ..schemas.education import Education
from ..schemas.work_history import WorkHistory
from ..schemas.skill import Skill


class UserBase(BaseModel):
    name:str 
    lastname:str 
    location:str = None
    email:str = None
    linkedin:str = None
    website:str = None

class User(UserBase):
    id: int

    works: list[WorkHistory] = []
    educations:list[Education] =[]
    skills: list[Skill] = []
    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    location:Optional[str] = None
    email:Optional[str] = None
    linkedin:Optional[str] = None
    website:Optional[str] = None
    username_id:Optional[int] = None

class UserCreate(UserBase):
    pass

