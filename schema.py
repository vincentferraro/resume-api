from typing import Union, Optional

from pydantic import BaseModel

class WorkHistoryBase(BaseModel):
    company_name:str
    start_date: str
    end_date: str
    role: str
    description: str

class WorkHistoryCreate(WorkHistoryBase):
    pass

class WorkHistory(WorkHistoryBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name:str
    lastname:str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int


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