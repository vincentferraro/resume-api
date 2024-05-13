from typing import Union, Optional, List

from pydantic import BaseModel

class UserBase(BaseModel):
    name:str
    lastname:str

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




class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    works: list[WorkHistory] = []
    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None

class WorkHistoryUpdate(BaseModel):
    company_name: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    role: Optional[str] = None
    description: Optional[str] = None