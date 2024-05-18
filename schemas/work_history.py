from typing import Optional
from pydantic import BaseModel


class WorkHistoryBase(BaseModel):
    company_name:str
    start_date: str
    end_date: str
    role: str
    description: str
    user_id: int

class WorkHistoryCreate(BaseModel):
    company_name:str
    start_date: str
    end_date: str
    role: str
    description: str
    user_id: int

class WorkHistory(WorkHistoryBase):
    id: int

    class Config:
        orm_mode = True



class WorkHistoryUpdate(BaseModel):
    company_name: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    role: Optional[str] = None
    description: Optional[str] = None

