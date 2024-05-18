from typing import  Optional
from pydantic import BaseModel

# Education
class EducationBase(BaseModel):
    title: str
    school:str
    year: str
    user_id:int

class EducationCreate(EducationBase):
    pass 

class EducationUpdate(BaseModel):
    title: Optional[str] = None
    school: Optional[str] = None
    year: Optional[int] = None


class Education(EducationBase):
    id: int
    class Config:
        orm_mode = True

